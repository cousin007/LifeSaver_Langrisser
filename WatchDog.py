##########################################
# This is a watch dog program to monitor #
# 1. Auto in the battle                  #
#                                        #
##########################################
import time
from lib.Adb import Adb
from lib.ImgHashAdaptor import ImgHashAdaptor
from GameHandler import GameHandler

class WatchDog(GameHandler):

    def __init__(self,bundle):
        super().__init__(bundle)
        
    ####################################
    # Checking the auto status, try to #
    # click if not                     #
    ####################################
    def monitorAuto(self):
        isAuto = False
        count = 0

        while not isAuto and count < 3:
            isAuto = self.img_compare('battle_auto')
            if not isAuto:
                print('[Info]: WOWO! Auto is not ready!')
                self.tap('auto_btn')
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