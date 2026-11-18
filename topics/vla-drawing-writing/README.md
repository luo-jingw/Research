# vla-drawing-writing

用 VLA（vision-language-action model）、WAM（world action model）或 LLM / VLM agent 控制机器人写字、画画，以仿真为主。本体、书写工具、写画内容都不限。核心问题是这类任务在仿真中如何实现与评测，现有 VLA / WAM 与 agent 能做到什么程度。

- 状态：第一轮综述完成（快照 2026-11-18）
- 最后更新：2026-11-18

## 范围

包含：
- 控制器是 VLA 或 WAM、实验中有写画任务的工作，仿真优先，真机工作作为对照；
- 含写画任务的仿真环境与基准、笔迹在仿真中的实现方式、写画示教的生成管线；
- 世界模型对写画画面的预测，包括把学习的世界模型当作模拟器；
- LLM / VLM agent 写画：LLM 或 VLM 输出笔画、航点、SVG、程序或工具调用，由运动基元、IK、优化器或学习策略执行，包括开环流水线与闭环 agent；以及被机器人写画工作复用的数字画布绘图 agent 与 VLM 评测器。

不包含：
- 控制器既不是 VLA / WAM、也不是 LLM / VLM agent 的写画工作（RL、轨迹优化、经典模仿学习），只作为环境来源或相邻工作列出；
- sim + real 共训练的一般配方，见 [sim-real-cotraining](../sim-real-cotraining/README.md)；
- 世界模型作为评测器或数据生成器的一般讨论，见 [real2sim](../real2sim/README.md)。

## 关键词

robot drawing, robot handwriting, calligraphy, sketching, painting, vision-language-action, world action model, video action model, ManiSkill3 DrawTriangle / DrawSVG, BURGER, DrawAnything, tactile VLA, force-aware writing, LLM agent, code as policies, sketch agent, human-robot co-painting, VLM-as-judge

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 交集规模与范围、分类框架、仿真与真机中的 VLA / WAM 写画、世界模型预测、环境与指标、LLM / VLM agent 写画、趋势、开放问题、阅读顺序 |
| [papers.md](papers.md) | 论文目录：8 篇 VLA / WAM 写画与世界模型、5 个环境与基准、7 个被评测的基座、18 篇 LLM / VLM agent 写画与数字画布 agent、16 篇相邻工作、5 篇易混淆工作 |
| `notes/` | 精读笔记（尚无） |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据与召回缺口：根目录 `issues.md` → ISSUE-006
- 候选研究方向：根目录 `opportunities.md` → OPT-011（力决定墨迹的仿真中评测 VLA 写画）、OPT-012（写画作为 sim + real 共训练的受控测试域）、OPT-013（VLM 规划笔画 + 学习策略执行的分层写画）
