############################################
# This is the handler for time limited event
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

        while cpt < self.rounds:
            print('{} [Info] 七音符 Round {} start!'.format(systime(), cpt+1))
            ## 起始點不正確
            if not self.img_compare('evt_nanatsu'):
                raise Exception
            
            self.tap('evt_onpu')
            time.sleep(2)
            self.tap('evt_lv55b')
            time.sleep(2)

            ## 食包
            if self.img_compare('hamburger'):
                self.eat_hamburger()
                continue

            ## 開始戰鬥                             
            time.sleep(5)
            if not self.img_compare('battle_ready'):
                raise Exception

            ## 戰鬥結束
            if self.battle_control(120, 10, 15):
                for i in range(2):
                    self.tap('battle_finish')
                    time.sleep(3)

                cpt += 1
                print('{} [Info] 七音符 Round {} completed'.format(systime(), cpt))
            else:
                raise Exception("戰鬥失敗") 
                        
            time.sleep(10)


        
