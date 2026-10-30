# PROJECT.md

Project-specific context that supplements `AGENTS.md`.

`AGENTS.md` is fixed across projects.
`PROJECT.md` accumulates what is specific to this one.

Update this file when a new project-specific constraint, environment
detail, or convention is discovered during work.

Do not duplicate:
- verified architecture → `docs/`;
- current work → `plan.md`;
- unresolved problems → `issues.md`.

## Template

- Initialized from (source, version, or commit): explicit-agent 0.1.0 (964b9d9c376f)
- Last synced to (source, version, or commit): explicit-agent 0.1.0 (964b9d9c376f)
- Last applied migration id (see the template's `migrations.json`): 0

## Purpose

多方向的科研调研工作区。每个研究方向（topic）独立成目录，沉淀文献调研、论文目录、精读笔记和对外汇报材料；方向之间共享同一套状态文件和写作约定。

## Environment

- Platform / hardware: Linux 工作站
- Shared with (other users or projects on the same account or machine):
- Constraints imposed by the environment: 工作区是 git 仓库（2026-10-30 初始化，分支 `main`，远程 `origin` = https://github.com/luo-jingw/Research.git，公开仓库）。提交身份只配置在仓库级，全局未配置。

## Credentials

Services that require a scoped identity in this project (git remotes,
package registries, model hubs, cloud APIs).

| Service | Scope | Source | Notes |
|---|---|---|---|
| git 提交身份 | 仅本仓库（`.git/config`） | 仓库所有者指定：Jingwu Luo / 学校邮箱 | 全局未配置；仓库公开，邮箱出现在公开提交记录中 |
| GitHub 远程 `luo-jingw/Research` | 仅本仓库的 `origin` | 文件 `/home/jingwu/workspace/github_token`（仓库外） | 每次 push 通过一次性 `-c credential.helper` 读取，不写入 `.git/config` 或远程 URL |

Do not assume a global or default identity applies.
See `AGENTS.md` → Credentials and Environment Isolation.

Do not record token values or other secrets here.

## Project-Specific Constraints

### 目录结构

```
Research/
├── AGENTS.md / PROJECT.md / plan.md / issues.md / opportunities.md
├── docs/                    跨 topic 的已验证内容（术语表、方法论等）
├── templates/               模板自带文件
└── topics/
    ├── README.md            全部研究方向的索引
    └── <topic-slug>/        一个研究方向一个目录
        ├── README.md        范围（含 / 不含）、关键词、状态、文件索引
        ├── survey.md        综述：分类法、各分支脉络、趋势、文献陈述的开放问题
        ├── papers.md        论文目录：一篇一行，元数据经检索核实
        ├── notes/           精读笔记，一篇一个文件（按需创建）
        └── reports/         对外产出：汇报 deck、结构图（按需创建）
```

### 命名

- `<topic-slug>`：小写、短横线分隔，例如 `real2sim`、`world-models`。
- 精读笔记：`notes/<year>-<short-name>.md`，例如 `notes/2024-rialto.md`。
- 汇报材料：`reports/<YYYY-MM-DD>-<subject>.html`。

### 状态归属

- `topics/README.md` 拥有 topic 列表；新建 topic 目录时同步加一行。
- `topics/<slug>/papers.md` 拥有该方向的论文元数据（标题、年份、会议、链接）。一篇论文属于多个方向时，各方向的 `papers.md` 各列一行，精读笔记只存一份，放在主归属方向的 `notes/`，其他方向用相对路径链接。
- `survey.md` 只写可溯源到文献的内容，每个论断引用 `papers.md` 中的简称。自己的推测和研究点子写入根目录 `opportunities.md`，`Area:` 填 topic slug。
- 调研中未能核实的元数据、相互矛盾的论文结论写入根目录 `issues.md`，`Area:` 填 topic slug。
- 某方向进入实验或写代码阶段时，代码放在 `projects/<name>/`，作为独立子项目，并在对应 topic 的 `README.md` 中链接。

### 写作语言

调研文档用中文撰写，方法名、术语和论文标题保留英文原文。

## Onboarding

先读 `topics/README.md` 了解已有研究方向，再进入对应 `topics/<slug>/README.md`。
