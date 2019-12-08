import subprocess
import time
import random

class Adb():
    def __init__(self,deviceName):
        ADB_PATH = 'Tools/adb.exe' #The path of adb.exe
        self.device = [ADB_PATH,'-s',deviceName] # The adb command header ex."adb -s emulator-5555 "

    # The caller of adb
    def adb_call(self,args,shell=True):
        if shell:
            cmd = self.device + ['shell'] + args # stick header and action
        else:
            cmd = self.device + args
        # print(cmd) # debug
        subprocess.Popen(cmd)

    # Tap action
    def tap(self, x1=None, y1=None, x2=None, y2=None, point=None):
        x = None 
        y = None

        if point is None:
            if x2 is None and y2 is None: # exact point
                x = str(x1)
                y = str(y1)
            else: # rand tap within a range
                x = str(random.randint(x1,x2))
                y = str(random.randint(y1,y2))
        else: # Param is a tuple
            x = str(point[0])
            y = str(point[1])

        self.adb_call(['input','tap',x,y])

    # Swipe action
    def swipe(self, x1, y1, x2, y2):
        x1 = str(x1)
        y1 = str(y1)
        x2 = str(x2)
        y2 = str(y2)
        self.adb_call(['input', 'swipe', x1 ,y1, x2, y2])
    

    # Cap and pull image
    def screencap(self, fileName, pc_path=None):
        self.adb_call(['screencap','-p','/sdcard/' + fileName])
        time.sleep(1)
        if pc_path is None:
            self.adb_call(['pull','/sdcard/' + fileName], shell=False)
        else:
            self.adb_call(['pull','/sdcard/' + fileName, pc_path + fileName], shell=False)

if __name__ == "__main__":
    a = Adb('127.0.0.1:62001')
    a.screencap('hamburger.png')