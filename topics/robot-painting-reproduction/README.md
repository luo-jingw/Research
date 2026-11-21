# robot-painting-reproduction

机器人临摹画：给定一幅目标图像，机器人用实体画具在纸或画布上把它画出来。两个目标场景是素描（铅笔、炭笔，线条加明暗）和油画（不透明彩色笔画分层覆盖）。调色暂以直接指定每笔颜色代替。核心问题是目标图怎样拆成可执行的笔画、介质在仿真中怎样表示、临摹得像不像怎样衡量、有哪些数据。

- 状态：第一轮综述完成（快照 2026-11-20）
- 最后更新：2026-11-21（增补排线方向：方向场方法、感知研究与绘画教学、排线笔画数据）

## 范围

包含：
- 目标图到笔画的分解：启发式笔画渲染（SBR）、逐图优化、强化学习、前馈预测、作画过程模型；素描的线稿前端、明暗合成、矢量笔画与笔画顺序、排线方向（方向场、感知研究、绘画教学）；
- 机器人素描、线描、油画、丙烯、水彩临摹系统：执行回路、笔画模型、颜色处理；
- 介质仿真与渲染：铅笔、炭笔与其他干性介质，油画颜料，刷毛模型，颜色合成，学习的与可微的笔画渲染器，机器人回路中的画布模型；
- 临摹的评测指标与数据：像素、感知、线稿几何、分布级与过程指标；作画过程数据、人类示教与真实笔画、素描数据集。

不包含：
- 控制器侧（VLA、world action model、LLM / VLM agent），见 [vla-drawing-writing](../vla-drawing-writing/README.md)；
- 毛笔书法与水墨，只作为相邻工作引用；
- 没有目标图像的创作式作画，只在其笔画分解方法可复用时引用。

## 关键词

robot painting, robot sketching, portrait drawing robot, stroke-based rendering, neural painting, Learning to Paint, Stylized Neural Painting, Paint Transformer, CLIPasso, vector sketch, hatching, stippling, TSP art, ergodic drawing, pencil rendering, hatching direction, cross-hatching, principal curvature, edge tangent flow, line integral convolution, graphite, charcoal, oil paint simulation, IMPaSTo, WetBrush, Kubelka–Munk, Mixbox, differentiable rasterizer, FRIDA, Spline-FRIDA, IMPASTO, e-David, painting process, time-lapse, LPIPS, Chamfer distance

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 定义与范围、五轴分类、素描分解（含 §2.5 排线方向）、机器人素描、油画分解、机器人油画与颜色、介质仿真、评测、数据、趋势、开放问题、阅读顺序 |
| [papers.md](papers.md) | 论文目录，共 165 项：素描分解 50（其中排线方向场 17、感知研究与绘画教学 13）、机器人素描 21、油画分解 16、机器人油画 14、介质仿真 30、指标 7、数据 24、综述 3 |
| `notes/` | 精读笔记（尚无） |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据与内容、原文之间的矛盾、召回缺口：根目录 `issues.md` → ISSUE-008
- 候选研究方向：根目录 `opportunities.md` → OPT-014（仿真素描临摹任务）、OPT-015（仿真油画临摹任务）、OPT-016（仿真生成的指令—笔迹数据与过程示教）、OPT-017（在 OpenSketch 上测排线相对轮廓的方向分布）
