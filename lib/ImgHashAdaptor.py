import imagehash
import os
import time
from PIL import Image

class ImgHashAdaptor():
    def __init__(self,adb,sample_path):
        self.adb = adb
        self.sample_path = sample_path # sample image folder path
        self.sample_hashes = self.load_sample_hashes() # store dhash associate with file names

    # record files under the target folder
    def lsdir(self):
        files = []
        for r,d,f in os.walk(self.sample_path):
            files += f 
        return files

    # open img from file list and get their hash
    def load_sample_hashes(self):
        sample_hashes = {}
        files = self.lsdir() 
        for f in files:
            file_path = '{}\\{}'.format(self.sample_path, f) # full path of file
            asso_key = f.split('.')[0] # use for dict key without file type

            img = Image.open(file_path)
            img_grey = img.convert('L') # convert to grayscale
            hash_sp = imagehash.dhash(img_grey) # get difference hash
            sample_hashes[asso_key] = hash_sp # store hash with asso key
        return sample_hashes

    # Image compare function
    # @param coordinates: the turple of coordinates in the image
    #        tgt: name of the sample
    #        imgName: the livetime captured image file name
    #
    # @reuturn True: image have high simularity
    #          False: image are totally different 
    def img_compare(self, coordinates, tgt, imgName='checking.png'):
        self.adb.screencap(imgName) #call Adb capture screen
        time.sleep(1) #wait for the image save
        
        img = Image.open(imgName) #open image
        area_grey = img.crop(coordinates).convert('L') 
        dhash = imagehash.dhash(area_grey)
        # print('diff mark: ' + str(dhash - self.sample_hashes[tgt])) # debug
        return dhash - self.sample_hashes[tgt] < 10 if True else False #return comparing result

if __name__ == "__main__":
    IHA = ImgHashAdaptor('.\\sample')
    print(IHA.sample_hashes)




