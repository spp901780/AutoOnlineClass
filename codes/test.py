import easyocr
import cv2
import pyautogui as pag
import time
import numpy as np
def recognize_digits_with_coordinates_from_array(image_array):
    # 创建 easyocr Reader 对象
    reader = easyocr.Reader(['en'])  # 这里指定语言为英文

    # 读取并识别图像中的文本
    results = reader.readtext(image_array, gpu=True)

    # 过滤出数字及其坐标
    digits_with_coordinates = []
    for (bbox, text, prob) in results:
        if text.isdigit():
            digits_with_coordinates.append((text, bbox))

    return digits_with_coordinates

time.sleep(2)
screen = pag.screenshot()
screen_np = np.array(screen)
screen_cv2 = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
cv2.imshow('screen', screen_cv2)
recognized_digits =  recognize_digits_with_coordinates_from_array(screen_np[2000:2559, 200:1380])
for digit, bbox in recognized_digits:
    print(f"Recognized digit: {digit}, Coordinates: {bbox}")