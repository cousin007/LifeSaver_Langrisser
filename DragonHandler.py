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
                self.tap('level_top') #出擊
                time.sleep(1)

                if self.img_compare('hamburger'):
                    self.eat_hamburger()
                    self.hamburger += 1
                    print('{} [Info] {} hamburgers ate!'.format(systime(), self.hamburger))
                    continue   
                             
                time.sleep(5)

                if not self.img_compare('battle_ready'):
                    raise Exception

                if self.battle_control(300, 10, 30):
                    self.tap('battle_finish')
                    time.sleep(2)
                    self.tap('battle_finish')
                    time.sleep(3)
                    self.screencap(str(complete), './result/') #結算圖
                    time.sleep(2)
                    self.tap('battle_finish')

                    complete += 1
                    print('{} [Info] 女神試練 Round {} completed'.format(systime(), complete))
                else:
                    raise Exception("戰鬥失敗") 
                           
                time.sleep(10)
            except:
                traceback.print_exc(file=sys.stdout)
                break

