"""
化工品涨价视频合成脚本
使用Python + moviepy + PIL创建60秒视频
"""

from moviepy import *
from PIL import Image, ImageDraw, ImageFont
import os

# 配置
OUTPUT_PATH = "C:\\Users\\Administrator\\Desktop\\化工品涨价_抖音_1080P.mp4"
AUDIO_PATH = "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\openclaw\\tts-i3qacR\\voice-1773471464969.mp3"
CAPTION_FILE = "C:\\Users\\Administrator\\.openclaw-autoclaw\\workspace\\video-script-chemical-boom.srt"

# 颜色定义
COLOR_BG = (26, 26, 46)       # 深蓝黑
COLOR_ORANGE = (255, 140, 0)  # 柱子色
COLOR_RED = (255, 50, 50)     # 红色
COLOR_GREEN = (46, 139, 87)   # 海绿
COLOR_GOLD = (255, 215, 0)    # 金色
COLOR_WHITE = (255, 255, 255)  # 白色

print("开始合成视频...")

# 检查音频文件是否存在
if not os.path.exists(AUDIO_PATH):
    print(f"错误：音频文件不存在 {AUDIO_PATH}")
    print("尝试查找备用音频...")
    # 查找TEMP目录下的mp3文件
    import glob
    mp3_files = glob.glob(os.path.expandvars(r"%TEMP%\openclaw\**\*.mp3"), recursive=True)
    if mp3_files:
        AUDIO_PATH = mp3_files[0]
        print(f"找到音频：{AUDIO_PATH}")
    else:
        print("未找到音频文件，创建静音...")
        AUDIO_PATH = None

# 创建背景视频
def create_background_clip(duration=60):
    """创建深色背景"""
    return ColorClip((1920, 1080), color=COLOR_BG, duration=duration)

def create_text_clip(text, duration, fontsize=100, color=COLOR_WHITE, position='center'):
    """创建文字片段"""
    try:
        clip = TextClip(text, fontsize=fontsize, color=color, font='SimHei-Bold', size=(1920, 1080))
        clip = clip.set_position(position).set_duration(duration)
        return clip
    except Exception as e:
        print(f"创建文字失败：{e}")
        # 如果系统字体失败，使用默认字体
        clip = TextClip(text, fontsize=fontsize, color=color, size=(1920, 1080))
        clip = clip.set_position(position).set_duration(duration)
        return clip

def create_number_clip(text, duration, fontsize=150, color=COLOR_RED, position='center'):
    """创建大数字片段"""
    return create_text_clip(text, duration, fontsize=fontsize, color=color, position=position)

# 创建各个分镜
def create_clips():
    """创建所有分镜"""
    clips = []
    
    # 分镜1（0:00-0:05）：钩子
    clip1 = create_number_clip("液氯 +300%", 5, fontsize=150, color=COLOR_RED, position='center')
    clips.append(clip1)
    
    # 分镜2（0:05-0:18）：数据展示
    clip2 = create_text_clip("扩散指数 60.39%", 13, fontsize=120, color=COLOR_ORANGE, position='center')
    clips.append(clip2)
    
    # 分镜3（0:18-0:38）：核心逻辑
    clip3 = create_text_clip("油煤套利\n利润空间放大", 20, fontsize=100, color=COLOR_GOLD, position='center')
    clips.append(clip3)
    
    # 分镜4（0:38-0:52）：受益标的
    clip4 = create_text_clip("宝丰能源 600989\n+6% 涨停", 14, fontsize=110, color=COLOR_GREEN, position='center')
    clips.append(clip4)
    
    # 分镜5（0:52-0:60）：品牌收尾
    clip5 = create_text_clip("柚子暴风眼\n专注硬核逻辑", 8, fontsize=100, color=COLOR_GOLD, position='center')
    clips.append(clip5)
    
    # 串联所有分镜
    final_clip = concatenate_videoclips(clips)
    return final_clip

# 主流程
try:
    print("创建分镜...")
    video_clip = create_clips()
    
    print("添加音频...")
    if AUDIO_PATH and os.path.exists(AUDIO_PATH):
        audio_clip = AudioFileClip(AUDIO_PATH)
        if audio_clip.duration < 60:
            # 如果音频不够60秒，循环
            audio_clip = audio_clip.loop(duration=60)
        video_clip = video_clip.set_audio(audio_clip)
    
    print("导出视频...")
    video_clip.write_videofile(
        OUTPUT_PATH,
        fps=30,
        codec='libx264',
        audio_codec='aac',
        bitrate='8000k',
        threads=4,
        verbose=False,
        logger=None
    )
    
    print(f"\n✅ 视频合成成功！")
    print(f"📍 输出路径：{OUTPUT_PATH}")
    print(f"⏱️ 时长：{video_clip.duration}秒")
    print(f"📐 分辨率：1920x1080")
    print(f"🎬 帧率：30fps")
    
except Exception as e:
    print(f"\n❌ 视频合成失败：{e}")
    import traceback
    traceback.print_exc()
