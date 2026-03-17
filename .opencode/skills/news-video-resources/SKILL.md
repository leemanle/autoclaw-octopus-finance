---
name: 新闻视频素材免费资源大全
description: 整理全球免费可商用的新闻视频素材网站，支持一键下载、版权说明、自动采集脚本
version: 1.0.0
author: 用户
dependencies:
  - requests
  - yt-dlp
  - beautifulsoup4
entry: news_video_resources.py
---

# 新闻视频素材免费资源大全

本技能专门整理了可用于**新闻资讯类短视频**制作的免费视频素材资源，包含：

- 国际新闻视频素材库（CC0协议，免费商用）
- 国内新闻/时事视频平台
- 新闻类视频下载工具
- 版权说明与商用指南

## 一、国际新闻视频素材网站（免费/CC0协议）

| 网站名称 | 特点 | 新闻素材类型 | 版权说明 | 网址 |
|---------|------|------------|---------|------|
| **Pexels Videos** | 超50万条4K素材，支持新闻/时事分类 | 城市新闻、事件现场、记者采访镜头 | CC0协议，免费商用无需署名 | https://www.pexels.com |
| **Pixabay** | 200万+视频，搜索关键词"news""journalist" | 新闻播报、采访场景、新闻直播间 | CC0协议，免费商用 | https://pixabay.com/videos |
| **Coverr** | 专业电影级素材，适合新闻包装 | 新闻演播室、会议现场 | CC0协议，免费商用 | https://coverr.co |
| **Videvo** | 免费视频素材库，含新闻类 | 记者出镜、新闻现场、突发事件 | 免费版可商用 | https://www.videvo.net |
| **Mixkit** | 高质量4K素材 | 新闻采访、发布会 | 免费商用 | https://mixkit.co |

## 二、视频下载工具

### yt-dlp 安装与使用

```bash
pip install yt-dlp
```

### 常用下载命令

```bash
# 下载Pexels视频
yt
-dlp "https://www.pexels.com/zh-cn/video/xxx/"

# 下载YouTube视频
yt-dlp "https://www.youtube.com/watch?v=xxx"

# 下载B站视频
yt-dlp "https://www.bilibili.com/video/xxx"

# 批量下载列表
yt-dlp --batch-file urls.txt
```

## 三、示例代码

```python
# news_video_resources.py
import requests
import yt_dlp
import os

class NewsVideoDownloader:
    def __init__(self, save_dir="videos"):
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def download_pexels(self, video_id, filename=None):
        """下载Pexels视频"""
        # 需要先获取视频URL
        url = f"https://www.pexels.com/video/{video_id}/"
        ydl_opts = {
            'outtmpl': f'{self.save_dir}/%(title)s.%(ext)s',
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def download_youtube(self, url, filename=None):
        """下载YouTube视频"""
        ydl_opts = {
            'outtmpl': f'{self.save_dir}/%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return info.get('title')

    def batch_download(self, url_list):
):
        """批量下载"""
        for url in url_list:
            try:
                self.download_youtube(url)
            except Exception as e:
                print(f"下载失败: {url}, 错误: {e}")

# 使用示例
if __name__ == "__main__":
    downloader = NewsVideoDownloader("news_videos")
    # 下载示例
    # downloader.download_youtube("https://www.youtube.com/watch?v=xxx")
    print("新闻视频素材下载工具")
    print("支持: Pexels, YouTube, B站等平台")
```
