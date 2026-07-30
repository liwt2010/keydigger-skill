#!/usr/bin/env python3
"""Extract chapter map and text from EPUB/TXT/MD books. Stdlib-only.

Usage:
    python extract_book.py book.epub --toc            chapter list + char counts
    python extract_book.py book.epub                  full text, chapter markers
    python extract_book.py book.epub --chapter 3      single chapter (1-based)
    python extract_book.py book.txt -o out.txt

Exit codes: 0 ok, 1 read/parse failure, 2 unsupported format.
"""

import argparse
import re
import sys
import zipfile
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

HEADING_RE = re.compile(
    r"^\s*(#{1,6}\s+\S.*|第[0-9零一二三四五六七八九十百千]+[章节部篇卷回].*|"
    r"(Chapter|CHAPTER|Part|PART)\s+\w+.*)$")


class TextExtractor(HTMLParser):
    """Collect visible text and the first heading from an HTML document."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.first_heading = ""
        self._skip = 0
        self._heading_tag = None
        self._heading_text = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self._skip += 1
        elif tag in ("h1", "h2", "h3") and not self._skip:
            self._heading_tag = tag
            self._heading_text = []
        elif tag in ("p", "div", "br", "li", "blockquote", "tr", "section"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self._skip:
            self._skip -= 1
        elif tag == self._heading_tag:
            if not self.first_heading:
                self.first_heading = "".join(self._heading_text).strip()
            self._heading_tag = None

    def handle_data(self, data):
        if self._skip:
            return
        self.parts.append(data)
        if self._heading_tag:
            self._heading_text.append(data)


def localname(tag):
    return tag.rsplit("}", 1)[-1]


def epub_chapters(path):
    """Yield (title, text) per spine item, in reading order."""
    with zipfile.ZipFile(path) as z:
        container = ET.fromstring(z.read("META-INF/container.xml"))
        opf_path = next(e.get("full-path") for e in container.iter()
                        if localname(e.tag) == "rootfile")
        opf_dir = opf_path.rsplit("/", 1)[0] + "/" if "/" in opf_path else ""
        opf = ET.fromstring(z.read(opf_path))

        manifest, spine = {}, []
        for e in opf.iter():
            name = localname(e.tag)
            if name == "item":
                manifest[e.get("id")] = e.get("href")
            elif name == "itemref":
                spine.append(e.get("idref"))

        for idref in spine:
            href = manifest.get(idref)
            if not href:
                continue
            try:
                raw = z.read(opf_dir + href)
            except KeyError:
                continue
            html = raw.decode("utf-8", errors="replace")
            ex = TextExtractor()
            ex.feed(html)
            text = re.sub(r"\n{3,}", "\n\n",
                          re.sub(r"[ \t]+", " ", "".join(ex.parts))).strip()
            title = ex.first_heading or href.rsplit("/", 1)[-1]
            if text:
                yield title, text


def text_chapters(path):
    """Split a TXT/MD file into (title, text) by heading lines."""
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read().lstrip("\ufeff")
    lines = text.splitlines()
    chapters, title, buf = [], "正文", []
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            if buf:
                chapters.append((title, "\n".join(buf).strip()))
            title = m.group(1).lstrip("#").strip()
            buf = []
        else:
            buf.append(line)
    if buf:
        chapters.append((title, "\n".join(buf).strip()))
    return [(t, b) for t, b in chapters if b]


def load(path):
    low = path.lower()
    if low.endswith(".epub"):
        return list(epub_chapters(path))
    if low.endswith((".txt", ".md")):
        return text_chapters(path)
    print("ERROR: unsupported format. Use EPUB/TXT/MD; extract PDFs to text first "
          "with your environment's PDF tools.", file=sys.stderr)
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser(description="Extract chapters from EPUB/TXT/MD books.")
    ap.add_argument("source", help="path to the book file")
    ap.add_argument("--toc", action="store_true", help="print chapter map only")
    ap.add_argument("--chapter", type=int, help="output only this 1-based chapter")
    ap.add_argument("-o", "--output", help="write to file instead of stdout")
    args = ap.parse_args()

    try:
        chapters = load(args.source)
    except SystemExit:
        raise
    except Exception as e:
        print(f"ERROR: could not read book: {e}", file=sys.stderr)
        sys.exit(1)

    if not chapters:
        print("ERROR: no text extracted from this book.", file=sys.stderr)
        sys.exit(1)

    if args.toc:
        total = sum(len(t) for _, t in chapters)
        out = [f"CHAPTERS: {len(chapters)}  TOTAL_CHARS: {total}", ""]
        out += [f"[{i}] {t}  ({len(b)} chars)"
                for i, (t, b) in enumerate(chapters, 1)]
        result = "\n".join(out)
    elif args.chapter:
        if not 1 <= args.chapter <= len(chapters):
            print(f"ERROR: chapter must be 1..{len(chapters)}", file=sys.stderr)
            sys.exit(1)
        t, b = chapters[args.chapter - 1]
        result = f"# [{args.chapter}] {t}\n\n{b}"
    else:
        result = "\n\n".join(f"# [{i}] {t}\n\n{b}"
                             for i, (t, b) in enumerate(chapters, 1))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
