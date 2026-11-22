# Changelog

格式遵循 Keep a Changelog，版本号语义化。

## [1.0.0] - 2026-11-22

### 从"能跑的脚本"升级为"可验证的工程"

此前只有 sync / restore 两个脚本，跑通就算完成，没有任何自动化校验。问题在于：脱敏规则漏一个字段、某个大文件误入、结构被改坏，都要靠人眼发现。

### Added

- `verify.ps1`：六类检查的校验器。禁止路径存在、必备资产缺失、单文件超 50/100MiB、真实密钥泄漏、manifest 与实际文件哈希不符、总体积超预算。任一 FAIL 返回非零。
- `generate-manifest.ps1`：产出 `manifest.json`，含版本号、生成时间、每文件 SHA256 与字节数、总量。用于事后核对"云端那份到底是不是我本机这份"。
- CI：`.github/workflows/verify.yml`，每次 push 在干净环境重跑校验，避免本地环境差异掩盖问题。
- `VERSION`：语义化版本，随 manifest 一起入库。
- 同步流程加入**阻断式校验门**：manifest 生成失败或 verify 出现 FAIL，直接中止提交，不再产出一个"看起来成功"的坏快照。

### Changed

- `sync.ps1` 从五步变七步，git 提交前必须先过校验。
- 传输通道固定为 SSH 443（22 端口在本机被周期性阻断）。

### Known gaps

- 仍与智谱时期的 `autoclaw-octopus-finance` 共用仓库，靠 `minimax-core/` 子目录隔离。拆成独立库需要可用 PAT 或网页登录。
- `auth/`、`keys_*` 属于凭据，永久不入库；换机后必须重新登录，这一点无法工程化绕过。
