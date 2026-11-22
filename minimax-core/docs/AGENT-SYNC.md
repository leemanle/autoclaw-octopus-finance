# 智能体状态同步 SOP（给 Mavis / MiniMax 执行）

## 解决什么

你的记忆、技能、人格、工作区散在 `%USERPROFILE%\.minimax`。机器坏了或换机就归零。
这份流程把它们变成可版本化、可恢复的状态。

**目标不是备份文件，是保住"你还是你"。**

---

## 坐标

- 远端：GitHub 私有库 `leemanle/autoclaw-octopus-finance` → 目录 `minimax-core/`
- 本地工作副本：`D:\gh_sync_work`
- 通道：SSH over 443（22 端口不稳）
- 规模：652 文件 / 20.33MB

---

## 何时触发

任一条件成立就跑：

1. 用户说"存一下""备份""同步"
2. 本次会话产生了长期记忆（写入 `memory/user.md` 或 `agents/mavis/memory/MEMORY.md`）
3. 新增或改动了技能
4. 配置变更（模型 / 渠道 / 权限 / MCP）
5. 距上次同步超过 3 天

不必跑的场景：纯问答、临时文件、只查数据没落盘。

---

## 执行

### 第一步：同步

```
powershell -ExecutionPolicy Bypass -File D:\gh_sync_work\minimax-core\sync.ps1
```

脚本顺序固定，不要跳：

1. 白名单增量复制（memory / skills / workspace / .builtin-skills / agents）
2. 座席记忆只取 `MEMORY.md` 最新版，`archive/` 按日快照不入库（Git 历史本身就是版本）
3. 8 个配置文件逐个读入 → 正则脱敏 → 写出到 `core/config/`
4. `git add minimax-core` → 有变更才提交 → `git push origin main`

### 第二步：校验（必做）

```
git -C D:\gh_sync_work log -1 --oneline
git -C D:\gh_sync_work status --short
git -C D:\gh_sync_work ls-remote origin refs/heads/main
```

判定：

- 本地 HEAD 与 `ls-remote` 返回的 SHA 一致 → 推送成功
- `status --short` 为空 → 无残留
- 提交信息形如 `sync YYYY-MM-DD HH:mm` → 时间对得上

任一不满足即失败，进故障处理，**不许报"已完成"**。

### 第三步：回报

一句话：提交短哈希、文件数、体积。不贴 diff，不列目录。

---

## 故障处理

| 现象 | 原因 | 动作 |
|---|---|---|
| `Connection timed out` / `reset` | 22 端口被断 | 确认 `~/.ssh/config` 里 github.com 走 443；`ssh -T git@github.com` 应返回 `Hi leemanle!` |
| `Permission denied (publickey)` | 密钥未加载 | 查 `~/.ssh/id_ed25519`；`ssh-add` |
| `robocopy` 退出码 ≥ 8 | 源被占用或路径不存在 | 记录跳过，不整体中止 |
| 仓库体积异常增长 | 大文件误入 | `git rm --cached` + 补 `.gitignore`，必要时清历史 |
| 敏感值出现在 diff | 脱敏规则漏字段 | 改 `sync.ps1` 的 `Sanitize-Text`，清历史，换密钥 |

---

## 恢复（换机 / 重装）

前提：装 Git，配 SSH key，`ssh -T git@github.com` 通。

```
git clone git@github.com:leemanle/autoclaw-octopus-finance.git D:\gh_sync_work
powershell -File D:\gh_sync_work\minimax-core\restore.ps1 -DryRun
powershell -File D:\gh_sync_work\minimax-core\restore.ps1
```

`restore.ps1` 做三件事：

1. 现有 `memory/ skills/ workspace/` 先备份到 `~/.minimax_backup_<时间戳>`
2. 按目录还原到 `%USERPROFILE%\.minimax`
3. 配置放 `~/.minimax/_restored_config/`，不直接覆盖生产路径

### 恢复后必补三项

1. **密钥**：`_restored_config/` 里 `<REDACTED:...>` 换真值，再合进 `~/.minimax/`
2. **登录态**：`auth/` 是凭据，不在备份范围，重新登录
3. **验证**：跑 `sync.ps1 -NoPush`，确认能读源、写 core

三项做完再启用定时任务。

---

## 红线

- 不打包 `auth/`、`keys_*`、`sessions/`、`v2/`、`tools/`、`computer-use/`、`background-tasks/`
- 不传 `mx_accounts.json`、`local-runtime.auth.json`、`codex-auth.json`
- 不把 `*.sqlite`、`*.log`、行情 zip、模型二进制塞进 Git
- 私有不等于保险箱，任何真密钥都不该进仓库
- 单文件超 50MiB 停手换方案；超 100MiB Git 直接拒

---

## 如果以后要独立成库

现在没独立库，是因为网页通道和密码都不可用，只能走 SSH 推已有库。
一旦拿到可用的 PAT 或能登录网页，一条命令即可拆分：

```
# 用 API 建空私有库后，把 minimax-core 作为独立仓库推出
git -C D:\gh_sync_work subtree split -p minimax-core -b minimax-core-only
git push git@github.com:<user>/doubao-agent-core.git minimax-core-only:main
```

拆完后把 `sync.ps1` 的 `$Repo` 指向新库工作副本即可，其余不变。
