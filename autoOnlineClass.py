import pyautogui
import time
pyautogui.PAUSE = 0.1
def mouseMove(pngLocat):
        time.sleep(1)  
        if not pngLocat is None : 
            x1,y1 = pyautogui.center(pngLocat)
        else:
            print(pngLocat)
            print("retry")
            return                                                               
        pyautogui.moveTo(x1,y1,0.5,pyautogui.easeInQuad)
        time.sleep(0.5)
        pyautogui.click()  

while (1):
    if not pyautogui.locateOnScreen(r'.\png\finished.png',confidence=0.9) is None:
        print("1")
        pyautogui.scroll(-2000)
        mouseMove(pyautogui.locateOnScreen(r'.\png\nextPage.png',confidence=0.9))   
        time.sleep(5)
    else:
        if not pyautogui.locateOnScreen(r'.\png\1.png',confidence=0.9) is None :
            print("2")
            pyautogui.scroll(-2000)
            mouseMove(pyautogui.locateOnScreen(r'.\png\nextPage.png',confidence=0.9))
            time.sleep(5)
            mouseMove(pyautogui.locateOnScreen(r'.\png\play.png',confidence=0.9))
        else:
            if not pyautogui.locateOnScreen(r'.\png\2.png',confidence=0.9) is None :
                print("3")
                pyautogui.scroll(-2000)
                mouseMove(pyautogui.locateOnScreen(r'.\png\nextPage.png',confidence=0.9))
                time.sleep(3)
                mouseMove(pyautogui.locateOnScreen(r'.\png\3.png',confidence=0.9))
                time.sleep(5)
                mouseMove(pyautogui.locateOnScreen(r'.\png\play.png',confidence=0.9))
            else:
                if not pyautogui.locateOnScreen(r'.\png\3.png',confidence=0.9) is None :
                    print('4')
                    mouseMove(pyautogui.locateOnScreen(r'.\png\nextPage.png',confidence=0.9))
                    time.sleep(5)
                else:
                    if not pyautogui.locateOnScreen(r'.\png\play.png',confidence=0.9) is None : 
                        print('5')  
                        mouseMove(pyautogui.locateOnScreen(r'.\png\play.png',confidence=0.9))
                    else:                     
                        if not pyautogui.locateOnScreen(r'.\png\unfinished.png',confidence=0.9) is None :
                            print("Playing")
                            time.sleep(10)
                        else:
                            print('6')
                            mouseMove(pyautogui.locateOnScreen(r'.\png\nextPage.png',confidence=0.9))   
                            time.sleep(5)