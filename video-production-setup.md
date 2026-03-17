# 视频生产环境安装指南

## 🎯 你的需求
- 抓取财经/军事/时政新闻和热点
- 一针见血解读（专业博主视角）
- 中文AI配音
- 视频剪辑、编辑、加字幕
- AI视频生成
- 文案+视频+配音完美结合

---

## ✅ 已就绪的能力（OpenClaw内置）

| 工具 | 功能 | 命令/技能 |
|------|------|-----------|
| 抓取新闻 | 读取网页内容 | `web_fetch`, `browser`, `autoglm-open-link` |
| 联网搜索 | 查找热点 | `autoglm-websearch` |
| 文案写作 | 说服性文案 | `copywriting`, `seo-content-writer` |
| AI配音 | 中文TTS | `tts` |
| FFmpeg剪辑 | 视频剪辑 | `FFmpeg Video Editor` skill |
| 生成配图 | 文字转图片 | `autoglm-generate-image` |

---

## ⚠️ 需要安装的本地软件

### 1. FFmpeg（必需）- 视频剪辑核心工具

**下载：**
https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip

**安装步骤：**
1. 下载并解压到 `C:\ffmpeg`
2. 将 `C:\ffmpeg\bin` 添加到系统PATH环境变量
3. 重启终端，验证：`ffmpeg -version`

**快速安装（如果有包管理器）：**
```bash
# 使用 scoop
scoop install ffmpeg

# 使用 chocolatey
choco install ffmpeg

# 使用 winget
winget install Gyan.FFmpeg
```

---

### 2. Python + 库AI视频

**安装Python：**
- https://www.python.org/downloads/ （勾选"Add to PATH"）

**安装库：**
```bash
pip install moviepy
pip install opencv-python
pip install pydub
```

---

### 3. AI视频生成工具（可选）

**推荐：**
- **Runway ML** — https://runwayml.com/ （需API key）
- **HeyGen** — https://www.heygen.com/ （数字人视频）
- **Stable Video Diffusion** — 本地部署

---

## 🚀 安装后验证

运行以下命令检查环境：

```bash
# FFmpeg
ffmpeg -version

# Python
python --version
pip list | grep -E "moviepy|opencv|pydub"
```

---

## 📋 工作流示例

```python
# 1. 抓取热点
使用 autoglm-websearch 或 web_fetch

# 2. 撰写文案
使用 copywriting 或 seo-content-writer

# 3. 生成配音
使用 tts 工具

# 4. 剪辑视频
使用 FFmpeg Video Editor skill

# 5. 合成
FFmpeg 合并视频+音频+字幕
```

---

## 💡 安装进度

- [ ] FFmpeg 已安装并添加到PATH
- [ ] Python 已安装
- [ ] 必要库已安装
- [ ] AI视频工具已配置（如需）
- [ ] 验证所有工具

**完成上述步骤后，告诉我"安装完成"，我会开始完整工作流测试。**
