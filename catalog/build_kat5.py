import base64, os, re
from problems33 import P

def U(path):
    e = "jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "png"
    return "data:image/%s;base64,%s" % (e, base64.b64encode(open(path, "rb").read()).decode())

I = {k: U("opt/%s.%s" % (k, e)) for k, e in
     [("d3", "png"), ("b12", "png"), ("multi", "png"), ("energy", "png"),
      ("sleep", "png"), ("hero", "jpeg"), ("lineup", "png"), ("qr", "png")]}
# real Nutrioz photography, harvested from the company Google Drive
R = {f[:-4]: U("opt2/" + f) for f in sorted(os.listdir("opt2")) if f.endswith(".jpg")}

CSS = """
*{box-sizing:border-box;margin:0;}
body{background:#0A1416;font-family:'Poppins',-apple-system,sans-serif;color:#0A1416;-webkit-font-smoothing:antialiased;}
.deck{max-width:1180px;margin:0 auto;padding:24px 16px 70px;display:flex;flex-direction:column;gap:14px;}
.dh{display:flex;justify-content:space-between;align-items:baseline;padding:10px 2px 4px;}
.dh b{font-size:17px;font-weight:600;color:#7FD3E2;} .dh b span{font-weight:200;color:#5E7278;}
.dh p{font-size:12px;color:#5E7278;font-weight:300;}
.s{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;background:#fff;}
.bleed{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.bleed.lift{filter:brightness(1.42) contrast(1.14);}
.veil{position:absolute;inset:0;}
.pad{position:absolute;inset:0;padding:4.6cqw 5.4cqw;display:flex;flex-direction:column;}
.top{display:flex;justify-content:space-between;align-items:baseline;flex:0 0 auto;}
.bot{display:flex;justify-content:space-between;align-items:flex-end;flex:0 0 auto;padding-top:1cqw;}
.mid{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:flex-end;padding-top:1.4cqw;}
.mid.c{justify-content:center;}
.wm{font-size:1.3cqw;font-weight:600;} .eb{font-size:.94cqw;font-weight:500;letter-spacing:.2em;text-transform:uppercase;}
.pg{font-size:.94cqw;font-weight:400;font-variant-numeric:tabular-nums;}
.d1{font-size:7cqw;font-weight:600;line-height:.99;letter-spacing:-.042em;}
.d2{font-size:4.2cqw;font-weight:600;line-height:1.05;letter-spacing:-.035em;}
.d3s{font-size:2.3cqw;font-weight:500;line-height:1.16;letter-spacing:-.02em;}
.mono{font-size:13cqw;font-weight:600;line-height:.82;letter-spacing:-.055em;}
.bd{font-size:1.26cqw;font-weight:300;line-height:1.52;}
.bd.lg{font-size:1.55cqw;line-height:1.48;}
.fn{font-size:.86cqw;font-weight:300;line-height:1.4;}
.lt{color:#0A1416;} .lt .eb,.lt .wm{color:#17879B;} .lt .bd{color:#4A5C61;} .lt .fn{color:#6E7F85;} .lt .pg{color:#B4C1C5;}
.dkt{color:#fff;} .dkt .eb{color:#7FD3E2;} .dkt .wm{color:#fff;} .dkt .bd{color:rgba(255,255,255,.74);}
.dkt .fn{color:rgba(255,255,255,.62);} .dkt .pg{color:rgba(255,255,255,.5);}
.dkt .eb,.dkt .wm,.dkt .fn,.dkt .pg{text-shadow:0 1px 10px rgba(4,16,19,.85);}
.tl{color:#17879B;} .dkt .tl{color:#7FD3E2;}
.cols{display:flex;gap:3.4cqw;}
.cols.big .kv .k{font-size:4.8cqw;letter-spacing:-.045em;}
.cols.big .kv .l{font-size:1.02cqw;}
.kv{display:flex;flex-direction:column;gap:.35cqw;}
.kv .k{font-size:2.7cqw;font-weight:600;letter-spacing:-.03em;line-height:1;}
.kv .l{font-size:.92cqw;font-weight:300;line-height:1.34;}
.cut{position:absolute;object-fit:contain;}
figure{margin:0;} figcaption{font-size:.86cqw;font-weight:300;line-height:1.4;margin-top:1.2cqw;}
svg{display:block;max-width:100%;height:auto;}
.prow{display:flex;align-items:flex-end;justify-content:space-between;gap:1.4cqw;height:100%;}
.pit{display:flex;flex-direction:column;align-items:center;gap:.8cqw;flex:1;min-width:0;height:100%;justify-content:flex-end;}
.pit img{height:62%;width:auto;max-width:100%;object-fit:contain;}
.pit .n{font-size:1.1cqw;font-weight:600;text-align:center;}
.pit .d{font-size:.84cqw;font-weight:300;line-height:1.3;text-align:center;}
.plist{display:grid;grid-template-columns:1fr 1fr;gap:.5cqw 3.2cqw;}
.pi{display:grid;grid-template-columns:2.4cqw 1fr;gap:.9cqw;padding:.62cqw 0;border-top:1px solid rgba(10,20,22,.10);align-items:start;}
.dkt .pi{border-top-color:rgba(255,255,255,.14);}
.pi .no{font-size:.92cqw;font-weight:600;font-variant-numeric:tabular-nums;padding-top:.16cqw;}
.pi .tx{min-width:0;}
.pi .pb{font-size:1.04cqw;font-weight:500;line-height:1.28;}
.pi .an{font-size:.94cqw;font-weight:300;line-height:1.3;margin-top:.16cqw;}
.pi .mk{font-size:.8cqw;font-weight:600;letter-spacing:.06em;}
.grph{font-size:.92cqw;font-weight:600;letter-spacing:.2em;text-transform:uppercase;margin:1.3cqw 0 .3cqw;}
.grph:first-child{margin-top:0;}
/* photo blocks */
.ph{position:absolute;overflow:hidden;background:#132328;}
.ph img{width:100%;height:100%;object-fit:cover;display:block;}
.ph .cap{position:absolute;left:0;right:0;bottom:0;padding:1.1cqw .9cqw .7cqw;
  background:linear-gradient(180deg,rgba(6,20,23,0),rgba(6,20,23,.88));
  font-size:.8cqw;font-weight:400;line-height:1.3;color:#fff;}
.pgrid{display:grid;gap:.9cqw;height:100%;}
.gph{position:relative;overflow:hidden;background:#132328;min-height:0;}
.gph img{width:100%;height:100%;object-fit:cover;display:block;}
.gph .cap{position:absolute;left:0;right:0;bottom:0;padding:1.6cqw .9cqw .75cqw;
  background:linear-gradient(180deg,rgba(6,20,23,0),rgba(6,20,23,.9));
  font-size:.82cqw;font-weight:400;line-height:1.32;color:#fff;}
.tick{display:flex;gap:.9cqw;align-items:baseline;font-size:1.28cqw;font-weight:300;line-height:1.46;padding:.72cqw 0;border-top:1px solid rgba(10,20,22,.09);}
.tick b{font-weight:600;font-size:1.06cqw;letter-spacing:.04em;flex:0 0 auto;}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:2.2cqw 4cqw;}
.fact{display:flex;flex-direction:column;gap:.5cqw;}
.fact .n{font-size:5.2cqw;font-weight:600;letter-spacing:-.045em;line-height:.92;}
.fact .t{font-size:1.16cqw;font-weight:400;line-height:1.38;}
.fact .src{font-size:.82cqw;font-weight:300;line-height:1.34;}
.dkt .fact .src{color:rgba(255,255,255,.5)} .lt .fact .src{color:#7E8D92}
.cite{font-size:.82cqw;font-weight:300;line-height:1.5;}
.cite b{font-weight:500}

"""


