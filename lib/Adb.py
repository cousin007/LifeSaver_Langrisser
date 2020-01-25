import subprocess
import time
import random
import re

class Adb():
    ADB_PATH = 'Tools/adb' #The path of adb.exe

    # Check the active emulator on PC
    # @return list of active emulators
    @staticmethod
    def check_devices():
        cmd = [Adb.ADB_PATH, 'devices']
        res = subprocess.run(cmd, capture_output=True, text=True).stdout
        return re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+',res)

    def __init__(self,deviceName):
        self.device = [Adb.ADB_PATH,'-s',deviceName] # The adb command header ex."adb -s emulator-5555 "

    # The caller of adb
    def adb_call(self,args,shell=True):
        if shell:
            cmd = self.device + ['shell'] + args # stick header and action
        else:
            cmd = self.device + args
        # print(cmd) # debug
        subprocess.Popen(cmd)

    # Tap action
    # @param: point: two coordinate 
    #         range: four coordinate, use to choose random point in range
    def tap(self, point=None, ranges=None):
        x = None 
        y = None

        if point is None:
            # rand tap within a range
            x = str(random.randint(ranges[0],ranges[2]))
            y = str(random.randint(ranges[1],ranges[3]))
        else: # tap exact point
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
    a.screencap('dev.png')