from typing import KeysView


def belt_count(dictionary):
    belts = list(dictionary.values())
    
    for belt in belts:
        num = belts.count(belt)
        print(f'There are {num}{belt} belts')
        
ninja_belts = {}
 
while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter a belt colour:')
    ninja_belts[ninja_name] =ninja_belt
    
    another = input('add another? (Y/N)')
    if another == 'y':
        continue
    else:
        break
    
    ninja_intro(ninja_belts)