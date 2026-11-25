# brush-simulation 综述

- 快照日期：2026-11-24
- 引用：论文用简称，元数据见 [papers.md](papers.md)；"P§x" 指 papers.md 的节号。
- 数字后括号里的位置（§、表、图、式）指原论文。

## 0. 这个方向讨论什么

核心问题：给定笔杆随时间的位姿（位置、下压深度、倾角与倾斜方向、绕轴转角）和笔上的墨量，预测笔毫的形状、纸上留下的墨迹（形状与浓淡），以及笔和墨的状态怎样变化。机器人书法的仿真、规划和学习都需要这样一个前向模型，而且要能在每个控制步调用。

"建模"有两种含义，本综述都覆盖，但以前一种为主：

- 前向模型：笔杆位姿与笔状态 → 笔毫形状与笔迹，用于仿真和规划；
- 逆模型：笔迹图像 → 笔杆动作，只在机器人书法一节作为相邻工作（§4.4）。

全文用下列笔法现象对照各类模型：

- **侧锋**：笔杆倾斜，笔尖偏在笔画一侧，笔印不再对称；
- **提按**：下压深度变化引起笔画宽度变化；
- **铺毫**：笔毫散开压平，宽度超出按深度缩放的形状；
- **飞白**：笔毫分叉、墨少，笔画中出现露白的条纹；
- **墨量**：笔上墨量随书写减少，墨色变淡、变枯；
- **渗化**：墨在吸水纸中向外扩散。

包含：

- 图形学的虚拟毛笔：笔印与印章、骨架与脊线、逐根笔毫模型；
- 墨、水与纸：吸水纸中的扩散与渗化、干笔与飞白、水墨渲染；
- 机器人书法与机器人绘画用的毛笔模型：实测笔印、带状态的动力学模型、从机器人自身笔画拟合的模型；
- 笔毫与纤维的物理仿真：杆模型、毛发接触与摩擦、湿毛发与液体，以及机器人仿真引擎对杆和形变体的支持；
- 学习式与可微的笔画模型：神经笔画渲染器、墨与书法专用的数据驱动渲染器、从机器人真实笔画学到的模型。

不包含：

- 铅笔、炭笔与油画颜料的仿真，见 [robot-painting-reproduction](../robot-painting-reproduction/README.md) §6；
- 控制器侧（VLA、world action model、LLM / VLM agent 写字），见 [vla-drawing-writing](../vla-drawing-writing/README.md)；
- 没有笔画形成模型的字体生成。

## 1. 分类框架

五个正交的轴：

- **笔的表示**：
  - 无状态笔印：每个位姿对应一个笔印形状，沿路径合成；
  - 少量状态的集总模型：宽度、滞后、偏移等几个状态变量；
  - 脊线：一根或几根骨架加侧向节点，表面由骨架扫出；
  - 逐根笔毫：几十到几百根杆或粒子链；
  - 连续体：FEM 或 MPM；
  - 图像空间的学习模型：直接预测笔迹图像。
- **时间上的处理**：静态映射；准静态平衡（每帧从上一帧出发求能量最小）；去掉惯性的动力学；完整动力学。
- **墨**：不建模；标量墨量；逐节点或逐笔毫的墨量；纸上扩散。
- **验证**：没有；画家评价或视觉对比；图像相似度（余弦、SSIM、LPIPS、L1）；毫米级几何误差。
- **用途**：交互绘画软件；机器人规划；学习环境。

## 2. 图形学的虚拟毛笔（P§1）

交互绘画软件要从笔的输入（位置、压力，有时还有倾角）实时画出像毛笔写出的笔画。这一支积累最久，表达的笔法现象最全，但几乎都只做视觉验证。

### 2.1 印章、笔印与骨架

- **形式**：笔画是一个笔印沿路径的扫掠或叠印（Brush Extrusion、Skeletal Strokes、Pudet Pressure Strokes）。压力、速度、"湿度"作为规则参数改变笔印形状（Droplet；Camshaft Brush 的凸轮曲线），或者笔印来自一个单独的简单形变笔（Guo Force-Feedback Brush：力驱动的弹簧质点笔变形，再逐个采样叠印二维笔印）。
- **能表达的**：提按表现为宽度；飞白只能靠样例或纹理库，如 Guo Force-Feedback Brush 的"半干值"加半干纹理库、An-Liu Half-dry 的墨迹纹理库。
- **表达不了的**：除非笔印生成器本身有倾斜的三维笔尖，否则表达不了侧锋的不对称形状，也没有作为物理过程的墨量消耗。
- **验证与代价**：验证是视觉的，最强的说法是 Camshaft Brush 的"perceptually invisible"，也不是笔印的定量对比；计算代价可忽略。

### 2.2 笔毫集合

