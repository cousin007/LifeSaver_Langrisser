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
        print("[Info] 練兵場...")
        ## 起始點不正確
        if not self.img_compare('index_main'):
            raise Exception
        
        ## 入場
        self.tap('hidden_area')
        time.sleep(2)
        self.tap('training_field')
        
        time.sleep(2)
        self.tap('level_top')

        ## 食包
        time.sleep(1)
        if self.img_compare('hamburger'):
            self.eat_hamburger()
            time.sleep(2)
            self.tap('level_top')
        
        ## 開始戰鬥
        time.sleep(5)
        if not self.img_compare('battle_ready'):
            raise Exception

        ## 戰鬥結束
        if self.battle_control(120, 5, 30):
            for i in range(3):
                self.tap('battle_finish')
                time.sleep(5)
        else:
            raise Exception("戰鬥失敗") 
        
        ## 返回大地圖
        for i in range(2):
            self.tap('return_btn')
            time.sleep(2)

    ## 友情抽
    def friend_draw(self):
        #TODO find exact column
        pass

    ## 友情點
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