_N=[0]
def S(cls, inner, eb="", bleed=None, veil=None, pg=True, bg=None, extra="", lift=False):
    _N[0]+=1; n=_N[0]
    im = '<img class="bleed%s" src="%s" alt="">' % (" lift" if lift else "", bleed) if bleed else ""
    vl = '<div class="veil" style="%s"></div>' % veil if veil else ""
    st = ' style="background:%s"' % bg if bg else ""
    return ('<div class="s %s"%s>%s%s%s<div class="pad">'
            '<div class="top"><div class="wm">Nutrioz</div><div class="eb">%s</div></div>%s'
            '<div class="bot"><div class="fn">nutrioz.lt</div><div class="pg">%s</div></div></div></div>'
            ) % (cls, st, im, vl, extra, eb, inner, "%02d" % n if pg else "")


def gph(key, cap):
    return '<div class="gph"><img src="%s" alt="%s"><div class="cap">%s</div></div>' % (R[key], cap, cap)


D = []

# 01 — cover, real macro spray photo
D.append(S("dkt",
  '<div class="mid"><div class="eb" style="margin-bottom:2cqw">Katalogas · 2026</div>'
  '<div class="d1">33 problemos.<br>Vienas sprendimas.</div>'
  '<div class="bd lg" style="max-width:34cqw;margin-top:2cqw;margin-bottom:2cqw">'
  'Ką maisto papildų pramonė paliko neišspręsta — ir ką pakeitė vienas 0,06 ml papurškimas.</div></div>',
  eb="Nutrioz Molecular Spray", bleed=R['spray_hero'], lift=True,
  veil="background:linear-gradient(100deg,rgba(6,26,30,.96) 0%,rgba(6,26,30,.86) 38%,rgba(6,26,30,.12) 74%,rgba(6,26,30,0) 100%)",
  pg=False))

