# Book & Long-Form Analysis

Workflow for books, long reports, and other documents too long to read front to back.
The goal is the same as short-form — dig, don't summarize — but the unit of analysis
changes: a book's value is its framework, logic chain, and evidence system.

Contents:
1. Honesty about coverage
2. Step A: map the book
3. Step B: plan the reading
4. Step C: dig (five lenses for books)
5. Book output template

## 1. Honesty About Coverage

Never imply you read more than you did. State coverage in one line at the top of the
output: 全书精读 / 骨架+重点章节精读 / 仅目录与首尾章. A skeleton-based reading is
legitimate for a first pass — pretending it is a full reading is not.

## 2. Step A: Map the Book

Get the chapter map before reading anything in depth:

```bash
python scripts/extract_book.py book.epub --toc          # chapter list + char counts
python scripts/extract_book.py book.epub -o book.txt    # full text with chapter markers
python scripts/extract_book.py book.epub --chapter 3    # one chapter only
```

Supports EPUB/TXT/MD. For PDF, extract text with the environment's PDF tools first,
then treat it as TXT. If the user only names a book without providing a file, ask for
the file or proceed from your own knowledge of the book — and say which you did.

## 3. Step B: Plan the Reading

Match effort to book size and user intent:

- **Short (< ~40k chars)**: read fully.
- **Long, user wants a quick map**: read table of contents + preface/intro +
  conclusion + each chapter's opening and closing sections. Then deep-read the 1-3
  chapters that carry the core argument.
- **Long, user wants depth**: read fully, chapter by chapter, keeping running notes
  per chapter (claim, reasoning, evidence, one-line takeaway).

Prefaces and conclusions punch above their weight: authors state their thesis and
their intended contribution there. Read them even in the fastest pass.

## 4. Step C: Dig — Five Lenses for Books

### Lens 1: The core question
What question is the book trying to answer? One sentence. If you cannot state it,
you have not found the book's center. Beware books whose real question differs from
their marketed one.

### Lens 2: The framework
The author's mental model: key concepts, distinctions, and how they connect
(e.g. "System 1 vs System 2"). Render it as a compact map — a short indented list or
a mermaid diagram if the structure is genuinely relational. This is usually the
book's most transferable asset.

### Lens 3: The logic chain
How the argument flows: premises -> reasoning -> conclusions. Note load-bearing
steps — the claims the whole book collapses without. Check for jumps: steps where
the author asserts rather than demonstrates.

### Lens 4: The evidence inventory
What kinds of support does the author actually use — data, experiments, case studies,
anecdotes, authority quotes, thought experiments? Assess quality: representative or
cherry-picked? Replicable or one-off? Current or dated? A book heavy on anecdotes
should be labeled as such.

### Lens 5: Assumptions, blind spots, and implications
What must be true for the argument to hold? What does the author ignore ( opposing
evidence, contexts where the framework breaks, who benefits from this narrative)?
Then the keydigger move: what does this framework imply for the reader's decisions,
and what is it worth watching in the real world?

## 5. Book Output Template

```markdown
## 一句话看懂
The book's core question and its answer in 1-2 plain sentences.

## 阅读覆盖说明
One line: what was read (全书精读 / 骨架+第X、Y章精读), and source (用户提供的文件 /
基于模型已有知识).

## 全书框架
The author's mental model as a compact structure map. Explain each concept in one
plain line. Use a diagram only if relations matter.

## 核心论点与逻辑链
3-7 core arguments, each: 论点 -> 作者如何论证 -> 依赖的前提. Mark the load-bearing
steps and any logical jumps.

## 关键论据
The evidence that matters most, typed (数据 / 实验 / 案例 / 轶事 / 权威背书), with a
quality note each (代表性 / 可复现性 / 时效性).

## 隐含启示与批判性思考
Assumptions the book silently makes; blind spots and counterexamples; what the
framework implies for practice; where it likely stops working. Label inference.

## 通俗解读 (optional, for dense books)
The hardest 1-2 ideas re-explained with everyday analogies.

## 对不同读者的意义 (optional)
Who benefits most from this book; what to do differently after reading; what to
read next if the topic matters.
```

Scale to the request: "快速挖框架" = 一句话看懂 + 全书框架 + 核心论点, skip the rest.
Full 拆书 = whole template.
