import sys, re, vtracer
from PIL import Image
import numpy as np

def masks(img):
    a = np.asarray(img.convert('RGB')).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    dark = (r + g + b) < 200                                  # near-black letters
    orange = (r > 200) & (g > 50) & (g < 150) & (b < 90)      # orange dot / tile
    cream = (r > 215) & (g > 205) & (b > 185)
    return dark, orange, cream

def trace(mask, tmp):
    Image.fromarray(np.where(mask, 0, 255).astype('uint8')).convert('RGB').save(tmp)
    svg = vtracer.convert_raw_image_to_svg  # noqa
    out = tmp.replace('.png', '.svg')
    vtracer.convert_image_to_svg_py(tmp, out, colormode='binary', mode='spline', filter_speckle=8,
                                    corner_threshold=60, length_threshold=4.0, splice_threshold=45, path_precision=2)
    s = open(out).read()
    return [re.sub(r'\sfill="[^"]*"', '', x) for x in re.findall(r'<path[^>]*/>', s)]

def bbox(mask, pad):
    ys, xs = np.where(mask)
    return max(xs.min() - pad, 0), max(ys.min() - pad, 0), xs.max() + pad, ys.max() + pad

def wordmark(src, dst):
    img = Image.open(src)
    dark, orange, _ = masks(img)
    x0, y0, x1, y1 = bbox(dark | orange, 6)
    crop = img.crop((x0, y0, x1 + 1, y1 + 1))
    d, o, _ = masks(crop)
    pd = trace(d, 'logo/svg/_d.png'); po = trace(o, 'logo/svg/_o.png')
    w, h = crop.size
    paths = ''.join(p.replace('<path', '<path fill="currentColor"', 1) for p in pd)
    paths += ''.join(p.replace('<path', '<path fill="#FF5A1F" class="dot"', 1) for p in po)
    paths = re.sub(r' fill="#[0-9A-Fa-f]{6}"(?= )', '', paths, count=0) if False else paths
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="7WILD.">{paths}</svg>'
    open(dst, 'w').write(svg); print(dst, w, h, len(pd), 'letter paths', len(po), 'dot paths', len(svg)//1024, 'KB')

def icon(src, dst):
    img = Image.open(src)
    dark, orange, cream = masks(img)
    x0, y0, x1, y1 = bbox(orange, 0)
    crop = img.crop((x0, y0, x1 + 1, y1 + 1))
    d, o, c = masks(crop)
    pd = trace(d, 'logo/svg/_d.png'); pc = trace(c & ~o & ~d, 'logo/svg/_c.png')
    w, h = crop.size
    r = round(w * 0.225)
    body = f'<rect width="{w}" height="{h}" rx="{r}" fill="#FF5A1F"/>'
    body += ''.join(p.replace('<path', '<path fill="#111111"', 1) for p in pd)
    # cream dot only (drop cream corner remnants outside the rounded square)
    body += ''.join(p.replace('<path', '<path fill="#F3EEE4"', 1) for p in pc)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="7WILD app icon"><clipPath id="r"><rect width="{w}" height="{h}" rx="{r}"/></clipPath><g clip-path="url(#r)">{body}</g></svg>'
    open(dst, 'w').write(svg); print(dst, w, h, len(svg)//1024, 'KB')

O = 'aic-7wild/7Wild/oneoff/out-logo/'
wordmark(O + 'wordmark-black-a.png', 'logo/svg/7wild-wordmark.svg')
wordmark(O + 'stacked.png', 'logo/svg/7wild-stacked.svg')
icon(O + 'icon-7.png', 'logo/svg/7wild-icon.svg')
