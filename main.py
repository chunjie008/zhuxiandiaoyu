# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#  pip install opencv-python
#  pip install pygetwindow.
#  pip install pyautogui
#  pip install --upgrade Pillow


import cv2
import pygetwindow as gw
import pyautogui
import time
import numpy as np  # 添加这一行

# 获取窗口
windows = gw.getWindowsWithTitle('ZhuxianClient')
if not windows:
    print("窗口未找到")
else:
    window = windows[0]

    # 确保窗口是激活的
    window.activate()

    # 获取窗口的位置和大小
    left, top, width, height = window.left, window.top, window.width, window.height

    # 捕获窗口内容
    while True:
        # 获取窗口截图
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot = np.array(screenshot)

        # 转换颜色通道顺序（从 BGR 到 RGB）
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

        # 生成文件名
        timestamp = int(time.time() * 1000)
        filename = f"img0/screenshot_{timestamp}.png"

        # 保存截图到当前目录
        cv2.imwrite(filename, screenshot)

        # 等待 500 毫秒
        time.sleep(0.3)