# 02 — the question
D.append(S("dkt",
  '<div class="mid"><div class="d2" style="max-width:56cqw;font-size:3.8cqw">Kodėl reikia nuryti 2 gramus,<br>kad gautum 25 mikrogramus?</div>'
  '<div class="cols" style="margin-top:2.4cqw">'
  '<div class="kv"><div class="k">2 000 000 µg</div><div class="l">medžiagos nuryjate<br>su 2 g tablete</div></div>'
  '<div class="kv"><div class="k tl">25 µg</div><div class="l">iš jų yra<br>vitaminas D3</div></div>'
  '<div class="kv"><div class="k tl">33×</div><div class="l">mažiau medžiagos<br>su Nutrioz</div></div></div>'
  '<div class="fn" style="max-width:50cqw;margin-top:1.8cqw">Purškiamos formulės masė vertinta esant ~1 g/ml tankiui. '
  'Tūrio ir masės palyginimas, ne klinikinio pranašumo teiginys.</div></div>',
  eb="Klausimas", bleed=I['hero'],
  veil="background:linear-gradient(90deg,rgba(6,26,30,0) 0%,rgba(6,26,30,.34) 26%,rgba(6,26,30,.9) 56%,rgba(6,26,30,.96) 100%)"))

# 03 — the spray itself, real photo, full bleed
D.append(S("dkt",
  '<div class="mid"><div class="d2" style="max-width:40cqw">0,06 ml.<br>Štai ir viskas.</div>'
  '<div class="cols" style="margin-top:2.2cqw">'
  '<div class="kv"><div class="k tl">1</div><div class="l">papurškimas</div></div>'
  '<div class="kv"><div class="k tl">25 µg</div><div class="l">vitamino D3<br>(1000 TV)</div></div>'
  '<div class="kv"><div class="k tl">2 s</div><div class="l">visa dienos<br>procedūra</div></div></div>'
  '<div class="fn" style="max-width:42cqw;margin-top:1.6cqw">Tikra Nutrioz purškimo nuotrauka, ne iliustracija.</div></div>',
  eb="Kaip tai atrodo iš tikrųjų", bleed=R['spray_wide'], lift=True,
  veil="background:linear-gradient(90deg,rgba(6,26,30,.94) 0%,rgba(6,26,30,.88) 30%,rgba(6,26,30,.34) 52%,rgba(6,26,30,0) 70%)"))

# 04 — technology, donkey-proof
TECH = '''<figure style="width:100%">
<svg viewBox="0 0 1000 250" role="img" aria-label="Tabletes kelias: nuryti, skrandis ardo, vitaminas issilaisvina, tik tada isisavinama. Nutrioz kelias: papurksti ant zando.">
 <defs><marker id="a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>
 <text x="0" y="12" font-size="13" font-weight="600" letter-spacing="2.6" fill="currentColor" opacity=".5">TABLETĖ — KETURI ŽINGSNIAI</text>
 <g opacity=".6">
  <circle cx="42" cy="62" r="26" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="42" y="67" font-size="15" text-anchor="middle" fill="currentColor">1</text>
  <text x="42" y="112" font-size="13" text-anchor="middle" fill="currentColor">Nuryti</text>
  <line x1="78" y1="62" x2="146" y2="62" stroke="currentColor" marker-end="url(#a1)"/>
  <circle cx="188" cy="62" r="26" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="188" y="67" font-size="15" text-anchor="middle" fill="currentColor">2</text>
  <text x="188" y="112" font-size="13" text-anchor="middle" fill="currentColor">Skrandis ardo</text>
  <line x1="224" y1="62" x2="292" y2="62" stroke="currentColor" marker-end="url(#a1)"/>
  <circle cx="334" cy="62" r="26" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="334" y="67" font-size="15" text-anchor="middle" fill="currentColor">3</text>
  <text x="334" y="112" font-size="13" text-anchor="middle" fill="currentColor">Vitaminas išsilaisvina</text>
  <line x1="370" y1="62" x2="438" y2="62" stroke="currentColor" marker-end="url(#a1)"/>
  <circle cx="480" cy="62" r="26" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="480" y="67" font-size="15" text-anchor="middle" fill="currentColor">4</text>
  <text x="480" y="112" font-size="13" text-anchor="middle" fill="currentColor">Tik dabar įsisavinama</text>
 </g>
 <text x="0" y="168" font-size="13" font-weight="600" letter-spacing="2.6" fill="#7FD3E2">NUTRIOZ — VIENAS</text>
 <circle cx="42" cy="216" r="26" fill="#7FD3E2" opacity=".18"/><circle cx="42" cy="216" r="26" fill="none" stroke="#7FD3E2" stroke-width="1.6"/>
 <text x="42" y="221" font-size="15" text-anchor="middle" fill="#7FD3E2">1</text>
 <text x="88" y="210" font-size="15" font-weight="500" fill="currentColor">Papurkšti ant žando.</text>
 <text x="88" y="232" font-size="13" fill="currentColor" opacity=".7">Vitaminas jau skystas — nieko nereikia ardyti, nieko nereikia nuryti.</text>
</svg>
<figcaption class="fn">Paaiškinanti schema. Nutrioz pašalina pirmuosius tris kietos formos etapus. Nutrioz produkto absorbcijos per gleivinę dalis nėra išmatuota; tai vartojimo būdo skirtumas, ne klinikinio pranašumo garantija.</figcaption></figure>'''
D.append(S("dkt",
  '<div class="mid c"><div class="d2" style="margin-bottom:2.2cqw">Kur dingsta trys žingsniai</div>' + TECH + '</div>',
  eb="Purškimo technologija", bg="#0A1416"))

