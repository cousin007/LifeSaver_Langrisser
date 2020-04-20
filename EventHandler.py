############################################
# This is the handler for time limited event
# dev log 20/4/20: 少女的旅途
#
############################################
from GameHandler import GameHandler

import sys
import time
import traceback

class EventHandler(GameHandler):

    def __init__(self, bundle):
        super().__init__(bundle)

        self.rounds = bundle['user_inp']['rounds']

    # deprecated!
    # Wait for invitation
    # @param loop: how many rounds you want to wait
    #        interval: how many seconds for one round
    #
    # @return True means event occured, False means no event in certain period
    #
    def wait_event(self, evt, loop, interval):
        # wait 10 times
        for count in range(loop):
            if self.img_compare(evt):
                print('{} received'.format(evt))
                return True
            
            print('{} times {} checked, still waiting...'.format(count+1, evt))
            time.sleep(interval)
        
        print('{} timeout'.format(evt))
        return False

    # main process for event handler
    # only call this function to start the special event process
    def run(self):
        systime = lambda : time.strftime('%H:%M', time.localtime())
        cpt = 0

        #禁中間，開選單
        self.tap("evt_center")
        time.sleep(2)
        self.tap('evt_lv55')
        time.sleep(2)

        ## 食包
        if self.img_compare('hamburger'):
            self.eat_hamburger()
            self.tap('evt_lv55')
            time.sleep(2)

        while cpt < self.rounds:
            print('{} [Info] 限時活動 Round {} start!'.format(systime(), cpt+1))
            
            ## 開始戰鬥                             
            time.sleep(5)
            if not self.img_compare('battle_ready'):
                raise Exception

            ## 戰鬥結束
            if self.battle_control(90, 8, 15):
                self.tap('battle_finish')
                time.sleep(2)
                cpt += 1
                print('{} [Info] 限時活動 Round {} completed'.format(systime(), cpt))

                ## 繼續
                if cpt < self.rounds:
                    self.tap('battle_con')
                else:
                    self.tap("battle_finish")
            else:
                raise Exception("戰鬥失敗") 
                        
            time.sleep(5)


        
