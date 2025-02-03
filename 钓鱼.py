import cv2
import pygetwindow as gw
import pyautogui
import time
import numpy as np
import random

# 获取窗口
windows = gw.getWindowsWithTitle('ZhuxianClient')
space = False;
if not windows:
    print("窗口未找到")
else:
    window = windows[0]

    # 确保窗口是激活的
    window.activate()

    # 获取窗口的位置和大小
    left, top, width, height = window.left, window.top, window.width, window.height

    # 读取模板图像
    templatepaogan = cv2.imread('paogan.png', cv2.IMREAD_COLOR)
    template_qigan = cv2.imread('qigan.png', cv2.IMREAD_COLOR)
    template_diaoyu = cv2.imread('diaoyu.png', cv2.IMREAD_COLOR)

    # 获取模板图像的宽度和高度
    wpaogan, hpaogan = templatepaogan.shape[1:]
    w_qigan, h_qigan = template_qigan.shape[1:]
    w_diaoyu, h_diaoyu = template_diaoyu.shape[1:]

    # 设置匹配阈值
    threshold = 0.9

    # 捕获窗口内容
    while True:
        # 获取窗口截图
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot = np.array(screenshot)

        # 转换颜色通道顺序（从 BGR 到 RGB）
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

        # 进行模板匹配

        res_diaoyu = cv2.matchTemplate(screenshot, template_diaoyu, cv2.TM_CCOEFF_NORMED)

        min_val_diaoyu, max_val_diaoyu, min_loc_diaoyu, max_loc_diaoyu = cv2.minMaxLoc(res_diaoyu)

        if max_val_diaoyu >= threshold and not space:
            pyautogui.keyDown('space')
            space = True
            print("钓鱼")

        if max_val_diaoyu < threshold and space:
            pyautogui.keyUp('space')
            space = False
            print("放鱼 ")

        if max_val_diaoyu < threshold and not space:
            res_paogan = cv2.matchTemplate(screenshot, templatepaogan, cv2.TM_CCOEFF_NORMED)
            res_qigan = cv2.matchTemplate(screenshot, template_qigan, cv2.TM_CCOEFF_NORMED)
            min_va_paogan, max_val_paogan, min_loc_paogan, max_loc_paogan = cv2.minMaxLoc(res_paogan)
            min_val_qigan, max_val_qigan, min_loc_qigan, max_loc_qigan = cv2.minMaxLoc(res_qigan)
            # 抛杆
            if max_val_paogan >= threshold:
                interval = random.uniform(0.01, 0.05)
                # 模拟按下空格键
                pyautogui.keyDown('space')
                # 设置按下和释放之间的间隔时间（例如 1 秒）
                pyautogui.sleep(interval)
                # 模拟释放空格键
                pyautogui.keyUp('space')
                print("找到抛杆模板，按下空格键")
                pyautogui.sleep(3)

            # 起杆
            if max_val_qigan >= threshold:
                interval = random.uniform(0.01, 0.05)
                # 模拟按下空格键
                pyautogui.keyDown('space')
                # 设置按下和释放之间的间隔时间（例如 1 秒）
                pyautogui.sleep(interval)
                # 模拟释放空格键
                pyautogui.keyUp('space')
                print("找到起杆子模板，按下空格键")

