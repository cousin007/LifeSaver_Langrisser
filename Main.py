from AnikiHandler import AnikiHandler
from DragonHandler import DragonHandler
from lib.Adb import Adb

import sys
import json
import traceback

class Main():

    def __init__(self):
        try:
            self.load_config()
            self.load_adb()
        except Exception:
            traceback.print_exc(file=sys.stdout)
            sys.exit()

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
        with open('./config/tap_map.json','r') as f:
            self.tap_map = json.load(f)
            print("[Initial] Tap Map... [OK]")
            # d = tuple(self.tap_map['start'])
            # print(d)
        with open('./config/img_map.json','r') as f:
            self.img_map = json.load(f)
            print("[Initial] Image Map... [OK]")

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

