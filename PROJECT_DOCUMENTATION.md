# 11SE Task 2 - OOP - Text Adventurer
## By Miles Cutting

***

Notes of Later Miles:
https://azgaar.github.io/Fantasy-Map-Generator/


# Sprint 1:
### **Requirements Outline**
#### **Functional Requirements**
- Data Retrieval: 
    - The user needs to be able to at any point in the program, view important player statistics such as
        - Inventory - Armour / Weapons
        - Health
        - Stamina
        - Mana
        - Gold/Currency
        - Location/Map

- User Interface:
    - The user will interact with the program via a the Python Terminal
    - Their will be a heavy use of ASCII art and emoji's to convey information to the player such as
        - Using a Heart to symbolize the health statistic
        - Using a Sword to symbolize the damage statistic
        - Using A combination of ( | + - / \ = [] ) to make pictures such as maps, or inventory screens
    - The user will move through locations / situations / interactions via shortcut commands such as ( N S E W 1 2 3 4 )

- Data Display:
    - The user will retrieve information about what is happening in the game such as
        - When they Encounter an Enemy
        - When they Encounter a Friend
        - When they need to find shelter
        - When they need to eat/drink
    - The user needs to receive a range of actions for how to handle a situation, with more then one change in any given situation to have a 'second chance' such as
        - Being able to turn around while adventuring
        - Combat involving multiple back and forth turns for the player to learn the type of attacks that work on enemies

#### **Non-Functional Requirements**
- Performance:
    - The program will be turn based, so their won't be any meaningful impact on the functionality of the game due too poor performance, however, to meet better user satisfaction, having the program work quickly will be a large point of focus. Because the system is text-based, I am expecting it to work quickly between changing scenes and scenarios.

- Reliability:
    - The program needs to have reliable handling of data, to ensure the user moves throughout the program with the same statistics, and inventory. To keep it reliable, i'll make use of separate python files to handle the different systems, such as adjusting health, and stamina, to avoid having the main program accidentally adjusting statistics without directly calling the other file., , which will use classes to handle each of the systems.

- Usability and Accessibility:
    - To make the system easy to navigate and interact with, each time the user needs to interact with a function, it will have a clear name, or instructions with it as to what the user wants to do, such as
        - Open Inventory
        - Move ( N S E W )
        - Use {Item}


### **Determining Specifications**
#### **Functional Specifications**
- User Requirements:
    - View Player Specific Information:
        - Health
        - Stamina
        - Mana
        - Inventory - Armour / Weapons / Items
        - Location / Map
    - Interact with what is Happening:
        - Move ( N S E W )
        - Attack
        - Trade
    - Get a Response from the Program as to what is happening:
        - A description of what is happening around them
        - A description of what other people / places / enemies are doing, such as Enemy XYZ attacks for 4 damage

- Inputs and Outputs:
    - The system will accept inputs such as ( N S E W 1 2 3 4 ), which will each correspond with an action the user can do, such as move, or attack
    - The system will then take the inputs from the user, and preform the corresponding action, such as moving the player to a different room, or attacking an enemy.
    - If the user inputs something the program doesn't understand, it will prompt the user to enter new information.

- Core Features:
    - The program will need to take in user inputs, and use them to interact with the program to overall progress through the adventure/story. Their will be a variety of unique systems for the user to interact with, such as
        - Combat System - Which will allow the user to attack enemies
        - Movement System - Which will allow the user to move throughout the world, and explore different places.
        - Inventory System - Which will make the user have to chose which items to take with them and which ones to leave behind
        - Trading/Currency System - Which will allow the user to trade with merchants to better their gear, and learn information
        - Magic / Enchantment System - Which will allow the user to have special abilities, unique to each play through, such as protection magic, and damage magic

- User Interaction:
    - The user will interact with the system by using the terminal/command line, and will have clear, and thorough instructions on how to navigate the UI. The user will only have to use quick, simple commands, such as ( N S E W 1 2 3 ), to ensure the interactions are fast.

- Error Handling:
    - The most common error the system will have to handle is issues with user inputs, which can be avoided through the use of if else statements, and try and except statements. 
    - Other errors can be avoided through try and except statements in the program, that will alert the user when an error has occurred, and the steps to take with fixing the error, such as restarting the program.

#### **Non-Functional Specifications**
- Performance:
    - The system should run in a highly efficient way, ensuring the program only runs what it needs to, when it needs to. The program needs to be able to load each part of the screen within half a second of the last user input, which will be achievable because of Text based UI. Furthermore, to keep it more engaging, the 'Story based' portion of the UI will be delivered overtime, with it appearing in a 'swipe' action across each line. While this may slow faster readers, it will mean the User isn't dumped with a collection of information all at once, making it more User friendly. To achieve all of this, I will make strong use of loops, and functions.

- Useability / Accessibility:
    - The system will use a basic Keyboard, and High contrast text (Such as White on Black, or Black on White). This will ensure the system can handle both unique forms of input, and support people with poor or limited vision. 

- Reliability:
    - To ensure the program is handling inputs and outputs correctly, their will be a range of validation and *** to ensure it is handling data correctly, and if it isn't, the User will be informed with not only what has happened, but with the measures that should be taken to rectify the issues, such as re-entering the information, or restarting the program.

#### **Use Cases:**

**Actors:**

    User  


**Preconditions:**

    The program has began with the programs that need to run to initialize the program have run. ** Need Help


**Main Flow:**

    Each 'Scene' the user is presented with, will present the user with a variety of options, numbered to allow for faster interaction. The user will then select what to do based of of those options, such as purchase an item, move on the map, or preform a move in combat.

**Alternate Flows:**

