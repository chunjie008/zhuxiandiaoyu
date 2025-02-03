# -- coding: utf-8 --
from PIL import Image

# 打开图片
image1 = Image.open('11.png')
image2 = Image.open('22.png')
image4 = Image.open('44.png')

# 获取图片的尺寸
width1, height1 = image1.size
width2, height2 = image2.size
width4, height4 = image4.size


print(f"1图片宽度: {width1} 像素")
print(f"1图片高度: {height1} 像素")

print(f"2图片宽度: {width2} 像素")
print(f"2图片高度: {height2} 像素")

print(f"4图片宽度: {width4} 像素")
print(f"4图片高度: {height4} 像素")