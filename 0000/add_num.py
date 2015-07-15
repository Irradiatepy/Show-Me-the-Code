# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


msyh  =  ImageFont.truetype ("msyh.ttf", 100)

avatar = Image.open(r"./avatar.jpg")
print avatar.size
draw = ImageDraw.Draw(avatar)

draw.text((360,0), "4", fill="red", font=msyh)

avatar.save("avatar2.jpg")


