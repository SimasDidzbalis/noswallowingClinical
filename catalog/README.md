# Nutrioz katalogas 2026 — "33 problemos, vienas sprendimas"

16-slide 16:9 sales catalogue for clinics, retailers and wholesale partners.

## Source of the photography

Every photograph is a real Nutrioz photo pulled from the company Google Drive
(`info@nutrioz.com`). No stock, no models, no Fortivitum assets.

- `photos/spray_hero.jpg`, `photos/spray_wide.jpg` — macro shots of an actual
  Nutrioz tube spraying (Drive: *Nutrioz Molecular spray technology*)
- `photos/p_*.jpg` — real people holding Nutrioz tubes
  (Drive: *Julija Stoliarenko Nutrioz*, Nov 2025)
- `photos/life_*.jpg` — D3 + B12 tubes in daily use, US, Jan 2026
  (Drive: *Nutrioz US 2026 / US Nutrioz Photos*)

`prep.py` regenerates these from the raw Drive downloads: it bakes in EXIF
rotation (iPhone photos are orientation-6) and downscales to web size.

## Build

```
python3 build_kat4.py      # -> nutrioz-katalogas-v4.html (images inlined as data URIs)
python3 qa4.py             # Playwright: overflow / broken image / collision check + slide PNGs
python3 pdf4.py            # -> Nutrioz-katalogas-2026.pdf (1600x900 per page)
```

`build_kat4.py` also expects the product cut-outs in `opt/` (transparent tube
renders, the tablets-in-a-glass photo, the QR code).

## Content rules baked into the deck

- Doses follow the founder's authoritative facts: 1 spray = 0.06 mL = 1,000 IU
  (25 µg), ~240 sprays per tube, ~8 months, $45 retail ≈ $0.19/day.
- US reference values are used (RDA 600 IU, DV 800 IU, UL 4,000 IU).
- The 33-problem list in `problems33.py` marks each entry `X` (the format
  removes it) or `~` (reduced, not eliminated). 23 removed, 10 reduced.
- No treatment, cure, prevention or deficiency-correction claims anywhere;
  trial findings are never attributed to Nutrioz.
