from AnikiHandler import AnikiHandler
import sys

branch = None
level = None
rounds = None

print('---------------------\nWelcome to LifeSaver!\n---------------------')
print('Select the branch:')
print('1. Swordman')
print('2. Archer')
print('3. Piker')
print('4. Airborne')
print('5. Knight')
print('6. Monk')
branch = input('branch: ')

print('Select the level:')
print('1. 30lv')
print('2. 35lv')
print('3. 55lv')
print('4. 60lv')
print('5. 65lv')
level = input('level: ')

print('How many rounds? (Max: 99)')
rounds = input('rounds: ')

if branch is not None and level is not None and rounds is not None:
    try:
        # check branch valid
        branch = int(branch)
        if branch > 6 or branch < 1:
            raise Exception

        #check level valid
        level = int(level)
        if level > 5 or level < 1:
            raise Exception
        
        #check rounds valid
        rounds = int(rounds)
        if rounds > 99 or rounds < 1:
            raise Exception

    except:
        print('Invalid input, program terminated!')
        sys.exit()
    
    print('Program initializing...')
    ah = AnikiHandler(branch, level, rounds)
    ah.main()
    print('Program Exit!')

