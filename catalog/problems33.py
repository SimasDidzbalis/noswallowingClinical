# 33 problemos su kitais papildais — ir ką Nutrioz su jomis daro.
# status: "X" = formatas problemą pašalina; "~" = sumažina, bet nepanaikina
P=[
 ("A","Rijimas ir fizinės kliūtys",[
  ("Tabletė per didelė nuryti","0,06 ml dulksna. Nieko nereikia ryti.","X"),
  ("Vėmimo refleksas nuo tabletės","Dozė lieka ant žando, į gerklę nepatenka.","X"),
  ("Disfagija — rijimo sutrikimas","Vartojimas nereikalauja rijimo veiksmo.","X"),
  ("Tabletė įstringa gerklėje","Skysta dulksna neturi kietos formos.","X"),
  ("Kapsulė prilimpa prie gomurio","Nėra apvalkalo, kuris galėtų prilipti.","X"),
  ("Reikia vandens, o jo ne visada yra","Vartojama neužgeriant.","X"),
  ("Negalima nuryti gulint","Purškiama bet kokioje padėtyje.","X"),
  ("Vyresni žmonės nesusitvarko su kietomis formomis","Vienas paspaudimas vietoj rijimo.","X"),
  ("Po operacijos kietos formos ribojamos","Skysta terpė be kietos formos.","~"),
  ("Sausa burna apsunkina rijimą","Dulksna pati sudrėkina gleivinę.","X"),
 ]),
 ("B","Dozė ir jos kontrolė",[
  ("Kapsulės perpus nepadalinsi","Dozė keičiama po vieną papurškimą.","X"),
  ("Rinkoje vyrauja 5000 TV megadozės","Vienas papurškimas — 1000 TV.","X"),
  ("Negali koreguoti dozės kas dieną","Šiandien vienas, rytoj du purškimai.","X"),
  ("Nežinai, kiek jau išgėrei","Purškimų skaičius fiksuotas ir skaičiuojamas.","~"),
  ("Vaikui reikia mažesnės dozės, o tabletė viena","Mažesnė dozė — mažiau purškimų.","X"),
 ]),
 ("C","Kas dar yra tabletėje",[
  ("2 g medžiagos, kad gautum 25 µg","0,06 ml — 33 kartus mažiau medžiagos.","X"),
  ("Rišikliai ir užpildai, kurių neprašei","Formulėje jų nėra.","~"),
  ("Želatinos kapsulės — netinka veganams","Purškiama formulė be želatinos.","X"),
  ("Dangos ir šelakas ant tabletės","Nėra jokios dangos.","X"),
  ("Cukrus guminukuose","Saldinama stevija, be cukraus.","X"),
  ("Guminukai kaista, sulimpa, keičia formą","Sandari tūbelė, skystis nesulimpa.","X"),
 ]),
 ("D","Įsisavinimas ir skrandis",[
  ("Riebaluose tirpiems vitaminams reikia riebalų su maistu","Formulėje jau yra riebalinė terpė.","~"),
  ("Įsisavinimas priklauso nuo tos dienos žarnyno būklės","Vartojimas prasideda burnoje, ne žarnyne.","~"),
  ("Skrandžio rūgštis veikia formulę prieš išsilaisvinimą","Veiklioji medžiaga jau skystoje terpėje.","~"),
  ("Vaistai (PSI, metforminas) keičia pasisavinimą","Kitas vartojimo kelias, bet sąveikas vertina gydytojas.","~"),
  ("Malabsorbcijos būklės","Purškiklis tirtas ir šios grupės pacientams (Satia, 2015).","~"),
 ]),
 ("E","Rutina, kelionė, atsargos",[
  ("Kelios pakuotės ir kelios tabletės per dieną","Viena tūbelė, vienas veiksmas.","X"),
  ("Reikia tablečių dėžutės","Tūbelė telpa kišenėje.","X"),
  ("Pamiršti, ar išgėrei","Vienas įprotis vietoj kelių.","~"),
  ("Buteliukai kelionėje užima vietą","13 cm tūbelė, be stiklo.","X"),
  ("Baigiasi po 30–60 dienų","240 papurškimų — apie 8 mėnesiai.","X"),
  ("Poskonis, atsirūgimas","Natūralus mėtų skonis, 0,06 ml.","X"),
  ("Pykinimas tuščiu skrandžiu","Nereikia nuryti 2 g medžiagos.","~"),
 ]),
]
if __name__=="__main__":
    n=sum(len(g[2]) for g in P)
    full=sum(1 for g in P for it in g[2] if it[2]=="X")
    print("problemų:",n," pilnai pašalina:",full," sumažina:",n-full)
    for code,name,items in P: print("  %s %-28s %d"%(code,name,len(items)))
