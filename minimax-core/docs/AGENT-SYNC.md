# 智能体状态同步 SOP（给 Mavis / MiniMax 执行）

## 这份文档解决什么

你的记忆、技能、人格、工作区散在本机 `%USERPROFILE%\.minimax` 里，机器坏了或换机就归零。
这个仓库把它们变成可版本化、可恢复的状态。

**目标不是备份文件，是保住"你还是你"。**

---

## 仓库定位

- 远端：GitHub 私有库 `doubao-agent-core`（账号 leemanle）
- 本地工作区：`D:\agent-core-sync`
- 协议：SSH（`~/.ssh/id_ed25519`），不走 HTTPS token
- 只存文本状态，约 20MB

---

## 何时触发同步

满足任一条件就跑：

1. 用户明确说"存一下""备份一下""同步"
2. 本次会话产生了长期记忆（写入 `memory/user.md` 或 `agents/mavis/memory/MEMORY.md`）
3. 新增或修改了技能（`skills/` 下有文件变化）
4. 配置变更（模型、渠道、权限、MCP 服务）
5. 距上次同步超过 3 天

不需要同步的场景：只做了问答、只生成了临时文件、只跑了数据查询没落盘。

---

## 执行流程

### 第一步：同步

```
powershell -ExecutionPolicy Bypass -File D:\agent-core-sync\sync.ps1
```

脚本内部顺序是固定的，不要跳过：

1. 白名单目录增量复制（memory / skills / workspace / .builtin-skills / agents）
2. 只取 `agents/mavis/memory/MEMORY.md` 最新版，`archive/` 按日快照不入库
3. 8 个配置文件逐个读入、正则脱敏、再写出到 `core/config/`
4. `git add -A` → 有变更才提交 → `git push origin HEAD`

### 第二步：校验（必做，不靠猜）

```
git -C D:\agent-core-sync log -1 --pretty="%h %ad %s" --date=iso
git -C D:\agent-core-sync status --short
git -C D:\agent-core-sync ls-remote origin HEAD
```

判定标准：

- 本地 HEAD 与 `ls-remote` 返回的 SHA 一致 → 推送成功
- `status --short` 为空 → 无残留未提交
- 提交信息是 `sync YYYY-MM-DD HH:mm` → 时间对得上

任一不满足，视为失败，进入故障处理，**不要向用户报告"已完成"**。

### 第三步：回报

一句话给结论：提交短哈希、文件数、体积。不要贴 diff，不要列目录。

---

## 故障处理

| 现象 | 原因 | 动作 |
|---|---|---|
| `git push` 报 `Connection reset` / timeout | HTTPS 或网页通道被掐，SSH 正常 | 确认 `git remote -v` 是 `git@github.com:` 开头；`ssh -T git@github.com` 应返回 `Hi leemanle!` |
| `Permission denied (publickey)` | SSH 密钥未加载 | 检查 `~/.ssh/id_ed25519` 存在；`ssh-add` |
| `robocopy` 退出码 ≥ 8 | 源文件被占用或路径不存在 | 看具体目录，跳过并记录，不整体中止 |
| 提交后仓库体积异常增长 | 误入大文件 | `git rm --cached` 该文件，补进 `.gitignore`，再强推前先确认历史是否需要清理 |
| 敏感值出现在 diff 里 | 脱敏规则漏了字段 | 立即改 `sync.ps1` 的 `Sanitize-Text` 函数，`git filter-repo` 清历史，改密钥 |

---

## 恢复流程（换机 / 重装后）

### 前提

装好 Git，配好 SSH 密钥，能 `ssh -T git@github.com` 通。

### 步骤

```
git clone git@github.com:leemanle/doubao-agent-core.git D:\agent-core-sync
powershell -ExecutionPolicy Bypass -File D:\agent-core-sync\restore.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File D:\agent-core-sync\restore.ps1
```

`restore.ps1` 做的事：

1. 现有 `memory/ skills/ workspace/` 先备份到 `~/.minimax_backup_<时间戳>`
2. 按目录还原到 `%USERPROFILE%\.minimax`
3. 配置不直接覆盖生产路径，放到 `~/.minimax/_restored_config/` 等你手工合并

### 恢复后必须手工补的三项

1. **密钥**：`_restored_config/` 里所有 `<REDACTED:...>` 换成真值，再合并进 `~/.minimax/`
2. **登录态**：`auth/` 属于凭据，不在备份范围，重新登录一次
3. **验证**：跑 `sync.ps1 -NoPush`，看能否正常读源、写 core

三项做完再启用定时任务。

---

## 红线（任何情况下不破）

- 不打包 `auth/`、`keys_*`、`sessions/`、`v2/`、`tools/`、`computer-use/`、`background-tasks/`
- 不传 `mx_accounts.json`、`local-runtime.auth.json`、`codex-auth.json`
- 不把 `*.sqlite`、`*.log`、行情数据 zip、模型二进制塞进 Git
- 仓库是私有的，但**私有不等于保险箱**：任何真密钥都不该进去
- 单文件超 50MiB 立刻停手，改方案；超 100MiB Git 直接拒绝

---

## 一句话总结

记忆和技能用 Git 管版本，密钥和执行态永远留在本机。仓库里只该有"能公开但不想公开"的东西。
