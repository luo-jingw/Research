# brush-simulation

毛笔与笔刷的仿真与建模：给定笔杆随时间的位姿（位置、下压深度、倾角、转角）和笔上的墨量，预测笔毫形状、纸上墨迹和笔与墨的状态变化。用一组笔法现象（侧锋、提按、铺毫、飞白、墨量、渗化）对照各类模型能表达什么、与真实毛笔对照过没有、计算代价多大。

- 状态：第一轮综述完成（快照 2026-11-24）
- 最后更新：2026-11-24

## 范围

包含：
- 图形学的虚拟毛笔：印章与参数笔印、笔毫集合、三维形变笔束（准静态脊线、逐根笔毫）、来自真实毛笔的数据驱动模型；
- 墨、水与纸：吸水纸中的扩散与渗化、水性颜料的参考模型、真实墨与纸的材料测量；
- 机器人书法与机器人绘画的毛笔模型：实测与几何笔印、带状态的动力学模型、从机器人自身笔画拟合的模型、学习系统中的隐式毛笔、笔状态感知；
- 笔毫与纤维的物理仿真：杆模型与求解器、接触摩擦与验证、湿笔毫与液体、机器人仿真引擎对杆与形变体的支持；
- 学习式与可微笔画模型：神经笔画渲染器、墨与书法专用的模型、从机器人真实笔画学的模型。

不包含：
- 铅笔、炭笔与油画颜料的仿真，见 [robot-painting-reproduction](../robot-painting-reproduction/README.md)；
- 控制器侧（VLA、world action model、LLM / VLM agent 写字），见 [vla-drawing-writing](../vla-drawing-writing/README.md)；
- 没有笔画形成模型的字体生成。

## 关键词

virtual brush, hairy brush, Chinese calligraphy brush, brush footprint, biased tip, side tip, bristle spreading, dry brush, Kasure, Nijimi, ink diffusion, absorbent paper, Xuan paper, MoXi, lattice Boltzmann, quasi-static brush, spine, SQP, data-driven brush, discrete elastic rods, Cosserat rod, XPBD, VBD, frictional contact, wet hair, elastocapillary, MuJoCo flex, Newton VBD, robot calligraphy, footprint model, tractrix, brush lag, dry brush model, neural stroke renderer, FRIDA, Spline-FRIDA, IMPASTO, RealBrush Ink

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 定义与范围、五轴分类、图形学毛笔、墨与纸、机器人毛笔模型、物理仿真与引擎、学习式模型、笔法现象覆盖表、趋势、开放问题、阅读顺序 |
| [papers.md](papers.md) | 论文目录，共 153 项：图形学毛笔 32、墨与纸 24、机器人毛笔模型 37、物理仿真与引擎 33、学习式模型 25、综述 2 |
| `notes/` | 精读笔记（尚无） |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据与内容、召回缺口：根目录 `issues.md` → ISSUE-009
- 候选研究方向：根目录 `opportunities.md` → OPT-018（倾斜笔杆下的带状态拖曳接触模型）、OPT-019（准静态脊线毛笔模块）、OPT-020（MuJoCo 1D flex 离散弹性杆笔束的复测）、OPT-021（墨量与飞白的逐步状态）
