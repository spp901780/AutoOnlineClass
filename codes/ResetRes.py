
##########################
#已集成到主程序中，暂时废弃#
##########################

import subprocess
try:
    from win32 import win32api, win32gui, win32print
    import win32con                           
    import pywintypes
    import os
except ImportError:
    print('安装依赖库')
    subprocess.call(['pip','install','pywin32'])

cwd = os.path.abspath(os.path.dirname(__file__))

try:
    with open(cwd + r'\UserFile.txt', 'r') as userFile:
        fileInput = userFile.readlines()
        userWidth = int(fileInput[2])
        userHeight = int(fileInput[4])
        userScale = int(fileInput[6]) 
except Exception as e:
    print("无法处理配置文件，删除\"UserFile.txt\"后重试")
    print("读取的文件为:",fileInput)
    print("获取的异常为", e)
    quit()


userFile = open(cwd + r'\UserFile.txt', 'w')
userFile.writelines(['Resolution has been reset once.\n', 'Manually configuring your resolution and scale ratio if any problem.'])
#    userFile.writelines(['notOriginal','\n', str(userWidth),'\n',str(userHeight),'\n',str(userScale)])   
userFile.close()

#更改分辨率
devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = userWidth
devmode.PelsHeight = userHeight

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)

#更改缩放
win32api.ShellExecute(0, 'open', cwd+'\SetDpi.exe', ' '+str(userScale), '', 0)