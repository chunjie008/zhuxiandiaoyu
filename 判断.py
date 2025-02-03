# -- coding: utf-8 --
import cv2
import numpy as np

# 读取主图像和模板图像
img = cv2.imread('4.png', cv2.IMREAD_COLOR)
template = cv2.imread('444.png', cv2.IMREAD_COLOR)

# 获取模板图像的宽度和高度
w, h = template.shape[1:]

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 设置匹配阈值
threshold = 0.8

# 判断模板是否在主图像中
if max_val >= threshold:
    print("1.png 包含 11.png")
else:
    print("1.png 不包含 11.png")
