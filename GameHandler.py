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
    
    ## check the game status based on the screen
    # @param img_target: the target name of image, must be match to the file name 
    #                    in sample folder
    #        offset_x: the picture's horizontal offset  
    #        offset_y: the picture's vertical offset
    # 
    # @return: True if the image is nearly same
    def img_compare(self, img_target, offset_x=None, offset_y=None):
        coords = self.img_map[img_target]
        if offset_x:
            coords[0] += offset_x
            coords[2] += offset_x

        if offset_y:
            coords[1] += offset_y
            coords[3] += offset_y

        return self.iha.img_compare(tuple(coords), img_target)

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

    def battle_control(self, init_wait, loop, loop_wait, pvp=False):
        self.tap('battle_start') 
        time.sleep(1)

        # Need auto battle
        if not pvp:
            if not self.check_auto():
                raise Exception("自動戰鬥檢測失敗")

        time.sleep(init_wait)
        check_count = 0
        while check_count < loop:
            # distinguish pvp and pve
            finish = pvp if self.img_compare('battle_finish',offset_y=-25) else self.img_compare('battle_finish')

            if finish:
                return True
            else:
                check_count += 1
                time.sleep(loop_wait)
        return False
