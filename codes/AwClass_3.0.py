#Every png is captured in the resolution of 2560x1440 and the windows scale of 125%.
#Any other display profile is not guaranteed to work.
#智慧树平台由于长宽比例缩放原因，仅在firefox中可用

import subprocess
try:
    import pyautogui as pag
    import cv2
    import time
    import tkinter as tk
    from os import path
    from win32 import win32api
    import win32con                           
    import pywintypes
except ImportError:
    print('安装依赖库')
    subprocess.call(['pip','install','pyautogui==0.9.54'])
    subprocess.call(['pip','install','opencv-python==4.9.0.80'])
    subprocess.call(['pip','install','pywin32==306'])
    subprocess.call(['pip','install','pypiwin32==223'])

    import pyautogui as pag
    import cv2
    import time
    import tkinter as tk
    from os import path
    from win32 import win32api
    import win32con                           
    import pywintypes

cwd = path.abspath(path.dirname(__file__))
pngsGroupLocation = path.abspath(path.join(cwd, path.pardir)) + r'\PngsGroup'
pag.PAUSE = 0   
pngsLocation = pngsGroupLocation + '1'
print(pngsLocation)


"""
以下为分辨率处理函数
"""

def resetResolution():
    try:
        with open(cwd + r'\UserFile.txt', 'r') as userFile:
            fileInput = userFile.readlines()
            userWidth = int(fileInput[2])
            userHeight = int(fileInput[4])
            userScale = int(fileInput[6]) 
    except:
        print("无法处理配置文件，删除\"UserFile.txt\"后重试")
        print("读取的文件为:",fileInput)
        quit()

    userFile = open(cwd + r'\UserFile.txt', 'w')
    userFile.writelines(['Resolution has been reset once. ', 'Manually configuring your resolution and scale ratio if there any problem.'])
    userFile.writelines(['\nWidth=\n', str(userWidth),'\nHeight=\n',str(userHeight),'\nScale=\n',str(userScale)])   
    userFile.close()

    #更改分辨率
    devmode = pywintypes.DEVMODEType()

    devmode.PelsWidth = userWidth
    devmode.PelsHeight = userHeight

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode, 0)

    #更改缩放
    win32api.ShellExecute(0, 'open', cwd+'\SetDpi.exe', ' '+str(userScale), '', 0)

def changeResolution():
    #运行调整分辨率的程序
    #由于PyautoGUI与获取Windows缩放的代码有冲突
    #会导致获取的缩放始终为100%
    #暂时使用另一程序实现
    subprocess.call(["python", cwd + r'\ChangeRes.py'])

"""
以下为通用的封装函数
"""

def qLocate(pngName:str, confidenceValve = 0.9):
    """
    重新封装的找图函数

    :param pngName: png格式的图片名称（不包含后缀名）
    :param confidenceValve: 找图的置信值，默认为0.9
    :return: PyAutoGUI定义的找图返回值，未找到则返回None
    """
    pathName = pngsLocation + '\\' + pngName + '.png'
    try:
        tempLocation = pag.locateOnScreen(pathName, confidence=confidenceValve)
    except pag.ImageNotFoundException:
        return None
    else:
        return tempLocation
    
def mouseMove(pngLocate, biasX=0, biasY=0):
    """
    封装的鼠标移动和点击函数，移动到图片加偏移的位置，等待500ms后点击

    :param pngLocate: PyAutoGUI定义的图片类型
    :param biasX: X轴方向上的坐标偏移
    :param biasY: Y轴方向上的坐标偏移
    """
    if not pngLocate is None:
        x1, y1 = pag.center(pngLocate)
        print(x1,' ',y1)
        pag.moveTo(x1 + biasX, y1+biasY, 0.3, pag.easeOutQuad)
        time.sleep(0.5)
        pag.click()



"""
以下为UI部分
"""

def exitProgram():
    #手动关闭窗口的回调函数
    #退出程序
    setupWindow.destroy()
    exit()

def displayOption():
    #选择超星尔雅平台后的回调函数
    #显示第二项选项
    lb2.grid(column=0, row=3, sticky=tk.W)
    rad2_1.grid(column=0, row=4, sticky=tk.W)
    rad2_2.grid(column=1, row=4, sticky=tk.W)

def undisplayOption():
    #选择超星尔雅平台的回调函数
    #取消显示第二项选项
    lb2.grid_forget()
    rad2_1.grid_forget()
    rad2_2.grid_forget()

def closeSetupGui():
    #确定按钮的回调函数
    #关闭窗口
    setupWindow.quit()
    setupWindow.destroy()