- Hairy Brushes 定下了沿用至今的拆分：笔（一组各带墨量的笔毫）、笔画（位置加压力）、蘸墨和纸。逐根笔毫的墨量消耗自然产生墨色变化和类似飞白的条纹。
- Ip-Wong Brush 和期刊版 Virtual Brush 加入笔的姿态和显式的墨吸收、沉积过程，摘要列出变宽、灰度和干笔的"black and white trails"。
- 弱点在笔印几何：
  - Virtual Brush 把毛笔当倒锥，笔印取锥体与纸面的交。Chu Thesis 指出这种笔印"fails to produce the biased-tip strokes (in which the tip travels along one side of a stroke rather than staying in the middle)"（§2.2）。
  - Lee Black-Ink 的笔毫是均匀弹性杆，Chu Thesis 指出弯曲不自然。
- 这些模型都没有与真实笔印对照。

### 2.3 三维形变笔束

- **主流是准静态**：每帧求一根脊线（或带侧向节点的脊线）在"不低于纸面"约束下的能量最小。
  - 起点是 Saito-Nakajima Brush 的 Bézier 脊线加圆盘。
  - Chu-Tai Efficient Brush 和 Chu-Tai VCB 用 SQP 求解，能量含应变能、内摩擦和外摩擦三项，有意不含惯性："real brushes reach equilibrium almost instantaneously as they are being pressed against or lifted from the paper"（Chu Thesis §2.5）。
  - Baxter-Lin Brush 用几根脊线带动细分曲面和最多 200 条插值笔毫带，加各向异性摩擦。
  - Van Laerhoven Brush 同属此类。
- **Chu-Tai VCB 表达的笔法最全**（细节见 Chu Thesis 第 2 章）：
  - 6 自由度输入，纸孔阻力约束带临界倾角，可以写出偏锋；
  - 压平和侧向铺毫，分叉图，最多 5 个子笔束；
  - 湿笔的塑性；
  - 干笔图由真实干笔印制成，按湿度和压力取阈值，再叠纸纹遮罩，得到飞白；
  - 墨量可选地扣除已沉积的墨；
  - 墨在纸上的扩散留作"a future goal"，后来由 MoXi 完成。
- **其他三维笔**：
  - Xu Solid Brush 把笔毫簇写成可分叉的 NURBS 扫掠体，Chu Thesis 指出体积穿透纸面导致笔印不真实；
  - Xu Advanced Brush 加入离线标定的笔运动和颜料分子扩散；
  - dAb、Yeh Haptic Brush、Guo Force-Feedback Brush 用弹簧质点或弯曲弹簧，侧重力反馈。
- **逐根笔毫**：
  - DiVerdi Bristles 让每根笔毫是去掉扭转的 DER，在笔管的非惯性系中模拟并去掉惯性项。理由是笔毫"too stiff to visibly react to the brisk motion of the brush during normal brush strokes"。
  - DiVerdi Bristles 报告笔毫被竖直压下并屈曲时，后向欧拉"stable but not monotone"，出现虚假振荡，于是改用位置投影加逐粒子对纸面的连续碰撞检测；不做笔毫间碰撞。
  - WetBrush 的惯性项按 β_B ∈ [0, 0.1] 缩放（β_B = 0 用于细而清晰的线），笔毫聚拢用最小密度约束代替碰撞检测。
- **代表数字**：
  - Chu-Tai VCB：Pentium 4 2.26 GHz、GeForce 4 上，1 / 3 / 5 个 6 段笔束整个系统 62.6 / 44.6 / 28.5 fps（Chu Thesis 表 2.1）；
  - Baxter-Lin Brush：3 关节脊线 5 次 SQP 迭代约 100 µs（1 GHz Pentium 4）；
  - DiVerdi Bristles：50 根笔毫每次印章物理约 0.5 ms（2.6 GHz Core2 Duo，表 1）；
  - WetBrush：GTX TITAN X 上 30–110 fps，210K 粒子的例子 46 fps，笔刷模拟 2.0 ms。
- **局限**：
  - 验证都是视觉的（Xu Solid Brush 的"nearly indistinguishable"也是视觉判断）；
  - DiVerdi Bristles 的笔毫数达不到真实毛笔的上千根；
  - Huang 2019 FITEE 指出 WetBrush 限制了笔画速度。

### 2.4 来自真实毛笔的数据

- 只有这一类的笔行为直接取自真实毛笔：
  - 真实光学接触笔印：Drawing Prism 的棱镜，FluidPaint 对真实湿笔的实时成像；
  - 扫描的笔画样例：RealBrush，数据公开，用户研究评测；
  - 从真实毛笔视频手描的平衡形状表：Baxter-Govindaraju Brush。
- **Baxter-Govindaraju Brush**：以笔毫根部离纸高度和攻角为输入，15 个表项，"as few as 6" 也可用。一根脊线"within 10 microseconds"，比优化式笔快 5–45 倍，也更稳定。它不含塑性和各向异性摩擦，作者写明"it is not possible to recreate every possible deformation of a real brush"（§5）；手工建表需要"an hour or two"。
- 精度受采集范围限制，这一类也没有报告笔印误差指标。

## 3. 墨、水与纸（P§2）

