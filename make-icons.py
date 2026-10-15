# Builds Android launcher icons from icon.png and replaces the default ones
import os, shutil
from PIL import Image, ImageDraw
res = 'android/app/src/main/res'
shutil.rmtree(res + '/mipmap-anydpi-v26', ignore_errors=True)  # use plain PNG icons
src = Image.open('icon.png').convert('RGBA')
for d, s in {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}.items():
    folder = f'{res}/mipmap-{d}'
    os.makedirs(folder, exist_ok=True)
    im = src.resize((s, s), Image.LANCZOS)
    im.save(f'{folder}/ic_launcher.png')
    im.save(f'{folder}/ic_launcher_foreground.png')
    mask = Image.new('L', (s * 4, s * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, s * 4 - 1, s * 4 - 1), fill=255)
    mask = mask.resize((s, s), Image.LANCZOS)
    r = im.copy(); r.putalpha(mask)
    r.save(f'{folder}/ic_launcher_round.png')
print('icons done')
