from lib.Adb import Adb
from PIL import Image
from lib.ImgHashAdaptor import hashExtractor
import imagehash
import json
import time
import sys

class EventHandler():
    IMG_BOX = {'invite': (214,212,276,273),
                'ready': (1160,650,1249,693),
                'auto': (1200,240,1260,275),
                'finish': (510,155,759,203)
                }

    def __init__(self, rounds):
        self.adb = Adb('127.0.0.1:30054')
        self.sample_hash = hashExtractor('.\\sample').process()
        
        self.rounds = rounds
    
    #
    # Image compare function
    # @param tgt: target of the checking components
    #        imgName: the livetime captured image file name
    #
    # @reuturn True: image have high simularity
    #          False: image are totally different 
    #
    def img_compare(self, tgt, imgName='checking.png'):
        self.adb.screencap(imgName) #call Adb capture screen
        time.sleep(1) #wait for the image save
        
        img = Image.open(imgName) #open image
        area_grey = img.crop(EventHandler.IMG_BOX[tgt]).convert('L')
        
        dhash = imagehash.dhash(area_grey)
        print('diff mark: ' + str(dhash - self.sample_hash[tgt])) # debug
        return dhash - self.sample_hash[tgt] < 10 if True else False #return comparing result
    
    #
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
    def main(self):
        systime = lambda : time.strftime('[%H:%M:%S]', time.localtime())

        for complete in range(self.rounds):
            print('{} {} rounds start'.format(systime(), complete+1))
            
            if self.wait_event('invite',6,10): #60sec for invite
                self.adb.tap(240,240)
                time.sleep(10)
                
                if self.wait_event('ready',4,15): #60sec for ready
                    self.adb.tap(1205,647)
                    time.sleep(10)

                    if self.wait_event('auto',20,3): #60sec for auto
                        self.adb.tap(1229,256)
                        time.sleep(120)

                        if self.wait_event('finish',20,30): #10min for finish
                            for i in range(3):
                                self.adb.tap(1186,669)
                                time.sleep(3)

            print('{} rounds finished\n ------------------------'.format(complete+1))

if __name__ == '__main__':
    eh = EventHandler(3)
    eh.main()