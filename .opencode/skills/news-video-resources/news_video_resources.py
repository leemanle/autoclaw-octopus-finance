#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻视频素材免费资源下载工具
支持 Pexels, YouTube, B站等平台的视频素材下载
"""

import requests
import yt_dlp
import os
import sys


class NewsVideoDownloader:
    def __init__(self, save_dir="videos"):
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def download_pexels(self, video_id, filename=None):
        """下载Pexels视频

        Args:
            video_id: Pexels视频ID
            filename: 可选的文件名
        """
        url = f"https://www.p.pexels.com/video/{video_id}/"
        ydl_opts = {
            'outtmpl': f'{self.save_dir}/%(title)s.%(ext)s',
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def download_youtube(self, url, filename=None):
        """下载YouTube视频

        Args:
            url: YouTube视频URL
            filename: 可选的文件名

        Returns:
            视频标题
        """
        ydl_opts = {
            'outtmpl': f'{self.save_dir}/%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return info.get('title')

    def batch_download(self, url_list):
        """批量下载视频

        Args:
            url_list: 视频URL列表
        """
        for url in url_list:
            try:
                print(f"正在下载: {url}")
                self.download_youtube(url)
                print(f"✓ 下载成功: {url}")
            except Exception as e:
                print(f"✗ 下载失败: {url}, 错误: {e}")


if __name__ == "__main__":
    downloader = NewsVideoDownloader("news_videos")
    print("新闻视频素材下载工具")
    print("支持: Pexels, YouTube, B站等平台")
    print("使用示例:")
    print("  python news_video_resources.py <url>")
