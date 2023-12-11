from win32 import win32api, win32gui, win32print
import win32con                           
import pywintypes
import os
cwd, temp=os.path.split(os.path.abspath(__file__))
userFile = open(cwd + r'\UserFile.txt', 'r')
fileInput = userFile.readlines()
userWidth = int(fileInput[0])
userHeight = int(fileInput[1])
userScale = int(fileInput[2])
userFile.close()

#更改分辨率
devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = userWidth
devmode.PelsHeight = userHeight

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)

#更改缩放
win32api.ShellExecute(0, 'open', cwd+'\SetDpi.exe', ' '+str(userScale), '', 0)