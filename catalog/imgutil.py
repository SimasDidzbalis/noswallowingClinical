import pymupdf, struct, os

def exif_orientation(path):
    try:
        d=open(path,'rb').read(200000)
    except: return 1
    i=2
    while i < len(d)-4:
        if d[i]!=0xFF: return 1
        m=d[i+1]; ln=struct.unpack('>H', d[i+2:i+4])[0]
        if m==0xE1 and d[i+4:i+10]==b'Exif\x00\x00':
            t=d[i+10:i+2+ln]
            if len(t)<8: return 1
            be = t[:2]==b'MM'
            u=lambda o,n: int.from_bytes(t[o:o+n],'big' if be else 'little')
            off=u(4,4)
            if off+2>len(t): return 1
            cnt=u(off,2)
            for k in range(cnt):
                e=off+2+k*12
                if e+12>len(t): break
                if u(e,2)==0x0112: return u(e+8,2) or 1
            return 1
        if m in (0xD8,0xD9,0xDA): return 1
        i += 2+ln
    return 1

ROT={1:0,3:180,6:90,8:270}

def load(path):
    """Return (pixmap, rotation_degrees_clockwise)."""
    p=pymupdf.Pixmap(path)
    if p.alpha: p=pymupdf.Pixmap(p,0)
    return p, ROT.get(exif_orientation(path),0)

def render(path, dst, maxdim=1600, quality=None):
    p,rot = load(path)
    w,h = (p.height,p.width) if rot in (90,270) else (p.width,p.height)
    f=min(1.0, maxdim/max(w,h))
    doc=pymupdf.open(); pg=doc.new_page(width=w*f, height=h*f)
    pg.insert_image(pg.rect, pixmap=p, rotate=(360-rot)%360)
    pg.get_pixmap(dpi=72).save(dst)
    return dst
