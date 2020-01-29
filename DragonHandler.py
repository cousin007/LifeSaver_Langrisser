#######################################
# Handling dragon quest of Langrisser #
#                                     #
#######################################
from WatchDog import WatchDog
from GameHandler import GameHandler

import sys
import time
import threading
import traceback

class DragonHandler(GameHandler):
    
    def __init__(self, bundle):
        super().__init__(bundle)

        # Working compartments 
        self.DOG = WatchDog(bundle)

        self.rounds = bundle['user_input']['rounds']
        self.hamburger = 0

    #TODO:
    #       customize exception
    def run(self):
        systime = lambda : time.strftime('%H:%M', time.localtime())
        complete = 0

        while complete < self.rounds:
            try:
                if not self.img_compare('index_dragon'):
                    raise Exception
                
                print('{} [Info] 女神試練 Round {} start'.format(systime(), complete+1))
                self.tap('index_start') #出擊
                time.sleep(1)

                if self.img_compare('hamburger'):
                    self.tap('hambuger') #食漢堡
                    self.hamburger += 1
                    print('{} [Info] {} hamburgers ate!'.format(systime(), self.hamburger))
                    time.sleep(1)
                    self.tap('index_start') #white space
                    continue                
                time.sleep(5)

                if not self.img_compare('battle_ready'):
                    raise Exception

                self.tap('battle_start') #出擊(戰鬥)
                time.sleep(5)

                # start watch dog to check auto stage
                t = threading.Thread(target=self.DOG.monitorAuto)
                t.start()

                # monitor battle process
                time.sleep(300) # wait 5 mins
                check_rds = 10 # last 10 check rounds
                while check_rds > 0:
                    # battle is win
                    if self.img_compare('battle_finish'):
                        complete += 1 
                        for i in range(2):
                            self.tap('battle_finish') #寶箱
                            time.sleep(3)
                        self.screencap(str(complete), './result/') #結算圖
                        time.sleep(1)
                        self.tap('battle_finish') #離開
                        print('{} [Info] 女神試練 Round {} completed'.format(systime(), complete))
                        break
                    
                    check_rds -= 1
                    print('{} [Info] {} times checked, battle in progress'.format(systime(), 10-check_rds))
                    time.sleep(30)
                    
                time.sleep(10)

            except:
                print('Exception catch!')
                traceback.print_exc(file=sys.stdout)
                break