Movement: ###### FINSH

    The User is presented with up to 4 options (N S E W), that will move them to new locations on the wider map. Each time the player moves, they will use part of their stamina, which requires food, water, or a stamina potion to replenish. Alternately, the user can use other forms of travel, such as horse and cart, to move quickly between key locations, at a cost, and with missing possibly key locations along the way. 

Combat:

    The user will have up to 2 damage items to use at any given point, that may be more or less effective against a range of different opponents which will further interact with the mana / magical system, such as a Fire Enchanted Item will do more damage against nature enemies, but be less effective against water enemies. Another example is a Sword being less effective against Goblins, who might be weak to daggers, verses a sword doing more damage to Trolls.

Mana / Magical:

    Their will be a heavy use of a Magical system, that will allow the player to better weapons in some aspects, and limit them in others. The Player will be able to receive better and better Magical items through the use of Experience, which will be collected when defeating enemies, making trades, or using a magical item. The Max Level for this system will allow for stronger damage on harder enemies. To preform each of these abilities, the player will use their 'Mana' values, which will be used each time a magical item is used. If the mana value runs out, all the enchantments the player has will stop working. To replenish their values, they can go to a towns priest, or if they are away from town, use a Mana Potion.


    Another key element of the Magic system, will be the use of enchanted items, which may increase the players speed (Lowering the )


### Review:

#### main.py
```Python
import items
import story
import UI
import variables

UI.TitleScreen()
```


#### UI.py
```Python
import os
import math
import story
import variables
import saves

#--- Displays the UI Screen for the User ---
def PrintMainUI(Room):
    os.system('cls')

    map_lines = Map(Room).splitlines()
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
    print(MoveOptions(Room))
    InputHandling(Room)

def Map(Room):

    def TitleGenerator(Title):
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+'

    if Room == 'Forest1':
        return f'''        {TitleGenerator('Dark Forest')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Enemy1':
        return f'''        {TitleGenerator('Dark Forest')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''

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
│   {'Weapon':<12} -   {variables.Inventory['WeaponSlot']:<15} {'Chestplate':<12} -   {variables.Inventory['ChestplateSlot']:<15} │
│   {'Helmet':<12} -   {variables.Inventory['HelmetSlot']:<15} {'Boots':<12} -   {variables.Inventory['BootSlot']:<15} │
+─────────────────────────────────────────────────────────────────────+
│   {variables.Inventory['OtherSlot1']['Item']:<18} -   {variables.Inventory['OtherSlot1']['Qty']:<9} {variables.Inventory['OtherSlot2']['Item']:<18} -   {variables.Inventory['OtherSlot2']['Qty']:<9} │
│   {variables.Inventory['OtherSlot3']['Item']:<18} -   {variables.Inventory['OtherSlot3']['Qty']:<9} {variables.Inventory['OtherSlot4']['Item']:<18} -   {variables.Inventory['OtherSlot4']['Qty']:<9} │
+─────────────────────────────────────────────────────────────────────+ '''

def DisplayMapKey():
    return f'''+─────────────────────────--==| Map Key |==--─────────────────────────+
│   ██ - You              🔮 - Wizard Tower                           │
│   🏠 - Village          ☠️  - Enemy            👑 - Goblin King      │
│   🌲 - Forest           ⛰️  - Mountain                               │
+─────────────────────────────────────────────────────────────────────+'''

def TitleScreen():
    os.system('cls')
    saves.Load() # Fill in for loading saves later
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
```

#### story.py
```Python
import math

def Story(Room):
    if Room == 'Forest1':
        return 'Interesting Story'
    
    elif Room == 'Enemy1':
        return 'You Have Encountered and Enemy!!! You will have to fight'
    
def Title(Room):
    if Room == 'Forest1':
        return TitleGenerator('Dark Forest')


def TitleGenerator(Title):
    return f'''
    +{'-'*64}+
    |{' '*((32-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{' '*((32-(math.ceil(len(Title)/2)))-6)}|
    +{'-'*64}+
    '''
```

####  variables.py
```Python
Health = 98
Max_Health = 100
Stamina = 65
Max_Stamina = 100
Mana = 23
Max_Mana = 100

Gold = 5

Name = 'John'
Room = 'Dark Forest'

#--- Weapons ---
Stick = 'Stick'
Wooden_Sword = 'Wooden_Sword'
Iron_Sword = 'Iron_Sword'

#--- Helmets ---
None_Helmet = 'None'

#--- ChestPlate ---
None_Chestplate = 'None'

#--- Boot ---
None_Boot = 'None'

#--- Item ---
None_Item = 'None'

Inventory = {
            'Player_Name': Name,
            'WeaponSlot': Wooden_Sword, 
            'HelmetSlot': None_Helmet, 
            'ChestplateSlot': None_Chestplate,
            'BootSlot': None_Boot,
            'OtherSlot1': {'Item': None_Item, 'Qty': 0},
            'OtherSlot2': {'Item': None_Item, 'Qty': 0},
            'OtherSlot3': {'Item': None_Item, 'Qty': 0},
            'OtherSlot4': {'Item': None_Item, 'Qty': 0}
    }
```

### Review Questions:

#### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
 - 

#### Analyse the performance of your program against the key use-cases you identified.
 - 

#### Assess the quality of your code in terms of readability, structure, and maintainability.
 - Based on Feedback from my previous task, I took lots of extra time in planning out my code to be more easily readable and conventional. I have made heavy uses of functions to sperate code blocks into smaller chuncks that can be more easily understood, and maintained. Furthermore, I have spread my code accross multiple files, making it easier and faster to fund and modify parts of the code based on the function. Their is also a strong use of comments to explain what code does, and why it works. These aspects of my code make my code a high qualilty in terms of readability, structure, and maintainaility.

#### Explain the improvements that should be made in the next stage of development.
 - 

