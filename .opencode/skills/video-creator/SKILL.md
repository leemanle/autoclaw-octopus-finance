---
name: 自媒体短视频自动制作
description: 自动完成短视频脚本撰写、素材搜索下载、AI中文配音、视频合成与发布的全流程自动化
version: 1.0.0
author: AutoClaw
metadata:
  emoji: 🎬
requires:
  bins:
    - ffmpeg
install:
  - id: pip_deps
    kind: pip
    packages:
      - yt-dlp
      - edge-tts
      - moviepy
      - requests
      - beautifulsoup4
    label: 安装Python依赖库
---

# 自媒体短视频自动制作

本技能实现从选题到成片的完整短视频自动化流程。

## 核心功能

- 自动获取当日热点话题/财经资讯
- 生成符合平台风格的短视频脚本
- 搜索并下载免费可商用视频素材
- 生成自然流畅的中文AI配音
- 智能匹配素材与配音，合成成品视频

## 使用方法

### 1. 热点视频生成

告诉我你想做什么主题的视频，例如：

- "做一个伊朗中东局势的财经分析视频"
- "生成一个科技热点短视频"

### 2. 技能会自动

1. 搜索相关热点资讯
2. 生成短视频脚本
3. 下载视频素材（如有）
4. 生成AI配音
5. 合成最终视频

### 3. 输出位置

视频会保存到：`C:\Users\admin\.openclaw-autoclaw\workspace\videos\`

## 示例命令

```
生成一个财经热点视频
```

## 依赖说明



- **ffmpeg**: 视频处理（已安装）
- **yt-dlp**: 视频素材下载
- **edge-tts**: AI中文配音
- **moviepy**: 视频合成
