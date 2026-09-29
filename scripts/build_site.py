#!/usr/bin/env python3

import argparse
import re
import shutil
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


ROOT = Path(__file__).resolve().parents[1]
SIDEBAR = ROOT / "_Sidebar.md"
LANGUAGES = (("ar", "العربية"), ("fr", "Français"), ("en", "English"))


class PageLinkTreeprocessor(Treeprocessor):
    def __init__(self, md, page_links):
        super().__init__(md)
        self.page_links = page_links

    def run(self, root):
        for element in root.iter("a"):
            href = element.get("href", "")
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue

            target = parsed.path.removeprefix("./").removesuffix(".md")
            if target in self.page_links:
                element.set(
                    "href",
                    urlunsplit(parsed._replace(path=self.page_links[target])),
                )


class PageLinkExtension(Extension):
    def __init__(self, page_links):
        super().__init__()
        self.page_links = page_links

    def extendMarkdown(self, md):
        md.treeprocessors.register(
            PageLinkTreeprocessor(md, self.page_links), "page_links", 15
        )


def page_slugs():
    links = re.findall(r"\]\(([^)]+)\)", SIDEBAR.read_text(encoding="utf-8"))
    slugs = [link for link in links if not link.startswith(("http://", "https://"))]
    if not slugs:
        raise RuntimeError("No local pages were found in _Sidebar.md")

    missing = [slug for slug in slugs if not (ROOT / f"{slug}.md").is_file()]
    if missing:
        raise RuntimeError(f"Sidebar pages are missing: {', '.join(missing)}")
    return slugs


def render_markdown(source, page_links):
    return markdown.markdown(
        source,
        extensions=["fenced_code", "tables", "sane_lists", PageLinkExtension(page_links)],
        output_format="html5",
    )


def page_language(slug):
    if slug.endswith("-ar"):
        return "ar"
    if slug.endswith("-fr"):
        return "fr"
    return "en"


def language_links(slug, slugs, page_links):
    language = page_language(slug)
    base = slug.removesuffix("-ar").removesuffix("-fr")
    links = []
    for code, label in LANGUAGES:
        candidate = base if code == "en" else f"{base}-{code}"
        if candidate not in slugs:
            candidate = {"ar": "Home-ar", "fr": "Home-fr", "en": "Home"}[code]
        current = ' aria-current="page"' if code == language else ""
        links.append(
            f'<a lang="{code}" href="{escape(page_links[candidate])}"{current}>'
            f"{label}</a>"
        )
    return "\n".join(links)


def page_title(source, fallback):
    match = re.search(r"^#\s+(.+)$", source, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def render_page(slug, slugs, page_links, sidebar_html):
    source = (ROOT / f"{slug}.md").read_text(encoding="utf-8")
    language = page_language(slug)
    direction = "rtl" if language == "ar" else "ltr"
    title = page_title(source, slug)
    body = render_markdown(source, page_links)
    switcher = language_links(slug, slugs, page_links)

    return f'''<!doctype html>
<html lang="{language}" dir="{direction}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Community troubleshooting notes for WebEtu 2.5.0 on Android">
  <title>{escape(title)} | WebEtu 2.5.0</title>
  <style>
    :root {{ color-scheme: light; --ink: #172a35; --muted: #52646c; --paper: #f1f5f4; --surface: #fff; --line: #d4dfdc; --accent: #087f70; --alert: #9c352b; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--paper); color: var(--ink); font-family: "Noto Sans Arabic", "Noto Sans", system-ui, sans-serif; line-height: 1.65; }}
    a {{ color: #006b61; text-underline-offset: .16em; }}
    a:hover {{ color: #9c352b; }}
    header {{ background: var(--ink); color: #fff; border-bottom: 4px solid var(--accent); }}
    .header-inner {{ max-width: 1240px; margin: auto; padding: 1rem 1.4rem; display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap; }}
    .brand {{ color: #fff; font-weight: 700; text-decoration: none; }}
    .languages {{ display: flex; gap: .9rem; flex-wrap: wrap; }}
    .languages a {{ color: #fff; }}
    .languages [aria-current="page"] {{ text-decoration-thickness: 3px; font-weight: 700; }}
    .layout {{ max-width: 1240px; margin: 1.5rem auto; padding: 0 1.4rem; display: grid; grid-template-columns: minmax(220px, 285px) minmax(0, 1fr); gap: 1.4rem; align-items: start; }}
    aside, article {{ background: var(--surface); border: 1px solid var(--line); border-radius: 4px; }}
    aside {{ padding: 1rem; position: sticky; top: 1rem; max-height: calc(100vh - 2rem); overflow: auto; }}
    aside h2 {{ font-size: 1rem; margin: .25rem 0 .6rem; }}
    aside h2:not(:first-child) {{ margin-top: 1.25rem; border-top: 1px solid var(--line); padding-top: .8rem; }}
    aside ul {{ list-style: none; margin: 0; padding-inline-start: 0; }}
    aside li {{ margin: .25rem 0; }}
    aside a {{ display: block; padding: .2rem .35rem; border-radius: 2px; }}
    aside a:hover {{ background: #e6f1ee; }}
    article {{ min-width: 0; padding: clamp(1rem, 3vw, 2.25rem); }}
    article h1 {{ margin-top: 0; font-size: clamp(1.55rem, 2.4vw, 2.1rem); line-height: 1.25; }}
    article h2 {{ margin-top: 1.8em; font-size: 1.3rem; border-bottom: 1px solid var(--line); padding-bottom: .3rem; }}
    article h3 {{ font-size: 1.08rem; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Consolas, monospace; direction: ltr; unicode-bidi: isolate; }}
    pre {{ overflow-x: auto; padding: 1rem; background: #182c35; color: #f5faf8; border-radius: 3px; direction: ltr; text-align: left; }}
    blockquote {{ border-inline-start: 4px solid var(--alert); margin-inline: 0; padding-inline-start: 1rem; color: var(--muted); }}
    @media (max-width: 760px) {{ .layout {{ grid-template-columns: 1fr; }} aside {{ position: static; max-height: none; }} .header-inner {{ align-items: flex-start; }} }}
  </style>
</head>
<body>
  <header><div class="header-inner">
    <a class="brand" href="index.html">WebEtu 2.5.0</a>
    <nav class="languages" aria-label="Language">{switcher}</nav>
  </div></header>
  <div class="layout">
    <aside aria-label="All pages">{sidebar_html}</aside>
    <article>{body}</article>
  </div>
</body>
</html>
'''


def build(output):
    slugs = page_slugs()
    page_links = {slug: f"{slug}.html" for slug in slugs}
    sidebar_source = SIDEBAR.read_text(encoding="utf-8")
    sidebar_html = render_markdown(sidebar_source, page_links)

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    for slug in slugs:
        page = render_page(slug, slugs, page_links, sidebar_html)
        (output / f"{slug}.html").write_text(page, encoding="utf-8")
        if slug == "Home-ar":
            (output / "index.html").write_text(page, encoding="utf-8")

    (output / ".nojekyll").touch()


def main():
    parser = argparse.ArgumentParser(description="Build the WebEtu support site")
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()