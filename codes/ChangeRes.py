import subprocess
try:
    from win32 import win32api, win32gui, win32print
    import win32con                           
    import pywintypes
    import os
except ImportError:
    print('安装依赖库')
    subprocess.call(['pip','install','pywin32'])

cwd, temp=os.path.split(os.path.abspath(__file__))
#获取用户分辨率和缩放

sX = win32api.GetSystemMetrics(0)   #获得屏幕分辨率X轴
sY = win32api.GetSystemMetrics(1)   #获得屏幕分辨率Y轴
#获取缩放前分辨率
hDC = win32gui.GetDC(0)
userWidth = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)  # 横向分辨率
userHeight = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)  # 纵向分辨率
print(userHeight, sY)
userScale = int(100 * round( userHeight/ sY, 2))

#保存用户设置

userFile = open(cwd + r'\UserFile.txt', 'r')

#检测配置状态，保存的不是用户初始分辨率的情况下保存显示设置
if(userFile.readline() != 'UserConfig\n'):
    userFile = open(cwd + r'\UserFile.txt', 'w')
    #保存原始显示设置
    userFile.writelines(['UserConfig','\nWidth = \n', str(userWidth),'\nHeight = \n',str(userHeight),'\nScale = \n',str(userScale)])
    print("Write")
userFile.close()

#更改分辨率
devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = 2560
devmode.PelsHeight = 1440

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)

#更改缩放
win32api.ShellExecute(0, 'open', cwd+'\SetDpi.exe', ' 125', '', 0)