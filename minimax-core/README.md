# doubao-agent-core

豆包 / MiniMax 智能体的**状态仓库**——只存"让它还是它"的那个部分：记忆、技能、人格、工作区、配置骨架。

不是网盘备份。桌面文件、行情数据包、模型二进制、登录凭据一律不进。

---

## 装了什么

| 目录 | 内容 | 作用 |
|---|---|---|
| `core/memory/` | `user.md`（用户画像，317KB）、`tracking/` 每日状态 | 换机后它还记得你是谁、在做什么 |
| `core/skills/` | 自建技能（ifind、mx 系列等） | 技能不丢 |
| `core/workspace/` | 工作区里的脚本与产物 | 现场可续 |
| `core/builtin-skills/` | 内置技能 18 套 | 补齐运行环境 |
| `core/agents/mavis/` | 座席级 `MEMORY.md`（最新版 2.9MB）、`scripts/`、`skills/` | 主智能体的人设与工具 |
| `core/agents/worker|explore|verifier/` | 子智能体的记忆与配置 | 派工链不断 |
| `core/config/` | 脱敏后的 yaml/json | 结构在，密钥空 |

`core/EXCLUDED.txt` 记录了刻意没备份的东西，一眼能查。

---

## 日常怎么用

**备份（本机 → 仓库）**

```powershell
powershell -ExecutionPolicy Bypass -File D:\agent-core-sync\sync.ps1
```

干的事：白名单目录增量同步 → 配置文件脱敏 → git 提交 → push。全程幂等，重复跑不会出脏数据。

只提交不推送：加 `-NoPush`。

**恢复（仓库 → 本机）**

```powershell
powershell -ExecutionPolicy Bypass -File D:\agent-core-sync\restore.ps1
```

会先把现有 `memory/ skills/ workspace/` 备份到 `~/.minimax_backup_<时间戳>`，再覆盖。
配置不会直接写进生产路径，而是放到 `~/.minimax/_restored_config/`，等你手工填密钥再合。

先看计划：加 `-DryRun`。

---

## 红线

以下永远不进仓库，脚本已硬性排除：

`auth/`、`keys_backup_*/`、`keys_new_*.txt`、`sessions/`、`v2/`、`tools/`、`computer-use/`、`background-tasks/`、`mx_accounts.json`、`local-runtime.auth.json`、`codex-auth.json`、任何 `*.sqlite`、`*.log`。

配置文件里的 `apiKey / appSecret / botToken / accessToken / sessionId` 在写入前统一替换成 `<REDACTED:...>` 占位符。仓库里不该出现真密钥。

---

## 体量

核心约 20MB，远低于 GitHub 单文件 100MiB 硬限和仓库 1GB 建议线。日期快照（`agents/mavis/memory/archive/`）不入库——Git 历史本身就是版本管理，不需要再叠一层。

---

## 恢复后要手工做的三件事

1. `~/.minimax/_restored_config/` 里的 `<REDACTED:...>` 换成真值，再合并到 `~/.minimax/`
2. 重新登录一次（`auth/` 属于凭据，不在备份范围）
3. 跑一次 `sync.ps1 -NoPush` 验证读写链路正常
