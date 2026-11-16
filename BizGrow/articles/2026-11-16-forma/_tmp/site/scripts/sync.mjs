/**
 * Rebuild the Bulgarian consultation form from docs/forma-bezplatna-konsultacia.md.
 * Run from site/: npm run sync:form
 *
 * English copy stays in src/content/consultation-form.en.ts, keyed by the ids
 * this script prints. Add a translation when a new id appears.
 */
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = process.env.FORM_ROOT;
const sourcePath = resolve(root, "docs/forma-bezplatna-konsultacia.md");
const outPath = resolve(root, "site/src/content/consultation-form.bg.ts");

const text = readFileSync(sourcePath, "utf8");
const lines = text.split(/\r?\n/);

let title = "";
const sections = [];
let current = null;
let note = "";
let consent = "";
let submit = "";
let seenHeading = false;

for (const raw of lines) {
  const line = raw.trim();
  if (line.startsWith("## Попълнен пример")) break;
  if (line.startsWith("# ")) {
    title = line.slice(2).trim();
    seenHeading = true;
    continue;
  }
  if (!seenHeading) continue;

  const heading = line.match(/^## \d+\.\s*(.*)$/);
  if (heading) {
    current = { title: heading[1].trim(), help: [], items: [], after: [] };
    sections.push(current);
    continue;
  }
  if (line.startsWith("Съгласие:")) {
    consent = unwrap(line.slice("Съгласие:".length).trim());
    current = null;
    continue;
  }
  if (line.startsWith("Под бутона:")) {
    note = unwrap(line.slice("Под бутона:".length).trim());
    current = null;
    continue;
  }
  if (line.startsWith("Бутон:")) {
    submit = line
      .slice("Бутон:".length)
      .replace(/\*\*/g, "")
      .trim();
    current = null;
    continue;
  }
  if (!line || !current) continue;
  if (line.startsWith("- ")) {
    current.items.push(line.slice(2).trim());
  } else if (current.items.length === 0) {
    current.help.push(line);
  } else {
    current.after.push(line);
  }
}

if (!title || !submit || sections.length === 0) {
  console.error("The consultation template is missing a title, sections, or a submit button.");
  process.exit(1);
}

const form = {
  title,
  intro: "",
  note,
  consent,
  submit,
  sections: sections.map((section, index) => buildSection(section, index + 1)),
};

const file = `// Generated from docs/forma-bezplatna-konsultacia.md by npm run sync:form.
// Do not edit. Change the Markdown template, then run the command again.
import type { ConsultationForm } from "./consultation-form";

export const consultationFormBg: ConsultationForm = ${JSON.stringify(form, null, 2)};
`;

writeFileSync(outPath, file);
console.log(`Wrote ${sections.length} sections to site/src/content/consultation-form.bg.ts`);
console.log("Ids that need an English string in consultation-form.en.ts:");
for (const id of collectIds(form)) console.log(`  ${id}`);

function buildSection(section, number) {
  const id = `s${number}`;
  const help = [...section.help, ...section.after.filter((line) => !line.includes("[текстово поле]"))].join(" ");
  const fields = [];
  const checks = [];
  const kind = choiceKind(section.title, help);

  for (const item of section.items) {
    const boxes = item.match(/^\[ \]\s+(.+)$/);
    if (boxes) {
      checks.push(parseChoice(boxes[1], `${id}.o${checks.length + 1}`));
      continue;
    }
    if (checks.length) {
      fields.push(choiceField(id, kind, checks.splice(0)));
    }
    const inline = item.match(/^(.+?):\s*((?:\[ \]\s*.+)+)$/);
    if (inline && inline[2].includes("[ ]")) {
      const options = [...inline[2].matchAll(/\[ \]\s*([^[]+)/g)].map((match, optionIndex) => ({
        id: `${id}.f${fields.length + 1}.o${optionIndex + 1}`,
        label: match[1].trim(),
      }));
      fields.push({ id: `${id}.f${fields.length + 1}`, kind: "radio", label: inline[1].trim(), options });
      continue;
    }
    const input = item.match(/^(.+?):\s*\[(.+)\]$/);
    if (input) {
      fields.push(parseInput(`${id}.f${fields.length + 1}`, input[1].trim(), input[2].trim()));
      continue;
    }
    throw new Error(`Unrecognised form line in section ${number}: ${item}`);
  }
  if (checks.length) fields.push(choiceField(id, kind, checks));

  for (const line of section.after) {
    const input = line.match(/^(.+?):\s*\[(.+)\]$/);
    if (!input) continue;
    fields.push({ ...parseInput(`${id}.extra`, input[1].trim(), input[2].trim()), optional: true });
  }

  const built = { id, title: section.title, fields };
  if (help) built.help = help;
  return built;
}

function choiceField(id, kind, options) {
  const field = { id, kind: kind.kind, options };
  if (kind.max) field.max = kind.max;
  return field;
}

function parseChoice(label, id) {
  const other = label.match(/^(.+?):\s*\[текстово поле\]$/);
  if (other) return { id, label: other[1].trim(), detail: { id: `${id}.detail`, label: other[1].trim() } };
  return { id, label };
}

function parseInput(id, label, bracket) {
  const placeholderMatch = bracket.match(/напр\.\s*(.+)$/);
  const kind = bracket.startsWith("имейл")
    ? "email"
    : bracket.startsWith("телефон")
      ? "tel"
      : bracket.startsWith("URL")
        ? "url"
        : "text";
  const field = { id, kind, label };
  if (placeholderMatch) field.placeholder = placeholderMatch[1].trim();
  if (kind === "email" || /име и фамилия/i.test(label)) field.required = true;
  return field;
}

function choiceKind(title, help) {
  const max = help.match(/до\s+(\d+)/);
  if (max) return { kind: "check", max: Number(max[1]) };
  if (/^Кои(\s|$)/.test(title)) return { kind: "check" };
  return { kind: "radio" };
}

function unwrap(value) {
  return value.replace(/^[„"]/, "").replace(/[“"]$/, "");
}

function collectIds(value, ids = []) {
  if (Array.isArray(value)) {
    for (const item of value) collectIds(item, ids);
    return ids;
  }
  if (value && typeof value === "object") {
    if (typeof value.id === "string" && Array.isArray(value.fields) && value.title) ids.push(value.id);
    if (typeof value.id === "string" && typeof value.label === "string") ids.push(value.id);
    if (typeof value.id === "string" && typeof value.placeholder === "string") ids.push(`${value.id}.placeholder`);
    if (typeof value.title === "string" && value.sections) ids.push("title", "intro", "note", "submit");
    if (typeof value.help === "string" && typeof value.id === "string") ids.push(`${value.id}.help`);
    for (const item of Object.values(value)) collectIds(item, ids);
  }
  return [...new Set(ids)];
}
