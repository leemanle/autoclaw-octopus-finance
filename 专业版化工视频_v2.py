"""
专业化工板块视频生成（增强版）
带动态效果、数据图表、专业UI
"""

from moviepy import *
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math

# 配置
OUTPUT_PATH = r"C:\Users\Administrator\Desktop\化工板块分析_V2_抖音_1080P.mp4"

# 颜色定义
COLOR_BG = (10, 10, 30)  # 深蓝黑
COLOR_ORANGE = (255, 140, 0)  # 橙色
COLOR_GOLD = (255, 215, 0)  # 金色
COLOR_GREEN = (46, 200, 100)  # 绿色
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (100, 100, 120)

print("Creating professional video...")

def create_gradient_background(width=1920, height=1080, color1=(10, 10, 30), color2=(30, 30, 80)):
    """创建渐变背景"""
    img = Image.new('RGB', (width, height))
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        for x in range(width):
            img.putpixel((x, y), (r, g, b))
    return np.array(img)

def create_title_frame(text, subtitle="", duration=5, color=COLOR_ORANGE):
    """创建标题帧（带装饰）"""
    # 渐变背景
    bg = create_gradient_background()
    
    # 创建主图像
    img = Image.new('RGB', (1920, 1080))
    pixels = np.array(bg)
    img = Image.fromarray(pixels)
    draw = ImageDraw.Draw(img)
    
    # 装饰线条
    for i in range(5):
        y = 200 + i * 20
        draw.line([(200, y), (1720, y)], fill=(color[0], color[1], color[2], 50), width=2)
    
    # 主标题
    try:
        font_large = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 150)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 60)
    except:
        font_large = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    
    # 主标题居中
    bbox = draw.textbbox((0, 0), text, font=font_large)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w) // 2, 350), text, fill=color, font=font_large)
    
    # 副标题
    if subtitle:
        bbox = draw.textbbox((0, 0), subtitle, font=font_sub)
        w = bbox[2] - bbox[0]
        draw.text(((1920 - w) // 2, 550), subtitle, fill=COLOR_WHITE, font=font_sub)
    
    # 底部装饰
    draw.line([(200, 900), (1720, 900)], fill=COLOR_ORANGE, width=3)
    draw.line([(200, 905), (1720, 905)], fill=COLOR_GOLD, width=1)
    
    # 添加一些装饰元素（圆点）
    for i in range(10):
        x = 200 + i * 170
        draw.ellipse([x-5, 895, x+5, 905], fill=COLOR_GOLD)
    
    return ImageClip(np.array(img)).with_duration(duration)

def create_data_frame(title, data_items, duration=15):
    """创建数据展示帧"""
    bg = create_gradient_background()
    img = Image.fromarray(bg)
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 80)
        font_data = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 50)
    except:
        font_title = ImageFont.load_default()
        font_data = ImageFont.load_default()
    
    # 标题
    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w) // 2, 100), title, fill=COLOR_ORANGE, font=font_title)
    
    # 数据项（带图标）
    y = 280
    for item, value in data_items:
        # 数据条背景
        draw.rectangle([200, y, 1720, y + 100], fill=(30, 30, 60))
        
        # 数值（右侧）
        bbox = draw.textbbox((0, 0), value, font=font_data)
        draw.text((1600 - bbox[2], y + 25), value, fill=COLOR_GREEN if "+" in value else COLOR_WHITE, font=font_data)
        
        # 名称（左侧）
        draw.text((250, y + 25), item, fill=COLOR_WHITE, font=font_data)
        
        # 进度条
        bar_width = int((1500) * min(1.0, abs(float(value.replace("%", "").replace("+", ""))) / 300))
        bar_color = COLOR_GREEN if "+" in value else COLOR_WHITE
        draw.rectangle([250, y + 80, 250 + bar_width, y + 90], fill=bar_color)
        
        y += 130
    
    return ImageClip(np.array(img)).with_duration(duration)

