from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('NameList.csv')
font = ImageFont.truetype('DancingScript-Bold.ttf',120)
color = 'rgba(0,48,60,255)'
for index,j in df.iterrows():
    img = Image.open('Certificate.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(114,761),text='{}'.format(j['Names']),fill=color,font=font)
    img.save('Certificates/{}.png'.format(j['Names']))