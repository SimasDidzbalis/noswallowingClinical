import asyncio, os
from playwright.async_api import async_playwright
HTML=open("nutrioz-katalogas-v5.html",encoding="utf-8").read()
PRINT="""<style>
@page{size:1600px 900px;margin:0}
body{background:#fff}
.deck{max-width:none;margin:0;padding:0;gap:0}
.dh{display:none}
.s{width:1600px;height:900px;aspect-ratio:auto;break-after:page;page-break-after:always}
.s:last-child{break-after:auto;page-break-after:auto}
</style>"""
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",args=["--no-sandbox"])
        pg=await b.new_page()
        await pg.set_content(HTML+PRINT, wait_until="networkidle")
        await pg.wait_for_timeout(2500)
        await pg.pdf(path="Nutrioz-katalogas-2026-v5.pdf", width="1600px", height="900px",
                     print_background=True, prefer_css_page_size=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
        await b.close()
asyncio.run(main())
print("%.2f MB"%(os.path.getsize("Nutrioz-katalogas-2026-v5.pdf")/1024/1024))
