#######################################
# Handling dragon quest of Langrisser #
#                                     #
#######################################
from lib.Adb import Adb
from lib.ImgHashAdaptor import ImgHashAdaptor
from WatchDog import WatchDog

import sys
import time
import threading
import traceback

class DragonHandler():
    
    def __init__(self, rounds):
        # Working compartments 
        self.ADB = Adb('127.0.0.1:62001')
        self.IHA = ImgHashAdaptor(self.ADB,'.\\sample')
        self.DOG = WatchDog(self.ADB,self.IHA)

        self.rounds = rounds
        self.hamburger = 0

    #TODO: Add parent class
    #       contain function: check state, as same as EventHandler wait_event
    #       customize exception
    def run(self):
        systime = lambda : time.strftime('[%H:%M]', time.localtime())
        complete = 0

        while complete < self.rounds:
            try:
                if not self.IHA.img_compare((1000,15,1250,60),'index_dragon'):
                    raise Exception
                
                print('{} [Dragon Handler]: Round {} start!'.format(systime(), complete+1))
                self.ADB.tap(1100,620) #出擊
                time.sleep(1)

                if self.IHA.img_compare((470,430,545,475),'hamburger'):
                    self.ADB.tap(510,450) #食漢堡
                    self.hamburger += 1
                    print('{} [Dragon Handler]: {} hamburgers ate!'.format(systime(), self.hamburger))
                    time.sleep(1)
                    self.ADB.tap(1100,620)
                    continue                
                time.sleep(5)

                if not self.IHA.img_compare((1160,650,1249,693),'ready'):
                    raise Exception

                self.ADB.tap(1205,650) #出擊(戰鬥)
                time.sleep(5)

                # start watch dog to check auto stage
                t = threading.Thread(target=self.DOG.monitorAuto)
                t.start()

                # monitor battle process
                time.sleep(300) # wait 5 mins
                check_rds = 10 # last 10 check rounds
                while check_rds > 0:
                    # battle is win
                    if self.IHA.img_compare((510,155,760,205),'finish'):
                        complete += 1 
                        for i in range(2):
                            self.ADB.tap(1185,670) #寶箱
                            time.sleep(3)
                        self.ADB.screencap(str(complete) + '.png', './result/') #結算圖
                        time.sleep(1)
                        self.ADB.tap(1185,670) #離開
                        print('{} [Dragon Handler]: Round {} completed!'.format(systime(), complete))
                        break
                    
                    check_rds -= 1
                    print('{} [Dragon Handler]: {} times checked, battle in progress'.format(systime(), 10-check_rds))
                    time.sleep(30)
                    
                time.sleep(10)

            except:
                print('Exception catch!')
                traceback.print_exc(file=sys.stdout)
                break

if __name__ == '__main__':
    DH = DragonHandler(20)
    DH.run()
    input('Press any key to exit...')