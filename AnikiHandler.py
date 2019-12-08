from lib.Adb import Adb
from lib.ImgHashAdaptor import ImgHashAdaptor

from PIL import Image
import imagehash
import json
import time
import sys

class AnikiHandler():
    IMG_BOX = {'index': (1014,5,1262,59),
                'finish': (510,155,759,203)
                }

    branch_map = {'1': (279,144),
                    '2': (279,244),
                    '3': (279,344),
                    '4': (279,444),
                    '5': (279,544),
                    '6': (279,644)
                }
    
    level_map = {'1':(1061,552),
                    '2':(1061,683),
                    '3':(1061,266),
                    '4':(1061,452),
                    '5':(1061,626)
                }

    def __init__(self, branch, level, rounds):
        # Working compartments 
        self.ADB = Adb('127.0.0.1:62001')
        self.IHA = ImgHashAdaptor(self.ADB,'.\\sample')
            
        self.branch = branch
        self.level = level
        self.rounds = rounds

    def checkIndex(self):
        return self.picCheck(AnikiHandler.IMG_BOX['index'],'index')
        
    def check_battle_finish(self):
        return self.picCheck(AnikiHandler.IMG_BOX['finish'],'finish')

    def main(self):
        complete = 0 #complete battle counts
        systime = lambda : time.strftime('[%H:%M]', time.localtime())

        while complete < self.rounds:
            print('{} {} rounds start'.format(systime(), complete+1))

            # Correct page to start, else do nothing
            if self.checkIndex():
                self.adb.tap(point=branch_map[self.branch]) #branch
                time.sleep(1)
                
                if self.level >= 3:
                    for i in range(2):
                        self.adb.swipe(807,667,792,141) # swipe to bottom
                        time.sleep(1)
                else:
                    self.adb.swipe(800,125,800,600)
                time.sleep(2)
                
                self.adb.tap(point=level_map[self.level]) # level
                time.sleep(10)

                self.adb.tap(1206,646) # start battle
                time.sleep(180) #3 mins
                check = 0
                while check < 5:
                    if self.check_battle_finish():
                        break
                    check += 1
                    print('{} {} time(s) checked, battle in progress'.format(systime(), check))
                    time.sleep(60)
                
                # battle not end properly, program terminated
                if check == 5:
                    print('Exception: Battle end improperly!')
                    sys.exit()
                else:
                    for i in range(3):
                        self.adb.tap(1186,669) # result
                        time.sleep(4)

                complete += 1
                print('{} {} rounds completed'.format(systime(), complete))
                time.sleep(10)
                print('-----------------------------')
            
            else:
                print('Initial fail: Starting point not correct!')
                sys.exit()
