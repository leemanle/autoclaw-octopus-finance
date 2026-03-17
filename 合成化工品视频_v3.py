"""
化工品涨价视频合成脚本（修复版）
使用Python + moviepy创建60秒视频
"""

from moviepy import *
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 配置
OUTPUT_PATH = r"C:\Users\Administrator\Desktop\化工品涨价_抖音_1080P.mp4"

# 颜色定义
COLOR_BG = (26, 26, 46)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 50, 50)
COLOR_ORANGE = (255, 140, 0)
COLOR_GOLD = (255, 215, 0)
COLOR_GREEN = (46, 139, 87)

print("Starting video composition...")

def find_audio_file():
    import glob
    mp3_files = glob.glob(os.path.expandvars(r"%TEMP%\openclaw\**\*.mp3"), recursive=True)
    if mp3_files:
        print(f"Found audio: {mp3_files[0]}")
        return mp3_files[0]
    return None

def create_text_clip(text, duration, color=COLOR_WHITE, size=100):
    img = Image.new('RGB', (1920, 1080), color=COLOR_BG)
    draw = ImageDraw.Draw(img)
    
    font_size = size
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    lines = text.split('\n')
    total_height = len(lines) * font_size
    y_start = (1080 - total_height) // 2
    
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (1920 - text_width) // 2
        y = y_start + i * font_size * 1.2
        draw.text((x, y), line, fill=color, font=font)
    
    return ImageClip(np.array(img)).with_duration(duration)

try:
    audio_path = find_audio_file()
    
    print("Creating clips...")
    clip1 = create_text_clip("液氯 +300%", 5, color=COLOR_RED, size=150)
    clip2 = create_text_clip("扩散指数\n60.39%", 13, color=COLOR_ORANGE, size=120)
    clip3 = create_text_clip("油煤套利\n利润空间放大", 20, color=COLOR_GOLD, size=100)
    clip4 = create_text_clip("宝丰能源 600989\n+6% 涨停", 14, color=COLOR_GREEN, size=110)
    clip5 = create_text_clip("柚子暴风眼\n专注硬核逻辑", 8, color=COLOR_GOLD, size=100)
    
    print("Concatenating...")
    video_clip = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])
    
    if audio_path:
        print("Adding audio...")
        audio_clip = AudioFileClip(audio_path)
        if audio_clip.duration < 60:
            audio_clip = audio_clip.loop(duration=60)
        video_clip = video_clip.set_audio(audio_clip)
    
    print(f"Exporting to: {OUTPUT_PATH}")
    video_clip.write_videofile(
        OUTPUT_PATH,
        fps=30,
        codec='libx264',
        audio_codec='aac',
        bitrate='8000k',
        threads=4
    )
    
    print(f"\nSUCCESS! Video created")
    print(f"Location: {OUTPUT_PATH}")
    print(f"Duration: {video_clip.duration}s")
    print(f"Resolution: 1920x1080")
    print(f"FPS: 30")
    
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
