#Every png is captured in the resolution of 2560x1440 and the windows scale of 125%.
#Any other display profile is not to be sure to work.

import pyautogui as pag
import cv2
import time
pag.PAUSE = 0   


def skipQuestion():
    optionsLocation = list(pag.locateAllOnScreen(r'.\awClass_v2png\Options.png', confidence=0.9))
    if not tempLocation is None:
        mouseMove(optionsLocation[0])
        submitLocation = pag.locateOnScreen(r'.\awClass_v2png\Submit.png', confidence=0.9)
        mouseMove(submitLocationn)
        for i in range(4):
            time.sleep(1)
            tempLocation = pag.locateOnScreen(r'.\awClass_v2png\NotCorrect.png', confidence=0.9)
            if not tempLocation is None:
                mouseMove(optionsLocation[1])
                mouseMove(submitLocation)
            else:
                break



def mouseMove(pngLocat):
    if not pngLocat is None:
        x1, y1 = pag.center(pngLocat)
        print(x1,' ',y1)
        pag.moveTo(x1, y1, 0.5, pag.easeInQuad)
        time.sleep(0.5)
        pag.click()


def findNextUnplay():
    locationX = []
    locationY = []
    for i in range(1, 8):
        filePath = r'.\awClass_v2png' + '\\' + str(i) + '.png'
        tempLocation = pag.locateOnScreen(filePath, confidence=0.9)
        if not tempLocation is None:
            x1, y1 = pag.center(tempLocation)
            locationX.append(x1)
            locationY.append(y1)
    if len(locationX) == 0:
        return False
    else:
        return [locationX[locationY.index(min(locationY))], min(locationY)]


width, height = pag.size()
classChoice = pag.confirm(text='"Which platform?', title='', buttons=['超星尔雅', 'zhi hui shu'])
if classChoice == '超星尔雅':
    choice = pag.confirm(text='Question after chapter?', title='', buttons=['Yes', 'No'])
    time.sleep(2)
    while (1):
        tempLocation = pag.locateOnScreen(r'.\awClass_v2png\Finished.png', confidence=0.9)
        if tempLocation is None:
        # 开始小节播放
            print("Play start")
            for i in range(10):
                time.sleep(1)
                tempLocation = pag.locateOnScreen(r'.\awClass_v2png\CentPlay.png', confidence=0.8)
                if not tempLocation is None:
                    mouseMove(tempLocation)
                    
                    # 确认出现播放控件
                    time.sleep(1)
                    tempLocation = None
                    while tempLocation is None:
                        pag.moveRel(0, -50, duration=0.2)
                        pag.moveRel(0, 50, duration=0.2)
                        time.sleep(1)
                        tempLocation = pag.locateOnScreen(r'.\awClass_v2png\Pause.png', confidence=0.9)
                        print(tempLocation)
                        if tempLocation is None:
                            pag.scroll(-height//10)
                            time.sleep(1)
                    print('found')

                    # 等待播放结束
                    replayNumBefore = len(list(pag.locateAllOnScreen(r'.\awClass_v2png\Replay.png', confidence=0.9)))
                    replayNumAfter = replayNumBefore
                    counter = 0
                    while replayNumBefore == replayNumAfter and counter<=240:
                        print('wait')
                        time.sleep(10)
                        replayNumAfter = len(list(pag.locateAllOnScreen(r'.\awClass_v2png\Replay.png', confidence=0.9)))
                        counter = counter + 1
                        tempLocation = pag.locateOnScreen(r'.\awClass_v2png\Submit.png', confidence=0.9)
                        if not tempLocation is None:
                            skipQuestion()

                    # 寻找下一视频
                    for j in range(5):
                        pag.scroll(-height//10)
                        time.sleep(1)
                        tempLocation = pag.locateOnScreen(r'.\awClass_v2png\CentPlay.png', confidence=0.8)
                        if not tempLocation is None:
                            pag.scroll(-height//10)
                            pag.moveRel(0, height//10, duration=0.2)
                            break
            pag.press('f5')
            time.sleep(4)
        print("Find next stage")
        #寻找下一小节
        if choice == 'No':
            #小节后无题目
            for i in range (6):
                tempReturn = findNextUnplay()
                if tempReturn != False:
                    pag.moveTo(tempReturn[0]-width//12, tempReturn[1], 0.5, pag.easeInQuad)
                    time.sleep(0.3)
                    pag.leftClick()
                    time.sleep(4)
                    break
                else:
                    pag.moveTo(width-width//20, height//2, 0.5, pag.easeInQuad)
                    pag.scroll(-height//3)
                    time.sleep(1)
        elif choice == 'Yes':
            #小节后有题目
            for i in range(6):
                tempLocation = pag.locateOnScreen(r'.\awClass_v2png\2.png', confidence=0.9)
                if not tempLocation is None:
                    x1, y1 = pag.center(tempLocation)
                    pag.moveTo(x1-width//12, y1, 0.5, pag.easeInQuad)
                    time.sleep(0.3)
                    pag.leftClick()
                    time.sleep(4)
                    break
                else:
                    pag.moveTo(width-width//20, height//2, 0.5, pag.easeInQuad)
                    pag.scroll(-height//3)
                    time.sleep(1)
else:
    
