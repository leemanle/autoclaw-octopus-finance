"""把 CCTV视频复制到桌面"""
import shutil, glob, os

src_dir = r'C:\Users\Administrator\Desktop\CCTV下载'
dst = r'C:\Users\Administrator\Desktop\陈文清主持专题会议强调依法从严查处危害食品安全违法犯罪.mp4'

files = glob.glob(os.path.join(src_dir, '*.mp4'))
print(f'找到 {len(files)} 个 mp4')
for f in files:
    print(f'  {f}')

if files:
    src = files[0]
    shutil.copy2(src, dst)
    print(f'\n复制 {src} -> {dst}')
    print(f'目标大小: {os.path.getsize(dst)} bytes')