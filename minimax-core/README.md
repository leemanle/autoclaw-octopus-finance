# minimax-core — 智能体状态仓库

豆包 / MiniMax 智能体的**状态**，不是桌面备份。

只存"让它还是它"的部分：记忆、技能、人格、工作区、配置骨架。桌面文件、行情包、模型二进制、登录凭据一律不进。

存放位置：GitHub 私有库 `leemanle/autoclaw-octopus-finance` → `minimax-core/`
本地工作副本：`D:\gh_sync_work`

---

## 装了什么

【记忆】`core/memory/user.md`（用户画像 318KB）、`core/memory/tracking/` 每日状态
【座席】`core/agents/mavis/memory/MEMORY.md`（主智能体记忆 2.9MB，每日快照不入库）
【技能】`core/skills/`（ifind、mx 系列共 8 套）、`core/builtin-skills/`（内置 18 套 + 图标资产）
【工作区】`core/workspace/`（脚本与产物）
【子智能体】`core/agents/worker|explore|verifier/`
【配置】`core/config/`（8 个文件，密钥已替换为 `<REDACTED:...>`）

`core/EXCLUDED.txt` 记录刻意没备份的内容，一眼能查。

---

## 日常操作

**备份（本机 → 远端）**

```powershell
powershell -ExecutionPolicy Bypass -File D:\gh_sync_work\minimax-core\sync.ps1
```

流程固定：白名单增量同步 → 配置脱敏 → `git add minimax-core` → 有变更才提交 → push。
重复跑幂等。只想提交不推送加 `-NoPush`。

**恢复（远端 → 本机）**

```powershell
powershell -ExecutionPolicy Bypass -File D:\gh_sync_work\minimax-core\restore.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File D:\gh_sync_work\minimax-core\restore.ps1
```

先看计划，再执行。执行时会把现有 `memory/ skills/ workspace/` 备份到 `~/.minimax_backup_<时间戳>`，配置不直写生产路径，放到 `~/.minimax/_restored_config/` 等手工填。

---

## 传输通道

SSH，端口 443（22 端口在这台机器上经常被断）。

`~/.ssh/config` 已配：

```
Host github.com
    HostName ssh.github.com
    Port 443
    User git
    IdentityFile ~/.ssh/id_ed25519
```

验证：`ssh -T git@github.com` 应返回 `Hi leemanle!`

---

## 红线

永不入库：`auth/`、`keys_backup_*/`、`keys_new_*.txt`、`sessions/`、`v2/`、`tools/`、`computer-use/`、`background-tasks/`、`mx_accounts.json`、`local-runtime.auth.json`、`codex-auth.json`、任何 `*.sqlite`、`*.log`。

写入前统一脱敏的字段：`apiKey / appSecret / botToken / accessToken / sessionId`。
仓库是私有的，但私有不是保险箱。

---

## 体量

652 文件 / 20.33MB。远低于 GitHub 单文件 100MiB 硬限与 1GB 建议线。

---

## 恢复后手工补三件

1. `~/.minimax/_restored_config/` 里的 `<REDACTED:...>` 换成真值，再合进 `~/.minimax/`
2. 重新登录一次（`auth/` 是凭据，不在备份范围）
3. 跑 `sync.ps1 -NoPush` 验证读写链路
