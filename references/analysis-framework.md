# Analysis Framework

The digging toolkit for step 3 of the workflow. Use it to move from "what the article
says" to "what the article means and implies."

Contents:
0. Historical context and what changed (mandatory for news/policy)
1. Finding the core viewpoints
2. Six lenses for hidden implications
3. Domain-specific angles
4. Calibration and confidence
5. Fact / opinion / speculation checklist

## 0. Historical Context and What Changed (News & Policy Analysis)

For news reports and policy articles, one step comes before the lenses: place the
current piece in its own history. A statement means little until you know what it
replaces. Always do this for recurring topics — policy meetings, market cycles,
company updates, industry milestones.

### Step A: Reconstruct the history

Summarize what is known about the issue before this article: prior statements,
events, policies, numbers, and outcomes. Sources in priority order:

- Earlier articles or materials the user provided in this conversation.
- Official archives and the outlet's own prior coverage (use a search tool when
  available; do not browse blindly — one focused query for the specific issue).
- Your own knowledge of the topic — and label it as such (基于既有知识).

If you genuinely do not know the history, say so honestly: do not invent a timeline.
Two well-documented prior data points beat a plausible but fabricated trend.

### Step B: Compare against the history

Build a delta table: 维度 | 过往情况 | 本次情况 | 变化. Check at least these
dimensions:

- **措辞变化**: New terms that appear (e.g. "破除内卷", "增量政策"); familiar terms
  that disappear. Each is a deliberate choice.
- **排序变化**: What moved up or down the list — priority shifts are policy signals.
- **数字变化**: Targets, tools, amounts, deadlines. Exact numbers matter (e.g. 8000亿,
  降息10bp).
- **时间变化**: Timing and duration — earlier or later than usual, extended or cut
  short.
- **主体变化**: Who is involved, who is addressed, who is missing.
- **基调变化**: 稳中求进 vs 持续发力适时加力; defensive vs offensive framing.
- **新增/删除**: Policy items added or dropped outright.

### Step C: State the deltas

The output of this step is a short "本次新变化" list: 2-4 concrete differences with
their likely meaning. Continuity is also a finding — "与去年表述基本一致" tells the
reader the policy is holding course. Put this in the output's 历史脉络与新变化 section.

Example (from this skill's own tests):

| 维度 | 2025-07 党外座谈会 | 2026-07 政治局会议 | 变化 |
|---|---|---|---|
| 政策基调 | 保持连续性稳定性，增强灵活性预见性 | 更加积极 + 适度宽松 + 及时谋划增量政策 | 从"连续性"转向"加码" |
| 核心任务 | 四个稳 + 破除内卷 | 扩大内需 + 人工智能+ + 防风险 | 科技产业权重上升 |
| 新提法 | 数据要素统一大市场 | 智能经济新形态、人工智能治理体系 | 新增长极明确 |

_(基于本技能对话中两篇通稿的对比；对外输出时应标注历史信息来源)_

## 1. Finding the Core Viewpoints

A core viewpoint is a claim the article would collapse without. To find them:

- **Ask what the author wants the reader to believe or do.** Strip anecdotes, quotes,
  and data decoration; what remains standing is the skeleton.
- **Separate headline from substance.** Headlines oversell. If the body supports less
  than the title promises, say so — that gap is itself a finding.
- **Distinguish load-bearing claims from support.** "Revenue grew 40%" is support;
  "the company has escaped its growth ceiling" is a viewpoint.
- **Note the genre.** News reports bury the lead in facts; opinion pieces state it;
  press releases hide it behind praise. A press release's core viewpoint is usually
  "we want you to think X about us."
- **2-5 viewpoints is the right range.** More means you are listing details, not
  digging.

## 2. Six Lenses for Hidden Implications

Run the article through each lens. Not every lens fires every time — report the ones
that yield something real, never force all six.

### Lens 1: Why now
Why is this happening (or being published) at this moment? News is often the visible
tip of a process that started months earlier. A product launch timed before a rival's
event, a policy after a public incident, a study released during a funding round —
timing is rarely neutral.

### Lens 2: Who benefits, who is threatened (cui bono)
Map the stakeholders: companies, industries, regulators, workers, consumers,
investors. For each, ask: does this make their position stronger or weaker? The
party pushing the narrative is often the beneficiary — consider who fed the story
to the press.

### Lens 3: Second-order effects
If the article's claims are true, what happens next that the article does not
mention? Cheaper X -> business models built on expensive X break -> jobs and prices
shift downstream. One or two hops of honest reasoning, clearly labeled as inference.

### Lens 4: Trend signal
Is this an isolated event or an instance of a larger shift? Single data points prove
little, but a data point plus a known pattern (adoption curves, regulatory cycles,
capital flows) can mark a direction. Historical parallels help when genuinely
similar — name the parallel and where it breaks.

### Lens 5: What is not said
Omissions are evidence. Missing data (no denominator, no baseline, no time frame),
one-sided sourcing, unnamed "people familiar with the matter," questions the article
raises but never answers. Absence of a affected party's voice usually means the story
was not written for them.

### Lens 6: Directions and actions
For each affected audience: what should they watch, prepare, or reconsider? Keep it
directional (值得关注的信号、需要准备的情景) rather than prescriptive advice —
especially for investment, legal, or medical topics, where you inform, not advise.

## 3. Domain-Specific Angles

Quick extra questions by content type:

- **Tech / AI**: Is the claimed capability benchmarked independently or self-reported?
  What gets cheaper / obsolete if true? Who owns the bottleneck (chips, data,
  distribution)?
- **Finance / markets**: Is this priced in? What is the base rate for this kind of
  event? Whose incentive is it to talk the market up or down?
- **Policy / regulation**: Who lobbied for this? What behavior does it actually change
  vs. what it claims? Implementation timeline and enforcement teeth?
- **Company news (funding, launches, executive moves)**: What problem forced this
  move? What does the funding amount / valuation imply about expectations? Why did
  the executive really leave?
- **Science / health**: Peer-reviewed or preprint? Sample size and effect size, not
  just statistical significance. Does the study show causation or correlation?
  Who funded it?
- **International / geopolitics**: Whose domestic audience is this for? What is each
  side's stated vs. likely actual goal? What changed materially vs. symbolically?

## 4. Calibration and Confidence

- Label every implication with its basis: (基于文中信息推断) = follows from the
  article's own content; (结合外部背景推测) = uses outside knowledge, flag the source
  of that knowledge.
- Prefer "这可能意味着…" over "这说明…" for anything beyond direct restatement.
- One strong, well-grounded insight beats five speculative ones. If the article
  supports little, say the honest thing: 这篇文章本身信息量有限.
- Never predict specific prices, dates, or verdicts. Predict directions and
  signposts to watch instead.

## 5. Fact / Opinion / Speculation Checklist

Before writing the 事实与观点 section, sort the article's claims:

- **Verified fact**: multiple independent sources or official records; numbers with
  clear provenance.
- **Reported but single-sourced**: attributed quotes, leaks, "according to X" —
  note the single source.
- **Author's framing**: word choices that presuppose a verdict ("重磅", "暴跌",
  "历史性突破"); strip the adjective and see what fact remains.
- **Unverified / questionable**: no source given, too-round numbers, claims that
  only benefit the source.

Also assess the outlet and author: official media, trade press, self-media, PR wire —
each has a typical stance worth one line of context.
