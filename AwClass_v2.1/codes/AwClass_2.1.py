#Every png is captured in the resolution of 2560x1440 and the windows scale of 125%.
#Any other display profile is not to be sure to work.
import pyautogui as pag
import cv2
import time
import os

cwd = os.path.abspath(os.path.dirname(__file__))
pngsLocation = os.path.abspath(os.path.join(cwd, os.path.pardir)) + r'\AwClass_v2png'
pag.PAUSE = 0   

def cx_skipQuestion():
    optionsLocation = list(pag.locateAllOnScreen(pngsLocation + r'\Options.png', confidence=0.9))
    if not tempLocation is None:
        mouseMove(optionsLocation[0])
        submitLocation = pag.locateOnScreen(pngsLocation + r'\Submit.png', confidence=0.9)
        mouseMove(submitLocation)
        for i in range(4):
            time.sleep(1)
            tempLocation = pag.locateOnScreen(pngsLocation + r'\NotCorrect.png', confidence=0.9)
            if not tempLocation is None:
                mouseMove(optionsLocation[1])
                mouseMove(submitLocation)
            else:
                break

def cx_findNextUnplay():
    locationX = []
    locationY = []
    for i in range(1, 8):
        filePath = pngsLocation + r'' + '\\' + str(i) + '.png'
        tempLocation = pag.locateOnScreen(filePath, confidence=0.9)
        if not tempLocation is None:
            x1, y1 = pag.center(tempLocation)
            locationX.append(x1)
            locationY.append(y1)
    if len(locationX) == 0:
        return False
    else:
        return [locationX[locationY.index(min(locationY))], min(locationY)]

def zh_skipQuesion():
    tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_optionA.png', confidence=0.9)
    if not tempLocation is None:
        mouseMove(tempLocation)
    else:
        tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_optionB.png', confidence=0.9)
        mouseMove(tempLocation)
    tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_closeQuestion.png', confidence=0.9)
    if not tempLocation is None:
        mouseMove(tempLocation)

def mouseMove(pngLocat):
    if not pngLocat is None:
        x1, y1 = pag.center(pngLocat)
        print(x1,' ',y1)
        pag.moveTo(x1, y1, 0.5, pag.easeInQuad)
        time.sleep(0.5)
        pag.click()


width, height = pag.size()
classChoice = pag.confirm(text='"Which platform?', title='', buttons=['超星尔雅', '智慧树'])
#超星尔雅平台
if classChoice == '超星尔雅':
    choice = pag.confirm(text='Question after chapter?', title='', buttons=['Yes', 'No'])
    time.sleep(2)
    while (1):
        tempLocation = pag.locateOnScreen(pngsLocation + r'\Finished.png', confidence=0.9)
        if tempLocation is None:
        # 开始小节播放
            print("Play start")
            for i in range(10):
                time.sleep(1)
                tempLocation = pag.locateOnScreen(pngsLocation + r'\CentPlay.png', confidence=0.8)
                if not tempLocation is None:
                    mouseMove(tempLocation)
                    
                    # 确认出现播放控件
                    time.sleep(1)
                    tempLocation = None
                    while tempLocation is None:
                        pag.moveRel(0, -50, duration=0.2)
                        pag.moveRel(0, 50, duration=0.2)
                        time.sleep(1)
                        tempLocation = pag.locateOnScreen(pngsLocation + r'\Pause.png', confidence=0.9)
                        print(tempLocation)
                        if tempLocation is None:
                            pag.scroll(-height//10)
                            time.sleep(1)
                    print('found')

                    # 等待播放结束
                    replayNumBefore = len(list(pag.locateAllOnScreen(pngsLocation + r'\Replay.png', confidence=0.9)))
                    replayNumAfter = replayNumBefore
                    counter = 0
                    while replayNumBefore == replayNumAfter and counter<=240:
                        print('wait')
                        time.sleep(10)
                        replayNumAfter = len(list(pag.locateAllOnScreen(pngsLocation + r'\Replay.png', confidence=0.9)))
                        counter = counter + 1
                        tempLocation = pag.locateOnScreen(pngsLocation + r'\Submit.png', confidence=0.9)
                        if not tempLocation is None:
                            cx_skipQuestion()

                    # 寻找下一视频
                    for j in range(5):
                        pag.scroll(-height//10)
                        time.sleep(1)
                        tempLocation = pag.locateOnScreen(pngsLocation + r'\CentPlay.png', confidence=0.8)
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
                tempReturn = cx_findNextUnplay()
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
                tempLocation = pag.locateOnScreen(pngsLocation + r'\2.png', confidence=0.9)
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

#智慧树平台
else:
    time.sleep(5)
    while(1):
        #开始播放
        pag.moveTo(900, 1000, 0.5, pag.easeInQuad)
        time.sleep(0.5)
        pag.click()
        #等待播放结束
        tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_finished.png', confidence=0.9)
        counter = 0
        while (counter<=360 and tempLocation is None):
            print("wait")
            time.sleep(10)
            #答题
            tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_question.png', confidence=0.9)
            if not tempLocation is None:
                zh_skipQuesion()
                time.sleep(1)
                pag.click()
            counter = counter+1
            tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_finished.png', confidence=0.9)

        #寻找下一节
        pag.moveTo(2200,900)
        pag.scroll(-50)
        time.sleep(1)        
        isFound = 0
        for i in range(10):
            allUnplay = pag.locateAllOnScreen(pngsLocation + r'\zh_unplay.png', confidence=0.9)
            for everyUnplay in allUnplay:
                listUnplay = list(everyUnplay)
                tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_played.png', region=(listUnplay[0]+250, listUnplay[1]-30, 60, 60), confidence=0.9)
                print(listUnplay[0]+250, listUnplay[1]-30)
                print(tempLocation)
                if tempLocation is None:
                    mouseMove(everyUnplay)
                    time.sleep(5)
                    isFound = 1
                    break
            if isFound == 0:
                pag.scroll(-height//4)
                time.sleep(1)
            else:
                break
