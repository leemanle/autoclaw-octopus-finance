---
name: agent-core-sync
display_name: 智能体状态同步
title: 记忆与技能云端备份 / 恢复
description: 把本机智能体状态（记忆、技能、人格、工作区、配置骨架）同步到 GitHub 私有库 minimax-core，并在换机后一键恢复。用户说"备份""存一下""同步""我的记忆会不会丢"或本次会话写入长期记忆、新增技能、改配置时使用。
version: 1.0.0
---

# agent-core-sync

## 这个技能干什么

把 `%USERPROFILE%\.minimax` 里"让它还是它"的部分推到云端，换机器能捡回来。
**不是备份桌面文件**，桌面文件、行情包、模型二进制、登录凭据一律不进。

- 远端：`leemanle/autoclaw-octopus-finance` 的 `minimax-core/` 目录（私有）
- 本地工作副本：`D:\gh_sync_work`
- 通道：SSH 443，无密码

## 何时执行

任一成立：

1. 用户要求备份 / 同步 / 存一下
2. 本次会话写了 `memory/user.md` 或 `agents/mavis/memory/MEMORY.md`
3. 新增或改动技能
4. 改了模型、渠道、权限、MCP 配置
5. 距上次同步超过 3 天

不用执行：纯问答、临时文件、只查数据没落盘。

## 备份

```
powershell -ExecutionPolicy Bypass -File D:\gh_sync_work\minimax-core\sync.ps1
```

脚本内部固定五步，不要绕开：

1. 白名单增量复制：memory / skills / workspace / .builtin-skills / agents
2. 座席记忆只取 `MEMORY.md` 最新版；`archive/` 按日快照不入库，Git 历史代替版本管理
3. 8 个配置文件读入 → 正则脱敏 → 写出到 `core/config/`
4. `git add minimax-core`，有变更才提交，信息格式 `sync YYYY-MM-DD HH:mm`
5. `git push origin main`

幂等，重复跑安全。只提交不推送加 `-NoPush`。

## 校验（必做，不靠猜）

```
git -C D:\gh_sync_work log -1 --oneline
git -C D:\gh_sync_work status --short
git -C D:\gh_sync_work ls-remote origin refs/heads/main
```

- 本地 HEAD 等于远端 SHA → 成功
- `status --short` 为空 → 无残留
- 任一不满足 → 视为失败，不许向用户报"已完成"

## 恢复

```
git clone git@github.com:leemanle/autoclaw-octopus-finance.git D:\gh_sync_work
powershell -File D:\gh_sync_work\minimax-core\restore.ps1 -DryRun
powershell -File D:\gh_sync_work\minimax-core\restore.ps1
```

还原前会把现有 `memory/ skills/ workspace/` 备份到 `~/.minimax_backup_<时间戳>`。
配置不覆盖生产路径，放 `~/.minimax/_restored_config/` 等人工合并。

恢复后必须补三件：填真密钥、重新登录（`auth/` 不在备份里）、跑 `sync.ps1 -NoPush` 验链路。

## 故障

| 现象 | 处理 |
|---|---|
| 连接超时 / reset | 确认 `~/.ssh/config` 里 github.com 走 443；`ssh -T git@github.com` 应返回 `Hi leemanle!` |
| publickey denied | 查 `~/.ssh/id_ed25519`，必要时 `ssh-add` |
| robocopy 退出码 ≥ 8 | 记录该目录跳过，不整体中止 |
| 仓库体积暴涨 | `git rm --cached` 误入文件，补 `.gitignore`，评估是否清历史 |
| diff 里出现敏感值 | 改 `sync.ps1` 的 `Sanitize-Text`，清历史，换密钥 |

## 红线

不入库：`auth/`、`keys_*`、`sessions/`、`v2/`、`tools/`、`computer-use/`、`background-tasks/`、`mx_accounts.json`、`local-runtime.auth.json`、`codex-auth.json`、`*.sqlite`、`*.log`。

脱敏字段：`apiKey / appSecret / botToken / accessToken / sessionId`。

仓库是私有的，但私有不是保险箱。单文件超 50MiB 停手，超 100MiB Git 直接拒。