- **演进**：
  - 一维滤波和纯扩散方程：Sumie Diffusion、Kunii Diffusion。MoXi 指出纯扩散方程只能得到模糊图像，没有流动纹理。Kunii Diffusion 的摘要称与真实图像"exactly the same intensity distribution"，但没有给出比较方法。
  - 没有动量的元胞自动机和局部平衡：Zhang Ink CA、Yu Oriental Painting。
  - 纤维网格纸：Lee Ink Diffusion、Nijimi，只处理前沿，能做的效果受限（MoXi §3）。
  - MoXi：改进的格子 Boltzmann 水流，表层、流动层、固着层三层水与颜料。它能表现羽状扩散、浅色边缘、分支、边界变粗糙和变深，以及胶矾形成的阻隔。
  - MoXi 之后：Wang-Rokne Ink 的毛细网络 Darcy 流，Sun Xuan Paper、Sun Ink Simulator 的纸单元与粒子，Fan-Li Xuan 的变系数扩散方程，Liao-Zhang Ink 的双层纸。
- **水性颜料的参考**：Curtis Watercolor 用浅水方程加 Kubelka–Munk，MoXi 指出它干湿边界固定、没有渗透；Van Laerhoven Watery Paint 实时实现了东方墨的深色边缘和湿接湿。
- **能表达的**：渗化（晕、羽状、分支、回流）、水和颜料的收支（墨量）；枯笔（Kasure）在纸的一侧由 Zhang Ink CA 和 Nijimi 表现。
- **笔与纸的耦合**：Chu Thesis 第 3 章给出笔印向纸面供水的公式；Chu-Tai VCB 与 MoXi 是同一系统的两部分。
- **代表数字**：
  - MoXi：Athlon XP 2600+、GeForce 6800 Ultra 上，512² 模拟、输出 1536²、每 300 帧更新一次时 44 fps，每帧都更新时 32 fps；256² 时 70 fps（表 1）。帧率"measured when there is no concurrent brush deformation"。
  - Nijimi：20 笔约 30 s。
  - Fan-Li Xuan：隐式差分，线性时间。
- **局限**：
  - 验证是与真实墨迹照片的视觉对照（MoXi 图 2、图 9）；
  - 宣纸上真实墨扩散的材料测量（Wu Qianlong Xuan、Liu GO Ink）和笔毫吸墨的测量（Liu-Liu Brush Hair）存在，但没有被用来拟合或检验这些模拟器。

## 4. 机器人书法与机器人绘画的毛笔模型（P§3）

机器人规划要的是"笔杆位姿 → 笔迹"的映射，而且要能在优化或学习中反复调用。这一支的模型因此大多是闭式的或查表的，验证用真实笔画。

### 4.1 实测与几何笔印

- **演进**：
  - Lo06 从玻璃板下方拍笔印，笔印近似为椭圆，长短轴随下压深度变化，沿路径取并集；速度 7.5–19 mm/s 对笔印影响不大。
  - Lam09 改为在纸上采笔印，用 8 顶点多边形表示，每个顶点是下压深度与倾角的三次函数，标定倾角 5–50°、深度 1–15 mm。倾斜时笔印变大、中心移向笔尖一侧。轨迹搜索只用了 5–20° 的倾角。
  - 武汉的一组工作把倾角留作输入，但实测只到 10°：Wang-Min21 用两段 Bézier 水滴形，尺寸是下降高度和倾角的线性函数；CCD-BSM 用斜圆锥截面加切线、按面积不变膨胀；CCD-BSMG 和 B-BSMG 再用这些解析模型生成的仿真笔画训练神经生成器；Guo25 加上转笔调锋、折笔、逆锋入笔、藏锋收笔的闭式笔杆运动；Guo26 按笔画阶段规划高度和速度。
- **设计轴**：笔印的参数化（椭圆、多边形、Bézier、圆锥截面）；输入（深度、倾角、转角）；沿路径的合成方式（并集、扫掠、生成器）。
- **代表数字**：
  - CCD-BSMG：狼毫笔（R 6 mm、L 48 mm）、宣纸，每个 (H, α) 至少 10 张图，与真实样本的相似度最高 98.21%；
  - Guo25：AUBO-i5 上两支狼毫笔、100 次书写，基本笔画平均余弦相似度 98.76–99.54%、SSIM 92.55–97.57%，整字"不""去"的 SSIM 只有 63.81% 和 68.73%；
  - Wang-Min21：横画综合相似度经三版轨迹从 76.36% 到 87.42%。
- **局限**：
  - 没有内部状态，笔印只由当前位姿决定；
  - 除 Lam09 外倾角只测到 10°，而且都是静态按压，没有带倾斜的运动笔画与真实墨迹的配对；
  - 只报图像相似度，不报毫米级几何误差；
  - 墨量只以"每次按压后重新蘸墨"（CCD-BSMG）或"假设墨量最大"（Lin20）出现。

### 4.2 带状态的动力学模型

