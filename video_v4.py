"""
Professional 60s video with multiple sections
"""

from moviepy import *
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUTPUT = r"C:\Users\Administrator\Desktop\化工板块_V4_60s_1080P.mp4"

def create_frame(text, subtext="", duration=5, color=(255,140,0)):
    def frame(t):
        img = Image.new('RGB', (1920, 1080), (10, 10, 30))
        d = ImageDraw.Draw(img)
        try:
            f1 = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 100)
            f2 = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 50)
        except:
            f1 = ImageFont.load_default()
            f2 = ImageFont.load_default()
        
        # Title
        b = d.textbbox((0,0), text, font=f1)
        d.text(((1920-(b[2]-b[0]))//2, 350), text, fill=color, font=f1)
        
        # Subtitle  
        if subtext:
            b = d.textbbox((0,0), subtext, font=f2)
            d.text(((1920-(b[2]-b[0]))//2, 500), subtext, fill=(255,255,255), font=f2)
        
        # Bottom line
        d.line([(200,900),(1720,900)], fill=color, width=3)
        
        return np.array(img)
    return VideoClip(frame, duration=duration)

try:
    print("Creating frames...")
    c1 = create_frame("化工板块", "强势崛起", 5, (255,140,0))
    c2 = create_frame("液氯 +300%", "扩散指数60.39%", 10, (255,50,50))
    c3 = create_frame("油煤套利", "产业链机会", 15, (255,215,0))
    c4 = create_frame("煤化工", "景气度上行", 15, (46,200,100))
    c5 = create_frame("柚子暴风眼", "市场有风险，投资需谨慎", 15, (255,140,0))
    
    print("Concatenating...")
    v = concatenate_videoclips([c1,c2,c3,c4,c5])
    
    print(f"Exporting to {OUTPUT}")
    v.write_videofile(OUTPUT, fps=30, codec='libx264', audio_codec='aac', bitrate='8000k', threads=4)
    
    print(f"SUCCESS: {OUTPUT}")
    print(f"Duration: {v.duration}s")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
