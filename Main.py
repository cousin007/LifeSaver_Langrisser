from AnikiHandler import AnikiHandler
from DragonHandler import DragonHandler
from DailyHandler import DailyHandler
from lib.Adb import Adb
from lib.ImgHashAdaptor import ImgHashAdaptor

import sys
import json
import traceback

class Main():

    def __init__(self):
        ## Initial Phrase
        try:
            self.load_config()
            self.load_adb()
            print("[Initial] Completed!")
        except Exception:
            traceback.print_exc(file=sys.stdout)
            print("[Error] Initial Fail!")
            sys.exit()

        ## Get User input
        self.user_input = {}
        # self.get_param()

        self.iha = ImgHashAdaptor(self.adb)
        self.bundle = {
            'tap_map': self.tap_map,
            'img_map': self.img_map,
            'adb': self.adb,
            'iha': self.iha,
            'user_input': self.user_input
        }

        # DH = DragonHandler(self.bundle)
        # DH.run()

        daily = DailyHandler(self.bundle)
        # daily.friend_point()
        daily.training_field()

    # Locate the active emulators on the PC
    # Auto create the adb interface if only one is found
    def load_adb(self):
        print("[Initial] Loading ADB interface...")
        devices = Adb.check_devices() #call Adb static method to return a list
        # if no emulator is found
        if len(devices) < 1:
            print('[Error] No Device Found!')
            raise Exception
        # if more than one emulators are found
        elif len(devices) > 1:
            print('[Info] multiple devices') #TODO: Handle This!
        # only one, create ADB object
        else:
            self.adb = Adb(devices[0])
            print("[Initial] {} connection established!".format(devices[0]))
        
    # Loading all necessary configuration files
    # including the coordinates of tap and screen capture
    def load_config(self):
        print("[Initial] Loading Configuration Files...")
        # Load map from json format and change to tuple type
        with open('./config/tap_map.json','r') as f:
            self.tap_map = json.load(f)
            for key,val in self.tap_map.items():
                self.tap_map[key] = tuple(val)
            print("[Initial] Tap Map... [OK]")

        with open('./config/img_map.json','r') as f:
            self.img_map = json.load(f)
            for key,val in self.img_map.items():
                self.img_map[key] = tuple(val)
            print("[Initial] Image Map... [OK]")

    def get_param(self):
        print('勇者啊! 請聆聽聖劍的召喚...\n啊!請先讓我把話說完\n好吧...這是免費的，這樣好不?')
        print('女神testing')
        
        self.user_input['rounds'] = int(input('rounds: '))


Main()
input('Press any key to exit...')

# branch = None
# level = None
# rounds = None

# print('---------------------\nWelcome to LifeSaver!\n---------------------')
# print('Select the branch:')
# print('1. Swordman')
# print('2. Archer')
# print('3. Piker')
# print('4. Airborne')
# print('5. Knight')
# print('6. Monk')
# branch = input('branch: ')

# print('Select the level:')
# print('1. 30lv')
# print('2. 35lv')
# print('3. 55lv')
# print('4. 60lv')
# print('5. 65lv')
# level = input('level: ')

# print('How many rounds? (Max: 99)')
# rounds = input('rounds: ')

# if branch is not None and level is not None and rounds is not None:
#     try:
#         # check branch valid
#         branch = int(branch)
#         if branch > 6 or branch < 1:
#             raise Exception

#         #check level valid
#         level = int(level)
#         if level > 5 or level < 1:
#             raise Exception
        
#         #check rounds valid
#         rounds = int(rounds)
#         if rounds > 99 or rounds < 1:
#             raise Exception

#     except:
#         print('Invalid input, program terminated!')
#         sys.exit()
    
#     print('Program initializing...')
#     ah = AnikiHandler(branch, level, rounds)
#     ah.main()
#     print('Program Exit!')