def create_logic_frame(title, points, duration=20):
    """创建逻辑分析帧"""
    bg = create_gradient_background()
    img = Image.fromarray(bg)
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 70)
        font_point = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 45)
    except:
        font_title = ImageFont.load_default()
        font_point = ImageFont.load_default()
    
    # 标题
    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w) // 2, 80), title, fill=COLOR_GOLD, font=font_title)
    
    # 流程点（带箭头）
    y = 250
    for i, point in enumerate(points):
        # 编号圆圈
        draw.ellipse([180, y, 240, y + 60], outline=COLOR_ORANGE, width=3)
        draw.text((200, y + 10), str(i + 1), fill=COLOR_ORANGE, font=font_point)
        
        # 内容
        draw.text((280, y + 10), point, fill=COLOR_WHITE, font=font_point)
        
        # 箭头
        if i < len(points) - 1:
            draw.line([(210, y + 75), (210, y + 115)], fill=COLOR_GRAY, width=2)
            draw.polygon([(210, y + 120), (200, y + 110), (220, y + 110)], fill=COLOR_GRAY)
        
        y += 140
    
    return ImageClip(np.array(img)).with_duration(duration)

def create_ending_frame(duration=8):
    """创建结尾帧（带Logo和风险提示）"""
    bg = create_gradient_background()
    img = Image.fromarray(bg)
    draw = ImageDraw.Draw(img)
    
    try:
        font_brand = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 100)
        font_risk = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 50)
    except:
        font_brand = ImageFont.load_default()
        font_risk = Font.load_default()
    
    # 品牌名
    bbox = draw.textbbox((0, 0), "柚子暴风眼", font=font_brand)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w) // 2, 350), "柚子暴风眼", fill=COLOR_ORANGE, font=font_brand)
    
    # 副标题
    draw.text((700, 500), "专注硬核逻辑", fill=COLOR_WHITE, font=font_risk)
    
    # 风险提示
    bbox = draw.textbbox((0, 0), "市场有风险，投资需谨慎", font=font_risk)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w) // 2, 800), "市场有风险，投资需谨慎", fill=COLOR_GRAY, font=font_risk)
    
    # 底部装饰线
    draw.line([(200, 750), (1720, 750)], fill=COLOR_GOLD, width=2)
    
    return ImageClip(np.array(img)).with_duration(duration)

try:
    # 创建各个分镜
    print("Creating Title frame...")
    clip1 = create_title_frame("化工板块", "强势崛起", 5, COLOR_ORANGE)
    
    print("Creating Data frame...")
    clip2 = create_data_frame("化工品涨幅TOP5", [
        ("液氯", "+300%"),
        ("国际柴油", "+68%"),
        ("顺酐", "+56%"),
        ("国际汽油", "+48%"),
        ("燃料油", "+38%"),
    ], 15)
    
    print("Creating Logic frame...")
    clip3 = create_logic_frame("核心逻辑：油煤套利", [
        "中东冲突 → 油价上涨",
        "化工品成本 → 石油衍生",
        "中国多煤 → 成本稳定",
        "价差扩大 → 利润放大",
    ], 18)
    
    print("Creating Industry frame...")
    clip4 = create_data_frame("煤化工板块", [
        ("行业景气", "持续上行"),
        ("成本优势", "显著放大"),
        ("替代路径", "价值凸显"),
    ], 14)
    
    print("Creating Ending frame...")
    clip5 = create_ending_frame(8)
    
    # 串联所有分镜
    print("Concatenating clips...")
    video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])
    
    # 添加背景音乐（如果有）
    # 暂时跳过
    
    # 导出
    print(f"Exporting to: {OUTPUT_PATH}")
    video.write_videofile(
        OUTPUT_PATH,
        fps=30,
        codec='libx264',
        audio_codec='aac',
        bitrate='8000k',
        threads=4
    )
    
    print(f"\n=== SUCCESS ===")
    print(f"Video: {OUTPUT_PATH}")
    print(f"Duration: {video.duration}s")
    print(f"Resolution: 1920x1080")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
