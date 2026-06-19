#!/usr/bin/env python3
"""Render a proposal HTML file to a 2-page A4 PDF.

Usage:
    python3 render.py path/to/proposal.html [output.pdf]

Tries Chromium (Playwright) first for highest fidelity, falls back to WeasyPrint.
If no output path is given, writes alongside the HTML with a YYYY-MM-DD suffix.
"""
import sys, os, datetime, pathlib

def out_path(html, given):
    if given:
        return given
    stem = pathlib.Path(html).with_suffix("")
    today = datetime.date.today().isoformat()
    return f"{stem}-{today}.pdf"

def render_chromium(html, pdf):
    from playwright.sync_api import sync_playwright
    uri = pathlib.Path(html).resolve().as_uri()
    # Allow an explicit binary via env (useful in restricted sandboxes).
    exe = os.environ.get("CHROMIUM_PATH")
    with sync_playwright() as p:
        launch = {"args": ["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"]}
        if exe:
            launch["executable_path"] = exe
        b = p.chromium.launch(**launch)
        pg = b.new_page()
        pg.goto(uri, wait_until="networkidle")
        pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True)
        b.close()

def render_weasyprint(html, pdf):
    from weasyprint import HTML
    HTML(html).write_pdf(pdf)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    html = sys.argv[1]
    pdf = out_path(html, sys.argv[2] if len(sys.argv) > 2 else None)
    try:
        render_chromium(html, pdf)
        print(f"[chromium] wrote {pdf}")
    except Exception as e:
        print(f"[chromium unavailable: {e}] falling back to WeasyPrint")
        render_weasyprint(html, pdf)
        print(f"[weasyprint] wrote {pdf}")

if __name__ == "__main__":
    main()