# ── ŠOKIRUOJANTYS FAKTAI ───────────────────────────────────────────────
def fact(n, t, src):
    return ('<div class="fact"><div class="n tl">%s</div><div class="t">%s</div>'
            '<div class="src">%s</div></div>' % (n, t, src))

D.append(S("dkt",
  '<div class="mid c"><div class="d1" style="font-size:5.6cqw;max-width:52cqw">Prieš perkant dar vieną tabletę — trys skaičiai.</div>'
  '<div class="bd" style="max-width:44cqw;margin-top:2cqw">Visi trys iš recenzuojamų tyrimų. Nė vienas iš jų nėra Nutrioz tyrimas '
  'ir nė vienas nieko neteigia apie Nutrioz.</div></div>',
  eb="Faktai, kurių pardavėjai nesako", bg="#0A1416"))

D.append(S("lt",
  '<div class="mid c"><div class="d2" style="margin-bottom:2.4cqw;max-width:52cqw">Trūkumas nėra retas atvejis. Jis yra norma.</div>'
  '<div class="facts">'
  + fact("40,4 %", "europiečių kraujo 25(OH)D buvo žemiau 50 nmol/l. Tirta 55 844 žmonės — nuo kūdikių iki senjorų.",
         "Cashman ir kt., <b>Am J Clin Nutr</b> 2016;103(4):1033–44. Standartizuoti 14 Europos populiacijų duomenys.")
  + fact("17,7 %", "žiemos pusmetį (spalis–kovas) buvo žemiau 30 nmol/l — tai jau sunkaus trūkumo riba.",
         "Ta pati Cashman 2016 analizė. Vasarą — 8,3 %.")
  + fact("78 %", "patalpose dirbančių žmonių turėjo vitamino D trūkumą, palyginti su 48 % dirbančių lauke.",
         "71 tyrimo sisteminė apžvalga. Biuras yra rizikos veiksnys.")
  + fact("2 sek.", "tiek trunka vienas Nutrioz papurškimas. Tai vienintelis šioje lentelėje skaičius apie Nutrioz.",
         "Nutrioz duomenys: 0,06 ml = 25 µg (1000 TV), ~240 papurškimų tūbelėje.")
  + '</div></div>',
  eb="Faktas 01 · Kiek žmonių tai liečia"))

D.append(S("dkt",
  '<div class="mid c"><div class="d2" style="margin-bottom:1.6cqw;max-width:56cqw">Didelė dozė kartą per mėnesį neveikė. Kasdienė — veikė.</div>'
  '<div class="cols big" style="gap:4.4cqw;margin-bottom:1.8cqw">'
  '<div class="kv"><div class="k tl">0,81</div><div class="l">šansų santykis, kai vitaminas D<br>duotas <b>kasdien arba kas savaitę</b></div></div>'
  '<div class="kv"><div class="k" style="color:#E06A5E">0,97</div><div class="l">šansų santykis, kai duota<br><b>viena didelė dozė</b> — poveikio nerasta</div></div>'
  '<div class="kv"><div class="k tl">0,30</div><div class="l">tiems, kurių pradinis 25(OH)D<br>buvo žemiau 25 nmol/l</div></div></div>'
  '<div class="bd" style="max-width:58cqw">Tai reiškia vieną dalyką: svarbu ne kiek išgeri iš karto, o ar padarai tai kiekvieną dieną. '
  'Formatas, kurio nepamiršti, yra svarbesnis už formatą, kurio dozė didesnė.</div>'
  '<div class="cite" style="margin-top:1.6cqw;max-width:64cqw">Šaltinis: <b>Martineau ir kt., BMJ 2017;356:i6583</b> — 25 atsitiktinių imčių tyrimų '
  'individualių dalyvių duomenų metaanalizė, 10 933 dalyviai nuo 0 iki 95 metų. Tyrime naudoti įvairūs vitamino D preparatai; '
  'Nutrioz jame nedalyvavo ir šie rezultatai nėra Nutrioz teiginys. Maisto papildas nėra vaistas ir negydo ligų.</div></div>',
  eb="Faktas 02 · Kodėl svarbu kasdien", bg="#0F2A30"))

