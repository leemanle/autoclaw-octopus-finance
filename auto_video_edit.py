# FFmpeg全自动视频剪辑脚本
# 功能：视频素材 + AI配音 + 字幕 -> 合成最终视频

import imageio_ffmpeg
import subprocess
import os
import sys

# 配置
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VIDEO_SRC = r"C:\Users\Administrator\Desktop\自媒体视频生产\01_素材\视频素材\test_bilibili.mp4"
AUDIO_SRC = r"C:\Users\Administrator\Desktop\自媒体视频生产\03_配音\voice_test.mp3"
SRT_SRC = r"C:\Users\Administrator\Desktop\自媒体视频生产\02_文案\字幕文件\2026-03-14_化工品涨价_字幕.srt"
OUTPUT_DIR = r"C:\Users\Administrator\Desktop\自媒体视频生产\04_视频\抖音"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "final_output.mp4")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr[:500]}")
        return False
    return True

# 如果没有配音文件，生成测试音调
if not os.path.exists(AUDIO_SRC):
    print("生成测试音频...")
    test_audio = os.path.join(OUTPUT_DIR, "test_tone.mp3")
    # 生成1分钟440Hz正弦波测试音
    cmd = [FFMPEG, "-f", "lavfi", "-i", "sine=frequency=440:duration=60", 
           "-ac", "2", "-y", test_audio]
    run_cmd(cmd)
    AUDIO_SRC = test_audio

print(f"FFmpeg: {FFMPEG}")
print(f"输入视频: {VIDEO_SRC}")
print(f"配音: {AUDIO_SRC}")
print(f"字幕: {SRT_SRC}")
print(f"输出: {OUTPUT_FILE}")

# 方案1: 有字幕文件 - 烧录字幕
if os.path.exists(SRT_SRC):
    print("\n=== 方案: 视频+配音+字幕 ===")
    cmd = [
        FFMPEG, "-i", VIDEO_SRC,           # 输入视频
        "-i", AUDIO_SRC,                    # 输入音频
        "-vf", f"subtitles='{SRT_SRC}'",    # 烧录字幕
        "-c:v", "libx264",                  # 视频编码
        "-preset", "fast",                  # 快速编码
        "-crf", "23",                       # 质量
        "-c:a", "aac",                      # 音频编码
        "-b:a", "128k",                     # 音频码率
        "-shortest",                        # 取音视频最短者
        "-y", OUTPUT_FILE                   # 输出
    ]
    run_cmd(cmd)

# 方案2: 无字幕 - 简单合成
else:
    print("\n=== 方案: 视频+配音(无字幕) ===")
    cmd = [
        FFMPEG, "-i", VIDEO_SRC,
        "-i", AUDIO_SRC,
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest", "-y", OUTPUT_FILE
    ]
    run_cmd(cmd)

# 检查输出
if os.path.exists(OUTPUT_FILE):
    size = os.path.getsize(OUTPUT_FILE)
    print(f"\n✅ 成功! 输出: {OUTPUT_FILE}")
    print(f"   大小: {size/1024/1024:.1f}MB")
else:
    print("\n❌ 失败!")
