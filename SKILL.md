---
name: keydigger
description: Interpret news, articles, and books into plain, easy-to-understand language, then dig out the core viewpoints, framework, and the hidden implications/directions behind them (新闻解读 / 文章解读 / 书籍解读 / 拆书 / 通俗易懂 / 核心观点 / 核心框架 / 隐含启示). Use whenever the user shares a news link, article URL, pasted text, book or document file (PDF/EPUB/TXT/MD), or screenshot/image of written content and asks to 解读, explain, summarize, analyze, digest, break down, or asks what it means, what the core framework/arguments are, or what it implies for the future (说明了什么 / 意味着什么 / 怎么看 / 深度分析 / 这本书讲了什么 / 核心逻辑). Works with links, raw text, books, files, and images, in any language.
---

# Keydigger

## Overview

Keydigger turns a piece of news or an article into an interpretation a smart outsider can
understand in minutes: what it says in plain language, what its core viewpoints are, and
what it quietly implies about the future. The value is not summarizing; it is digging.

## Workflow

### 1. Acquire the content

Match the input type:

- **URL / link**: Fetch with the best available web tool (web search, browser, fetch MCP).
  If no web tool exists, run `scripts/fetch_article.py <url>` (Python, stdlib only) to
  extract the main text. If the page is paywalled, blocked, or requires login, say so
  honestly and ask the user to paste the text or provide a screenshot. Never invent
  content for a page you could not read.
- **Pasted text**: Use it directly.
- **Image / screenshot**: Read the text with vision. If parts are illegible, interpret
  what is readable and note the gap.
- **File (PDF, DOCX, etc.)**: Extract the text with the appropriate tool first.
- **Book / long document (EPUB, TXT, MD, long PDF)**: Do NOT try to read it front to
  back into context. Run `scripts/extract_book.py <file> --toc` to get the chapter
  map, then follow the long-form workflow in `references/book-analysis.md`.

Read the FULL text before interpreting. If the source is truncated, say the reading is
based on partial content.

### 2. Understand before judging

Identify: What happened? Who is involved? What is the author trying to convince the
reader of? Note genre (news report, opinion piece, press release, research, rumor) —
genre changes how much trust the claims deserve.

### 3. Dig for viewpoints and implications

**Books and long documents**: use `references/book-analysis.md` instead — it covers
coverage planning (what to read fully vs. sample), framework extraction, argument
mapping, evidence inventory, and the book output template.

**News and articles**: 
Read `references/analysis-framework.md` and apply its lenses: core viewpoints, why-now,
who-benefits, second-order effects, trend signals, what-is-not-said. The hidden
implications are the heart of this skill — never skip them, but always label them as
inference, not fact. For calibration, `references/examples.md` shows a complete model
interpretation.

### 4. Write the interpretation

Use the output format below. Write in the user's language (default: the language of
their request, otherwise the language of the source).

## Output Format

For books, use the book template in `references/book-analysis.md` instead.

Default structure (adapt section names to the output language):

```markdown
## 一句话看懂
1-2 sentences: what happened and why it matters. No jargon.

## 通俗解读
Plain-language retelling: background a layperson needs, then what the article is
actually saying. Explain every technical term in one line; use a concrete analogy
when it helps. Assume a smart reader outside the field.

## 核心观点
Numbered list of the 2-5 viewpoints the article really rests on, each with one line
of support from the text. Distinguish the author's claims from reported facts.

## 深层解读与隐含启示
The dig: why this is happening now, who benefits / who is threatened, second-order
effects, what trend or direction it signals, what to watch next. Mark each insight
with its basis: (基于文中信息推断) or (结合外部背景推测).

## 事实与观点
What is verified fact, what is the author's opinion or framing, what is unverified
or single-sourced. Note the source's likely stance if relevant.

## 对不同读者的意义 (optional)
Concrete implications or directions for the audiences this news touches
(e.g. 从业者 / 投资者 / 普通消费者). Include when the content clearly has them.
```

Scale down gracefully: for a short or simple piece, merge sections rather than padding.
Scale up for long reports: keep the skeleton, deepen each section.

## Principles

- **Plain language is mandatory.** If a sentence needs domain knowledge to parse,
  rewrite it. Test: would a curious high-schooler follow it?
- **Separate fact from inference.** Article facts, author opinions, and your own
  extrapolations must be visibly different. Implication sections are inference —
  label their basis.
- **Stay grounded in the source.** Do not add claims the source does not support.
  When outside context genuinely helps (background, a trend), flag it as external.
- **No fake certainty.** Use confidence language: 可能 / 大概率 / 值得观察. A wrong
  prediction stated confidently is worse than no prediction.
- **Respect paywalls and gaps.** Partial content = partial interpretation, stated
  upfront.
- **Keep the user's stake in mind.** If the user says who they are (investor,
  student, founder), weight the implications toward their angle.

## References

- `references/analysis-framework.md` — the digging lenses and per-domain angles
  (tech, finance, policy, company, science). Read before step 3 on any non-trivial
  piece.
- `references/book-analysis.md` — long-form workflow for books and lengthy reports:
  coverage planning, framework and argument extraction, book output template.
- `references/examples.md` — a complete worked example showing target depth and tone.

## Scripts

- `scripts/fetch_article.py` — fetch a URL and extract the main article text
  (stdlib-only Python). Usage: `python scripts/fetch_article.py <url> [--output file]`.
  Also accepts a local HTML file path.
- `scripts/extract_book.py` — extract chapter map and text from EPUB/TXT/MD books
  (stdlib-only Python). Usage: `python scripts/extract_book.py <file> [--toc]`
  `[--chapter N] [--output file]`. For PDFs use the environment's own PDF tools.
