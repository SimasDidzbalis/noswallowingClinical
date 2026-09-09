# Nutrioz / noswallowing.com

Next.js landing page that acts as the clinical-adherence entry point for Nutrioz
oral sprays. The commercial context below matters more than the code — this repo
is a sales asset, not a product.

## Standing working rules

- **New buyers only.** Do not propose winback, replenishment, or reactivation
  campaigns aimed at people who have already bought. Every plan must target
  buyers Nutrioz does not yet have.
- **Prefer buyers who purchase in volume on a deadline** over one-bottle
  consumers. One reseller or corporate order outweighs months of retail.
- Report revenue honestly. Zero is zero.

## Product facts (authoritative — from the founder)

These are the physical facts of the product. Treat them as given.

- One spray = **0.06 mL = 1,000 IU (25 mcg) vitamin D3**
- **~240 sprays per bottle**
- One spray per day → **240 days ≈ 8 months from a single bottle**
- Retail price **$45** → about **$0.19 per day**

US reference values, for context when writing copy:

| | Value |
|---|---|
| RDA, adults 19–70 | 600 IU |
| RDA, 71+ | 800 IU |
| Daily Value (supplement labels) | 800 IU |
| Tolerable Upper Intake Level | 4,000 IU |

One spray therefore delivers **125% of the US Daily Value**.

## Positioning

The old framing — "no swallowing required" — reads as a disability
accommodation and reaches a small, hard-to-find audience that buys one bottle at
a time.

The working framing is **frictionless daily adherence**: 45 $ covers one person
for a whole winter, at two seconds a day. That sells to gift and bulk buyers,
who purchase on a deadline and in quantity.

Supporting evidence (cite by name, never as a Nutrioz claim):

- **VITAL telomere sub-study**, *Am J Clin Nutr* 2025 — 2,000 IU/day for 4 years
  reduced telomere attrition by 140 bp (~3 years of aging). n=1,054.
- **Martineau et al.**, *BMJ* 2017 — vitamin D and acute respiratory infection,
  OR 0.88, NNT 33; OR 0.30 where baseline 25(OH)D < 25 nmol/L.
- **Satia et al.**, *Nutrition Journal* 2015 — oral spray raised 25(OH)D roughly
  twice as much as capsules at 1,000 IU/day.
- Systematic review of 71 studies — vitamin D deficiency in 78% of indoor
  workers vs 48% of outdoor workers.
- **Cashman et al.**, *Am J Clin Nutr* 2016;103(4):1033–44 — standardised
  25(OH)D across 14 European studies, n=55,844: **40.4%** below 50 nmol/L;
  **17.7%** below 30 nmol/L in winter vs 8.3% in summer.
  doi:10.3945/ajcn.115.120873
- **Martineau et al.**, *BMJ* 2017;356:i6583 — the detail that matters
  commercially: daily or weekly dosing OR 0.81, **bolus dosing OR 0.97 (no
  effect)**, OR 0.30 where baseline 25(OH)D < 25 nmol/L. 25 RCTs, 10,933
  participants aged 0–95. doi:10.1136/bmj.i6583
- **Serrano Santos et al.**, *Int J Pharm* 2016;512(2):416–21 — UK care homes:
  50% of residents have dysphagia; medication-administration error rate 57.3%
  in them vs 30.8% in others. doi:10.1016/j.ijpharm.2016.02.036
- **Buhmann et al.**, *Parkinsonism Relat Disord* 2019;62:51–56 — endoscopic
  assessment: 28% of Parkinson's patients and **16% of healthy controls** had
  substantially impaired pill swallowing. doi:10.1016/j.parkreldis.2019.02.002
- **Jagani et al.**, *Pediatrics* 2016;138(6) — children on long-term therapy
  carry an average burden of **3.5 tablets per day**. doi:10.1542/peds.2016-0680

All six were retrieved from PubMed. Cite them by author, journal and year; never
attribute any of these findings to Nutrioz.

## Photography available (Google Drive, info@nutrioz.com)

Real Nutrioz photography exists for: macro spray shots (*Nutrioz Molecular spray
technology*), people holding tubes (*Julija Stoliarenko Nutrioz*, Nov 2025),
D3+B12 in daily use (*Nutrioz US 2026*), elderly hands holding a tube (*Nutrioz
Photos for Google*), and Dr. Elena Dudėnaitė (*Social media assets → Linkedin*).

**There are no photographs of children with the product, and none of a doctor
or pharmacist actually using it.** Do not imply otherwise in any asset. Much of
the lifestyle material is HEIC, which the build container cannot decode —
convert to JPEG in Drive before it can be used.

## Compliance guardrails

Nutrioz is a dietary supplement, not a treatment. Never write that it treats,
cures, prevents, or corrects a deficiency, and never attribute trial findings to
Nutrioz itself. Describe the trial dose and cite the trial. The same rules gate
listing approval on Amazon, Faire, and TikTok Shop.

## Store state (as of 2026-08-29)

Shopify, Basic plan, USD, ~10,970 units of D3 in stock.

- `vitamin-d3` — $45, rewritten around the 240-day story
- `winter-pack-vitamin-d3-oral-spray` — $79, 2 bottles; volume tiers $69/$64/$59
- `vitamin-d3-5-bottle-partner-pilot` — $109 wholesale pilot, UNLISTED (direct
  link only), for clinics and retailers
- Sales channels live: Online Store, Shop, Google, Facebook, TikTok, and
  **Faire wholesale** (5 products published, no orders yet)

Two products are ACTIVE but **not published to the Online Store**, so they have
no buyable page: the dysphagia B12 spray (`10151463453010`) and the dysphagia
Sleep spray (`10151502020946`). Unresolved — they may be intentional duplicates.
