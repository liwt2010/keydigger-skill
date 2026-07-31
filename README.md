# Keydigger

把新闻、文章、书籍解读成通俗易懂的语言，挖出核心观点与隐含启示。

Keydigger 是一个面向 Agent（Codex / Claude Code / Cursor 等）的解读技能（Skill），也可作为写作模板供人参考。它不满足于摘要式复述，而是帮你**挖出来**——核心框架、逻辑链、关键论据，以及文本不敢明说的那些方向和风险。

---

## 能力速览

| 输入 | 解读模式 | 输出 |
|------|----------|------|
| 新闻链接 / URL | 短篇模板 | 一句话看懂 + 通俗解读 + 历史脉络与新变化 + 核心观点 + 深层解读与隐含启示 + 事实与观点 + 对不同读者的意义 |
| 文章正文 / 截图 | 同上 | 同上 |
| PDF / DOCX | 同上 | 同上 |
| 书籍 (EPUB / TXT / MD) | 长文模板 | 全书框架 + 核心论点与逻辑链 + 关键论据 + 隐含启示与批判性思考 |
| 图片/截图 | OCR/视觉读取后进入短篇模式 | 同上 |

## 快速安装

安装后 Agent 会自动发现该技能：

```bash
# Codex（推荐）
git clone https://github.com/liwt2010/keydigger-skill.git ~/.codex/skills/keydigger

# Claude Code
git clone https://github.com/liwt2010/keydigger-skill.git ~/.claude/skills/keydigger

# 手动
git clone https://github.com/liwt2010/keydigger-skill.git
# 然后软链或复制到 ~/.codex/skills/keydigger
```

## 使用方式

直接对 Agent 说出类似的话即可触发：

> 帮我解读这篇文章：[链接]
>
> 这篇新闻说明了什么？核心观点和隐含的意思是什么？[粘贴内容]
>
> 帮我拆解这本书的核心框架和论点：book.epub
>
> 这张截图里的报道有什么值得关注的方向？

## 仓库结构

```
keydigger-skill/
├── SKILL.md                        # 技能入口：触发词、工作流、输出模板、原则
├── agents/
│   └── openai.yaml                 # UI 元数据
├── references/
│   ├── analysis-framework.md       # 短篇挖掘方法论：六透镜 + 领域角度
│   ├── book-analysis.md            # 长文/书籍工作流 + 输出模板
│   └── examples.md                 # 完整案例示范
└── scripts/
    ├── fetch_article.py            # 网页正文提取（纯 Python 标准库）
    └── extract_book.py             # 书籍章节提取（EPUB/TXT/MD，纯标准库）
```

## License

MIT

---

# Keydigger (English)

A Codex/Claude skill that "digs out" what news, articles and books really say — core viewpoints, hidden implications, frameworks, and evidence quality — in plain language.

**Install**: clone into ``~/.codex/skills/keydigger`` (Codex) or ``~/.claude/skills/keydigger``.

For details see ``SKILL.md`` and ``references/``.
