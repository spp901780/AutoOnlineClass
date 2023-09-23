import pyautogui as pag
import cv2
import time
pag.PAUSE = 0.1
while (1):
    temp1 = pag.locateOnScreen(r'.\png\finished.png',confidence=0.9)
    if not temp1 is None:
        pag.press('f5')
        print('1')
        time.sleep(2)
        temp1 = pag.locateOnScreen(r'.\png\1.png',confidence=0.9)
        if temp1 is None:
            pag.moveTo(2400,700,0.5,pag.easeInQuad)
            print('2')
            pag.scroll(-300)
            time.sleep(0.3)
            temp1 = pag.locateOnScreen(r'.\png\1.png',confidence=0.9)
        if not temp1 is None:
            x1,y1 = pag.center(temp1)
            pag.moveTo(x1-250,y1,0.5,pag.easeInQuad)
            time.sleep(0.3)
            pag.leftClick()
            time.sleep(1)
            print('3')
        else:
            break
        temp1 = pag.locateOnScreen(r'.\png\play_2.png',confidence=0.9)
        if not temp1 is None:
            x1,y1 = pag.center(temp1)
            pag.moveTo(x1,y1,0.5,pag.easeInQuad)     
            time.sleep(0.3)
            pag.leftClick()
            print('4')
        else:
            break
    elif not pag.locateOnScreen(r'.\png\tinyPlay.png',confidence=0.9) is None:
        x1,y1 = pag.center(pag.locateOnScreen(r'.\png\tinyPlay.png',confidence=0.9))
        pag.moveTo(x1,y1,0.5,pag.easeInQuad)     
        time.sleep(0.3)
        pag.leftClick()
        print('5')
    elif not pag.locateOnScreen(r'.\png\play_2.png',confidence=0.9) is None:
        x1,y1 = pag.center(pag.locateOnScreen(r'.\png\play_2.png',confidence=0.9))
        pag.moveTo(x1,y1,0.5,pag.easeInQuad)     
        time.sleep(0.3)
        pag.leftClick()
        print('5')
    else:
        time.sleep(10)
        print('6')