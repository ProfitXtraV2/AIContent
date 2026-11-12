// The social boards and post files, read and written exactly as the Python side does it
// (scripts/social/mdtable.py, pack.py, links.py, settings.py), so a change made from the dashboard
// gives the same bytes the checks and the publishing check expect. Pure functions: the pages use
// them in the browser, the tests run them in node.
(function (root) {
  // --- markdown tables (mdtable.py) ---------------------------------------------------------
  const cells = line => line.trim().replace(/^\|+/, '').replace(/\|+$/, '').split('|').map(c => c.trim());
  const isSep = cs => cs.some(c => c) && cs.every(c => !c || /^[-: ]+$/.test(c));
  // like Python's str.splitlines(): no empty last item for a text that ends with a newline
  function lines(text) {
    const out = String(text || '').split(/\r\n|\n|\r/);
    if (out.length && out[out.length - 1] === '') out.pop();
    return out;
  }

  function tables(md) {
    const ls = lines(md);
    const out = [];
    let i = 0;
    while (i < ls.length) {
      if (ls[i].trim().startsWith('|') && i + 1 < ls.length && ls[i + 1].trim().startsWith('|') && isSep(cells(ls[i + 1]))) {
        const header = cells(ls[i]).map(c => c.toLowerCase());
        let j = i + 2;
        const rows = [];
        while (j < ls.length && ls[j].trim().startsWith('|')) {
          const cs = cells(ls[j]);
          const row = {};
          header.forEach((h, k) => { row[h] = cs[k] || ''; });
          rows.push(row);
          j++;
        }
        out.push({ header, rows, start: i, end: j });
        i = j;
      } else i++;
    }
    return out;
  }

  function find(md, ...columns) {
    const want = columns.map(c => c.toLowerCase());
    return tables(md).find(t => want.every(c => t.header.includes(c))) || null;
  }

  const clean = v => String(v == null ? '' : v).replace(/\s+/g, ' ').replace(/\|/g, '/').trim();
  const renderRow = (header, row) => '| ' + header.map(h => clean(row[h])).join(' | ') + ' |';
  function render(header, rows) {
    return ['| ' + header.join(' | ') + ' |', '|' + header.map(() => '---').join('|') + '|',
            ...rows.map(r => renderRow(header, r))].join('\n');
  }

  function replace(md, table, rows) {
    const ls = lines(md);
    const out = [...ls.slice(0, table.start), ...render(table.header, rows).split('\n'), ...ls.slice(table.end)];
    return out.join('\n') + (/\n$/.test(md) ? '\n' : '');
  }

  const splitList = v => String(v || '').split(',').map(s => s.trim()).filter(Boolean);

  // a table written before some columns existed: the missing ones go in at their place in `columns`
  function withColumns(table, columns) {
    const header = [...table.header];
    columns.forEach((c, i) => {
      if (header.includes(c)) return;
      const before = columns.slice(0, i).reverse().find(p => header.includes(p));
      header.splice(before ? header.indexOf(before) + 1 : 0, 0, c);
    });
    return { ...table, header };
  }
  const REQUEST_COLS = ['id', 'kind', 'target', 'angle', 'format', 'slides', 'sources', 'target_page', 'accounts',
                        'earliest', 'status', 'reason', 'pack_id', 'added'];
  const ACCOUNT_COLS = ['account_id', 'network', 'postiz_channel_id', 'active', 'posts_per_article', 'followup_delay_days',
                        'format', 'slides', 'max_hashtags', 'link', 'slots', 'max_per_day', 'emoji', 'tone_override',
                        'test_post_seen', 'profile_link_set'];

  // --- post files (pack.py) -------------------------------------------------------------------
  const HEADINGS = { 'post text': 'text', 'hashtags': 'hashtags', 'image text': 'image_text', 'alt text': 'alt_text',
                     'english reference (for review only)': 'english' };
  const ORDER = ['Post text', 'Hashtags', 'Image text', 'Alt text', 'English reference (for review only)'];

  function parsePost(text) {
    const found = { text: [], hashtags: [], image_text: [], alt_text: [], english: [] };
    let current = null;
    for (const line of lines(text)) {
      const m = /^##\s+(.+?)\s*$/.exec(line);
      if (m) { current = HEADINGS[m[1].trim().toLowerCase()] || null; continue; }
      if (line.startsWith('# ') && current === null) continue;
      if (current) found[current].push(line);
    }
    const joined = {};
    for (const k of Object.keys(found)) joined[k] = found[k].join('\n').trim();
    return {
      text: joined.text,
      hashtags: joined.hashtags.split(/[\s,]+/).filter(Boolean).map(h => h.startsWith('#') ? h : '#' + h),
      image_text: lines(joined.image_text).map(l => l.trim()).filter(Boolean),
      alt_text: joined.alt_text, english: joined.english,
    };
  }

  function renderPost(postId, f) {
    const values = { 'Post text': f.text || '', 'Hashtags': (f.hashtags || []).join(' '),
                     'Image text': (f.image_text || []).join('\n'), 'Alt text': f.alt_text || '',
                     'English reference (for review only)': f.english || '' };
    const parts = [`# ${postId}`, ''];
    for (const h of ORDER) parts.push(`## ${h}`, values[h].trim(), '');
    return parts.join('\n').replace(/\s+$/, '') + '\n';
  }

  function publishText(f) {
    const text = (f.text || '').trim();
    const tags = (f.hashtags || []).join(' ');
    return text + (tags ? '\n\n' + tags : '');
  }

  // --- links (links.py, checks.expected_address) ------------------------------------------------
  const UTM = { facebook: 'facebook', instagram: 'instagram', x: 'x', 'linkedin-page': 'linkedin', 'linkedin-profile': 'linkedin' };
  function tagged(url, network, campaign, content) {
    const q = new URLSearchParams({ utm_source: UTM[network] || network, utm_medium: 'social',
                                    utm_campaign: campaign || '', utm_content: content || '' });
    return url + (url.includes('?') ? '&' : '?') + q.toString();
  }

  function expectedAddress(meta, post, brand) {
    const src = (meta && meta.source) || {};
    const link = (post && post.link) || {};
    if (link.target) return link.target;
    const slug = String(src.slug || '');
    if (src.kind === 'intro' || slug.startsWith('hub-intro-'))
      return `${brand.site}/blog/${slug.replace('hub-intro-', '')}/`;
    if (slug) return (brand.address_pattern || `${brand.site}/blog/{slug}/`).replace('{slug}', slug);
    return null;
  }

  // --- settings (settings.py) -----------------------------------------------------------------------
  const DAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];
  function slotDays(spec) {
    if (['daily', 'everyday', 'every-day'].includes(spec)) return [0, 1, 2, 3, 4, 5, 6];
    const out = new Set();
    for (const piece of spec.split(',')) {
      if (piece.includes('-')) {
        const [a, b] = piece.split('-', 2);
        if (!DAYS.includes(a) || !DAYS.includes(b)) throw new Error(`unknown days "${piece}" (use mon … sun, or daily)`);
        let i = DAYS.indexOf(a);
        const j = DAYS.indexOf(b);
        for (;;) { out.add(i); if (i === j) break; i = (i + 1) % 7; }
      } else if (DAYS.includes(piece)) out.add(DAYS.indexOf(piece));
      else throw new Error(`unknown day "${piece}" (use mon … sun, or daily)`);
    }
    return [...out].sort((x, y) => x - y);
  }

  // 'daily 12:30, 19:30; sat 11:00' → [{days, times}]; throws a plain message when it cannot read it
  function parseSlots(text) {
    const rules = [];
    for (const part of String(text || '').split(';').map(p => p.trim()).filter(Boolean)) {
      const m = /^([a-z,\- ]+?)\s+(\d.*)$/.exec(part.toLowerCase());
      if (!m) throw new Error(`cannot read the slot rule "${part}" (write e.g. "daily 12:30, 19:30")`);
      const days = slotDays(m[1].replace(/ /g, ''));
      const times = [];
      for (const t of m[2].split(',').map(x => x.trim()).filter(Boolean)) {
        const tm = /^(\d{1,2}):(\d{2})$/.exec(t);
        if (!tm || +tm[1] > 23 || +tm[2] > 59) throw new Error(`slot "${t}" is outside 00:00–23:59`);
        times.push(`${String(+tm[1]).padStart(2, '0')}:${tm[2]}`);
      }
      if (!times.length) throw new Error(`the slot rule "${part}" has no time`);
      rules.push({ days, times: [...new Set(times)].sort() });
    }
    if (!rules.length) throw new Error('no posting slots');
    return rules;
  }

  // {brand: {key: value}, accounts: [{…}], brandTable, accountTable} from settings.md
  function parseSettings(md) {
    const bt = find(md, 'key', 'value');
    const at = find(md, 'account_id', 'network');
    const brand = {};
    for (const r of (bt ? bt.rows : [])) if (r.key) brand[r.key.trim().toLowerCase()] = (r.value || '').trim();
    return { brand, accounts: at ? at.rows.filter(r => r.account_id) : [], brandTable: bt, accountTable: at };
  }

  // settings.md with brand values and account fields changed; rows keep their order and columns
  function updateSettings(md, brandChanges, accountChanges) {
    let out = md;
    let bt = find(out, 'key', 'value');
    if (bt && brandChanges && Object.keys(brandChanges).length) {
      const rows = bt.rows.map(r => ({ ...r }));
      for (const [key, value] of Object.entries(brandChanges)) {
        const row = rows.find(r => (r.key || '').trim().toLowerCase() === key);
        if (row) row.value = value; else rows.push({ key, value });
      }
      out = replace(out, bt, rows);
    }
    const at = find(out, 'account_id', 'network');
    if (at && accountChanges && Object.keys(accountChanges).length) {
      const rows = at.rows.map(r => ({ ...r, ...(accountChanges[r.account_id] || {}) }));
      const keys = Object.values(accountChanges).flatMap(Object.keys);
      out = replace(out, withColumns(at, ACCOUNT_COLS.filter(c => at.header.includes(c) || keys.includes(c))), rows);
    }
    return out;
  }

  // --- requests.md (board.py) -----------------------------------------------------------------------
  function parseRequests(md) {
    const rt = find(md, 'kind', 'target');
    const ct = find(md, 'command', 'post_id');
    return { requests: rt ? rt.rows.filter(r => r.target || r.id) : [],
             commands: ct ? ct.rows.filter(r => r.command || r.post_id) : [] };
  }

  // a new request row (id, status and the rest are filled by the workflows and the runs); an older
  // table gains the format, slides and sources columns
  function addRequest(md, req, today) {
    const rt = find(md, 'kind', 'target');
    if (!rt) throw new Error('requests.md has no Requests table');
    const row = { id: '', kind: req.kind, target: req.target, angle: req.angle || '', format: req.format || '',
                  slides: req.slides || '', sources: (req.sources || []).join(', '), target_page: req.target_page || '',
                  accounts: (req.accounts || []).join(', '), earliest: req.earliest || '', status: '', reason: '',
                  pack_id: '', added: today || '' };
    return replace(md, withColumns(rt, REQUEST_COLS), [...rt.rows, row]);
  }

  // a text source pasted into a request: its file under <Brand>/social/sources/ ({path, text})
  function sourceFile(target, text, stamp) {
    const slug = String(target || 'source').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, '-')
      .replace(/^-+|-+$/g, '').slice(0, 40) || 'source';
    return { path: `sources/${stamp}-${slug}.md`, text: `# Source for: ${clean(target)}\n\n${String(text).trim()}\n` };
  }

  // one or more command rows ({command, post_id, date?, note?}) at the end of the Commands table
  function addCommand(md, cmd) {
    const cmds = Array.isArray(cmd) ? cmd : [cmd];
    const ct = find(md, 'command', 'post_id');
    if (!ct) throw new Error('requests.md has no Commands table');
    if (cmds.length > 1) {
      let out = md;
      for (const c of cmds) out = addCommand(out, c);
      return out;
    }
    cmd = cmds[0];
    if (!['fix', 'cancel', 'not before', 'post now', 'post at'].includes(cmd.command)) throw new Error(`unknown command ${cmd.command}`);
    if (cmd.command === 'not before' && !/^\d{4}-\d{2}-\d{2}$/.test(cmd.date || '')) throw new Error('not before needs a date (YYYY-MM-DD)');
    if (cmd.command === 'post at' && !/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$/.test(cmd.date || '')) throw new Error('post at needs a day and a time (YYYY-MM-DD HH:MM)');
    const row = { id: '', command: cmd.command, post_id: cmd.post_id, date: cmd.date || '', status: '', note: cmd.note || '' };
    return replace(md, ct, [...ct.rows, row]);
  }

  // --- length as the networks count it (postnumbers.py) -------------------------------------------
  const LINK = '[[LINK]]';
  const weight = cp => (cp <= 0x10FF || (cp >= 0x2000 && cp <= 0x200D) || (cp >= 0x2010 && cp <= 0x201F) ||
                        (cp >= 0x2032 && cp <= 0x2037)) ? 1 : 2;
  const emojiBase = cp => (cp >= 0x1F000 && cp <= 0x1FAFF) || (cp >= 0x2600 && cp <= 0x27BF) ||
                          (cp >= 0x2B00 && cp <= 0x2BFF) || (cp >= 0x1F1E6 && cp <= 0x1F1FF);
  function xLength(text, linkLength = 23) {
    let t = String(text || '').normalize('NFC');
    const linkRe = /\[\[LINK\]\]|https?:\/\/\S+/g;
    let n = (t.match(linkRe) || []).length * linkLength;
    t = t.replace(linkRe, '');
    const cps = [...t].map(c => c.codePointAt(0));
    let i = 0;
    while (i < cps.length) {
      const cp = cps[i];
      if (emojiBase(cp)) {
        n += 2; i++;
        while (i < cps.length && ([0xFE0F, 0xFE0E].includes(cps[i]) || (cps[i] >= 0x1F3FB && cps[i] <= 0x1F3FF) ||
               (cp >= 0x1F1E6 && cp <= 0x1F1FF && cps[i] >= 0x1F1E6 && cps[i] <= 0x1F1FF))) i++;
        while (i + 1 < cps.length && cps[i] === 0x200D && emojiBase(cps[i + 1])) {
          i += 2;
          while (i < cps.length && ([0xFE0F, 0xFE0E].includes(cps[i]) || (cps[i] >= 0x1F3FB && cps[i] <= 0x1F3FF))) i++;
        }
        continue;
      }
      if (cp === 0xFE0F || cp === 0xFE0E) { i++; continue; }
      n += weight(cp); i++;
    }
    return n;
  }
  // characters as the network counts them; the placeholder counts as the tagged link it becomes
  function length(text, network, linkLength) {
    if (network === 'x') return xLength(text);
    const t = String(text || '');
    const links = t.split(LINK).length - 1;
    return [...t.split(LINK).join('')].length + links * (linkLength != null ? linkLength : 120);
  }

  const api = { tables, find, render, replace, clean, splitList, withColumns, parsePost, renderPost, publishText, tagged,
                 expectedAddress, parseSlots, parseSettings, updateSettings, parseRequests, addRequest, addCommand,
                 sourceFile, length, LINK };
  root.SocialMd = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
