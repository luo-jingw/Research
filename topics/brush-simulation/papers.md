# brush-simulation 论文目录

- 快照日期：2026-11-24
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment 字段、Crossref 记录、出版方页面或论文集确认的发表处；"预印本"表示未找到发表处。
- 标 † 的条目有未核实的元数据或内容（只读到摘要或 TLDR、全文不可得、发表处未确认），见根目录 `issues.md` → ISSUE-009。
- 1990–2015 年的图形学与机器人论文多数没有 arXiv 版本，给出 DOI。
- 与 [vla-drawing-writing](../vla-drawing-writing/papers.md)、[robot-painting-reproduction](../robot-painting-reproduction/papers.md) 重复的论文沿用其简称（dAb、Baxter-Lin Brush、WetBrush、MoXi、FRIDA、Spline-FRIDA、IMPASTO、RealBrush Ink 等）。
- 分节对应 [survey.md](survey.md) 的分类；一篇论文只列在主归属的一节。

## 1. 图形学的虚拟毛笔

### 1.1 印章、笔印与骨架

- **Brush Extrusion** · 1983 · SIGGRAPH 1983 · [DOI](https://doi.org/10.1145/800059.801144)
  - Anti-aliased line drawing using brush extrusion
  - 笔刷沿路径拖动、线型由笔刷决定的印章模型的起点
- **Skeletal Strokes** · 1994 · SIGGRAPH 1994 · [DOI](https://doi.org/10.1145/192161.192186)
  - Drawing and animation using skeletal strokes
  - 把任意图片沿路径变形成笔画；Chu Thesis 指出毛笔笔画需要大量样例且在高曲率处失效
- **Pudet Pressure Strokes** · 1994 · Computer Graphics Forum 13(3) · [DOI](https://doi.org/10.1111/1467-8659.1330205)
  - Real Time Fitting of Hand-Sketched Pressure Brushstrokes
  - 压力到变宽轮廓，用 Bézier 实时拟合
- **Droplet**† · 2002 · WACV 2002；J. Computer Science and Technology 19(3)（2004） · [DOI](https://doi.org/10.1109/ACV.2002.1182203) · [DOI](https://doi.org/10.1007/BF02944909)
  - The droplet virtual brush for Chinese calligraphic character modeling；Droplet: A virtual brush model to simulate Chinese calligraphy and painting
  - 二维参数化水滴形笔印，参数含速度、湿度和压力，可合并与分裂；有意回到规则驱动的二维笔印
- **Camshaft Brush** · 2015 · CAD/Graphics 2015 · [DOI](https://doi.org/10.1109/CADGraphics.2015.17)
  - Modeling Virtual Chinese Brush Using Camshaft Curve and Stochastic Process
  - 解析"凸轮曲线"笔印加离散随机的颜料转移；作者称与真迹的差别"perceptually invisible"（视觉判断）
- **Guo Force-Feedback Brush** · 2015 · Math. Problems in Engineering 2015；FITEE 18(11)（2017）；Proc. SPIE 10225（2017） · [DOI](https://doi.org/10.1155/2015/164821) · [DOI](https://doi.org/10.1631/FITEE.1601283) · [DOI](https://doi.org/10.1117/12.2266338)
  - A virtual 3D interactive painting method for Chinese calligraphy and painting based on real-time force feedback technology，及同组 2015、2017 年的笔画与半干笔论文
  - 力驱动的弹簧质点笔变形成二维笔印，沿路径叠印；飞白由"半干值"从半干纹理库中选取
- **An-Liu Half-dry** · 2018 · IEEE ICCC 2018；CISP-BMEI 2020 · [DOI](https://doi.org/10.1109/CompComm.2018.8780952) · [DOI](https://doi.org/10.1109/CISP-BMEI51763.2020.9263592)
  - Modeling of Chinese Brush Deformation Behaviors and Real-time Simulation of Half-dry Strokes，及 2018 年的沉浸式毛笔
  - 蒙皮网格的弯曲、扭转、压平、分叉，加墨迹纹理库合成飞白

### 1.2 笔毫集合

- **Hairy Brushes** · 1986 · SIGGRAPH 1986 · [DOI](https://doi.org/10.1145/15922.15911)
  - Hairy brushes
  - 把问题拆成笔（一组各带墨量的笔毫）、笔画（位置加压力）、蘸墨和纸，逐根笔毫的墨量变化产生条纹
- **Ip-Wong Brush** · 1997 · CGI 1997 · [DOI](https://doi.org/10.1109/CGI.1997.601261)
  - Calligraphic character synthesis using a brush model
  - 第一个有物理动机的书法毛笔：笔的几何、沿轨迹的姿态、墨的吸收与沉积；摘要列出变宽、灰度、干笔的"black and white trails"
- **Virtual Brush**† · 2000 · Computers & Graphics 24(1) · [DOI](https://doi.org/10.1016/S0097-8493(99)00141-7)
  - Virtual brush: a model-based synthesis of Chinese calligraphy
  - Ip-Wong Brush 的期刊版；毛笔是倒锥，笔印取锥体与纸面的交，Chu Thesis 指出它做不出偏锋笔画
- **Lee Black-Ink**† · 1997 · Computer Networks and ISDN Systems 29(14)；IEEE CG&A 19(3)（1999） · [DOI](https://doi.org/10.1016/S0169-7552(97)00073-1) · [DOI](https://doi.org/10.1109/38.761553)
  - Physically-based modeling of brush painting；Simulating oriental black-ink painting
  - 笔毫是弹性杆，对力作弹性响应；Chu Thesis 指出均匀弹性导致不自然的弯曲

### 1.3 三维形变笔束

- **Saito-Nakajima Brush**† · 1999 · SIGGRAPH 1999 Conference Abstracts and Applications · [DOI](https://doi.org/10.1145/311625.312110)
  - 3D physics-based brush model for painting
  - 最早的 Bézier 脊线加圆盘、准静态能量最小化毛笔，一页摘要
- **dAb** · 2001 · SIGGRAPH 2001 · [DOI](https://doi.org/10.1145/383259.383313)
  - DAB: interactive haptic painting with 3D virtual brushes
  - 弹簧质点三维笔刷加力反馈与双层颜料转移，面向西洋颜料
- **Chu-Tai Efficient Brush** · 2002 · Pacific Graphics 2002 · [DOI](https://doi.org/10.1109/PCCGA.2002.1167885)
  - An efficient brush model for physically-based 3D painting
  - 骨架加表面，由约束能量最小化变形，含压平、侧向摩擦导致的铺毫、湿笔塑性和纸孔阻力；SQP 一般少于 10 次迭代
- **Xu Solid Brush** · 2002 · Computer Graphics Forum 21(3) · [DOI](https://doi.org/10.1111/1467-8659.00589)
  - A Solid Model Based Virtual Hairy Brush
  - 笔毫簇写成 NURBS 扫掠体"书写图元"，可分叉；Chu Thesis 指出体积穿透纸面导致笔印不真实
- **Yeh Haptic Brush** · 2002 · Pacific Graphics 2002 · [DOI](https://doi.org/10.1109/PCCGA.2002.1167892)
  - On the effects of haptic display in brush and ink simulation for Chinese painting and calligraphy
  - 弯曲弹簧笔毫加墨水转移，初步用户实验显示力反馈更好
- **Xu Advanced Brush** · 2003 · Computer Graphics Forum 22(3) · [DOI](https://doi.org/10.1111/1467-8659.t01-2-00701)
  - Advanced Design for a Realistic Virtual Brush
  - 分层笔几何、离线标定的笔运动和颜料分子扩散模型
- **Chu-Tai VCB** · 2004 · IEEE CG&A 24(5) · [DOI](https://doi.org/10.1109/MCG.2004.37) · [项目](https://cse.hkust.edu.hk/VCB/)
  - Real-Time Painting with an Expressive Virtual Chinese Brush
  - 脊线加侧向节点的笔束每帧用 SQP 求准静态平衡，6 自由度输入；含偏锋、铺毫（最多 5 个子笔束）、塑性、由真实干笔印做的干笔图；墨在纸上的扩散留作后续
- **Baxter-Lin Brush** · 2004 · Pacific Graphics 2004 · [DOI](https://doi.org/10.1109/PCCGA.2004.1348363)
  - A Versatile Interactive 3D Brush Model
  - 几根优化求解的脊线带动细分曲面和最多 200 条插值笔毫带，含各向异性摩擦、塑性和笔尖散开
- **Girshick Hairy Brush**† · 2004 · SIGGRAPH 2004 Posters · [DOI](https://doi.org/10.1145/1186415.1186442)
  - Simulating Chinese brush painting: the parametric hairy brush
  - 海报级的参数化三维毛笔，动力学按规则给出
- **Xu Hairy Brush**† · 2004 · Graphical Models 66(5)；Science in China Series F 48(3)（2005） · [DOI](https://doi.org/10.1016/j.gmod.2004.05.006) · [DOI](https://doi.org/10.1360/03yf0389)
  - Virtual hairy brush for painterly rendering；Virtual hairy brush for digital painting and calligraphy
  - Xu Solid Brush 一系的期刊版本
- **Chu Thesis** · 2007 · 香港科技大学博士论文 · [PDF](http://visgraph.cse.ust.hk/MoXi/ChuPhDThesis2007.pdf)
  - Making Digital Painting Organic
  - Chu-Tai VCB 与 MoXi 的完整细节；第 2 章给出能量项、偏锋所需的纸孔阻力、干笔图与帧率表，第 3 章给出笔到纸的供水公式
- **Bai Brush**† · 2007 · Frontiers in Algorithmics（LNCS） · [DOI](https://doi.org/10.1007/978-3-540-73814-5_25)
  - An Efficient Physically-Based Model for Chinese Brush
  - Huang 2019 FITEE 称其为锥形笔加弹簧网格
- **Van Laerhoven Brush** · 2007 · The Visual Computer 23(9–11) · [DOI](https://doi.org/10.1007/s00371-007-0158-z)
  - Brush up your painting skills: Realistic brush design for interactive painting applications
  - 与 Baxter-Lin Brush 类似的能量优化笔
- **DiVerdi Bristles** · 2010 · VRST 2010 · [DOI](https://doi.org/10.1145/1889863.1889889)
  - Industrial-strength painting with a virtual bristle brush
  - 每根笔毫是去掉扭转的 DER，在笔管的非惯性系中模拟并去掉惯性项；50 根笔毫每次印章物理约 0.5 ms；作者报告笔毫被竖直压下屈曲时后向欧拉出现振荡，改用投影
- **Chu Detail-Preserving** · 2010 · NPAR 2010 · [DOI](https://doi.org/10.1145/1809939.1809943)
  - Detail-preserving paint modeling for 3D brushes
  - 笔下的二维拾取图加画布快照，保留细条纹
- **WetBrush** · 2015 · ACM TOG 34(6) · [DOI](https://doi.org/10.1145/2816795.2818066)
  - Wetbrush: GPU-based 3D Painting Simulation at the Bristle Level
  - 40–600 根笔毫、每根 10 个顶点，惯性项按 β_B ∈ [0, 0.1] 缩放，笔毫聚拢用最小密度约束代替碰撞；GTX TITAN X 上 30–110 fps
- **Huang-Hou Brush**† · 2020 · Math. Problems in Engineering 2020 · [DOI](https://doi.org/10.1155/2020/6942947)
  - A Novel Virtual 3D Brush Model Based on Variable Stiffness and Haptic Feedback
  - 变刚度弯曲弹簧毛笔加力反馈；内容未读

### 1.4 来自真实毛笔的数据

- **Drawing Prism** · 1985 · SIGGRAPH 1985 · [DOI](https://doi.org/10.1145/325334.325202)
  - The drawing prism: a versatile graphic input device
  - 用棱镜面拍摄真实工具的光学接触笔印，是"以真实笔印为基准"的源头
- **FluidPaint** · 2008 · IEEE TABLETOP 2008；ITS 2009 · [DOI](https://doi.org/10.1109/TABLETOP.2008.4660185) · [DOI](https://doi.org/10.1145/1731903.1731914)
  - IntuPaint；FluidPaint: an interactive digital painting system using real wet brushes
  - 实时成像真实湿笔的笔印，颜料是模拟的，笔印是真实的
- **Baxter-Govindaraju Brush** · 2010 · ACM I3D 2010 · [DOI](https://doi.org/10.1145/1730804.1730826)
  - Simple data-driven modeling of brushes
  - 以笔毫根部离纸高度和攻角为输入的二维查找表，15 个表项由真实毛笔视频逐帧手描，6 个即可用；一根脊线 10 µs 内求出，比优化式快 5–45 倍；不含塑性和各向异性摩擦
- **RealBrush** · 2013 · ACM TOG 32(4) · [DOI](https://doi.org/10.1145/2461912.2461998) · [项目](https://gfx.cs.princeton.edu/pubs/Lu_2013_RPW/)
  - RealBrush: Painting with Examples of Physical Media
  - 从扫描的真实笔画样例合成新笔画，避开物理模拟；扫描数据公开（224 MB），用户研究评测；不含水墨

## 2. 墨、水与纸

### 2.1 吸水纸中的扩散与渗化

- **Sumie Diffusion** · 1991 · Modeling in Computer Graphics（Springer） · [DOI](https://doi.org/10.1007/978-4-431-68147-2_21)
  - Modeling the Diffuse Paintings of 'Sumie'
  - MoXi 称之为第一个东方墨扩散模型：不同大小的颜料粒子、一维滤波
- **Kunii Diffusion** · 1995 · Computer Animation 1995；Int. J. Shape Modeling 7(1)（2001） · [DOI](https://doi.org/10.1109/CA.1995.393542) · [DOI](https://doi.org/10.1142/S0218654301000047)
  - A diffusion model for computer animation of diffuse ink painting；Two-dimensional diffusion model for diffuse ink painting
  - 多维扩散方程，含墨晕的强度"singularities"；摘要称与真实图像"exactly the same intensity distribution"，未给比较方法
- **Zhang Ink CA** · 1999 · J. Visualization and Computer Animation 10(1) · [DOI](https://doi.org/10.1002/(SICI)1099-1778(199901/03)10:1<27::AID-VIS194>3.0.CO;2-C)
  - Simple cellular automaton-based simulation of ink behaviour and its application to Suibokuga-like 3D rendering of trees
  - 水与墨粒子的二维元胞自动机，表现渗化、浓淡和枯笔（Kasure）
- **Lee Ink Diffusion**† · 2001 · Computers & Graphics 25(2) · [DOI](https://doi.org/10.1016/S0097-8493(00)00132-1)
  - Diffusion rendering of black ink paintings using new paper and ink models
  - 纤维网格纸上的扩散，只处理前沿以求速度
- **Yu Oriental Painting** · 2002 · Pacific Graphics 2002 · [DOI](https://doi.org/10.1109/PCCGA.2002.1167898)
  - A model based technique for realistic oriental painting
  - 局部平衡模型，纤维网格纸每格 3 层，支持叠笔
- **Nijimi** · 2003 · CGI 2003 · [DOI](https://doi.org/10.1109/CGI.2003.1214460)
  - "Nijimi" rendering algorithm for creating quality black ink paintings
  - 墨向吸水纸动态扩散加枯笔渲染；个人电脑上 20 笔约 30 s
- **MoXi** · 2005 · ACM TOG 24(3) · [DOI](https://doi.org/10.1145/1073204.1073221) · [项目](http://visgraph.cse.ust.hk/MoXi/)
  - MoXi: Real-Time Ink Dispersion in Absorbent Paper
  - 改进的格子 Boltzmann 水流，表层、流动层、固着层三层水与颜料；512² 模拟（输出 1536²）44 fps、256² 70 fps，帧率不含同时进行的笔形变；项目页发布了水流的 Cg 代码
- **Sun Xuan Paper** · 2005 · CGIV 2005 · [DOI](https://doi.org/10.1109/CGIV.2005.59)
  - Physical Modeling of "Xuan" Paper in the Simulation of Chinese Ink-Wash Drawing
  - 随机纤维的纸单元，参数含密度、吸水性和纹理
- **Wang-Rokne Ink** · 2007 · GRAPP 2007 · [DOI](https://doi.org/10.5220/0002071902710276)
  - Pressure based ink diffusion model for real-time simulation of Chinese calligraphy
  - 毛细网络中的 Darcy 压力驱动扩散，含沉积层、冲淡、不规则边缘
- **Sun Ink Simulator** · 2010 · ICMT 2010 · [DOI](https://doi.org/10.1109/ICMULT.2010.5629733)
  - Physical Modeling Based Graphical Simulator of Water-Ink Diffusion and Multi-Stroke Superposition
  - 布朗加毛细的粒子运动、蒸发、沉积和多笔叠加
- **Xu Ink Diffusion** · 2011 · VRCAI 2011 · [DOI](https://doi.org/10.1145/2087756.2087770)
  - Interactive visual simulation of dynamic ink diffusion effects
  - 网格与粒子混合的墨，GPU 交互
- **Shin Ink 3D** · 2013 · JACIII 17(4) · [DOI](https://doi.org/10.20965/jaciii.2013.p0598)
  - Ink Diffusion Simulation for 3D Virtual Calligraphy
  - 墨滴模型，扩散随墨浓度和水量变化，实时
- **Fan-Li Xuan** · 2014 · Proc. SPIE 9069 · [DOI](https://doi.org/10.1117/12.2049943)
  - Simulation of ink diffusion on Xuan paper
  - 扩散系数随纤维权重和局部墨量变化的扩散方程，隐式差分，线性时间
- **Yhang Capillary** · 2015 · SIGGRAPH Asia 2015 Posters · [DOI](https://doi.org/10.1145/2820926.2820947)
  - Simulating water dispersion in chinese absorbent paper with capillary tubes model
  - 毛细管膜中的 Darcy 流
- **Wang Ink Wash** · 2018 · J. Physics: Conference Series 1004 · [DOI](https://doi.org/10.1088/1742-6596/1004/1/012026)
  - Ink Wash Painting Style Rendering With Physically-based Ink Dispersion Model
  - GPU 多孔介质扩散，用于三维非真实感渲染
- **Liao-Zhang Ink** · 2024 · Proc. SPIE（EIBDCT 2024） · [DOI](https://doi.org/10.1117/12.3031372)
  - Real-time ink diffusion simulation in digital ink painting
  - 接触层与扩散层双层纸，改进的系数扩散方程

### 2.2 水性颜料的参考模型

- **Curtis Watercolor** · 1997 · SIGGRAPH 1997 · [DOI](https://doi.org/10.1145/258734.258896)
  - Computer-generated watercolor
  - 浅水加 Kubelka–Munk 的水彩参考模型；MoXi 指出其干湿边界固定、没有渗透
- **Van Laerhoven Watery Paint** · 2005 · Computer Animation and Virtual Worlds 16(3–4) · [DOI](https://doi.org/10.1002/cav.95)
  - Real-time simulation of watery paint
  - 分层画布的 GPU 水彩，含东方墨的深色边缘与湿接湿
- **Wang-Wang Color Ink** · 2007 · IEEE TVCG 13(2) · [DOI](https://doi.org/10.1109/TVCG.2007.41)
  - Image-Based Color Ink Diffusion Rendering
  - 基于图像的彩墨扩散，无笔画
- **You Paint** · 2013 · Computer Animation and Virtual Worlds 24(3–4) · [DOI](https://doi.org/10.1002/cav.1500)
  - Realistic paint simulation based on fluidity, diffusion, and absorption
  - SPH 流动、Fick 扩散和 Lucas–Washburn 吸收
- **Ďurikovič Watercolor** · 2017 · IV 2017 · [DOI](https://doi.org/10.1109/iV.2017.10)
  - Real-Time Watercolor Simulation with Fluid Vorticity Within Brush Stroke
  - GPU 上带涡量的 Navier–Stokes，纸面粗糙度进入黏性项

### 2.3 真实墨、纸与笔毫的材料测量

- **Wu Qianlong Xuan**† · 2016 · J. Materials Science & Technology 32(2) · [DOI](https://doi.org/10.1016/j.jmst.2015.12.014)
  - Ink Dispersion on Qianlong Xuan Paper with Improved Ink Expression
  - 乾隆宣纸上的墨扩散测量，未与模拟器对照
- **Liu GO Ink** · 2024 · Nordic Pulp & Paper Research J. · [DOI](https://doi.org/10.1515/npprj-2023-0041)
  - Penetration and spreading of graphene oxide ink in rice paper enabling its unique expressiveness in Chinese paintings
  - 墨在宣纸中的渗透与铺展测量
- **Liu-Liu Brush Hair** · 2025 · npj Heritage Science · [DOI](https://doi.org/10.1038/s40494-025-02005-1)
  - Analyzing the intrinsic connection between Chinese calligraphy creation and brush properties from a micro perspective
  - 笔毫微观结构与吸墨性测量

## 3. 机器人书法与机器人绘画的毛笔模型

### 3.1 实测与几何笔印模型

- **Lo06** · 2006 · IROS 2006 · [DOI](https://doi.org/10.1109/IROS.2006.281655)
  - Brush Footprint Acquisition and Preliminary Analysis for Chinese Calligraphy using a Robot Drawing Platform
  - 玻璃板下方的相机采集笔印，椭圆长短轴随下压深度（0 至 −8.5 mm）变化，沿路径取笔印并集；速度 7.5–19 mm/s 对笔印影响不大
- **Kwok06**† · 2006 · CASE 2006 · [DOI](https://doi.org/10.1109/COASE.2006.326926)
  - Evolutionary Replication of Calligraphic Characters By A Robot Drawing Platform Using Experimentally Acquired Brush Footprint
  - 实测笔印加遗传算法搜索书写轨迹
- **Lam09** · 2009 · IROS 2009 · [DOI](https://doi.org/10.1109/IROS.2009.5354709)
  - Stroke trajectory generation experiment for a robotic Chinese calligrapher using a geometric brush footprint model
  - 8 顶点多边形笔印，每个顶点是下压深度与倾角的三次函数；在纸上标定倾角 5–50°、深度 1–15 mm，是倾角范围最宽的实测笔印模型
- **Lam11**† · 2011 · CogInfoCom 2011 · 无链接
  - Application of Brush Footprint Geometric Model for Realization of Robotic Chinese Calligraphy
  - Lam09 的后续，发表处只见于他人参考文献
- **Fan18**† · 2018 · YAC 2018 · [DOI](https://doi.org/10.1109/YAC.2018.8406533)
  - Fine grained control of robotic calligraphy
  - 研究路径、下压深度和"笔滞后"对笔印的影响
- **Li19**† · 2019 · ICIRA 2019 · [DOI](https://doi.org/10.1007/978-3-030-27529-7_8)
  - Robot Brush-Writing System of Chinese Calligraphy Characters
  - 闵华松组的毛笔书写系统，Wang-Min21 的前身
- **Wang-Min21** · 2021 · 智能系统学报 16(4) · [DOI](https://doi.org/10.11992/tis.202006033)
  - 基于毛笔建模的机器人书法系统（Robot calligraphy system based on brush modeling）
  - 两段三次 Bézier 拼成水滴形笔印，尺寸是下降高度 h（8–20 mm）与倾角 α（0–10°）的线性函数；横画综合相似度经三版轨迹从 76.36% 升到 87.42%
- **CCD-BSM**† · 2022 · Applied Intelligence 53(11) · [DOI](https://doi.org/10.1007/s10489-022-04210-y) · [代码](https://github.com/LeafThink/CCD-BSM)
  - CCD-BSM: composite-curve-dilation brush stroke model for robotic chinese calligraphy
  - 斜圆锥截面加切线、按面积不变膨胀，得到随下压与倾角变化的笔印；代码仓库按名称匹配，论文中未给链接
- **CCD-BSMG** · 2023 · IEEE Access 11 · [DOI](https://doi.org/10.1109/ACCESS.2023.3333558)
  - CCD-BSMG: Composite-Curve-Dilation-Based Brush Stroke Model Generator for Robotic Chinese Calligraphy
  - 用 H、α、R、L 的闭式笔印生成仿真笔画，训练可微生成器；狼毫笔、宣纸、α = 0/5/10°，与真实样本的相似度最高 98.21%；完整真实数据需签协议获取
- **Yan23**† · 2023 · ICCSIP 2022（CCIS） · [DOI](https://doi.org/10.1007/978-981-99-0617-8_30)
  - Robot Calligraphy Based on Footprint Model and Brush Trajectory Extraction
  - 笔印模型加毛笔轨迹提取
- **B-BSMG**† · 2024 · Int. J. Computational Intelligence Systems 17(1) · [DOI](https://doi.org/10.1007/s44196-024-00499-4)
  - B-BSMG: Bézier Brush Stroke Model-Based Generator for Robotic Chinese Calligraphy
  - 两条对称三次 Bézier 的笔画模型由笔的物理特性和书写姿态决定，再蒸馏成生成器
- **Guo25** · 2025 · Electronics 14(15) · [DOI](https://doi.org/10.3390/electronics14153000)
  - Brush Stroke-Based Writing Trajectory Control Model for Robotic Chinese Calligraphy
  - CCD-BSM 笔印加转笔调锋、折笔、逆锋入笔、藏锋收笔的闭式笔杆运动；基本笔画余弦相似度 98.76–99.54%，"不""去"两字 SSIM 63.81% / 68.73%
- **Guo26**† · 2026 · Int. J. Computational Intelligence Systems 19(1) · [DOI](https://doi.org/10.1007/s44196-026-01222-1)
  - Three-Dimensional Trajectory Planning for Robotic Chinese Calligraphy: Conforming to Brush Stroke Dynamics
  - 按笔画阶段规划高度、速度和加速度

### 3.2 带状态的毛笔动力学模型

- **Robot Calligraphy POC** · 2019 · IROS 2020 · [arXiv 1911.08002](https://arxiv.org/abs/1911.08002) · [DOI](https://doi.org/10.1109/IROS45743.2020.9341787)
  - Robot Calligraphy using Pseudospectral Optimal Control in Conjunction with a Novel Dynamic Brush Model
  - 7 维毛笔状态：宽度与拖尾以惯性松弛到 Width(z)、Drag(z)，笔尖偏移靠摩擦保持、超限后突变；用伪谱最优控制优化轨迹，作者称仍有"considerable Sim2Real gap"
- **Lin20** · 2020 · Applied Sciences 10(23) · [DOI](https://doi.org/10.3390/app10238694)
  - Calligraphy Brush Trajectory Control of by a Robotic Arm
  - 按位移和高度索引的笔印库，加滞后 η(z) 与笔印角 φ；按压后的笔印在 3 / 5 / 6 mm 行程内（z = 1 / 2 / 3 mm）变窄趋稳，转折后笔印需一段距离重新对齐
- **Karimov24 Brush** · 2024 · Robotics 13(6) · [DOI](https://doi.org/10.3390/robotics13060094)
  - Physically Motivated Model of a Painting Brush for Robotic Painting and Calligraphy
  - 接触区沿 tractrix 追随笔杆，滞后 r(z)、笔尖间隙 b = k_b·z，加换向规则，用笔印图像库渲染；z = 10 mm 的 90° 转角 y 误差 ≤ 2%，并给出三种标定方法
- **Gülzow24** · 2024 · 康斯坦茨大学博士论文；Arts 11(4)（2022） · [DOI](https://doi.org/10.3390/arts11040077)
  - Robotic Painting with Region-Based Techniques；Region-Based Approaches in Robotic Painting
  - 笔毫绕笔管转动、笔尖落在圆弧上，侧向倾斜时由线圆交点算出笔尖超出量；可用倾角 15–45°

### 3.3 从机器人自身笔画拟合的模型

- **Mueller13**† · 2013 · IROS 2013 · [DOI](https://doi.org/10.1109/IROS.2013.6696583)
  - Robotic calligraphy — Learning how to write single strokes of Chinese and Japanese characters
  - 用相机图像迭代学习单笔轨迹，仿真中用简单毛笔模型
- **e-David Replication** · 2018 · Arts 7(4) · [DOI](https://doi.org/10.3390/arts7040084)
  - Self-Improving Robotic Brushstroke Replication
  - 由机器人自己的笔画建立压力到宽度的查找表，回归的最大宽度误差 0.5 mm，再用相机迭代修正轨迹
- **Zingrebe23** · 2023 · Robotics 12(3) · [DOI](https://doi.org/10.3390/robotics12030072)
  - Robotic Writing of Arbitrary Unicode Characters Using Paintbrushes
  - 用半圆标定网格拟合宽度与滞后随压力、曲率的变化并预补偿路径；作者写明只考虑竖直握笔
- **Jin23 Ink** · 2023 · IEEE RA-L 8(10) · [arXiv 2308.11187](https://arxiv.org/abs/2308.11187) · [DOI](https://doi.org/10.1109/LRA.2023.3311364)
  - A Semi-Automatic Oriental Ink Painting Framework for Robotic Drawing From 3D Models
  - 下降深度到线宽的线性拟合（R² 0.957），浓淡由蘸墨时间与比例控制，枯笔程度取笔画面积与吸墨量之比
- **Degradable Tools** · 2023 · IFAC World Congress 2023 · [arXiv 2305.16650](https://arxiv.org/abs/2305.16650)
  - Data-Driven Optimization for Deposition with Degradable Tools
  - 铅笔的力到沉积宽度加工具磨损状态，在线最小二乘更新；考虑磨损后沉积误差最多降低 65%
- **Karimov24 Dry** · 2024 · Izv. VUZ Priborostroenie 67(7)（俄文） · [DOI](https://doi.org/10.17586/0021-3454-2024-67-7-574-585)
  - Модель сухой кисти для робототехнической живописи (Dry brush model for robotic painting)
  - 宽度 w = k_w·Z + w0，笔画密度每笔按 α[i+1] = k·α[i] 衰减（k = 0.71–0.89），是唯一在机器人上实测的墨量递减与干笔模型

### 3.4 学习系统中的隐式毛笔

- **Sun14**† · 2014 · IROS 2014 · [DOI](https://doi.org/10.1109/IROS.2014.6943186)
  - Robot learns Chinese calligraphy from Demonstrations
  - 局部加权回归从笔画参数映射到 6 维笔轨迹，倾斜只来自示教
- **GAN Calligraphy**† · 2017 · ICRA 2018 · [DOI](https://doi.org/10.1109/ICRA.2018.8460787)
  - Generative Adversarial Nets in Robotic Chinese Calligraphy
  - Chao 等人用判别器评价机器人写出的笔画；同组后续有 Gao 2019 CAE-DE、Wu 2020 AC-GAN 等，摘要中看不到训练时的毛笔渲染方式
- **Gao 2019 CAE-DE**† · 2019 · Knowledge-Based Systems 182 · [DOI](https://doi.org/10.1016/j.knosys.2019.06.010)
  - A data-driven robotic Chinese calligraphy system using convolutional auto-encoder and differential evolution
  - 卷积自编码器的重建误差作笔画质量评价，差分进化搜索轨迹
- **Wu 2020 AC-GAN**† · 2020 · Neurocomputing 388 · [DOI](https://doi.org/10.1016/j.neucom.2020.01.043)
  - Integration of an actor-critic model and generative adversarial networks for a Chinese calligraphy robot
  - GAN 判别器作奖励训练 actor-critic 写字策略
- **HGN Virtual**† · 2020 · IEEE Access · [DOI](https://doi.org/10.1109/ACCESS.2020.2991767)
  - Deep Learning-Based Hypothesis Generation Model and Its Application on Virtual Chinese Calligraphy-Writing Robot
  - 虚拟书写环境中从图像生成书写动作
- **HGN Delta** · 2023 · IEEE Access · [DOI](https://doi.org/10.1109/ACCESS.2023.3252902)
  - A Chinese Calligraphy-Writing Robotic System Based on Image-to-Action Translations and a Hypothesis Generation Net
  - 从笔画图像生成含笔杆转角与倾角的五自由度动作（逆映射），修正加线性回归后平均绝对百分比误差小于 2%
- **Variational IL Calligraphy** · 2023 · 预印本 · [arXiv 2304.02801](https://arxiv.org/abs/2304.02801)
  - End-to-end Manipulator Calligraphy Planning via Variational Imitation Learning
  - 从图像和位姿生成三维轨迹与笔尖旋转，真机写日文书法
- **Sim-to-Real Brush** · 2023 · 预印本 · [arXiv 2309.08457](https://arxiv.org/abs/2309.08457)
  - Sim-to-Real Brush Manipulation using Behavior Cloning and Reinforcement Learning
  - MyPaint 作仿真器，真机由笔画图像标定压力范围；作者写明 3 自由度臂无法倾斜
- **CalliRewrite** · 2024 · ICRA 2024 · [arXiv 2405.15776](https://arxiv.org/abs/2405.15776) · [代码](https://github.com/LoYuXr/CalliRewrite)
  - CalliRewrite: Recovering Handwriting Behaviors from Calligraphy Images without Supervision
  - 毛笔简化为水滴形笔印 (r, l, θ)，l = 0.003 + 2.021·r，加三段式笔尖转向规则；z 与 r 由 8 点线性拟合

### 3.5 笔状态感知与力控制

- **Kob22**† · 2022 · AMC 2022 · [DOI](https://doi.org/10.1109/AMC51637.2022.9729276)
  - Motion-Copying System with Compensation of Environmental Changes for Calligraphy Robot
  - 把毛笔当作环境阻抗，复现人的书写运动
- **Chen24 Cable** · 2024 · IROS 2024 · [arXiv 2403.12214](https://arxiv.org/abs/2403.12214)
  - Architectural-Scale Artistic Brush Painting with a Hybrid Cable Robot
  - 写明不用复杂毛笔模型，每走 0.5 m 重新蘸墨
- **Flying Calligrapher** · 2024 · IEEE RA-L 9(12) · [arXiv 2407.05587](https://arxiv.org/abs/2407.05587)
  - Flying Calligrapher: Contact-Aware Motion and Force Planning and Control for Aerial Manipulation
  - 海绵笔，宽度随法向力变化；IoU 0.59，力 RMSE 0.7 N
- **Sch25**† · 2025 · Scientific Reports · [DOI](https://doi.org/10.1038/s41598-025-92081-x)
  - A neuromorphic electronic artist for robotic painting
  - 力–力矩反馈补偿笔刷形变，不建毛笔模型
- **CalliSense** · 2025 · CHI 2025 · [arXiv 2502.15883](https://arxiv.org/abs/2502.15883)
  - CalliSense: An Interactive Educational Tool for Process-based Learning in Chinese Calligraphy
  - 笔杆 IMU、拇指力传感器和相机记录人的书写过程

## 4. 笔毫与纤维的物理仿真

### 4.1 杆模型与求解器

- **Super-helices** · 2006 · ACM TOG 25(3) · [DOI](https://doi.org/10.1145/1141911.1142012)
  - Super-helices for predicting the dynamics of natural hair
  - 分段螺旋的约化坐标 Kirchhoff 杆，去掉刚性拉伸模态，可用大时间步；与真实头发运动对比
- **DER** · 2008 · ACM TOG 27(3) · [DOI](https://doi.org/10.1145/1360612.1360662)
  - Discrete Elastic Rods
  - 离散 Kirchhoff 杆：中心线动态、材料标架准静态，不可伸长由流形投影实现；后续笔毫与湿发工作的基础模型
- **DVT** · 2010 · ACM TOG 29(4) · [DOI](https://doi.org/10.1145/1778765.1778853)
  - Discrete Viscous Threads
  - 隐式 DER，带状 Hessian，弹性杆提速一个数量级；多数后续 DER 代码的求解基础
- **PBD-Cosserat** · 2016 · SCA 2016 · [DOI](https://doi.org/10.2312/sca.20161234) · [代码](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics)
  - Position and Orientation Based Cosserat Rods
  - 以四元数朝向约束表示 Cosserat 杆的弯曲与扭转，比早期 PBD 杆快一个数量级以上
- **Direct XPBD Rods** · 2018 · Computer Graphics Forum 37(6) · [DOI](https://doi.org/10.1111/cgf.13326)
  - Direct Position-Based Solver for Stiff Rods
  - 对树形结构做直接求解加少量 Newton 迭代；指出 Gauss–Seidel 式 XPBD 不收敛时材料"too soft"
- **VBD** · 2024 · ACM TOG 43(4) · [arXiv 2403.06321](https://arxiv.org/abs/2403.06321)
  - Vertex Block Descent
  - 对隐式欧拉变分目标做顶点级块坐标下降，任意迭代次数都稳定；Newton 的 SolverVBD
- **AVBD** · 2025 · ACM TOG 44(4) · [DOI](https://doi.org/10.1145/3731195)
  - Augmented Vertex Block Descent
  - 增广拉格朗日处理无穷刚度的硬约束，改善高刚度比下的收敛
- **Stable Cosserat Rods** · 2025 · SIGGRAPH 2025 Conference Papers · [DOI](https://doi.org/10.1145/3721238.3730618)
  - Stable Cosserat Rods
  - 位置与朝向分开优化，朝向用闭式准静态更新；作者称比 XPBD 和 DER 快且稳定"orders of magnitude"
- **Lie-group XPBD**† · 2026 · 预印本 · [arXiv 2608.23606](https://arxiv.org/abs/2608.23606)
  - Orientation in Extended Position-Based Dynamics: Application to Rigid Bodies and Cosserat Rods
  - 李群形式的 XPBD 朝向；线性有限元离散优于刚体链离散

### 4.2 接触、摩擦与验证

- **NSN** · 2011 · ACM TOG 30(1) · [DOI](https://doi.org/10.1145/1899404.1899410)
  - A nonsmooth Newton solver for capturing exact Coulomb friction in fiber assemblies
  - 精确 Coulomb 摩擦的非光滑 Newton 求解，再现纤维集合的粘滑
- **Daviet Hybrid** · 2011 · ACM TOG 30(6) · [DOI](https://doi.org/10.1145/2070781.2024173)
  - A hybrid iterative solver for robustly capturing Coulomb friction in hair dynamics
  - 接触级 Gauss–Seidel 加逐接触求根；数千根头发、数万个摩擦接触，与真实头发运动做视觉对比
- **FTL** · 2012 · VRIPHYS 2012 · [DOI](https://doi.org/10.2312/PE/vriphys/vriphys12/039-044)
  - Fast Simulation of Inextensible Hair and Fur
  - 几何式 follow-the-leader 投影，一次迭代保持不可伸长，实时模拟数千根头发
- **Kaufman ANL** · 2014 · ACM TOG 33(4) · [DOI](https://doi.org/10.1145/2601097.2601100)
  - Adaptive Nonlinearity for Collisions in Complex Rod Assemblies
  - 指出时间步受"拉伸模态对横向冲击的强非线性响应"限制，按需调整碰撞响应的非线性程度
- **Aniso-MPM** · 2017 · ACM TOG 36(4) · [DOI](https://doi.org/10.1145/3072959.3073623)
  - Anisotropic elastoplasticity for cloth, knit and hair frictional contact
  - 各向异性 MPM 表示纤维集合的摩擦接触，百万自由度每帧数十秒到数分钟
- **CIPC** · 2020 · ACM TOG 40(4) · [arXiv 2012.04457](https://arxiv.org/abs/2012.04457) · [代码](https://github.com/ipc-sim/Codim-IPC)
  - Codimensional Incremental Potential Contact
  - 带厚度的余维 IPC，保证杆中心线间距不小于设定厚度，离线方法
- **IMC** · 2021 · J. Applied Mechanics 88(5)；Extreme Mechanics Letters 58（2023） · [DOI](https://doi.org/10.1115/1.4050238) · [arXiv 2205.10309](https://arxiv.org/abs/2205.10309)
  - Implicit Contact Model for Discrete Elastic Rods in Knot Tying；A Fully Implicit Method for Robust Frictional Contact Handling in Elastic Rods
  - 全隐式罚函数摩擦接触，与 IPC 性能相当且收敛更快
- **Romero Validation** · 2021 · ACM TOG 40(4) · [DOI](https://doi.org/10.1145/3450626.3459931)
  - Physical validation of simulators in computer graphics: a new framework dedicated to slender elastic structures and frictional contact
  - 悬臂、弯扭耦合、粘滑的实验验证协议；部分流行模拟器在最简单的摩擦接触场景就失败，杆代码总体表现好
- **Daviet ADMM** · 2023 · SIGGRAPH 2023 Conference Proceedings · [DOI](https://doi.org/10.1145/3588432.3591551)
  - Interactive Hair Simulation on the GPU using ADMM
  - GPU 上带 Coulomb 摩擦的 DER，实时模拟数千根弹性杆，并复现悬臂、弯扭和粘滑实验
- **Frictional Elastica** · 2023 · Physical Review E 109 · [arXiv 2311.11504](https://arxiv.org/abs/2311.11504)
  - Indentation of an elastic arch on a frictional substrate: Pinning, unfolding and snapping
  - 压在摩擦平面上的弹性拱存在多个稳定构型和突跳，力出现不连续跳变
- **DisMech** · 2023 · IEEE RA-L 9(4) · [arXiv 2311.18126](https://arxiv.org/abs/2311.18126) · [代码](https://github.com/StructuresComp/dismech-rods)
  - DisMech: A Discrete Differential Geometry-Based Physical Simulator for Soft Robots and Structures
  - 全隐式 DER 加 IMC 接触的机器人杆仿真器，有与硬件对比的 real2sim 验证

### 4.3 湿笔毫、内聚与液体

- **Bico Coalescence** · 2004 · Nature 432 · [DOI](https://doi.org/10.1038/432690a)
  - Elastocapillary coalescence in wet hair
  - 湿毛刷在毛细桥作用下逐级聚拢的实验
- **Ratchet Hairs**† · 2014 · Advanced Materials 26(28) · [DOI](https://doi.org/10.1002/adma.201400865)
  - Chinese Brushes: Controllable Liquid Transfer in Ratchet Conical Hairs
  - 毛笔锥形、鳞片状毛发上的可控液体转移实验
- **Wet Hair** · 2017 · ACM TOG 36(4) · [DOI](https://doi.org/10.1145/3072959.3073630) · [代码](https://github.com/raymondyfei/libWetHair)
  - A multi-scale model for simulating liquid-hair interactions
  - DER 头发、APIC 液体和逐根约化液膜，液桥产生内聚；每步 3–57 s，参数"largely based on visual interpretation"
- **Creamy Strands** · 2019 · ACM TOG 38(6) · [DOI](https://doi.org/10.1145/3355089.3356532) · [代码](https://github.com/raymondyfei/creamystrand)
  - A multi-scale model for coupling strands with shear-dependent liquid
  - DER 纤维与剪切依赖液体耦合，内聚改用位移的二阶 Coulomb 锥；指出罚函数内聚需要精调刚度以避免不稳定和穿透
- **Rigid Brush Fluid Capture** · 2024 · J. Fluid Mechanics 1014 · [arXiv 2411.15970](https://arxiv.org/abs/2411.15970)
  - Optimal rigid brush for fluid capture
  - 毛刷提起时带走的液体量随提起过程非单调变化
- **Paintbrush Scaling** · 2026 · 预印本 · [arXiv 2609.39410](https://arxiv.org/abs/2609.39410)
  - The hidden side of paintbrushes: a geometry shaped by power laws
  - 数百支画笔的标度律；圆笔的颜料印大小随压缩距离标度，只取决于施力而不取决于笔的力学响应

### 4.4 引擎与机器人仿真器

- **MuJoCo 4.0** · 2026 · 文档 · [文档](https://mujoco.readthedocs.io/en/stable/modeling.html) · [更新日志](https://mujoco.readthedocs.io/en/stable/changelog.html)
  - MuJoCo documentation: deformable objects (flex), integrators, changelog 3.14–4.0.1
  - 3.17.0（2026-10-22）给 1D flex 加入无扭转的离散弹性杆弯曲，由 `discrete` 积分器隐式积分；4.0.0（2026-11-06）删除 cable 插件和 `composite`；`ipc` 无穿透接触只支持 2D flex 且无摩擦
- **MuJoCo Warp** · 2026 · 代码仓库文档 · [代码](https://github.com/google-deepmind/mujoco_warp)
  - MuJoCo Warp README: MuJoCo API compatibility
  - GPU 版 MuJoCo；flex 标为 experimental，不支持插件
- **Newton** · 2026 · 文档 · [文档](https://newton-physics.github.io/newton/latest/solvers/index.html)
  - Newton documentation: solvers, VBD, VBD tuning, deformable objects
  - SolverVBD 支持 ROD 关节连接的胶囊体缆绳与 Dahl 弯曲迟滞；调参页说明信息每次迭代传一圈邻居、未解完的部分变成速度
- **Genesis** · 2026 · 文档 · [文档](https://genesis-world.readthedocs.io/en/latest/user_guide/physics/beyond_rigid_bodies.html)
  - Genesis World documentation: beyond rigid bodies, soft solvers, IPC coupler
  - MPM、FEM、PBD、SPH，没有杆模型；IPC 耦合只覆盖 FEM 和布料
- **PhysX FEM** · 2026 · 文档 · [文档](https://nvidia-omniverse.github.io/PhysX/physx/latest/docs/DeformableVolume.html)
  - PhysX SDK documentation: Deformable Volume; Isaac Lab DeformableObject API
  - 体素仿真网格加贴合碰撞网格的四面体体积形变体，没有纤维方向
- **ManiSkill2** · 2023 · ICLR 2023 · [arXiv 2302.04659](https://arxiv.org/abs/2302.04659)
  - ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills
  - Warp MPM 软体任务中的 Write 是刚性棍压写 MPM 材料，不是毛笔
- **PlasticineLab** · 2021 · ICLR 2021 · [arXiv 2104.03311](https://arxiv.org/abs/2104.03311)
  - PlasticineLab: A Soft-Body Manipulation Benchmark with Differentiable Physics
  - DiffTaichi 弹塑性 MPM 基准，含 Writer 任务

## 5. 学习式与可微笔画模型

### 5.1 神经笔画渲染器与学画

- **SPIRAL** · 2018 · ICML 2018 · [arXiv 1804.01118](https://arxiv.org/abs/1804.01118)
  - Synthesizing Programs for Images using Reinforced Adversarial Learning
  - 智能体驱动 libmypaint 作画，渲染器不可微
- **Wu Oil-GAN** · 2018 · Expressive 2018 · [DOI](https://doi.org/10.1145/3229147.3229150)
  - Brush stroke synthesis with a generative adversarial network driven by physically based simulation
  - 用离线物理模拟器数据训练 GAN 作快速替代，输入含压力和颜料高度；RealBrush Ink 称之为 DeepBrush，用真实墨笔画重训作基线
- **StrokeNet**† · 2019 · ICLR 2019 · [代码](https://github.com/vexilligera/strokenet)
  - StrokeNet: A Neural Painting Environment
  - 用生成网络近似绘图程序以获得梯度
- **Learning to Paint** · 2019 · ICCV 2019 · [arXiv 1903.04411](https://arxiv.org/abs/1903.04411)
  - Learning to Paint With Model-based Deep Reinforcement Learning
  - 二次 Bézier 加粗细、透明度、颜色的神经渲染器与基于模型的 DDPG；FRIDA 报告其笔画上真机后与仿真"vastly dissimilar"
- **Neural Painters** · 2019 · 预印本 · [arXiv 1904.08410](https://arxiv.org/abs/1904.08410)
  - Neural Painters: A learned differentiable constraint for generating brushstroke paintings
  - MyPaint 动作（含起止压力）的可微替代
- **SNP** · 2020 · CVPR 2021 · [arXiv 2011.08114](https://arxiv.org/abs/2011.08114)
  - Stylized Neural Painting
  - 形状与颜色分两路渲染，含水彩墨风格；最优传输损失避免零梯度
- **Kotovenko 2021** · 2021 · CVPR 2021 · [arXiv 2103.17185](https://arxiv.org/abs/2103.17185)
  - Rethinking Style Transfer: From Pixels to Parameterized Brushstrokes
  - 显式可微渲染参数化笔画
- **Paint Transformer** · 2021 · ICCV 2021 · [arXiv 2108.03798](https://arxiv.org/abs/2108.03798)
  - Paint Transformer: Feed Forward Neural Painting with Stroke Prediction
  - 不学渲染器，用几何变换后的笔刷贴图，前馈一次预测多笔
- **Intelli-Paint** · 2021 · ECCV 2022 · [arXiv 2112.08930](https://arxiv.org/abs/2112.08930)
  - Intelli-Paint: Towards Developing More Human-Intelligible Painting Agents
  - 关注作画顺序像人，不涉及笔刷物理
- **NBE**† · 2022 · ACM TOG 2022 · [DOI](https://doi.org/10.1145/3550454.3555472)
  - Neural Brushstroke Engine: Learning a Latent Style Space of Interactive Drawing Tools
  - 用约 200 张无标注图像学多种画具的风格隐空间
- **AttentionPainter** · 2024 · IEEE TVCG 2025 · [arXiv 2410.16418](https://arxiv.org/abs/2410.16418)
  - AttentionPainter: An Efficient and Adaptive Stroke Predictor for Scene Painting
  - 单次前向预测大量笔画参数
- **MambaPainter** · 2024 · SIGGRAPH Asia 2024 Posters · [arXiv 2410.12524](https://arxiv.org/abs/2410.12524)
  - MambaPainter: Neural Stroke-Based Rendering in a Single Step
  - 选择性状态空间模型一次预测 100 多笔
- **Birth of a Painting** · 2025 · 预印本 · [arXiv 2511.13191](https://arxiv.org/abs/2511.13191)
  - Birth of a Painting: Differentiable Brushstroke Reconstruction
  - 印章式 Bézier 笔画加 StyleGAN 纹理和可微涂抹算子，不含笔刷力学
- **StrokeDiff** · 2026 · 预印本 · [arXiv 2603.01103](https://arxiv.org/abs/2603.01103)
  - Data-Efficient Brushstroke Generation with Diffusion Models for Oil Painting
  - 520 条真实油画笔画训练扩散模型，留出集 LPIPS 0.232 / FID 52；数据公开，作者称在建 1,008 条墨笔画数据集
- **DQ-Transformer** · 2026 · IEEE TVCG 2026 · [arXiv 2603.27720](https://arxiv.org/abs/2603.27720)
  - Look, Compare and Draw: Differential Query Transformer for Automatic Oil Painting
  - 2026 年仍以合成笔画为主的笔画式渲染

### 5.2 墨与书法专用的模型

- **Artist Agent** · 2012 · ICML 2012 · [arXiv 1206.4634](https://arxiv.org/abs/1206.4634)
  - Artist Agent: A Reinforcement Learning Approach to Automatic Stroke Generation in Oriental Ink Painting
  - 圆形笔印序列贴真实毛笔在不同墨量下的笔印纹理，动作含下压、上提和转笔杆，可得干墨与中空效果
- **RealBrush Ink**† · 2023 · Computer Graphics Forum 2023 · [DOI](https://doi.org/10.1111/cgf.14965) · [PDF](https://esslab.jp/publications/MadonoPG2023.pdf)
  - Data-Driven Ink Painting Brushstroke Rendering
  - 1,818 条机器人画的真实墨笔画（4 种笔、2 种纸）训练递归 CNN，墨量用累计路径长度的褪墨嵌入表示；留出集 LPIPS 0.2593 / SSIM 0.9070；输入没有压力和倾角
- **OnOff** · 2026 · ECCV 2026 · [arXiv 2608.03198](https://arxiv.org/abs/2608.03198)
  - Bridging Online and Offline Handwriting via Differentiable Physical Rendering
  - 6 参数可微笔刷，压力由速度推出，宽度 = w_base + k_spread·p；作者承认参数不是物理单位，没有湿度和三维笔刷动力学
- **TBR** · 2026 · 预印本 · [arXiv 2609.08722](https://arxiv.org/abs/2609.08722)
  - TBR: Transport-Based Rendering with Deposition Strokes for Inverse Graphics
  - 后一笔以保面积方式输运已有痕迹的可微沉积（流墨、大理石纹），不是毛笔

### 5.3 面向机器人、从真实笔画学的模型

- **CML** · 2020 · AAAI 2021 · [arXiv 2012.10043](https://arxiv.org/abs/2012.10043)
  - Content Masked Loss: Human-Like Brush Stroke Planning in a Reinforcement Learning Painting Agent
  - 把神经渲染器的笔画约束到机器人可执行；FRIDA 报告 RL 难以复现目标
- **Bidgoli 2020** · 2020 · RO-MAN 2020 · [arXiv 2007.03647](https://arxiv.org/abs/2007.03647)
  - Artistic Style in Robotic Painting; a Machine Learning Approach to Learning Brushstroke from Human Artists
  - 730 多条人类笔画配六自由度笔运动的 VAE，只生成图像，不是动作到图像的前向模型
- **FRIDA** · 2022 · ICRA 2023 · [arXiv 2210.00664](https://arxiv.org/abs/2210.00664) · [代码](https://github.com/cmubig/Frida)
  - FRIDA: A Collaborative Robot Painter with a Differentiable, Real2Sim2Real Planning Environment
  - 约 100 条真实随机笔画训练 param2stroke（下压深度 h、长度、弯曲）；作者认为笔上颜料量是最主要的未建模变量；笔垂直于画布
- **CoFRIDA** · 2024 · ICRA 2024 · [arXiv 2402.13442](https://arxiv.org/abs/2402.13442)
  - CoFRIDA: Self-Supervised Fine-Tuning for Human-Robot Co-Painting
  - 用 FRIDA 的笔画模型批量生成机器人可执行的训练对
- **Spline-FRIDA** · 2024 · IEEE RA-L 2025 · [arXiv 2412.00597](https://arxiv.org/abs/2412.00597)
  - Spline-FRIDA: Towards Diverse, Humanlike Robot Painting Styles with a Sample-Efficient, Differentiable Brush Stroke Model
  - Traj2Stroke 只有 7 个可学参数，粗细随笔高仿射变化；分布外 L1 细画笔 0.00158（CNN 0.00162），U-Net 细化能学刷毛拖曳纹理但损害泛化，最终未采用
- **IMPASTO** · 2026 · ICRA 2026 · [arXiv 2603.29315](https://arxiv.org/abs/2603.29315) · [DOI](https://doi.org/10.1109/ICRA57385.2026.11696393)
  - IMPASTO: Integrating Model-Based Planning with Learned Dynamics Models for Robotic Oil Painting Reproduction
  - 以当前画布和法向力为条件的像素动力学模型加 MPC；900 条自对弈样本时 L1 0.0285，画家单笔上加权 L1 比 FRIDA-CNN 低 19.48%；笔垂直于画布

## 6. 综述

- **Huang 2019 FITEE** · 2019 · Frontiers of Information Technology & Electronic Engineering 20(10) · [DOI](https://doi.org/10.1631/FITEE.1900195)
  - Research progress on and prospects for virtual brush modeling in digital calligraphy and painting
  - 唯一专门的虚拟毛笔综述，把模型分为经验式（接触面积）与物理式，覆盖笔–纸、纸–墨与输入设备
- **Zhang 2024 JCST** · 2023 · J. Computer Science and Technology 39(2)（2024） · [arXiv 2307.14227](https://arxiv.org/abs/2307.14227) · [DOI](https://doi.org/10.1007/s11390-024-3408-x)
  - Computational Approaches for Traditional Chinese Painting: From the "Six Principles of Painting" Perspective
  - 按"六法"整理 92 篇国画计算方法，多数不涉及毛笔物理
