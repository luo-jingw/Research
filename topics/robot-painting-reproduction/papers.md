# robot-painting-reproduction 论文目录

- 快照日期：2026-11-20
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment 字段、Crossref 记录或论文集页面确认的发表处；"预印本"表示未找到发表处。
- 标 † 的条目有未核实的元数据或内容（只读到摘要、标题不全、正文不可得、数据是否公开不明），见根目录 `issues.md` → ISSUE-008。
- 标题、年份、arXiv 编号或 DOI 经 arxiv.org、Crossref 或出版方页面核实；1990–2010 年的图形学论文多数没有 arXiv 版本，给出 DOI。
- 与 [vla-drawing-writing](../vla-drawing-writing/papers.md) 重复的论文沿用其简称（SketcherX、GeminiPainter、FRIDA、Spline-FRIDA、IMPASTO 等）。
- 分节对应 [survey.md](survey.md) 的分类；一篇论文只列在主归属的一节。

## 1. 素描：目标图到线条与明暗

### 1.1 线稿前端

- **CLD / FDoG** · 2007 · NPAR 2007 · [DOI](https://doi.org/10.1145/1274871.1274878)
  - Coherent Line Drawing
  - 沿边缘切向流做各向异性 DoG 滤波，得到连贯线稿；RoboCoDraw 用它提取轮廓
- **Photo-Sketching** · 2019 · WACV 2019 · [arXiv 1901.00542](https://arxiv.org/abs/1901.00542) · [项目](https://mtli.github.io/sketch)
  - Photo-Sketching: Inferring Contour Drawings from Images
  - 从 5,000 幅众包描摹的轮廓画学习照片到轮廓线稿；数据带笔画时间戳，许可 CC BY-NC-SA
- **APDrawingGAN** · 2019 · CVPR 2019 · [项目](https://github.com/yiranran/APDrawingGAN)
  - APDrawingGAN: Generating Artistic Portrait Drawings From Face Photos With Hierarchical GANs
  - 分面部区域的层次 GAN 生成艺术家风格肖像线稿；140 对照片与画家线稿，用距离变换损失容忍线条错位
- **QMUPD** · 2022 · IEEE TPAMI 2023 · [arXiv 2202.03678](https://arxiv.org/abs/2202.03678) · [项目](https://github.com/yiranran/QMUPD)
  - Quality Metric Guided Portrait Line Drawing Generation from Unpaired Training Data
  - 用质量指标引导、非配对数据训练的肖像线稿生成
- **Informative Drawings** · 2022 · CVPR 2022 · [arXiv 2203.12691](https://arxiv.org/abs/2203.12691)
  - Learning to Generate Line Drawings That Convey Geometry and Semantics
  - 加入深度与 CLIP 损失，让线稿表达几何与语义；用人类 2AFC 和深度、语义可恢复性评测，而不是像素匹配

### 1.2 铅笔明暗合成

- **Lu-Xu-Jia Pencil** · 2012 · NPAR 2012 · [DOI](https://doi.org/10.2312/PE/NPAR/NPAR12/065-073)
  - Combining Sketch and Tone for Pencil Drawing Production
  - 把铅笔画分成笔触结构层和色调层分别合成；只输出像素，不给工具路径
- **Im2Pencil** · 2019 · CVPR 2019 · [arXiv 1903.08682](https://arxiv.org/abs/1903.08682)
  - Im2Pencil: Controllable Pencil Illustration from Photographs
  - 轮廓与明暗两个分支分别学习、风格可控的照片转铅笔画

### 1.3 图像到矢量笔画

- **DiffDraw** · 2021 · 预印本 · [arXiv 2103.16194](https://arxiv.org/abs/2103.16194)
  - Differentiable Drawing and Sketching
  - 用距离变换的可微松弛渲染点、线、曲线，组合用 soft-OR 1 − ∏(1 − Iᵢ)
- **Virtual Sketching** · 2021 · ACM TOG 2021 · [DOI](https://doi.org/10.1145/3450626.3459833)
  - General Virtual Sketching Framework for Vector Line Art
  - 循环网络在画布上逐笔画出矢量线稿，用于线稿矢量化、照片转素描等
- **Pixelor**† · 2020 · ACM TOG 2020 · [DOI](https://doi.org/10.1145/3414685.3417840)
  - Pixelor: A Competitive Sketching AI Agent. So you think you can sketch?
  - 按可识别性学习笔画顺序，让画面尽早可辨认
- **CLIPasso** · 2022 · ACM TOG 2022 · [arXiv 2202.05822](https://arxiv.org/abs/2202.05822) · [项目](https://clipasso.github.io/clipasso)
  - CLIPasso: Semantically-Aware Object Sketching
  - 用 CLIP 损失经可微光栅器优化 Bézier 笔画，笔画数决定抽象程度
- **CLIPascene** · 2022 · ICCV 2023 · [arXiv 2211.17256](https://arxiv.org/abs/2211.17256) · [项目](https://clipascene.github.io/CLIPascene)
  - CLIPascene: Scene Sketching with Different Types and Levels of Abstraction
  - 场景素描，保真度与简洁度两个轴分开控制
- **SwiftSketch** · 2025 · SIGGRAPH 2025 · [arXiv 2502.08642](https://arxiv.org/abs/2502.08642) · [项目](https://swiftsketch.github.io)
  - SwiftSketch: A Diffusion Model for Image-to-Vector Sketch Generation
  - 在控制点上做扩散，前馈生成矢量素描，不到 1 秒
- **Sketch & Paint** · 2025 · ECCV 2024 Workshop · [arXiv 2502.20119](https://arxiv.org/abs/2502.20119)
  - Sketch & Paint: Stroke-by-Stroke Evolution of Visual Artworks
  - 按聚类排序、逐笔演化的素描与绘画生成
- **SLDgen** · 2026 · Computer Graphics Forum 2026 · [arXiv 2606.01910](https://arxiv.org/abs/2606.01910)
  - Single-Line Drawing Generation via Semantics-Driven Optimization
  - 用分数蒸馏优化一条均匀有理 B 样条，生成一笔画
- **Draw This First** · 2026 · 预印本 · [arXiv 2608.12064](https://arxiv.org/abs/2608.12064)
  - Draw This First
  - 预测一个决定笔画先后的二维顺序场，再把分割矢量化为折线并排序
- **SketchForge** · 2026 · SIGGRAPH Asia 2026 TC · [arXiv 2611.00253](https://arxiv.org/abs/2611.00253)
  - SketchForge: Training-Free Scene-to-Vector Sketching via Decoupled Structure and Texture Optimization
  - 免训练的场景转矢量素描，轮廓笔画和明暗纹理笔画分开优化

### 1.4 用点和线的密度表现明暗

- **WVS** · 2002 · NPAR 2002 · [DOI](https://doi.org/10.1145/508530.508537)
  - Weighted Voronoi Stippling
  - 加权 Voronoi 点画，点的密度表现明暗
- **TSP Art** · 2005 · Bridges 2005 · [页面](https://archive.bridgesmathart.org/2005/bridges2005-301.html)
  - TSP Art
  - 用一条 TSP 回路连接点画的点，单条连续线靠局部密度表现明暗，适合不抬笔的机器人
- **StippleDiffusion** · 2026 · 预印本 · [arXiv 2605.15816](https://arxiv.org/abs/2605.15816)
  - StippleDiffusion: Capacity-Constrained Stippling using Controlled Diffusion
  - 以图像为容量约束的扩散点画采样器

## 2. 机器人素描与线描临摹

- **Calinon Portrait** · 2005 · Humanoids 2005 · [DOI](https://doi.org/10.1109/ichr.2005.1573562)
  - A Humanoid Robot Drawing Human Portraits
  - 人形机器人画人像
- **Lu-Lam-Yam Hatching** · 2009 · IEEE/ASME AIM 2009 · [DOI](https://doi.org/10.1109/aim.2009.5229949)
  - Preliminary Study on Vision-based Pen-and-Ink Drawing by a Robotic Manipulator
  - 带视觉闭环的排线临摹：用随目标亮度变化的核模糊当前画面，与目标比较后在差异最大处排线，并有停止准则
- **Paul**† · 2013 · Computers & Graphics 2013
  - Portrait Drawing by Paul the Robot
  - 肖像素描机器人，靠视觉反馈逐步加线条和排线
- **Ergodic Rendering** · 2016 · WAFR 2016 · [arXiv 1709.02758](https://arxiv.org/abs/1709.02758)
  - Autonomous Visual Rendering using Physical Motion
  - 用遍历控制让停留时间正比于暗度来复现图像，自带定量的遍历度量
- **SSK** · 2018 · ICRA 2018
  - Artistic Pen Drawing on an Arbitrary Surface using an Impedance-controlled Robot
  - 阻抗控制机器人在任意曲面上作钢笔画，提出用笔压数据决定笔高与线宽
- **O'Dowd Pencil** · 2019 · EVA London 2019
  - A Robot That Draws and Shades with Tactile Force Feedback Sensed Through a Pencil
  - 通过铅笔感知触觉力反馈、可画明暗的机器人
- **Lau IBVS** · 2019 · Knowledge Engineering Review 2019 · [DOI](https://doi.org/10.1017/s0269888919000146)
  - A Sketch Drawing Humanoid Robot Using Image-Based Visual Servoing
  - 基于图像视觉伺服的人形素描机器人
- **Line-Art Replication** · 2019 · WACV 2020 · [arXiv 1910.07860](https://arxiv.org/abs/1910.07860)
  - Can I Teach a Robot to Replicate a Line Art
  - 学习把线稿转成机器人可执行的笔画；指出基于规则的矢量化在复杂线稿上失败
- **AiSketcher** · 2020 · IROS 2020 · [arXiv 2005.05526](https://arxiv.org/abs/2005.05526)
  - Making Robots Draw A Vivid Portrait In Two Minutes
  - 照片到风格化线稿，骨架化后用 BFS 追踪成折线，3 自由度机械臂约 2 分钟画完；自述细节受机械臂限制而丢失
- **Chitrakar** · 2020 · 预印本 · [arXiv 2011.10781](https://arxiv.org/abs/2011.10781)
  - Chitrakar: Robotic System for Drawing Jordan Curve of Facial Portrait
  - 把人像转成一条 Jordan 曲线由机器人画出
- **RoboCoDraw** · 2019 · AAAI 2020 · [arXiv 1912.05099](https://arxiv.org/abs/1912.05099)
  - RoboCoDraw: Robotic Avatar Drawing with GAN-based Style Transfer and Time-efficient Path Optimization
  - GAN 风格迁移 + FDoG 轮廓 + GTSP 路径优化；路径比贪心好 17.34%，实画 43.2 秒
- **Embodied DIO** · 2022 · NeurIPS 2021 Workshop · [arXiv 2201.08142](https://arxiv.org/abs/2201.08142)
  - Physically Embodied Deep Image Optimisation
  - 把深度图像优化的笔画导出为 G-code 由绘图机执行
- **Adamik GA Pencil** · 2022 · Robotics and Autonomous Systems 2022
  - Fast Robotic Pencil Drawing Based on Image Evolution by Means of Genetic Algorithm
  - 用遗传算法演化线段图像，快速铅笔素描
- **drozBot** · 2022 · IEEE RA-L 2022
  - drozBot: Using Ergodic Control to Draw Portraits
  - 用遍历控制画人像，以覆盖密度表现明暗
- **SBR Planning** · 2022 · IROS 2023 · [arXiv 2210.07590](https://arxiv.org/abs/2210.07590)
  - Stroke-based Rendering and Planning for Robotic Performance of Artistic Drawing
  - 按全景分割和深度排序笔画，让形状尽早出现；k-means 调色板，机器人上 4 支彩笔，实物颜色与调色板不一致
- **Nasrat 80 s** · 2023 · Sensors 2023 · [DOI](https://doi.org/10.3390/s23125589)
  - Artistic Robotic Arm: Drawing Portraits on Physical Canvas under 80 Seconds
  - 80 秒内在实物画布上画人像；用笔高调线宽约 0.1–2.25 mm
- **TSP-Bot** · 2022 · Ubiquitous Robots 2024 · [arXiv 2210.07592](https://arxiv.org/abs/2210.07592)
  - TSP-Bot: Robotic TSP Pen Art using High-DoF Manipulators
  - 高自由度机械臂画 TSP 连续线艺术，路径平滑成曲率有界的 Bézier 样条
- **SketcherX** · 2024 · 预印本 · [arXiv 2409.15292](https://arxiv.org/abs/2409.15292)
  - SketcherX: AI-Driven Interactive Robotic drawing with Diffusion model and Vectorization Techniques
  - 扩散模型 + 矢量化的交互式机器人肖像素描（另见 vla-drawing-writing）
- **Piktor-o-bot**† · 2024 · IMEKO 2024 / Measurement: Sensors 2025
  - Programming and Control Challenges of the Portrait Drawing Piktor-o-bot
  - 铅笔压力映射灰度：2–16 N 只能稳定画出约 4 级灰，铅笔硬度、倾角和削尖都有影响
- **Berio ΣΛ** · 2025 · RO-MAN 2025 · [arXiv 2507.03166](https://arxiv.org/abs/2507.03166)
  - Image-driven Robot Drawing with Rapid Lognormal Movements
  - 用快速对数正态运动模型生成图像驱动的机器人笔画，竖直轴控制笔刷宽度
- **GeminiPainter** · 2026 · 预印本 · [arXiv 2608.00829](https://arxiv.org/abs/2608.00829)
  - GeminiPainter's sequence-formed pipeline comprised of perception, cognition, planning, and action stages
  - 感知、认知、规划、执行四阶段的 VLM 机器人绘画流水线（另见 vla-drawing-writing）

## 3. 油画：目标图到笔画

### 3.1 经典笔画渲染（SBR）

- **Paint by Numbers** · 1990 · SIGGRAPH 1990 · [DOI](https://doi.org/10.1145/97879.97902)
  - Paint by Numbers: Abstract Image Representations
  - 把图像表示为颜色、形状、大小、方向可控的有序笔画集合
- **Litwinowicz97** · 1997 · SIGGRAPH 1997 · [DOI](https://doi.org/10.1145/258734.258893)
  - Processing Images and Video for an Impressionist Effect
  - 网格播种短笔画，方向沿图像梯度、遇边缘截断，颜色取笔画中心的源图颜色并加扰动
- **Hertzmann98** · 1998 · SIGGRAPH 1998 · [DOI](https://doi.org/10.1145/280814.280951)
  - Painterly Rendering with Curved Brush Strokes of Multiple Sizes
  - 按笔刷半径从大到小分层，每层只在与模糊参考误差超过阈值处起笔；单色曲线笔画，颜色取参考图

### 3.2 神经网络与优化画家

- **Learning to Paint** · 2019 · ICCV 2019 · [arXiv 1903.04411](https://arxiv.org/abs/1903.04411)
  - Learning to Paint With Model-based Deep Reinforcement Learning
  - 13 维笔画（二次 Bézier、两端粗细与透明度、RGB）+ 神经渲染器 + 基于模型的 DDPG；后续工作的通用基线
- **SNP** · 2020 · CVPR 2021 · [arXiv 2011.08114](https://arxiv.org/abs/2011.08114) · [项目](https://jiupinjia.github.io/neuralpainter)
  - Stylized Neural Painting
  - 经双通路神经渲染器对笔画参数做梯度搜索；油画笔画可有头尾两种颜色，分块渐进细化
- **Param. Brushstrokes** · 2021 · CVPR 2021 · [arXiv 2103.17185](https://arxiv.org/abs/2103.17185)
  - Rethinking Style Transfer: From Pixels to Parameterized Brushstrokes
  - 在笔画参数空间做风格迁移，数千笔联合优化；神经渲染器显存太大，改用显式可微渲染器
- **Paint Transformer** · 2021 · ICCV 2021 · [arXiv 2108.03798](https://arxiv.org/abs/2108.03798)
  - Paint Transformer: Feed Forward Neural Painting with Stroke Prediction
  - 前馈集合预测，每个 32×32 块 8 笔、4 级由粗到细，512 像素推理 0.3 秒
- **Intelli-Paint** · 2021 · ECCV 2022 · [arXiv 2112.08930](https://arxiv.org/abs/2112.08930)
  - Intelli-Paint: Towards Developing Human-like Painting Agents (ECCV title: "…More Human-Intelligible Painting Agents")
  - 先背景后前景、逐区域作画，去掉 60–80% 的笔画；对相邻笔画的颜色变化加惩罚
- **Im2Oil** · 2022 · ACM MM 2022 · [arXiv 2209.13219](https://arxiv.org/abs/2209.13219) · [项目](https://github.com/TZYSJTU/Im2Oil)
  - Im2Oil: Stroke-Based Oil Painting Rendering with Linearly Controllable Fineness Via Adaptive Sampling
  - 非神经的油画 SBR：按梯度密度采样锚点，颜色取锚点像素，从大到小画，一个参数控制精细度
- **Compositional Neural Painter** · 2023 · ACM MM 2023 · [arXiv 2309.03504](https://arxiv.org/abs/2309.03504)
  - Stroke-based Neural Painting and Stylization with Dynamically Predicted Painting Region
  - RL 组合器预测下一个作画区域，避免均匀网格的块边界问题
- **SBP** · 2023 · ICMEW 2024 · [arXiv 2311.14271](https://arxiv.org/abs/2311.14271)
  - Segmentation-Based Parametric Painting
  - 按全景分割分语义层、多遍由粗到细的批量梯度优化，适合大画布
- **AttentionPainter** · 2024 · IEEE TVCG 2025 · [arXiv 2410.16418](https://arxiv.org/abs/2410.16418)
  - AttentionPainter: An Efficient and Adaptive Stroke Predictor for Scene Painting
  - 一次前向预测整幅画数千笔，每张 0.08 秒
- **Birth of a Painting** · 2025 · 预印本 · [arXiv 2511.13191](https://arxiv.org/abs/2511.13191)
  - Birth of a Painting: Differentiable Brushstroke Reconstruction
  - 可微的作画—揉擦循环：Bézier 笔画、笔画纹理风格化和可微揉擦算子；按油画、水彩、水墨、数字分别评测
- **DQ-Transformer** · 2026 · 预印本 · [arXiv 2603.27720](https://arxiv.org/abs/2603.27720)
  - Look, Compare and Draw: Differential Query Transformer for Automatic Oil Painting
  - 以目标与当前画布的差异作查询的 Transformer 油画生成
- **Dual-Param SBR** · 2026 · 预印本 · [arXiv 2604.02752](https://arxiv.org/abs/2604.02752)
  - Differentiable Stroke Planning with Dual Parameterization for Efficient and High-Fidelity Painting Creation
  - 折线与 Bézier 控制点双重表示，搜索与梯度结合跳出局部最优
- **QBS** · 2026 · 预印本 · [arXiv 2611.10713](https://arxiv.org/abs/2611.10713)
  - Quadratic Bezier Splatting with Structural Initialization for Efficient Painting Rendering
  - 二次 Bézier splatting 解析渲染 + 多尺度初始化 + 逐笔审查

## 4. 机器人油画与彩绘系统

- **e-David 2013** · 2013 · Computers & Graphics 2013 · [DOI](https://doi.org/10.1016/j.cag.2013.01.005)
  - Image stylization with a painting machine using semantic hints
  - 仿真候选笔画、挑误差下降最大的约 300 笔执行、拍照、再循环；实验只用灰度墨，每幅 3–4 万笔、10–15 小时
- **e-David 2015**† · 2015 · Computer Graphics Forum 2015 · [DOI](https://doi.org/10.1111/cgf.12562)
  - Hardware-Based Non-Photorealistic Rendering Using a Painting Robot
  - 用固定丙烯颜料库复现颜色：近透明笔画罩染，或不透明笔画抖动排列
- **e-David 2022** · 2022 · Arts 2022 · [DOI](https://doi.org/10.3390/arts11040077)
  - Region-Based Approaches in Robotic Painting
  - 以区域而非笔画为规划单元，预混丙烯自动取色，反馈图像做畸变、光照和颜色校正
- **Karimov 2019**† · 2019 · Robotics and Autonomous Systems 2019 · [DOI](https://doi.org/10.1016/j.robot.2019.02.009)
  - Advanced tone rendition technique for a painting robot
  - 注射泵自动调配黑白丙烯的色调再现
- **Karimov 2021** · 2021 · Inventions 2021 · [DOI](https://doi.org/10.3390/inventions6010019)
  - Image Preprocessing for Artistic Robotic Painting
  - 自动调色机器人每调一种色就画完该色所有笔画再清洗；一幅人像约 3.3 万笔
- **Karimov 2023**† · 2023 · J. Intell. Robot. Syst. 2023 · [DOI](https://doi.org/10.1007/s10846-023-01831-4)
  - A Robot for Artistic Painting in Authentic Colors
  - 把自动调色机器人扩展到彩色
- **Busker Watercolour**† · 2018 · J. Intell. Robot. Syst. 2019 · [DOI](https://doi.org/10.1007/s10846-018-0937-y)
  - Watercolour Robotic Painting: a Novel Automatic System for Artistic Rendering
  - 水彩排线机器人，视觉测量笔画上颜料的消耗
- **CML** · 2020 · AAAI 2021 · [arXiv 2012.10043](https://arxiv.org/abs/2012.10043)
  - Content Masked Loss: Human-Like Brush Stroke Planning in a Reinforcement Learning Painting Agent
  - 把 Learning to Paint 的笔画约束到机器人可执行（固定宽度、不透明、限长）；k-means 选 10 色由人调配，开环
- **Bidgoli 2020** · 2020 · RO-MAN 2020 · [arXiv 2007.03647](https://arxiv.org/abs/2007.03647)
  - Artistic Style in Robotic Painting; a Machine Learning Approach to Learning Brushstroke from Human Artists
  - 动作捕捉艺术家笔触训练 VAE，再由机械臂执行；5 级灰，开环
- **FRIDA** · 2022 · ICRA 2023 · [arXiv 2210.00664](https://arxiv.org/abs/2210.00664) · [DOI](https://doi.org/10.1109/ICRA48891.2023.10160702)
  - FRIDA: A Collaborative Robot Painter with a Differentiable, Real2Sim2Real Planning Environment
  - 从真机笔画学习 param2stroke，经可微仿真优化计划、分批执行后拍照重规划；最多 12 种预混丙烯，优化中反复 k-means 离散颜色，由浅到深作画
- **CoFRIDA** · 2024 · ICRA 2024 · [arXiv 2402.13442](https://arxiv.org/abs/2402.13442) · [DOI](https://doi.org/10.1109/ICRA57147.2024.10610618)
  - CoFRIDA: Self-Supervised Fine-Tuning for Human-Robot Co-Painting
  - 微调图像编辑模型，让人机共画的目标图符合机器人能力和已有笔画
- **Spline-FRIDA** · 2024 · IEEE RA-L 2025 · [arXiv 2412.00597](https://arxiv.org/abs/2412.00597) · [DOI](https://doi.org/10.1109/LRA.2025.3563131)
  - Spline-FRIDA: Towards Diverse, Humanlike Robot Painting Styles with a Sample-Efficient, Differentiable Brush Stroke Model
  - 动作捕捉的人类笔迹训练轨迹 VAE；Traj2Stroke 让粗细随笔高线性变化，每种画具约 1 小时采数据、20 分钟训练
- **IMPASTO** · 2026 · 预印本 · [arXiv 2603.29315](https://arxiv.org/abs/2603.29315) · [项目](https://impasto-robopainting.github.io)
  - IMPASTO: Integrating Model-Based Planning with Learned Dynamics Models for Robotic Oil Painting Reproduction
  - 机器人自对弈学习像素动力学模型 + 滚动时域 MPC 规划轨迹和力；调色盘 24 格预混油彩、按目标画取子集，模型内颜色按灰度处理
- **Cable Mural Robot** · 2024 · 预印本 · [arXiv 2403.12214](https://arxiv.org/abs/2403.12214)
  - Architectural-Scale Artistic Brush Painting with a Hybrid Cable Robot
  - 27 m 壁画的绳索 + 机械臂绘画；每色一个轨迹文件和一支笔，换色人工完成

## 5. 介质仿真与渲染

### 5.1 铅笔、炭笔与其他干性介质

- **Sousa-Buchanan GI** · 1999 · Graphics Interface 1999 · [PDF](https://graphicsinterface.org/wp-content/uploads/gi1999-21.pdf)
  - Observational Model of Blenders and Erasers in Computer-Generated Pencil Rendering
  - 铅笔观测模型：纸面高度场 + 逐位置的石墨、黏土、蜡累积量，沉积取决于笔尖形状、压力和硬度；含擦笔与橡皮
- **Sousa-Buchanan CGF** · 2000 · Computer Graphics Forum 2000 · [DOI](https://doi.org/10.1111/1467-8659.00386)
  - Observational Models of Graphite Pencil Materials
  - 完整的铅笔、纸、擦笔、橡皮材料模型，与数字化的真实铅笔画对比
- **Sousa-Buchanan 3D** · 1999 · Computer Graphics Forum 1999 · [DOI](https://doi.org/10.1111/1467-8659.00340)
  - Computer-Generated Graphite Pencil Rendering of 3D Polygonal Models
  - 在上述材料模型上从三维模型生成轮廓和明暗笔画
- **Takagi Colored Pencil** · 1999 · Pacific Graphics 1999 · [DOI](https://doi.org/10.1109/PCCGA.1999.803369)
  - Volumetric modeling of colored pencil drawing
  - 彩色铅笔颜料在纸中的体积分布模型
- **Durand Thresholding** · 2001 · Rendering Techniques 2001 · [DOI](https://doi.org/10.1007/978-3-7091-6242-2_7)
  - Decoupling Strokes and High-Level Attributes for Interactive Traditional Drawing
  - 用笔画阈值纹理对目标色调做阈值，实时生成铅笔、炭笔色调；不保存沉积状态
- **Majumder-Gopi Charcoal** · 2002 · NPAR 2002 · [DOI](https://doi.org/10.1145/508530.508541)
  - Hardware Accelerated Real Time Charcoal Rendering
  - 噪声纹理上的对比度增强 + 模糊，实时炭笔效果，无沉积状态
- **Rudolf Crayon** · 2005 · Computer Graphics Forum 2005 · [DOI](https://doi.org/10.1111/j.1467-8659.2005.00826.x)
  - A Bidirectional Deposition Model of Wax Crayons
  - 蜡笔双向沉积：每个纸格保存一列蜡层，由接触轮廓、力和摩擦计算沉积，可涂抹；每笔 0.1–4 秒
- **Van Haevre Pastel**† · 2007 · The Visual Computer 2007 · [DOI](https://doi.org/10.1007/s00371-007-0144-5)
  - From dust till drawn
  - 粉彩双向转移，纸面受压凹陷，工具磨损

### 5.2 油画颜料与笔刷

- **Strassmann** · 1986 · SIGGRAPH 1986 · [DOI](https://doi.org/10.1145/15886.15911)
  - Hairy brushes
  - 笔刷由一组随笔画演化的刷毛构成，笔画是位置加压力的轨迹
- **Cockshott Wet&Sticky** · 1992 · Computer Graphics Forum 1992 · [DOI](https://doi.org/10.1111/1467-8659.1130217)
  - Modelling the Texture of Paint
  - 元胞自动机颜料模型的纹理与光泽扩展，最早的颜料高度模型之一
- **dAb** · 2001 · SIGGRAPH 2001 · [DOI](https://doi.org/10.1145/383259.383313)
  - DAB: interactive haptic painting with 3D virtual brushes
  - 可形变三维虚拟笔刷 + 笔刷与画布双向颜料转移 + 力反馈
- **Fast Paint Texture** · 2002 · NPAR 2002 · [DOI](https://doi.org/10.1145/508530.508546)
  - Fast paint texture
  - 每笔一张高度图合成高度场再做凹凸光照，给笔画加厚涂质感
- **IMPaSTo** · 2004 · NPAR 2004 · [DOI](https://doi.org/10.1145/987657.987665)
  - IMPaSTo: A Realistic, Interactive Model for Paint
  - 二维网格，每格最多 8 种颜料浓度和颜料体积，一层湿层加若干干层，8 波长 Kubelka–Munk 渲染；26×26 笔印每秒 116 次
- **Baxter Viscous** · 2004 · Computer Animation and Virtual Worlds 2004 · [DOI](https://doi.org/10.1002/cav.47)
  - A viscous paint model for interactive applications
  - 三维 Stokes 黏性流颜料，只能在 32×32×16 的粗网格上达到 20 fps
- **Baxter-Lin Brush** · 2004 · Pacific Graphics 2004 · [DOI](https://doi.org/10.1109/PCCGA.2004.1348363)
  - A Versatile Interactive 3D Brush Model
  - 少量模拟主干插值出数百条刷毛，含各向异性摩擦、塑性和笔尖散开
- **Okaichi Knife** · 2008 · The Visual Computer 2008 · [DOI](https://doi.org/10.1007/s00371-008-0257-5)
  - A virtual painting knife
  - 三维画刀推动厚油彩
- **Chu Detail-Preserving** · 2010 · NPAR 2010 · [DOI](https://doi.org/10.1145/1809939.1809943)
  - Detail-preserving paint modeling for 3D brushes
  - 从笔画开始前的画布快照拾取颜料、拾取图与画布同分辨率，消除涂抹时的细节模糊；60×60 笔印 145 fps
- **RealBrush** · 2013 · ACM TOG 2013 · [DOI](https://doi.org/10.1145/2461912.2461998)
  - RealBrush: Painting with Examples of Physical Media
  - 用拍摄的真实笔画样例合成油画、粉彩、炭笔等笔画与涂抹；2AFC 显示单笔与真实难以区分，涂抹可以区分
- **WetBrush** · 2015 · ACM TOG 2015 · [DOI](https://doi.org/10.1145/2816795.2818066)
  - Wetbrush: GPU-based 3D Painting Simulation at the Bristle Level
  - 刷毛级三维油画模拟：40–600 根刷毛，近处颜料用粒子、远处用密度网格，GTX TITAN X 上 30–110 fps

### 5.3 颜色合成

- **Haase-Meyer** · 1992 · ACM TOG 1992 · [DOI](https://doi.org/10.1145/146443.146452)
  - Modeling pigmented materials for realistic image synthesis
  - 把 Kubelka–Munk 颜料混合引入图形学
- **Curtis Watercolour** · 1997 · SIGGRAPH 1997 · [DOI](https://doi.org/10.1145/258734.258896)
  - Computer-generated watercolor
  - 水彩流动模拟；NPR 中 Kubelka–Munk 分层合成的来源
- **RealPigment** · 2014 · NPAR 2014 · [DOI](https://doi.org/10.1145/2630397.2630401)
  - RealPigment: Paint Compositing by Example
  - 从一张拍摄的色卡拟合颜料叠加的颜色，用 CIELAB 留一误差评测
- **Mixbox** · 2021 · ACM TOG 2021 · [DOI](https://doi.org/10.1145/3478513.3480549) · [项目](https://github.com/scrtwpns/pigment-mixing)
  - Practical pigment mixing for digital painting
  - RGB 进出的 Kubelka–Munk 式颜料混合：4 种颜料浓度 + RGB 残差的 7 维隐空间，中位开销是 RGB 混合的 2.3 倍

### 5.4 学习的与可微的笔画渲染器

- **SPIRAL** · 2018 · ICML 2018 · [arXiv 1804.01118](https://arxiv.org/abs/1804.01118)
  - Synthesizing Programs for Images using Reinforced Adversarial Learning
  - 智能体驱动 libmypaint 作画，用判别器奖励训练；确立 MyPaint 作为 RL 绘画环境
- **Wu Oil-GAN** · 2018 · Expressive 2018 · [DOI](https://doi.org/10.1145/3229147.3229150)
  - Brush stroke synthesis with a generative adversarial network driven by physically based simulation
  - 用离线物理模拟器数据训练 GAN，从已有画布和新轨迹预测油画笔画的高度与颜色
- **Neural Painters** · 2019 · 预印本 · [arXiv 1904.08410](https://arxiv.org/abs/1904.08410)
  - Neural Painters: A learned differentiable constraint for generating brushstroke paintings
  - 学习 MyPaint 笔画的可微替代模型
- **SPIRAL++** · 2019 · 预印本 · [arXiv 1910.01007](https://arxiv.org/abs/1910.01007)
  - Unsupervised Doodling and Painting with Improved SPIRAL
  - 在 libmypaint 和 Fluid Paint 上作画；指出流体颜料有隐藏速度场，画布图像不是完整状态
- **DiffVG** · 2020 · ACM TOG 2020 · [DOI](https://doi.org/10.1145/3414685.3417871)
  - Differentiable vector graphics rasterization for editing and learning
  - 可微矢量图光栅化，对位置、颜色、线宽求梯度；FRIDA 测得它与真实机器人笔画的 L1 误差明显更大
- **NBE** · 2022 · ACM TOG 2022 · [DOI](https://doi.org/10.1145/3550454.3555472)
  - Neural Brushstroke Engine: Learning a Latent Style Space of Interactive Drawing Tools
  - 用约 200 张无标注图像学习多种画具的笔画风格隐空间

### 5.5 相邻：水墨

- **MoXi** · 2005 · ACM TOG 2005 · [DOI](https://doi.org/10.1145/1073204.1073221)
  - MoXi: Real-Time Ink Dispersion in Absorbent Paper
  - 格子 Boltzmann 模拟墨在吸水纸中的渗化，实时

## 6. 评测指标

- **Rough Sketch Bench** · 2020 · ACM TOG 2020 · [项目](https://cragl.cs.gmu.edu/sketchbench)
  - A Benchmark for Rough Sketch Cleanup
  - 在受控错位上比较 IoU、Hausdorff、F-score 和 Chamfer，选定 Chamfer 作线稿相似度
- **LPIPS** · 2018 · CVPR 2018 · [arXiv 1801.03924](https://arxiv.org/abs/1801.03924)
  - The Unreasonable Effectiveness of Deep Features as a Perceptual Metric
  - 深度特征距离，与人类感知相似度判断的一致性高于 PSNR 和 SSIM
- **DreamSim** · 2023 · NeurIPS 2023 · [arXiv 2306.09344](https://arxiv.org/abs/2306.09344)
  - DreamSim: Learning New Dimensions of Human Visual Similarity using Synthetic Data
  - 用合成三元组上的人类 2AFC 判断调出的中层视觉相似度
- **ArtFID** · 2022 · GCPR 2022 · [arXiv 2207.12280](https://arxiv.org/abs/2207.12280)
  - ArtFID: Quantitative Evaluation of Neural Style Transfer
  - 风格迁移的分布级指标，结合内容 LPIPS 和用艺术品训练的 FID
- **SketchRef** · 2024 · 预印本 · [arXiv 2408.08623](https://arxiv.org/abs/2408.08623)
  - SketchRef: a Multi-Task Evaluation Benchmark for Sketch Synthesis
  - 素描合成评测；SSIM、MS-SSIM、LPIPS 与人类结构判断相关性弱，提出基于关键点的评分
- **Scoot** · 2019 · ICCV 2019 · [arXiv 1908.08433](https://arxiv.org/abs/1908.08433) · [项目](https://mmcheng.net/scoot)
  - Scoot: A Perceptual Metric for Facial Sketches
  - 人脸素描的结构共现纹理指标，基于 15.2 万条人类判断；SSIM 和 FSIM 在此任务上失效
- **NPRportrait** · 2020 · 预印本 · [arXiv 2009.00633](https://arxiv.org/abs/2009.00633)
  - NPRportrait 1.0: A Three-Level Benchmark for Non-Photorealistic Rendering of Portraits
  - 三级人像非真实感渲染基准，用用户研究比较方法

## 7. 数据

### 7.1 作画过程

- **Timecraft** · 2020 · CVPR 2020 · [arXiv 2001.01026](https://arxiv.org/abs/2001.01026) · [项目](https://xamyzhao.github.io/timecraft)
  - Painting Many Pasts: Synthesizing Time Lapse Videos of Paintings
  - 从成画采样合理的作画延时视频；117 段数字和 116 段水彩延时视频
- **Inverse Painting** · 2024 · SIGGRAPH Asia 2024 · [arXiv 2409.20556](https://arxiv.org/abs/2409.20556) · [项目](https://inversepainting.github.io)
  - Inverse Painting: Reconstructing The Painting Process
  - 自回归扩散逐步预测文字指令、区域掩码和画布更新，重建作画过程；294 段丙烯风景视频，提出过程距离曲线 DDC
- **ProcessPainter** · 2024 · 预印本 · [arXiv 2406.06062](https://arxiv.org/abs/2406.06062)
  - ProcessPainter: Learn Painting Process from Sequence Data
  - 用笔画渲染器生成的合成过程序列预训练文生视频模型，再用少量画家过程微调
- **Loomis Painter** · 2025 · 预印本 · [arXiv 2511.17344](https://arxiv.org/abs/2511.17344)
  - Loomis Painter: Reconstructing the Painting Process
  - 多介质作画过程重建，737 段视频含油画 151、铅笔 298；数据因许可不公开，提出逐帧到终画的距离曲线 PDP
- **Painting Change Map** · 2026 · 预印本 · [arXiv 2610.25369](https://arxiv.org/abs/2610.25369)
  - Painting Change Map as guidance for generating painting processes
  - 用时空变化图控制正向作画和反向擦除的视频生成
- **PPJudge** · 2025 · ACM MM 2025 · [arXiv 2507.09242](https://arxiv.org/abs/2507.09242)
  - PPJudge: Towards Human-Aligned Assessment of Artistic Painting Process
  - 约 1.5 万段美术专业学生的真实作画过程（部分临摹参考画），8 项专家评分，训练过程质量评判模型
- **Paints-Undo**† · 2024 · GitHub 项目，无论文 · [项目](https://github.com/lllyasviel/Paints-UNDO)
  - Paints-Undo
  - 把成品数字插画反推成类似撤销记录的作画序列
- **Collaborative Neural Painting** · 2023 · 预印本 · [arXiv 2312.01800](https://arxiv.org/abs/2312.01800) · [项目](https://fodark.github.io/collaborative-neural-painting)
  - Collaborative Neural Painting
  - 用 SNP 分解生成 10 万条合成笔画序列，定义笔画序列补全任务与基准

### 7.2 真实笔画数据

- **RealBrush Ink**† · 2023 · Computer Graphics Forum 2023 · [DOI](https://doi.org/10.1111/cgf.14965)
  - Data-Driven Ink Painting Brushstroke Rendering
  - 1,818 条机器人画的墨笔画，带人工标注路径及其与参考矢量的对应；论文称计划公开

### 7.3 素描与线稿数据集

- **QuickDraw** · 2017 · 预印本 · [arXiv 1704.03477](https://arxiv.org/abs/1704.03477) · [数据](https://github.com/googlecreativelab/quickdraw-dataset)
  - A Neural Representation of Sketch Drawings (Quick, Draw! dataset)
  - 345 类、5,000 万幅带笔画时间的涂鸦，无目标图像；CC BY 4.0
- **Sketchy**† · 2016 · SIGGRAPH 2016
  - The Sketchy Database: Learning to Retrieve Badly Drawn Bunnies
  - 照片与素描配对的大规模检索数据库
- **SketchyScene** · 2018 · ECCV 2018 · [arXiv 1808.02473](https://arxiv.org/abs/1808.02473)
  - SketchyScene: Richly-Annotated Scene Sketches
  - 2.9 万多幅场景素描，带语义与实例掩码
- **FS-COCO** · 2022 · ECCV 2022 · [arXiv 2203.02113](https://arxiv.org/abs/2203.02113) · [项目](https://fscoco.github.io)
  - FS-COCO: Towards Understanding of Freehand Sketches of Common Objects in Context
  - 1 万幅凭记忆画的 MS-COCO 场景素描，带时空数据和描述；CC BY-NC 4.0
- **OpenSketch** · 2019 · ACM TOG 2019 · [项目](https://repo-sam.inria.fr/d3/OpenSketch)
  - OpenSketch: A Richly-Annotated Dataset of Product Design Sketches
  - 400 多幅产品设计素描，数位板记录笔迹、压力和时间，每幅 200–400 笔
- **SEVA** · 2023 · NeurIPS 2023 D&B · [arXiv 2312.03035](https://arxiv.org/abs/2312.03035)
  - SEVA: Leveraging sketches to evaluate alignment between human and machine visual abstraction
  - 限时（4–32 秒）素描 8.98 万幅，测量模型与人类在素描识别上的一致性
- **Cole 2008** · 2008 · ACM TOG 2008 · [项目](https://gfx.cs.princeton.edu/proj/ld3d)
  - Where Do People Draw Lines?
  - 29 位画家对三维模型的 208 幅铅笔线稿；约 75% 的线条像素落在其他画家线条 1 mm 内

## 8. 现有综述

- **Hertzmann SBR Survey** · 2003 · IEEE CG&A 2003 · [DOI](https://doi.org/10.1109/MCG.2003.1210867)
  - A Survey of Stroke-Based Rendering
  - 笔画渲染算法综述：贪心放置与优化放置
- **SBR Survey 2022** · 2022 · 预印本 · [arXiv 2302.00595](https://arxiv.org/abs/2302.00595)
  - Stroke-based Rendering: From Heuristics to Deep Learning
  - 从启发式到深度学习的笔画渲染综述（只核实了元数据）
- **Gülzow 2020** · 2020 · Applied Sciences 2020 · [DOI](https://doi.org/10.3390/app10103396)
  - Recent Developments Regarding Painting Robots for Research in Automatic Painting, Artificial Creativity, and Machine Learning
  - e-David 团队对绘画机器人研究的回顾（只读到摘要）