D.append(S("lt",
  '<div class="mid c"><div class="d2" style="margin-bottom:2.4cqw;max-width:54cqw">O dabar — apie patį nurijimą.</div>'
  '<div class="facts">'
  + fact("50 %", "slaugos namų gyventojų Jungtinėje Karalystėje turi rijimo sutrikimą (disfagiją).",
         "Serrano Santos ir kt., <b>Int J Pharm</b> 2016;512(2):416–21.")
  + fact("57,3 %", "vaistų davimo atvejų šiems žmonėms buvo su klaida — prieš 30,8 % tiems, kurie ryja normaliai.",
         "Ta pati stebėjimo studija: 738 vaistų davimo atvejai, 166 pacientai.")
  + fact("16 %", "sveikų kontrolinės grupės žmonių irgi buvo ryškiai sutrikęs gebėjimas nuryti tabletę.",
         "Buhmann ir kt., <b>Parkinsonism Relat Disord</b> 2019;62:51–56, endoskopinis vertinimas.")
  + fact("3,5", "tabletės per dieną — vidutinė našta vaikams, ilgai vartojantiems vaistus.",
         "Jagani ir kt., <b>Pediatrics</b> 2016;138(6). Rijimo sunkumai jiems yra kasdienė kova.")
  + '</div>'
  '<div class="cite" style="margin-top:1.8cqw;max-width:72cqw">Šie tyrimai atlikti su vaistais, ne su Nutrioz, ir nieko neteigia apie Nutrioz veiksmingumą. '
  'Jie paaiškina, kodėl kieta forma pati savaime yra kliūtis — ir kodėl jos pašalinimas yra atskira vertė.</div></div>',
  eb="Faktas 03 · Kaina, kurios niekas neskaičiuoja"))

# 33 intro
D.append(S("lt",
  '<div class="mid c"><div class="mono tl">33</div>'
  '<div class="d3s" style="margin-top:.5cqw;max-width:44cqw">problemos, kurias turi tabletės, kapsulės ir guminukai.</div>'
  '<div class="cols" style="margin-top:2.6cqw">'
  '<div class="kv"><div class="k tl">23</div><div class="l">pašalina pats formatas</div></div>'
  '<div class="kv"><div class="k">10</div><div class="l">sumažina, bet nepanaikina</div></div></div>'
  '<div class="fn" style="max-width:48cqw;margin-top:2cqw">Sąrašas sudarytas sąžiningai. Ten, kur Nutrioz problemos nepanaikina iki galo, '
  'tai pažymėta ženklu ~ — nes tikrinamas sąrašas įtikina labiau nei nepatikrinamas.</div></div>'
  f'<img class="cut" src="{I["d3"]}" alt="" style="right:-9cqw;top:-16cqw;height:152%;transform:rotate(14deg)">',
  eb="Ką iš tikrųjų išsprendžia naujas būdas"))


def plist(groups, letters):
    out = []
    n = 1
    for code, name, items in groups:
        if code not in letters:
            n += len(items)
            continue
        out.append('<div class="grph tl" style="grid-column:1/-1">%s</div>' % name)
        for pb, an, st in items:
            mk = ('<span class="mk tl">✕ pašalinta</span>' if st == "X"
                  else '<span class="mk" style="color:#8B999E">~ sumažinta</span>')
            out.append('<div class="pi"><div class="no tl">%02d</div><div class="tx">'
                       '<div class="pb">%s</div><div class="an">%s &nbsp;%s</div></div></div>' % (n, pb, an, mk))
            n += 1
    return '<div class="plist">%s</div>' % "".join(out)


D.append(S("lt", '<div class="mid c">' + plist(P, {"A", "B"}) + '</div>', eb="Problemos 01–15"))
D.append(S("lt", '<div class="mid c">' + plist(P, {"C", "D"}) + '</div>', eb="Problemos 16–26"))
D.append(S("lt", '<div class="mid c">' + plist(P, {"E"})
  + '<div class="fn" style="margin-top:1.6cqw;max-width:56cqw">Visos 33 problemos kyla ne iš vitamino, o iš jo pateikimo formos. '
    'Todėl jas ir sprendžia kitas formatas, o ne kita formulė.</div></div>',
  eb="Problemos 27–33"))