def displaySetupGui():
    global setupWindow
    setupWindow = tk.Tk()
    setupWindow.title("设置窗口")
    setupWindow.geometry('500x200')
    
    #调整分辨率按钮
    btn1 = tk.Button(setupWindow, text='调整分辨率', command= changeResolution).grid(column=0, row=0)
    btn2 = tk.Button(setupWindow, text='恢复分辨率', command= resetResolution).grid(column=1, row=0)

    #注册第二个选项相关组件
    global lb2, rad2_1, rad2_2, isQuestion
    lb2 = tk.Label(setupWindow, text=' 2.选择小节后是否有题目')
    isQuestion = tk.IntVar()
    isQuestion.set(0)
    rad2_1 = tk.Radiobutton(setupWindow, width=20, text='有题目', variable= isQuestion, value=1)
    rad2_2 = tk.Radiobutton(setupWindow, text='无题目', variable= isQuestion, value=0)

    #注册第一个选项相关组件
    lb1 = tk.Label(setupWindow, text=' 1.选择平台')
    lb1.grid(column=0, row=1, sticky=tk.W)
    global classChoice
    classChoice = tk.StringVar()
    classChoice.set('智慧树')
    rad1_1 = tk.Radiobutton(setupWindow, width=20, text='超星尔雅', variable= classChoice, value='超星尔雅', command=displayOption)
    rad1_2 = tk.Radiobutton(setupWindow, text='智慧树(Experimental)', variable= classChoice, value='智慧树', command=undisplayOption)
    rad1_1.grid(column=0, row=2, sticky=tk.W)
    rad1_2.grid(column=1, row=2, sticky=tk.W)

    #注册确认按钮组件
    btn = tk.Button(setupWindow, text='确认', command=closeSetupGui)
    btn.grid(column=3, row=5)

    setupWindow.protocol("WM_DELETE_WINDOW", exitProgram)#注册手动关闭窗口回调函数
    setupWindow.mainloop()


"""
以下为超星尔雅的函数
"""

def cx_skipQuestion():
    try:
        optionsLocation = list(pag.locateAllOnScreen(pngsLocation + r'\Options.png', confidence=0.9))
        mouseMove(optionsLocation[0])
        submitLocation = qLocate('Submit')
        mouseMove(submitLocation)
        for i in range(1,4):
            time.sleep(1)
            tempLocation = qLocate('NotCorrect')
            if not tempLocation is None:
                mouseMove(optionsLocation[i])
                mouseMove(submitLocation)
            else:
                break
    except pag.ImageNotFoundException:
        return

def cx_playVideo():
    """
    播放视频，包含弹出题目处理
    """
    tempLocation = qLocate("cx_point",0.95)
    print("find point")
    print(tempLocation)
    mouseMove(tempLocation, 375, 355) #偏移了播放键相对于任务点的位置
    time.sleep(1)
    pag.move(0, -20, 0.5, pag.easeOutQuad)
    pag.move(0, 20, 0.5, pag.easeOutQuad)
    tempLocation = qLocate("Pause")
    if not tempLocation is None:
        try:
            print(pngsLocation + r'\Replay.png')
            tempLocation = pag.locateAllOnScreen(pngsLocation + r'\Replay.png',confidence=0.9)
            replayCountBefore = len(list(tempLocation))
        except:
            replayCountBefore = 0
        
        time.sleep(5)
        waitCount = 0
        while (1):
            tempLocation = qLocate("Submit")
            if not tempLocation is None:
                cx_skipQuestion()
            time.sleep(10)
            waitCount += 1
            print(waitCount)
            if(waitCount >=240):
                break
            try:
                tempLocation = pag.locateAllOnScreen(pngsLocation + r'\Replay.png',confidence=0.9)
                replayCountAfter = len(list(tempLocation))
            except:
                replayCountAfter = 0
            if(replayCountBefore != replayCountAfter):
                break

def cx_startChapter():
    """
    开始一个小节的播放
    """
    pag.moveTo(1750,730)
    searchCoumt = 0
    while (searchCoumt<=30):
        tempLocation = qLocate("cx_point",0.96)
        if not tempLocation is None:
            print("findpoint")
            print(tempLocation)
            x1, y1 = pag.center(tempLocation)
            while(y1>=700):
                pag.scroll(-80)
                time.sleep(0.1)
                try:
                    x1, y1 = pag.center(qLocate("cx_point",0.96))
                except:
                    None
            cx_playVideo()
            searchCoumt = 0
        else:
            pag.scroll(-200)
            time.sleep(0.1)
            searchCoumt += 1

