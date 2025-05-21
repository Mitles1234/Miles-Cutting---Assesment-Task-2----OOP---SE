import os
import math
import story
import items
import variables
import json

#--- Displays the UI Screen for the User ---
def PrintMainUI(Room):
    os.system('cls')
    print(f'''

        {story.Title(Room)}

        {Map(Room)}
        {story.Story(Room)}

        +----------------==Stats==--------------+
        |   Health:  ♥️  \033[31m{StatBar(variables.Health, variables.Max_Health)} \033[0m {f'({variables.Health}/{variables.Max_Health})':<12}|
        |   Stamina: 🔋 \033[32m{StatBar(variables.Stamina, variables.Max_Stamina)} \033[0m {f'({variables.Stamina}/{variables.Max_Stamina})':<12}|
        |   Mana:    💠 \033[34m{StatBar(variables.Mana, variables.Max_Mana)} \033[0m {f'({variables.Mana}/{variables.Max_Mana})':<12}|
        +---------------------------------------+

        +----------------------------==Inventory==----------------------------+
        |   {'🪙  Gold':<12} -   {variables.Gold:<48} |
        |   {'Weapon':<12} -   {variables.Inventory['WeaponSlot'].name:<15} {'Chestplate':<12} -   {variables.Inventory['ChestplateSlot'].name:<15} |
        |   {'Helmet':<12} -   {variables.Inventory['HelmetSlot'].name:<15} {'Boots':<12} -   {variables.Inventory['BootSlot'].name:<15} |
        +---------------------------------------------------------------------+
        |   {variables.Inventory['OtherSlot1']['Item'].name:<18} -   {variables.Inventory['OtherSlot1']['Qty']:<9} {variables.Inventory['OtherSlot2']['Item'].name:<18} -   {variables.Inventory['OtherSlot2']['Qty']:<9} |
        |   {variables.Inventory['OtherSlot3']['Item'].name:<18} -   {variables.Inventory['OtherSlot3']['Qty']:<9} {variables.Inventory['OtherSlot4']['Item'].name:<18} -   {variables.Inventory['OtherSlot4']['Qty']:<9} |
        +---------------------------------------------------------------------+

    {MoveOptions(Room)}
    ''')
    
    InputHandling(Room)

def Map(Room):
    if Room == 'Forest1':
        return '''       
        +--------------------==Map==---------------------+-------------------------+
        |                                                |   ██ - You              |
        | ⬆                             🌲------⭐---+   |   🏠 - Village          |
        | N                            /              \\  |   ⭐ - Special Place    |
        |                /------------+-------🏠----- 🌲 |   ☠️  - Enemy            |
        |██ ----------- ☠️                                |   🌲 - Forest           |
        |                \\------------------ 🌲          |                         |
        |                                                |                         |
        +------------------------------------------------+-------------------------+
    '''
    
    elif Room == 'Enemy1':
        return '''       
        +--------------------==Map==---------------------+-------------------------+
        |                                                |   ██ - You              |
        | ⬆                             🌲------⭐---+   |   🏠 - Village          |
        | N                            /              \\  |   ⭐ - Special Place    |
        |                /------------+-------🏠----- 🌲 |   ☠️  - Enemy            |
        | 🌲----------- ██                               |   🌲 - Forest           |
        |                \\------------------ 🌲          |                         |
        |                                                |                         |
        +------------------------------------------------+-------------------------+
        '''

def StatBar(Stat, Max_Stat):
    StatBar = (math.floor(Stat/(Max_Stat/10)))*'█'

    if StatBar == '' and Stat > 0:
        StatBar = '█'

    elif len(StatBar) > 10:
        Statbar = '█'*10
        return Statbar

    while len(StatBar) < 10:
        StatBar += '-'
    return StatBar

def MoveOptions(Room):
    if Room == 'Forest1':
        return '''
            0. Inventory
            1. East
        '''
    
    elif Room == 'Enemy1':
        return '''
            0. Inventory
            1. North
            2. South
        '''

def InputHandling(Room):
    def ReplaceInput():
            print("\033[2A", end="")
            print('Error With Input')
            NextMove = ''
            InputHandling(Room)

    NextMove = input(f'What do You want to do? ')

    if Room == 'Forest1':
        if NextMove == '1':
            PrintMainUI('Enemy1')

        elif NextMove == '0':
            pass

        else:
            ReplaceInput()

    elif Room == 'Enemy1':
        if NextMove == '1':
            PrintMainUI('Enemy1', story.Enemy1())
            
        elif NextMove == '0':
            pass
        else:
            ReplaceInput()
    
def TitleScreen():
    os.system('cls')
    print(f'''
    +------------------------------------------------------------------------------------------------------------------------------------+     
    |                                                                                                                                    |
    |   ███╗   ██╗██╗ █████╗ ██████╗  ██████╗ ███╗   ██╗          _____ _            _              _     ____            _              |
    |   ████╗  ██║██║██╔══██╗██╔══██╗██╔═══██╗████╗  ██║         |_   _| |__   ___  | |    ___  ___| |_  |  _ \ ___  __ _| |_ __ ___     |
    |   ██╔██╗ ██║██║███████║██║  ██║██║   ██║██╔██╗ ██║  _____    | | | '_ \ / _ \ | |   / _ \/ __| __| | |_) / _ \/ _` | | '_ ` _ \    |
    |   ██║╚██╗██║██║██╔══██║██║  ██║██║   ██║██║╚██╗██║ |_____|   | | | | | |  __/ | |__| (_) \__ \ |_  |  _ <  __/ (_| | | | | | | |   |
    |   ██║ ╚████║██║██║  ██║██████╔╝╚██████╔╝██║ ╚████║           |_| |_| |_|\___| |_____\___/|___/\__| |_| \_\___|\__,_|_|_| |_| |_|   |
    |   ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝                                                                                 |
    |                                                                                                                                    |
    +------------------------------------------------------------------------------------------------------------------------------------+     
          
   Welcome to Your Adventure, Continue with your adventure, or start a new one!
    
    +----------Save 1----------+    +----------Save 2----------+    +----------Save 3----------+    +----------Save 4----------+
    |Name: {variables.Name:<20}|    |Name: {variables.Name:<20}|    |Name: {variables.Name:<20}|    |Name: {variables.Name:<20}|
    |Room: {variables.Room:<20}|    |Room: {variables.Room:<20}|    |Room: {variables.Room:<20}|    |Room: {variables.Room:<20}|
    +--------------------------+    +--------------------------+    +--------------------------+    +--------------------------+

    0. Exit
    
    1. Save 1
    2. Save 2
    3. Save 3
    4. Save 4

    ''')
    def TitleSelection():

        def ReplaceInput():
                print("\033[2A", end="")
                print('Error With Input')
                SaveSelection = ''
                TitleSelection()
        
        SaveSelection = input('Choice: ')

        if SaveSelection == '0':
            quit()

        elif SaveSelection == '1':
            PrintMainUI('Forest1')

        elif SaveSelection == '2':
            PrintMainUI('Enemy1')

        elif SaveSelection == '3':
            PrintMainUI('Enemy1')

        elif SaveSelection == '4':
            PrintMainUI('Enemy1')

        else:
            ReplaceInput()
    
    TitleSelection()