# 09 — 240
D.append(S("dkt",
  '<div class="mid c"><div class="mono tl">240</div>'
  '<div class="d3s" style="margin-top:.5cqw;max-width:42cqw">papurškimų. Vienas per dieną — tūbelės užtenka apie aštuonis mėnesius.</div>'
  '<div class="fn" style="max-width:44cqw;margin-top:1.8cqw">Vienas papurškimas — 25 µg (1000 TV) vitamino D3. '
  'JAV rekomenduojama paros norma suaugusiesiems 600 TV, etiketės dienos norma 800 TV, viršutinė leistina riba 4000 TV. '
  'Individualią dozę derinti su gydytoju.</div></div>'
  f'<img class="cut" src="{I["d3"]}" alt="" style="right:-11cqw;top:-20cqw;height:164%;transform:rotate(16deg)">',
  eb="Viena tūbelė", bg="#0F2A30"))

# 10 — real people, hero split
D.append(S("dkt",
  '<div class="mid c" style="max-width:44cqw"><div class="d2">Tikri žmonės.<br>Tikros tūbelės.</div>'
  '<div class="bd" style="margin-top:1.6cqw;max-width:34cqw">Nė vienos nupirktos nuotraukos. Nė vieno modelio. '
  'Visi šiame kataloge esantys žmonės laiko rankose tą patį Nutrioz produktą, kurį galite užsisakyti šiandien.</div>'
  '<div class="fn" style="margin-top:1.6cqw;max-width:34cqw">Nutrioz archyvas, 2025–2026.</div></div>'
  '<div class="ph" style="left:50cqw;top:0;width:25cqw;height:100%"><img src="' + R['p_hero'] + '" alt="Vyras laiko Nutrioz Vitamin D3 purskikli"></div>'
  '<div class="ph" style="left:75cqw;top:0;width:25cqw;height:100%"><img src="' + R['p_pair'] + '" alt="Du vyrai su Nutrioz purskikliais sporto klube"></div>',
  eb="Kas jau vartoja", bg="#0A1416"))

# 11 — people grid
D.append(S("dkt",
  '<div class="mid c" style="padding-top:0">'
  '<div class="pgrid" style="grid-template-columns:repeat(4,1fr);grid-template-rows:1fr">'
  + gph('p_gym', 'Bokso klubas — tūbelė sportinėje krepšyje, ne vaistinėlėje')
  + gph('p_pair2', 'Sportininkas ir platintojas — tas pats produktas rankose')
  + gph('p_hand', 'Perdavimas iš rankų į rankas — jokių instrukcijų nereikėjo')
  + gph('p_duo', 'Treniruočių salė, vakaras — dvi sekundės ir grįžtama prie darbo')
  + '</div></div>',
  eb="Realios naudojimo situacijos", bg="#0A1416"))

# 12 — daily use / lifestyle
D.append(S("dkt",
  '<div class="mid c" style="padding-top:0">'
  '<div class="d2" style="max-width:30cqw;position:absolute;left:5.4cqw;top:11cqw">Telpa ten,<br>kur jau esate.</div>'
  '<div class="bd" style="max-width:26cqw;position:absolute;left:5.4cqw;top:27cqw">Ant pusryčių stalo, kavinėje, kelionės krepšyje. '
  'Nereikia vandens, nereikia stiklinės, nereikia laukti.</div>'
  '<div class="pgrid" style="grid-template-columns:repeat(3,1fr);position:absolute;left:38cqw;right:5.4cqw;top:9cqw;bottom:9cqw;height:auto">'
  + gph('life_juice', 'D3 ir B12 prie ryto sulčių — JAV, 2026')
  + gph('life_salad', 'Pietūs mieste: tūbelė ant stalo, ne kišenėje')
  + gph('life_table', 'Du produktai, du papurškimai, jokio vandens')
  + '</div></div>',
  eb="Kasdienybėje", bg="#0F2A30"))

# ── SENJORAI / GYDYTOJAI / VAIKAI ──────────────────────────────────────
D.append(S("dkt",
  '<div class="mid c" style="max-width:42cqw"><div class="d2">Rankos, kurioms<br>tabletė jau sunki.</div>'
  '<div class="bd" style="margin-top:1.6cqw;max-width:34cqw">Blisteris, kurio nepavyksta atplėšti. Tabletė, kurią reikia perlaužti pusiau. '
  'Stiklinė vandens, kurios reikia ieškoti. Nutrioz nereikia nė vieno iš šių žingsnių.</div>'
  '<div class="cite" style="margin-top:1.6cqw;max-width:34cqw">Pusė slaugos namų gyventojų JK turi rijimo sutrikimą '
  '(Serrano Santos, Int J Pharm 2016). Nutrioz yra maisto papildas, o ne gydymo priemonė.</div></div>'
  '<div class="ph" style="left:47cqw;top:0;width:53cqw;height:100%"><img src="' + R['senior_hands'] + '" alt="Vyresnio zmogaus rankos laiko Nutrioz Vitamin D3 purskikli"></div>',
  eb="Senjorai", bg="#0A1416"))

