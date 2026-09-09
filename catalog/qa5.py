import asyncio, json, os
from playwright.async_api import async_playwright
HTML=open("nutrioz-katalogas-v5.html",encoding="utf-8").read()
async def main():
    os.makedirs("qa5", exist_ok=True)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1280,"height":900}, device_scale_factor=1.4)
        await pg.set_content(HTML, wait_until="networkidle")
        await pg.wait_for_timeout(2500)
        rep=await pg.evaluate("""() => {
          const out=[];
          document.querySelectorAll('.s').forEach((s,i)=>{
            const sr=s.getBoundingClientRect(); const iss=[];
            s.querySelectorAll('*').forEach(e=>{
              const r=e.getBoundingClientRect();
              if(r.width===0&&r.height===0) return;
              if(r.right>sr.right+1.5||r.left<sr.left-1.5||r.bottom>sr.bottom+1.5||r.top<sr.top-1.5){
                const t=(e.textContent||'').trim().slice(0,42);
                iss.push('OVERFLOW '+e.className+' :: '+t);
              }
            });
            s.querySelectorAll('img').forEach(im=>{
              if(!im.complete||im.naturalWidth===0) iss.push('BROKEN IMG '+im.className+' '+im.alt);
            });
            const mid=s.querySelector('.mid'), bot=s.querySelector('.bot');
            if(mid&&bot){const m=mid.getBoundingClientRect(),bo=bot.getBoundingClientRect();
              if(m.bottom>bo.top+1) iss.push('MID/FOOTER COLLISION '+(m.bottom-bo.top).toFixed(1)+'px');}
            out.push({slide:i+1, issues:[...new Set(iss)]});
          });
          return out;}""")
        bad=[r for r in rep if r["issues"]]
        print(json.dumps(bad, ensure_ascii=False, indent=1) if bad else "CLEAN: no overflow, no broken images, no collisions")
        for i,el in enumerate(await pg.query_selector_all(".s")):
            await el.screenshot(path="qa5/s%02d.png"%(i+1))
        await b.close()
asyncio.run(main())
