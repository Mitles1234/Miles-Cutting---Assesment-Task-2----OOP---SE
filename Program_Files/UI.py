import os
import math
import story
import items
import variables
import json
import saves
import movement
import trading
import magic

#--- Displays the UI Screen for the User ---
def PrintMainUI(Room):
    os.system('cls')

    map_lines = movement.Map(Room).splitlines()
    stats_lines = DisplayStats().splitlines()
    inventory_lines = DisplayInventory().splitlines()
    MapKey_lines = DisplayMapKey().splitlines()

    side_panel = stats_lines + inventory_lines + MapKey_lines
    max_lines = max(len(map_lines), len(side_panel))

    print()

    for i in range(max_lines):
        map_line = map_lines[i] if i < len(map_lines) else ""
        side_line = side_panel[i] if i < len(side_panel) else ""
        print(f"{map_line:<60} {side_line}")

    print()

    print(story.Story(Room))
    print(movement.MoveOptions(Room))
    movement.InputHandling(Room)

def DisplayStats():
    def StatBar(Stat, Max_Stat):
        StatBar = (math.floor(Stat/(Max_Stat/10)))*'█'
        DeadBar = ''

        if StatBar == '' and Stat > 0:
            StatBar = '█'

        elif len(StatBar) > 10:
            Statbar = '█'*10
            return Statbar

        for i in range(0, 10-len(StatBar)):
            DeadBar += f'-'
            
        return StatBar + f'\033[37m{DeadBar}'
    
    return f'''+───────────--==| Stats |==--───────────+
│                                       │
│   Health:  ♥️  \033[31m{StatBar(variables.Health, variables.Max_Health)} \033[0m {f'({variables.Health}/{variables.Max_Health})':<12}│
│   Stamina: 🔋 \033[32m{StatBar(variables.Stamina, variables.Max_Stamina)} \033[0m {f'({variables.Stamina}/{variables.Max_Stamina})':<12}│
│   Mana:    💠 \033[34m{StatBar(variables.Mana, variables.Max_Mana)} \033[0m {f'({variables.Mana}/{variables.Max_Mana})':<12}│
│                                       │
+───────────────────────────────────────+'''

def DisplayInventory():
    return f'''+────────────────────────--==| Inventory |==--────────────────────────+
│   {'🪙  Gold':<12} -   {variables.Gold:<48} |
│   {'Weapon':<12} -   {variables.Inventory['WeaponSlot'].name:<15} {'Chestplate':<12} -   {variables.Inventory['ChestplateSlot'].name:<15} │
│   {'Helmet':<12} -   {variables.Inventory['HelmetSlot'].name:<15} {'Boots':<12} -   {variables.Inventory['BootSlot'].name:<15} │
+─────────────────────────────────────────────────────────────────────+
│   {variables.Inventory['OtherSlot1']['Item'].name:<18} -   {variables.Inventory['OtherSlot1']['Qty']:<9} {variables.Inventory['OtherSlot2']['Item'].name:<18} -   {variables.Inventory['OtherSlot2']['Qty']:<9} │
│   {variables.Inventory['OtherSlot3']['Item'].name:<18} -   {variables.Inventory['OtherSlot3']['Qty']:<9} {variables.Inventory['OtherSlot4']['Item'].name:<18} -   {variables.Inventory['OtherSlot4']['Qty']:<9} │
+─────────────────────────────────────────────────────────────────────+ '''

def DisplayMapKey():
    return f'''+─────────────────────────--==| Map Key |==--─────────────────────────+
│   ██ - You              🔮 - Wizard Tower                           │
│   🏠 - Village          ☠️  - Enemy            👑 - Goblin King      │
│   🌲 - Forest           ⛰️  - Mountain                               │
+─────────────────────────────────────────────────────────────────────+'''

def DisplayInventoryScreen():
    print('''


''')

def TitleScreen():
    os.system('cls')
    
    with open(f'Save1.json', 'r') as f:
            Player_Data_1 = json.load(f)

    with open(f'Save2.json', 'r') as f:
            Player_Data_2 = json.load(f)

    with open(f'Save3.json', 'r') as f:
            Player_Data_3 = json.load(f)

    with open(f'Save4.json', 'r') as f:
            Player_Data_4 = json.load(f)


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
    |Name: {Player_Data_1.get('Player_Name', 'None'):<20}|    |Name: {Player_Data_2.get('Player_Name', 'None'):<20}|    |Name: {Player_Data_3.get('Player_Name', 'None'):<20}|    |Name: {Player_Data_4.get('Player_Name', 'None'):<20}|
    |Room: {Player_Data_1.get('Location', 'None'):<20}|    |Room: {Player_Data_2.get('Location', 'None'):<20}|    |Room: {Player_Data_3.get('Location', 'None'):<20}|    |Room: {Player_Data_4.get('Location', 'None'):<20}|
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

def VillagerMenu(Village):
    os.system('cls')
    
    print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {Village.name:<38}|
    |                                                         |
    |   Profession:     {Village.profession:<38}|
    |                                                         |
    +---------------------------------------------------------+
    
    0. Exit
    1. Trade with {Village.name}
    ''')

    def VillagerSelection():
        Selection = input('Choice: ')

        if Selection == '1':
            print(Village.Inventory_Trading())

        else:
            print("Invalid selection, please try again.")
            VillagerSelection()

    VillagerSelection()

def EnchantmentScreen(Wizard):
    print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {Wizard.name:<38}|
    |                                                         |
    +---------------------------------------------------------+
    
    0. Exit
    1. Enchant Item with {Wizard.name}
    ''') 

    def VillagerSelection():
        def Inventory_Display():
            return f'''
            +---+{'-'*30}+- Wat -+- Fir -+- Nat -+
            |1  |Weapon Slot: {saves.User.WeaponSlot:<20}|{saves.User.WeaponSlot['multiplyers']['Fir']}
            '''
        Selection = input('Choice: ')

        if Selection == '1':
            print('''Select Item to Enchant: ''')

        else:
            print("Invalid selection, please try again.")
            VillagerSelection()

    VillagerSelection()

Bob = trading.ArmourSmith('Bob')
VillagerMenu(Bob)