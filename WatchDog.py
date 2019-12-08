##########################################
# This is a watch dog program to monitor #
# 1. Auto in the battle                  #
#                                        #
##########################################
import time
from lib.Adb import Adb
from lib.ImgHashAdaptor import ImgHashAdaptor

class WatchDog():

    def __init__(self, adb, iha):
        self.ADB = adb
        self.IHA = iha
        
    ####################################
    # Checking the auto status, try to #
    # click if not                     #
    ####################################
    def monitorAuto(self):
        isAuto = False
        count = 0

        while not isAuto and count < 3:
            isAuto = self.IHA.img_compare((18,20,167,60),'auto')
            if not isAuto:
                print('[Watch Dog]: WOWO! Auto is not ready!')
                self.ADB.tap(1229,256)
            else:
                print('[Watch Dog]: WOWO! Auto is ready now.')
                return True
            count += 1
            time.sleep(2)
        print('[Watch Dog]: Woo... Auto is not confirm.')
        return False

if __name__ == '__main__':
    adb = Adb('127.0.0.1:62001')
    iha = ImgHashAdaptor(adb,'.\\sample')
    wd = WatchDog(adb,iha)
    wd.monitorAuto()