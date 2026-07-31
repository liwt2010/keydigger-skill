# HTML Output Guide

When the user asks for HTML output (图文并茂 / 网页 / 可视化页面 / 报告页), or when a
rich visual page clearly serves the request, produce a single self-contained HTML file
instead of (or in addition to) markdown.

Copy `assets/template.html` and fill it in. This guide explains the design system so you
can adapt it per article without reading the whole template.

## When to use HTML

- User explicitly asks for HTML / 网页 / 图文并茂 / 好看的报告.
- The content has a structure worth visualizing (mindmap, timeline, stakeholder map).
- The output will be shared or opened in a browser.

When in doubt, prefer markdown + mermaid for chat contexts, HTML for files.

## File conventions

- Name: `keydigger-<slug>.html` in the working directory (e.g. `keydigger-politburo-2026.html`).
- Self-contained: inline all CSS; load mermaid from CDN with a `<noscript>`-safe fallback
  (the text sections must remain readable without JS).
- Encoding: UTF-8, `lang="zh-CN"` or the output language.

## Design system

The template defines these blocks. Use them in this order:

1. **Header**: gradient background + title + source meta + genre badge.
2. **Executive summary bar**: 4 KPI-style cards (`.exec-item`), each a key number/phrase
   + one-line label. This is the 3-second scan.
3. **Source quote** (`<details>`): collapsible original text excerpt, keeps output clean.
4. **TL;DR** (`.tldr`): 1-2 sentences, the single most important takeaway, key phrase in
   contrast color.
5. **通俗解读**: plain-language section; use the glossary grid for jargon terms.
6. **核心观点**: mermaid `mindmap` + numbered viewpoint list (`.viewpoint-list`).
7. **深层解读**: mermaid diagram (flowchart/quadrantChart/timeline as needed) + insight
   cards (`.insight-list`), each tagged with its inference basis.
8. **事实与观点**: `.fact-table` with 分类 | 内容 | 可信度 columns.
9. **对不同读者的意义**: `.stake-grid` with 4 colored audience cards.

## Genre theming

Change the accent color to match the source genre — this is a deliberate signal:

| Genre | Accent | Example |
|---|---|---|
| 官方通稿 / 政策 | green (`#14532d`) | 党外人士座谈会 |
| 分析师观点 / 预测 | purple (`#7c4dff`) | 宏观分析师解读 |
| 科技 / 产业新闻 | blue (`#0f3460`) | AI 公司融资 |
| 财经 / 市场 | indigo (`#1e3a8a`) | 市场分析 |
| 默认 / 通用 | slate (`#334155`) | — |

Change the CSS variables (`--accent`, `--accent-dark`, `--accent-soft`) rather than
hunting individual rules.

## Emphasis rules (from SKILL.md)

- At most 1-2 mermaid diagrams per page; always pair with text.
- Highlight only the highest-signal sentence per section (`.highlight`).
- Every inference carries a tag: 基于文中信息推断 (blue), 结合外部背景推测 (amber),
  可核实事实 (green), 待跟踪 (red).
- Colors are never the only signal: keep labels, bold, and layout working in grayscale.
- Genre badge in the header tells the reader how much to trust the content.

## Responsive rules

- `max-width: 860px` content column, 20px gutters.
- Grids collapse to one column under 600px.
- Mermaid containers scroll horizontally (`overflow-x: auto`) instead of shrinking text.
- Never use viewport-scaled font sizes.

## Fallback behavior

- If the environment cannot render mermaid (offline, no JS), the page still works:
  every section has full text, and `.mermaid-wrap` shows the diagram source as text.
- If user only asked for markdown, do not silently produce HTML. If they asked for
  HTML, do not return markdown-only.

## 历史脉络与新变化 section (news & policy)

For news and policy analysis, add this section after 通俗解读 and before 核心观点.
It operationalizes step 3 of SKILL.md (compare against history):

- One intro line naming the history source: 官方档案 / 既有知识 / 本对话前文.
- A `.compare-table` with 4 columns: 维度 | 过往 | 本次 | 新变化.
- End with a `.highlight` box naming the single most important delta.

```html
<table class="compare-table">
  <tr><th>维度</th><th>过往</th><th>本次</th><th>新变化</th></tr>
  <tr><td><strong>政策基调</strong></td><td>...</td><td>...</td><td class="delta">...</td></tr>
</table>
```

Rules: never invent history — label the source and say 未知 when unknown; the
`delta` column carries the analysis value, so it should name the meaning, not just
the difference; continuity rows are allowed and worth one line each.
