// How a social post will look on its network: Instagram, Facebook, X or LinkedIn. A close
// likeness of each feed (the network renders the final post itself). Used by the dashboard's
// review panel and by scripts/social/preview.py's offline page. Post text is only ever set as
// text, never as HTML.
//
//   SocialPreview.slot(post) → <section> with the label, the mockup and the review notes
//   post: {post_id, network, account_id, handle, name, format, text, images: [url], image_text: [..],
//          alt, hashtags: [..], link, link_note, length, limit}
const SocialPreview = (() => {
  // where each feed folds a caption: characters, and the line break it stops at (null: none)
  const FOLD = { instagram: [125, 1], facebook: [480, 4], x: [280, null], 'linkedin-page': [210, 2], 'linkedin-profile': [210, 2] };
  const NET = { instagram: 'Instagram', facebook: 'Facebook', x: 'X', 'linkedin-page': 'LinkedIn Page', 'linkedin-profile': 'LinkedIn profile' };
  const ICON = {
    heart: 'M12 20.5s-7.5-4.6-7.5-10.4A4.3 4.3 0 0 1 12 7.4a4.3 4.3 0 0 1 7.5 2.7c0 5.8-7.5 10.4-7.5 10.4z',
    comment: 'M20.5 11.6a8.4 8.4 0 0 1-12.4 7.4L3.5 20.5l1.6-4.4a8.4 8.4 0 1 1 15.4-4.5z',
    send: 'M21.5 3.5 10.2 13.1M21.5 3.5l-6.6 17-4.7-7.4-7.2-4.4z',
    save: 'M18.5 20.5 12 15.6l-6.5 4.9V4.5a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1z',
    dots: 'M5 12h.01M12 12h.01M19 12h.01',
    like: 'M7.5 10.5v10h-4v-10zm2 10h8.6a2 2 0 0 0 2-1.6l1.3-6.4a2 2 0 0 0-2-2.4h-5.4l.9-4.2a1.7 1.7 0 0 0-1.7-2.1l-3.7 6.2',
    share: 'M14 5.5 20.5 12 14 18.5M20.5 12H10a6.5 6.5 0 0 0-6.5 6.5',
    repost: 'M4 9.5V8a3 3 0 0 1 3-3h11.5M15.5 2l3 3-3 3M20 14.5V16a3 3 0 0 1-3 3H5.5M8.5 22l-3-3 3-3',
    views: 'M5 20V12M10 20V6M15 20v-9M20 20V9',
    globe: 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9s1-6.5 3.5-9z',
  };
  const CSS = `
  .pv-slot { width: 470px; max-width: 100%; }
  .pv-label { font-size: 12px; color: #6b7280; margin: 0 0 8px; letter-spacing: .02em; }
  .pv-label b { color: #14161a; }
  .pv-notes { font-size: 12px; color: #6b7280; margin-top: 10px; background: #fff; border: 1px dashed #dbdfe6;
              border-radius: 8px; padding: 8px 10px; }
  .pv-notes div + div { margin-top: 4px; }
  .pv-over { color: #b42318; font-weight: 600; }
  .pv-card { background: #fff; border: 1px solid #dbdfe6; border-radius: 10px; overflow: hidden; color: #14161a;
             font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; text-align: left; }
  .pv-row { display: flex; align-items: center; gap: 10px; }
  .pv-avatar { width: 34px; height: 34px; border-radius: 50%; display: grid; place-items: center; flex: none;
               background: #0f7b5a; color: #fff; font-weight: 700; font-size: 13px; }
  .pv-ring { padding: 2px; border-radius: 50%; background: linear-gradient(45deg, #f9ce34, #ee2a7b, #6228d7); }
  .pv-ring .pv-avatar { border: 2px solid #fff; }
  .pv-name { font-weight: 600; }
  .pv-sub { color: #6b7280; font-size: 12px; }
  .pv-icons { display: flex; gap: 16px; align-items: center; }
  svg.pv-i { width: 24px; height: 24px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
  .pv-media { position: relative; background: #000; }
  .pv-media img { display: block; width: 100%; height: auto; }
  .pv-slides { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
  .pv-slides::-webkit-scrollbar { display: none; }
  .pv-slides img { flex: none; width: 100%; scroll-snap-align: center; }
  .pv-count { position: absolute; top: 10px; right: 10px; background: rgba(0,0,0,.6); color: #fff; font-size: 12px; padding: 2px 8px; border-radius: 12px; }
  .pv-dots { display: flex; justify-content: center; gap: 4px; }
  .pv-dots span { width: 6px; height: 6px; border-radius: 50%; background: #c7ccd4; }
  .pv-dots span.on { background: #0095f6; }
  .pv-caption { white-space: pre-wrap; word-wrap: break-word; }
  .pv-more { color: #6b7280; cursor: pointer; background: none; border: 0; padding: 0; font: inherit; }
  .pv-ig .pv-top { padding: 10px 12px; justify-content: space-between; }
  .pv-ig .pv-acts { padding: 8px 12px 4px; justify-content: space-between; }
  .pv-ig .pv-body { padding: 0 12px 14px; }
  .pv-ig a { color: #00376b; text-decoration: none; }
  .pv-fb .pv-top { padding: 12px 14px 8px; }
  .pv-fb .pv-body { padding: 0 14px 12px; }
  .pv-fb a { color: #0064d1; text-decoration: none; }
  .pv-fb .pv-bar, .pv-li .pv-bar { display: flex; justify-content: space-around; border-top: 1px solid #dbdfe6; padding: 6px 0;
                                   color: #65676b; font-weight: 600; font-size: 13px; }
  .pv-fb .pv-bar { margin: 0 14px; } .pv-li .pv-bar { margin: 0 16px; }
  .pv-bar span { display: flex; align-items: center; gap: 6px; }
  .pv-fb .pv-avatar, .pv-x .pv-avatar { width: 40px; height: 40px; }
  .pv-x { padding: 12px 16px; display: flex; gap: 10px; }
  .pv-x a { color: #1d9bf0; text-decoration: none; }
  .pv-x .pv-media { border-radius: 16px; overflow: hidden; border: 1px solid #dbdfe6; margin-top: 10px; }
  .pv-x .pv-acts { display: flex; justify-content: space-between; color: #536471; margin-top: 10px; max-width: 420px; }
  .pv-x svg.pv-i { width: 19px; height: 19px; }
  .pv-li .pv-top { padding: 12px 16px 8px; }
  .pv-li .pv-avatar { width: 48px; height: 48px; border-radius: 6px; }
  .pv-li .pv-body { padding: 0 16px 10px; }
  .pv-li a { color: #0a66c2; text-decoration: none; font-weight: 600; }
  .pv-doc { position: absolute; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,.65); color: #fff; font-size: 12px; padding: 6px 10px; }`;

  let styled = false;
  function injectCss() {
    if (styled || typeof document === 'undefined') return;
    const st = document.createElement('style');
    st.textContent = CSS;
    document.head.appendChild(st);
    styled = true;
  }

  function svg(name) {
    const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('class', 'pv-i');
    const p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    p.setAttribute('d', ICON[name]); s.appendChild(p);
    return s;
  }
  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  // links and hashtags as link-coloured text; everything else stays plain text
  function richText(parent, text, xShort) {
    const re = /(https?:\/\/[^\s]+)|(#[\p{L}\p{N}_]+)/gu;
    let last = 0, m;
    while ((m = re.exec(text))) {
      if (m.index > last) parent.appendChild(document.createTextNode(text.slice(last, m.index)));
      const a = el('a', '', m[0]);
      if (m[1]) {
        a.href = m[1]; a.target = '_blank'; a.rel = 'noopener';
        if (xShort) { const shown = m[1].replace(/^https?:\/\//, ''); a.textContent = shown.length > 26 ? shown.slice(0, 25) + '…' : shown; }
      } else { a.href = '#'; a.addEventListener('click', ev => ev.preventDefault()); }
      parent.appendChild(a);
      last = m.index + m[0].length;
    }
    if (last < text.length) parent.appendChild(document.createTextNode(text.slice(last)));
  }
  function foldAt(text, fold, breaks) {
    let at = text.length > fold ? text.slice(0, fold).replace(/\s+\S*$/, '').length : -1;
    if (breaks != null) {
      let n = 0;
      for (let i = 0; i < text.length; i++) {
        if (text[i] === '\n' && ++n === breaks) { if (at < 0 || i < at) at = i; break; }
      }
    }
    return at >= 0 && at < text.trimEnd().length ? at : -1;
  }
  function caption(p, label, prefix, xShort) {
    const [fold, breaks] = FOLD[p.network] || [300, null];
    const box = el('div', 'pv-caption');
    const at = foldAt(p.text, fold, breaks);
    const draw = (open) => {
      box.textContent = '';
      if (prefix) { box.appendChild(el('span', 'pv-name', prefix)); box.appendChild(document.createTextNode(' ')); }
      const cut = !open && at >= 0;
      richText(box, cut ? p.text.slice(0, at).trimEnd() : p.text, xShort);
      if (cut) {
        box.appendChild(document.createTextNode('… '));
        const b = el('button', 'pv-more', label); b.type = 'button'; b.onclick = () => draw(true); box.appendChild(b);
      }
    };
    draw(false);
    return box;
  }
  function avatar(p, ring) {
    const a = el('div', 'pv-avatar', (p.handle || p.name || '?').replace(/[^\p{L}\p{N}]/gu, '').slice(0, 2).toUpperCase());
    if (!ring) return a;
    const r = el('div', 'pv-ring'); r.appendChild(a); return r;
  }
  function media(p, opts) {
    const box = el('div', 'pv-media');
    const images = p.images || [];
    if (!images.length) { box.appendChild(el('div', 'pv-count', 'no image')); box.style.minHeight = '120px'; return box; }
    if (images.length === 1) { const img = el('img'); img.src = images[0]; img.alt = p.alt || ''; box.appendChild(img); return box; }
    const strip = el('div', 'pv-slides');
    images.forEach((src, i) => { const img = el('img'); img.src = src; img.alt = (p.image_text || [])[i] || p.alt || ''; strip.appendChild(img); });
    box.appendChild(strip);
    const count = el('div', 'pv-count', `1/${images.length}`);
    box.appendChild(count);
    strip.addEventListener('scroll', () => {
      const i = Math.round(strip.scrollLeft / strip.clientWidth);
      count.textContent = `${i + 1}/${images.length}`;
      if (opts && opts.dots) opts.dots.querySelectorAll('span').forEach((d, j) => d.classList.toggle('on', i === j));
      if (opts && opts.doc) opts.doc.textContent = `${(p.image_text || [])[0] || 'Carousel'} · ${i + 1} / ${images.length}`;
    });
    return box;
  }
  function bar(items) {
    const b = el('div', 'pv-bar');
    items.forEach(([i, t]) => { const s = el('span'); s.appendChild(svg(i)); s.appendChild(document.createTextNode(t)); b.appendChild(s); });
    return b;
  }
  function instagram(p) {
    const c = el('article', 'pv-card pv-ig');
    const top = el('div', 'pv-row pv-top'); const who = el('div', 'pv-row');
    who.appendChild(avatar(p, true)); who.appendChild(el('span', 'pv-name', p.handle));
    top.appendChild(who); top.appendChild(svg('dots')); c.appendChild(top);
    const dots = (p.images || []).length > 1 ? el('div', 'pv-dots') : null;
    if (dots) p.images.forEach((_, i) => dots.appendChild(el('span', i === 0 ? 'on' : '')));
    c.appendChild(media(p, { dots }));
    const acts = el('div', 'pv-row pv-acts'); const left = el('div', 'pv-icons');
    ['heart', 'comment', 'send'].forEach(n => left.appendChild(svg(n)));
    acts.appendChild(left); if (dots) acts.appendChild(dots); acts.appendChild(svg('save')); c.appendChild(acts);
    const body = el('div', 'pv-body'); body.appendChild(caption(p, 'още', p.handle));
    body.appendChild(el('div', 'pv-sub', 'Насрочен')); c.appendChild(body);
    return c;
  }
  function facebook(p) {
    const c = el('article', 'pv-card pv-fb');
    const top = el('div', 'pv-row pv-top'); top.appendChild(avatar(p));
    const who = el('div'); who.appendChild(el('div', 'pv-name', p.name));
    const sub = el('div', 'pv-sub pv-row'); sub.appendChild(document.createTextNode('Насрочен · '));
    const g = svg('globe'); g.style.width = g.style.height = '12px'; sub.appendChild(g);
    who.appendChild(sub); top.appendChild(who); c.appendChild(top);
    const body = el('div', 'pv-body'); body.appendChild(caption(p, 'Вижте още')); c.appendChild(body);
    c.appendChild(media(p));
    c.appendChild(bar([['like', 'Харесва ми'], ['comment', 'Коментар'], ['share', 'Споделяне']]));
    return c;
  }
  function xpost(p) {
    const c = el('article', 'pv-card pv-x'); c.appendChild(avatar(p));
    const main = el('div'); main.style.flex = '1';
    const who = el('div', 'pv-row'); who.appendChild(el('span', 'pv-name', p.name)); who.appendChild(el('span', 'pv-sub', '@' + p.handle + ' · сега'));
    main.appendChild(who); main.appendChild(caption(p, 'Покажи още', null, true));
    main.appendChild(media(p));
    const acts = el('div', 'pv-acts'); ['comment', 'repost', 'heart', 'views', 'save'].forEach(n => acts.appendChild(svg(n)));
    main.appendChild(acts); c.appendChild(main);
    return c;
  }
  function linkedin(p) {
    const c = el('article', 'pv-card pv-li');
    const top = el('div', 'pv-row pv-top'); top.appendChild(avatar(p));
    const who = el('div'); who.appendChild(el('div', 'pv-name', p.name)); who.appendChild(el('div', 'pv-sub', 'Последователи · Насрочен'));
    top.appendChild(who); c.appendChild(top);
    const body = el('div', 'pv-body'); body.appendChild(caption(p, 'вижте повече')); c.appendChild(body);
    const doc = (p.images || []).length > 1 ? el('div', 'pv-doc', `${(p.image_text || [])[0] || 'Carousel'} · 1 / ${p.images.length}`) : null;
    const m = media(p, { doc }); if (doc) m.appendChild(doc); c.appendChild(m);
    c.appendChild(bar([['like', 'Харесва ми'], ['comment', 'Коментар'], ['repost', 'Репост'], ['send', 'Изпращане']]));
    return c;
  }
  const RENDER = { instagram, facebook, x: xpost, 'linkedin-page': linkedin, 'linkedin-profile': linkedin };

  function card(p) { injectCss(); return (RENDER[p.network] || facebook)(p); }

  function slot(p) {
    injectCss();
    const s = el('section', 'pv-slot');
    const label = el('p', 'pv-label'); label.appendChild(el('b', '', NET[p.network] || p.network));
    label.appendChild(document.createTextNode(` · ${p.account_id} · ${p.post_id} · ${p.format}`));
    s.appendChild(label);
    s.appendChild(card(p));
    const notes = el('div', 'pv-notes');
    const len = el('div', '', `Length: ${p.length}${p.limit ? ' / ' + p.limit : ''}` + (p.network === 'x' ? ' (X counts a link as 23)' : ''));
    if (p.limit && p.length > p.limit) len.className = 'pv-over';
    notes.appendChild(len);
    notes.appendChild(el('div', '', `Hashtags: ${(p.hashtags || []).length}`));
    notes.appendChild(el('div', '', `Link: ${p.link || p.link_note || 'none'}`));
    if ((p.image_text || []).length) notes.appendChild(el('div', '', `Image text: ${p.image_text.join(' / ')}`));
    if (p.alt) notes.appendChild(el('div', '', `Alt text: ${p.alt}`));
    s.appendChild(notes);
    return s;
  }

  return { FOLD, NET, card, slot, injectCss };
})();
if (typeof module !== 'undefined' && module.exports) module.exports = SocialPreview;
