#!/usr/bin/env python3
"""Fetch a URL (or read a local HTML file) and extract the main article text.

Stdlib-only, for agents without a web-fetch tool. Heuristic extraction:
skips navigation/boilerplate tags, keeps paragraph-level blocks, drops
chunks that are mostly links.

Usage:
    python fetch_article.py <url-or-file> [--output FILE] [--max-chars N]

Exit codes: 0 ok, 1 fetch/parse failure, 2 page looks blocked or empty.
"""

import argparse
import re
import sys
import urllib.request
from html.parser import HTMLParser

SKIP_TAGS = {"script", "style", "noscript", "nav", "header", "footer", "aside",
             "form", "iframe", "svg", "button", "select", "template"}
BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "blockquote", "pre"}

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch(source: str) -> bytes:
    if re.match(r"^https?://", source):
        req = urllib.request.Request(source, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    with open(source, "rb") as f:
        return f.read()


def decode(raw: bytes) -> str:
    head = raw[:4096].decode("ascii", errors="ignore")
    m = re.search(r'charset=["\']?([\w-]+)', head, re.IGNORECASE)
    for enc in ([m.group(1)] if m else []) + ["utf-8", "gb18030"]:
        try:
            return raw.decode(enc)
        except (LookupError, UnicodeDecodeError):
            continue
    return raw.decode("utf-8", errors="replace")


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.og_title = ""
        self.blocks = []          # list of (tag, text, link_text_len)
        self._skip = 0            # depth inside SKIP_TAGS
        self._in_title = False
        self._cur_tag = None
        self._cur_text = []
        self._cur_link = 0
        self._in_link = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self._skip += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            d = dict(attrs)
            if d.get("property") == "og:title" and d.get("content"):
                self.og_title = d["content"].strip()
        elif tag == "a" and self._cur_tag:
            self._in_link = True
        elif tag in BLOCK_TAGS and not self._skip and not self._cur_tag:
            self._cur_tag, self._cur_text, self._cur_link = tag, [], 0
        elif tag == "br" and self._cur_tag:
            self._cur_text.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self._skip:
            self._skip -= 1
        elif tag == "title":
            self._in_title = False
        elif tag == "a":
            self._in_link = False
        elif tag == self._cur_tag:
            text = "".join(self._cur_text)
            self.blocks.append((tag, text, self._cur_link))
            self._cur_tag = None

    def handle_data(self, data):
        if self._skip:
            return
        if self._in_title:
            self.title += data
        if self._cur_tag:
            self._cur_text.append(data)
            if self._in_link:
                self._cur_link += len(data.strip())


def clean(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def extract(html: str):
    p = ArticleParser()
    p.feed(html)
    title = clean(p.title) or p.og_title
    out = []
    for tag, text, link_len in p.blocks:
        text = clean(text)
        if len(text) < 25:                      # too short to be article prose
            continue
        if link_len / max(len(text), 1) > 0.6:  # mostly a link list = boilerplate
            continue
        out.append(text)
    return title, out


def main():
    ap = argparse.ArgumentParser(description="Extract main article text from a URL or HTML file.")
    ap.add_argument("source", help="http(s) URL or local HTML file path")
    ap.add_argument("--output", help="write result to this file instead of stdout")
    ap.add_argument("--max-chars", type=int, default=20000,
                    help="truncate extracted text to this many chars (default 20000)")
    args = ap.parse_args()

    try:
        html = decode(fetch(args.source))
    except Exception as e:
        print(f"ERROR: could not fetch/read source: {e}", file=sys.stderr)
        sys.exit(1)

    title, blocks = extract(html)
    if not blocks:
        print("ERROR: no article text extracted (page may be blocked, JS-rendered, "
              "or paywalled). Ask the user to paste the text or a screenshot.",
              file=sys.stderr)
        sys.exit(2)

    body = "\n\n".join(blocks)
    truncated = len(body) > args.max_chars
    result = (f"TITLE: {title}\n\n{body[:args.max_chars]}"
              + ("\n\n[... truncated ...]" if truncated else ""))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