- **Robot Calligraphy POC**：
  - 7 维状态，宽度和拖尾以惯性 0.02 松弛到 Width(z)、Drag(z)，笔尖偏移靠摩擦保持、超出后突变；
  - 在伪谱最优控制中用 Levenberg–Marquardt 优化 Chebyshev 轨迹；
  - 笔杆竖直，不建模笔毫分叉；每笔后蘸墨，同时让笔复位；
  - 真机结果只给差异图，作者称仍有"considerable Sim2Real gap"（§V.G）。
- **Lin20**：
  - 按位移和高度索引的笔印库，加滞后 η(z) 和笔印角 φ；
  - 按压后笔印在 3 / 5 / 6 mm 行程内（z = 1 / 2 / 3 mm）变窄趋稳，转折后笔印需要一段距离重新对齐；
  - "永"字的美观评分用模型约 94、不用约 88。
- **Karimov24 Brush**：
  - 从笔毫梁的论证推出接触区沿 tractrix 追随笔杆：tan(α/2) = tan(α₀/2)·exp(−∫ds/r)，滞后 r(z) 随深度变化，笔尖间隙 b = k_b·z，另有换向规则，渲染用笔印图像库；
  - z = 10 mm 的 90° 转角，y 误差 ≤ 2%、RMSE 0.05；滞后拟合 R² 0.98；k_b = 0.52 ± 0.09；
  - 笔毫的残余弯曲（迟滞）最大约 5 mm，随湿度变化，没有建模其衰减；笔杆竖直；
  - 给出三种标定方法：磨砂玻璃上的笔印、标定笔画、侧面投影。
- **Gülzow24**：笔毫绕笔管转动，笔尖落在圆弧上；侧向倾斜时由线与圆的交点算出笔尖超出量，可用倾角 15–45°。这是唯一针对有意倾斜毛笔的机器人几何，但没有动力学。
- **局限**：两个带状态、按控制步更新的模型（Robot Calligraphy POC、Karimov24 Brush）都假设笔杆竖直；倾斜只有 Gülzow24 的几何。

### 4.3 从机器人自身笔画拟合的模型

- **压力与宽度**：
  - e-David Replication 用机器人自己的笔画建压力到宽度的查找表，按笔的不同，宽度精度 0.02–1.32 mm，回归的最大宽度误差 0.5 mm；再用相机逐轮修正轨迹，10 条笔画中控制点平均距离每轮减少约 14 mm；
  - Zingrebe23 用半圆标定网格拟合宽度与滞后随压力和曲率的变化，并据此预补偿路径；竖直落笔会留下"big blob"，需要入笔压力斜坡；作者有意不量化精度；
  - Mueller13 用相机图像迭代修正单笔样条。
- **墨量与干笔**：
  - Karimov24 Dry：宽度 w = k_w·Z + w0（k_w = 0.595 ± 0.024，w0 = 1.07 ± 0.16 mm，首笔 1.64 ± 0.19 mm），笔画密度每笔按 α[i+1] = k·α[i] 衰减，k 首段 0.71、后段 0.89、整体 0.81（64 条 80 mm 笔画）；这是唯一在机器人上实测的墨量递减与干笔规律；
  - Jin23 Ink：下降深度 2–18 mm 对应线宽 3–14.5 mm（线性拟合 R² 0.957），浓淡由蘸墨时间与比例控制，枯笔程度取笔画面积与吸墨量之比；
  - Degradable Tools 对铅笔磨损建了显式工具状态，在线最小二乘更新，考虑磨损后沉积误差最多降低 65%。
- **局限**：都不含倾斜；Zingrebe23 写明"only considered holding the brush vertically, while most writing is performed with brushes being held at an angle"（§5）。

### 4.4 学习系统中的隐式毛笔

- 这一类学习轨迹或笔画外观，毛笔由三者之一代替：真机本身、一个标定过的小工具模型、或一个图形学笔刷引擎。
  - 真机：Chao 等人的 GAN Calligraphy、Gao 2019 CAE-DE、Wu 2020 AC-GAN 用判别器或自编码器评价真机写出的笔画；摘要中看不到训练时的毛笔渲染方式。
  - 标定的工具模型：CalliRewrite 把毛笔简化为水滴形笔印 (r, l, θ)，l = 0.003 + 2.021·r，加三段式笔尖转向规则，z 与 r 由 8 点线性拟合。
  - 图形学引擎：Sim-to-Real Brush 用 MyPaint 作仿真器，真机由笔画图像标定压力范围。
- 机械臂多为 3–4 自由度，不能倾斜；Sim-to-Real Brush 写明"our 3-DoF robot cannot"。
- 逆映射：HGN Delta 从笔画图像生成含笔杆转角和倾角的五自由度动作，是少数把侧锋当学习输出的工作；Variational IL Calligraphy 输出三维轨迹加笔尖旋转；Sun14 的倾斜只来自示教。
- 验证都是图像级的。

### 4.5 笔状态的感知

