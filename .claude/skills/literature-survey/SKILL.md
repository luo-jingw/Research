---
name: literature-survey
description: 为一个研究方向做一轮文献调研：界定范围、拆分子方向并行检索、核实元数据、写综述与论文目录、记录待核实项与候选研究方向，最后提交推送。
---

# Trigger

用于：
- 新开一个研究方向（`topics/<slug>/`）的第一轮调研；
- 围绕一篇新论文调研它所在的谱系；
- 对已有方向做增量更新（补新论文、补分支）。

不用于：单篇论文的问答、术语解释、只改排版。

# Inputs

读：
- `PROJECT.md`：目录结构、命名、状态归属、写作语言、排版、Credentials；
- 根目录 `README.md`：已有方向列表；
- 相关方向的 `topics/<slug>/README.md`、`survey.md`；
- `issues.md`、`opportunities.md` 中同一 `Area:` 的记录。

# Procedure

## 1. 界定范围

- 确定 slug 与"包含 / 不包含"。与已有方向重叠的部分写成"不包含，见 [其他方向]"，不重复调研。
- 关键词有多种含义时（例如"加速"可以指推理延迟，也可以指执行速度），在综述第 0 节写明采用的拆分，覆盖所有合理含义，不为此单独提问。
- 新建 `topics/<slug>/`，在根目录 `README.md` 加一行，综述完成前不加链接。

## 2. 精读锚点论文（如有）

- 用 WebFetch 打开 arXiv abs 页确认元数据；正文用 PDF：下载文件放进 scratchpad 下单独的目录，用 `pdftotext -layout` 提取。
- 重点读 Related Work（它自己划定的谱系）、方法、关键数字、附录中的评测口径、自述局限。
- 写 `notes/<year>-<short-name>.md`。

## 3. 拆分子方向并行检索

- 拆成 3–4 个互不重叠的子方向，每个交给一个 general-purpose 子 agent，在同一条消息中并行启动。
- 每份 brief 包含：
  - 研究问题，以及这个子方向在其中的位置；
  - 范围内要覆盖的点，附若干种子论文名；
  - 范围外的内容，写明"由其他子方向负责"；
  - 已在其他方向综述过的内容，只引用、不重复调研；
  - 核实要求（见下）；
  - 返回格式：论文表（标题、简称、年份、会议、arXiv、项目链接、子类、领域相关的 2–4 列、一句话、Verified）、各子类 3–6 句综合、文献自述的开放问题（注明出处）、新手必读 5 篇，并把副本存到 scratchpad。
- 核实要求：
  - WebSearch 的额度在整个会话内共享，约 15–20 次就会用完；每个子 agent 最多用约 5–8 次。
  - 发现与核实以 arxiv.org 的 abs、listing、HTML 页面为主；arXiv API 可能返回 429，此时改用 HTML 页面。
  - 标题、年份、arXiv 编号必须来自一手页面；发表处只取 arXiv comment 字段或论文集；无法确认的标 UNVERIFIED。
  - Awesome 类列表只用于发现论文，不作为发表处来源。
- 子 agent 运行期间不重复做它们的检索。

## 4. 抽查与对账

- 每轮自己抽查 3–4 条：优先选 2026 年的论文，以及综述里要引用的关键数字。打开 arXiv abs 页或 HTML 全文核对。
- 原文措辞与子 agent 的转述不一致时，按原文改写。例如原文是"基线不优于"，就不要写成"胜过"。
- 子方向之间结论矛盾时（例如一个说"没有这类工作"，另一个找到了），回到原文核实后再写。

## 5. 写文件

格式按 `PROJECT.md` → 排版。

- **`papers.md`**：按综述分节，每篇一项。标题从子 agent 存在 scratchpad 的表格里取，不凭记忆写。文件头写明快照日期、年份口径、"预印本"与 † 的含义。
- **`survey.md`**，按顺序：
  1. 快照日期与引用格式；
  2. 定义与范围（第 0 节）；
  3. 分类框架（正交的几个轴）；
  4. 各分支：问题 → 演进 → 设计轴 → 代表数字 → 局限；
  5. 横向趋势（每条附论文名）；
  6. 文献自述的开放问题（注明来源）；
  7. 现有综述的分类对照（如有）；
  8. 入门阅读顺序。
- **`README.md`**：范围（包含 / 不包含）、关键词、文件索引、相关记录。

## 6. 区分事实与设想

- `survey.md` 只写能对应到具体论文的内容。
- 基于文献缺口提出的研究设想写入 `opportunities.md`，按 OPT 模板填 Observation / Opportunity / Expected Mechanism / Required Evidence / Promotion Condition，`Area:` 填 slug。Expected Mechanism 以"假设："开头。
- 未能核实的元数据、相互矛盾的结论写入 `issues.md` 的 ISSUE 记录，`Area:` 填 slug；`papers.md` 中对应条目标 †。

## 7. 检查

- `python3 -I .claude/skills/literature-survey/scripts/check_tables.py README.md issues.md opportunities.md topics/*/*.md topics/*/notes/*.md`：以 `WIDE` 开头的表格要改写。
- 文中的跨方向相对链接能对应到实际文件。

## 8. 收尾

- 根目录 `README.md` 中该方向一行补上链接、状态与日期。
- 用英文提交信息提交，写明改了什么、为什么；不加任何 agent 署名。
- 按 `PROJECT.md` → Credentials 推送。

# Stop Conditions

- 新方向与已有方向的边界无法从请求中判断。
- 推送所需的身份或凭据缺失或不明确。
- 子 agent 的关键结论相互矛盾，且一手来源无法判定；此时写入 `issues.md`，综述中只陈述两边各自的原文结论。

# Completion

一轮调研结束时具备：
- `topics/<slug>/` 下的 `README.md`、`survey.md`、`papers.md`，以及精读笔记（如有）；
- 根目录 `README.md` 中带链接的索引行；
- `issues.md` 与 `opportunities.md` 中的对应记录；
- 检查脚本输出无 `WIDE`；
- 已推送的提交；
- 给用户的汇报：论文数、核心结论、抽查结果与更正、未核实项所在的 ISSUE 编号、候选研究方向所在的 OPT 编号。
