from win32 import win32api, win32gui, win32print
import win32con                           
import pywintypes
import os
cwd, temp=os.path.split(os.path.abspath(__file__))
#获取用户分辨率和缩放
sX = win32api.GetSystemMetrics(0)   #获得屏幕分辨率X轴
sY = win32api.GetSystemMetrics(1)   #获得屏幕分辨率Y轴
#获取缩放前分辨率
hDC = win32gui.GetDC(0)
userWidth = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)  # 横向分辨率
userHeight = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)  # 纵向分辨率
userScale = int(100 * round( userHeight/ sY, 2))

#保存用户设置
userFile = open(cwd + r'\UserFile.txt', 'w')
userFile.writelines([str(userWidth),'\n',str(userHeight),'\n',str(userScale)])
userFile.close()

#更改分辨率
devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = 2560
devmode.PelsHeight = 1440

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)

#更改缩放
win32api.ShellExecute(0, 'open', cwd+'\SetDpi.exe', ' 125', '', 0)