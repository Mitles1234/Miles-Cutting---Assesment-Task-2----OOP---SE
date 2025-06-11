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
    Input_Selection(movement.MoveOptions(Room))

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
│   Health:  ♥️  \033[31m{StatBar(saves.User.Health['Health'], saves.User.Health['Max_Health'])} \033[0m {f'({saves.User.Health['Health']}/{saves.User.Health['Max_Health']})':<12}│
│   Stamina: 🔋 \033[32m{StatBar(saves.User.Stamina['Stamina'], saves.User.Stamina['Max_Stamina'])} \033[0m {f'({saves.User.Stamina['Stamina']}/{saves.User.Stamina['Max_Stamina']})':<12}│
│   Mana:    💠 \033[34m{StatBar(saves.User.Mana['Mana'], saves.User.Mana['Max_Mana'])} \033[0m {f'({saves.User.Mana['Mana']}/{saves.User.Mana['Max_Mana']})':<12}│
│                                       │
+───────────────────────────────────────+'''

def DisplayInventory():
    return f'''+────────────────────────--==| Inventory |==--────────────────────────+
│   {'🪙  Gold':<12} -   {saves.User.Gold:<48} |
│   {'Weapon':<12} -   {saves.User.WeaponSlot.name:<15} {'Chestplate':<12} -   {saves.User.ChestplateSlot.name:<15} │
│   {'Helmet':<12} -   {saves.User.HelmetSlot.name:<15} {'Boots':<12} -   {saves.User.BootSlot.name:<15} │
+─────────────────────────────────────────────────────────────────────+
│   {saves.User.OtherSlot1['Item'].name:<18} -   {saves.User.OtherSlot1['Qty']:<9} {saves.User.OtherSlot2['Item'].name:<18} -   {saves.User.OtherSlot2['Qty']:<9} │
│   {saves.User.OtherSlot3['Item'].name:<18} -   {saves.User.OtherSlot3['Qty']:<9} {saves.User.OtherSlot4['Item'].name:<18} -   {saves.User.OtherSlot4['Qty']:<9} │
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
    try:
        with open(f'Save1.json', 'r') as f:
            Player_Data_1 = json.load(f)
    except:
        Player_Data_1 = {}
    
    try:
        with open(f'Save2.json', 'r') as f:
            Player_Data_2 = json.load(f)
    except:
        Player_Data_2 = {}

    try:
        with open(f'Save3.json', 'r') as f:
            Player_Data_3 = json.load(f)
    except:
        Player_Data_3 = {}
   
    try:
        with open(f'Save4.json', 'r') as f:
                Player_Data_4 = json.load(f)
    except:
        Player_Data_4 = {}


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
    |Name: {Player_Data_1.get('Name', 'None'):<20}|    |Name: {Player_Data_2.get('Name', 'None'):<20}|    |Name: {Player_Data_3.get('Name', 'None'):<20}|    |Name: {Player_Data_4.get('Name', 'None'):<20}|
    |Room: {Player_Data_1.get('Location', 'None'):<20}|    |Room: {Player_Data_2.get('Location', 'None'):<20}|    |Room: {Player_Data_3.get('Location', 'None'):<20}|    |Room: {Player_Data_4.get('Location', 'None'):<20}|
    +--------------------------+    +--------------------------+    +--------------------------+    +--------------------------+


    ''')
    Input_Selection({
         'Save 1': lambda: saves.load(Player_Data_1, 1),
         'Save 2': lambda: saves.load(Player_Data_2, 2),
         'Save 3': lambda: saves.load(Player_Data_3, 3),
         'Save 4': lambda: saves.load(Player_Data_4, 4),

         'Exit': lambda: saves.leave()
    })

    PrintMainUI(saves.User.Location)

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
        def EnchantmentDisplay():
            return f'''
            +---+{'-'*39}+- Wat -+- Fir -+- Nat -+
            | 1 | Weapon Slot:     {saves.User.WeaponSlot.name:<20} | {saves.User.WeaponSlot.multiplyers['Wat']:<3.3f} | {saves.User.WeaponSlot.multiplyers['Fir']:<3.3f} | {saves.User.WeaponSlot.multiplyers['Nat']:<3.3f} |
            | 2 | Helmet Slot:     {saves.User.HelmetSlot.name:<20} | {saves.User.HelmetSlot.multiplyers['Wat']:<3.3f} | {saves.User.HelmetSlot.multiplyers['Fir']:<3.3f} | {saves.User.HelmetSlot.multiplyers['Nat']:<3.3f} |
            | 3 | Chestplate Slot: {saves.User.ChestplateSlot.name:<20} | {saves.User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {saves.User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {saves.User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
            | 4 | Boot Slot:       {saves.User.BootSlot.name:<20} | {saves.User.BootSlot.multiplyers['Wat']:<3.3f} | {saves.User.BootSlot.multiplyers['Fir']:<3.3f} | {saves.User.BootSlot.multiplyers['Nat']:<3.3f} |
            +---+{'-'*39}+-------+-------+-------+'''
        
        Selection = input('Choice: ')

        if Selection == '1':
            print('''Select Item to Enchant: ''')

        else:
            print("Invalid selection, please try again.")
            VillagerSelection()

    VillagerSelection()

def Input_Selection(options: dict):
    def ReplaceInput():
        print("\033[2A", end="")  # Move cursor up 2 lines
        print('Error With Input')
        return get_input()  # Re-prompt
    
    def get_input():
        try:
            SaveSelection = input('Choice: ')

            SaveSelection = int(SaveSelection)
            if 1 <= SaveSelection <= len(option_list):
                option_list[SaveSelection - 1][1]()  # Call the corresponding function
            else:
                ReplaceInput()
        except (ValueError, IndexError):
            ReplaceInput()

    # Print options
    option_list = list(options.items())
    print("Select an option:")
    for i, (name, _) in enumerate(option_list, start=1):
        print(f"{i}. {name}")
    print()
    get_input()