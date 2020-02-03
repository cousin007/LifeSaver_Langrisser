#######################################
# Handling Daily quest of Langrisser #
#                                     #
#######################################
from GameHandler import GameHandler
from WatchDog import WatchDog

import time

class DailyHandler(GameHandler):
    def __init__(self, bundle):
        super().__init__(bundle)

    ##TODO 
    # 英雄經驗
    # 時空3場
    
    # 競技場

    ## 練兵場
    def training_field(self):
        if not self.img_compare('index_main'):
            raise Exception

        print("[Info] 練兵場...")
        self.tap('hidden_area')
        time.sleep(2)
        self.tap('training_field')
        time.sleep(2)
        self.tap('level_top')

        ## 唔夠體，食包
        time.sleep(1)
        if self.img_compare('hamburger'):
            self.eat_hamburger()
            continue

        time.sleep(5)
        if not self.img_compare('battle_ready'):
            raise Exception

    ##友情抽
    def friend_draw(self):
        #TODO 
        pass

    ##友情點
    def friend_point(self):
        if not self.img_compare('index_main'):
            raise Exception
        
        print('[Info] 收發友情點...')
        self.tap('friend_page')
        time.sleep(3)
        self.tap('friend_give')
        time.sleep(2)
        self.tap('friend_get')
        time.sleep(2)
        self.tap('return_btn')