- 本轮没有找到在书写过程中用触觉或视觉估计笔尖状态的机器人书法论文。
- 已有的做法：力补偿（Sch25、Kob22），力到宽度（Flying Calligrapher，海绵笔），笔画之间用相机修正（e-David Replication、Zingrebe23、Mueller13），用砚台复位代替估计（Robot Calligraphy POC），以及人的书写过程记录（CalliSense）。

## 5. 笔毫与纤维的物理仿真（P§4）

### 5.1 杆模型与求解器

- **稳健的杆模型都把刚性模态去掉或解耦**：DER 让材料标架准静态、用流形投影保持不可伸长；DVT 做隐式积分，Hessian 是带状的；Super-helices 用约化坐标，可用大时间步；Stable Cosserat Rods 用闭式准静态更新朝向。
- **位置式求解器的软化**：
  - Direct XPBD Rods 指出 Gauss–Seidel 式 XPBD"requires many iterations to converge… if convergence is not reached, the material becomes too soft"，改为对树形结构直接求解；一束笔毫正是以笔管为根的树。
  - Newton 的 VBD 调参文档列出相关机制："Information moves one ring per iteration"，"An unfinished solve becomes velocity"，"Stiff terms win the local solve"。
  - VBD 在任意迭代次数下都稳定，但没有收敛的迭代会改变结果；AVBD 用增广拉格朗日改善高刚度比下的收敛。

### 5.2 接触、摩擦与验证

- **精确 Coulomb 摩擦**：光滑化的摩擦会丢掉粘滑（NSN、Daviet Hybrid）；Daviet Hybrid 写明此前的头发模型"neglect friction or use an approximate smooth friction model, thus losing important visual features"。
- **落笔**：Kaufman ANL 指出时间步"severely restricted by a strong nonlinearity in the response of stretching modes to transversal impact"，正是笔尖触纸的情形。
- **多稳态**：Frictional Elastica 显示压在摩擦平面上的弹性拱有多个稳定构型，并会突跳，力出现不连续的跳变。
- **无穿透**：CIPC 对带厚度的杆保证中心线间距不小于设定厚度，属于离线方法；IMC 的全隐式罚函数接触与 IPC 性能相当、收敛更快；DisMech 把全隐式 DER 和 IMC 做成机器人仿真器，有与硬件对比的 real2sim 验证，其 README 待办仍列着"Improve robustness of friction"。
- **验证协议**：Romero Validation 给出悬臂、弯扭耦合、粘滑三类实验对照协议，发现"some popular simulators for plates/shells and frictional contact fail even on the simplest scenarios"，杆代码"generally perform well"。
- **连续体**：Aniso-MPM 用各向异性弹塑性表示纤维集合的摩擦接触，百万自由度每帧数十秒到数分钟；各向同性的四面体体积（PhysX FEM）没有纤维方向。

### 5.3 湿笔毫、内聚与液体

- 湿笔聚成笔锋来自弹性毛细作用（Bico Coalescence）。
- Wet Hair 用 DER 头发、APIC 液体和逐根的约化液膜模拟湿发聚拢，液体主要沿毛发表面和毛发之间流动（引 Ratchet Hairs）。4K–32K 根头发每步 3–57 s，参数标定"largely based on visual interpretation"。
- Creamy Strands 把内聚改为位移的二阶 Coulomb 锥，理由是罚函数内聚"requires a finely-tuned stiffness parameter to balance collision and cohesion effects, and thereby avoid both instability and tunneling"。它的例子里有旋转画刷与油画颜料的双向耦合，约 28 分钟一帧。
- 两个与毛笔直接相关的实验：
  - Rigid Brush Fluid Capture：毛刷提起时带走的液体量随提起过程非单调变化；
  - Paintbrush Scaling：对数百支画笔的测量表明，圆笔的颜料印大小随压缩距离标度，"only depends on the force applied by the painter and not on the mechanical responses of the brushes"。

### 5.4 引擎与机器人仿真器

- **MuJoCo**：
  - 3.17.0（2026-10-22）给 1D flex 加入无扭转的离散弹性杆弯曲，由 `discrete` 积分器隐式积分；
  - 4.0.0（2026-11-06）删除 cable 插件和 `composite`，由 1D flexcomp 取代，并加入扭转；
  - 接触是软约束；3.14.0 加入的 `ipc` 无穿透模式只支持 2D flex，接触无摩擦，不支持精确回放。
- **MuJoCo Warp**：flex 标为 experimental，不支持插件。
- **Newton**：SolverVBD 支持由 ROD 关节连接的胶囊体缆绳和 Dahl 弯曲迟滞；DAT 无穿透接触覆盖粒子自接触和可选的刚–软接触，不覆盖胶囊体杆；文档写明有限刚度在收敛后仍允许拉伸、关节位移和接触穿透。
- **Genesis**：有 MPM、FEM、PBD、SPH，没有杆模型；IPC 耦合只覆盖 FEM 和布料。
- **PhysX / Isaac Lab**：体素仿真网格加贴合碰撞网格的四面体形变体，"very stiff materials typically require more solver iterations"。
- **机器人软体基准**：ManiSkill2 的 Write 是 Panda 持刚性棍在 MPM 材料上压写；PlasticineLab 的 Writer 同属此类。
- 六个引擎的文档都没有毛笔或笔毫束模型。

