#!/usr/bin/env node
// Render an SVG illustration to PNG with headless Chromium (Playwright).
// Usage: node render.js <in.svg> <out.png> [scale=1] [--only=<groupId>[,<groupId>]]
// --only renders just the named top-level groups (others hidden) so layers
// can be composited separately (see composite.py).
// The SVG's width/height attributes define the canvas; scale multiplies
// device pixels (use 2 for delivery renders, 1 for quick inspection).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const args = process.argv.slice(2);
  const only = (args.find(a => a.startsWith('--only=')) || '').slice(7).split(',').filter(Boolean);
  const [inPath, outPath, scaleArg] = args.filter(a => !a.startsWith('--'));
  if (!inPath || !outPath) {
    console.error('usage: node render.js <in.svg> <out.png> [scale]');
    process.exit(2);
  }
  const svg = fs.readFileSync(inPath, 'utf8');
  const w = parseFloat((svg.match(/<svg[^>]*\swidth="([\d.]+)"/) || [])[1]);
  const h = parseFloat((svg.match(/<svg[^>]*\sheight="([\d.]+)"/) || [])[1]);
  if (!w || !h) { console.error('svg needs numeric width/height'); process.exit(2); }
  const scale = parseFloat(scaleArg || '1');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: scale });
  const hide = only.length
    ? `<style>svg > g[id^="layer-"]{display:none} ${only.map(id => `svg > g#${id}{display:inline}`).join(' ')}</style>`
    : '';
  await page.setContent(`<!doctype html><html><head>${hide}</head><body style="margin:0;background:transparent">${svg}</body></html>`);
  await page.locator('svg').first().screenshot({ path: outPath, omitBackground: true });
  await browser.close();
  console.log(`rendered ${path.basename(outPath)} ${w * scale}x${h * scale}`);
})().catch(e => { console.error(e); process.exit(1); });