def cx_locateNextChapter(isQuestion:bool):
    """
    判断处理小节后问题以及小节目录的滚动
    :param isQuestion: 用户选择的章节后是否有题目
    """
    pag.moveTo(2300,700)
    locateCount = 0
    while(locateCount<=15):
        if(isQuestion):
            tempLocate = cx_locateChapterPosition(2)
        else:
            tempLocate = cx_locateChapterPosition(1)
        if not tempLocate is None:
            pag.moveTo(tempLocate[0]-250, tempLocate[1])#200为点击位置相对剩余视频数标识
            time.sleep(0.5)
            pag.click()
            time.sleep(3)
            return
        else:
            pag.scroll(-50)
            time.sleep(0.3)
    pag.press("F5")


def cx_locateChapterPosition(startNum:int):
    """
    在一个固定界面寻找下一个小节的位置，依靠未播放的视频数判断。

    :param startNum: 搜索起始的剩余视频数
    :return: 最靠上的未完成的小节的位置，以列表形式返回。若没有找到任何符合条件的小节，返回None
    """
    locationX = []
    locationY = []
    for i in range(startNum, 8):
        filePath = ''+str(i)
        tempLocation = qLocate(filePath)
        if not tempLocation is None:
            x1, y1 = pag.center(tempLocation)
            locationX.append(x1)
            locationY.append(y1)
    if len(locationX) == 0:
        return None
    else:
        return [locationX[locationY.index(min(locationY))], min(locationY)]



"""
以下为智慧树平台函数
"""

def zh_skipQuesion():
    """
    跳过视频中间弹出的问题
    """
    tempLocation = qLocate('zh_optionA')
    if not tempLocation is None:
        mouseMove(tempLocation)
    else:
        tempLocation = qLocate('zh_optionB')
        mouseMove(tempLocation)
    tempLocation = qLocate('zh_closeQuestion')
    if not tempLocation is None:
        mouseMove(tempLocation)



"""
以下为主函数
"""

width, height = pag.size()

displaySetupGui()

time.sleep(5)
while (1):
    #超星尔雅平台
    if(classChoice.get() == '超星尔雅'):
        #开始播放小节
        cx_startChapter()
        #寻找下一小节
        print("Find next stage")
        cx_locateNextChapter(isQuestion.get())


    #智慧树平台
    else:
        time.sleep(5)
        tempLocation = qLocate('zh_caution')
        if not tempLocation is None:
            mouseMove('zh_skipCaution')
        while(1):
            #开始播放
            pag.moveTo(900, 1000, 0.5, pag.easeInQuad)
            time.sleep(0.5)
            pag.click()
            #等待播放结束
            pag.move(0, -15, 0.5, pag.easeInQuad)
            time.sleep(0.1)
            pag.move(0, 15, 0.5, pag.easeInQuad)
            tempLocation = qLocate('zh_finished')
            counter = 0
            while (counter<=360 and tempLocation is None):
                print("wait")
                time.sleep(7)               
                pag.moveTo(900, 1000, 0.5, pag.easeInQuad)
                pag.move(0, -15, 0.5, pag.easeInQuad)
                time.sleep(0.1)
                pag.move(0, 15, 0.5, pag.easeInQuad)
                #答题
                tempLocation = qLocate('zh_question')
                if not tempLocation is None:
                    zh_skipQuesion()
                    time.sleep(1)
                    pag.click()
                counter = counter+1
                tempLocation = qLocate('zh_finished')

            #寻找下一节
            pag.moveTo(2200,900)
            pag.scroll(-50)
            time.sleep(1)        
            isFound = False
            for i in range(10):
                try:
                    allUnplay = pag.locateAllOnScreen(pngsLocation + r'\zh_unplay.png', confidence=0.9)
                except:
                    allUnplay = None
                for everyUnplay in allUnplay:
                    listUnplay = list(everyUnplay)
                    try:
                        tempLocation = pag.locateOnScreen(pngsLocation + r'\zh_played.png', region=(listUnplay[0]+250, listUnplay[1]-30, 60, 60), confidence=0.9)
                    except:
                        tempLocation = None
                    print(listUnplay[0]+250, listUnplay[1]-30)
                    print(tempLocation)
                    if tempLocation is None:
                        mouseMove(everyUnplay)
                        time.sleep(5)
                        isFound = True
                        break
                if isFound == False:
                    pag.scroll(-height//3)
                    time.sleep(1)
                else:
                    break
