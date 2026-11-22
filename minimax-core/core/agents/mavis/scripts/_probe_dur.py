"""用 ffmpeg 子进程拿两个 mp4 的时长"""
import subprocess
files = [
    r'C:\Users\Administrator\Desktop\CCTV下载\[视频]陈文清主持召开专题会议强调 依法从严查处危害食品安全违法犯罪 守护好人民群众“舌尖上的安全”.mp4',
    r'C:\Users\Administrator\Desktop\CCTV下载\《新闻1+1》 20260922 网络食品安全：以案为鉴，防线怎么守？.mp4',
]
for f in files:
    p = subprocess.run([r'C:\Windows\System32\ffmpeg.exe', '-i', f], capture_output=True, text=True)
    out = p.stderr
    for line in out.splitlines():
        if 'Duration' in line:
            print(f)
            print('  ', line.strip())