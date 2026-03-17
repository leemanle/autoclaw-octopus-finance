"""
Simple professional video with data visualization
"""

from moviepy import *
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUTPUT_PATH = r"C:\Users\Administrator\Desktop\化工板块分析_V3_抖音_1080P.mp4"

COLOR_BG = (10, 10, 30)
COLOR_ORANGE = (255, 140, 0)
COLOR_GOLD = (255, 215, 0)
COLOR_GREEN = (46, 200, 100)
COLOR_WHITE = (255, 255, 255)

print("Creating professional video...")

def make_frame(t):
    img = Image.new('RGB', (1920, 1080), color=COLOR_BG)
    draw = ImageDraw.Draw(img)
    
    # Dynamic title
    title = "化工板块"
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 120)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), title, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w)//2, 400), title, fill=COLOR_ORANGE, font=font)
    
    subtitle = "强势崛起"
    bbox = draw.textbbox((0, 0), subtitle, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((1920 - w)//2, 550), subtitle, fill=COLOR_WHITE, font=font)
    
    return np.array(img)

try:
    # Use VideoClip to create custom animation
    clip = VideoClip(make_frame, duration=5)
    
    print(f"Exporting: {OUTPUT_PATH}")
    clip.write_videofile(OUTPUT_PATH, fps=30, codec='libx264')
    
    print(f"SUCCESS: {OUTPUT_PATH}")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
