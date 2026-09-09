import pymupdf, imgutil, os
JOBS=[
 ("drive/Nutrioz_Oral_Spray_Molecular_spray_macro_photo_3.jpg","spray_hero",1700),
 ("drive/Nutrioz_Oral_Spray_Molecular_spray_macro_photo_24.jpg","spray_wide",1700),
 ("drive/IMG_1293.jpg","p_hero",1200),
 ("drive/IMG_1308.jpg","p_pair",1200),
 ("drive/IMG_1301.jpg","p_gym",1100),
 ("drive/IMG_1296.jpg","p_hand",1100),
 ("drive/IMG_1275.jpg","p_duo",1200),
 ("drive/IMG_1291.jpg","p_stand",1000),
 ("drive/IMG_1310.jpg","p_pair2",1100),
 ("drive/IMG_1306.jpg","p_pair3",1100),
 ("drive/IMG_2565.jpg","life_juice",1200),
 ("drive/IMG_2572.jpg","life_salad",1300),
 ("drive/IMG_2573.jpg","life_table",1300),
 ("drive/IMG_2567.jpg","life_bowl",1300),
]
for src,name,mx in JOBS:
    p,rot=imgutil.load(src)
    w,h=(p.height,p.width) if rot in (90,270) else (p.width,p.height)
    f=min(1.0,mx/max(w,h))
    doc=pymupdf.open(); pg=doc.new_page(width=w*f,height=h*f)
    pg.insert_image(pg.rect,pixmap=p,rotate=(360-rot)%360)
    pm=pg.get_pixmap(dpi=72)
    dst="opt2/%s.jpg"%name
    pm.save(dst, jpg_quality=76)
    print(name, pm.width, pm.height, os.path.getsize(dst)//1024, "KB")

JOBS2=[
 ("drive/DR._Elena_Dudenaite_Nutrioz_Oral_Sray_Large.png.jpg","doctor",1100),
 ("drive/The_Best__Vitamin_D3__Nutrioz_Oral_Spray_in_old_hands.jpg","senior_hands",1500),
 ("drive/The_Best__Vitamin_D3__Nutrioz_Oral_Spray_in_old_hands_close.jpg","senior_close",1400),
]
for src,name,mx in JOBS2:
    p,rot=imgutil.load(src)
    w,h=(p.height,p.width) if rot in (90,270) else (p.width,p.height)
    f=min(1.0,mx/max(w,h))
    doc=pymupdf.open(); pg=doc.new_page(width=w*f,height=h*f)
    pg.insert_image(pg.rect,pixmap=p,rotate=(360-rot)%360)
    pm=pg.get_pixmap(dpi=72); dst="opt2/%s.jpg"%name; pm.save(dst, jpg_quality=78)
    print(name, pm.width, pm.height, os.path.getsize(dst)//1024,"KB")
