###################################################
# This is the parent class of all in-game handler #
# Providing common function interfaces            #
#                                                 #
###################################################

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