D.append(S("lt",
  '<div class="mid c" style="max-width:50cqw"><div class="d2">Kai rekomenduoja<br>specialistas.</div>'
  '<div class="bd" style="margin-top:1.6cqw;max-width:40cqw">Klinikoms, vaistinėms ir sveikatingumo kabinetams Nutrioz yra paprastas atsakymas '
  'pacientui, kuris sako: „aš tų tablečių tiesiog negeriu“.</div>'
  '<div class="cols" style="margin-top:2.2cqw">'
  '<div class="kv"><div class="k tl">109 $</div><div class="l">partnerio pilotas,<br>5 tūbelės</div></div>'
  '<div class="kv"><div class="k tl">240</div><div class="l">papurškimų<br>vienoje tūbelėje</div></div>'
  '<div class="kv"><div class="k tl">0,19 $</div><div class="l">paciento kaina<br>vienai dienai</div></div></div>'
  '<div class="cite" style="margin-top:1.8cqw;max-width:42cqw">Dienos kaina skaičiuota nuo 45 $ mažmeninės kainos ir 240 papurškimų. '
  'Nutrioz yra maisto papildas — jis negydo, nediagnozuoja ir nepakeičia gydytojo nurodymų.</div></div>'
  '<div class="ph" style="left:56cqw;top:0;width:44cqw;height:100%"><img src="' + R['doctor'] + '" alt="Gydytoja Elena Dudenaite"><div class="cap">Dr. Elena Dudėnaitė</div></div>',
  eb="Gydytojams ir klinikoms"))

D.append(S("dkt",
  '<div class="mid c"><div class="d2" style="max-width:48cqw;margin-bottom:2cqw">Vaikas nesiginčija su purškikliu.</div>'
  '<div class="cols" style="gap:4cqw;margin-bottom:1.8cqw">'
  '<div class="kv"><div class="k tl">3,5</div><div class="l">tabletės per dieną — vidutinė<br>našta vaikui, ilgai vartojančiam vaistus</div></div>'
  '<div class="kv"><div class="k tl">0</div><div class="l">tablečių, kurias reikia<br>nuryti su Nutrioz</div></div>'
  '<div class="kv"><div class="k tl">2 sek.</div><div class="l">tiek trunka visa<br>rytinė procedūra</div></div></div>'
  '<div class="bd" style="max-width:56cqw">Rijimo sunkumai vaikams nėra retenybė ir nėra užgaida — tai kasdienė kova, kurią aprašo pediatrinė literatūra. '
  'Purškiama forma šios kovos tiesiog nesukuria.</div>'
  '<div class="cite" style="margin-top:1.6cqw;max-width:64cqw">Skaičius apie 3,5 tabletės: <b>Jagani ir kt., Pediatrics 2016;138(6)</b>. '
  'Tyrimas atliktas su vaistais, ne su Nutrioz. Vaikams skirtą dozę ir amžiaus ribas žiūrėkite konkretaus produkto etiketėje '
  'ir derinkite su vaiko gydytoju.</div></div>',
  eb="Vaikams ir tėvams", bleed=R['spray_wide'], lift=True,
  veil="background:linear-gradient(90deg,rgba(6,26,30,.95) 0%,rgba(6,26,30,.9) 42%,rgba(6,26,30,.34) 66%,rgba(6,26,30,0) 88%)"))

# why only Nutrioz
D.append(S("lt",
  '<div class="mid c"><div class="d2" style="max-width:46cqw;margin-bottom:2cqw">Kodėl nuo šiol — tik Nutrioz</div>'
  '<div class="cols" style="gap:4.4cqw">'
  '<div style="flex:1">'
  '<div class="tick"><b class="tl">01</b><span>Vitaminas jau ištirpęs. Nereikia ardyti tabletės, kad jį pasiektum.</span></div>'
  '<div class="tick"><b class="tl">02</b><span>0,06 ml vietoje 2 g — apie 33 kartus mažiau medžiagos per parą.</span></div>'
  '<div class="tick"><b class="tl">03</b><span>Nereikia vandens. Vadinasi, nereikia ir progos, kad prisimintum.</span></div>'
  '<div class="tick"><b class="tl">04</b><span>Viena tūbelė — apie 240 papurškimų, apie 8 mėnesiai.</span></div>'
  '</div><div style="flex:1">'
  '<div class="tick"><b class="tl">05</b><span>Tūbelė telpa į kišenę ir nesuyra kelionėje.</span></div>'
  '<div class="tick"><b class="tl">06</b><span>Dozė matuojama purkštuku, ne akimi ir ne dalijant tabletę.</span></div>'
  '<div class="tick"><b class="tl">07</b><span>Nėra ko užspringti — nei vaikui, nei senjorui.</span></div>'
  '<div class="tick"><b class="tl">08</b><span>Apie 0,19 $ už dieną prie 45 $ mažmeninės kainos.</span></div>'
  '</div></div>'
  '<div class="fn" style="margin-top:2.2cqw;max-width:76cqw">Maisto papildas nėra vaistas ir negydo ligų. Išvardyti punktai apibūdina vartojimo formą, '
  'ne klinikinį poveikį. Pilnas 33 problemų sąrašas — 06–08 puslapiuose.</div></div>',
  eb="Aštuonios priežastys"))

