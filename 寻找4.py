# -- coding: utf-8 --
import cv2
import numpy as np

# 读取主图像和模板图像
img = cv2.imread('4.png', cv2.IMREAD_COLOR)
template = cv2.imread('444.png', cv2.IMREAD_COLOR)

# 获取模板图像的宽度和高度
w, h = template.shape[1:]  # 修改这里

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 获取模板在主图像中的左上角坐标
top_left = max_loc

# 计算模板在主图像中的右下角坐标
bottom_right = (top_left[0] + w, top_left[1] + h)

print(f"模板在主图像中的左上角坐标: {top_left}")
print(f"模板在主图像中的右下角坐标: {bottom_right}")

