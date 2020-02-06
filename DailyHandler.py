####################################
# Handling Daily quest of Langrisser 
# 日任列表︰
# 1. 經驗水  
# 2. 競技場
# 3. 友情抽
# 4. 練兵場
# (額外) 友情點
#
# 手打︰
# 1. 兄貴
# 2. 女神
# 3. 絆      
# 4. 事件關卡 
# 5. 三場時空
# 6. 附魔
# (額外) 合戰                     
#####################################
from GameHandler import GameHandler
from WatchDog import WatchDog

import time

class DailyHandler(GameHandler):
    def __init__(self, bundle):
        super().__init__(bundle)

    def run(self):
        self.exp_flask()
        time.sleep(3)
        self.friend_point()
        time.sleep(3)
        self.training_field()


    ## 英雄經驗
    def exp_flask(self):
        print("[Info] 食經驗水...")
        ## 起始點不正確
        if not self.img_compare('index_main'):
            raise Exception
        
        self.tap('index_hero')
        time.sleep(3)
        self.tap('exp_details')
        time.sleep(2)
        self.tap('exp_add')
        time.sleep(2)
        self.tap('exp_flask')
        time.sleep(2)
        self.tap('exp_confirm')
        time.sleep(2)
        for i in range(3):
            self.tap('return_btn')
            time.sleep(2)
    
    ## 競技場
    def arena(self):
        print("[Info] 競技場...")
        ## 起始點不正確
        if not self.img_compare('index_main'):
            raise Exception
         
        self.tap('index_arena')
        time.sleep(2)
        self.tap('arena_normal')
        time.sleep(3)

    ## 練兵場
    def training_field(self):
        print("[Info] 練兵場...")
        ## 起始點不正確
        if not self.img_compare('index_main'):
            raise Exception
        
        ## 入場
        self.tap('index_hikyou')
        time.sleep(3)
        self.tap('hikyou_training')
        
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
        self.tap('index_friend')
        time.sleep(3)
        self.tap('friend_give')
        time.sleep(2)
        self.tap('friend_get')
        time.sleep(2)
        self.tap('return_btn')