## 6. 学习式与可微笔画模型（P§5）

### 6.1 神经笔画渲染器（背景）

- 2018–2021 年这一支（SPIRAL → StrokeNet、Learning to Paint、Neural Painters → SNP、Paint Transformer）的动机是绘图程序不可微，于是用网络近似 MyPaint 或矢量渲染器，换取梯度和批量渲染。
- 训练数据都来自软件，参数里最多有一个压力或粗细。
- 上真机的结果：FRIDA 报告 Learning to Paint 的笔画（尺寸过大、透明度可变）在真机上与仿真和目标都"vastly dissimilar"；CML 把笔画约束成机器人可执行后，RL 仍难以复现目标。
- 2024–2026 年的 AttentionPainter、MambaPainter、DQ-Transformer 追求预测速度，仍用合成笔画；Birth of a Painting 加了可微涂抹算子；StrokeDiff 用 520 条真实油画笔画训练扩散模型，留出集 LPIPS 0.232、FID 52，数据公开。

### 6.2 墨与书法专用的模型

- **RealBrush Ink**：
  - 机器人用 4 种真实毛笔在 2 种纸上画了 1,818 条墨笔画；
  - 墨量用"自上次蘸墨起的累计路径长度"驱动的褪墨嵌入表示，递归 CNN 预测新画布；
  - 21 幅、148 笔的留出画上 LPIPS 0.2593 / SSIM 0.9070，DeepBrush（Wu Oil-GAN 重训）为 0.2691 / 0.9011，商业软件 Expresii、Fresco、Rebelle 6 更差；
  - 输入只有二维路径，没有压力和倾角；湿画法（在未干区域上画导致渗化）仍明显不如参考（§6）；
  - 论文称希望发布数据，本轮没有找到发布页。
- **OnOff**：6 参数可微笔刷 {w_base, k_spread, ρ_ink, σ_sharp, p_min, p_max}，压力由速度推出，宽度 = w_base + k_spread·p；作者承认参数不是物理单位，省略了三维笔刷动力学、湿度扩散和纸张吸收（§3.1、§6）；真机演示用的是铅笔、Sharpie 和马克笔。
- **Artist Agent**：圆形笔印序列贴真实毛笔在不同墨量下的笔印纹理，策略动作含下压、上提和转笔杆，可以得到干墨和中空的笔画效果；没有定量对比。
- **TBR**：后一笔以保面积的方式输运已有痕迹的可微沉积模型（流墨、大理石纹），可参考"后一笔改变前一笔"的可微写法，但不是毛笔。

### 6.3 面向机器人、从真实笔画学的模型

- **FRIDA**：约 100 条机器人随机画的真实笔画训练 param2stroke，输入为下压深度 h、长度和弯曲；作者认为笔上颜料量是最主要的未建模变量；笔始终垂直于画布。
- **Spline-FRIDA**：
  - Traj2Stroke 只有 7 个可学参数，粗细随笔高仿射变化；
  - 分布外轨迹上的平均 L1：Sharpie 0.00055（CNN 0.00107），细画笔 0.00158（CNN 0.00162），加 U-Net 后 0.00153；
  - U-Net 能学到刷毛拖曳的纹理，但损害分布外泛化，最终没有采用；
  - 每种画具采集约 1 小时、训练约 20 分钟。
- **IMPASTO**：
  - 以当前画布、法向力 F 和平面内朝向为条件的 U-Net 像素动力学模型，加滚动时域 MPC；
  - 900 条自对弈样本时 L1 0.0285；5 位画家各 12 条单笔上，执行阶段加权 L1 比 FRIDA-CNN 低 19.48%、LPIPS 低 35.36%；
  - 笔垂直于画布；作者指出真实笔与颜料的交互本身是随机的，公平比较必须匹配笔的状态和颜料条件。
- **CoFRIDA**：用 FRIDA 的笔画模型批量生成机器人可执行的训练对。
- **Bidgoli 2020**：730 多条人类笔画配六自由度笔运动，VAE 只生成图像，不是动作到图像的前向模型。
- **共同点**：
  - 没有一个前向模型以笔杆倾角为输入；
  - 铺毫在所有模型里都只是"宽度"这一个标量；
  - 飞白只以学到的纹理出现，没有模型以干湿状态为条件；
  - 墨量只有 RealBrush Ink 用一个标量状态（累计路径长度）表示。
- **数据量**：FRIDA 约 100 条，Spline-FRIDA 每种画具约 1 小时，IMPASTO 900 条，RealBrush Ink 1,818 条（未见发布）；公开的配对数据只有 StrokeDiff 的 520 条油画笔画（没有轨迹），本轮没有找到带倾角的公开配对数据。

## 7. 笔法现象的覆盖

