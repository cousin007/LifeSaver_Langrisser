###################################################
# This is the parent class of all in-game handler #
# Providing common function interfaces            #
#                                                 #
###################################################
import time

class GameHandler():

    def __init__(self, bundle):
        # Working compartments
        self.img_map = bundle['img_map']
        self.tap_map = bundle['tap_map']
        self.adb = bundle['adb']
        self.iha = bundle['iha']

    def img_compare(self, img_target):
        return self.iha.img_compare(self.img_map[img_target], img_target)

    def tap(self,tap_target):
        self.adb.tap(self.tap_map[tap_target])
    
    def screencap(self, img_name, tgt_dir):
        self.adb.screencap(img_name + '.png', tgt_dir)

    def eat_hamburger(self):
        self.tap('hambuger')
        time.sleep(2)
        self.tap('level_top') #white space

    def check_auto(self):
        loop = 5
        loop_wait = 3
        check_count = 0
        while check_count < loop:
            if self.img_compare('battle_auto'):
                return True
            else:
                self.tap('auto_btn')
                check_count += 1
                time.sleep(loop_wait)
        return False

    def battle_control(self, init_wait, loop, loop_wait):
        self.tap('battle_start') 
        time.sleep(1)

        if not self.check_auto():
            raise Exception("自動戰鬥檢測失敗")

        time.sleep(init_wait)
        check_count = 0
        while check_count < loop:
            if self.img_compare('battle_finish'):
                return True
            else:
                check_count += 1
                time.sleep(loop_wait)
        return False