# 14 platform
D.append(S("lt",
  '<div class="mid" style="justify-content:space-between;padding-top:1.2cqw">'
  '<div class="d2">Viena platforma.<br>Penkios formulės.</div>'
  '<div class="prow" style="height:62%;margin-top:1.4cqw">'
  + "".join(f'<div class="pit"><img src="{I[k]}" alt=""><div class="n" style="color:{c}">{n}</div><div class="d">{ds}</div></div>'
            for k, n, c, ds in [
      ("d3", "D3", "#17879B", "Imuninė sistema,<br>kaulai, raumenys"),
      ("b12", "B12 / B9 / B6", "#7E42CC", "Energijos apykaita,<br>nervų sistema"),
      ("multi", "Multivitaminas", "#C87A2E", "10 vitaminų<br>vienoje formulėje"),
      ("energy", "Energy", "#C8262C", "Formulė su kofeinu<br>suaugusiesiems"),
      ("sleep", "Sleep", "#2466BA", "Melatonino formulė<br>prieš miegą")]) + '</div></div>',
  eb="Asortimentas"))

# 15 how to use — over the real macro
D.append(S("dkt",
  '<div class="mid"><div class="d2" style="max-width:38cqw">Keturi žingsniai.<br>Dvi sekundės.</div>'
  '<div class="cols" style="margin-top:2.2cqw;max-width:58cqw">'
  '<div class="kv"><div class="k tl">01</div><div class="l">Suplakti</div></div>'
  '<div class="kv"><div class="k tl">02</div><div class="l">Nukreipti į vidinę<br>žando pusę</div></div>'
  '<div class="kv"><div class="k tl">03</div><div class="l">Papurkšti pagal<br>etiketę</div></div>'
  '<div class="kv"><div class="k tl">04</div><div class="l">Neužgerti vandeniu</div></div></div></div>',
  eb="Kaip vartoti", bleed=R['spray_hero'], lift=True,
  veil="background:linear-gradient(90deg,rgba(6,26,30,.95) 0%,rgba(6,26,30,.86) 34%,rgba(6,26,30,.3) 58%,rgba(6,26,30,0) 76%)"))

# 16 contact
D.append(S("dkt",
  '<div class="mid c" style="align-items:flex-start;max-width:48cqw">'
  '<div class="d2">Nutrioz Molecular Spray®</div>'
  '<div class="bd lg" style="max-width:32cqw;margin-top:1.4cqw">Visą asortimentą, sudėtis ir etiketes rasite nutrioz.lt</div>'
  f'<img src="{I["qr"]}" alt="QR kodas i nutrioz.lt" style="width:9cqw;background:#fff;padding:.8cqw;margin-top:2cqw">'
  '<div class="bd" style="margin-top:1.2cqw">nutrioz.lt · info@nutrioz.com</div>'
  '<div class="fn" style="max-width:44cqw;margin-top:1.8cqw">Maisto papildas nėra visavertės ir subalansuotos mitybos pakaitalas. '
  'Neviršykite rekomenduojamos paros dozės. Dozė, amžius ir įspėjimai — tik pagal konkretaus produkto etiketę.</div></div>'
  '<div class="ph" style="left:56cqw;top:0;width:44cqw;height:100%"><img src="' + R['p_pair3'] + '" alt="Nutrioz komanda su produktais"></div>',
  eb="Kontaktai", pg=False, bg="#0A1416"))

html = ('<title>33 problemos, vienas sprendimas</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap">\n'
        '<style>%s</style>\n<div class="deck"><div class="dh"><b>Nutrioz <span>Oral Spray</span></b>'
        '<p>33 problemos · Katalogas · 2026</p></div>\n%s\n</div>') % (CSS, "\n".join(D))
open("nutrioz-katalogas-v5.html", "w", encoding="utf-8").write(html)
print("built %.2f MB, slides=%d, photos=%d" % (
    os.path.getsize("nutrioz-katalogas-v5.html") / 1024 / 1024, html.count('class="s '), len(R)))