记号：✓ 显式建模；△ 部分建模、启发式或只在静态下；✗ 不建模；— 不适用。"对照"指与真实笔迹的比较方式。

| 模型类（代表） | 侧锋 | 提按 | 铺毫 | 飞白 | 墨量 | 对照 |
|---|---|---|---|---|---|---|
| 参数笔印（Droplet） | ✗ | ✓ | ✗ | 纹理库 | 参数 | 视觉 |
| 倒锥笔印（Virtual Brush） | ✗ | ✓ | ✗ | ✓ | ✓ | 视觉 |
| 实测笔印（Lam09、CCD-BSMG） | △ | ✓ | △ | ✗ | ✗ | 图像相似度 |
| 集总动力学（Karimov24 Brush） | ✗ | ✓ | △ | ✗ | △ | 毫米级 |
| 准静态脊线（Chu-Tai VCB） | ✓ | ✓ | ✓ | ✓ | ✓ | 视觉 |
| 查表脊线（Baxter-Govindaraju） | △ | ✓ | △ | ✗ | ✗ | 无 |
| 逐根笔毫（DiVerdi、WetBrush） | 未报告 | ✓ | ✓ | △ | ✓ | 视觉 |
| 学习式（Spline-FRIDA） | ✗ | ✓ | △ | △ | ✗ | L1 |
| 学习式（RealBrush Ink） | ✗ | ✗ | ✗ | △ | ✓ | LPIPS、SSIM |
| 墨纸扩散（MoXi） | — | — | — | △ | ✓ | 视觉 |

- 实测笔印的侧锋只在静态按压下标定：Lam09 到 50°，CCD-BSMG 和 Wang-Min21 到 10°。
- 毫米级的对照只有 Karimov24 Brush（转角）和 e-David Replication（宽度）。
- 通用的杆、FEM、MPM 模拟（§5）没有用于毛笔并与真实笔迹对照的例子。

## 8. 横向趋势

- **准静态代替完整动力学**：图形学毛笔每帧求平衡或去掉惯性（Chu-Tai VCB、Baxter-Lin Brush、DiVerdi Bristles、WetBrush），机器人一侧用闭式或松弛模型（Karimov24 Brush、Robot Calligraphy POC），理由都是笔毫惯性小、阻尼大、刚度高。
- **把解析或物理模型蒸馏成网络**：Wu Oil-GAN 用物理模拟数据，CCD-BSMG、B-BSMG 用解析笔画模型，Neural Painters 用 MyPaint，换取可微和速度；精度上限是被蒸馏的模型。
- **少参数骨架加学习**：Spline-FRIDA 的 7 参数 Traj2Stroke、OnOff 的 6 参数笔刷、Baxter-Govindaraju Brush 的 15 项表，都以少量参数换样本效率和泛化。
- **从真实毛笔取数据**：从 Drawing Prism、FluidPaint、RealBrush 的真实笔印和笔画样例，到 RealBrush Ink、FRIDA、IMPASTO 的机器人采集；带倾角的采集只有 Lam09、CCD-BSMG 的静态按压。
- **验证从视觉走向图像指标**：图形学几乎都是视觉对照，机器人与学习模型用余弦、SSIM、L1、LPIPS；毫米级的几何误差只有 Karimov24 Brush 和 e-David Replication。
- **倾斜在图形学里先于机器人**：Chu-Tai VCB 2004 年就有 6 自由度输入和偏锋；机器人一侧的倾斜模型只有静态笔印（Lam09、Wang-Min21、CCD-BSM、Guo25）和几何（Gülzow24）；学习模型都没有倾角输入。
- **引擎开始提供杆模型，但没有毛笔**：MuJoCo 2026 年给 1D flex 加入 DER，Newton 有 VBD 缆绳与 Dahl 迟滞；六个引擎都没有毛笔或笔毫束模型（§5.4）。

## 9. 文献自述的开放问题

- 图形学毛笔与墨：
  - 墨在纸上的扩散（Chu-Tai VCB 摘要；后由 MoXi 处理）
  - 倒锥笔印做不出偏锋；体积穿透纸面导致笔印不真实（Chu Thesis §2.2，评 Virtual Brush 与 Xu Solid Brush）
  - 笔内的墨扩散、直观的蘸色方式（Chu Thesis §2.6）
  - 逐根笔毫模拟达不到真实毛笔的上千根；笔毫塑性带来工作流问题，从产品版中去掉（DiVerdi Bristles）
  - 低端硬件上性能不够；颜色混合模型过于简单（WetBrush）
  - 更高输出分辨率、用拉格朗日粒子表现很细的条纹、同时只能有三种颜料、帧率未含笔形变（MoXi §7–8）
  - 数据驱动的笔不能复现所有形变，不含各向异性摩擦和塑性（Baxter-Govindaraju Brush §5）
  - 笔毫软硬不一、随机分叉、扭转；叠笔和一笔之内墨色渐变；宣纸纤维结构与墨的传输机理（Huang 2019 FITEE §5）
- 机器人毛笔模型：
  - 需要"more predictable brush models"和围绕优化轨迹的反馈；复杂笔画后笔尖"may become messy"，靠砚台复位（Robot Calligraphy POC §V.G、§VII）
  - 只考虑竖直握笔，加倾角需要多角度标定；抬笔时笔毫前移；笔画后笔毫保持反向弯曲、影响下一笔；恒压下宽度漂移；像素重叠作精度指标"not very satisfactory"（Zingrebe23 §5）
  - 迟滞随湿度变化、衰减未建模；自动标定、平头笔、带模型的实时规划（Karimov24 Brush §5）
  - 生成器是黑箱；旋转和运动中的变形、到 6 自由度位姿的映射留作后续（CCD-BSMG §V）
  - 轨迹模型"nonlinear and highly complicated"，建议按笔的尺寸用神经网络或决策树映射位移和高度到宽度、滞后与角度（Lin20 §5.2）
  - 墨耗尽时要逐笔预测干笔量（Karimov24 Dry）
  - 无法控制单根笔毫的属性，枯笔只能靠墨量和笔画面积间接控制（Jin23 Ink）
  - 工具模型不精确，缺少真实环境中的训练（CalliRewrite §V）
  - 纸上墨扩散模型、起笔收笔、动态建模与参数辨识（Lo06）
- 物理仿真：
  - XPBD 不收敛时材料变软（Direct XPBD Rods）
  - 时间步受横向冲击下拉伸模态的强非线性限制（Kaufman ANL）
  - 参数标定靠视觉判断；需要时间步要求更宽松、又能正确处理毛发间物理的模型（Wet Hair）
  - 混合 SOCCP 求解器不保证收敛，可能穿透；参数采集需要专门的实验装置（Creamy Strands）
  - 部分流行模拟器在最简单的摩擦接触场景就失败（Romero Validation）
  - 摩擦的稳健性（DisMech README 待办）
  - `ipc` 接触无摩擦、只支持 2D flex、不支持精确回放；MuJoCo Warp 的 flex 是 experimental（MuJoCo 4.0、MuJoCo Warp 文档）
  - 物理正确的毛笔效应模型和最佳标定方法"has not been presented in the literature"（Karimov24 Brush）
- 学习式模型：
  - 湿画法的渗化明显不如参考，需要表示湿度的递归模型；整幅画布输入限制分辨率（RealBrush Ink §6）
  - 笔刷参数不是物理单位；省略三维笔刷动力学、湿度扩散和纸张吸收；压力来自速度代理（OnOff §3.1、§6）
  - 缺少水彩、水墨的专门数据集（StrokeDiff §6.2）
  - 笔上颜料量是最主要的未建模变量（FRIDA）
  - 真实笔与颜料的交互本身是随机的，公平比较要匹配笔的状态（IMPASTO）

## 10. 现有综述的分类对照

- **Huang 2019 FITEE**：把虚拟毛笔分为经验式（接触面积）与物理式两类，并分别讨论笔–纸、纸–墨模型与输入设备。经验式对应本文"笔的表示"轴上的无状态笔印（§2.1、§2.2），物理式对应脊线与逐根笔毫（§2.3）。它不覆盖机器人书法的毛笔模型、物理引擎和学习式模型。它还指出数位板只能有限地检测笔杆倾斜。
- **Zhang 2024 JCST**：按"六法"整理 92 篇国画计算方法，主要是风格化与生成，毛笔物理只占很小一部分。
- **robot-painting-reproduction**：其 §6.3 刷毛模型、§6.5 学习的与可微的笔画渲染器与本文 §2.3、§6 重叠，侧重油画颜料；本文侧重毛笔与墨。

## 11. 入门阅读顺序

1. Huang 2019 FITEE：虚拟毛笔的全景和自述缺口。
2. Hairy Brushes：笔、笔画、蘸墨、纸的拆分。
3. Chu-Tai VCB，配合 Chu Thesis 第 2、3 章：表达最全的准静态脊线毛笔，含偏锋、铺毫、飞白和墨，以及帧率表和笔到纸的耦合。
4. Baxter-Govindaraju Brush：以笔高和攻角为输入、由真实毛笔建表的最便宜的形变笔。
5. DiVerdi Bristles：逐根笔毫在接触下保持稳定的做法，以及屈曲振荡的报告。
6. MoXi：墨在吸水纸中的参考模型。
7. Karimov24 Brush：唯一在转角上做了毫米级验证的逐步更新模型，附三种标定方法。
8. Robot Calligraphy POC：带状态的毛笔模型放进轨迹优化，以及对 sim-to-real 差距的分析。
9. Lam09，再读 CCD-BSMG 与 Guo25：倾斜笔印的实测与笔法的笔杆运动。
10. Karimov24 Dry：机器人上实测的墨量递减规律。
11. Spline-FRIDA，再读 RealBrush Ink：少参数可学笔画模型与真实墨笔画数据。
12. Direct XPBD Rods 与 Romero Validation：杆求解器为什么对迭代敏感，以及怎样验证。
