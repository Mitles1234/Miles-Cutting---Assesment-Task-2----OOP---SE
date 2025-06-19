# 11SE Task 2 - OOP - Text Adventurer Dungeon Crawler
## By Miles Cutting

***

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

### **Use Cases:**

**Actors:**

    User  


**Preconditions:**

    The game begins by initializing the required systems, including loading maps, setting up the UI, and preparing the stat systems. There is a login system that is password-protected, ensuring only authorized players can access their game data. All players start with the same base stats, so there is no need for the user to input personal character data. A stat setup system automatically configures each player's initial statistics, providing a consistent and fair starting point for every user. Once the system is initialized and the user is logged in, the main game loop begins.


**Main Flow:**

    Each 'Scene' the user is presented with will offer a variety of options, numbered for fast and easy interaction. These options allow the user to make choices such as purchasing an item, moving around the map, inspecting their inventory, or engaging in combat. The player selects actions by entering the associated number or shortcut command, like N, S, E, or W for movement. The system is designed to provide a clear and intuitive flow from one situation to the next, ensuring the player always has multiple options and can see the results of their decisions.



**Alternate Flows:**

Movement:

    The user is presented with up to four directional option (N S E W) which move them to new locations across the map. Each movement uses a portion of the player's stamina, which can be replenished by consuming food items like bread or using certain magical items. Players can also travel quickly between key locations using methods like horse and cart, but doing so may skip over important side locations or hidden items. While most areas are accessible, some are designed to be ‘soft locked,’ meaning the player can enter them at any time but will likely be under-equipped and face much stronger enemies. Villages provide safe spots where the player can rest without using stamina and prepare for future travel.

Combat:

    In combat, the player can equip and use only one physical damage item at a time, such as a sword, dagger, or axe. This item is their primary melee weapon, but its effectiveness varies depending on the enemy type—certain enemies may be resistant or vulnerable to specific weapon types. In addition to their physical weapon, the player can access a range of offensive spells, each consuming mana when cast. These spells may include elemental attacks like fireball, ice shard, or lightning strike, and can be more effective against specific enemy classes, for example, fire-based spells dealing extra damage to nature-type enemies. Combat remains turn-based, giving the player time to consider their options and adapt to enemy behavior over multiple rounds. This allows for strategic decision, making, where the player might switch between physical attacks and magical abilities depending on the opponent’s strengths and weaknesses. The combat system encourages experimentation and progression as the player learns which tactics are most effective in different encounters.

Inventory: (Mana / Magical)

    The magic system plays a major role in gameplay, with mana being consumed whenever a magical item is used. This includes attacking with enchanted weapons, taking damage while wearing enchanted armor, casting spells like fireball, or activating magical items such as stamina necklaces. If the player runs out of mana, all enchantments become inactive until mana is replenished. Mana can be restored either by visiting a priest in a town or using a mana potion in the field. As the player earns experience from combat, trades, and magical item use, they gain access to stronger magical items and abilities. One key feature of this system is the use of enchanted gear, which can grant passive bonuses—such as increased speed, which reduces stamina usage when moving or gives the player stronger actions during combat.

#### Use Case Diagram:
<img src="Images/Usecase_Diagram.png" alt="Alt Text" width="500">


### **Data Flow Diagram**

#### **Level 0:**
<img src="Images/DFD_Level0.png" alt="Alt Text" width="500">

#### **Level 1:**
<img src="Images/DFD_Level1.png" alt="Alt Text" width="500">


### **Story Boards**
<img src="Images/StoryBoard_MainUI.png" alt="StoryBoard_MainUI" width="500">    <img src="Images/StoryBoard_TitleScreenUI.png" alt="StoryBoard_TitleScreenUI" width="500">
<img src="Images/StoryBoard_CombatUI.png" alt="StoryBoard_CombatUI" width="500">    <img src="Images/StoryBoard_VillagerUI.png" alt="StoryBoard_VillagerUI" width="500">

<img src="Images/StoryBoard_Complete.png" alt="Alt Text" width="1000"> 


### Build:

#### main.py
```Python
# --- Imports ---
'''Imports the Necessary Files so the Main file can access informations'''
import items
import story
import UI
import variables

UI.TitleScreen() # From the File 'UI' run Titlescreen
```

#### UI.py
```Python
# --- Imports ---
'''Imports the Necessary Files so the file can access informations'''
import os
import math
import story
import variables
import saves

#--- Displays the UI Screen for the User ---
def PrintMainUI(Room):
    '''This function is the Key UI screen for each Room, where it pulls information from a range of sources, and lays it out in a efficent layout'''
    os.system('cls') # Clears the screen (This makes for a more adaptive, and engaing UI)

    # Each of these retrieves the UI data, i.e StatBars, Maps, and Inventory, and splits them up into their individual lines
    # This allows them to be printed next to eachother by printing it layer by layer rather than section by section
    map_lines = Map(Room).splitlines() # Splits Map lines
    stats_lines = DisplayStats().splitlines() # Splits Stat lines
    inventory_lines = DisplayInventory().splitlines() # Splits Inventory lines
    MapKey_lines = DisplayMapKey().splitlines() # Splits Map Key lines

    side_panel = stats_lines + inventory_lines + MapKey_lines # Alligns the Stat Line, Inventoy Line, and Map Key lines to be ontop of eachother
    max_lines = max(len(map_lines), len(side_panel)) # Calculates how many lines it needs to print for the UI

    print() # Spacer in the Terminal

    for i in range(max_lines): # For each line in Max_Lines
        map_line = map_lines[i] if i < len(map_lines) else "" # Retrieve Map line of the Value of i, or if too big, return blank
        side_line = side_panel[i] if i < len(side_panel) else "" # Retrieve Side Panel line of the Value of i, or if too big, return blank
        print(f"{map_line:<60} {side_line}") # Prints the two elements next to eachother, using the :<60 to keep the side pannel allined if it is bigger than the map

    print() # Spacer in the Terminal

    print(story.Story(Room)) # From the File Story, Retrieves and prnts the story
    print(MoveOptions(Room)) # Prints the Move options for this room
    InputHandling(Room) # Runs the Input handling for this room

def Map(Room):
    '''This functions runs the Map handling for the room, containing all of the maps, for all the rooms'''
    def TitleGenerator(Title):
        '''This function creates a title for each of the rooms, ensuring it is alligned in the center'''
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+'

    if Room == 'Forest1': # If requested the map for Forest1, returns the map for Forest1 (The map doesn't look alligned but it is due to the emojis.)
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
        │ ██────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Enemy1': # If requested the map for Enemy1, returns the map for Enemy1
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
        │ 🌲────██       🏠       🌲             ├────☠️ ─────👑  │
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
    '''This function contains the possible moves for each room, and tells the player where they can go'''
    if Room == 'Forest1': # If room is Forest1, return the Move options Inventory, and East
        return '''
            0. Inventory
            1. East
        '''
    
    elif Room == 'Enemy1': # If room is Enemy1, return the Move options Inventory, North, and South
        return '''
            0. Inventory
            1. North
            2. South
        '''

def InputHandling(Room):
    '''This function handles the user inputs for each room'''
    def ReplaceInput():
        '''This function removes incorrect user inputs, and alerts the player their is an issue'''
            print("\033[2A", end="") # Removes the past two lines in the Terminal
            print('Error With Input') # Alerts the Player of the Error with Input
            NextMove = '' # Resets the Player input
            InputHandling(Room) # Re-Runs Input handling

    NextMove = input(f'What do You want to do? ') # Retieves the Input for what the player wants to do

    if Room == 'Forest1': # If the Room is Forest1, continue
        if NextMove == '1': # If the Move input was 1, continue
            PrintMainUI('Enemy1') # Prints the Next UI screen for the Room Ememy1

        elif NextMove == '0': # If the Input was 0, pass (Adding this functionality in a later sprint)
            pass 

        else: # If none of these options, continue
            ReplaceInput() # Re-Runs the Input selection process

    elif Room == 'Enemy1': # If the Room is Enemy1, continue (This was mostly a fill in for and idea as for how the program should handle inputs)
        if NextMove == '1': # If the Move input was 1, continue
            PrintMainUI('Village1') # Prints the Next UI screen for the Room Village1

        # Adding other inputs in later sprints when the final input handling is worked out
            
        elif NextMove == '0':# If the Input was 0, pass (Adding this functionality in a later sprint)
            pass

        else: # If none of these options, continue
            ReplaceInput() # Re-Runs the Input selection process

def DisplayStats():
    '''This function returns the Player statistic's to be printed in the UI (This whole program used to be much simpler, but I wanted the dashes to be white instead of the colour they where origionally, which tripled the complexity of this function)'''
    def StatBar(Stat, Max_Stat):
        '''This function turns the players 'Number Statistics', into visually represented bars, allowing for faster, and more effective communication'''
        StatBar = (math.floor(Stat/(Max_Stat/10)))*'█' # Calculates the amount of Bars depending on Max Health to fit 10 unit bar
        DeadBar = '' # Creates value DeadBar
 
        if StatBar == '' and Stat > 0: # Statbar is blank, but the the player isnt dead, continue
            StatBar = '█' # Adds one bar to stat bar

        elif len(StatBar) > 10: # If the statbar is more than 10 units long (More Health than Max Health - Bonus Health/Extra Life)
            Statbar = '█'*10 # Sets stat bar to 10
            return Statbar # Returns Statbar as Full

        for i in range(0, 10-len(StatBar)): # Calculates how many dashes to add to take up the full amount of space
            DeadBar += f'-' # For each blank space, adds a dash
        return StatBar + f'\033[37m{DeadBar}' # Returns the completed bar plus the Missing health (In White), back to the function that called it.
    
    # This returns the 'Stat Block', completed with fully coloured bars representing the players statistics and values, also giving them a numericl value.
    return f'''+───────────--==| Stats |==--───────────+
│                                       │
│   Health:  ♥️  \033[31m{StatBar(variables.Health, variables.Max_Health)} \033[0m {f'({variables.Health}/{variables.Max_Health})':<12}│
│   Stamina: 🔋 \033[32m{StatBar(variables.Stamina, variables.Max_Stamina)} \033[0m {f'({variables.Stamina}/{variables.Max_Stamina})':<12}│
│   Mana:    💠 \033[34m{StatBar(variables.Mana, variables.Max_Mana)} \033[0m {f'({variables.Mana}/{variables.Max_Mana})':<12}│
│                                       │
+───────────────────────────────────────+'''

def DisplayInventory():
    '''This function returns the player inventory block, which is a grid system (Using the :<Number) to align each of the title for what it is with the equipment the player has by retrieving it from the variables file'''

    return f'''+────────────────────────--==| Inventory |==--────────────────────────+
│   {'🪙  Gold':<12} -   {variables.Gold:<48} |
│   {'Weapon':<12} -   {variables.Inventory['WeaponSlot']:<15} {'Chestplate':<12} -   {variables.Inventory['ChestplateSlot']:<15} │
│   {'Helmet':<12} -   {variables.Inventory['HelmetSlot']:<15} {'Boots':<12} -   {variables.Inventory['BootSlot']:<15} │
+─────────────────────────────────────────────────────────────────────+
│   {variables.Inventory['OtherSlot1']['Item']:<18} -   {variables.Inventory['OtherSlot1']['Qty']:<9} {variables.Inventory['OtherSlot2']['Item']:<18} -   {variables.Inventory['OtherSlot2']['Qty']:<9} │
│   {variables.Inventory['OtherSlot3']['Item']:<18} -   {variables.Inventory['OtherSlot3']['Qty']:<9} {variables.Inventory['OtherSlot4']['Item']:<18} -   {variables.Inventory['OtherSlot4']['Qty']:<9} │
+─────────────────────────────────────────────────────────────────────+ '''

def DisplayMapKey():
    '''This function returns the Map Key block, which is used to make sense of the map and its icon based system'''
    return f'''+─────────────────────────--==| Map Key |==--─────────────────────────+
│   ██ - You              🔮 - Wizard Tower                           │
│   🏠 - Village          ☠️  - Enemy            👑 - Goblin King      │
│   🌲 - Forest           ⛰️  - Mountain                               │
+─────────────────────────────────────────────────────────────────────+'''

def TitleScreen():
    '''This function runs the process for the Title Screen - Some of the functionality works, but most is a fill in until the later sprints where it will be more cohesively filled out'''
    os.system('cls') # Clears the Terminal for a more sleek and engaing appearence.
    saves.Load() # Fill in for loading saves later
    # Prints the Titlescreen in large Ascii Letters
    # Welcomes the User
    # Shows them their save files and gives them instrusctions on how to pick
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
        '''This function allow the user to select which save file they would like to chose, and then runs dummy code until other parts of the code are finished in later sprints'''
        def ReplaceInput():
            '''This function removes incorrect user inputs, and alerts the player their is an issue'''
            print("\033[2A", end="") # Removes the past two lines in the Terminal
            print('Error With Input') # Alerts the Player of the Error with Input
            SaveSelection = '' # Resets the Player input
            TitleSelection() # Re-Runs Input handling
        
        SaveSelection = input('Choice: ') # Retrieves the User input

        if SaveSelection == '0': # If user input is 0, quits the program
            quit()

        elif SaveSelection == '1': # If the user input is 1, Runs the MainUI for the Room Forest1 (Dummy Code)
            PrintMainUI('Forest1')

        elif SaveSelection == '2': # If the user input is 2, Runs the MainUI for the Room Enemy1 (Dummy Code)
            PrintMainUI('Enemy1')

        elif SaveSelection == '3': # If the user input is 3, Runs the MainUI for the Room Enemy1 (Dummy Code)
            PrintMainUI('Enemy1')

        elif SaveSelection == '4': # If the user input is 4, Runs the MainUI for the Room Enemy1 (Dummy Code)
            PrintMainUI('Enemy1')

        else: # If input is not known, runs replace input, restarting the input process
            ReplaceInput()
    
    TitleSelection() # Runs the Title Selection process as the end of the Printing the Titlescreen UI elements.
```

#### story.py
```Python
# --- Imports ---
'''Imports the Necessary Files so the Main file can access informations'''
import math

def Story(Room):
    '''This function consolidates the story line, allowing for simpler expansion in future sprints. It works by taking a Room input, and returning the neccessary story elements.'''
    if Room == 'Forest1': # If the Room is Forest1
        return 'Interesting Story' # Returns Fill in Text
    
    elif Room == 'Enemy1': # if the Room is Enemy1
        return 'You Have Encountered and Enemy!!! You will have to fight' # Returns Fill in Text
    
def Title(Room):
    '''This function, similar to story, returns a title for each of the rooms'''
    if Room == 'Forest1': # If room is Forest1
        return TitleGenerator('Dark Forest') # Returns a title made with TitleGerator for the Title 'Dark Forest'


def TitleGenerator(Title):
    '''This function generates titles that are centered, bassed on the length of the title'''
    # Generates the Top wall of the box
    # Calculates how much padding is required on each side to center it (If it is odd it is slightly to the left)
    # Generates the Bottom wall of the box
    # Returns the Generated Title
    return f'''
    +{'-'*64}+
    |{' '*((32-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{' '*((32-(math.ceil(len(Title)/2)))-6)}|
    +{'-'*64}+
    '''
```

####  variables.py
```Python
'''This file contains all the neccessary Variables, that need to be accessed and changed when being used accross files'''
Health = 98 # Sets Health to 98
Max_Health = 100 # Sets Max Health to 100
Stamina = 65 # Sets Stamina to 65
Max_Stamina = 100 # Sets Max Stamina to 100
Mana = 23 # Sets Mana to 23
Max_Mana = 100 # Sets Max Mana to 100

Gold = 5 # Sets Gold to 5

Name = 'John' # Sets name to John
Room = 'Dark Forest' # Sets Room to 'Dark Forest'

#--- Weapons ---
Stick = 'Stick' # Sets stick to 'Stick'
Wooden_Sword = 'Wooden_Sword' # Sets Wooden_Sword to 'Wooden_Sword'
Iron_Sword = 'Iron_Sword' # Sets Iron_Sword to 'Iron_Sword'

#--- Helmets ---
None_Helmet = 'None' # Sets None_Helmet = 'None' 

#--- ChestPlate ---
None_Chestplate = 'None'# Sets None_Chestplate = 'None' 

#--- Boot ---
None_Boot = 'None'# Sets None_Boot = 'None' 

#--- Item ---
None_Item = 'None'# Sets None_Item = 'None' 

Inventory = { # Creates a Dictionary based on the information set previously (Designed to be used later with saving functionality)
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
 - The project meets most of the planned functional and non-functional requirements effectively, offering clear player statistics, intuitive ASCII and emoji-based UI elements, and responsive text-based interactions. Players can view and manage inventory, health, and location, with meaningful turn-based gameplay that includes multiple decision points and combat strategy. The game performs quickly due to its lightweight design and organized file structure, ensuring consistent tracking of stats and player actions. While usability is already strong with labeled commands and accessible options, some features, such as expanded scenario interactions and second-chance events, will be more fully implimented and polished in the second and third sprint.

#### Analyse the performance of your program against the key use-cases you identified.
 - The program largely behaves as expected and handles input/output effectively according to the planned design. Basic command systems have been successfully implemented, with more advanced interactions scheduled for future sprints. Input handling works well, although there is a minor bug where incorrect inputs are removed, but the display of previous inputs isn't fully cleared—this visual glitch does not affect functionality or performance and is planned to be resolved in a later sprint. Player statistics such as health, stamina, mana, and location are clearly displayed, making excellent use of terminal space, and emojis render correctly, though their irregular print sizes present a slight challenge during development. The game provides clear textual feedback for player actions and events, and the map system effectively tracks player movement in real time. Because the game operates on a turn-based system, player stats are accurately updated after each action, keeping the interface consistent and informative throughout gameplay.

#### Assess the quality of your code in terms of readability, structure, and maintainability.
 - Based on Feedback from my previous task, I took lots of extra time in planning out my code to be more easily readable and conventional. I have made heavy uses of functions to sperate code blocks into smaller chuncks that can be more easily understood, and maintained. Furthermore, I have spread my code accross multiple files, making it easier and faster to fund and modify parts of the code based on the function. Their is also a strong use of comments to explain what code does, and why it works. These aspects of my code make my code a high qualilty in terms of readability, structure, and maintainaility.

#### Explain the improvements that should be made in the next stage of development.
 - In the next stage of development, the primary focus will be on completing and refining the movement, combat, and trading systems, which are currently only partially implemented. These features are essential for the core gameplay loop and will provide players with a more interactive and dynamic experience. Alongside these enhancements, improvements to code quality will also be prioritized. Although the codebase is already readable due to previous planning, the next sprint will focus on adding more detailed comments throughout the program to better document how each system functions. Additionally, there are plans to implement a more robust and efficient system for tracking the player’s location, which will improve consistency across scenes and interactions. These refinements will help streamline development in future sprints and make the codebase easier to expand and maintain.

# Sprint 2

### Structure Chart
<img src="Images/Structure_Chart.png" alt="Alt Text" width="500">

## Algorithms

### Mainline (PrintMainUI)
``` 
BEGIN PrintMainUI (Room)
	Exited = False
    Clear Terminal


	IF User Health is less than or Equal to 0 THEN
		Player Died
    ELIF Enemy Health is less than or Equal to 0 THEN
        Died (‘No Stamina’)
    ENDIF

    FOR i IN 1 TO max_lines STEP 1
            Display Mapline Row i + SidePanel Row i

    Users_Location = Room

    Display

    Display Story (Room)

    Display

    WHILE true
        IF Exited is False THEN
            SET User.Room to True
            Input_Selection(MoveOptions(Room))
                        ClearLines ( length of (MoveOptions (Room) ) + 3)
        ELSE
            BREAK
        ENDIF

    ENDWHILE

END PrintMainUI (Room)
```

### Subroutine (Combat)
```
BEGIN Combat (Enemy, Room)
	IF Enemy Type is ‘Fir’ THEN
		Type = ‘Fire’
	ELIF Enemy Type is ‘Wat’ THEN
		Type = ‘Water’
	ELIF Enemy Type is ‘Nat’ THEN
		Type = ‘Nature’
	ENDIF
	
	Display You have Encountered an Enemy

	WHILE true
		Exited = False
		Display Enemy and Player Statistics
		IF Enemy Health is Less than or Equal to 0 THEN
			Clear 17 Lines of the Terminal
			Display You have Defeated Enemy
			Increase Players Weapon Level by Half of the Level of the Enemy
			END Combat (Enemy, Room)

		ELIF Player Health is Less than or Equal to 0 THEN
			Died (Enemy.name)
			END Combat (Enemy, Room)

        Input_Selection (Attack, Use Item)

        IF Exited is False THEN
            Enemy.Attacking (User)

        Clear 20 Lines of the Terminal

    ENDWHILE

END Combat (Enemy, Room)

```

### Subroutine (Statbar)
```
BEGIN Statbar (Stat, Max_Stat)
    StatBar = Create stat bar with blocks based on percentage of max
	Deadbar = Blank
	
	IF StatBar is Blank AND Stat Greater than 0 THEN
		StatBar = '█'
	ELIF lenngth of (StatBar) is greater than 10 THEN
		StatBar = '█'*10

	FOR i IN 1 TO (10 - len (StatBar)) STEP 1
		Add One Unit to Deadbar

	Return StatBar + *White* Deadbar

END Statbar (Stat, Max_Stat)
```

### Flowcharts
<img src="Images/Flowchart1.png" alt="Alt Text" width="300">  <img src="Images/Flowchart2.png" alt="Alt Text" width="300">  <img src="Images/Flowchart3.png" alt="Alt Text" width="300">

### Build: (main.py)
```Python
#--- Imports ---
import os # Used for editing the terminal view
import random # Allows for randomness between different runs
import time # Allows for more interactive UI by incorperating time
import json # Used for saving
import math # Used to calculate events
from wcwidth import wcswidth # Used to handle the Emoji and Ascii problems
from functools import partial 



#--- Classes ---
class Player():
    '''This class is used to create the Player information system, and is designed to be adaptive, allowing for different save files to be loaded, and unloaded'''
    def __init__(self, Save):
        '''Loads the Player data from the Save file (Which is a Dictionary)'''
        self.Player_Name = Save['Player_Name'] # Loads Player Name from Save file

        self.Health = {'Health': Save['Health']['Health'], 'Max_Health': Save['Health']['Max_Health']} # Loads Health and Max Health into a dictionary
        self.Stamina = {'Stamina': Save['Stamina']['Stamina'], 'Max_Stamina': Save['Stamina']['Max_Stamina']} # Loads Stamina and Max Stamina into a dictionary
        self.Mana = {'Mana': Save['Mana']['Mana'], 'Max_Mana': Save['Mana']['Max_Mana']} # Loads Mana and Max Mana into a dictionary

        self.WeaponSlot = Save['WeaponSlot'] # Loads Weapon from the Save File
        self.HelmetSlot = Save['HelmetSlot'] # Loads the Helmet from the Save File
        self.ChestplateSlot = Save['ChestplateSlot'] # Loads the Chestplate from the Save file
        self.BootSlot = Save['BootSlot'] # Loads the Boot from the Chestplate

        self.OtherSlot1 = {'Item': Save['OtherSlot1']['Item'], 'Qty': Save['OtherSlot1']['Qty']} # Loads the Item and Qty from save file for Save File 1
        self.OtherSlot2 = {'Item': Save['OtherSlot2']['Item'], 'Qty': Save['OtherSlot2']['Qty']} # Loads the Item and Qty from save file for Save File 2
        self.OtherSlot3 = {'Item': Save['OtherSlot3']['Item'], 'Qty': Save['OtherSlot3']['Qty']} # Loads the Item and Qty from save file for Save File 3
        self.OtherSlot4 = {'Item': Save['OtherSlot4']['Item'], 'Qty': Save['OtherSlot4']['Qty']} # Loads the Item and Qty from save file for Save File 4
        
        self.Location = Save['Location'] # Loads the Player Location
        self.Gold = Save['Gold'] # Loads the Player Gold

        self.Enemy1 = Save['Enemy1'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy2 = Save['Enemy2'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy3 = Save['Enemy3'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy4 = Save['Enemy4'] # Loads wether the player has been in room for a more adaptive story 
        self.Village1 = Save['Village1'] # Loads wether the player has been in room for a more adaptive story 
        self.Village2 = Save['Village2'] # Loads wether the player has been in room for a more adaptive story 
        self.Village3 = Save['Village3'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest1 = Save['Forest1'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest2 = Save['Forest2'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest3 = Save['Forest3'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest4 = Save['Forest4'] # Loads wether the player has been in room for a more adaptive story 
        self.SeenW1 = Save['SeenW1'] # Loads wether the player has been in room for a more adaptive story 
        self.SeenW2 = Save['SeenW2'] # Loads wether the player has been in room for a more adaptive story 
        self.Wizard1 = Save['Wizard1'] # Loads wether the player has been in room for a more adaptive story 
        self.Wizard2 = Save['Wizard2'] # Loads wether the player has been in room for a more adaptive story 
        self.Mountain = Save['Mountain'] # Loads wether the player has been in room for a more adaptive story 
        self.GoblinKing = Save['GoblinKing'] # Loads wether the player has been in room for a more adaptive story 
        self.RareFlower = Save['RareFlower'] # Loads wether the player has obtained the Flower
        self.RareRune = Save['RareRune'] # Loads wether the player has obtained the Rune

        self.Enemies = {'G': Save['Enemies']['G'], 'O': Save['Enemies']['O'], 'D': Save['Enemies']['D'], 'Og': Save['Enemies']['Og']} # Loads the Health of Each Enemy

        Load_Enemies(Save['Enemies']['G'], Save['Enemies']['O'], Save['Enemies']['D'], Save['Enemies']['Og']) # Loads the Enemies into the System, with the health files

    def Save(self, Save):
        '''Transfers the Information from the Save File into the JSON File'''

        Player_Stats = { # Creates a Dictionary of the Data
            'Player_Name': self.Player_Name, # Loads Player Name from the Player Attributes
            'Health': self.Health, # Loads the Player Health Dictionary from Player Attributes, making it contain both player Health and Max Health
            'Stamina': self.Stamina, # Loads the Player Stamina Dictionary from Player Attributes, making it contain both player Stamina and Max Stamina
            'Mana': self.Mana, # Loads the Player Mana Dictionary from Player Attributes, making it contain both player Mana and Max Mana
            'WeaponSlot': {'Name': self.WeaponSlot.name, 'Level': self.WeaponSlot.level, 'Multiplyers': self.WeaponSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Weapon
            'HelmetSlot': {'Name': self.HelmetSlot.name, 'Level': self.HelmetSlot.level, 'Multiplyers': self.HelmetSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Helmet
            'ChestplateSlot': {'Name': self.ChestplateSlot.name, 'Level': self.ChestplateSlot.level, 'Multiplyers': self.ChestplateSlot.multiplyers},  # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Chestplate
            'BootSlot': {'Name': self.BootSlot.name, 'Level': self.BootSlot.level, 'Multiplyers': self.BootSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Boots
            'OtherSlot1': {'Item': self.OtherSlot1['Item'].name, 'Qty': self.OtherSlot1['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot2': {'Item': self.OtherSlot2['Item'].name, 'Qty': self.OtherSlot2['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot3': {'Item': self.OtherSlot3['Item'].name, 'Qty': self.OtherSlot3['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot4': {'Item': self.OtherSlot4['Item'].name, 'Qty': self.OtherSlot4['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'Location': self.Location, # Stores The Player Location
            'Gold': self.Gold, # Stores the Players amount of Gold

            'Enemy1': self.Enemy1, # Stores Whether the Player has been in the Room
            'Enemy2': self.Enemy2, # Stores Whether the Player has been in the Room
            'Enemy3': self.Enemy3, # Stores Whether the Player has been in the Room
            'Enemy4': self.Enemy4, # Stores Whether the Player has been in the Room

            'Village1': self.Village1, # Stores Whether the Player has been in the Room
            'Village2': self.Village2, # Stores Whether the Player has been in the Room
            'Village3': self.Village3, # Stores Whether the Player has been in the Room

            'Forest1': self.Forest1, # Stores Whether the Player has been in the Room
            'Forest2': self.Forest2, # Stores Whether the Player has been in the Room
            'Forest3': self.Forest3, # Stores Whether the Player has been in the Room
            'Forest4': self.Forest4, # Stores Whether the Player has been in the Room

            'SeenW1': self.SeenW1, # Stores Whether the Player has been in the Room
            'SeenW2': self.SeenW2, # Stores Whether the Player has been in the Room

            'Wizard1': self.Wizard1, # Stores Whether the Player has been in the Room
            'Wizard2': self.Wizard2, # Stores Whether the Player has been in the Room
            'Mountain': self.Mountain, # Stores Whether the Player has been in the Room
            'GoblinKing': self.GoblinKing, # Stores Whether the Player has been in the Room

            'RareFlower': self.RareFlower, # Stores Whether the Player has obtained the Rare Flower
            'RareRune': self.RareRune,# Stores Whether the Player has obtained the Rare Rune

            'Enemies': {'G': Goblin.health, 'O': Orc.health, 'D': Druid.health, 'Og': Ogre.health} # Stores the Enemy Health
        }

        with open(f'Save{Save}.json', 'w') as f: # Opens the JSON file attached to the Load File
            json.dump(Player_Stats, f) # Puts the Player Data into the JSON file

    def Attacking(self, Target):
        '''Allows the Player to Attack an Enemy, by Specifying which Enemy to Attack'''
        Target.Player_Attacked() # Runs the Player_Attacked Function of the specified Target

    def Attacked(self, Damage, Type):
        '''Calculates Damage of Enemy, based of of the Multipliers on the Players Armour'''
        try:
            self.Health['Health'] -= round(Damage / ((self.HelmetSlot.protection + self.ChestplateSlot.protection + self.BootSlot.protection) / 3) * ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3)) # Calculates the Protection based on factors such as Protection and Enchantment Levels

        except:
            self.Health['Health'] -= Damage

class Item():
    '''This class creates the Foundation for Creating Items in the Game'''
    def __init__(self, name, level):
        'This function initalises the Items Variables'
        self.name = name # Defines the Items Name
        self.level = level # Defines the Ites Level

class Weapons(Item):
    '''This Class outlines the basics for creating Weapons'''
    def __init__(self, name, level, type, damage, multiplyers=None): 
        '''This Function Inherits the Prarameters from Item, and adds Weapon Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.type = type # Defines the Weapon Type - i.e Sword, Axe, Mace
        self.damage = damage # Defines the Weapons Damage
        
        if multiplyers is None: # If Multipliers is Undefined - Not given when creating the Weapon
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1} # Sets Multiplers all to 1
        else:
            self.multiplyers = multiplyers # If Multiplers are given, uses the given ones

    def setmultiplyers(self, Multiplyers):
        '''This Function allows the setting of the Multiplers - Used to Enchant the Item'''
        self.multiplyers = Multiplyers # Sets the Multiplers

class Armour(Item):
    '''This Class outlines the basics for creating Armour'''
    def __init__(self, name, level, type, protection, multiplyers=None):
        '''This Function Inherits the Prarameters from Item, and adds Armour Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.type = type # Defines the Type of Armour - i.e Helmet, Chestplate, Boots
        self.protection = protection # Defines the Protection level of the Armour


        if multiplyers is None: # If Multipliers is Undefined - Not given when creating the Armour piece
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1} # Sets Multiplers all to 1
        else:
            self.multiplyers = multiplyers # If Multiplers are given, uses the given ones

    def setmultiplyers(self, Multiplyers):
        self.multiplyers = Multiplyers
            
class Potion(Item):
    '''This Class creates potions, and allows them to be made at different strengths, to impact the Player different stats'''
    def __init__(self, name, level, effect, strength):
        '''This Function Inherits the Prarameters from Item, and adds Potion Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.effect = effect # Defines the effect the Potion impacts - i.e Health, Stamina, Mana
        self.strength = strength # Defines the Strength of the Potion

    def Use_Potion(self, Target):
        '''This function allows the Potion to be Used'''
        getattr(Target, self.effect)[self.effect] += self.strength # Applies the Effect to the Target
        if getattr(Target, self.effect)[self.effect] > getattr(Target, self.effect)[f'Max_{self.effect}']: # If the Potion atted too much statistic compared to the Max...
            getattr(Target, self.effect)[self.effect] = getattr(Target, self.effect)[f'Max_{self.effect}'] # Brings the Health Back down to the Max Health

        # Remove potion from inventory after use
        for slot in [Target.OtherSlot1, Target.OtherSlot2, Target.OtherSlot3, Target.OtherSlot4]: # Finds Which slot Potion is In
            if slot['Item'] is self and slot['Qty'] > 0: # Item is in Slot, and the Quantity is More than 0
                slot['Qty'] -= 1 # Removes of from the Quantity
                if slot['Qty'] == 0: # If their is None left in the Slot
                    slot['Item'] = None_Item # Reverts Slot back to None_Item
                break # Stops looking for where the Item is

```python
# Enemy class: Handles enemy creation, stats, and combat logic
class Enemy():
    '''This Class Creates a Enemy System, that allows for the creation of Enemies, and Allows them to interact / attack other Players and Enemies'''
    def __init__(self, name, health, max_health, damage, type, level):
        '''Initializes enemy attributes: name, health, max_health, damage, type, and level'''
        self.name = name
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.type = type
        self.level = level

    def Attacking(self, Target):
        # Enemy attacks a target, calling their Attacked method
        Target.Attacked(self.damage, self.type)

    def Player_Attacked(self):
        # Handles logic when the player attacks this enemy
        self.health -= round(User.WeaponSlot.damage * User.WeaponSlot.multiplyers[self.type])

    def Attacked(self, Damage, Type):
        # Handles logic when this enemy is attacked, with elemental strengths/weaknesses
        if self.type == 'Fir' and Type == 'Wat': # Fire is weak to Water
            self.health -= round(Damage * 1.5)
        elif self.type == 'Wat' and Type == 'Fir': # Water is weak to Fire
            self.health -= round(Damage * 0.5)
        elif self.type == 'Nat' and Type == 'Fir': # Nature is weak to Fire
            self.health -= round(Damage * 1.5)
        elif self.type == 'Fir' and Type == 'Nat': # Fire is weak to Nature
            self.health -= round(Damage * 0.5)
        elif self.type == 'Wat' and Type == 'Nat': # Water is weak to Nature
            self.health -= round(Damage * 1.5)
        elif self.type == 'Nat' and Type == 'Wat': # Nature is weak to Water
            self.health -= round(Damage * 0.5)
        else:
            self.health -= round(Damage)

# Villager base class: Handles villager creation, profession, and inventory trading
class Villager:
    def __init__(self, name, profession):
        # Initializes villager name, profession, and items for sale
        self.name = name
        self.profession = profession
        self.items = {}

    def Inventory_Trading(self):
        '''Allows the user to purchase items from the villager'''
        os.system('cls') # Clears Screen

        # Print villager shop UI
        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     {self.profession:<38}|
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {str(User.Gold) + ' 🪙':<38}|
    +---------------------------------------------------------+
    ''')
        count = 1
        # Print table header for items
        print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
        for item in self.items.values():
            # Print each item with its cost and quantity
            print(f"|{count:<3}| {item['Item'].name:<30}   |   Cost: {item['Cost']:<4} 🪙    |   Qty: {item['Qty']:<10} |")
            print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
            count += 1

        # Calculate lines printed for clearing later
        lines_printed = (count * 2) + 1
        while True:
            try:
                # Prompt user for purchase input
                Puchase_Input = int(input('Enter the number of the item you want to purchase (0 to exit): '))
                if Puchase_Input == 0:
                    # Exit and clear lines
                    ClearLines(lines_printed + 1)
                    break
                elif 1 > Puchase_Input or Puchase_Input >= count:
                    print('Not a Valid Number')
                elif 1 <= Puchase_Input < count:
                    selected_item = list(self.items.values())[Puchase_Input - 1]
                    item = selected_item['Item']
                    if selected_item['Qty'] > 0:
                        if User.Gold >= selected_item['Cost']:
                            # Determine item type and assign to correct slot
                            goto_inventory = False
                            equipped = False
                            if isinstance(item, Weapons):
                                print(f"Equipped {item.name} to Weapon Slot (replacing {User.WeaponSlot.name}).")
                                User.WeaponSlot = item
                                equipped = True
                            elif isinstance(item, Armour):
                                if item.type == 'Helmet':
                                    print(f"Equipped {item.name} to Helmet Slot (replacing {User.HelmetSlot.name}).")
                                    User.HelmetSlot = item
                                    equipped = True
                                elif item.type == 'ChestPlate':
                                    print(f"Equipped {item.name} to Chestplate Slot (replacing {User.ChestplateSlot.name}).")
                                    User.ChestplateSlot = item
                                    equipped = True
                                elif item.type == 'Boot':
                                    print(f"Equipped {item.name} to Boot Slot (replacing {User.BootSlot.name}).")
                                    User.BootSlot = item
                                    equipped = True
                                else:
                                    print(f"Unknown armour type: {item.type}. Placing in inventory.")
                                    goto_inventory = True
                            else:
                                goto_inventory = True

                            # Handle inventory slots for non-equipment or full inventory
                            inventory_slots = [User.OtherSlot1, User.OtherSlot2, User.OtherSlot3, User.OtherSlot4]
                            found = False
                            replace_cancelled = False

                            if goto_inventory:
                                for slot in inventory_slots:
                                    if slot['Item'] is item:
                                        slot['Qty'] += 1
                                        found = True
                                        break
                                if not found:
                                    # Find first empty slot
                                    empty_slot = None
                                    for slot in inventory_slots:
                                        if slot['Item'].name == 'None':
                                            empty_slot = slot
                                            break
                                    if empty_slot:
                                        empty_slot['Item'] = item
                                        empty_slot['Qty'] = 1
                                    else:
                                        # No empty slot, prompt user to bin or cancel
                                        print("Your inventory is full. Choose an item to replace or cancel:")
                                        for idx, slot in enumerate(inventory_slots, 1):
                                            print(f"{idx}. {slot['Item'].name} (x{slot['Qty']})")
                                        print(f"{len(inventory_slots)+1}. Cancel purchase")
                                        while True:
                                            try:
                                                replace_choice = int(input("Enter number to replace or cancel: "))
                                                if 1 <= replace_choice <= len(inventory_slots):
                                                    slot = inventory_slots[replace_choice-1]
                                                    print(f"Replaced {slot['Item'].name} with {item.name}.")
                                                    slot['Item'] = item
                                                    slot['Qty'] = 1
                                                    break
                                                elif replace_choice == len(inventory_slots)+1:
                                                    print("Purchase cancelled.")
                                                    replace_cancelled = True
                                                    break
                                                else:
                                                    print("Invalid choice.")
                                            except ValueError:
                                                print("Invalid input.")
                            if not goto_inventory or not replace_cancelled:
                                # Complete purchase: decrement quantity and gold
                                selected_item['Qty'] -= 1
                                User.Gold -= selected_item['Cost']
                                print(f"You bought 1x {item.name} for {selected_item['Cost']} 🪙.")
                            else:
                                continue
                    else:
                        print("Sorry, this item is out of stock.")
                else:
                    print("You do not have enough gold to purchase this item.")
            except Exception:
                print("Invalid input. Please enter a number.")

# Brewer subclass: Sells potions with random cost and quantity
class Brewer(Villager):
    def __init__(self, name):
        super().__init__(name, 'Brewer')
        self.items = {
            'Health Potion': {'Item': random.choice([Health_Potion_Small, Health_Potion_Medium, Health_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(3, 12)},
            'Mana Potion': {'Item': random.choice([Mana_Potion_Small, Mana_Potion_Medium, Mana_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(3, 12)},
            'Stamina Potion': {'Item': random.choice([Stamina_Potion_Small, Stamina_Potion_Medium, Stamina_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(3, 12)}
        }

# SwordSmith subclass: Sells swords with random cost and quantity
class SwordSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'SwordSmith')
        self.items = {
            'Wooden Sword': {'Item': Wooden_Sword, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Sword': {'Item': Bronze_Sword, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Sword': {'Item': Iron_Sword, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Sword': {'Item': Platinum_Sword, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

# AxeSmith subclass: Sells axes with random cost and quantity
class AxeSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'AxeSmith')
        self.items = {
            'Wooden Axe': {'Item': Wooden_Axe, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Axe': {'Item': Bronze_Axe, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Axe': {'Item': Iron_Axe, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Axe': {'Item': Platinum_Axe, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

# MaceSmith subclass: Sells maces with random cost and quantity
class MaceSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'MaceSmith')
        self.items = {
            'Wooden Mace': {'Item': Wooden_Mace, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Mace': {'Item': Bronze_Mace, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Mace': {'Item': Iron_Mace, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Mace': {'Item': Platinum_Mace, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

# ArmourSmith subclass: Sells armor pieces with random cost and quantity
class ArmourSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'ArmourSmith')
        self.items = {
            'Leather Helmet': {'Item': Leather_Helmet, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Helmet': {'Item': Bronze_Helmet, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Helmet': {'Item': Iron_Helmet, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Helmet': {'Item': Platinum_Helmet, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Chestplate': {'Item': Leather_Chestplate, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Chestplate': {'Item': Bronze_Chestplate, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Chestplate': {'Item': Iron_Chestplate, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Chestplate': {'Item': Platinum_Chestplate, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Boot': {'Item': Leather_Boot, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Boot': {'Item': Bronze_Boot, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Boot': {'Item': Iron_Boot, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Boot': {'Item': Platinum_Boot, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

# Wizard subclass: Handles enchanting logic and quest progression
class Wizard(Villager):
    def __init__(self, name):
        super().__init__(name, 'Wizard')
    
    def WizardStore(self, Room):
        global User
        os.system('cls')
        if Room == 'Wizard1':
            if User.SeenW1 == False:
                # First visit: explain quest
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Their is a rare flower in the south forest, bring it to me, and I will help you enchant!
                    ''')
                User.SeenW1 = True
                input('     Enter to Continue...')
                PrintMainUI('Wizard1')
            elif User.SeenW1 == True and User.RareFlower == False:
                # Remind player to bring flower
                print("Have you Brought me my Flower Yet? It's in the South Forest")
                input('Enter to Continue...')
                PrintMainUI('Wizard1')
            elif User.RareFlower == True:
                # Allow enchanting if quest complete
                print()
                print('Thanks for bringing me my flower, what can I help you enchant today?')
                enchanted_item = {'item': None}
                def make_enchant_lambda(slot):
                    return lambda: slot.setmultiplyers(Enchantment(slot))
                options = {
                    User.WeaponSlot.name: make_enchant_lambda(User.WeaponSlot)
                }
                if User.HelmetSlot.name != "None_Helmet":
                    options[User.HelmetSlot.name] = make_enchant_lambda(User.HelmetSlot)
                if User.ChestplateSlot.name != "None_Chestplate":
                    options[User.ChestplateSlot.name] = make_enchant_lambda(User.ChestplateSlot)
                if User.BootSlot.name != "None_Boot":
                    options[User.BootSlot.name] = make_enchant_lambda(User.BootSlot)
                options['Exit'] = lambda: PrintMainUI('Wizard1')
                Input_Selection(options)
                # Print enchanted item multipliers if any
                item = enchanted_item['item']
                if item is not None:
                    print(f"You enchanted: {item.name}")
                    print("New multipliers:")
                    for key, value in item.multiplyers.items():
                        print(f"  {key}: {value:.2f}")

        elif Room == 'Wizard2':
            if User.SeenW2 == False:
                # First visit: explain rune quest
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Up in the high mountains of Sorvo, their is an ancient rune, ensribed with ancient information.
            Bring it to me, and I will help you enchant!
                    ''')
                User.SeenW2 = True
                input('     Enter to Continue...')
                PrintMainUI('Wizard2')
            elif User.SeenW2 == True and User.RareRune == False:
                # Remind player to bring rune
                print("Have you Brought me my RareRune Yet? It's in the high mountains of Sorvo")
                input('Enter to Continue...')
                PrintMainUI('Wizard2')
            elif User.RareRune == True:
                # Allow enchanting if quest complete
                print()
                print('Thanks for bringing me my Rune, what can I help you enchant today?')
                enchanted_item = {'item': None}
                def make_enchant_lambda(slot):
                    return lambda: slot.setmultiplyers(Enchantment(slot))
                options = {
                    User.WeaponSlot.name: make_enchant_lambda(User.WeaponSlot)
                }
                if User.HelmetSlot.name != "None_Helmet":
                    options[User.HelmetSlot.name] = make_enchant_lambda(User.HelmetSlot)
                if User.ChestplateSlot.name != "None_Chestplate":
                    options[User.ChestplateSlot.name] = make_enchant_lambda(User.ChestplateSlot)
                if User.BootSlot.name != "None_Boot":
                    options[User.BootSlot.name] = make_enchant_lambda(User.BootSlot)
                options['Exit'] = lambda: PrintMainUI('Wizard2')
                Input_Selection(options)
                # Print enchanted item multipliers if any
                item = enchanted_item['item']
                if item is not None:
                    print(f"You enchanted: {item.name}")
                    print("New multipliers:")
                    for key, value in item.multiplyers.items():
                        print(f"  {key}: {value:.2f}")

                # Display summary table of all equipped item multipliers
                print(f'''
        +---+{'-'*39}+- Wat -+- Fir -+- Nat -+
        | 1 | Weapon Slot:     {User.WeaponSlot.name:<20} | {User.WeaponSlot.multiplyers['Wat']:<3.3f} | {User.WeaponSlot.multiplyers['Fir']:<3.3f} | {User.WeaponSlot.multiplyers['Nat']:<3.3f} |
        | 2 | Helmet Slot:     {User.HelmetSlot.name:<20} | {User.HelmetSlot.multiplyers['Wat']:<3.3f} | {User.HelmetSlot.multiplyers['Fir']:<3.3f} | {User.HelmetSlot.multiplyers['Nat']:<3.3f} |
        | 3 | Chestplate Slot: {User.ChestplateSlot.name:<20} | {User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
        | 4 | Boot Slot:       {User.BootSlot.name:<20} | {User.BootSlot.multiplyers['Wat']:<3.3f} | {User.BootSlot.multiplyers['Fir']:<3.3f} | {User.BootSlot.multiplyers['Nat']:<3.3f} |
        +---+{'-'*39}+-------+-------+-------+''')
                input('Enter to Continue...')

                
class LumberJack(Villager):
    def __init__(self, name):
        super().__init__(name, 'LumberJack')

    def ChopWood(self):
        os.system('cls') # Clears the Screen

        # Tells the User the Amount of gold they have, and the Villager Statistics
        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     Lumberjack                            |
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {str(User.Gold) + ' 🪙':<38}|
    +---------------------------------------------------------+

    You can Earn extra money for equipment!
''')
        print('Chop Wood!')
        for i in range(0, 5): # Run 5 Times
            print() # Creates a Spacer in the Terminal
            print('CHOP') # Prints 'Chop' to Symbolise Something Happend
            print() # Creates a Spacer in the Terminal
            time.sleep(random.randint(10, 20) / 10) # Waites Between 1 and 2 seconds
        print('Good Job, Heres a piece of Gold!') # Tells the User they have earnt a piuce of Gold
        User.Gold += 1 # Gives the User a Piece of Gold
        
        input('Enter to Continue...') # Waits for the User to Continue

class Gambler(Villager):
    def __init__(self, name):
        super().__init__(name, 'Gambler')

    def Casino(self):
        '''This Fuction runs the Casino, allowing the User to make more money'''
        CasinoNumber = random.randint(1,5) # Picks Random Number between 1 and 5

        print("Welcome to the Casino") # Welcomes User
        print() # Creates a Spacer in the Terminal
        print("If you win you'll get 5 times what you put in, if you lose, we just keep what you bet") # Explains the Game
        print() # Creates a Spacer in the Terminal

        while True: # Until Broken
            try: # Try to Recieve Input
                Betting = int(input(f"How Much Gold would you Like to Bet? (0 to Not Bet) Current Balance: {User.Gold} ")) # Asks for How much the User wants to bet
                if Betting > User.Gold or Betting < 0: # If Betting Amount it outside of Acceptable Rand
                    print("You don't have that Much Gold") # Prints Error Message
                else: # If User Input is Correct
                    break # Breaks Loop
            except: # If Error with Input
                print("Invalid input. Please enter a number.") # Prints error Message

        while True: # Until Broken
            try: # Try to Recieve Input
                Guess = int(input("Put your Bet on a Number 1-5 ")) # Asks User to Guess a Number
                if 1 <= Guess <= 5: # if Guess is In Acceptable Range
                    break # Break Loop
                else: # If not in Acceptable Range
                    print('Not an Option') # Alert the Player it is not an option
            except: # If error with Input
                print("Invalid input. Please enter a number between 1 and 5.") # Prints error Message

        if Guess == CasinoNumber: # If Player Guesses Right
            User.Gold += 4*Betting # Multiply Betting Amount by 4 (Its Multiplied by 4 because It hasnt actually removed any Gold Yet) and is added to User.Gold

        else: # If Player Guesses Wrong
            print("It'll seem you've lost, maybe next time you'll think twice about going up against the house") # Tells the User they Guessed Wrong
            User.Gold -= Betting # Removes the Betting Amount from the Users Gold

        print() # Creates a Spacer in the Terminal
        print(f"The Number was: {CasinoNumber}") # Tells the Player what it was
        print() # Creates a Spacer in the Terminal
        print(f"Current Balence: {User.Gold}") # Tells the Player their Current Gold Amount

        input('Enter to Continue...') # Waits to Continue

def Load_Items(Name, Level, Multipliers): # Converts simplified JSON data back into full Item objects for use in the program
    '''Since JSON's cant store Items, This function converts the data JSON's can store, and convert it back into the Item Form for the program'''
    
    #--- Weapons ---
    if Name == 'Stick': # If the stored item is Stick
        return Weapons('Stick', Level, 'Stick', 2, Multipliers) # Return a Stick, with the saved Level and Multipliers
    
    elif Name == 'Wooden_Sword': # If the stored item is Wooden_Sword
        return Weapons('Wooden_Sword', Level, 'Sword', 4, Multipliers) # Return a Wooden Sword, with saved Level and Multipliers
    elif Name == 'Bronze_Sword': # If the stored item is Bronze_Sword
        return Weapons('Bronze_Sword', Level, 'Sword', 5, Multipliers) # Return a Bronze Sword, with saved Level and Multipliers
    elif Name == 'Iron_Sword': # If the stored item is Iron_Sword
        return Weapons('Iron_Sword', Level, 'Sword', 6, Multipliers) # Return an Iron Sword, with saved Level and Multipliers
    elif Name == 'Platinum_Sword': # If the stored item is Platinum_Sword
        return Weapons('Platinum_Sword', Level, 'Sword', 8, Multipliers) # Return a Platinum Sword, with saved Level and Multipliers

    elif Name == 'Wooden_Axe': # If the stored item is Wooden_Axe
        return Weapons('Wooden_Axe', Level, 'Axe', 4, Multipliers) # Return a Wooden Axe, with saved Level and Multipliers
    elif Name == 'Bronze_Axe': # If the stored item is Bronze_Axe
        return Weapons('Bronze_Axe', Level, 'Axe', 5, Multipliers) # Return a Bronze Axe, with saved Level and Multipliers
    elif Name == 'Iron_Axe': # If the stored item is Iron_Axe
        return Weapons('Iron_Axe', Level, 'Axe', 6, Multipliers) # Return an Iron Axe, with saved Level and Multipliers
    elif Name == 'Platinum_Axe': # If the stored item is Platinum_Axe
        return Weapons('Platinum_Axe', Level, 'Axe', 8, Multipliers) # Return a Platinum Axe, with saved Level and Multipliers

    elif Name == 'Wooden_Mace': # If the stored item is Wooden_Mace
        return Weapons('Wooden_Mace', Level, 'Mace', 4, Multipliers) # Return a Wooden Mace, with saved Level and Multipliers
    elif Name == 'Bronze_Mace': # If the stored item is Bronze_Mace
        return Weapons('Bronze_Mace', Level, 'Mace', 5, Multipliers) # Return a Bronze Mace, with saved Level and Multipliers
    elif Name == 'Iron_Mace': # If the stored item is Iron_Mace
        return Weapons('Iron_Mace', Level, 'Mace', 6, Multipliers) # Return an Iron Mace, with saved Level and Multipliers
    elif Name == 'Platinum_Mace': # If the stored item is Platinum_Mace
        return Weapons('Platinum_Mace', Level, 'Mace', 8, Multipliers) # Return a Platinum Mace, with saved Level and Multipliers

    #--- Armour ---
    elif Name == 'None_Helmet': # If no helmet is equipped
        return Armour('None_Helmet', 0, 'Helmet', 0, Multipliers) # Return a default empty Helmet
    elif Name == 'Leather_Helmet': # If the stored item is Leather_Helmet
        return Armour('Leather_Helmet', Level, 'Helmet', 1, Multipliers) # Return a Leather Helmet, with saved Level and Multipliers
    elif Name == 'Bronze_Helmet': # If the stored item is Bronze_Helmet
        return Armour('Bronze_Helmet', Level, 'Helmet', 2, Multipliers) # Return a Bronze Helmet, with saved Level and Multipliers
    elif Name == 'Iron_Helmet': # If the stored item is Iron_Helmet
        return Armour('Iron_Helmet', Level, 'Helmet', 3, Multipliers) # Return an Iron Helmet, with saved Level and Multipliers
    elif Name == 'Platinum_Helmet': # If the stored item is Platinum_Helmet
        return Armour('Platinum_Helmet', Level, 'Helmet', 4, Multipliers) # Return a Platinum Helmet, with saved Level and Multipliers

    elif Name == 'None_Chestplate': # If no chestplate is equipped
        return Armour('None_Chestplate', 0, 'ChestPlate', 0, Multipliers) # Return a default empty ChestPlate
    elif Name == 'Leather_Chestplate': # If the stored item is Leather_Chestplate
        return Armour('Leather_Chestplate', Level, 'ChestPlate', 1, Multipliers) # Return a Leather Chestplate, with saved Level and Multipliers
    elif Name == 'Bronze_Chestplate': # If the stored item is Bronze_Chestplate
        return Armour('Bronze_Chestplate', Level, 'ChestPlate', 2, Multipliers) # Return a Bronze Chestplate, with saved Level and Multipliers
    elif Name == 'Iron_Chestplate': # If the stored item is Iron_Chestplate
        return Armour('Iron_Chestplate', Level, 'ChestPlate', 3, Multipliers) # Return an Iron Chestplate, with saved Level and Multipliers
    elif Name == 'Platinum_Chestplate': # If the stored item is Platinum_Chestplate
        return Armour('Platinum_Chestplate', Level, 'ChestPlate', 4, Multipliers) # Return a Platinum Chestplate, with saved Level and Multipliers

    elif Name == 'None_Boot': # If no boots are equipped
        return Armour('None_Boot', 0, 'Boot', 0, Multipliers) # Return default empty Boots
    elif Name == 'Leather_Boot': # If the stored item is Leather_Boot
        return Armour('Leather_Boot', Level, 'Boot', 1, Multipliers) # Return Leather Boots, with saved Level and Multipliers
    elif Name == 'Bronze_Boot': # If the stored item is Bronze_Boot
        return Armour('Bronze_Boot', Level, 'Boot', 2, Multipliers) # Return Bronze Boots, with saved Level and Multipliers
    elif Name == 'Iron_Boot': # If the stored item is Iron_Boot
        return Armour('Iron_Boot', Level, 'Boot', 3, Multipliers) # Return Iron Boots, with saved Level and Multipliers
    elif Name == 'Platinum_Boot': # If the stored item is Platinum_Boot
        return Armour('Platinum_Boot', Level, 'Boot', 4, Multipliers) # Return Platinum Boots, with saved Level and Multipliers

    #--- Items/Potions ---
    elif Name == 'None': # If slot is empty or nothing equipped
        return Item('None', 0) # Return a basic empty item

    elif Name == 'Health_Potion_Small': # If the stored item is Health_Potion_Small
        return Potion('Health_Potion_Small', Level, 'Health', 10) # Return a small health potion healing 10
    elif Name == 'Health_Potion_Medium': # If the stored item is Health_Potion_Medium
        return Potion('Health_Potion_Medium', Level, 'Health', 25) # Return a medium health potion healing 25
    elif Name == 'Health_Potion_Large': # If the stored item is Health_Potion_Large
        return Potion('Health_Potion_Large', Level, 'Health', 50) # Return a large health potion healing 50

    elif Name == 'Stamina_Potion_Small': # If the stored item is Stamina_Potion_Small
        return Potion('Stamina_Potion_Small', Level, 'Stamina', 10) # Return a small stamina potion restoring 10
    elif Name == 'Stamina_Potion_Medium': # If the stored item is Stamina_Potion_Medium
        return Potion('Stamina_Potion_Medium', Level, 'Stamina', 25) # Return a medium stamina potion restoring 25
    elif Name == 'Stamina_Potion_Large': # If the stored item is Stamina_Potion_Large
        return Potion('Stamina_Potion_Large', Level, 'Stamina', 50) # Return a large stamina potion restoring 50

    elif Name == 'Mana_Potion_Small': # If the stored item is Mana_Potion_Small
        return Potion('Mana_Potion_Small', Level, 'Mana', 10) # Return a small mana potion restoring 10
    elif Name == 'Mana_Potion_Medium': # If the stored item is Mana_Potion_Medium
        return Potion('Mana_Potion_Medium', Level, 'Mana', 25) # Return a medium mana potion restoring 25
    elif Name == 'Mana_Potion_Large': # If the stored item is Mana_Potion_Large
        return Potion('Mana_Potion_Large', Level, 'Mana', 50) # Return a large mana potion restoring 50

    else: # If item name is not recognized
        return None_Item # Return a fallback None_Item object

def Load_Enemies(G, O, D, Og):
    '''Since JSON files cant store classes, this function loads variable Enemy data into the Enemy'''
    global Goblin, Orc, Druid, Ogre # Globalises the Enemies
    Goblin = Enemy('Goblin', G, 10, 5, 'Fir', 1) # Creates Goblin with the Saved Health Attribute
    Orc = Enemy('Orc', O, 20, 7, 'Wat', 8) # Creates Orc with the Saved Health Attribute
    Druid = Enemy('Druid', D, 20, 12, 'Nat', 16) # Creates Druid with the Saved Health Attribute
    Ogre = Enemy('Ogre', Og, 50, 10, 'Fir', 20) # Creates Ogre with the Saved Health Attribute

#--- Variables ---
User = None # Creates the User Tag

Load_File = 0 # Predefines the Load File to be 0 - No Load_File

#--- Items ---
Stick = Weapons('Stick', 1, 'Stick', 2) # Creates a Weapon named Stick that does 2 damage

# Swords
Wooden_Sword = Weapons('Wooden_Sword', 3, 'Sword', 4) # Creates a Sword named Wooden_Sword that does 4 damage
Bronze_Sword = Weapons('Bronze_Sword', 6, 'Sword', 5) # Creates a Sword named Bronze_Sword that does 5 damage
Iron_Sword = Weapons('Iron_Sword', 12, 'Sword', 6) # Creates a Sword named Iron_Sword that does 6 damage
Platinum_Sword = Weapons('Platinum_Sword', 16, 'Sword', 8) # Creates a Sword named Platinum_Sword that does 8 damage

# Axes
Wooden_Axe = Weapons('Wooden_Axe', 3, 'Axe', 4) # Creates an Axe named Wooden_Axe that does 4 damage
Bronze_Axe = Weapons('Bronze_Axe', 6, 'Axe', 5) # Creates an Axe named Bronze_Axe that does 5 damage
Iron_Axe = Weapons('Iron_Axe', 12, 'Axe', 6) # Creates an Axe named Iron_Axe that does 6 damage
Platinum_Axe = Weapons('Platinum_Axe', 16, 'Axe', 8) # Creates an Axe named Platinum_Axe that does 8 damage

# Maces
Wooden_Mace = Weapons('Wooden_Mace', 3, 'Mace', 4) # Creates a Mace named Wooden_Mace that does 4 damage
Bronze_Mace = Weapons('Bronze_Mace', 6, 'Mace', 5) # Creates a Mace named Bronze_Mace that does 5 damage
Iron_Mace = Weapons('Iron_Mace', 12, 'Mace', 6) # Creates a Mace named Iron_Mace that does 6 damage
Platinum_Mace = Weapons('Platinum_Mace', 16, 'Mace', 8) # Creates a Mace named Platinum_Mace that does 8 damage

#--- Armour ---
# Helmet
None_Helmet = Armour('None_Helmet', 0, 'Helmet', 0) # Creates a Helmet named None_Helmet that provides 0 protection
Leather_Helmet = Armour('Leather_Helmet', 1, 'Helmet', 1) # Creates a Helmet named Leather_Helmet that provides 1 protection
Bronze_Helmet = Armour('Bronze_Helmet', 3, 'Helmet', 2) # Creates a Helmet named Bronze_Helmet that provides 2 protection
Iron_Helmet = Armour('Iron_Helmet', 6, 'Helmet', 3) # Creates a Helmet named Iron_Helmet that provides 3 protection
Platinum_Helmet = Armour('Platinum_Helmet', 10, 'Helmet', 4) # Creates a Helmet named Platinum_Helmet that provides 4 protection

# ChestPlate
None_Chestplate = Armour('None_Chestplate', 0, 'ChestPlate', 0) # Creates a ChestPlate named None_Chestplate that provides 0 protection
Leather_Chestplate = Armour('Leather_Chestplate', 1, 'ChestPlate', 1) # Creates a ChestPlate named Leather_Chestplate that provides 1 protection
Bronze_Chestplate = Armour('Bronze_Chestplate', 3, 'ChestPlate', 2) # Creates a ChestPlate named Bronze_Chestplate that provides 2 protection
Iron_Chestplate = Armour('Iron_Chestplate', 6, 'ChestPlate', 3) # Creates a ChestPlate named Iron_Chestplate that provides 3 protection
Platinum_Chestplate = Armour('Platinum_Chestplate', 10, 'ChestPlate', 4) # Creates a ChestPlate named Platinum_Chestplate that provides 4 protection

# Boot
None_Boot = Armour('None_Boot', 0, 'Boot', 0) # Creates a Boot named None_Boot that provides 0 protection
Leather_Boot = Armour('Leather_Boot', 1, 'Boot', 1) # Creates a Boot named Leather_Boot that provides 1 protection
Bronze_Boot = Armour('Bronze_Boot', 3, 'Boot', 2) # Creates a Boot named Bronze_Boot that provides 2 protection
Iron_Boot = Armour('Iron_Boot', 6, 'Boot', 3) # Creates a Boot named Iron_Boot that provides 3 protection
Platinum_Boot = Armour('Platinum_Boot', 10, 'Boot', 4) # Creates a Boot named Platinum_Boot that provides 4 protection

# Items
None_Item = Item('None', 0) # Creates an Item named None

# Potions
Health_Potion_Small = Potion('Health_Potion_Small', 1, 'Health', 10) # Creates a Potion named Health_Potion_Small that replenishes 10 Health
Health_Potion_Medium = Potion('Health_Potion_Medium', 3, 'Health', 25) # Creates a Potion named Health_Potion_Medium that replenishes 25 Health
Health_Potion_Large = Potion('Health_Potion_Large', 5, 'Health', 50) # Creates a Potion named Health_Potion_Large that replenishes 50 Health

Stamina_Potion_Small = Potion('Stamina_Potion_Small', 1, 'Stamina', 10) # Creates a Potion named Stamina_Potion_Small that replenishes 10 Stamina
Stamina_Potion_Medium = Potion('Stamina_Potion_Medium', 3, 'Stamina', 25) # Creates a Potion named Stamina_Potion_Medium that replenishes 25 Stamina
Stamina_Potion_Large = Potion('Stamina_Potion_Large', 5, 'Stamina', 50) # Creates a Potion named Stamina_Potion_Large that replenishes 50 Stamina

Mana_Potion_Small = Potion('Mana_Potion_Small', 1, 'Mana', 10) # Creates a Potion named Mana_Potion_Small that replenishes 10 Mana
Mana_Potion_Medium = Potion('Mana_Potion_Medium', 3, 'Mana', 25) # Creates a Potion named Mana_Potion_Medium that replenishes 25 Mana
Mana_Potion_Large = Potion('Mana_Potion_Large', 5, 'Mana', 50) # Creates a Potion named Mana_Potion_Large that replenishes 50 Mana

#--- Functions ---
# Combat
def Combat(Enemy, Room):
    '''This Function handles the Combat between the Player and an Enemy'''
    global Exited, User  # Uses the Global Exited Variable

    def Attack():
        User.Attacking(Enemy)

    if Enemy.type == 'Fir':  # If the Enemy is Fire Type
        Type = 'Fire'  # Set Type to Fire
    elif Enemy.type == 'Wat':  # If the Enemy is Water Type
        Type = 'Water'  # Set Type to Water
    elif Enemy.type == 'Nat':  # If the Enemy is Nature Type
        Type = 'Nature'  # Set Type to Nature

    print(f"You have Encountered a {Enemy.name}")  # Informs the Player of the Enemy they have encountered

    while True:  # Runs the Combat Loop until someone wins or loses
        Exited = False  # Reset Exited at the start of each loop
        print(f"""
    +-----------------------------------------------+
    |{' '*21}Enemy{' '*21}|
    +-----------------------------------------------+
    {Enemy.name}: 
        Health:  ♥️  \033[31m{StatBar(Enemy.health, Enemy.max_health)} ({Enemy.health}/{Enemy.max_health})
        Damage:  ⚔️  \033[34m{Enemy.damage}\033[0m
        Type:    ☯️  \033[33m{Type}\033[0m

    {User.Player_Name}:
        Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} ({User.Health['Health']}/{User.Health['Max_Health']})
        Damage:  ⚔️  \033[34m{User.WeaponSlot.damage}\033[0m
        Elemental Damage:        ☯️  \033[33m{User.WeaponSlot.multiplyers[Enemy.type]}\033[0m
        Elemental Protection:    ☯️  \033[33m{round((User.HelmetSlot.multiplyers[Enemy.type] + User.ChestplateSlot.multiplyers[Enemy.type] + User.BootSlot.multiplyers[Enemy.type]) / 3)}\033[0m
        """) # Displays Full Combat UI with Stats for Both the Player and Enemy

        if Enemy.health <= 0:  # If the Enemy has run out of Health
            ClearLines(17)  # Clears the Combat UI
            print(f"You have defeated the {Enemy.name}!")  # Informs the Player they won
            User.WeaponSlot.level += Enemy.level / 2  # Increases the Weapon Level by Half the Enemy Level
            input("Press Enter to continue...")
            ClearLines(1)
            break  # Breaks the Loop

        elif User.Health['Health'] <= 0:  # If the Player has run out of Health
            Died(Enemy.name)
            break

        Input_Selection({
            "Attack": lambda: Attack(),  # Attacks the Enemy
            "Use Item": lambda: DisplayInventoryScreen()  # Opens Inventory to Use Items
        })

            # After using an item, Exited may be set to True, so check before enemy attacks
        if Exited:
            pass
        else:
            Enemy.Attacking(User)  # The Enemy Attacks the Player

        ClearLines(20)  # Clears the Combat UI before Refreshing

# UI
def PrintMainUI(Room):
    '''This Function combines a variety of other functions - and Displays them in the correct way'''
    Exited = False # Sets Exited to False
    os.system('cls') # Clears the Screen
    
    if User.Health['Health'] <= 0: # If the User has ran out of Health
        Died('No Health') # Run the Player has Died due to No health
    elif User.Stamina['Stamina'] <= 0: # If the User has ran out of Stamina
        Died('No Stamina') # Run the Player has Died due to No Stamina
    
    User.Location = Room # Sets the Users Location to be the Current Room    

    map_lines = Map(Room).splitlines() # Splits the Lines from Map
    stats_lines = DisplayStats().splitlines() # Splits the Lines for Stats
    inventory_lines = DisplayInventory().splitlines() # Splits the Lines for Player Inventory
    MapKey_lines = DisplayMapKey().splitlines() # Splits the Line from Map Key

    side_panel = stats_lines + inventory_lines + MapKey_lines # Combines the Lines of each of the elements to be printed on the Side Panel
    max_lines = max(len(map_lines), len(side_panel)) # Calculates which is the Tallest (Map or Side Panel)

    print() # Creates a Spacer in the Terminal

    for i in range(max_lines): # For each line in (Which ever Element had more Lines)
        map_line = map_lines[i] if i < len(map_lines) else "" # Figures out if their is content in the Lines - Else: Sets it to be a Blank line - But a Line that Exists
        side_line = side_panel[i] if i < len(side_panel) else "" # Figures out if their is content in the Lines - Else: Sets it to be a Blank line - But a Line that Exists

        map_width = wcswidth(map_line) # Calculates the Width of the Map line (Accounting for Emojis)
        padding = max(0, 60 - map_width) # Calculates if the Map is Square - If Not - Adds padding
        print(map_line + ' ' * padding + side_line) # Prints the Map Line, then the Padding, then the Side panel line
    
    print() # Creates a Spacer in the Terminal

    print(Story(Room)) # Prints the Story for the Room
    
    print() # Creates a Spacer in the Terminal
    while True: # Run until broken
        if Exited == False: # If player has Exited
            setattr(User, Room, True) # Set the Room variable for the Player to be True
            Input_Selection(MoveOptions(Room)) # Runs the Input selection for the Room - Based on the Options from MoveOptions
            ClearLines(len(MoveOptions(Room))+3)
            
        else: # If their is a Problem - Breaks the Loop to stop a crash
            break # Breaks the Loop

def StatBar(Stat, Max_Stat):
    '''This function create statbars for statisics'''
    StatBar = (math.floor(Stat/(Max_Stat/10)))*'█' # Calculates how much health their is based on the Stat and Max Stat
    DeadBar = '' # Initalises 'Dead Bar'

    if StatBar == '' and Stat > 0: # Because it rounds down, if the player is alive, but has below 10% health...
        StatBar = '█' # Gives them 1 block of health

    elif len(StatBar) > 10: # If Health is more than 10
        Statbar = '█'*10 # Sets Stat bar to Full
        return Statbar
        

    for i in range(0, 10-len(StatBar)): # Fills up the excess of statbar to Deadbar
        DeadBar += f'-' # Adds a '-' to DeadBar
        
    return StatBar + f'\033[37m{DeadBar}' # returns the completed Bar - Combines the two, and makes the 'Dead Bar' White

def DisplayStats():
    '''This function displates the Stats Block of the UI'''
    return f'''+───────────--==| Stats |==--───────────+
│                                       │
│   Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} \033[0m {f'({User.Health['Health']}/{User.Health['Max_Health']})':<12}│
│   Stamina: 🔋 \033[32m{StatBar(User.Stamina['Stamina'], User.Stamina['Max_Stamina'])} \033[0m {f'({User.Stamina['Stamina']}/{User.Stamina['Max_Stamina']})':<12}│
│   Mana:    {f'💠 \033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}' if MountainIssue == True else f'💠\033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}'}│
│                                       │
+───────────────────────────────────────+''' # The Mana function is different because that is what lines up with the Mountain and causes problems (More context in Map Comment)

def DisplayInventory():
    '''This function returns the Users Inventory in a Asethetic way'''
    return f'''+──────────────────────────────────--==| Inventory |==--──────────────────────────────────+
│   {'🪙  Gold':<12} -   {User.Gold:<68} │
│   {'Weapon':<12} -   {User.WeaponSlot.name:<25} {'Chestplate':<12} -   {User.ChestplateSlot.name:<25} │
│   {'Helmet':<12} -   {User.HelmetSlot.name:<25} {'Boots':<12} -   {User.BootSlot.name:<25} │
+{'─'*89}+ 
│   {User.OtherSlot1['Item'].name:<28} -   {User.OtherSlot1['Qty']:<9} {User.OtherSlot2['Item'].name:<28} -   {User.OtherSlot2['Qty']:<9} │
│   {User.OtherSlot3['Item'].name:<28} -   {User.OtherSlot3['Qty']:<9} {User.OtherSlot4['Item'].name:<28} -   {User.OtherSlot4['Qty']:<9} │
+{'─'*89}+'''

def DisplayMapKey():
    '''This function returns the Map key - Allowing the User to figure out which symbols mean what'''
    return f'''+─────────────────────────--==| Map Key |==--─────────────────────────+
│   ██ - You              🔮 - Wizard Tower                           │
│   🏠 - Village          💀 - Enemy             👑 - Goblin King     │
│   🌲 - Forest           🏔️  - Mountain                               │
+─────────────────────────────────────────────────────────────────────+'''

def DisplayInventoryScreen():
    global Exited

    def SetItemUsed():
        global Exited
        Exited = True

    print('''
    Which Item would you like to use?
    ''')
    
    options = {}
    for slot in [User.OtherSlot1, User.OtherSlot2, User.OtherSlot3, User.OtherSlot4]:
        item = slot['Item']
        if item.name != 'None':
            options[f"{item.name:<25} - ({slot['Qty']})"] = lambda item=item: item.Use_Potion(User)
    options['Exit'] = lambda: SetItemUsed()

    
    Input_Selection(options)
        
    ClearLines(6 + len(options))

def TitleScreen():
    '''This Function Handles Displaying and calculating what happens in the TitleScreen'''
    def OverWrite():
        '''This functions handles what to do if the User wants to Overwrite a Save file'''
        print('Which save do you you want to overwrite?') # Instructs the User
        print() # Creates a Spacer in the Terminal
        options = {} # Initalises the Options
        if Player_Data_1: # If Player_Data_1 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 1'] = lambda: (load({}, 1)) # Appends Save 1 to Option and starts creating a character with no attributes to save file 1

        elif Player_Data_2: # If Player_Data_2 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 2'] = lambda: (load({}, 2)) # Appends Save 2 to Option and starts creating a character with no attributes to save file 2

        elif Player_Data_3: # If Player_Data_3 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 3'] = lambda: (load({}, 3)) # Appends Save 3 to Option and starts creating a character with no attributes to save file 3
            
        elif Player_Data_4: # If Player_Data_4 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 4'] = lambda: (load({}, 4)) # Appends Save 4 to Option and starts creating a character with no attributes to save file 4

        options['Exit'] = lambda: TitleScreen() # Appends Exit to Option - Restarting back to Titlescreen

        Input_Selection(options) # Loads Options into Input Selection
                
    os.system('cls') # Clears Screen
    try: # Try to open Save 1 and Append it to Player_Data_1
        with open(f'Save1.json', 'r') as f:
            Player_Data_1 = json.load(f)
    except: # If JSON is blank, sets Player_Data_1 to a Blank Dictionary
        Player_Data_1 = {} # Sets to blank Dictionary
    
    try: # Try to open Save 2 and Append it to Player_Data_2
        with open(f'Save2.json', 'r') as f:
            Player_Data_2 = json.load(f)
    except: # If JSON is blank, sets Player_Data_2 to a Blank Dictionary
        Player_Data_2 = {} # Sets to blank Dictionary

    try: # Try to open Save 3 and Append it to Player_Data_3
        with open(f'Save3.json', 'r') as f:
            Player_Data_3 = json.load(f)
    except: # If JSON is blank, sets Player_Data_3 to a Blank Dictionary
        Player_Data_3 = {} # Sets to blank Dictionary
   
    try: # Try to open Save 4 and Append it to Player_Data_4
        with open(f'Save4.json', 'r') as f:
                Player_Data_4 = json.load(f)
    except: # If JSON is blank, sets Player_Data_4 to a Blank Dictionary
        Player_Data_4 = {} # Sets to blank Dictionary

    # Prints the Title of the Game, and each of the Save Name and Location - If their is no save information - Sets it to None
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


    ''')
    Input_Selection({ # Sends the Dictionary to Input_Selection
         'Save 1': lambda: (load(Player_Data_1, 1)), # Sets Save 1 to Load data from Player_Data_1 to load
         'Save 2': lambda: (load(Player_Data_2, 2)), # Sets Save 2 to Load data from Player_Data_2 to load
         'Save 3': lambda: (load(Player_Data_3, 3)), # Sets Save 3 to Load data from Player_Data_3 to load
         'Save 4': lambda: (load(Player_Data_4, 4)), # Sets Save 4 to Load data from Player_Data_4 to load
         'OverWrite Save': lambda: OverWrite(), # If player Wants to OverWrite a Save - OverWrites it
         'Exit': lambda: quit() # If the player wants to leave, quits the program
    })

    PrintMainUI(User.Location) # Starts to Game Based of the Users Location

def Input_Selection(options: dict): # ":dict" - Ensures it is a Dictionary
    '''This function handles the Input selection process for a variety of functions in my program'''
    def ReplaceInput():
        '''This function replaces the Input and prints Error Message'''
        ClearLines(2)  # Clears 2 Lines Above
        print('Error With Input') # Error Message
        return get_input()  # Re-prompt's the User for an Input
    
    def get_input():
        '''This function handles recieving Inputs from the User'''
        try: # Try to Recieve and Input from the User
            SaveSelection = input('Choice: ') # Recieve input from User
            SaveSelection = int(SaveSelection) # Check if Input is a Integer
            if 1 <= SaveSelection <= len(option_list): # if Input is an option in avaliable options
                option_list[SaveSelection - 1][1]()  # Call the corresponding function
            else: # If it is not an Option
                ReplaceInput() # Give an Error Message
        except Exception: # If error with Input (but not SystemExit)
            ReplaceInput() # Give an Error Message

    # Print options
    option_list = list(options.items()) # Option List is List of Dictionary
    print("Select an option:") # Directs User
    for i, (name, _) in enumerate(option_list, start=1): # For Each Option in option list, display the Item and its associated value
        print(f"{i}. {name}")  # Prints the Number and the Name of the function it is associated to
    print() # Creates a Spacer in the Terminal
    get_input() # Runs Recieve Input

# Player Functions
def load(Player_Data, Save):
    '''Loads Player Data from the JSON to the format for creating a Player'''
    global User, Load_File # Globalises the User and Load file Attributes

    Load_File = Save # Sets the Load File

    if len(Player_Data) == 0: # If their is no save data
        CreateCharacter() # Create a Character

    else: # Convert the information from the JSON file to a dictionary to create the player
        Data = { # Creates a dictionary to store all player data
        'Player_Name': Player_Data['Player_Name'], # Stores the player's name

        'Health': Player_Data['Health'], # Stores current and max health
        'Stamina': Player_Data['Stamina'], # Stores current and max stamina
        'Mana': Player_Data['Mana'], # Stores current and max mana

        'Location': Player_Data['Location'], # Stores the last known location
        'Gold': Player_Data['Gold'], # Stores the player's gold amount

        'WeaponSlot': Load_Items(Player_Data['WeaponSlot']['Name'], Player_Data['WeaponSlot']['Level'], Player_Data['WeaponSlot']['Multiplyers']), # Loads the weapon item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'HelmetSlot': Load_Items(Player_Data['HelmetSlot']['Name'], Player_Data['HelmetSlot']['Level'], Player_Data['HelmetSlot']['Multiplyers']), # Loads the helmet item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'ChestplateSlot': Load_Items(Player_Data['ChestplateSlot']['Name'], Player_Data['ChestplateSlot']['Level'], Player_Data['ChestplateSlot']['Multiplyers']), # Loads the chestplate item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'BootSlot': Load_Items(Player_Data['BootSlot']['Name'], Player_Data['BootSlot']['Level'], Player_Data['BootSlot']['Multiplyers']), # Loads the boots item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        
        'OtherSlot1': {'Item': Load_Items(Player_Data['OtherSlot1']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot1']['Qty']}, # Loads item in OtherSlot1 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot2': {'Item': Load_Items(Player_Data['OtherSlot2']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot2']['Qty']}, # Loads item in OtherSlot2 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot3': {'Item': Load_Items(Player_Data['OtherSlot3']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot3']['Qty']}, # Loads item in OtherSlot3 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot4': {'Item': Load_Items(Player_Data['OtherSlot4']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot4']['Qty']}, # Loads item in OtherSlot4 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        
        'Enemy1': Player_Data['Enemy1'], # Tracks if Enemy1 has been visted
        'Enemy2': Player_Data['Enemy2'], # Tracks if Enemy2 has been visted
        'Enemy3': Player_Data['Enemy3'], # Tracks if Enemy3 has been visted
        'Enemy4': Player_Data['Enemy4'], # Tracks if Enemy4 has been visted

        'Village1': Player_Data['Village1'], # Tracks if Village1 has been visited
        'Village2': Player_Data['Village2'], # Tracks if Village2 has been visited
        'Village3': Player_Data['Village3'], # Tracks if Village3 has been visited

        'Forest1': Player_Data['Forest1'], # Tracks if Forest1 has been visited
        'Forest2': Player_Data['Forest2'], # Tracks if Forest2 has been visited
        'Forest3': Player_Data['Forest3'], # Tracks if Forest3 has been visited
        'Forest4': Player_Data['Forest4'], # Tracks if Forest4 has been visited

        'SeenW1': Player_Data['SeenW1'], # Tracks if the player has met Wizard1
        'SeenW2': Player_Data['SeenW2'], # Tracks if the player has met Wizard2

        'Wizard1': Player_Data['Wizard1'], # Tracks if Wizard1 area has been visted
        'Wizard2': Player_Data['Wizard2'], # Tracks if Wizard2 area has been visted

        'Mountain': Player_Data['Mountain'], # Tracks if the Mountain has been visited

        'GoblinKing': Player_Data['GoblinKing'], # Tracks if Goblin King has been visited

        'RareFlower': Player_Data['RareFlower'], # Tracks if Rare Flower has been collected
        'RareRune': Player_Data['RareRune'], # Tracks if Rare Rune has been collected


        'Enemies': Player_Data['Enemies'] # Stores the state of all enemies
        }


        User = Player(Data) # Creates a new Player object with the loaded data

def CreateCharacter():
    '''This Function Creates a Character if their is no existing player data'''
    global User # Globaises the User Attribute
    print('Welcome New Adventurer!') # Welecomes the User
    while True: # Run until broken
        Name_Input = input("What's your Name Adventurer? ") # Ask's the Player their Name

        if len(Name_Input) == 0: # If User Doesnt Enter a Name
            print("You must enter a name!") # Prints and Error Message
        elif len(Name_Input) > 20: # If the User enters a name that is too long
            print("Your name is too long! Please keep it under 20 characters.") # Prints and Error Message
        else: # If their is no problems with the Users Name
            print(f'Welcome {Name_Input}, This is where your Journey Begins!') # Welcomes user
            break # Breaks the Loop

    Player_Data = { # Initalises Player Data to Defaults
        'Player_Name': Name_Input, # Player Name is set to Players Chosen Name

        'Health': {'Health': 100, 'Max_Health': 100}, # Sets player Health to 100, and Max Health to 100
        'Stamina': {'Stamina': 100, 'Max_Stamina': 100}, # Sets player Stamina to 100, and Max Stamina to 100
        'Mana': {'Mana': 100, 'Max_Mana': 100}, # Sets player Mana to 100, and Max Mana to 100

        'WeaponSlot': Stick, # Sets Users Weapon to Stick
        'HelmetSlot': None_Helmet, # Sets Users Helmet to None_Helmet
        'ChestplateSlot': None_Chestplate, # Sets Users Chestplate to None_Chestplate
        'BootSlot': None_Boot, # Sets Users Boots to None_Boot
        
        'OtherSlot1': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot2': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot3': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot4': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0

        'Location': 'Forest1', # Sets Users location to be 'Forest1' - the Default Room
        'Gold': 25, # Sets Users gold to be 25 - 25 is Enough to make money through the Casino - the Lumberjack is more designed to prevent soft locking

        'Enemy1': False, # Sets Room to be False
        'Enemy2': False, # Sets Room to be False
        'Enemy3': False, # Sets Room to be False
        'Enemy4': False, # Sets Room to be False

        'Village1': False, # Sets Room to be False
        'Village2': False, # Sets Room to be False
        'Village3': False, # Sets Room to be False

        'Forest1': False, # Sets Room to be False
        'Forest2': False, # Sets Room to be False
        'Forest3': False, # Sets Room to be False
        'Forest4': False, # Sets Room to be False


        'SeenW1': False, # Sets Seen Wizard 1 to be False
        'SeenW2': False, # Sets Seen Wizard 2 to be False
        
        'Wizard1': False,  # Sets Room to be False
        'Wizard2': False, # Sets Room to be False
        'Mountain': False, # Sets Room to be False
        'GoblinKing': False, # Sets Room to be False

        'RareFlower': False, # Sets Room to be False
        'RareRune': False, # Sets Room to be False

        'Enemies': {'G': 10, 'O': 20, 'D': 20, 'Og': 50} # Sets Room to be False
    }

    User = Player(Player_Data) # Creates a Player based off of those attributes



# Magic
def Enchantment(item, type=None):
    '''This function Enchants items to be more effective against enemy types'''    
    Level = item.level # Sets level to the Item of the Level being Encahanted

    Multiplyer = (random.randint(0, round(Level)+10)/10) # This calculate the strength of the Enchant - with a higher level allowing for a higher chance of a better enchantment

    if type == None: # If Player wants a Neuteral Buff
        item.setmultipliers({'Wat': (1+((Multiplyer)/4)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1+((Multiplyer)/4))}) # If the Player wants a overall Neutral Buff
    else:
        if type == 'Fir': # If Player wants a Fire Buff 
            item.setmultipliers({'Wat': (1-((Multiplyer)/4)), 'Fir': (1+(Multiplyer)), 'Nat': (1+((Multiplyer)/4))}) # If the Player wants a stronge buff to Fire, but at the cost of Water Strength
        
        elif type == 'Wat': # If Player wants a Water Buff
            item.setmultipliers({'Wat': (1+(Multiplyer)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1-((Multiplyer)/4))}) # If the Player wants a strong buff to Water, but at the cost of Nature Strength
        
        elif type == 'Nat': # If Player wants a Nature Buff
            item.setmultipliers({'Wat': (1+((Multiplyer)/4)), 'Fir': (1-((Multiplyer)/4)), 'Nat': (1+(Multiplyer))}) # If the Player wants a strong buff to Nature, but at the cost of Fire Strenth
# Movement
def MoveOptions(Room):
    '''Curates the Avaliable Moves for the Player based on their current Location'''
    global User  # Access the global User object

    def RemoveStamina(Stamina): 
        '''This function removes stamina from the Player'''
        User.Stamina['Stamina'] -= Stamina  # Removes X stamina from the player

    Default = {
        "Inventory": lambda: DisplayInventoryScreen(),  # Opens the inventory screen
        "Exit": lambda: Exiting()  # Exits the current screen/menu
    }

    def RoomOptions():
        '''Curates the Room Specific Moves'''
        if Room == 'Enemy1':
            return {
                "North East (Enemy2) (6)": lambda: (RemoveStamina(6), PrintMainUI('Enemy2')),  # -6 stamina, loads Enemy2
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),  # -4 stamina, loads Forest2
                "East (Vilage1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),  # -2 stamina, loads Village1
                "West (Forest1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Forest1')),  # -2 stamina, loads Forest1
            }
        elif Room == 'Enemy2':
            return {
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),  # -3 stamina, loads Enemy3
                "South East (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),  # -6 stamina, loads Forest3
                "South West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
                "East (Wizard1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Wizard1')),  # -2 stamina, loads Wizard1
            }
        elif Room == 'Enemy3':
            return {
                "South East (Wizard1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Wizard1')),  # -4 stamina, loads Wizard1
                "South West (Enemy2) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy2')),  # -3 stamina, loads Enemy2
                "West (Mountain) (20)": lambda: (RemoveStamina(20), PrintMainUI('Mountain')),  # -20 stamina, loads Mountain
            }
        elif Room == 'Enemy4':
            return {
                "North West (Forest4) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),  # -8 stamina, loads Village2
                "East (GoblinKing) (4)": lambda: (RemoveStamina(4), PrintMainUI('GoblinKing')),  # -4 stamina, loads GoblinKing
                "West (Village2) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),  # -8 stamina, loads Village2
            }
        elif Room == 'Village1':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village1')),  # Clears 8 lines, enters Village1
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),  # -4 stamina, loads Forest2
                "East (Village2) (5)": lambda: (RemoveStamina(5), PrintMainUI('Village2')),  # -5 stamina, loads Village2
                "West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
            }
        elif Room == 'Village2':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village2')),  # Clears 8 lines, enters Village2
                "South East (Wizard2) (7)": lambda: (RemoveStamina(7), PrintMainUI('Wizard2')),  # -7 stamina, loads Wizard2
                "East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),  # -5 stamina, loads Enemy4
                "West (Village1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),  # -2 stamina, loads Village1
            }
        elif Room == 'Village3':
            return {
                "Enter Village": lambda: (ClearLines(5), EnterVillage('Village1')),  # Clears 5 lines, enters Village1
                "North West (Forest4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest4')),  # -4 stamina, loads Forest4
            }
        elif Room == 'Forest1':
            return {
                "East (Enemy) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
            }
        elif Room == 'Forest2':
            if User.SeenW1:
                User.RareFlower = True  # Player receives a rare flower
                print('''
        You found a Rare Flower!
                ''')
            return {
                "North East (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),  # -4 stamina, loads Village1
                "North West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),  # -4 stamina, loads Enemy1
            }
        elif Room == 'Forest3':
            return {
                "North East (Forest4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Forest4')),  # -5 stamina, loads Forest4
                "North West (Enemy2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy2')),  # -4 stamina, loads Enemy2
                "East (Enemy4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),  # -4 stamina, loads Enemy4
                "West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),  # -4 stamina, loads Enemy1
            }
        elif Room == 'Forest4':
            return {
                "South East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),  # -5 stamina, loads Enemy4
                "South West (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),  # -6 stamina, loads Forest3
                "East (Village3) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village3')),  # -4 stamina, loads Village3
            }
        elif Room == 'Wizard1':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard1'),  # Enters Wizard1's tower
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),  # -3 stamina, loads Enemy3
                "West (Enemy2) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy2')),  # -2 stamina, loads Enemy2
            }
        elif Room == 'Wizard2':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard2'),  # Enters Wizard2's tower
                "North East (Village2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village2')),  # -4 stamina, loads Village2
                "North West (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),  # -4 stamina, loads Village1
            }
        elif Room == 'Mountain':
            if User.SeenW2:
                User.RareRune = True  # Player receives a rare rune
                print('''
        You found a Rare Rune!
                ''')
            return {
                "East (Enemy3) (10)": lambda: (RemoveStamina(10), PrintMainUI('Enemy3')),  # -10 stamina, loads Enemy3
            }
        elif Room == 'GoblinKing':
            return {
                "West (Enemy 4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),  # -4 stamina, loads Enemy4
            }
        else:
            return {}  # If no known room, return empty movement options

    options = {}  # Initialize the options dictionary
    options.update(Default)  # Add inventory and exit options
    options.update(RoomOptions())  # Add movement options for the current room
    return options  # Return all available options

def Story(Room):
    '''This function returns story elements depending on the Room, and whether the player has been in the room, it also starts Combat sequences'''
    if Room == 'Enemy1':
        if User.Enemy1 == False:
            input('Press Enter to Enter Combat...')
            Combat(Goblin, 'Enemy1')
            return ''
        else:
            return f'''You See the remains of a battle fought here. The ground is scorched, and the air is heavy with the scent of burnt wood and blood.'''
    
    elif Room == 'Enemy2':
        if User.Enemy2 == False:
            input('Press Enter to Enter Combat...')
            Combat(Orc, 'Enemy2')
            return ''
        else:
            return f'''None'''
    
    elif Room == 'Enemy3':
        if User.Enemy3 == False:
            input('Press Enter to Enter Combat...')
            Combat(Druid, 'Enemy3')
            return ''
        else:
            return f'''None'''
    
    elif Room == 'Enemy4':
        if User.Enemy4 == False:
            input('Press Enter to Enter Combat...')
            Combat(Ogre, 'Enemy4')
            return ''
        else:
            return f'''None'''
    
    elif Room == 'Village1':
        if User.Village1 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Village2':
        if User.Village2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Village3':
        if User.Village3 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Forest1':
        if User.Forest1 == False:
            return f'''Your Eyes flutter open...'''
        else:
            return f'''You return to the Dark Forest, where you first awoke. The trees are still as dark and foreboding as ever, but you feel a sense of familiarity here.'''
    
    elif Room == 'Forest2':
        if User.Forest2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Forest3':
        if User.Forest3 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Forest4':
        if User.Forest4 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Wizard1':
        if User.Wizard1 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Wizard2':
        if User.Wizard2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Mountain':
        if User.Mountain == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'GoblinKing':
        if User.GoblinKing == False:
            return f'''None'''
        else:
            return f'''None'''

def Map(Room):
    global MountainIssue
    if Room == 'Mountain': # If the Room is Mountain
        MountainIssue = True # Mountain Issue is True (This is because the Mountain Emoji's are some of the only emoji's that are 2 character symbols long - But created the issue where it would skew the UI elements, not in the part adjectent to the map, but at the next part Ascii Component)
    else: # If room isn't mountain
        MountainIssue = False # Sets MountainIssue to False

    def pad(symbol, width=2):
        '''This function uses wcswidth to adjust the Emojis to better calculate the width'''
        real_width = wcswidth(symbol)
        return symbol + ' ' * (width - real_width)

    Enemy1 = pad('💀') if Room != 'Enemy1' else pad('██') # If room is Enemy1, changes the Room Icon to the Player Icon
    Enemy2 = pad('💀') if Room != 'Enemy2' else pad('██') # If room is Enemy2, changes the Room Icon to the Player Icon
    Enemy3 = pad('💀') if Room != 'Enemy3' else pad('██') # If room is Enemy3, changes the Room Icon to the Player Icon
    Enemy4 = pad('💀') if Room != 'Enemy4' else pad('██') # If room is Enemy4, changes the Room Icon to the Player Icon
    Village1 = pad('🏠') if Room != 'Village1' else pad('██') # If room is Village1, changes the Room Icon to the Player Icon
    Village2 = pad('🏠') if Room != 'Village2' else pad('██') # If room is Village2, changes the Room Icon to the Player Icon
    Village3 = pad('🏠') if Room != 'Village3' else pad('██') # If room is Village3, changes the Room Icon to the Player Icon
    Forest1 = pad('🌲') if Room != 'Forest1' else pad('██') # If room is Forest1, changes the Room Icon to the Player Icon
    Forest2 = pad('🌲') if Room != 'Forest2' else pad('██') # If room is Forest2, changes the Room Icon to the Player Icon
    Forest3 = pad('🌲') if Room != 'Forest3' else pad('██') # If room is Forest3, changes the Room Icon to the Player Icon
    Forest4 = pad('🌲') if Room != 'Forest4' else pad('██') # If room is Forest4, changes the Room Icon to the Player Icon
    Wizard1 = pad('🔮') if Room != 'Wizard1' else pad('██') # If room is Wizard1, changes the Room Icon to the Player Icon
    Wizard2 = pad('🔮') if Room != 'Wizard2' else pad('██') # If room is Wizard2, changes the Room Icon to the Player Icon
    Mountain = pad('🏔️ ') if Room != 'Mountain' else pad('██') # If room is Mountain, changes the Room Icon to the Player Icon
    GoblinKing = pad('👑') if Room != 'GoblinKing' else pad('██') # If room is GoblinKing, changes the Room Icon to the Player Icon

    def TitleGenerator(Title):
        '''This function creates a centered title for each of the Rooms, being able to adapt to the length of the title''' 
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+' # Math to calculate the Center and have everything fit

    # This returns the Map, with each of the Locations attcaked with their variables - This system - While more complex - is significantly more efficient in creating the map
    return f'''    {TitleGenerator(Room)}
    │                                                       │
    │           ┌──────{Enemy3}          {Forest4} ────┐                 │
    │           │       │           │     │                 │
    │     {Mountain} ───┘       │           │     │                 │
    │                   │           │     └────{Village3}           │
    │               {Enemy2} ─┴────{Wizard1}     │                       │
    │                │              │                       │
    │        ┌───────┴────────┬─────┤                       │
    │        │                │     └───────┐               │
    │ {Forest1}────{Enemy1}      {Village1}       {Forest3}             ├────{Enemy4} ────{GoblinKing}  │
    │        │       │            {Village2} ───────┘               │
    │        └────┬──┴──┬──────────┘                        │
    │             │     │                                   │
    │             │     └──┐                                │
    │             │        │                                │
    │        {Forest2} ──┘        │                             ⬆  │
    │                      └────────────{Wizard2}               N  │
    │                                                       │
    +───────────────────────────────────────────────────────+'''

def EnterVillage(Village):
    '''This function handles the process of creating villagers, and displaying them in the Village'''

    Mort = ArmourSmith('Mort') # Creates an ArmourSmith named Mort
    Alex = AxeSmith('Alex') # Creates an AxeSmith named Alex
    Melvin = Brewer('Melvin') # Creates a Brewer named Melvin
    Zuba = LumberJack('Zuba') # Creates a LumberJack named Zuba

    Bill = Gambler('Bill') # Creates a Gambler named Bill

    Julian = ArmourSmith('Julian') # Creates an ArmourSmith named Julian
    Gloria = SwordSmith('Gloria') # Creates a SwordSmith named Gloria
    Marty = AxeSmith('Marty') # Creates an AxeSmith named Marty
    Kowalski = Brewer('Kowalski') # Creates a Brewer named Kowalski
    Moto = LumberJack('Moto') # Creates a LumberJack named Moto

    Dole = Gambler('Dole') # Creates a Gambler named Dole

    Maurice = ArmourSmith('Maurice') # Creates an ArmourSmith named Maurice
    Rico = SwordSmith('Rico') # Creates a SwordSmith named Rico
    Skipper = Brewer('Skipper') # Creates a Brewer named Skipper
    Milton = LumberJack('Milton') # Creates a LumberJack named Milton

    Doh = Gambler('Doh') # Creates a Gambler named Doh

    while True: # Continuously loop until the player chooses to exit
        os.system('cls') # Clears the terminal screen
        print('Select a Merchant to Interact With!') # Prompts the user to select a merchant
        print() # Prints a blank line for spacing

        Exiting = False # Initializes the exiting flag as False

        def Break():
            '''This function handles when the User wants to exit the Village'''
            nonlocal Exiting # Allows modification of the Exiting variable from the outer scope
            os.system('cls') # Clears the terminal screen
            print() # Prints a blank line for spacing
            print('Select a Merchant to Interact With!') # Re-prompts the user after exiting
            print() # Prints a blank line for spacing
            Exiting = True # Sets the exiting flag to True

        if Village == 'Village1': # If the player is in Village1
            Input_Selection({ # Displays the merchant options for Village1
                'Mort - Armoursmith': lambda: Mort.Inventory_Trading(), # Opens Mort's armour shop
                'Alex - Axesmith': lambda: Alex.Inventory_Trading(), # Opens Alex's axe shop
                'Melvin - Brewer': lambda: Melvin.Inventory_Trading(), # Opens Melvin's potion shop
                'Zuba - LumberJack': lambda: Zuba.ChopWood(), # Starts Zuba's woodcutting activity
                'Bill - Casino Owner': lambda: Bill.Casino(), # Enters Bill's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

        elif Village == 'Village2': # If the player is in Village2
            Input_Selection({ # Displays the merchant options for Village2
                'Julian - Armoursmith': lambda: Julian.Inventory_Trading(), # Opens Julian's armour shop
                'Gloria - Swordsmith': lambda: Gloria.Inventory_Trading(), # Opens Gloria's sword shop
                'Marty - Axesmith': lambda: Marty.Inventory_Trading(), # Opens Marty's axe shop
                'Kowalski - Brewer': lambda: Kowalski.Inventory_Trading(), # Opens Kowalski's potion shop
                'Moto - LumberJack': lambda: Moto.ChopWood(), # Starts Moto's woodcutting activity
                'Dole - Casino Owner': lambda: Dole.Casino(), # Enters Dole's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

        elif Village == 'Village3': # If the player is in Village3
            Input_Selection({ # Displays the merchant options for Village3
                'Maurice - Armoursmith': lambda: Maurice.Inventory_Trading(), # Opens Maurice's armour shop
                'Rico - Swordsmith': lambda: Rico.Inventory_Trading(), # Opens Rico's sword shop
                'Skipper - Brewer': lambda: Skipper.Inventory_Trading(), # Opens Skipper's potion shop
                'Milton - LumberJack': lambda: Milton.ChopWood(), # Starts Milton's woodcutting activity
                'Doh - Casino Owner': lambda: Doh.Casino(), # Enters Doh's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

    PrintMainUI(Village) # Returns the user back to the main UI of the current village

def EnterWizardTower(wizard_room):
    '''This Function handles the Wizard Tower Interactions, and Ensuring a Wizard is Intialised'''
    Jake = Wizard('Jake') # Since the Name of the Wizard is Irrelivent for the Wizard function, the rooms can share the same Wizard Object

    Jake.WizardStore(wizard_room) # Runs the Wizard Store function, also providing which room it is happening in, allowing the Function to differenciate between the two rooms

def ClearLines(n):
    '''This function allows me to clear lines by the specified amount'''
    for _ in range(n): # For each of the lines specified in the Parameters
        print("\033[1A\033[2K", end="") # Clear the most recent line

def Exiting():
    '''Handles the Exiting of the Game back to the Titlescreen'''
    global Load_File, User # Globaises the Varibales
    User.Save(Load_File) # Saves the Users Progress
    User = None # Resets the User
    Load_File = 0 # Resets the Load File
    TitleScreen() # Restarts back to the Titlescreen

def Died(DeathCause):
    '''This Function handles the Death of the Player'''
    global Load_File # Globalises the Variables in the Function
    os.system('cls') # Clears the Screen
    # Prints You Died Ascii Art and the Death message
    print(f'''
 ▄· ▄▌      ▄• ▄▌    ·▄▄▄▄  ▪  ▄▄▄ .·▄▄▄▄  
▐█▪██▌▪     █▪██▌    ██▪ ██ ██ ▀▄.▀·██▪ ██ 
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▐█· ▐█▌▐█·▐▀▀▪▄▐█· ▐█▌
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ██. ██ ▐█▌▐█▄▄▌██. ██ 
  ▀ •  ▀█▄▀▪ ▀▀▀     ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀• 

You Died to {DeathCause}
''')
    input('Enter to Delete Save...') # Waits so the user can see

    with open(f'Save{Load_File}.json', 'w') as file: # Opens the Current save file
        json.dump({}, file) # Dumps an empty dictionary to the file - Causing it to get deleted
    
    Load_File = 0

    TitleScreen() # Loads the Titlescreen Program - Restating the Program


TitleScreen() # Runs the Program from Titlescreen
```

## Review Questions:

### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
 - The project successfully meets the majority of its functional and non-functional requirements as outlined in the initial planning documents. Core features such as displaying player statistics (health, stamina, mana, inventory, gold, location) and supporting terminal-based interaction using simplified input commands are fully implemented and operational. Originally planned to use directional inputs like "N", "S", "E", and "W" for movement, the system has since been refined to use a numbered input system instead. This change improves usability by allowing users to make decisions more quickly and intuitively, streamlining the experience and minimizing typing errors.

 - The system also meets key non-functional goals. It performs efficiently due to its text-based design, quickly handling scene changes and updates with minimal delay. User feedback is clear and consistent throughout, and reliable input handling ensures a smooth user experience. The program responds eficiently, and directly to invalid inputs without crashing, fulfilling error handling. Reliability is further supported through the use of classes and structured systems for statistics and interactions.

 - The final two areas that still require work are the inventory screen, which I want to refine to display more relevent data, and the Boss Battle scene, which still needs to be developed.

### Analyse the performance of your program against the key use-cases you identified.
 - The program performs well across the key use-cases defined in the design phase. Movement between areas is handled using a numbered input system rather than the initially planned directional (N/S/E/W) system. This update has improved ease of use and reduced input errors, allowing for quicker navigation and a more streamlined experience.

 - Combat encounters function as expected, with turn-based logic that allows players to equip a physical weapon and engage in multi-turn battles. Damage is calculated based on the player’s equipped weapon and the enemy’s attributes, and players are able to adapt their strategy across rounds. The system responds accurately to player choices, such as attacking or using items, and clearly displays the results of each action.

 - Players can view their statistics and inventory at any time, completing my data retrieval reuirement. Inventory interaction, trading, and exploration function correctly, and stamina is managed consistently during travel. Input validation has been thoroughly tested, and no major errors or crashes have occurred thanks to the robust input handling function.

 - Although the final boss fight and story progression are still in development, the core use-cases for interaction, navigation, combat, and stat management are effectively implemented.

### Assess the quality of your code in terms of readability, structure, and maintainability.
 - Overall, the code is high quality in terms of readability and maintainability. My code has conistent and cohesive comments to thoroughly explain logic, which improves readability for others.

 - The use of classes for modular components (e.g., Player, Enemy, Villager) improves reusability. Each of the functions efficiently uses parameters to effecively and effciently transmit code throughout the system's range of functions.

 - Currently, the entire program resides in a single file due to previous issues with circular imports. However, there is a plan to split the program into separate files again (e.g., for inventory, UI, enemies, etc.), which would greatly enhance maintainability and organization.

#### Explain the improvements that should be made in the next stage of development.
 - The next stage of development should focus on both feature completion and structural refinement:

    - Feature Enhancements:

        - Finalize the inventory system to improve its visual layout and include additional data (e.g. Show more items, and more statistics)

        - Implement the boss fight to complete the game’s core narrative and difficulty arc.

        - Integrate the story and scripted events to enhance immersion and give purpose to gameplay progression.

    - Code Improvements:

        - Reorganize the code into multiple Python modules once circular import issues are resolved. This will make the program easier to scale and debug.

 - These improvements will not only polish the game experience but also position the project as a well-structured, maintainable application.

# Sprint 3

### UML Class Diagram: 
<img src="Images/UML_Class_Diagram.png" alt="Alt Text" width="500">

### Build: (main.py)
```Python
#--- Imports ---
import os # Used for editing the terminal view
import random # Allows for randomness between different runs
import time # Allows for more interactive UI by incorperating time
import json # Used for saving
import math # Used to calculate events
from wcwidth import wcswidth # Used to handle the Emoji and Ascii problems

#--- Classes ---
class Player():
    '''This class is used to create the Player information system, and is designed to be adaptive, allowing for different save files to be loaded, and unloaded'''
    def __init__(self, Save):
        '''Loads the Player data from the Save file (Which is a Dictionary)'''
        self.Player_Name = Save['Player_Name'] # Loads Player Name from Save file

        self.Health = {'Health': Save['Health']['Health'], 'Max_Health': Save['Health']['Max_Health']} # Loads Health and Max Health into a dictionary
        self.Stamina = {'Stamina': Save['Stamina']['Stamina'], 'Max_Stamina': Save['Stamina']['Max_Stamina']} # Loads Stamina and Max Stamina into a dictionary
        self.Mana = {'Mana': Save['Mana']['Mana'], 'Max_Mana': Save['Mana']['Max_Mana']} # Loads Mana and Max Mana into a dictionary

        self.WeaponSlot = Save['WeaponSlot'] # Loads Weapon from the Save File
        self.HelmetSlot = Save['HelmetSlot'] # Loads the Helmet from the Save File
        self.ChestplateSlot = Save['ChestplateSlot'] # Loads the Chestplate from the Save file
        self.BootSlot = Save['BootSlot'] # Loads the Boot from the Chestplate

        self.OtherSlot1 = {'Item': Save['OtherSlot1']['Item'], 'Qty': Save['OtherSlot1']['Qty']} # Loads the Item and Qty from save file for Save File 1
        self.OtherSlot2 = {'Item': Save['OtherSlot2']['Item'], 'Qty': Save['OtherSlot2']['Qty']} # Loads the Item and Qty from save file for Save File 2
        self.OtherSlot3 = {'Item': Save['OtherSlot3']['Item'], 'Qty': Save['OtherSlot3']['Qty']} # Loads the Item and Qty from save file for Save File 3
        self.OtherSlot4 = {'Item': Save['OtherSlot4']['Item'], 'Qty': Save['OtherSlot4']['Qty']} # Loads the Item and Qty from save file for Save File 4
        
        self.Location = Save['Location'] # Loads the Player Location
        self.Gold = Save['Gold'] # Loads the Player Gold

        self.Enemy1 = Save['Enemy1'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy2 = Save['Enemy2'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy3 = Save['Enemy3'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy4 = Save['Enemy4'] # Loads wether the player has been in room for a more adaptive story 
        self.Village1 = Save['Village1'] # Loads wether the player has been in room for a more adaptive story 
        self.Village2 = Save['Village2'] # Loads wether the player has been in room for a more adaptive story 
        self.Village3 = Save['Village3'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest1 = Save['Forest1'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest2 = Save['Forest2'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest3 = Save['Forest3'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest4 = Save['Forest4'] # Loads wether the player has been in room for a more adaptive story 
        self.SeenW1 = Save['SeenW1'] # Loads wether the player has been in room for a more adaptive story 
        self.SeenW2 = Save['SeenW2'] # Loads wether the player has been in room for a more adaptive story 
        self.Wizard1 = Save['Wizard1'] # Loads wether the player has been in room for a more adaptive story 
        self.Wizard2 = Save['Wizard2'] # Loads wether the player has been in room for a more adaptive story 
        self.Mountain = Save['Mountain'] # Loads wether the player has been in room for a more adaptive story 
        self.GoblinKing = Save['GoblinKing'] # Loads wether the player has been in room for a more adaptive story 
        self.RareFlower = Save['RareFlower'] # Loads wether the player has obtained the Flower
        self.RareRune = Save['RareRune'] # Loads wether the player has obtained the Rune

        self.Enemies = {'G': Save['Enemies']['G'], 'O': Save['Enemies']['O'], 'D': Save['Enemies']['D'], 'Og': Save['Enemies']['Og']} # Loads the Health of Each Enemy

        Load_Enemies(Save['Enemies']['G'], Save['Enemies']['O'], Save['Enemies']['D'], Save['Enemies']['Og']) # Loads the Enemies into the System, with the health files

    def Save(self, Save):
        '''Transfers the Information from the Save File into the JSON File'''

        Player_Stats = { # Creates a Dictionary of the Data
            'Player_Name': self.Player_Name, # Loads Player Name from the Player Attributes
            'Health': self.Health, # Loads the Player Health Dictionary from Player Attributes, making it contain both player Health and Max Health
            'Stamina': self.Stamina, # Loads the Player Stamina Dictionary from Player Attributes, making it contain both player Stamina and Max Stamina
            'Mana': self.Mana, # Loads the Player Mana Dictionary from Player Attributes, making it contain both player Mana and Max Mana
            'WeaponSlot': {'Name': self.WeaponSlot.name, 'Level': self.WeaponSlot.level, 'Multiplyers': self.WeaponSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Weapon
            'HelmetSlot': {'Name': self.HelmetSlot.name, 'Level': self.HelmetSlot.level, 'Multiplyers': self.HelmetSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Helmet
            'ChestplateSlot': {'Name': self.ChestplateSlot.name, 'Level': self.ChestplateSlot.level, 'Multiplyers': self.ChestplateSlot.multiplyers},  # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Chestplate
            'BootSlot': {'Name': self.BootSlot.name, 'Level': self.BootSlot.level, 'Multiplyers': self.BootSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Boots
            'OtherSlot1': {'Item': self.OtherSlot1['Item'].name, 'Qty': self.OtherSlot1['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot2': {'Item': self.OtherSlot2['Item'].name, 'Qty': self.OtherSlot2['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot3': {'Item': self.OtherSlot3['Item'].name, 'Qty': self.OtherSlot3['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot4': {'Item': self.OtherSlot4['Item'].name, 'Qty': self.OtherSlot4['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'Location': self.Location, # Stores The Player Location
            'Gold': self.Gold, # Stores the Players amount of Gold

            'Enemy1': self.Enemy1, # Stores Whether the Player has been in the Room
            'Enemy2': self.Enemy2, # Stores Whether the Player has been in the Room
            'Enemy3': self.Enemy3, # Stores Whether the Player has been in the Room
            'Enemy4': self.Enemy4, # Stores Whether the Player has been in the Room

            'Village1': self.Village1, # Stores Whether the Player has been in the Room
            'Village2': self.Village2, # Stores Whether the Player has been in the Room
            'Village3': self.Village3, # Stores Whether the Player has been in the Room

            'Forest1': self.Forest1, # Stores Whether the Player has been in the Room
            'Forest2': self.Forest2, # Stores Whether the Player has been in the Room
            'Forest3': self.Forest3, # Stores Whether the Player has been in the Room
            'Forest4': self.Forest4, # Stores Whether the Player has been in the Room

            'SeenW1': self.SeenW1, # Stores Whether the Player has been in the Room
            'SeenW2': self.SeenW2, # Stores Whether the Player has been in the Room

            'Wizard1': self.Wizard1, # Stores Whether the Player has been in the Room
            'Wizard2': self.Wizard2, # Stores Whether the Player has been in the Room
            'Mountain': self.Mountain, # Stores Whether the Player has been in the Room
            'GoblinKing': self.GoblinKing, # Stores Whether the Player has been in the Room

            'RareFlower': self.RareFlower, # Stores Whether the Player has obtained the Rare Flower
            'RareRune': self.RareRune,# Stores Whether the Player has obtained the Rare Rune

            'Enemies': {'G': Goblin.health, 'O': Orc.health, 'D': Druid.health, 'Og': Ogre.health} # Stores the Enemy Health
        }

        with open(f'Save{Save}.json', 'w') as f: # Opens the JSON file attached to the Load File
            json.dump(Player_Stats, f) # Puts the Player Data into the JSON file

    def Attacking(self, Target):
        '''Allows the Player to Attack an Enemy, by Specifying which Enemy to Attack'''
        Target.Player_Attacked() # Runs the Player_Attacked Function of the specified Target

    def Attacked(self, Damage, Type):
        '''Calculates Damage of Enemy, based of of the Multipliers on the Players Armour'''
        try:
            self.Health['Health'] -= round(Damage / ((self.HelmetSlot.protection + self.ChestplateSlot.protection + self.BootSlot.protection) / 3) * ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3)) # Calculates the Protection based on factors such as Protection and Enchantment Levels

        except:
            self.Health['Health'] -= Damage

class Item():
    '''This class creates the Foundation for Creating Items in the Game'''
    def __init__(self, name, level):
        'This function initalises the Items Variables'
        self.name = name # Defines the Items Name
        self.level = level # Defines the Ites Level

class Weapons(Item):
    '''This Class outlines the basics for creating Weapons'''
    def __init__(self, name, level, type, damage, multiplyers=None): 
        '''This Function Inherits the Prarameters from Item, and adds Weapon Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.type = type # Defines the Weapon Type - i.e Sword, Axe, Mace
        self.damage = damage # Defines the Weapons Damage
        
        if multiplyers is None: # If Multipliers is Undefined - Not given when creating the Weapon
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1} # Sets Multiplers all to 1
        else:
            self.multiplyers = multiplyers # If Multiplers are given, uses the given ones

    def setmultiplyers(self, Multiplyers):
        '''This Function allows the setting of the Multiplers - Used to Enchant the Item'''
        self.multiplyers = Multiplyers # Sets the Multiplers

class Armour(Item):
    '''This Class outlines the basics for creating Armour'''
    def __init__(self, name, level, type, protection, multiplyers=None):
        '''This Function Inherits the Prarameters from Item, and adds Armour Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.type = type # Defines the Type of Armour - i.e Helmet, Chestplate, Boots
        self.protection = protection # Defines the Protection level of the Armour


        if multiplyers is None: # If Multipliers is Undefined - Not given when creating the Armour piece
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1} # Sets Multiplers all to 1
        else:
            self.multiplyers = multiplyers # If Multiplers are given, uses the given ones

    def setmultiplyers(self, Multiplyers):
        self.multiplyers = Multiplyers
            
class Potion(Item):
    '''This Class creates potions, and allows them to be made at different strengths, to impact the Player different stats'''
    def __init__(self, name, level, effect, strength):
        '''This Function Inherits the Prarameters from Item, and adds Potion Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.effect = effect # Defines the effect the Potion impacts - i.e Health, Stamina, Mana
        self.strength = strength # Defines the Strength of the Potion

    def Use_Potion(self, Target):
        '''This function allows the Potion to be Used'''
        getattr(Target, self.effect)[self.effect] += self.strength # Applies the Effect to the Target
        if getattr(Target, self.effect)[self.effect] > getattr(Target, self.effect)[f'Max_{self.effect}']: # If the Potion atted too much statistic compared to the Max...
            getattr(Target, self.effect)[self.effect] = getattr(Target, self.effect)[f'Max_{self.effect}'] # Brings the Health Back down to the Max Health

        # Remove potion from inventory after use
        for slot in [Target.OtherSlot1, Target.OtherSlot2, Target.OtherSlot3, Target.OtherSlot4]: # Finds Which slot Potion is In
            if slot['Item'] is self and slot['Qty'] > 0: # Item is in Slot, and the Quantity is More than 0
                slot['Qty'] -= 1 # Removes of from the Quantity
                if slot['Qty'] == 0: # If their is None left in the Slot
                    slot['Item'] = None_Item # Reverts Slot back to None_Item
                break # Stops looking for where the Item is

class Enemy():
    '''This Class Creates a Enemy System, that allows for the creation of Enemies, and Allows them to interact / attack other Players and Enemies'''
    def __init__(self, name, health, max_health, damage, type, level):
        '''This function allows the User to '''
        self.name = name
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.type = type
        self.level = level

    def Attacking(self, Target):
        Target.Attacked(self.damage, self.type)

    def Player_Attacked(self):
        self.health -= round(User.WeaponSlot.damage * User.WeaponSlot.multiplyers[self.type])

    def Attacked(self, Damage, Type):
        if self.type == 'Fir' and Type == 'Wat': # Strong < Weak
            self.health -= round(Damage * 1.5)

        elif self.type == 'Wat' and Type == 'Fir': # Strong > Weak
            self.health -= round(Damage * 0.5)

        elif self.type == 'Nat' and Type == 'Fir': # Strong < Weak
            self.health -= round(Damage * 1.5)

        elif self.type == 'Fir' and Type == 'Nat': # Strong > Weak
            self.health -= round(Damage * 0.5)

        elif self.type == 'Wat' and Type == 'Nat': # Strong < Weak
            self.health -= round(Damage * 1.5)
        
        elif self.type == 'Nat' and Type == 'Wat': # Strong > Weak
            self.health -= round(Damage * 0.5)
        
        else:
            self.health -= round(Damage)

class Villager:
    '''This class handles the Villager Creation Process'''
    def __init__(self, name, profession):
        '''This function initalizes the Villager attributes'''
        self.name = name # Creates a Villager Name 
        self.profession = profession # Gives the Villager a Profession
        self.items = {} # Creates a dicitonary for each item the User Sells

    def Inventory_Trading(self):
        '''This Function allows the user to purchase the items that each villager sells'''
        os.system('cls')  # Clear the terminal screen for a clean display

        # Print villager's shop interface with their name, profession, and the user's gold
        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     {self.profession:<38}|
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {str(User.Gold) + ' 🪙':<38}|
    +---------------------------------------------------------+
    ''') 

        count = 1  # Start item count at 1 for menu numbering

        # Print the table header with item structure
        print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')  
        for item in self.items.values():  # Loop through each item the villager sells
            # Print item number, name, cost, and quantity available
            print(f"|{count:<3}| {item['Item'].name:<30}   |   Cost: {item['Cost']:<4} 🪙    |   Qty: {item['Qty']:<10} |")
            # Print divider line between items
            print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
            count += 1  # Increment count for the next item

        # Calculate number of lines printed to later clear the screen
        lines_printed = (count * 2) + 1  # Includes rows and dividers

        while True:  # Start purchase loop until the player exits or breaks
            try:  # Attempt to get valid input from the player
                # Ask user to select an item to buy or 0 to exit
                Puchase_Input = int(input('Enter the number of the item you want to purchase (0 to exit): '))
                
                if Puchase_Input == 0:  # If player chose to exit
                    ClearLines(lines_printed + 1)  # Clear the printed table
                    break  # Exit the while loop
                
                elif 1 > Puchase_Input or Puchase_Input >= count:  # Input outside valid range
                    print('Not a Valid Number')  # Print error message
                
                elif 1 <= Puchase_Input < count:  # Valid item selection
                    selected_item = list(self.items.values())[Puchase_Input - 1]  # Get selected item
                    item = selected_item['Item']  # Extract the actual item object

                    if selected_item['Qty'] > 0:  # Check if the item is in stock
                        if User.Gold >= selected_item['Cost']:  # Check if player has enough gold
                            goto_inventory = False  # Flag for sending item to inventory (if not equippable)

                            # If the item is a Weapon, equip it directly
                            if isinstance(item, Weapons):
                                print(f"Equipped {item.name} to Weapon Slot (replacing {User.WeaponSlot.name}).")
                                User.WeaponSlot = item  # Replace player's weapon

                            # If the item is Armour, check which slot it belongs to
                            elif isinstance(item, Armour):
                                if item.type == 'Helmet':  # If it's a helmet
                                    print(f"Equipped {item.name} to Helmet Slot (replacing {User.HelmetSlot.name}).")
                                    User.HelmetSlot = item
                                elif item.type == 'ChestPlate':  # If it's a chestplate
                                    print(f"Equipped {item.name} to Chestplate Slot (replacing {User.ChestplateSlot.name}).")
                                    User.ChestplateSlot = item
                                elif item.type == 'Boot':  # If it's boots
                                    print(f"Equipped {item.name} to Boot Slot (replacing {User.BootSlot.name}).")
                                    User.BootSlot = item
                                else:  # Unknown armour type, treat as regular item
                                    print(f"Unknown armour type: {item.type}. Placing in inventory.")
                                    goto_inventory = True  # Send to inventory
                            else:
                                goto_inventory = True  # All other item types go to inventory

                            # Define player's inventory slots for other items
                            inventory_slots = [User.OtherSlot1, User.OtherSlot2, User.OtherSlot3, User.OtherSlot4]
                            found = False  # Track if item was already in inventory
                            replace_cancelled = False  # Track if player cancelled replace prompt

                            if goto_inventory:
                                # Check if the item is already in inventory
                                for slot in inventory_slots:
                                    if slot['Item'] is item:  # Found matching item
                                        slot['Qty'] += 1  # Increase quantity
                                        found = True
                                        break

                                if not found:  # If item not found in existing slots
                                    empty_slot = None  # Track first empty slot
                                    for slot in inventory_slots:  # Search for an empty slot
                                        if slot['Item'].name == 'None':  # Empty if item is 'None'
                                            empty_slot = slot
                                            break
                                    
                                    if empty_slot:  # Place item in empty slot
                                        empty_slot['Item'] = item
                                        empty_slot['Qty'] = 1
                                    else:
                                        # No empty slot: ask player to replace an item or cancel
                                        print("Your inventory is full. Choose an item to replace or cancel:")
                                        for idx, slot in enumerate(inventory_slots, 1):  # List current items
                                            print(f"{idx}. {slot['Item'].name} (x{slot['Qty']})")
                                        print(f"{len(inventory_slots)+1}. Cancel purchase")

                                        while True:  # Loop until valid input
                                            try:
                                                replace_choice = int(input("Enter number to replace or cancel: "))  # Get replace input
                                                if 1 <= replace_choice <= len(inventory_slots):  # Valid replace
                                                    slot = inventory_slots[replace_choice - 1]  # Chosen slot
                                                    print(f"Replaced {slot['Item'].name} with {item.name}.")  # Feedback
                                                    slot['Item'] = item  # Replace item
                                                    slot['Qty'] = 1
                                                    break
                                                elif replace_choice == len(inventory_slots) + 1:  # Cancel option
                                                    print("Purchase cancelled.")  # Cancelled
                                                    replace_cancelled = True
                                                    break
                                                else:
                                                    print("Invalid choice.")  # Error
                                            except ValueError:
                                                print("Invalid input.")  # Error for non-numbers

                            # Finalize purchase if not cancelled
                            if not goto_inventory or not replace_cancelled:
                                selected_item['Qty'] -= 1  # Reduce villager’s item stock
                                User.Gold -= selected_item['Cost']  # Deduct gold from user
                                print(f"You bought 1x {item.name} for {selected_item['Cost']} 🪙.")  # Confirm purchase
                            else:
                                continue  # If cancelled, skip rest of loop
                        else:
                            print("You do not have enough gold to purchase this item.")  # Not enough gold
                    else:
                        print("Sorry, this item is out of stock.")  # Item unavailable
            except Exception:  # Catch any unexpected error
                print("Invalid input. Please enter a number.")  # Prompt retry

class Brewer(Villager):
    """A villager that specializes in selling health, mana, and stamina potions."""
    def __init__(self, name):
        super().__init__(name, 'Brewer')  # Call the base Villager constructor with name and profession
        self.items = {  # Dictionary of potion types sold by the Brewer
            'Health Potion': {
                'Item': random.choice([Health_Potion_Small, Health_Potion_Medium, Health_Potion_Large]),  # Random potion size
                'Cost': random.randint(3, 10),  # Random cost for the potion
                'Qty': random.randint(3, 12)  # Random quantity available
            },
            'Mana Potion': {
                'Item': random.choice([Mana_Potion_Small, Mana_Potion_Medium, Mana_Potion_Large]),
                'Cost': random.randint(3, 10),
                'Qty': random.randint(3, 12)
            },
            'Stamina Potion': {
                'Item': random.choice([Stamina_Potion_Small, Stamina_Potion_Medium, Stamina_Potion_Large]),
                'Cost': random.randint(3, 10),
                'Qty': random.randint(3, 12)
            }
        }

class SwordSmith(Villager):
    """A villager that sells swords made of different materials."""
    def __init__(self, name):
        super().__init__(name, 'SwordSmith')  # Call base Villager constructor
        self.items = {
            'Wooden Sword': {'Item': Wooden_Sword, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Sword': {'Item': Bronze_Sword, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Sword': {'Item': Iron_Sword, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Sword': {'Item': Platinum_Sword, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class AxeSmith(Villager):
    """A villager that sells axes made of different materials."""
    def __init__(self, name):
        super().__init__(name, 'AxeSmith')
        self.items = {
            'Wooden Axe': {'Item': Wooden_Axe, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Axe': {'Item': Bronze_Axe, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Axe': {'Item': Iron_Axe, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Axe': {'Item': Platinum_Axe, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class MaceSmith(Villager):
    """A villager that sells maces made of different materials."""
    def __init__(self, name):
        super().__init__(name, 'MaceSmith')
        self.items = {
            'Wooden Mace': {'Item': Wooden_Mace, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Mace': {'Item': Bronze_Mace, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Mace': {'Item': Iron_Mace, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Mace': {'Item': Platinum_Mace, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class ArmourSmith(Villager):
    """A villager that sells different pieces of armor, including helmets, chestplates, and boots."""
    def __init__(self, name):
        super().__init__(name, 'ArmourSmith')
        self.items = {
            'Leather Helmet': {'Item': Leather_Helmet, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Helmet': {'Item': Bronze_Helmet, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Helmet': {'Item': Iron_Helmet, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Helmet': {'Item': Platinum_Helmet, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Chestplate': {'Item': Leather_Chestplate, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Chestplate': {'Item': Bronze_Chestplate, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Chestplate': {'Item': Iron_Chestplate, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Chestplate': {'Item': Platinum_Chestplate, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Boot': {'Item': Leather_Boot, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Boot': {'Item': Bronze_Boot, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Boot': {'Item': Iron_Boot, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Boot': {'Item': Platinum_Boot, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class Wizard(Villager):
    """A villager that enchants gear after the player completes certain quests."""
    def __init__(self, name):
        super().__init__(name, 'Wizard')  # Set name and role as Wizard
    
    def WizardStore(self, Room):
        """Handles player interaction with the Wizard based on the room (Wizard1 or Wizard2)."""
        global User  # Access the global User object
        os.system('cls')  # Clear the screen
        
        # First wizard interaction logic
        if Room == 'Wizard1':
            if User.SeenW1 == False:  # If user has not seen Wizard1 before
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Their is a rare flower in the south forest, bring it to me, and I will help you enchant!
                    ''')
                User.SeenW1 = True  # Set flag that user has now seen Wizard1
                input('     Enter to Continue...')  # Pause for input
                PrintMainUI('Wizard1')  # Return to main UI
            elif User.SeenW1 == True and User.RareFlower == False:  # If user has seen wizard but not brought the flower
                print("Have you Brought me my Flower Yet? It's in the South Forest")
                input('Enter to Continue...')
                PrintMainUI('Wizard1')
            elif User.RareFlower == True:  # If player has brought the flower
                print()
                print('Thanks for bringing me my flower, what can I help you enchant today?')
                enchanted_item = {'item': None}  # Placeholder for enchanted item
                def make_enchant_lambda(slot):  # Closure to create enchantment functions for items
                    return lambda: slot.setmultiplyers(Enchantment(slot))  # Apply enchantment to item slot
                options = {
                    User.WeaponSlot.name: make_enchant_lambda(User.WeaponSlot)
                }
                if User.HelmetSlot.name != "None_Helmet":
                    options[User.HelmetSlot.name] = make_enchant_lambda(User.HelmetSlot)
                if User.ChestplateSlot.name != "None_Chestplate":
                    options[User.ChestplateSlot.name] = make_enchant_lambda(User.ChestplateSlot)
                if User.BootSlot.name != "None_Boot":
                    options[User.BootSlot.name] = make_enchant_lambda(User.BootSlot)
                options['Exit'] = lambda: PrintMainUI('Wizard1')  # Add exit option
                Input_Selection(options)  # Allow player to choose item to enchant

                item = enchanted_item['item']  # Retrieve the enchanted item
                if item is not None:
                    print(f"You enchanted: {item.name}")
                    print("New multipliers:")
                    for key, value in item.multiplyers.items():
                        print(f"  {key}: {value:.2f}")
        
        # Second wizard interaction logic (for Rune quest)
        elif Room == 'Wizard2':
            if User.SeenW2 == False:
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Up in the high mountains of Sorvo, their is an ancient rune, ensribed with ancient information.
            Bring it to me, and I will help you enchant!
                    ''')
                User.SeenW2 = True
                input('     Enter to Continue...')
                PrintMainUI('Wizard2')
            elif User.SeenW2 == True and User.RareRune == False:
                print("Have you Brought me my RareRune Yet? It's in the high mountains of Sorvo")
                input('Enter to Continue...')
                PrintMainUI('Wizard2')
            elif User.RareRune == True:
                print()
                print('Thanks for bringing me my Rune, what can I help you enchant today?')
                enchanted_item = {'item': None}
                def make_enchant_lambda(slot):
                    return lambda: slot.setmultiplyers(Enchantment(slot))
                options = {
                    User.WeaponSlot.name: make_enchant_lambda(User.WeaponSlot)
                }
                if User.HelmetSlot.name != "None_Helmet":
                    options[User.HelmetSlot.name] = make_enchant_lambda(User.HelmetSlot)
                if User.ChestplateSlot.name != "None_Chestplate":
                    options[User.ChestplateSlot.name] = make_enchant_lambda(User.ChestplateSlot)
                if User.BootSlot.name != "None_Boot":
                    options[User.BootSlot.name] = make_enchant_lambda(User.BootSlot)
                options['Exit'] = lambda: PrintMainUI('Wizard2')
                Input_Selection(options)

                item = enchanted_item['item']
                if item is not None:
                    print(f"You enchanted: {item.name}")
                    print("New multipliers:")
                    for key, value in item.multiplyers.items():
                        print(f"  {key}: {value:.2f}")

                # Display a formatted stat chart for all gear slots with elemental multipliers
                print(f'''
        +---+{'-'*39}+- Wat -+- Fir -+- Nat -+
        | 1 | Weapon Slot:     {User.WeaponSlot.name:<20} | {User.WeaponSlot.multiplyers['Wat']:<3.3f} | {User.WeaponSlot.multiplyers['Fir']:<3.3f} | {User.WeaponSlot.multiplyers['Nat']:<3.3f} |
        | 2 | Helmet Slot:     {User.HelmetSlot.name:<20} | {User.HelmetSlot.multiplyers['Wat']:<3.3f} | {User.HelmetSlot.multiplyers['Fir']:<3.3f} | {User.HelmetSlot.multiplyers['Nat']:<3.3f} |
        | 3 | Chestplate Slot: {User.ChestplateSlot.name:<20} | {User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
        | 4 | Boot Slot:       {User.BootSlot.name:<20} | {User.BootSlot.multiplyers['Wat']:<3.3f} | {User.BootSlot.multiplyers['Fir']:<3.3f} | {User.BootSlot.multiplyers['Nat']:<3.3f} |
        +---+{'-'*39}+-------+-------+-------+''')
                input('Enter to Continue...')  # Pause before exiting            

class LumberJack(Villager):
    def __init__(self, name):
        '''This function initiates the parameters for the Lumberjack'''
        super().__init__(name, 'LumberJack') # Sets Profession to Lumberjack

    def ChopWood(self):
        '''This function allows the User to gain gold - this prevent softlocking the progression if gear'''
        os.system('cls') # Clears the Screen

        # Tells the User the Amount of gold they have, and the Villager Statistics
        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     Lumberjack                            |
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {str(User.Gold) + ' 🪙':<38}|
    +---------------------------------------------------------+

    You can Earn extra money for equipment!
''')
        print('Chop Wood!')
        for i in range(0, 5): # Run 5 Times
            print() # Creates a Spacer in the Terminal
            print('CHOP') # Prints 'Chop' to Symbolise Something Happend
            print() # Creates a Spacer in the Terminal
            time.sleep(random.randint(10, 20) / 10) # Waites Between 1 and 2 seconds
        print('Good Job, Heres a piece of Gold!') # Tells the User they have earnt a piuce of Gold
        User.Gold += 1 # Gives the User a Piece of Gold
        
        input('Enter to Continue...') # Waits for the User to Continue

class Gambler(Villager):
    def __init__(self, name):
        super().__init__(name, 'Gambler')

    def Casino(self):
        '''This Fuction runs the Casino, allowing the User to make more money'''
        CasinoNumber = random.randint(1,5) # Picks Random Number between 1 and 5

        print("Welcome to the Casino") # Welcomes User
        print() # Creates a Spacer in the Terminal
        print("If you win you'll get 5 times what you put in, if you lose, we just keep what you bet") # Explains the Game
        print() # Creates a Spacer in the Terminal

        while True: # Until Broken
            try: # Try to Recieve Input
                Betting = int(input(f"How Much Gold would you Like to Bet? (0 to Not Bet) Current Balance: {User.Gold} ")) # Asks for How much the User wants to bet
                if Betting > User.Gold or Betting < 0: # If Betting Amount it outside of Acceptable Rand
                    print("You don't have that Much Gold") # Prints Error Message
                else: # If User Input is Correct
                    break # Breaks Loop
            except: # If Error with Input
                print("Invalid input. Please enter a number.") # Prints error Message

        while True: # Until Broken
            try: # Try to Recieve Input
                Guess = int(input("Put your Bet on a Number 1-5 ")) # Asks User to Guess a Number
                if 1 <= Guess <= 5: # if Guess is In Acceptable Range
                    break # Break Loop
                else: # If not in Acceptable Range
                    print('Not an Option') # Alert the Player it is not an option
            except: # If error with Input
                print("Invalid input. Please enter a number between 1 and 5.") # Prints error Message

        if Guess == CasinoNumber: # If Player Guesses Right
            User.Gold += 4*Betting # Multiply Betting Amount by 4 (Its Multiplied by 4 because It hasnt actually removed any Gold Yet) and is added to User.Gold

        else: # If Player Guesses Wrong
            print("It'll seem you've lost, maybe next time you'll think twice about going up against the house") # Tells the User they Guessed Wrong
            User.Gold -= Betting # Removes the Betting Amount from the Users Gold

        print() # Creates a Spacer in the Terminal
        print(f"The Number was: {CasinoNumber}") # Tells the Player what it was
        print() # Creates a Spacer in the Terminal
        print(f"Current Balence: {User.Gold}") # Tells the Player their Current Gold Amount

        input('Enter to Continue...') # Waits to Continue

def Load_Items(Name, Level, Multipliers): # Converts simplified JSON data back into full Item objects for use in the program
    '''Since JSON's cant store Items, This function converts the data JSON's can store, and convert it back into the Item Form for the program'''
    
    #--- Weapons ---
    if Name == 'Stick': # If the stored item is Stick
        return Weapons('Stick', Level, 'Stick', 2, Multipliers) # Return a Stick, with the saved Level and Multipliers
    
    elif Name == 'Wooden_Sword': # If the stored item is Wooden_Sword
        return Weapons('Wooden_Sword', Level, 'Sword', 4, Multipliers) # Return a Wooden Sword, with saved Level and Multipliers
    elif Name == 'Bronze_Sword': # If the stored item is Bronze_Sword
        return Weapons('Bronze_Sword', Level, 'Sword', 5, Multipliers) # Return a Bronze Sword, with saved Level and Multipliers
    elif Name == 'Iron_Sword': # If the stored item is Iron_Sword
        return Weapons('Iron_Sword', Level, 'Sword', 6, Multipliers) # Return an Iron Sword, with saved Level and Multipliers
    elif Name == 'Platinum_Sword': # If the stored item is Platinum_Sword
        return Weapons('Platinum_Sword', Level, 'Sword', 8, Multipliers) # Return a Platinum Sword, with saved Level and Multipliers

    elif Name == 'Wooden_Axe': # If the stored item is Wooden_Axe
        return Weapons('Wooden_Axe', Level, 'Axe', 4, Multipliers) # Return a Wooden Axe, with saved Level and Multipliers
    elif Name == 'Bronze_Axe': # If the stored item is Bronze_Axe
        return Weapons('Bronze_Axe', Level, 'Axe', 5, Multipliers) # Return a Bronze Axe, with saved Level and Multipliers
    elif Name == 'Iron_Axe': # If the stored item is Iron_Axe
        return Weapons('Iron_Axe', Level, 'Axe', 6, Multipliers) # Return an Iron Axe, with saved Level and Multipliers
    elif Name == 'Platinum_Axe': # If the stored item is Platinum_Axe
        return Weapons('Platinum_Axe', Level, 'Axe', 8, Multipliers) # Return a Platinum Axe, with saved Level and Multipliers

    elif Name == 'Wooden_Mace': # If the stored item is Wooden_Mace
        return Weapons('Wooden_Mace', Level, 'Mace', 4, Multipliers) # Return a Wooden Mace, with saved Level and Multipliers
    elif Name == 'Bronze_Mace': # If the stored item is Bronze_Mace
        return Weapons('Bronze_Mace', Level, 'Mace', 5, Multipliers) # Return a Bronze Mace, with saved Level and Multipliers
    elif Name == 'Iron_Mace': # If the stored item is Iron_Mace
        return Weapons('Iron_Mace', Level, 'Mace', 6, Multipliers) # Return an Iron Mace, with saved Level and Multipliers
    elif Name == 'Platinum_Mace': # If the stored item is Platinum_Mace
        return Weapons('Platinum_Mace', Level, 'Mace', 8, Multipliers) # Return a Platinum Mace, with saved Level and Multipliers

    #--- Armour ---
    elif Name == 'None_Helmet': # If no helmet is equipped
        return Armour('None_Helmet', 0, 'Helmet', 0, Multipliers) # Return a default empty Helmet
    elif Name == 'Leather_Helmet': # If the stored item is Leather_Helmet
        return Armour('Leather_Helmet', Level, 'Helmet', 1, Multipliers) # Return a Leather Helmet, with saved Level and Multipliers
    elif Name == 'Bronze_Helmet': # If the stored item is Bronze_Helmet
        return Armour('Bronze_Helmet', Level, 'Helmet', 2, Multipliers) # Return a Bronze Helmet, with saved Level and Multipliers
    elif Name == 'Iron_Helmet': # If the stored item is Iron_Helmet
        return Armour('Iron_Helmet', Level, 'Helmet', 3, Multipliers) # Return an Iron Helmet, with saved Level and Multipliers
    elif Name == 'Platinum_Helmet': # If the stored item is Platinum_Helmet
        return Armour('Platinum_Helmet', Level, 'Helmet', 4, Multipliers) # Return a Platinum Helmet, with saved Level and Multipliers

    elif Name == 'None_Chestplate': # If no chestplate is equipped
        return Armour('None_Chestplate', 0, 'ChestPlate', 0, Multipliers) # Return a default empty ChestPlate
    elif Name == 'Leather_Chestplate': # If the stored item is Leather_Chestplate
        return Armour('Leather_Chestplate', Level, 'ChestPlate', 1, Multipliers) # Return a Leather Chestplate, with saved Level and Multipliers
    elif Name == 'Bronze_Chestplate': # If the stored item is Bronze_Chestplate
        return Armour('Bronze_Chestplate', Level, 'ChestPlate', 2, Multipliers) # Return a Bronze Chestplate, with saved Level and Multipliers
    elif Name == 'Iron_Chestplate': # If the stored item is Iron_Chestplate
        return Armour('Iron_Chestplate', Level, 'ChestPlate', 3, Multipliers) # Return an Iron Chestplate, with saved Level and Multipliers
    elif Name == 'Platinum_Chestplate': # If the stored item is Platinum_Chestplate
        return Armour('Platinum_Chestplate', Level, 'ChestPlate', 4, Multipliers) # Return a Platinum Chestplate, with saved Level and Multipliers

    elif Name == 'None_Boot': # If no boots are equipped
        return Armour('None_Boot', 0, 'Boot', 0, Multipliers) # Return default empty Boots
    elif Name == 'Leather_Boot': # If the stored item is Leather_Boot
        return Armour('Leather_Boot', Level, 'Boot', 1, Multipliers) # Return Leather Boots, with saved Level and Multipliers
    elif Name == 'Bronze_Boot': # If the stored item is Bronze_Boot
        return Armour('Bronze_Boot', Level, 'Boot', 2, Multipliers) # Return Bronze Boots, with saved Level and Multipliers
    elif Name == 'Iron_Boot': # If the stored item is Iron_Boot
        return Armour('Iron_Boot', Level, 'Boot', 3, Multipliers) # Return Iron Boots, with saved Level and Multipliers
    elif Name == 'Platinum_Boot': # If the stored item is Platinum_Boot
        return Armour('Platinum_Boot', Level, 'Boot', 4, Multipliers) # Return Platinum Boots, with saved Level and Multipliers

    #--- Items/Potions ---
    elif Name == 'None': # If slot is empty or nothing equipped
        return Item('None', 0) # Return a basic empty item

    elif Name == 'Health_Potion_Small': # If the stored item is Health_Potion_Small
        return Potion('Health_Potion_Small', Level, 'Health', 10) # Return a small health potion healing 10
    elif Name == 'Health_Potion_Medium': # If the stored item is Health_Potion_Medium
        return Potion('Health_Potion_Medium', Level, 'Health', 25) # Return a medium health potion healing 25
    elif Name == 'Health_Potion_Large': # If the stored item is Health_Potion_Large
        return Potion('Health_Potion_Large', Level, 'Health', 50) # Return a large health potion healing 50

    elif Name == 'Stamina_Potion_Small': # If the stored item is Stamina_Potion_Small
        return Potion('Stamina_Potion_Small', Level, 'Stamina', 10) # Return a small stamina potion restoring 10
    elif Name == 'Stamina_Potion_Medium': # If the stored item is Stamina_Potion_Medium
        return Potion('Stamina_Potion_Medium', Level, 'Stamina', 25) # Return a medium stamina potion restoring 25
    elif Name == 'Stamina_Potion_Large': # If the stored item is Stamina_Potion_Large
        return Potion('Stamina_Potion_Large', Level, 'Stamina', 50) # Return a large stamina potion restoring 50

    elif Name == 'Mana_Potion_Small': # If the stored item is Mana_Potion_Small
        return Potion('Mana_Potion_Small', Level, 'Mana', 10) # Return a small mana potion restoring 10
    elif Name == 'Mana_Potion_Medium': # If the stored item is Mana_Potion_Medium
        return Potion('Mana_Potion_Medium', Level, 'Mana', 25) # Return a medium mana potion restoring 25
    elif Name == 'Mana_Potion_Large': # If the stored item is Mana_Potion_Large
        return Potion('Mana_Potion_Large', Level, 'Mana', 50) # Return a large mana potion restoring 50

    else: # If item name is not recognized
        return None_Item # Return a fallback None_Item object

def Load_Enemies(G, O, D, Og):
    '''Since JSON files cant store classes, this function loads variable Enemy data into the Enemy'''
    global Goblin, Orc, Druid, Ogre # Globalises the Enemies
    Goblin = Enemy('Goblin', G, 10, 5, 'Fir', 1) # Creates Goblin with the Saved Health Attribute
    Orc = Enemy('Orc', O, 20, 7, 'Wat', 8) # Creates Orc with the Saved Health Attribute
    Druid = Enemy('Druid', D, 20, 12, 'Nat', 16) # Creates Druid with the Saved Health Attribute
    Ogre = Enemy('Ogre', Og, 50, 10, 'Fir', 20) # Creates Ogre with the Saved Health Attribute

#--- Variables ---
User = None # Creates the User Tag

Load_File = 0 # Predefines the Load File to be 0 - No Load_File

#--- Items ---
Stick = Weapons('Stick', 1, 'Stick', 2) # Creates a Weapon named Stick that does 2 damage

# Swords
Wooden_Sword = Weapons('Wooden_Sword', 3, 'Sword', 4) # Creates a Sword named Wooden_Sword that does 4 damage
Bronze_Sword = Weapons('Bronze_Sword', 6, 'Sword', 5) # Creates a Sword named Bronze_Sword that does 5 damage
Iron_Sword = Weapons('Iron_Sword', 12, 'Sword', 6) # Creates a Sword named Iron_Sword that does 6 damage
Platinum_Sword = Weapons('Platinum_Sword', 16, 'Sword', 8) # Creates a Sword named Platinum_Sword that does 8 damage

# Axes
Wooden_Axe = Weapons('Wooden_Axe', 3, 'Axe', 4) # Creates an Axe named Wooden_Axe that does 4 damage
Bronze_Axe = Weapons('Bronze_Axe', 6, 'Axe', 5) # Creates an Axe named Bronze_Axe that does 5 damage
Iron_Axe = Weapons('Iron_Axe', 12, 'Axe', 6) # Creates an Axe named Iron_Axe that does 6 damage
Platinum_Axe = Weapons('Platinum_Axe', 16, 'Axe', 8) # Creates an Axe named Platinum_Axe that does 8 damage

# Maces
Wooden_Mace = Weapons('Wooden_Mace', 3, 'Mace', 4) # Creates a Mace named Wooden_Mace that does 4 damage
Bronze_Mace = Weapons('Bronze_Mace', 6, 'Mace', 5) # Creates a Mace named Bronze_Mace that does 5 damage
Iron_Mace = Weapons('Iron_Mace', 12, 'Mace', 6) # Creates a Mace named Iron_Mace that does 6 damage
Platinum_Mace = Weapons('Platinum_Mace', 16, 'Mace', 8) # Creates a Mace named Platinum_Mace that does 8 damage

#--- Armour ---
# Helmet
None_Helmet = Armour('None_Helmet', 0, 'Helmet', 0) # Creates a Helmet named None_Helmet that provides 0 protection
Leather_Helmet = Armour('Leather_Helmet', 1, 'Helmet', 1) # Creates a Helmet named Leather_Helmet that provides 1 protection
Bronze_Helmet = Armour('Bronze_Helmet', 3, 'Helmet', 2) # Creates a Helmet named Bronze_Helmet that provides 2 protection
Iron_Helmet = Armour('Iron_Helmet', 6, 'Helmet', 3) # Creates a Helmet named Iron_Helmet that provides 3 protection
Platinum_Helmet = Armour('Platinum_Helmet', 10, 'Helmet', 4) # Creates a Helmet named Platinum_Helmet that provides 4 protection

# ChestPlate
None_Chestplate = Armour('None_Chestplate', 0, 'ChestPlate', 0) # Creates a ChestPlate named None_Chestplate that provides 0 protection
Leather_Chestplate = Armour('Leather_Chestplate', 1, 'ChestPlate', 1) # Creates a ChestPlate named Leather_Chestplate that provides 1 protection
Bronze_Chestplate = Armour('Bronze_Chestplate', 3, 'ChestPlate', 2) # Creates a ChestPlate named Bronze_Chestplate that provides 2 protection
Iron_Chestplate = Armour('Iron_Chestplate', 6, 'ChestPlate', 3) # Creates a ChestPlate named Iron_Chestplate that provides 3 protection
Platinum_Chestplate = Armour('Platinum_Chestplate', 10, 'ChestPlate', 4) # Creates a ChestPlate named Platinum_Chestplate that provides 4 protection

# Boot
None_Boot = Armour('None_Boot', 0, 'Boot', 0) # Creates a Boot named None_Boot that provides 0 protection
Leather_Boot = Armour('Leather_Boot', 1, 'Boot', 1) # Creates a Boot named Leather_Boot that provides 1 protection
Bronze_Boot = Armour('Bronze_Boot', 3, 'Boot', 2) # Creates a Boot named Bronze_Boot that provides 2 protection
Iron_Boot = Armour('Iron_Boot', 6, 'Boot', 3) # Creates a Boot named Iron_Boot that provides 3 protection
Platinum_Boot = Armour('Platinum_Boot', 10, 'Boot', 4) # Creates a Boot named Platinum_Boot that provides 4 protection

# Items
None_Item = Item('None', 0) # Creates an Item named None

# Potions
Health_Potion_Small = Potion('Health_Potion_Small', 1, 'Health', 10) # Creates a Potion named Health_Potion_Small that replenishes 10 Health
Health_Potion_Medium = Potion('Health_Potion_Medium', 3, 'Health', 25) # Creates a Potion named Health_Potion_Medium that replenishes 25 Health
Health_Potion_Large = Potion('Health_Potion_Large', 5, 'Health', 50) # Creates a Potion named Health_Potion_Large that replenishes 50 Health

Stamina_Potion_Small = Potion('Stamina_Potion_Small', 1, 'Stamina', 10) # Creates a Potion named Stamina_Potion_Small that replenishes 10 Stamina
Stamina_Potion_Medium = Potion('Stamina_Potion_Medium', 3, 'Stamina', 25) # Creates a Potion named Stamina_Potion_Medium that replenishes 25 Stamina
Stamina_Potion_Large = Potion('Stamina_Potion_Large', 5, 'Stamina', 50) # Creates a Potion named Stamina_Potion_Large that replenishes 50 Stamina

Mana_Potion_Small = Potion('Mana_Potion_Small', 1, 'Mana', 10) # Creates a Potion named Mana_Potion_Small that replenishes 10 Mana
Mana_Potion_Medium = Potion('Mana_Potion_Medium', 3, 'Mana', 25) # Creates a Potion named Mana_Potion_Medium that replenishes 25 Mana
Mana_Potion_Large = Potion('Mana_Potion_Large', 5, 'Mana', 50) # Creates a Potion named Mana_Potion_Large that replenishes 50 Mana

# Creation of Goblin King Enemy (This does not need to be saved, as once the User has interacted with the Boss, that is the end of their run)
Goblin_King = Enemy('Goblin_King', 100, 100, 15, 'Fir', 100)

#--- Functions ---
# Combat
def Combat(Enemy, Room):
    '''This Function handles the Combat between the Player and an Enemy'''
    global Exited, User  # Uses the Global Exited Variable

    def Attack():
        User.Attacking(Enemy)

    if Enemy.type == 'Fir':  # If the Enemy is Fire Type
        Type = 'Fire'  # Set Type to Fire
    elif Enemy.type == 'Wat':  # If the Enemy is Water Type
        Type = 'Water'  # Set Type to Water
    elif Enemy.type == 'Nat':  # If the Enemy is Nature Type
        Type = 'Nature'  # Set Type to Nature

    print(f"You have Encountered a {Enemy.name}")  # Informs the Player of the Enemy they have encountered

    while True:  # Runs the Combat Loop until someone wins or loses
        Exited = False  # Reset Exited at the start of each loop
        print(f"""
    +-----------------------------------------------+
    |{' '*21}Enemy{' '*21}|
    +-----------------------------------------------+
    {Enemy.name}: 
        Health:  ♥️  \033[31m{StatBar(Enemy.health, Enemy.max_health)} ({Enemy.health}/{Enemy.max_health})
        Damage:  ⚔️  \033[34m{Enemy.damage}\033[0m
        Type:    ☯️  \033[33m{Type}\033[0m

    {User.Player_Name}:
        Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} ({User.Health['Health']}/{User.Health['Max_Health']})
        Damage:  ⚔️  \033[34m{User.WeaponSlot.damage}\033[0m
        Elemental Damage:        ☯️  \033[33m{User.WeaponSlot.multiplyers[Enemy.type]}\033[0m
        Elemental Protection:    ☯️  \033[33m{round((User.HelmetSlot.multiplyers[Enemy.type] + User.ChestplateSlot.multiplyers[Enemy.type] + User.BootSlot.multiplyers[Enemy.type]) / 3)}\033[0m
        """) # Displays Full Combat UI with Stats for Both the Player and Enemy

        if Enemy.health <= 0:  # If the Enemy has run out of Health
            if Room != 'GoblinKing': # If the Player is not battling GoblinKing
                ClearLines(17)  # Clears the Combat UI
                print(f"You have defeated the {Enemy.name}!")  # Informs the Player they won
                User.WeaponSlot.level += Enemy.level / 2  # Increases the Weapon Level by Half the Enemy Level
                input("Press Enter to continue...")
                ClearLines(1)
                break  # Breaks the Loop

            else:
                DefeatedGK()

        elif User.Health['Health'] <= 0:  # If the Player has run out of Health
            Died(Enemy.name)
            break

        Input_Selection({
            "Attack": lambda: Attack(),  # Attacks the Enemy
            "Use Item": lambda: DisplayInventoryScreen()  # Opens Inventory to Use Items
        })

            # After using an item, Exited may be set to True, so check before enemy attacks
        if Exited:
            pass
        else:
            Enemy.Attacking(User)  # The Enemy Attacks the Player

        ClearLines(20)  # Clears the Combat UI before Refreshing

# UI
def PrintMainUI(Room):
    '''This Function combines a variety of other functions - and Displays them in the correct way'''
    Exited = False # Sets Exited to False
    os.system('cls') # Clears the Screen
    
    if User.Health['Health'] <= 0: # If the User has ran out of Health
        Died('No Health') # Run the Player has Died due to No health
    elif User.Stamina['Stamina'] <= 0: # If the User has ran out of Stamina
        Died('No Stamina') # Run the Player has Died due to No Stamina
    
    User.Location = Room # Sets the Users Location to be the Current Room    

    map_lines = Map(Room).splitlines() # Splits the Lines from Map
    stats_lines = DisplayStats().splitlines() # Splits the Lines for Stats
    inventory_lines = DisplayInventory().splitlines() # Splits the Lines for Player Inventory
    MapKey_lines = DisplayMapKey().splitlines() # Splits the Line from Map Key

    side_panel = stats_lines + inventory_lines + MapKey_lines # Combines the Lines of each of the elements to be printed on the Side Panel
    max_lines = max(len(map_lines), len(side_panel)) # Calculates which is the Tallest (Map or Side Panel)

    print() # Creates a Spacer in the Terminal

    for i in range(max_lines): # For each line in (Which ever Element had more Lines)
        map_line = map_lines[i] if i < len(map_lines) else "" # Figures out if their is content in the Lines - Else: Sets it to be a Blank line - But a Line that Exists
        side_line = side_panel[i] if i < len(side_panel) else "" # Figures out if their is content in the Lines - Else: Sets it to be a Blank line - But a Line that Exists

        map_width = wcswidth(map_line) # Calculates the Width of the Map line (Accounting for Emojis)
        padding = max(0, 60 - map_width) # Calculates if the Map is Square - If Not - Adds padding
        print(map_line + ' ' * padding + side_line) # Prints the Map Line, then the Padding, then the Side panel line
    
    print() # Creates a Spacer in the Terminal

    print(Story(Room)) # Prints the Story for the Room
    
    print() # Creates a Spacer in the Terminal
    while True: # Run until broken

        if Room == 'GoblinKing':
            break

        elif Exited == False: # If player has Exited
            setattr(User, Room, True) # Set the Room variable for the Player to be True
            Input_Selection(MoveOptions(Room)) # Runs the Input selection for the Room - Based on the Options from MoveOptions
            ClearLines(len(MoveOptions(Room))+3)
            
        else: # If their is a Problem - Breaks the Loop to stop a crash
            break # Breaks the Loop

def StatBar(Stat, Max_Stat):
    '''This function create statbars for statisics'''
    StatBar = (math.floor(Stat/(Max_Stat/10)))*'█' # Calculates how much health their is based on the Stat and Max Stat
    DeadBar = '' # Initalises 'Dead Bar'

    if StatBar == '' and Stat > 0: # Because it rounds down, if the player is alive, but has below 10% health...
        StatBar = '█' # Gives them 1 block of health

    elif len(StatBar) > 10: # If Health is more than 10
        Statbar = '█'*10 # Sets Stat bar to Full
        return Statbar
        

    for i in range(0, 10-len(StatBar)): # Fills up the excess of statbar to Deadbar
        DeadBar += f'-' # Adds a '-' to DeadBar
        
    return StatBar + f'\033[37m{DeadBar}' # returns the completed Bar - Combines the two, and makes the 'Dead Bar' White

def DisplayStats():
    '''This function displates the Stats Block of the UI'''
    return f''' +───────────--==| Stats |==--───────────+
 │                                       │
 │   Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} \033[0m {f'({User.Health['Health']}/{User.Health['Max_Health']})':<12}│
 │   Stamina: 🔋 \033[32m{StatBar(User.Stamina['Stamina'], User.Stamina['Max_Stamina'])} \033[0m {f'({User.Stamina['Stamina']}/{User.Stamina['Max_Stamina']})':<12}│
 │   Mana:    {f'💠 \033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}' if MountainIssue == True else f'💠\033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}'}│
 │                                       │
 +───────────────────────────────────────+''' # The Mana function is different because that is what lines up with the Mountain and causes problems (More context in Map Comment)

def DisplayInventory():
    '''This function returns the Users Inventory in a Asethetic way'''
    return f''' +──────────────────────────────────--==| Inventory |==--──────────────────────────────────+
 │   {'🪙  Gold':<12} -   {User.Gold:<68} │
 │   {'Weapon':<12} -   {User.WeaponSlot.name:<25} {'Chestplate':<12} -   {User.ChestplateSlot.name:<25} │
 │   {'Helmet':<12} -   {User.HelmetSlot.name:<25} {'Boots':<12} -   {User.BootSlot.name:<25} │
 +{'─'*89}+ 
 │   {User.OtherSlot1['Item'].name:<28} -   {User.OtherSlot1['Qty']:<9} {User.OtherSlot2['Item'].name:<28} -   {User.OtherSlot2['Qty']:<9} │
 │   {User.OtherSlot3['Item'].name:<28} -   {User.OtherSlot3['Qty']:<9} {User.OtherSlot4['Item'].name:<28} -   {User.OtherSlot4['Qty']:<9} │
 +{'─'*89}+'''

def DisplayMapKey():
    '''This function returns the Map key - Allowing the User to figure out which symbols mean what'''
    return f''' +─────────────────────────--==| Map Key |==--─────────────────────────+
 │   ██ - You              🔮 - Wizard Tower                           │
 │   🏠 - Village          💀 - Enemy             👑 - Goblin King     │
 │   🌲 - Forest           🏔️  - Mountain                               │
 +─────────────────────────────────────────────────────────────────────+'''

def DisplayInventoryScreen():
    global Exited

    def SetItemUsed():
        global Exited
        Exited = True
        
    print(f'''
    {' '*40}       -= Dmg / Pro =-   -= Fir =-= Wat =-= Nat =-
    WeaponSlot:       {User.WeaponSlot.name:<30}     {User.WeaponSlot.damage:<13}  {str(User.WeaponSlot.multiplyers['Fir'])[:3]:<5}   {str(User.WeaponSlot.multiplyers['Wat'])[:5]:<5}   {str(User.WeaponSlot.multiplyers['Nat'])[:5]:<5}
    HelmetSlot:       {User.HelmetSlot.name:<30}     {User.HelmetSlot.protection:<13}  {str(User.HelmetSlot.multiplyers['Fir'])[:3]:<5}   {str(User.HelmetSlot.multiplyers['Wat'])[:5]:<5}   {str(User.HelmetSlot.multiplyers['Nat'])[:5]:<5}
    ChestplateSlot:   {User.ChestplateSlot.name:<30}     {User.ChestplateSlot.protection:<13}  {str(User.ChestplateSlot.multiplyers['Fir'])[:3]:<5}   {str(User.ChestplateSlot.multiplyers['Wat'])[:5]:<5}   {str(User.ChestplateSlot.multiplyers['Nat'])[:5]:<5}
    BootSlot:         {User.BootSlot.name:<30}     {User.BootSlot.protection:<13}  {str(User.BootSlot.multiplyers['Fir'])[:3]:<5}   {str(User.BootSlot.multiplyers['Wat'])[:5]:<5}   {str(User.BootSlot.multiplyers['Nat'])[:5]:<5}
    
    Gold:             {str(User.Gold)} 🪙
''')
    print('''
Which Item would you like to use?
    ''')
    
    options = {}
    for slot in [User.OtherSlot1, User.OtherSlot2, User.OtherSlot3, User.OtherSlot4]:
        item = slot['Item']
        if item.name != 'None':
            options[f"{item.name:<25} - ({slot['Qty']})"] = lambda item=item: item.Use_Potion(User)
    options['Exit'] = lambda: SetItemUsed()

    
    Input_Selection(options)
        
    ClearLines(15 + len(options))

def TitleScreen():
    '''This Function Handles Displaying and calculating what happens in the TitleScreen'''
    def OverWrite():
        '''This functions handles what to do if the User wants to Overwrite a Save file'''
        print('Which save do you you want to overwrite?') # Instructs the User
        print() # Creates a Spacer in the Terminal
        options = {} # Initalises the Options
        if Player_Data_1: # If Player_Data_1 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 1'] = lambda: (load({}, 1)) # Appends Save 1 to Option and starts creating a character with no attributes to save file 1

        elif Player_Data_2: # If Player_Data_2 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 2'] = lambda: (load({}, 2)) # Appends Save 2 to Option and starts creating a character with no attributes to save file 2

        elif Player_Data_3: # If Player_Data_3 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 3'] = lambda: (load({}, 3)) # Appends Save 3 to Option and starts creating a character with no attributes to save file 3
            
        elif Player_Data_4: # If Player_Data_4 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 4'] = lambda: (load({}, 4)) # Appends Save 4 to Option and starts creating a character with no attributes to save file 4

        options['Exit'] = lambda: TitleScreen() # Appends Exit to Option - Restarting back to Titlescreen

        Input_Selection(options) # Loads Options into Input Selection
                
    os.system('cls') # Clears Screen
    try: # Try to open Save 1 and Append it to Player_Data_1
        with open(f'Save1.json', 'r') as f:
            Player_Data_1 = json.load(f)
    except: # If JSON is blank, sets Player_Data_1 to a Blank Dictionary
        Player_Data_1 = {} # Sets to blank Dictionary
    
    try: # Try to open Save 2 and Append it to Player_Data_2
        with open(f'Save2.json', 'r') as f:
            Player_Data_2 = json.load(f)
    except: # If JSON is blank, sets Player_Data_2 to a Blank Dictionary
        Player_Data_2 = {} # Sets to blank Dictionary

    try: # Try to open Save 3 and Append it to Player_Data_3
        with open(f'Save3.json', 'r') as f:
            Player_Data_3 = json.load(f)
    except: # If JSON is blank, sets Player_Data_3 to a Blank Dictionary
        Player_Data_3 = {} # Sets to blank Dictionary
   
    try: # Try to open Save 4 and Append it to Player_Data_4
        with open(f'Save4.json', 'r') as f:
                Player_Data_4 = json.load(f)
    except: # If JSON is blank, sets Player_Data_4 to a Blank Dictionary
        Player_Data_4 = {} # Sets to blank Dictionary

    # Prints the Title of the Game, and each of the Save Name and Location - If their is no save information - Sets it to None
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


    ''')
    Input_Selection({ # Sends the Dictionary to Input_Selection
         'Save 1': lambda: (load(Player_Data_1, 1)), # Sets Save 1 to Load data from Player_Data_1 to load
         'Save 2': lambda: (load(Player_Data_2, 2)), # Sets Save 2 to Load data from Player_Data_2 to load
         'Save 3': lambda: (load(Player_Data_3, 3)), # Sets Save 3 to Load data from Player_Data_3 to load
         'Save 4': lambda: (load(Player_Data_4, 4)), # Sets Save 4 to Load data from Player_Data_4 to load
         'OverWrite Save': lambda: OverWrite(), # If player Wants to OverWrite a Save - OverWrites it
         'Exit': lambda: quit() # If the player wants to leave, quits the program
    })

    PrintMainUI(User.Location) # Starts to Game Based of the Users Location

def Input_Selection(options: dict): # ":dict" - Ensures it is a Dictionary
    '''This function handles the Input selection process for a variety of functions in my program'''
    def ReplaceInput():
        '''This function replaces the Input and prints Error Message'''
        ClearLines(2)  # Clears 2 Lines Above
        print('Error With Input') # Error Message
        return get_input()  # Re-prompt's the User for an Input
    
    def get_input():
        '''This function handles recieving Inputs from the User'''
        try: # Try to Recieve and Input from the User
            SaveSelection = input('Choice: ') # Recieve input from User
            SaveSelection = int(SaveSelection) # Check if Input is a Integer
            if 1 <= SaveSelection <= len(option_list): # if Input is an option in avaliable options
                option_list[SaveSelection - 1][1]()  # Call the corresponding function
            else: # If it is not an Option
                ReplaceInput() # Give an Error Message
        except Exception: # If error with Input (but not SystemExit)
            ReplaceInput() # Give an Error Message

    # Print options
    option_list = list(options.items()) # Option List is List of Dictionary
    print("Select an option:") # Directs User
    for i, (name, _) in enumerate(option_list, start=1): # For Each Option in option list, display the Item and its associated value
        print(f"{i}. {name}")  # Prints the Number and the Name of the function it is associated to
    print() # Creates a Spacer in the Terminal
    get_input() # Runs Recieve Input

# Player Functions
def load(Player_Data, Save):
    '''Loads Player Data from the JSON to the format for creating a Player'''
    global User, Load_File # Globalises the User and Load file Attributes

    Load_File = Save # Sets the Load File

    if len(Player_Data) == 0: # If their is no save data
        CreateCharacter() # Create a Character

    else: # Convert the information from the JSON file to a dictionary to create the player
        Data = { # Creates a dictionary to store all player data
        'Player_Name': Player_Data['Player_Name'], # Stores the player's name

        'Health': Player_Data['Health'], # Stores current and max health
        'Stamina': Player_Data['Stamina'], # Stores current and max stamina
        'Mana': Player_Data['Mana'], # Stores current and max mana

        'Location': Player_Data['Location'], # Stores the last known location
        'Gold': Player_Data['Gold'], # Stores the player's gold amount

        'WeaponSlot': Load_Items(Player_Data['WeaponSlot']['Name'], Player_Data['WeaponSlot']['Level'], Player_Data['WeaponSlot']['Multiplyers']), # Loads the weapon item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'HelmetSlot': Load_Items(Player_Data['HelmetSlot']['Name'], Player_Data['HelmetSlot']['Level'], Player_Data['HelmetSlot']['Multiplyers']), # Loads the helmet item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'ChestplateSlot': Load_Items(Player_Data['ChestplateSlot']['Name'], Player_Data['ChestplateSlot']['Level'], Player_Data['ChestplateSlot']['Multiplyers']), # Loads the chestplate item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'BootSlot': Load_Items(Player_Data['BootSlot']['Name'], Player_Data['BootSlot']['Level'], Player_Data['BootSlot']['Multiplyers']), # Loads the boots item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        
        'OtherSlot1': {'Item': Load_Items(Player_Data['OtherSlot1']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot1']['Qty']}, # Loads item in OtherSlot1 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot2': {'Item': Load_Items(Player_Data['OtherSlot2']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot2']['Qty']}, # Loads item in OtherSlot2 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot3': {'Item': Load_Items(Player_Data['OtherSlot3']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot3']['Qty']}, # Loads item in OtherSlot3 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot4': {'Item': Load_Items(Player_Data['OtherSlot4']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot4']['Qty']}, # Loads item in OtherSlot4 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        
        'Enemy1': Player_Data['Enemy1'], # Tracks if Enemy1 has been visted
        'Enemy2': Player_Data['Enemy2'], # Tracks if Enemy2 has been visted
        'Enemy3': Player_Data['Enemy3'], # Tracks if Enemy3 has been visted
        'Enemy4': Player_Data['Enemy4'], # Tracks if Enemy4 has been visted

        'Village1': Player_Data['Village1'], # Tracks if Village1 has been visited
        'Village2': Player_Data['Village2'], # Tracks if Village2 has been visited
        'Village3': Player_Data['Village3'], # Tracks if Village3 has been visited

        'Forest1': Player_Data['Forest1'], # Tracks if Forest1 has been visited
        'Forest2': Player_Data['Forest2'], # Tracks if Forest2 has been visited
        'Forest3': Player_Data['Forest3'], # Tracks if Forest3 has been visited
        'Forest4': Player_Data['Forest4'], # Tracks if Forest4 has been visited

        'SeenW1': Player_Data['SeenW1'], # Tracks if the player has met Wizard1
        'SeenW2': Player_Data['SeenW2'], # Tracks if the player has met Wizard2

        'Wizard1': Player_Data['Wizard1'], # Tracks if Wizard1 area has been visted
        'Wizard2': Player_Data['Wizard2'], # Tracks if Wizard2 area has been visted

        'Mountain': Player_Data['Mountain'], # Tracks if the Mountain has been visited

        'GoblinKing': Player_Data['GoblinKing'], # Tracks if Goblin King has been visited

        'RareFlower': Player_Data['RareFlower'], # Tracks if Rare Flower has been collected
        'RareRune': Player_Data['RareRune'], # Tracks if Rare Rune has been collected


        'Enemies': Player_Data['Enemies'] # Stores the state of all enemies
        }


        User = Player(Data) # Creates a new Player object with the loaded data

def CreateCharacter():
    '''This Function Creates a Character if their is no existing player data'''
    global User # Globaises the User Attribute
    print('Welcome New Adventurer!') # Welecomes the User
    while True: # Run until broken
        Name_Input = input("What's your Name Adventurer? ") # Ask's the Player their Name

        if len(Name_Input) == 0: # If User Doesnt Enter a Name
            print("You must enter a name!") # Prints and Error Message
        elif len(Name_Input) > 20: # If the User enters a name that is too long
            print("Your name is too long! Please keep it under 20 characters.") # Prints and Error Message
        else: # If their is no problems with the Users Name
            print(f'Welcome {Name_Input}, This is where your Journey Begins!') # Welcomes user
            break # Breaks the Loop

    Player_Data = { # Initalises Player Data to Defaults
        'Player_Name': Name_Input, # Player Name is set to Players Chosen Name

        'Health': {'Health': 100, 'Max_Health': 100}, # Sets player Health to 100, and Max Health to 100
        'Stamina': {'Stamina': 100, 'Max_Stamina': 100}, # Sets player Stamina to 100, and Max Stamina to 100
        'Mana': {'Mana': 100, 'Max_Mana': 100}, # Sets player Mana to 100, and Max Mana to 100

        'WeaponSlot': Stick, # Sets Users Weapon to Stick
        'HelmetSlot': None_Helmet, # Sets Users Helmet to None_Helmet
        'ChestplateSlot': None_Chestplate, # Sets Users Chestplate to None_Chestplate
        'BootSlot': None_Boot, # Sets Users Boots to None_Boot
        
        'OtherSlot1': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot2': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot3': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot4': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0

        'Location': 'Forest1', # Sets Users location to be 'Forest1' - the Default Room
        'Gold': 25, # Sets Users gold to be 25 - 25 is Enough to make money through the Casino - the Lumberjack is more designed to prevent soft locking

        'Enemy1': False, # Sets Room to be False
        'Enemy2': False, # Sets Room to be False
        'Enemy3': False, # Sets Room to be False
        'Enemy4': False, # Sets Room to be False

        'Village1': False, # Sets Room to be False
        'Village2': False, # Sets Room to be False
        'Village3': False, # Sets Room to be False

        'Forest1': False, # Sets Room to be False
        'Forest2': False, # Sets Room to be False
        'Forest3': False, # Sets Room to be False
        'Forest4': False, # Sets Room to be False


        'SeenW1': False, # Sets Seen Wizard 1 to be False
        'SeenW2': False, # Sets Seen Wizard 2 to be False
        
        'Wizard1': False,  # Sets Room to be False
        'Wizard2': False, # Sets Room to be False
        'Mountain': False, # Sets Room to be False
        'GoblinKing': False, # Sets Room to be False

        'RareFlower': False, # Sets Room to be False
        'RareRune': False, # Sets Room to be False

        'Enemies': {'G': 10, 'O': 20, 'D': 20, 'Og': 50} # Sets Room to be False
    }

    User = Player(Player_Data) # Creates a Player based off of those attributes

# Magic
def Enchantment(item, type=None):
    '''This function Enchants items to be more effective against enemy types'''    
    Level = item.level # Sets level to the Item of the Level being Encahanted

    Multiplyer = (random.randint(0, round(Level)+10)/10) # This calculate the strength of the Enchant - with a higher level allowing for a higher chance of a better enchantment

    if type == None: # If Player wants a Neuteral Buff
        item.setmultipliers({'Wat': (1+((Multiplyer)/4)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1+((Multiplyer)/4))}) # If the Player wants a overall Neutral Buff
    else:
        if type == 'Fir': # If Player wants a Fire Buff 
            item.setmultipliers({'Wat': (1-((Multiplyer)/4)), 'Fir': (1+(Multiplyer)), 'Nat': (1+((Multiplyer)/4))}) # If the Player wants a stronge buff to Fire, but at the cost of Water Strength
        
        elif type == 'Wat': # If Player wants a Water Buff
            item.setmultipliers({'Wat': (1+(Multiplyer)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1-((Multiplyer)/4))}) # If the Player wants a strong buff to Water, but at the cost of Nature Strength
        
        elif type == 'Nat': # If Player wants a Nature Buff
            item.setmultipliers({'Wat': (1+((Multiplyer)/4)), 'Fir': (1-((Multiplyer)/4)), 'Nat': (1+(Multiplyer))}) # If the Player wants a strong buff to Nature, but at the cost of Fire Strenth
# Movement
def MoveOptions(Room):
    '''Curates the Avaliable Moves for the Player based on their current Location'''
    global User  # Access the global User object

    def RemoveStamina(Stamina): 
        '''This function removes stamina from the Player'''
        User.Stamina['Stamina'] -= Stamina  # Removes X stamina from the player

    Default = {
        "Inventory": lambda: DisplayInventoryScreen(),  # Opens the inventory screen
        "Exit": lambda: Exiting()  # Exits the current screen/menu
    }

    def RoomOptions():
        '''Curates the Room Specific Moves'''
        if Room == 'Enemy1':
            return {
                "North East (Enemy2) (6)": lambda: (RemoveStamina(6), PrintMainUI('Enemy2')),  # -6 stamina, loads Enemy2
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),  # -4 stamina, loads Forest2
                "East (Vilage1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),  # -2 stamina, loads Village1
                "West (Forest1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Forest1')),  # -2 stamina, loads Forest1
            }
        elif Room == 'Enemy2':
            return {
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),  # -3 stamina, loads Enemy3
                "South East (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),  # -6 stamina, loads Forest3
                "South West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
                "East (Wizard1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Wizard1')),  # -2 stamina, loads Wizard1
            }
        elif Room == 'Enemy3':
            return {
                "South East (Wizard1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Wizard1')),  # -4 stamina, loads Wizard1
                "South West (Enemy2) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy2')),  # -3 stamina, loads Enemy2
                "West (Mountain) (20)": lambda: (RemoveStamina(20), PrintMainUI('Mountain')),  # -20 stamina, loads Mountain
            }
        elif Room == 'Enemy4':
            return {
                "North West (Forest4) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),  # -8 stamina, loads Village2
                "East (GoblinKing) (4)": lambda: (RemoveStamina(4), PrintMainUI('GoblinKing')),  # -4 stamina, loads GoblinKing
                "West (Village2) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),  # -8 stamina, loads Village2
            }
        elif Room == 'Village1':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village1')),  # Clears 8 lines, enters Village1
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),  # -4 stamina, loads Forest2
                "East (Village2) (5)": lambda: (RemoveStamina(5), PrintMainUI('Village2')),  # -5 stamina, loads Village2
                "West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
            }
        elif Room == 'Village2':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village2')),  # Clears 8 lines, enters Village2
                "South East (Wizard2) (7)": lambda: (RemoveStamina(7), PrintMainUI('Wizard2')),  # -7 stamina, loads Wizard2
                "East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),  # -5 stamina, loads Enemy4
                "West (Village1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),  # -2 stamina, loads Village1
            }
        elif Room == 'Village3':
            return {
                "Enter Village": lambda: (ClearLines(5), EnterVillage('Village1')),  # Clears 5 lines, enters Village1
                "North West (Forest4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest4')),  # -4 stamina, loads Forest4
            }
        elif Room == 'Forest1':
            return {
                "East (Enemy) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
            }
        elif Room == 'Forest2':
            if User.SeenW1:
                User.RareFlower = True  # Player receives a rare flower
                print('''
        You found a Rare Flower!
                ''')
            return {
                "North East (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),  # -4 stamina, loads Village1
                "North West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),  # -4 stamina, loads Enemy1
            }
        elif Room == 'Forest3':
            return {
                "North East (Forest4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Forest4')),  # -5 stamina, loads Forest4
                "North West (Enemy2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy2')),  # -4 stamina, loads Enemy2
                "East (Enemy4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),  # -4 stamina, loads Enemy4
                "West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),  # -4 stamina, loads Enemy1
            }
        elif Room == 'Forest4':
            return {
                "South East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),  # -5 stamina, loads Enemy4
                "South West (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),  # -6 stamina, loads Forest3
                "East (Village3) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village3')),  # -4 stamina, loads Village3
            }
        elif Room == 'Wizard1':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard1'),  # Enters Wizard1's tower
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),  # -3 stamina, loads Enemy3
                "West (Enemy2) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy2')),  # -2 stamina, loads Enemy2
            }
        elif Room == 'Wizard2':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard2'),  # Enters Wizard2's tower
                "North East (Village2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village2')),  # -4 stamina, loads Village2
                "North West (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),  # -4 stamina, loads Village1
            }
        elif Room == 'Mountain':
            if User.SeenW2:
                User.RareRune = True  # Player receives a rare rune
                print('''
        You found a Rare Rune!
                ''')
            return {
                "East (Enemy3) (10)": lambda: (RemoveStamina(10), PrintMainUI('Enemy3')),  # -10 stamina, loads Enemy3
            }
        elif Room == 'GoblinKing':
            return {
                "West (Enemy 4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),  # -4 stamina, loads Enemy4
            }
        else:
            return {}  # If no known room, return empty movement options

    options = {}  # Initialize the options dictionary
    options.update(Default)  # Add inventory and exit options
    options.update(RoomOptions())  # Add movement options for the current room
    return options  # Return all available options

def Story(Room):    
    '''
    This function handles the story events based on the current Room the Player is in.
    It checks whether the Player has already visited the Room, and triggers combat if it is the first encounter
    with an enemy. Otherwise, it returns a descriptive story message for the area.
    '''
    
    # Enemy Encounter: Goblin
    if Room == 'Enemy1':  # The function is requesting the storyline for room Enemy1
        if User.Enemy1 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Goblin, 'Enemy1')  # Start combat with the Goblin
            return ''
        else:  # The user has been in this room before
            return '''Ash and smoke linger in the air, the battlefield now eerily quiet. You remember the heat of combat, and the pain it brought.'''

    # Enemy Encounter: Orc
    elif Room == 'Enemy2':  # The function is requesting the storyline for room Enemy2
        if User.Enemy2 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Orc, 'Enemy2')  # Start combat with the Orc
            return ''
        else:  # The user has been in this room before
            return '''The blue blood still stains the earth. You breathe heavily, remembering the brute strength of the Orc and your narrow survival.'''

    # Enemy Encounter: Druid
    elif Room == 'Enemy3':  # The function is requesting the storyline for room Enemy3
        if User.Enemy3 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Druid, 'Enemy3')  # Start combat with the Druid
            return ''
        else:  # The user has been in this room before
            return '''A circle of withered trees marks the place where the Druid fell. The silence feels sacred now, almost like a grave.'''

    # Enemy Encounter: Ogre
    elif Room == 'Enemy4':  # The function is requesting the storyline for room Enemy4
        if User.Enemy4 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Ogre, 'Enemy4')  # Start combat with the Ogre
            return ''
        else:  # The user has been in this room before
            return '''You stare into the distance, the final road ahead. This was the last guardian before the Goblin King. Are you truly ready?'''

    # Village 1
    elif Room == 'Village1':  # The function is requesting the storyline for room Village1
        if User.Village1 == False:  # The user has not been in this room before
            return '''You step into a lively village where children laugh and fires crackle. Peace, it seems, still exists in this world.'''
        else:  # The user has been in this room before
            return '''The village greets you like an old friend. The same smiles, the same warmth — a comforting familiarity.'''

    # Village 2
    elif Room == 'Village2':  # The function is requesting the storyline for room Village2
        if User.Village2 == False:  # The user has not been in this room before
            return '''You enter a quiet village under dark clouds. Every shadow feels longer, every glance colder — danger is in the air.'''
        else:  # The user has been in this room before
            return '''The uneasy tension remains. Though it's quiet, you can’t shake the feeling that something watches from the trees.'''

    # Village 3
    elif Room == 'Village3':  # The function is requesting the storyline for room Village3
        if User.Village3 == False:  # The user has not been in this room before
            return '''A haunting wind whistles between crooked houses. You wonder how people survive out here, so far from the known world.'''
        else:  # The user has been in this room before
            return '''The villagers wave to you, their faces lit by warm fires. You smile — even in isolation, kindness endures.'''

    # Forest 1 (Starting Point)
    elif Room == 'Forest1':  # The function is requesting the storyline for room Forest1
        if User.Forest1 == False:  # The user has not been in this room before
            return '''Your eyes flutter open among twisted trees and mist. A worn pouch of gold sits beside you, and a crooked stick gleams faintly nearby.'''
        else:  # The user has been in this room before
            return '''You return to where it all began. The darkness of the forest no longer scares you — it feels like home.'''

    # Forest 2
    elif Room == 'Forest2':  # The function is requesting the storyline for room Forest2
        if User.Forest2 == False:  # The user has not been in this room before
            return '''Bright blossoms dot the forest floor. For a moment, the beauty distracts you from the weight of your journey.'''
        else:  # The user has been in this room before
            return '''You pluck a flower and smile. Among all this chaos, even nature finds time to bloom.'''

    # Forest 3 (Center of the World)
    elif Room == 'Forest3':  # The function is requesting the storyline for room Forest3
        if User.Forest3 == False:  # The user has not been in this room before
            return '''Strangely calm, the center of the world offers no grand treasure or battle — just peace, and a whisper of serenity.'''
        else:  # The user has been in this room before
            return '''Returning here eases your mind. The silence heals, and you consider staying... just a little longer.'''

    # Forest 4
    elif Room == 'Forest4':  # The function is requesting the storyline for room Forest4
        if User.Forest4 == False:  # The user has not been in this room before
            return '''After a long hike, you crest a hill to find endless mountains stretching beneath a golden sky. The wind is crisp, the view breathtaking.'''
        else:  # The user has been in this room before
            return '''The wind greets you again as you look out across the vast wilds. Some things never lose their wonder.'''

    # Wizard Tower 1
    elif Room == 'Wizard1':  # The function is requesting the storyline for room Wizard1
        if User.Wizard1 == False:  # The user has not been in this room before
            return '''A crooked stone tower leans impossibly to one side. How it still stands is beyond reason or physics.'''
        else:  # The user has been in this room before
            return '''The tower creaks in the wind, still standing against all odds. You wonder how many more visits it can endure.'''

    # Wizard Tower 2
    elif Room == 'Wizard2':  # The function is requesting the storyline for room Wizard2
        if User.Wizard2 == False:  # The user has not been in this room before
            return '''The second tower is even stranger — half-buried, with missing stones and an angle so steep it defies gravity.'''
        else:  # The user has been in this room before
            return '''Each time you gaze upon this broken tower, you're filled with both dread and awe — magic, no doubt, is involved.'''

    # Mountain Peak
    elif Room == 'Mountain':  # The function is requesting the storyline for room Mountain
        if User.Mountain == False:  # The user has not been in this room before
            return '''You climb higher than you ever have. The biting wind stings your face, but the sight of endless snow is unforgettable.'''
        else:  # The user has been in this room before
            return '''You trudge through the snow again. Nothing has changed — white, cold, endless. Why did you return?'''

    # Final Battle: Goblin King
    elif Room == 'GoblinKing':  # The function is requesting the storyline for room GoblinKing
        Combat(Goblin_King, 'GoblinKing')
        return''
    
def Map(Room):
    global MountainIssue
    if Room == 'Mountain': # If the Room is Mountain
        MountainIssue = True # Mountain Issue is True (This is because the Mountain Emoji's are some of the only emoji's that are 2 character symbols long - But created the issue where it would skew the UI elements, not in the part adjectent to the map, but at the next part Ascii Component)
    else: # If room isn't mountain
        MountainIssue = False # Sets MountainIssue to False

    def pad(symbol, width=2):
        '''This function uses wcswidth to adjust the Emojis to better calculate the width'''
        real_width = wcswidth(symbol)
        return symbol + ' ' * (width - real_width)

    Enemy1 = pad('💀') if Room != 'Enemy1' else pad('██') # If room is Enemy1, changes the Room Icon to the Player Icon
    Enemy2 = pad('💀') if Room != 'Enemy2' else pad('██') # If room is Enemy2, changes the Room Icon to the Player Icon
    Enemy3 = pad('💀') if Room != 'Enemy3' else pad('██') # If room is Enemy3, changes the Room Icon to the Player Icon
    Enemy4 = pad('💀') if Room != 'Enemy4' else pad('██') # If room is Enemy4, changes the Room Icon to the Player Icon
    Village1 = pad('🏠') if Room != 'Village1' else pad('██') # If room is Village1, changes the Room Icon to the Player Icon
    Village2 = pad('🏠') if Room != 'Village2' else pad('██') # If room is Village2, changes the Room Icon to the Player Icon
    Village3 = pad('🏠') if Room != 'Village3' else pad('██') # If room is Village3, changes the Room Icon to the Player Icon
    Forest1 = pad('🌲') if Room != 'Forest1' else pad('██') # If room is Forest1, changes the Room Icon to the Player Icon
    Forest2 = pad('🌲') if Room != 'Forest2' else pad('██') # If room is Forest2, changes the Room Icon to the Player Icon
    Forest3 = pad('🌲') if Room != 'Forest3' else pad('██') # If room is Forest3, changes the Room Icon to the Player Icon
    Forest4 = pad('🌲') if Room != 'Forest4' else pad('██') # If room is Forest4, changes the Room Icon to the Player Icon
    Wizard1 = pad('🔮') if Room != 'Wizard1' else pad('██') # If room is Wizard1, changes the Room Icon to the Player Icon
    Wizard2 = pad('🔮') if Room != 'Wizard2' else pad('██') # If room is Wizard2, changes the Room Icon to the Player Icon
    Mountain = pad('🏔️ ') if Room != 'Mountain' else pad('██') # If room is Mountain, changes the Room Icon to the Player Icon
    GoblinKing = pad('👑') if Room != 'GoblinKing' else pad('██') # If room is GoblinKing, changes the Room Icon to the Player Icon

    def TitleGenerator(Title):
        '''This function creates a centered title for each of the Rooms, being able to adapt to the length of the title''' 
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+' # Math to calculate the Center and have everything fit

    # This returns the Map, with each of the Locations attcaked with their variables - This system - While more complex - is significantly more efficient in creating the map
    return f'''    {TitleGenerator(Room)}
    │                                                       │
    │           ┌──────{Enemy3}          {Forest4} ────┐                 │
    │           │       │           │     │                 │
    │     {Mountain} ───┘       │           │     │                 │
    │                   │           │     └────{Village3}           │
    │               {Enemy2} ─┴────{Wizard1}     │                       │
    │                │              │                       │
    │        ┌───────┴────────┬─────┤                       │
    │        │                │     └───────┐               │
    │ {Forest1}────{Enemy1}      {Village1}       {Forest3}             ├────{Enemy4} ────{GoblinKing}  │
    │        │       │            {Village2} ───────┘               │
    │        └────┬──┴──┬──────────┘                        │
    │             │     │                                   │
    │             │     └──┐                                │
    │             │        │                                │
    │        {Forest2} ──┘        │                             ⬆  │
    │                      └────────────{Wizard2}               N  │
    │                                                       │
    +───────────────────────────────────────────────────────+'''

def EnterVillage(Village):
    '''This function handles the process of creating villagers, and displaying them in the Village'''

    Mort = ArmourSmith('Mort') # Creates an ArmourSmith named Mort
    Alex = AxeSmith('Alex') # Creates an AxeSmith named Alex
    Melvin = Brewer('Melvin') # Creates a Brewer named Melvin
    Zuba = LumberJack('Zuba') # Creates a LumberJack named Zuba

    Bill = Gambler('Bill') # Creates a Gambler named Bill

    Julian = ArmourSmith('Julian') # Creates an ArmourSmith named Julian
    Gloria = SwordSmith('Gloria') # Creates a SwordSmith named Gloria
    Marty = AxeSmith('Marty') # Creates an AxeSmith named Marty
    Kowalski = Brewer('Kowalski') # Creates a Brewer named Kowalski
    Moto = LumberJack('Moto') # Creates a LumberJack named Moto

    Dole = Gambler('Dole') # Creates a Gambler named Dole

    Maurice = ArmourSmith('Maurice') # Creates an ArmourSmith named Maurice
    Rico = SwordSmith('Rico') # Creates a SwordSmith named Rico
    Skipper = Brewer('Skipper') # Creates a Brewer named Skipper
    Milton = LumberJack('Milton') # Creates a LumberJack named Milton

    Doh = Gambler('Doh') # Creates a Gambler named Doh

    while True: # Continuously loop until the player chooses to exit
        os.system('cls') # Clears the terminal screen
        print('Select a Merchant to Interact With!') # Prompts the user to select a merchant
        print() # Prints a blank line for spacing

        Exiting = False # Initializes the exiting flag as False

        def Break():
            '''This function handles when the User wants to exit the Village'''
            nonlocal Exiting # Allows modification of the Exiting variable from the outer scope
            os.system('cls') # Clears the terminal screen
            print() # Prints a blank line for spacing
            print('Select a Merchant to Interact With!') # Re-prompts the user after exiting
            print() # Prints a blank line for spacing
            Exiting = True # Sets the exiting flag to True

        if Village == 'Village1': # If the player is in Village1
            Input_Selection({ # Displays the merchant options for Village1
                'Mort - Armoursmith': lambda: Mort.Inventory_Trading(), # Opens Mort's armour shop
                'Alex - Axesmith': lambda: Alex.Inventory_Trading(), # Opens Alex's axe shop
                'Melvin - Brewer': lambda: Melvin.Inventory_Trading(), # Opens Melvin's potion shop
                'Zuba - LumberJack': lambda: Zuba.ChopWood(), # Starts Zuba's woodcutting activity
                'Bill - Casino Owner': lambda: Bill.Casino(), # Enters Bill's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

        elif Village == 'Village2': # If the player is in Village2
            Input_Selection({ # Displays the merchant options for Village2
                'Julian - Armoursmith': lambda: Julian.Inventory_Trading(), # Opens Julian's armour shop
                'Gloria - Swordsmith': lambda: Gloria.Inventory_Trading(), # Opens Gloria's sword shop
                'Marty - Axesmith': lambda: Marty.Inventory_Trading(), # Opens Marty's axe shop
                'Kowalski - Brewer': lambda: Kowalski.Inventory_Trading(), # Opens Kowalski's potion shop
                'Moto - LumberJack': lambda: Moto.ChopWood(), # Starts Moto's woodcutting activity
                'Dole - Casino Owner': lambda: Dole.Casino(), # Enters Dole's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

        elif Village == 'Village3': # If the player is in Village3
            Input_Selection({ # Displays the merchant options for Village3
                'Maurice - Armoursmith': lambda: Maurice.Inventory_Trading(), # Opens Maurice's armour shop
                'Rico - Swordsmith': lambda: Rico.Inventory_Trading(), # Opens Rico's sword shop
                'Skipper - Brewer': lambda: Skipper.Inventory_Trading(), # Opens Skipper's potion shop
                'Milton - LumberJack': lambda: Milton.ChopWood(), # Starts Milton's woodcutting activity
                'Doh - Casino Owner': lambda: Doh.Casino(), # Enters Doh's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

    PrintMainUI(Village) # Returns the user back to the main UI of the current village

def EnterWizardTower(wizard_room):
    '''This Function handles the Wizard Tower Interactions, and Ensuring a Wizard is Intialised'''
    Jake = Wizard('Jake') # Since the Name of the Wizard is Irrelivent for the Wizard function, the rooms can share the same Wizard Object

    Jake.WizardStore(wizard_room) # Runs the Wizard Store function, also providing which room it is happening in, allowing the Function to differenciate between the two rooms

def ClearLines(n):
    '''This function allows me to clear lines by the specified amount'''
    for _ in range(n): # For each of the lines specified in the Parameters
        print("\033[1A\033[2K", end="") # Clear the most recent line

def Exiting():
    '''Handles the Exiting of the Game back to the Titlescreen'''
    global Load_File, User # Globaises the Varibales
    User.Save(Load_File) # Saves the Users Progress
    User = None # Resets the User
    Load_File = 0 # Resets the Load File
    TitleScreen() # Restarts back to the Titlescreen

def Died(DeathCause):
    '''This Function handles the Death of the Player'''
    global Load_File # Globalises the Variables in the Function
    os.system('cls') # Clears the Screen
    # Prints You Died Ascii Art and the Death message
    print(f'''
 ▄· ▄▌      ▄• ▄▌    ·▄▄▄▄  ▪  ▄▄▄ .·▄▄▄▄  
▐█▪██▌▪     █▪██▌    ██▪ ██ ██ ▀▄.▀·██▪ ██ 
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▐█· ▐█▌▐█·▐▀▀▪▄▐█· ▐█▌
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ██. ██ ▐█▌▐█▄▄▌██. ██ 
  ▀ •  ▀█▄▀▪ ▀▀▀     ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀• 

You Died to {DeathCause}
''')
    input('Enter to Delete Save...') # Waits so the user can see

    with open(f'Save{Load_File}.json', 'w') as file: # Opens the Current save file
        json.dump({}, file) # Dumps an empty dictionary to the file - Causing it to get deleted
    
    Load_File = 0

    TitleScreen() # Loads the Titlescreen Program - Restating the Program

def DefeatedGK():
    '''
    This function is called when the player defeats the Goblin King.
    It clears the terminal and displays a heartfelt, cinematic conclusion to the game.
    '''
    global Load_File
    os.system('cls')  # Clears the terminal for a clean ending screen

    # Prints the Victory Message to the Player
    print('''
╔══════════════════════════════════════════════════════════════╗
║                   ✨ VICTORY IN NIADON ✨                    ║
╚══════════════════════════════════════════════════════════════╝

With a final cry, the Goblin King falls — his reign of terror ended,
his crown shattered on the stone floor of his dark throne room.

The skies above Niadon begin to clear for the first time in years.
Sunlight pierces the once-eternal gloom, casting golden light
across the mountains, forests, and forgotten ruins.

Villages rejoice. Children sing your name. Stories of your bravery
echo across every continent, whispered around fires and carved into stone.

You are no longer just a wanderer...

               You are the Hero of Niadon.

Thank you, brave adventurer, for your courage, your sacrifice,
and your unyielding spirit. You restored balance to a world on the brink.

                 May peace follow in your footsteps.

════════════════════════════════════════════════════════════════

                ~ THE END ~     (for now...)

    ''')

    input('Enter to Complete Game (This Resets Save File Information)...')

    with open(f'Save{Load_File}.json', 'w') as file: # Opens the Current save file
        json.dump({}, file) # Dumps an empty dictionary to the file - Causing it to get deleted
    
    Load_File = 0

    TitleScreen() # Loads the Titlescreen Program - Restating the Program

TitleScreen() # Runs the Program from Titlescreen
```
## Review Questions

### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning

This sprint was highly effective in meeting all of the core functional and non-functional goals. Two of the major feature implementations, the story integration and the final boss battle, were both completed and function correctly. These were key functional requirements outlined in planning, and their completion brings narrative closure and structure to the gameplay loop.

On the non-functional side, user feedback was implemented to polish and improve the UI layout, making the interface more intuitive and visually clear. In particular, peer testing highlighted areas where information could be displayed more cleanly, and these improvements have led to a more enjoyable and accessible user experience.

Input handling remains highly reliable, and response times are fast due to the efficient, text-based nature of the program. The design also continues to meet goals for consistent user feedback and error prevention, using structured validation and logical control flows to guide the player’s interaction.

### Analyse the performance of your program against the key use-cases you identified

The program performs well across all originally defined use-cases. Some of the most relevant ones for this sprint include:

- *"The user engages in a boss fight"* – This has now been fully implemented. The final battle behaves as intended, with turn-based combat that takes into account player stats, weapons, and enemy characteristics.

- *"The user interacts with narrative content"* – This use-case is now operational through the integrated story system, which triggers based on the player's location and progress, creating a more immersive journey across the world map.

- *"The user receives feedback for invalid inputs"* – Input validation has continued to perform reliably, catching improper entries and prompting users clearly, reducing confusion and preventing crashes.

All core gameplay loops, including exploration, combat, stat tracking, and story progression are fully functional. The game now has a start, middle, and end, tying the key use-cases together into a coherent experience.

### Assess the quality of your code in terms of readability, structure, and maintainability
Code quality remains high. All my programs classes and functions include thorough comments that explain purpose, logic, and flow, making the code accessible and easy to understand for both the developer and external readers.

While the program remains in a single file, this decision was intentional. Due to the scale and structure of the project, maintaining a single file has allowed for simpler management and easier debugging during development, avoiding unnecessary complexity caused by circular imports.

Error handling has been improved in this sprint. New and refined techniques ensure the program gracefully manages unexpected inputs or edge cases, enhancing the reliability of the program.

### Explain the improvements that should be made in the next stage of development
The focus for Sprint 4 will be on feature refinement and immersion enhancements:

Feature Imrpovements:
- Refining the enchanting system: Players will be given the ability to choose which weapon attributes they wish to enhance (e.g., power, elemental affinity). This will deepen player agency and add strategic depth.

- Mana usage implementation: The magic and spell systems will be fully tied to mana, requiring players to manage resources thoughtfully during combat.

Immersion Improvements:
- Scroll-text using the time module: Story events and dialogues will be presented with gradual text reveal. This will improve pacing, simulate a storytelling atmosphere, and increase immersion in key moments.

 These additions will round out the gameplay experience, improving player engagement while continuing to follow structured and maintainable design principles.



# Sprint 4

## Design

### **Potential Enhancements or Features**
As the project progresses into its final stages, several targeted enhancements are planned to improve both functionality and user immersion. These features are aligned with earlier design goals and peer feedback, and are intended to polish the overall experience without overcomplicating the existing system.

**Scrolling Text Integration**
- One of the previously outlined goals was to enhance immersion through the use of dynamic, story-driven text presentation. This will be achieved by integrating the time module to create a scrolling text effect, where story segments are revealed character-by-character. This will give dramatic weight to key narrative moments and improve storytelling delivery by mimicking the pacing of traditional RPGs.

**UI Enhancements Based on Peer Feedback**
- Based on testing and feedback from peers, visual clarity remains an area of improvement. A simple but impactful change will be to increase the spacing between the map display and other UI elements (e.g., player stats, inventory). This added padding will help reduce visual clutter, making it easier for players to process the game state at a glance, especially during combat or navigation.

**Refined Enchantment System**
- The current enchanting system is functional but basic. An upgrade will give players more agency in how enchantments are applied, allowing them to choose which stats or elements to improve. This turns enchanting into a strategic decision rather than a random bonus, adding depth to gameplay and rewarding player planning and resource management.

### **Implimentation of Features**

Rather than introducing entirely new systems, these enhancements will build directly on top of existing frameworks within the game. This approach is both practical and efficient, ensuring that:

- Current systems like text display, enchantment logic, and UI rendering are reused and extended, making implementation faster and more maintainable.

- The player experience is improved, while the underlying architecture remains stable and understandable.

By extending rather than replacing core components, the final sprint will focus on polish, player choice, and narrative delivery—key factors in transforming a strong foundation into a memorable and complete adventure.

### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning

The final version of the project meets all core functional and non-functional requirements as defined in the original planning document. Key functional goals such as character statistics tracking, inventory interaction, exploration, combat, and story progression are fully implemented. Notably, the addition of the final boss battle and a adaptive story system completes the narrative arc and gives players a satisfying endgame challenge.

Aswell as this, the Non-Functional requirements of the project performs reliably across different systems and inputs. The text-based interface ensures fast response times, and the input system is resilient, with clear feedback for errors and invalid entries. Improvements to user interface layout and the addition of scrolling text further enhance accessibility and immersion, fulfilling the user experience goals outlined during planning.

The transition from the original directional movement system to numbered inputs demonstrates responsiveness to usability goals, and extensive peer testing helped refine the overall presentation and flow. While some minor enhancements are still planned, the project has succeeded in delivering a functional, engaging, and user-friendly experience that adheres to both the original brief and evolving player feedback.

### Analyse the performance of your program against the key use-cases you identified
The program performs strongly across all key use-cases identified in the design phase. Examples include:

- *“The user moves between different areas on a map”* – Implemented using a numbered input system, area transitions are responsive and intuitive.

- *“The user engages in combat with enemies”* – Players can initiate and participate in turn-based battles, using physical or enchanted weapons, and adapting strategy based on the enemy type.

- *“The user views and manages inventory and stats”* – At any point, the user can check their inventory, stats, gold, and equipment. The enchantment system now allows players to customize gear, further supporting this use-case.

- *“The user interacts with story elements or triggers events”* – Fully functional through the Story() system, adapts based of where the player has been, and at which point of progess the player is at.

The game responds correctly to user input, including invalid or unexpected entries. Output is consistent, informative, and styled for clarity. No major crashes or logic failures have been identified, and input/output behavior matches the expected flow in all tested scenarios.

### Assess the quality of your code in terms of readability, structure, and maintainability
The code demonstrates a high standard of quality in terms of both structure and readability:

Consistent naming conventions make it easy to understand the purpose of variables, functions, and classes at a glance.

Functions and classes are modular, reusable, and logically scoped, with each one handling a clearly defined task (e.g., Combat(), Story(), Input_Selection()).

Every major section of the codebase is accompanied by thorough and meaningful comments, including docstrings for classes and detailed inline explanations for complex logic.

Although all the code is kept in a single file, this was a deliberate choice due to the risk of circular imports and the small-to-medium scale of the game. This approach has helped streamline development without sacrificing clarity.

In terms of maintainability, future developers will be able to continue development with minimal onboarding time, thanks to the logical organization, clear function boundaries, and extensive documentation throughout the codebase.

### Explain the improvements that should be made in the next stage of development
With the core gameplay loop complete, the next stage of development will focus on refinement and replayability. Planned improvements include:

#### Feature Enhancements:
- Refine the enchantment system to allow greater control over how items are enhanced (e.g., increase elemental damage, buff specific stats).

- Introduce mana usage for spells, allowing for a move diverse gaming system, and allow for more statergy in the game play system.
 
- Adding More Content - i.e The current game would fit well into one level of a larger game, or impliment it in a chronologically connected series, such as what is seen in games such as the Elder Scrolls.

### Code and Structural Refinements:
- Explore modularization: Although the current single-file structure is effective, breaking the program into logical modules (e.g., combat.py, ui.py, items.py) could improve scalability and make collaborative development easier in future iterations.

- Optimizing the Input Selection Function. This will make it more versitile, and require less supporting code in each instance it is called.

By focusing on polish, customizability, and long-term structure, these final improvements will elevate the game from a working prototype to a robust and replayable application that demonstrates strong software design and player-centered thinking.

### Build: (main.py)
```Python
#--- Imports ---
import os # Used for editing the terminal view
import random # Allows for randomness between different runs
import time # Allows for more interactive UI by incorperating time
import json # Used for saving
import math # Used to calculate events
from wcwidth import wcswidth # Used to handle the Emoji and Ascii problems
import sys # Used for Scrolling Text

#--- Classes ---
class Player():
    '''This class is used to create the Player information system, and is designed to be adaptive, allowing for different save files to be loaded, and unloaded'''
    def __init__(self, Save):
        '''Loads the Player data from the Save file (Which is a Dictionary)'''
        self.Player_Name = Save['Player_Name'] # Loads Player Name from Save file

        self.Health = {'Health': Save['Health']['Health'], 'Max_Health': Save['Health']['Max_Health']} # Loads Health and Max Health into a dictionary
        self.Stamina = {'Stamina': Save['Stamina']['Stamina'], 'Max_Stamina': Save['Stamina']['Max_Stamina']} # Loads Stamina and Max Stamina into a dictionary
        self.Mana = {'Mana': Save['Mana']['Mana'], 'Max_Mana': Save['Mana']['Max_Mana']} # Loads Mana and Max Mana into a dictionary

        self.WeaponSlot = Save['WeaponSlot'] # Loads Weapon from the Save File
        self.HelmetSlot = Save['HelmetSlot'] # Loads the Helmet from the Save File
        self.ChestplateSlot = Save['ChestplateSlot'] # Loads the Chestplate from the Save file
        self.BootSlot = Save['BootSlot'] # Loads the Boot from the Chestplate

        self.OtherSlot1 = {'Item': Save['OtherSlot1']['Item'], 'Qty': Save['OtherSlot1']['Qty']} # Loads the Item and Qty from save file for Save File 1
        self.OtherSlot2 = {'Item': Save['OtherSlot2']['Item'], 'Qty': Save['OtherSlot2']['Qty']} # Loads the Item and Qty from save file for Save File 2
        self.OtherSlot3 = {'Item': Save['OtherSlot3']['Item'], 'Qty': Save['OtherSlot3']['Qty']} # Loads the Item and Qty from save file for Save File 3
        self.OtherSlot4 = {'Item': Save['OtherSlot4']['Item'], 'Qty': Save['OtherSlot4']['Qty']} # Loads the Item and Qty from save file for Save File 4
        
        self.Location = Save['Location'] # Loads the Player Location
        self.Gold = Save['Gold'] # Loads the Player Gold

        self.Enemy1 = Save['Enemy1'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy2 = Save['Enemy2'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy3 = Save['Enemy3'] # Loads wether the player has been in room for a more adaptive story 
        self.Enemy4 = Save['Enemy4'] # Loads wether the player has been in room for a more adaptive story 
        self.Village1 = Save['Village1'] # Loads wether the player has been in room for a more adaptive story 
        self.Village2 = Save['Village2'] # Loads wether the player has been in room for a more adaptive story 
        self.Village3 = Save['Village3'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest1 = Save['Forest1'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest2 = Save['Forest2'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest3 = Save['Forest3'] # Loads wether the player has been in room for a more adaptive story 
        self.Forest4 = Save['Forest4'] # Loads wether the player has been in room for a more adaptive story 
        self.SeenW1 = Save['SeenW1'] # Loads wether the player has been in room for a more adaptive story 
        self.SeenW2 = Save['SeenW2'] # Loads wether the player has been in room for a more adaptive story 
        self.Wizard1 = Save['Wizard1'] # Loads wether the player has been in room for a more adaptive story 
        self.Wizard2 = Save['Wizard2'] # Loads wether the player has been in room for a more adaptive story 
        self.Mountain = Save['Mountain'] # Loads wether the player has been in room for a more adaptive story 
        self.GoblinKing = Save['GoblinKing'] # Loads wether the player has been in room for a more adaptive story 
        self.RareFlower = Save['RareFlower'] # Loads wether the player has obtained the Flower
        self.RareRune = Save['RareRune'] # Loads wether the player has obtained the Rune

        self.Enemies = {'G': Save['Enemies']['G'], 'O': Save['Enemies']['O'], 'D': Save['Enemies']['D'], 'Og': Save['Enemies']['Og']} # Loads the Health of Each Enemy

        Load_Enemies(Save['Enemies']['G'], Save['Enemies']['O'], Save['Enemies']['D'], Save['Enemies']['Og']) # Loads the Enemies into the System, with the health files

    def Save(self, Save):
        '''Transfers the Information from the Save File into the JSON File'''

        Player_Stats = { # Creates a Dictionary of the Data
            'Player_Name': self.Player_Name, # Loads Player Name from the Player Attributes
            'Health': self.Health, # Loads the Player Health Dictionary from Player Attributes, making it contain both player Health and Max Health
            'Stamina': self.Stamina, # Loads the Player Stamina Dictionary from Player Attributes, making it contain both player Stamina and Max Stamina
            'Mana': self.Mana, # Loads the Player Mana Dictionary from Player Attributes, making it contain both player Mana and Max Mana
            'WeaponSlot': {'Name': self.WeaponSlot.name, 'Level': self.WeaponSlot.level, 'Multiplyers': self.WeaponSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Weapon
            'HelmetSlot': {'Name': self.HelmetSlot.name, 'Level': self.HelmetSlot.level, 'Multiplyers': self.HelmetSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Helmet
            'ChestplateSlot': {'Name': self.ChestplateSlot.name, 'Level': self.ChestplateSlot.level, 'Multiplyers': self.ChestplateSlot.multiplyers},  # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Chestplate
            'BootSlot': {'Name': self.BootSlot.name, 'Level': self.BootSlot.level, 'Multiplyers': self.BootSlot.multiplyers}, # Stores only Necessary Values - i.e Name, Item Level, and the Encahntments on the Boots
            'OtherSlot1': {'Item': self.OtherSlot1['Item'].name, 'Qty': self.OtherSlot1['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot2': {'Item': self.OtherSlot2['Item'].name, 'Qty': self.OtherSlot2['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot3': {'Item': self.OtherSlot3['Item'].name, 'Qty': self.OtherSlot3['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'OtherSlot4': {'Item': self.OtherSlot4['Item'].name, 'Qty': self.OtherSlot4['Qty']}, # Stores only Necessary Values - i.e Name and Quantity of the Items
            'Location': self.Location, # Stores The Player Location
            'Gold': self.Gold, # Stores the Players amount of Gold

            'Enemy1': self.Enemy1, # Stores Whether the Player has been in the Room
            'Enemy2': self.Enemy2, # Stores Whether the Player has been in the Room
            'Enemy3': self.Enemy3, # Stores Whether the Player has been in the Room
            'Enemy4': self.Enemy4, # Stores Whether the Player has been in the Room

            'Village1': self.Village1, # Stores Whether the Player has been in the Room
            'Village2': self.Village2, # Stores Whether the Player has been in the Room
            'Village3': self.Village3, # Stores Whether the Player has been in the Room

            'Forest1': self.Forest1, # Stores Whether the Player has been in the Room
            'Forest2': self.Forest2, # Stores Whether the Player has been in the Room
            'Forest3': self.Forest3, # Stores Whether the Player has been in the Room
            'Forest4': self.Forest4, # Stores Whether the Player has been in the Room

            'SeenW1': self.SeenW1, # Stores Whether the Player has been in the Room
            'SeenW2': self.SeenW2, # Stores Whether the Player has been in the Room

            'Wizard1': self.Wizard1, # Stores Whether the Player has been in the Room
            'Wizard2': self.Wizard2, # Stores Whether the Player has been in the Room
            'Mountain': self.Mountain, # Stores Whether the Player has been in the Room
            'GoblinKing': self.GoblinKing, # Stores Whether the Player has been in the Room

            'RareFlower': self.RareFlower, # Stores Whether the Player has obtained the Rare Flower
            'RareRune': self.RareRune,# Stores Whether the Player has obtained the Rare Rune

            'Enemies': {'G': Goblin.health, 'O': Orc.health, 'D': Druid.health, 'Og': Ogre.health} # Stores the Enemy Health
        }

        with open(f'Save{Save}.json', 'w') as f: # Opens the JSON file attached to the Load File
            json.dump(Player_Stats, f) # Puts the Player Data into the JSON file

    def Attacking(self, Target):
        '''Allows the Player to Attack an Enemy, by Specifying which Enemy to Attack'''
        Target.Player_Attacked() # Runs the Player_Attacked Function of the specified Target

    def Attacked(self, Damage, Type):
        '''Calculates Damage of Enemy, based of of the Multipliers on the Players Armour'''
        try:
            self.Health['Health'] -= round(Damage / ((self.HelmetSlot.protection + self.ChestplateSlot.protection + self.BootSlot.protection) / 3) * ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3)) # Calculates the Protection based on factors such as Protection and Enchantment Levels

        except:
            self.Health['Health'] -= Damage

class Item():
    '''This class creates the Foundation for Creating Items in the Game'''
    def __init__(self, name, level):
        'This function initalises the Items Variables'
        self.name = name # Defines the Items Name
        self.level = level # Defines the Ites Level

class Weapons(Item):
    '''This Class outlines the basics for creating Weapons'''
    def __init__(self, name, level, type, damage, multiplyers=None): 
        '''This Function Inherits the Prarameters from Item, and adds Weapon Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.type = type # Defines the Weapon Type - i.e Sword, Axe, Mace
        self.damage = damage # Defines the Weapons Damage
        
        if multiplyers is None: # If Multipliers is Undefined - Not given when creating the Weapon
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1} # Sets Multiplers all to 1
        else:
            self.multiplyers = multiplyers # If Multiplers are given, uses the given ones

    def setmultiplyers(self, Multiplyers):
        '''This Function allows the setting of the Multiplers - Used to Enchant the Item'''
        self.multiplyers = Multiplyers # Sets the Multiplers

class Armour(Item):
    '''This Class outlines the basics for creating Armour'''
    def __init__(self, name, level, type, protection, multiplyers=None):
        '''This Function Inherits the Prarameters from Item, and adds Armour Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.type = type # Defines the Type of Armour - i.e Helmet, Chestplate, Boots
        self.protection = protection # Defines the Protection level of the Armour


        if multiplyers is None: # If Multipliers is Undefined - Not given when creating the Armour piece
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1} # Sets Multiplers all to 1
        else:
            self.multiplyers = multiplyers # If Multiplers are given, uses the given ones

    def setmultiplyers(self, Multiplyers):
        self.multiplyers = Multiplyers
            
class Potion(Item):
    '''This Class creates potions, and allows them to be made at different strengths, to impact the Player different stats'''
    def __init__(self, name, level, effect, strength):
        '''This Function Inherits the Prarameters from Item, and adds Potion Specific Parameters'''
        super().__init__(name, level) # Inherits the Parameters from Item
        self.effect = effect # Defines the effect the Potion impacts - i.e Health, Stamina, Mana
        self.strength = strength # Defines the Strength of the Potion

    def Use_Potion(self, Target):
        '''This function allows the Potion to be Used'''
        getattr(Target, self.effect)[self.effect] += self.strength # Applies the Effect to the Target
        if getattr(Target, self.effect)[self.effect] > getattr(Target, self.effect)[f'Max_{self.effect}']: # If the Potion atted too much statistic compared to the Max...
            getattr(Target, self.effect)[self.effect] = getattr(Target, self.effect)[f'Max_{self.effect}'] # Brings the Health Back down to the Max Health

        # Remove potion from inventory after use
        for slot in [Target.OtherSlot1, Target.OtherSlot2, Target.OtherSlot3, Target.OtherSlot4]: # Finds Which slot Potion is In
            if slot['Item'] is self and slot['Qty'] > 0: # Item is in Slot, and the Quantity is More than 0
                slot['Qty'] -= 1 # Removes of from the Quantity
                if slot['Qty'] == 0: # If their is None left in the Slot
                    slot['Item'] = None_Item # Reverts Slot back to None_Item
                break # Stops looking for where the Item is

class Enemy():
    '''This Class Creates a Enemy System, that allows for the creation of Enemies, and Allows them to interact / attack other Players and Enemies'''
    def __init__(self, name, health, max_health, damage, type, level):
        '''This function allows the User to '''
        self.name = name
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.type = type
        self.level = level

    def Attacking(self, Target):
        Target.Attacked(self.damage, self.type)

    def Player_Attacked(self):
        self.health -= round(User.WeaponSlot.damage * User.WeaponSlot.multiplyers[self.type])

    def Attacked(self, Damage, Type):
        if self.type == 'Fir' and Type == 'Wat': # Strong < Weak
            self.health -= round(Damage * 1.5)

        elif self.type == 'Wat' and Type == 'Fir': # Strong > Weak
            self.health -= round(Damage * 0.5)

        elif self.type == 'Nat' and Type == 'Fir': # Strong < Weak
            self.health -= round(Damage * 1.5)

        elif self.type == 'Fir' and Type == 'Nat': # Strong > Weak
            self.health -= round(Damage * 0.5)

        elif self.type == 'Wat' and Type == 'Nat': # Strong < Weak
            self.health -= round(Damage * 1.5)
        
        elif self.type == 'Nat' and Type == 'Wat': # Strong > Weak
            self.health -= round(Damage * 0.5)
        
        else:
            self.health -= round(Damage)

class Villager:
    '''This class handles the Villager Creation Process'''
    def __init__(self, name, profession):
        '''This function initalizes the Villager attributes'''
        self.name = name # Creates a Villager Name 
        self.profession = profession # Gives the Villager a Profession
        self.items = {} # Creates a dicitonary for each item the User Sells

    def Inventory_Trading(self):
        '''This Function allows the user to purchase the items that each villager sells'''
        os.system('cls')  # Clear the terminal screen for a clean display

        # Print villager's shop interface with their name, profession, and the user's gold
        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     {self.profession:<38}|
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {str(User.Gold) + ' 🪙':<38}|
    +---------------------------------------------------------+
    ''') 

        count = 1  # Start item count at 1 for menu numbering

        # Print the table header with item structure
        print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')  
        for item in self.items.values():  # Loop through each item the villager sells
            # Print item number, name, cost, and quantity available
            print(f"|{count:<3}| {item['Item'].name:<30}   |   Cost: {item['Cost']:<4} 🪙    |   Qty: {item['Qty']:<10} |")
            # Print divider line between items
            print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
            count += 1  # Increment count for the next item

        # Calculate number of lines printed to later clear the screen
        lines_printed = (count * 2) + 1  # Includes rows and dividers

        while True:  # Start purchase loop until the player exits or breaks
            try:  # Attempt to get valid input from the player
                # Ask user to select an item to buy or 0 to exit
                Puchase_Input = int(input('Enter the number of the item you want to purchase (0 to exit): '))
                
                if Puchase_Input == 0:  # If player chose to exit
                    ClearLines(lines_printed + 1)  # Clear the printed table
                    break  # Exit the while loop
                
                elif 1 > Puchase_Input or Puchase_Input >= count:  # Input outside valid range
                    print('Not a Valid Number')  # Print error message
                
                elif 1 <= Puchase_Input < count:  # Valid item selection
                    selected_item = list(self.items.values())[Puchase_Input - 1]  # Get selected item
                    item = selected_item['Item']  # Extract the actual item object

                    if selected_item['Qty'] > 0:  # Check if the item is in stock
                        if User.Gold >= selected_item['Cost']:  # Check if player has enough gold
                            goto_inventory = False  # Flag for sending item to inventory (if not equippable)

                            # If the item is a Weapon, equip it directly
                            if isinstance(item, Weapons):
                                print(f"Equipped {item.name} to Weapon Slot (replacing {User.WeaponSlot.name}).")
                                User.WeaponSlot = item  # Replace player's weapon

                            # If the item is Armour, check which slot it belongs to
                            elif isinstance(item, Armour):
                                if item.type == 'Helmet':  # If it's a helmet
                                    print(f"Equipped {item.name} to Helmet Slot (replacing {User.HelmetSlot.name}).")
                                    User.HelmetSlot = item
                                elif item.type == 'ChestPlate':  # If it's a chestplate
                                    print(f"Equipped {item.name} to Chestplate Slot (replacing {User.ChestplateSlot.name}).")
                                    User.ChestplateSlot = item
                                elif item.type == 'Boot':  # If it's boots
                                    print(f"Equipped {item.name} to Boot Slot (replacing {User.BootSlot.name}).")
                                    User.BootSlot = item
                                else:  # Unknown armour type, treat as regular item
                                    print(f"Unknown armour type: {item.type}. Placing in inventory.")
                                    goto_inventory = True  # Send to inventory
                            else:
                                goto_inventory = True  # All other item types go to inventory

                            # Define player's inventory slots for other items
                            inventory_slots = [User.OtherSlot1, User.OtherSlot2, User.OtherSlot3, User.OtherSlot4]
                            found = False  # Track if item was already in inventory
                            replace_cancelled = False  # Track if player cancelled replace prompt

                            if goto_inventory:
                                # Check if the item is already in inventory
                                for slot in inventory_slots:
                                    if slot['Item'] is item:  # Found matching item
                                        slot['Qty'] += 1  # Increase quantity
                                        found = True
                                        break

                                if not found:  # If item not found in existing slots
                                    empty_slot = None  # Track first empty slot
                                    for slot in inventory_slots:  # Search for an empty slot
                                        if slot['Item'].name == 'None':  # Empty if item is 'None'
                                            empty_slot = slot
                                            break
                                    
                                    if empty_slot:  # Place item in empty slot
                                        empty_slot['Item'] = item
                                        empty_slot['Qty'] = 1
                                    else:
                                        # No empty slot: ask player to replace an item or cancel
                                        print("Your inventory is full. Choose an item to replace or cancel:")
                                        for idx, slot in enumerate(inventory_slots, 1):  # List current items
                                            print(f"{idx}. {slot['Item'].name} (x{slot['Qty']})")
                                        print(f"{len(inventory_slots)+1}. Cancel purchase")

                                        while True:  # Loop until valid input
                                            try:
                                                replace_choice = int(input("Enter number to replace or cancel: "))  # Get replace input
                                                if 1 <= replace_choice <= len(inventory_slots):  # Valid replace
                                                    slot = inventory_slots[replace_choice - 1]  # Chosen slot
                                                    print(f"Replaced {slot['Item'].name} with {item.name}.")  # Feedback
                                                    slot['Item'] = item  # Replace item
                                                    slot['Qty'] = 1
                                                    break
                                                elif replace_choice == len(inventory_slots) + 1:  # Cancel option
                                                    print("Purchase cancelled.")  # Cancelled
                                                    replace_cancelled = True
                                                    break
                                                else:
                                                    print("Invalid choice.")  # Error
                                            except ValueError:
                                                print("Invalid input.")  # Error for non-numbers

                            # Finalize purchase if not cancelled
                            if not goto_inventory or not replace_cancelled:
                                selected_item['Qty'] -= 1  # Reduce villager’s item stock
                                User.Gold -= selected_item['Cost']  # Deduct gold from user
                                print(f"You bought 1x {item.name} for {selected_item['Cost']} 🪙.")  # Confirm purchase
                            else:
                                continue  # If cancelled, skip rest of loop
                        else:
                            print("You do not have enough gold to purchase this item.")  # Not enough gold
                    else:
                        print("Sorry, this item is out of stock.")  # Item unavailable
            except Exception:  # Catch any unexpected error
                print("Invalid input. Please enter a number.")  # Prompt retry

class Brewer(Villager):
    """A villager that specializes in selling health, mana, and stamina potions."""
    def __init__(self, name):
        super().__init__(name, 'Brewer')  # Call the base Villager constructor with name and profession
        self.items = {  # Dictionary of potion types sold by the Brewer
            'Health Potion': {
                'Item': random.choice([Health_Potion_Small, Health_Potion_Medium, Health_Potion_Large]),  # Random potion size
                'Cost': random.randint(3, 10),  # Random cost for the potion
                'Qty': random.randint(3, 12)  # Random quantity available
            },
            'Mana Potion': {
                'Item': random.choice([Mana_Potion_Small, Mana_Potion_Medium, Mana_Potion_Large]),
                'Cost': random.randint(3, 10),
                'Qty': random.randint(3, 12)
            },
            'Stamina Potion': {
                'Item': random.choice([Stamina_Potion_Small, Stamina_Potion_Medium, Stamina_Potion_Large]),
                'Cost': random.randint(3, 10),
                'Qty': random.randint(3, 12)
            }
        }

class SwordSmith(Villager):
    """A villager that sells swords made of different materials."""
    def __init__(self, name):
        super().__init__(name, 'SwordSmith')  # Call base Villager constructor
        self.items = {
            'Wooden Sword': {'Item': Wooden_Sword, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Sword': {'Item': Bronze_Sword, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Sword': {'Item': Iron_Sword, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Sword': {'Item': Platinum_Sword, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class AxeSmith(Villager):
    """A villager that sells axes made of different materials."""
    def __init__(self, name):
        super().__init__(name, 'AxeSmith')
        self.items = {
            'Wooden Axe': {'Item': Wooden_Axe, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Axe': {'Item': Bronze_Axe, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Axe': {'Item': Iron_Axe, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Axe': {'Item': Platinum_Axe, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class MaceSmith(Villager):
    """A villager that sells maces made of different materials."""
    def __init__(self, name):
        super().__init__(name, 'MaceSmith')
        self.items = {
            'Wooden Mace': {'Item': Wooden_Mace, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Mace': {'Item': Bronze_Mace, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Mace': {'Item': Iron_Mace, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Mace': {'Item': Platinum_Mace, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class ArmourSmith(Villager):
    """A villager that sells different pieces of armor, including helmets, chestplates, and boots."""
    def __init__(self, name):
        super().__init__(name, 'ArmourSmith')
        self.items = {
            'Leather Helmet': {'Item': Leather_Helmet, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Helmet': {'Item': Bronze_Helmet, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Helmet': {'Item': Iron_Helmet, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Helmet': {'Item': Platinum_Helmet, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Chestplate': {'Item': Leather_Chestplate, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Chestplate': {'Item': Bronze_Chestplate, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Chestplate': {'Item': Iron_Chestplate, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Chestplate': {'Item': Platinum_Chestplate, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Boot': {'Item': Leather_Boot, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Boot': {'Item': Bronze_Boot, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Boot': {'Item': Iron_Boot, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Boot': {'Item': Platinum_Boot, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class Wizard(Villager):
    """A villager that enchants gear after the player completes certain quests."""
    def __init__(self, name):
        super().__init__(name, 'Wizard')  # Set name and role as Wizard
    
    def WizardStore(self, Room):
        """Handles player interaction with the Wizard based on the room (Wizard1 or Wizard2)."""
        global User  # Access the global User object
        os.system('cls')  # Clear the screen
        
        # First wizard interaction logic
        if Room == 'Wizard1':
            if User.SeenW1 == False:  # If user has not seen Wizard1 before
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Their is a rare flower in the south forest, bring it to me, and I will help you enchant!
                    ''')
                User.SeenW1 = True  # Set flag that user has now seen Wizard1
                input('     Enter to Continue...')  # Pause for input
                PrintMainUI('Wizard1')  # Return to main UI
            elif User.SeenW1 == True and User.RareFlower == False:  # If user has seen wizard but not brought the flower
                print("Have you Brought me my Flower Yet? It's in the South Forest")
                input('Enter to Continue...')
                PrintMainUI('Wizard1')
            elif User.RareFlower == True:  # If player has brought the flower
                print()
                print('Thanks for bringing me my flower, what can I help you enchant today? Remember, Enachting Requires 40 Mana a Piece')
                if User.Mana['Mana'] > 40:
                    def make_enchant_lambda(slot):  # Closure to create enchantment functions for items
                        print('Would you Like a Type Based Enchant?')
                        User.Mana['Mana'] -= 40
                        Input_Selection({
                            'Fire': lambda: Enchantment(slot, 'Fir'),
                            'Water': lambda: Enchantment(slot, 'Wat'),
                            'Nature': lambda: Enchantment(slot, 'Nat'),
                            'Regular': lambda: Enchantment(slot)
                        })
                    options = {
                        User.WeaponSlot.name: lambda: make_enchant_lambda(User.WeaponSlot)
                    }
                    if User.HelmetSlot.name != "None_Helmet":
                        options[User.HelmetSlot.name] = lambda: make_enchant_lambda(User.HelmetSlot)
                    if User.ChestplateSlot.name != "None_Chestplate":
                        options[User.ChestplateSlot.name] = lambda: make_enchant_lambda(User.ChestplateSlot)
                    if User.BootSlot.name != "None_Boot":
                        options[User.BootSlot.name] = lambda: make_enchant_lambda(User.BootSlot)
                    options['Exit'] = lambda: PrintMainUI('Wizard1')  # Add exit option
                    Input_Selection(options)  # Allow player to choose item to enchant

                    # Prints each item and it's enchantment level
                    print(f'''
        +---+{'-'*39}+- Wat -+- Fir -+- Nat -+
        | 1 | Weapon Slot:     {User.WeaponSlot.name:<20} | {User.WeaponSlot.multiplyers['Wat']:<3.3f} | {User.WeaponSlot.multiplyers['Fir']:<3.3f} | {User.WeaponSlot.multiplyers['Nat']:<3.3f} |
        | 2 | Helmet Slot:     {User.HelmetSlot.name:<20} | {User.HelmetSlot.multiplyers['Wat']:<3.3f} | {User.HelmetSlot.multiplyers['Fir']:<3.3f} | {User.HelmetSlot.multiplyers['Nat']:<3.3f} |
        | 3 | Chestplate Slot: {User.ChestplateSlot.name:<20} | {User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
        | 4 | Boot Slot:       {User.BootSlot.name:<20} | {User.BootSlot.multiplyers['Wat']:<3.3f} | {User.BootSlot.multiplyers['Fir']:<3.3f} | {User.BootSlot.multiplyers['Nat']:<3.3f} |
        +---+{'-'*39}+-------+-------+-------+''')
                    input('Enter to Continue...')  # Pause before exiting 
                    PrintMainUI('Wizard1')

                else:
                    print('You dont have Enough Mana to Enchant - Talk to your local Brewer to get some more')
                    input('Enter to Continue...')
                    PrintMainUI('Wizard1')
        elif Room == 'Wizard2':
            if User.SeenW1 == False:  # If user has not seen Wizard1 before
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Up in the high mountains of Sorvo, their is an ancient rune, ensribed with ancient information.
            Bring it to me, and I will help you enchant!
                    ''')
                User.SeenW1 = True  # Set flag that user has now seen Wizard1
                input('     Enter to Continue...')  # Pause for input
                PrintMainUI('Wizard2')  # Return to main UI
            elif User.SeenW1 == True and User.RareRune == False:  # If user has seen wizard but not brought the Rune
                print("Have you Brought me my Rune Yet? It's in the high mountains of Sorvo")
                print() # Spacer in Temrinal
                input('Enter to Continue...')
                PrintMainUI('Wizard2')
            elif User.RareRune == True:  # If player has brought the flower
                print()
                print('Thanks for bringing me my Rune, what can I help you enchant today? Remember, Enachting Requires 40 Mana a Piece')
                if User.Mana['Mana'] > 40:
                    def make_enchant_lambda(slot):  # Closure to create enchantment functions for items
                        print('Would you Like a Type Based Enchant?')
                        User.Mana['Mana'] -= 40
                        Input_Selection({
                            'Fire': lambda: Enchantment(slot, 'Fir'),
                            'Water': lambda: Enchantment(slot, 'Wat'),
                            'Nature': lambda: Enchantment(slot, 'Nat'),
                            'Regular': lambda: Enchantment(slot)
                        })
                    options = {
                        User.WeaponSlot.name: lambda: make_enchant_lambda(User.WeaponSlot)
                    }
                    if User.HelmetSlot.name != "None_Helmet":
                        options[User.HelmetSlot.name] = lambda: make_enchant_lambda(User.HelmetSlot)
                    if User.ChestplateSlot.name != "None_Chestplate":
                        options[User.ChestplateSlot.name] = lambda: make_enchant_lambda(User.ChestplateSlot)
                    if User.BootSlot.name != "None_Boot":
                        options[User.BootSlot.name] = lambda: make_enchant_lambda(User.BootSlot)
                    options['Exit'] = lambda: PrintMainUI('Wizard2')  # Add exit option
                    Input_Selection(options)  # Allow player to choose item to enchant

                    print(f'''
        +---+{'-'*39}+- Wat -+- Fir -+- Nat -+
        | 1 | Weapon Slot:     {User.WeaponSlot.name:<20} | {User.WeaponSlot.multiplyers['Wat']:<3.3f} | {User.WeaponSlot.multiplyers['Fir']:<3.3f} | {User.WeaponSlot.multiplyers['Nat']:<3.3f} |
        | 2 | Helmet Slot:     {User.HelmetSlot.name:<20} | {User.HelmetSlot.multiplyers['Wat']:<3.3f} | {User.HelmetSlot.multiplyers['Fir']:<3.3f} | {User.HelmetSlot.multiplyers['Nat']:<3.3f} |
        | 3 | Chestplate Slot: {User.ChestplateSlot.name:<20} | {User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
        | 4 | Boot Slot:       {User.BootSlot.name:<20} | {User.BootSlot.multiplyers['Wat']:<3.3f} | {User.BootSlot.multiplyers['Fir']:<3.3f} | {User.BootSlot.multiplyers['Nat']:<3.3f} |
        +---+{'-'*39}+-------+-------+-------+''')
                    input('Enter to Continue...')  # Pause before exiting 
                    PrintMainUI('Wizard2')

                else:
                    print('You dont have Enough Mana to Enchant - Talk to your local Brewer to get some more')
                    input('Enter to Continue...')
                    PrintMainUI('Wizard2')
        # Second wizard interaction logic (for Rune quest)

class LumberJack(Villager):
    def __init__(self, name):
        '''This function initiates the parameters for the Lumberjack'''
        super().__init__(name, 'LumberJack') # Sets Profession to Lumberjack

    def ChopWood(self):
        '''This function allows the User to gain gold - this prevent softlocking the progression if gear'''
        os.system('cls') # Clears the Screen

        # Tells the User the Amount of gold they have, and the Villager Statistics
        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     Lumberjack                            |
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {str(User.Gold) + ' 🪙':<38}|
    +---------------------------------------------------------+

    You can Earn extra money for equipment!
''')
        print('Chop Wood!')
        for i in range(0, 5): # Run 5 Times
            print() # Creates a Spacer in the Terminal
            print('CHOP') # Prints 'Chop' to Symbolise Something Happend
            print() # Creates a Spacer in the Terminal
            time.sleep(random.randint(10, 20) / 10) # Waites Between 1 and 2 seconds
        print('Good Job, Heres 5 Gold!') # Tells the User they have earnt a piuce of Gold
        User.Gold += 5 # Gives the User a Piece of Gold
        
        input('Enter to Continue...') # Waits for the User to Continue

class Gambler(Villager):
    def __init__(self, name):
        super().__init__(name, 'Gambler')

    def Casino(self):
        '''This Fuction runs the Casino, allowing the User to make more money'''
        CasinoNumber = random.randint(1,5) # Picks Random Number between 1 and 5

        print("Welcome to the Casino") # Welcomes User
        print() # Creates a Spacer in the Terminal
        print("If you win you'll get 5 times what you put in, if you lose, we just keep what you bet") # Explains the Game
        print() # Creates a Spacer in the Terminal

        while True: # Until Broken
            try: # Try to Recieve Input
                Betting = int(input(f"How Much Gold would you Like to Bet? (0 to Not Bet) Current Balance: {User.Gold} ")) # Asks for How much the User wants to bet
                if Betting > User.Gold or Betting < 0: # If Betting Amount it outside of Acceptable Rand
                    print("You don't have that Much Gold") # Prints Error Message
                else: # If User Input is Correct
                    break # Breaks Loop
            except: # If Error with Input
                print("Invalid input. Please enter a number.") # Prints error Message

        while True: # Until Broken
            try: # Try to Recieve Input
                Guess = int(input("Put your Bet on a Number 1-5 ")) # Asks User to Guess a Number
                if 1 <= Guess <= 5: # if Guess is In Acceptable Range
                    break # Break Loop
                else: # If not in Acceptable Range
                    print('Not an Option') # Alert the Player it is not an option
            except: # If error with Input
                print("Invalid input. Please enter a number between 1 and 5.") # Prints error Message

        if Guess == CasinoNumber: # If Player Guesses Right
            User.Gold += 4*Betting # Multiply Betting Amount by 4 (Its Multiplied by 4 because It hasnt actually removed any Gold Yet) and is added to User.Gold

        else: # If Player Guesses Wrong
            print("It'll seem you've lost, maybe next time you'll think twice about going up against the house") # Tells the User they Guessed Wrong
            User.Gold -= Betting # Removes the Betting Amount from the Users Gold

        print() # Creates a Spacer in the Terminal
        print(f"The Number was: {CasinoNumber}") # Tells the Player what it was
        print() # Creates a Spacer in the Terminal
        print(f"Current Balence: {User.Gold}") # Tells the Player their Current Gold Amount

        input('Enter to Continue...') # Waits to Continue

def Load_Items(Name, Level, Multipliers): # Converts simplified JSON data back into full Item objects for use in the program
    '''Since JSON's cant store Items, This function converts the data JSON's can store, and convert it back into the Item Form for the program'''
    
    #--- Weapons ---
    if Name == 'Stick': # If the stored item is Stick
        return Weapons('Stick', Level, 'Stick', 2, Multipliers) # Return a Stick, with the saved Level and Multipliers
    
    elif Name == 'Wooden_Sword': # If the stored item is Wooden_Sword
        return Weapons('Wooden_Sword', Level, 'Sword', 4, Multipliers) # Return a Wooden Sword, with saved Level and Multipliers
    elif Name == 'Bronze_Sword': # If the stored item is Bronze_Sword
        return Weapons('Bronze_Sword', Level, 'Sword', 5, Multipliers) # Return a Bronze Sword, with saved Level and Multipliers
    elif Name == 'Iron_Sword': # If the stored item is Iron_Sword
        return Weapons('Iron_Sword', Level, 'Sword', 6, Multipliers) # Return an Iron Sword, with saved Level and Multipliers
    elif Name == 'Platinum_Sword': # If the stored item is Platinum_Sword
        return Weapons('Platinum_Sword', Level, 'Sword', 8, Multipliers) # Return a Platinum Sword, with saved Level and Multipliers

    elif Name == 'Wooden_Axe': # If the stored item is Wooden_Axe
        return Weapons('Wooden_Axe', Level, 'Axe', 4, Multipliers) # Return a Wooden Axe, with saved Level and Multipliers
    elif Name == 'Bronze_Axe': # If the stored item is Bronze_Axe
        return Weapons('Bronze_Axe', Level, 'Axe', 5, Multipliers) # Return a Bronze Axe, with saved Level and Multipliers
    elif Name == 'Iron_Axe': # If the stored item is Iron_Axe
        return Weapons('Iron_Axe', Level, 'Axe', 6, Multipliers) # Return an Iron Axe, with saved Level and Multipliers
    elif Name == 'Platinum_Axe': # If the stored item is Platinum_Axe
        return Weapons('Platinum_Axe', Level, 'Axe', 8, Multipliers) # Return a Platinum Axe, with saved Level and Multipliers

    elif Name == 'Wooden_Mace': # If the stored item is Wooden_Mace
        return Weapons('Wooden_Mace', Level, 'Mace', 4, Multipliers) # Return a Wooden Mace, with saved Level and Multipliers
    elif Name == 'Bronze_Mace': # If the stored item is Bronze_Mace
        return Weapons('Bronze_Mace', Level, 'Mace', 5, Multipliers) # Return a Bronze Mace, with saved Level and Multipliers
    elif Name == 'Iron_Mace': # If the stored item is Iron_Mace
        return Weapons('Iron_Mace', Level, 'Mace', 6, Multipliers) # Return an Iron Mace, with saved Level and Multipliers
    elif Name == 'Platinum_Mace': # If the stored item is Platinum_Mace
        return Weapons('Platinum_Mace', Level, 'Mace', 8, Multipliers) # Return a Platinum Mace, with saved Level and Multipliers

    #--- Armour ---
    elif Name == 'None_Helmet': # If no helmet is equipped
        return Armour('None_Helmet', 0, 'Helmet', 0, Multipliers) # Return a default empty Helmet
    elif Name == 'Leather_Helmet': # If the stored item is Leather_Helmet
        return Armour('Leather_Helmet', Level, 'Helmet', 1, Multipliers) # Return a Leather Helmet, with saved Level and Multipliers
    elif Name == 'Bronze_Helmet': # If the stored item is Bronze_Helmet
        return Armour('Bronze_Helmet', Level, 'Helmet', 2, Multipliers) # Return a Bronze Helmet, with saved Level and Multipliers
    elif Name == 'Iron_Helmet': # If the stored item is Iron_Helmet
        return Armour('Iron_Helmet', Level, 'Helmet', 3, Multipliers) # Return an Iron Helmet, with saved Level and Multipliers
    elif Name == 'Platinum_Helmet': # If the stored item is Platinum_Helmet
        return Armour('Platinum_Helmet', Level, 'Helmet', 4, Multipliers) # Return a Platinum Helmet, with saved Level and Multipliers

    elif Name == 'None_Chestplate': # If no chestplate is equipped
        return Armour('None_Chestplate', 0, 'ChestPlate', 0, Multipliers) # Return a default empty ChestPlate
    elif Name == 'Leather_Chestplate': # If the stored item is Leather_Chestplate
        return Armour('Leather_Chestplate', Level, 'ChestPlate', 1, Multipliers) # Return a Leather Chestplate, with saved Level and Multipliers
    elif Name == 'Bronze_Chestplate': # If the stored item is Bronze_Chestplate
        return Armour('Bronze_Chestplate', Level, 'ChestPlate', 2, Multipliers) # Return a Bronze Chestplate, with saved Level and Multipliers
    elif Name == 'Iron_Chestplate': # If the stored item is Iron_Chestplate
        return Armour('Iron_Chestplate', Level, 'ChestPlate', 3, Multipliers) # Return an Iron Chestplate, with saved Level and Multipliers
    elif Name == 'Platinum_Chestplate': # If the stored item is Platinum_Chestplate
        return Armour('Platinum_Chestplate', Level, 'ChestPlate', 4, Multipliers) # Return a Platinum Chestplate, with saved Level and Multipliers

    elif Name == 'None_Boot': # If no boots are equipped
        return Armour('None_Boot', 0, 'Boot', 0, Multipliers) # Return default empty Boots
    elif Name == 'Leather_Boot': # If the stored item is Leather_Boot
        return Armour('Leather_Boot', Level, 'Boot', 1, Multipliers) # Return Leather Boots, with saved Level and Multipliers
    elif Name == 'Bronze_Boot': # If the stored item is Bronze_Boot
        return Armour('Bronze_Boot', Level, 'Boot', 2, Multipliers) # Return Bronze Boots, with saved Level and Multipliers
    elif Name == 'Iron_Boot': # If the stored item is Iron_Boot
        return Armour('Iron_Boot', Level, 'Boot', 3, Multipliers) # Return Iron Boots, with saved Level and Multipliers
    elif Name == 'Platinum_Boot': # If the stored item is Platinum_Boot
        return Armour('Platinum_Boot', Level, 'Boot', 4, Multipliers) # Return Platinum Boots, with saved Level and Multipliers

    #--- Items/Potions ---
    elif Name == 'None': # If slot is empty or nothing equipped
        return Item('None', 0) # Return a basic empty item

    elif Name == 'Health_Potion_Small': # If the stored item is Health_Potion_Small
        return Potion('Health_Potion_Small', Level, 'Health', 10) # Return a small health potion healing 10
    elif Name == 'Health_Potion_Medium': # If the stored item is Health_Potion_Medium
        return Potion('Health_Potion_Medium', Level, 'Health', 25) # Return a medium health potion healing 25
    elif Name == 'Health_Potion_Large': # If the stored item is Health_Potion_Large
        return Potion('Health_Potion_Large', Level, 'Health', 50) # Return a large health potion healing 50

    elif Name == 'Stamina_Potion_Small': # If the stored item is Stamina_Potion_Small
        return Potion('Stamina_Potion_Small', Level, 'Stamina', 10) # Return a small stamina potion restoring 10
    elif Name == 'Stamina_Potion_Medium': # If the stored item is Stamina_Potion_Medium
        return Potion('Stamina_Potion_Medium', Level, 'Stamina', 25) # Return a medium stamina potion restoring 25
    elif Name == 'Stamina_Potion_Large': # If the stored item is Stamina_Potion_Large
        return Potion('Stamina_Potion_Large', Level, 'Stamina', 50) # Return a large stamina potion restoring 50

    elif Name == 'Mana_Potion_Small': # If the stored item is Mana_Potion_Small
        return Potion('Mana_Potion_Small', Level, 'Mana', 10) # Return a small mana potion restoring 10
    elif Name == 'Mana_Potion_Medium': # If the stored item is Mana_Potion_Medium
        return Potion('Mana_Potion_Medium', Level, 'Mana', 25) # Return a medium mana potion restoring 25
    elif Name == 'Mana_Potion_Large': # If the stored item is Mana_Potion_Large
        return Potion('Mana_Potion_Large', Level, 'Mana', 50) # Return a large mana potion restoring 50

    else: # If item name is not recognized
        return None_Item # Return a fallback None_Item object

def Load_Enemies(G, O, D, Og):
    '''Since JSON files cant store classes, this function loads variable Enemy data into the Enemy'''
    global Goblin, Orc, Druid, Ogre # Globalises the Enemies
    Goblin = Enemy('Goblin', G, 10, 5, 'Fir', 1) # Creates Goblin with the Saved Health Attribute
    Orc = Enemy('Orc', O, 20, 7, 'Wat', 8) # Creates Orc with the Saved Health Attribute
    Druid = Enemy('Druid', D, 20, 12, 'Nat', 16) # Creates Druid with the Saved Health Attribute
    Ogre = Enemy('Ogre', Og, 50, 10, 'Fir', 20) # Creates Ogre with the Saved Health Attribute

#--- Variables ---
User = None # Creates the User Tag

Load_File = 0 # Predefines the Load File to be 0 - No Load_File

#--- Items ---
Stick = Weapons('Stick', 1, 'Stick', 2) # Creates a Weapon named Stick that does 2 damage

# Swords
Wooden_Sword = Weapons('Wooden_Sword', 3, 'Sword', 4) # Creates a Sword named Wooden_Sword that does 4 damage
Bronze_Sword = Weapons('Bronze_Sword', 6, 'Sword', 5) # Creates a Sword named Bronze_Sword that does 5 damage
Iron_Sword = Weapons('Iron_Sword', 12, 'Sword', 6) # Creates a Sword named Iron_Sword that does 6 damage
Platinum_Sword = Weapons('Platinum_Sword', 16, 'Sword', 8) # Creates a Sword named Platinum_Sword that does 8 damage

# Axes
Wooden_Axe = Weapons('Wooden_Axe', 3, 'Axe', 4) # Creates an Axe named Wooden_Axe that does 4 damage
Bronze_Axe = Weapons('Bronze_Axe', 6, 'Axe', 5) # Creates an Axe named Bronze_Axe that does 5 damage
Iron_Axe = Weapons('Iron_Axe', 12, 'Axe', 6) # Creates an Axe named Iron_Axe that does 6 damage
Platinum_Axe = Weapons('Platinum_Axe', 16, 'Axe', 8) # Creates an Axe named Platinum_Axe that does 8 damage

# Maces
Wooden_Mace = Weapons('Wooden_Mace', 3, 'Mace', 4) # Creates a Mace named Wooden_Mace that does 4 damage
Bronze_Mace = Weapons('Bronze_Mace', 6, 'Mace', 5) # Creates a Mace named Bronze_Mace that does 5 damage
Iron_Mace = Weapons('Iron_Mace', 12, 'Mace', 6) # Creates a Mace named Iron_Mace that does 6 damage
Platinum_Mace = Weapons('Platinum_Mace', 16, 'Mace', 8) # Creates a Mace named Platinum_Mace that does 8 damage

#--- Armour ---
# Helmet
None_Helmet = Armour('None_Helmet', 0, 'Helmet', 0) # Creates a Helmet named None_Helmet that provides 0 protection
Leather_Helmet = Armour('Leather_Helmet', 1, 'Helmet', 1) # Creates a Helmet named Leather_Helmet that provides 1 protection
Bronze_Helmet = Armour('Bronze_Helmet', 3, 'Helmet', 2) # Creates a Helmet named Bronze_Helmet that provides 2 protection
Iron_Helmet = Armour('Iron_Helmet', 6, 'Helmet', 3) # Creates a Helmet named Iron_Helmet that provides 3 protection
Platinum_Helmet = Armour('Platinum_Helmet', 10, 'Helmet', 4) # Creates a Helmet named Platinum_Helmet that provides 4 protection

# ChestPlate
None_Chestplate = Armour('None_Chestplate', 0, 'ChestPlate', 0) # Creates a ChestPlate named None_Chestplate that provides 0 protection
Leather_Chestplate = Armour('Leather_Chestplate', 1, 'ChestPlate', 1) # Creates a ChestPlate named Leather_Chestplate that provides 1 protection
Bronze_Chestplate = Armour('Bronze_Chestplate', 3, 'ChestPlate', 2) # Creates a ChestPlate named Bronze_Chestplate that provides 2 protection
Iron_Chestplate = Armour('Iron_Chestplate', 6, 'ChestPlate', 3) # Creates a ChestPlate named Iron_Chestplate that provides 3 protection
Platinum_Chestplate = Armour('Platinum_Chestplate', 10, 'ChestPlate', 4) # Creates a ChestPlate named Platinum_Chestplate that provides 4 protection

# Boot
None_Boot = Armour('None_Boot', 0, 'Boot', 0) # Creates a Boot named None_Boot that provides 0 protection
Leather_Boot = Armour('Leather_Boot', 1, 'Boot', 1) # Creates a Boot named Leather_Boot that provides 1 protection
Bronze_Boot = Armour('Bronze_Boot', 3, 'Boot', 2) # Creates a Boot named Bronze_Boot that provides 2 protection
Iron_Boot = Armour('Iron_Boot', 6, 'Boot', 3) # Creates a Boot named Iron_Boot that provides 3 protection
Platinum_Boot = Armour('Platinum_Boot', 10, 'Boot', 4) # Creates a Boot named Platinum_Boot that provides 4 protection

# Items
None_Item = Item('None', 0) # Creates an Item named None

# Potions
Health_Potion_Small = Potion('Health_Potion_Small', 1, 'Health', 10) # Creates a Potion named Health_Potion_Small that replenishes 10 Health
Health_Potion_Medium = Potion('Health_Potion_Medium', 3, 'Health', 25) # Creates a Potion named Health_Potion_Medium that replenishes 25 Health
Health_Potion_Large = Potion('Health_Potion_Large', 5, 'Health', 50) # Creates a Potion named Health_Potion_Large that replenishes 50 Health

Stamina_Potion_Small = Potion('Stamina_Potion_Small', 1, 'Stamina', 10) # Creates a Potion named Stamina_Potion_Small that replenishes 10 Stamina
Stamina_Potion_Medium = Potion('Stamina_Potion_Medium', 3, 'Stamina', 25) # Creates a Potion named Stamina_Potion_Medium that replenishes 25 Stamina
Stamina_Potion_Large = Potion('Stamina_Potion_Large', 5, 'Stamina', 50) # Creates a Potion named Stamina_Potion_Large that replenishes 50 Stamina

Mana_Potion_Small = Potion('Mana_Potion_Small', 1, 'Mana', 10) # Creates a Potion named Mana_Potion_Small that replenishes 10 Mana
Mana_Potion_Medium = Potion('Mana_Potion_Medium', 3, 'Mana', 25) # Creates a Potion named Mana_Potion_Medium that replenishes 25 Mana
Mana_Potion_Large = Potion('Mana_Potion_Large', 5, 'Mana', 50) # Creates a Potion named Mana_Potion_Large that replenishes 50 Mana

# Creation of Goblin King Enemy (This does not need to be saved, as once the User has interacted with the Boss, that is the end of their run)
Goblin_King = Enemy('Goblin_King', 100, 100, 15, 'Fir', 100)

#--- Functions ---
# Combat
def Combat(Enemy, Room):
    '''This Function handles the Combat between the Player and an Enemy'''
    global Exited, User  # Uses the Global Exited Variable

    def Attack():
        User.Attacking(Enemy)

    if Enemy.type == 'Fir':  # If the Enemy is Fire Type
        Type = 'Fire'  # Set Type to Fire
    elif Enemy.type == 'Wat':  # If the Enemy is Water Type
        Type = 'Water'  # Set Type to Water
    elif Enemy.type == 'Nat':  # If the Enemy is Nature Type
        Type = 'Nature'  # Set Type to Nature

    print(f"You have Encountered a {Enemy.name}")  # Informs the Player of the Enemy they have encountered

    while True:  # Runs the Combat Loop until someone wins or loses
        Exited = False  # Reset Exited at the start of each loop
        print(f"""
    +-----------------------------------------------+
    |{' '*21}Enemy{' '*21}|
    +-----------------------------------------------+
    {Enemy.name}: 
        Health:  ♥️  \033[31m{StatBar(Enemy.health, Enemy.max_health)} ({Enemy.health}/{Enemy.max_health})
        Damage:  ⚔️  \033[34m{Enemy.damage}\033[0m
        Type:    ☯️  \033[33m{Type}\033[0m

    {User.Player_Name}:
        Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} ({User.Health['Health']}/{User.Health['Max_Health']})
        Damage:  ⚔️  \033[34m{User.WeaponSlot.damage}\033[0m
        Elemental Damage:        ☯️  \033[33m{User.WeaponSlot.multiplyers[Enemy.type]}\033[0m
        Elemental Protection:    ☯️  \033[33m{round((User.HelmetSlot.multiplyers[Enemy.type] + User.ChestplateSlot.multiplyers[Enemy.type] + User.BootSlot.multiplyers[Enemy.type]) / 3)}\033[0m
        """) # Displays Full Combat UI with Stats for Both the Player and Enemy

        if Enemy.health <= 0:  # If the Enemy has run out of Health
            if Room != 'GoblinKing': # If the Player is not battling GoblinKing
                ClearLines(17)  # Clears the Combat UI
                print(f"You have defeated the {Enemy.name}!")  # Informs the Player they won
                User.WeaponSlot.level += Enemy.level / 2  # Increases the Weapon Level by Half the Enemy Level
                input("Press Enter to continue...")
                setattr(User, Room, True) # Set the Room variable for the Player to be True
                PrintMainUI(Room)

            else:
                DefeatedGK()

        elif User.Health['Health'] <= 0:  # If the Player has run out of Health
            Died(Enemy.name)
            break

        Input_Selection({
            "Attack": lambda: Attack(),  # Attacks the Enemy
            "Use Item": lambda: DisplayInventoryScreen()  # Opens Inventory to Use Items
        })

            # After using an item, Exited may be set to True, so check before enemy attacks
        if Exited:
            pass
        else:
            Enemy.Attacking(User)  # The Enemy Attacks the Player

        ClearLines(20)  # Clears the Combat UI before Refreshing

# UI
def PrintMainUI(Room):
    '''This Function combines a variety of other functions - and Displays them in the correct way'''
    Exited = False # Sets Exited to False
    os.system('cls') # Clears the Screen
    
    if User.Health['Health'] <= 0: # If the User has ran out of Health
        Died('No Health') # Run the Player has Died due to No health
    elif User.Stamina['Stamina'] <= 0: # If the User has ran out of Stamina
        Died('No Stamina') # Run the Player has Died due to No Stamina
    
    User.Location = Room # Sets the Users Location to be the Current Room    

    map_lines = Map(Room).splitlines() # Splits the Lines from Map
    stats_lines = DisplayStats().splitlines() # Splits the Lines for Stats
    inventory_lines = DisplayInventory().splitlines() # Splits the Lines for Player Inventory
    MapKey_lines = DisplayMapKey().splitlines() # Splits the Line from Map Key

    side_panel = stats_lines + inventory_lines + MapKey_lines # Combines the Lines of each of the elements to be printed on the Side Panel
    max_lines = max(len(map_lines), len(side_panel)) # Calculates which is the Tallest (Map or Side Panel)

    print() # Creates a Spacer in the Terminal

    for i in range(max_lines): # For each line in (Which ever Element had more Lines)
        map_line = map_lines[i] if i < len(map_lines) else "" # Figures out if their is content in the Lines - Else: Sets it to be a Blank line - But a Line that Exists
        side_line = side_panel[i] if i < len(side_panel) else "" # Figures out if their is content in the Lines - Else: Sets it to be a Blank line - But a Line that Exists

        map_width = wcswidth(map_line) # Calculates the Width of the Map line (Accounting for Emojis)
        padding = max(0, 60 - map_width) # Calculates if the Map is Square - If Not - Adds padding
        print(map_line + ' ' * padding + side_line) # Prints the Map Line, then the Padding, then the Side panel line
    
    print() # Creates a Spacer in the Terminal

    for char in Story(Room):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

    print('''
''') # Creates a Spacer in the Terminal
    while True: # Run until broken

        if Room == 'GoblinKing':
            break

        elif Exited == False: # If player has Exited
            setattr(User, Room, True) # Set the Room variable for the Player to be True
            Input_Selection(MoveOptions(Room)) # Runs the Input selection for the Room - Based on the Options from MoveOptions
            ClearLines(len(MoveOptions(Room))+3)
            
        else: # If their is a Problem - Breaks the Loop to stop a crash
            break # Breaks the Loop

def StatBar(Stat, Max_Stat):
    '''This function create statbars for statisics'''
    StatBar = (math.floor(Stat/(Max_Stat/10)))*'█' # Calculates how much health their is based on the Stat and Max Stat
    DeadBar = '' # Initalises 'Dead Bar'

    if StatBar == '' and Stat > 0: # Because it rounds down, if the player is alive, but has below 10% health...
        StatBar = '█' # Gives them 1 block of health

    elif len(StatBar) > 10: # If Health is more than 10
        Statbar = '█'*10 # Sets Stat bar to Full
        return Statbar
        

    for i in range(0, 10-len(StatBar)): # Fills up the excess of statbar to Deadbar
        DeadBar += f'-' # Adds a '-' to DeadBar
        
    return StatBar + f'\033[37m{DeadBar}' # returns the completed Bar - Combines the two, and makes the 'Dead Bar' White

def DisplayStats():
    '''This function displates the Stats Block of the UI'''
    return f''' +───────────--==| Stats |==--───────────+
 │                                       │
 │   Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} \033[0m {f'({User.Health['Health']}/{User.Health['Max_Health']})':<12}│
 │   Stamina: 🔋 \033[32m{StatBar(User.Stamina['Stamina'], User.Stamina['Max_Stamina'])} \033[0m {f'({User.Stamina['Stamina']}/{User.Stamina['Max_Stamina']})':<12}│
 │   Mana:    {f'💠 \033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}' if MountainIssue == True else f'💠\033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}'}│
 │                                       │
 +───────────────────────────────────────+''' # The Mana function is different because that is what lines up with the Mountain and causes problems (More context in Map Comment)

def DisplayInventory():
    '''This function returns the Users Inventory in a Asethetic way'''
    return f''' +──────────────────────────────────--==| Inventory |==--──────────────────────────────────+
 │   {'🪙  Gold':<12} -   {User.Gold:<68} │
 │   {'Weapon':<12} -   {User.WeaponSlot.name:<25} {'Chestplate':<12} -   {User.ChestplateSlot.name:<25} │
 │   {'Helmet':<12} -   {User.HelmetSlot.name:<25} {'Boots':<12} -   {User.BootSlot.name:<25} │
 +{'─'*89}+ 
 │   {User.OtherSlot1['Item'].name:<28} -   {User.OtherSlot1['Qty']:<9} {User.OtherSlot2['Item'].name:<28} -   {User.OtherSlot2['Qty']:<9} │
 │   {User.OtherSlot3['Item'].name:<28} -   {User.OtherSlot3['Qty']:<9} {User.OtherSlot4['Item'].name:<28} -   {User.OtherSlot4['Qty']:<9} │
 +{'─'*89}+'''

def DisplayMapKey():
    '''This function returns the Map key - Allowing the User to figure out which symbols mean what'''
    return f''' +─────────────────────────--==| Map Key |==--─────────────────────────+
 │   ██ - You              🔮 - Wizard Tower                           │
 │   🏠 - Village          💀 - Enemy             👑 - Goblin King     │
 │   🌲 - Forest           🏔️  - Mountain                               │
 +─────────────────────────────────────────────────────────────────────+'''

def DisplayInventoryScreen():
    global Exited

    def SetItemUsed():
        global Exited
        Exited = True
        
    print(f'''
    {' '*40}       -= Dmg / Pro =-   -= Fir =-= Wat =-= Nat =-
    WeaponSlot:       {User.WeaponSlot.name:<30}     {User.WeaponSlot.damage:<13}  {str(User.WeaponSlot.multiplyers['Fir'])[:3]:<5}   {str(User.WeaponSlot.multiplyers['Wat'])[:5]:<5}   {str(User.WeaponSlot.multiplyers['Nat'])[:5]:<5}
    HelmetSlot:       {User.HelmetSlot.name:<30}     {User.HelmetSlot.protection:<13}  {str(User.HelmetSlot.multiplyers['Fir'])[:3]:<5}   {str(User.HelmetSlot.multiplyers['Wat'])[:5]:<5}   {str(User.HelmetSlot.multiplyers['Nat'])[:5]:<5}
    ChestplateSlot:   {User.ChestplateSlot.name:<30}     {User.ChestplateSlot.protection:<13}  {str(User.ChestplateSlot.multiplyers['Fir'])[:3]:<5}   {str(User.ChestplateSlot.multiplyers['Wat'])[:5]:<5}   {str(User.ChestplateSlot.multiplyers['Nat'])[:5]:<5}
    BootSlot:         {User.BootSlot.name:<30}     {User.BootSlot.protection:<13}  {str(User.BootSlot.multiplyers['Fir'])[:3]:<5}   {str(User.BootSlot.multiplyers['Wat'])[:5]:<5}   {str(User.BootSlot.multiplyers['Nat'])[:5]:<5}
    
    Gold:             {str(User.Gold)} 🪙
''')
    print('''
Which Item would you like to use?
    ''')
    
    options = {}
    for slot in [User.OtherSlot1, User.OtherSlot2, User.OtherSlot3, User.OtherSlot4]:
        item = slot['Item']
        if item.name != 'None':
            options[f"{item.name:<25} - ({slot['Qty']})"] = lambda item=item: item.Use_Potion(User)
    options['Exit'] = lambda: SetItemUsed()

    
    Input_Selection(options)
        
    ClearLines(15 + len(options))

def TitleScreen():
    '''This Function Handles Displaying and calculating what happens in the TitleScreen'''
    def OverWrite():
        '''This functions handles what to do if the User wants to Overwrite a Save file'''
        print('Which save do you you want to overwrite?') # Instructs the User
        print() # Creates a Spacer in the Terminal
        options = {} # Initalises the Options
        if Player_Data_1: # If Player_Data_1 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 1'] = lambda: (load({}, 1)) # Appends Save 1 to Option and starts creating a character with no attributes to save file 1

        elif Player_Data_2: # If Player_Data_2 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 2'] = lambda: (load({}, 2)) # Appends Save 2 to Option and starts creating a character with no attributes to save file 2

        elif Player_Data_3: # If Player_Data_3 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 3'] = lambda: (load({}, 3)) # Appends Save 3 to Option and starts creating a character with no attributes to save file 3
            
        elif Player_Data_4: # If Player_Data_4 is 'Truthfully' - i.e Has Data in it (So Makes Sure it isnt Already Blank)
            options['Save 4'] = lambda: (load({}, 4)) # Appends Save 4 to Option and starts creating a character with no attributes to save file 4

        options['Exit'] = lambda: TitleScreen() # Appends Exit to Option - Restarting back to Titlescreen

        Input_Selection(options) # Loads Options into Input Selection
                
    os.system('cls') # Clears Screen
    try: # Try to open Save 1 and Append it to Player_Data_1
        with open(f'Save1.json', 'r') as f:
            Player_Data_1 = json.load(f)
    except: # If JSON is blank, sets Player_Data_1 to a Blank Dictionary
        Player_Data_1 = {} # Sets to blank Dictionary
    
    try: # Try to open Save 2 and Append it to Player_Data_2
        with open(f'Save2.json', 'r') as f:
            Player_Data_2 = json.load(f)
    except: # If JSON is blank, sets Player_Data_2 to a Blank Dictionary
        Player_Data_2 = {} # Sets to blank Dictionary

    try: # Try to open Save 3 and Append it to Player_Data_3
        with open(f'Save3.json', 'r') as f:
            Player_Data_3 = json.load(f)
    except: # If JSON is blank, sets Player_Data_3 to a Blank Dictionary
        Player_Data_3 = {} # Sets to blank Dictionary
   
    try: # Try to open Save 4 and Append it to Player_Data_4
        with open(f'Save4.json', 'r') as f:
                Player_Data_4 = json.load(f)
    except: # If JSON is blank, sets Player_Data_4 to a Blank Dictionary
        Player_Data_4 = {} # Sets to blank Dictionary

    # Prints the Title of the Game, and each of the Save Name and Location - If their is no save information - Sets it to None
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


    ''')
    Input_Selection({ # Sends the Dictionary to Input_Selection
         'Save 1': lambda: (load(Player_Data_1, 1)), # Sets Save 1 to Load data from Player_Data_1 to load
         'Save 2': lambda: (load(Player_Data_2, 2)), # Sets Save 2 to Load data from Player_Data_2 to load
         'Save 3': lambda: (load(Player_Data_3, 3)), # Sets Save 3 to Load data from Player_Data_3 to load
         'Save 4': lambda: (load(Player_Data_4, 4)), # Sets Save 4 to Load data from Player_Data_4 to load
         'OverWrite Save': lambda: OverWrite(), # If player Wants to OverWrite a Save - OverWrites it
         'Exit': lambda: quit() # If the player wants to leave, quits the program
    })

    PrintMainUI(User.Location) # Starts to Game Based of the Users Location

def Input_Selection(options: dict): # ":dict" - Ensures it is a Dictionary
    '''This function handles the Input selection process for a variety of functions in my program'''
    def ReplaceInput():
        '''This function replaces the Input and prints Error Message'''
        ClearLines(2)  # Clears 2 Lines Above
        print('Error With Input') # Error Message
        return get_input()  # Re-prompt's the User for an Input
    
    def get_input():
        '''This function handles recieving Inputs from the User'''
        try: # Try to Recieve and Input from the User
            SaveSelection = input('Choice: ') # Recieve input from User
            SaveSelection = int(SaveSelection) # Check if Input is a Integer
            if 1 <= SaveSelection <= len(option_list): # if Input is an option in avaliable options
                option_list[SaveSelection - 1][1]()  # Call the corresponding function
            else: # If it is not an Option
                ReplaceInput() # Give an Error Message
        except Exception: # If error with Input (but not SystemExit)
            ReplaceInput() # Give an Error Message

    # Print options
    option_list = list(options.items()) # Option List is List of Dictionary
    print("Select an option:") # Directs User
    for i, (name, _) in enumerate(option_list, start=1): # For Each Option in option list, display the Item and its associated value
        print(f"{i}. {name}")  # Prints the Number and the Name of the function it is associated to
    print() # Creates a Spacer in the Terminal
    get_input() # Runs Recieve Input

# Player Functions
def load(Player_Data, Save):
    '''Loads Player Data from the JSON to the format for creating a Player'''
    global User, Load_File # Globalises the User and Load file Attributes

    Load_File = Save # Sets the Load File

    if len(Player_Data) == 0: # If their is no save data
        CreateCharacter() # Create a Character

    else: # Convert the information from the JSON file to a dictionary to create the player
        Data = { # Creates a dictionary to store all player data
        'Player_Name': Player_Data['Player_Name'], # Stores the player's name

        'Health': Player_Data['Health'], # Stores current and max health
        'Stamina': Player_Data['Stamina'], # Stores current and max stamina
        'Mana': Player_Data['Mana'], # Stores current and max mana

        'Location': Player_Data['Location'], # Stores the last known location
        'Gold': Player_Data['Gold'], # Stores the player's gold amount

        'WeaponSlot': Load_Items(Player_Data['WeaponSlot']['Name'], Player_Data['WeaponSlot']['Level'], Player_Data['WeaponSlot']['Multiplyers']), # Loads the weapon item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'HelmetSlot': Load_Items(Player_Data['HelmetSlot']['Name'], Player_Data['HelmetSlot']['Level'], Player_Data['HelmetSlot']['Multiplyers']), # Loads the helmet item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'ChestplateSlot': Load_Items(Player_Data['ChestplateSlot']['Name'], Player_Data['ChestplateSlot']['Level'], Player_Data['ChestplateSlot']['Multiplyers']), # Loads the chestplate item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'BootSlot': Load_Items(Player_Data['BootSlot']['Name'], Player_Data['BootSlot']['Level'], Player_Data['BootSlot']['Multiplyers']), # Loads the boots item with its properties - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        
        'OtherSlot1': {'Item': Load_Items(Player_Data['OtherSlot1']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot1']['Qty']}, # Loads item in OtherSlot1 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot2': {'Item': Load_Items(Player_Data['OtherSlot2']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot2']['Qty']}, # Loads item in OtherSlot2 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot3': {'Item': Load_Items(Player_Data['OtherSlot3']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot3']['Qty']}, # Loads item in OtherSlot3 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        'OtherSlot4': {'Item': Load_Items(Player_Data['OtherSlot4']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot4']['Qty']}, # Loads item in OtherSlot4 with quantity - Using Load Items - Which takes the variable data and combines it with absolute data and combines to two
        
        'Enemy1': Player_Data['Enemy1'], # Tracks if Enemy1 has been visted
        'Enemy2': Player_Data['Enemy2'], # Tracks if Enemy2 has been visted
        'Enemy3': Player_Data['Enemy3'], # Tracks if Enemy3 has been visted
        'Enemy4': Player_Data['Enemy4'], # Tracks if Enemy4 has been visted

        'Village1': Player_Data['Village1'], # Tracks if Village1 has been visited
        'Village2': Player_Data['Village2'], # Tracks if Village2 has been visited
        'Village3': Player_Data['Village3'], # Tracks if Village3 has been visited

        'Forest1': Player_Data['Forest1'], # Tracks if Forest1 has been visited
        'Forest2': Player_Data['Forest2'], # Tracks if Forest2 has been visited
        'Forest3': Player_Data['Forest3'], # Tracks if Forest3 has been visited
        'Forest4': Player_Data['Forest4'], # Tracks if Forest4 has been visited

        'SeenW1': Player_Data['SeenW1'], # Tracks if the player has met Wizard1
        'SeenW2': Player_Data['SeenW2'], # Tracks if the player has met Wizard2

        'Wizard1': Player_Data['Wizard1'], # Tracks if Wizard1 area has been visted
        'Wizard2': Player_Data['Wizard2'], # Tracks if Wizard2 area has been visted

        'Mountain': Player_Data['Mountain'], # Tracks if the Mountain has been visited

        'GoblinKing': Player_Data['GoblinKing'], # Tracks if Goblin King has been visited

        'RareFlower': Player_Data['RareFlower'], # Tracks if Rare Flower has been collected
        'RareRune': Player_Data['RareRune'], # Tracks if Rare Rune has been collected


        'Enemies': Player_Data['Enemies'] # Stores the state of all enemies
        }


        User = Player(Data) # Creates a new Player object with the loaded data

def CreateCharacter():
    '''This Function Creates a Character if their is no existing player data'''
    global User # Globaises the User Attribute
    print('Welcome New Adventurer!') # Welecomes the User
    while True: # Run until broken
        Name_Input = input("What's your Name Adventurer? ") # Ask's the Player their Name

        if len(Name_Input) == 0: # If User Doesnt Enter a Name
            print("You must enter a name!") # Prints and Error Message
        elif len(Name_Input) > 20: # If the User enters a name that is too long
            print("Your name is too long! Please keep it under 20 characters.") # Prints and Error Message
        else: # If their is no problems with the Users Name
            print(f'Welcome {Name_Input}, This is where your Journey Begins!') # Welcomes user
            break # Breaks the Loop

    Player_Data = { # Initalises Player Data to Defaults
        'Player_Name': Name_Input, # Player Name is set to Players Chosen Name

        'Health': {'Health': 100, 'Max_Health': 100}, # Sets player Health to 100, and Max Health to 100
        'Stamina': {'Stamina': 100, 'Max_Stamina': 100}, # Sets player Stamina to 100, and Max Stamina to 100
        'Mana': {'Mana': 100, 'Max_Mana': 100}, # Sets player Mana to 100, and Max Mana to 100

        'WeaponSlot': Stick, # Sets Users Weapon to Stick
        'HelmetSlot': None_Helmet, # Sets Users Helmet to None_Helmet
        'ChestplateSlot': None_Chestplate, # Sets Users Chestplate to None_Chestplate
        'BootSlot': None_Boot, # Sets Users Boots to None_Boot
        
        'OtherSlot1': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot2': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot3': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0
        'OtherSlot4': {'Item': None_Item, 'Qty': 0}, # Sets Item slot to be None_Item, and Qty to be 0

        'Location': 'Forest1', # Sets Users location to be 'Forest1' - the Default Room
        'Gold': 25, # Sets Users gold to be 25 - 25 is Enough to make money through the Casino - the Lumberjack is more designed to prevent soft locking

        'Enemy1': False, # Sets Room to be False
        'Enemy2': False, # Sets Room to be False
        'Enemy3': False, # Sets Room to be False
        'Enemy4': False, # Sets Room to be False

        'Village1': False, # Sets Room to be False
        'Village2': False, # Sets Room to be False
        'Village3': False, # Sets Room to be False

        'Forest1': False, # Sets Room to be False
        'Forest2': False, # Sets Room to be False
        'Forest3': False, # Sets Room to be False
        'Forest4': False, # Sets Room to be False


        'SeenW1': False, # Sets Seen Wizard 1 to be False
        'SeenW2': False, # Sets Seen Wizard 2 to be False
        
        'Wizard1': False,  # Sets Room to be False
        'Wizard2': False, # Sets Room to be False
        'Mountain': False, # Sets Room to be False
        'GoblinKing': False, # Sets Room to be False

        'RareFlower': False, # Sets Room to be False
        'RareRune': False, # Sets Room to be False

        'Enemies': {'G': 10, 'O': 20, 'D': 20, 'Og': 50} # Sets Room to be False
    }

    User = Player(Player_Data) # Creates a Player based off of those attributes

# Magic
def Enchantment(item, type=None):
    '''This function Enchants items to be more effective against enemy types'''    
    Level = item.level # Sets level to the Item of the Level being Encahanted

    Multiplyer = (random.randint(0, round(Level)+10)/10) # This calculate the strength of the Enchant - with a higher level allowing for a higher chance of a better enchantment

    if type == None: # If Player wants a Neuteral Buff
        item.setmultiplyers({'Wat': (1+((Multiplyer)/4)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1+((Multiplyer)/4))}) # If the Player wants a overall Neutral Buff
    else:
        if type == 'Fir': # If Player wants a Fire Buff 
            item.setmultiplyers({'Wat': (1-((Multiplyer)/4)), 'Fir': (1+(Multiplyer)), 'Nat': (1+((Multiplyer)/4))}) # If the Player wants a stronge buff to Fire, but at the cost of Water Strength
        
        elif type == 'Wat': # If Player wants a Water Buff
            item.setmultiplyers({'Wat': (1+(Multiplyer)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1-((Multiplyer)/4))}) # If the Player wants a strong buff to Water, but at the cost of Nature Strength
        
        elif type == 'Nat': # If Player wants a Nature Buff
            item.setmultiplyers({'Wat': (1+((Multiplyer)/4)), 'Fir': (1-((Multiplyer)/4)), 'Nat': (1+(Multiplyer))}) # If the Player wants a strong buff to Nature, but at the cost of Fire Strenth
# Movement
def MoveOptions(Room):
    '''Curates the Avaliable Moves for the Player based on their current Location'''
    global User  # Access the global User object

    def RemoveStamina(Stamina): 
        '''This function removes stamina from the Player'''
        User.Stamina['Stamina'] -= Stamina  # Removes X stamina from the player

    Default = {
        "Inventory": lambda: DisplayInventoryScreen(),  # Opens the inventory screen
        "Exit": lambda: Exiting()  # Exits the current screen/menu
    }

    def RoomOptions():
        '''Curates the Room Specific Moves'''
        if Room == 'Enemy1':
            return {
                "North East (Enemy2) (6)": lambda: (RemoveStamina(6), PrintMainUI('Enemy2')),  # -6 stamina, loads Enemy2
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),  # -4 stamina, loads Forest2
                "East (Vilage1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),  # -2 stamina, loads Village1
                "West (Forest1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Forest1')),  # -2 stamina, loads Forest1
            }
        elif Room == 'Enemy2':
            return {
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),  # -3 stamina, loads Enemy3
                "South East (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),  # -6 stamina, loads Forest3
                "South West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
                "East (Wizard1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Wizard1')),  # -2 stamina, loads Wizard1
            }
        elif Room == 'Enemy3':
            return {
                "South East (Wizard1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Wizard1')),  # -4 stamina, loads Wizard1
                "South West (Enemy2) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy2')),  # -3 stamina, loads Enemy2
                "West (Mountain) (20)": lambda: (RemoveStamina(20), PrintMainUI('Mountain')),  # -20 stamina, loads Mountain
            }
        elif Room == 'Enemy4':
            return {
                "North West (Forest4) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),  # -8 stamina, loads Village2
                "East (GoblinKing) (4)": lambda: (RemoveStamina(4), PrintMainUI('GoblinKing')),  # -4 stamina, loads GoblinKing
                "West (Village2) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),  # -8 stamina, loads Village2
            }
        elif Room == 'Village1':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village1')),  # Clears 8 lines, enters Village1
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),  # -4 stamina, loads Forest2
                "East (Village2) (5)": lambda: (RemoveStamina(5), PrintMainUI('Village2')),  # -5 stamina, loads Village2
                "West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
            }
        elif Room == 'Village2':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village2')),  # Clears 8 lines, enters Village2
                "South East (Wizard2) (7)": lambda: (RemoveStamina(7), PrintMainUI('Wizard2')),  # -7 stamina, loads Wizard2
                "East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),  # -5 stamina, loads Enemy4
                "West (Village1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),  # -2 stamina, loads Village1
            }
        elif Room == 'Village3':
            return {
                "Enter Village": lambda: (ClearLines(5), EnterVillage('Village3')),  # Clears 5 lines, enters Village1
                "North West (Forest4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest4')),  # -4 stamina, loads Forest4
            }
        elif Room == 'Forest1':
            return {
                "East (Enemy) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),  # -2 stamina, loads Enemy1
            }
        elif Room == 'Forest2':
            if User.SeenW1:
                User.RareFlower = True  # Player receives a rare flower
                print('''
        You found a Rare Flower!
                ''')
            return {
                "North East (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),  # -4 stamina, loads Village1
                "North West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),  # -4 stamina, loads Enemy1
            }
        elif Room == 'Forest3':
            return {
                "North East (Forest4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Forest4')),  # -5 stamina, loads Forest4
                "North West (Enemy2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy2')),  # -4 stamina, loads Enemy2
                "East (Enemy4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),  # -4 stamina, loads Enemy4
                "West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),  # -4 stamina, loads Enemy1
            }
        elif Room == 'Forest4':
            return {
                "South East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),  # -5 stamina, loads Enemy4
                "South West (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),  # -6 stamina, loads Forest3
                "East (Village3) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village3')),  # -4 stamina, loads Village3
            }
        elif Room == 'Wizard1':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard1'),  # Enters Wizard1's tower
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),  # -3 stamina, loads Enemy3
                "West (Enemy2) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy2')),  # -2 stamina, loads Enemy2
            }
        elif Room == 'Wizard2':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard2'),  # Enters Wizard2's tower
                "North East (Village2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village2')),  # -4 stamina, loads Village2
                "North West (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),  # -4 stamina, loads Village1
            }
        elif Room == 'Mountain':
            if User.SeenW2:
                User.RareRune = True  # Player receives a rare rune
                print('''
        You found a Rare Rune!
                ''')
            return {
                "East (Enemy3) (10)": lambda: (RemoveStamina(10), PrintMainUI('Enemy3')),  # -10 stamina, loads Enemy3
            }
        elif Room == 'GoblinKing':
            return {
                "West (Enemy 4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),  # -4 stamina, loads Enemy4
            }
        else:
            return {}  # If no known room, return empty movement options

    options = {}  # Initialize the options dictionary
    options.update(RoomOptions())  # Add movement options for the current room
    options.update(Default)  # Add inventory and exit options
    return options  # Return all available options

def Story(Room):    
    '''
    This function handles the story events based on the current Room the Player is in.
    It checks whether the Player has already visited the Room, and triggers combat if it is the first encounter
    with an enemy. Otherwise, it returns a descriptive story message for the area.
    '''
    
    # Enemy Encounter: Goblin
    if Room == 'Enemy1':  # The function is requesting the storyline for room Enemy1
        if User.Enemy1 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Goblin, 'Enemy1')  # Start combat with the Goblin
            return ''
        else:  # The user has been in this room before
            return '''Ash and smoke linger in the air, the battlefield now eerily quiet. You remember the heat of combat, and the pain it brought.'''

    # Enemy Encounter: Orc
    elif Room == 'Enemy2':  # The function is requesting the storyline for room Enemy2
        if User.Enemy2 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Orc, 'Enemy2')  # Start combat with the Orc
            return ''
        else:  # The user has been in this room before
            return '''The blue blood still stains the earth. You breathe heavily, remembering the brute strength of the Orc and your narrow survival.'''

    # Enemy Encounter: Druid
    elif Room == 'Enemy3':  # The function is requesting the storyline for room Enemy3
        if User.Enemy3 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Druid, 'Enemy3')  # Start combat with the Druid
            return ''
        else:  # The user has been in this room before
            return '''A circle of withered trees marks the place where the Druid fell. The silence feels sacred now, almost like a grave.'''

    # Enemy Encounter: Ogre
    elif Room == 'Enemy4':  # The function is requesting the storyline for room Enemy4
        if User.Enemy4 == False:  # The user has not been in this room before
            input('Press Enter to Enter Combat...')
            Combat(Ogre, 'Enemy4')  # Start combat with the Ogre
            return ''
        else:  # The user has been in this room before
            return '''You stare into the distance, the final road ahead. This was the last guardian before the Goblin King. Are you truly ready?'''

    # Village 1
    elif Room == 'Village1':  # The function is requesting the storyline for room Village1
        if User.Village1 == False:  # The user has not been in this room before
            return '''You step into a lively village where children laugh and fires crackle. Peace, it seems, still exists in this world.'''
        else:  # The user has been in this room before
            return '''The village greets you like an old friend. The same smiles, the same warmth — a comforting familiarity.'''

    # Village 2
    elif Room == 'Village2':  # The function is requesting the storyline for room Village2
        if User.Village2 == False:  # The user has not been in this room before
            return '''You enter a quiet village under dark clouds. Every shadow feels longer, every glance colder — danger is in the air.'''
        else:  # The user has been in this room before
            return '''The uneasy tension remains. Though it's quiet, you can’t shake the feeling that something watches from the trees.'''

    # Village 3
    elif Room == 'Village3':  # The function is requesting the storyline for room Village3
        if User.Village3 == False:  # The user has not been in this room before
            return '''A haunting wind whistles between crooked houses. You wonder how people survive out here, so far from the known world.'''
        else:  # The user has been in this room before
            return '''The villagers wave to you, their faces lit by warm fires. You smile — even in isolation, kindness endures.'''

    # Forest 1 (Starting Point)
    elif Room == 'Forest1':  # The function is requesting the storyline for room Forest1
        if User.Forest1 == False:  # The user has not been in this room before
            return '''Your eyes flutter open among twisted trees and mist. A worn pouch of gold sits beside you, and a crooked stick gleams faintly nearby.'''
        else:  # The user has been in this room before
            return '''You return to where it all began. The darkness of the forest no longer scares you — it feels like home.'''

    # Forest 2
    elif Room == 'Forest2':  # The function is requesting the storyline for room Forest2
        if User.Forest2 == False:  # The user has not been in this room before
            return '''Bright blossoms dot the forest floor. For a moment, the beauty distracts you from the weight of your journey.'''
        else:  # The user has been in this room before
            return '''You pluck a flower and smile. Among all this chaos, even nature finds time to bloom.'''

    # Forest 3 (Center of the World)
    elif Room == 'Forest3':  # The function is requesting the storyline for room Forest3
        if User.Forest3 == False:  # The user has not been in this room before
            return '''Strangely calm, the center of the world offers no grand treasure or battle — just peace, and a whisper of serenity.'''
        else:  # The user has been in this room before
            return '''Returning here eases your mind. The silence heals, and you consider staying... just a little longer.'''

    # Forest 4
    elif Room == 'Forest4':  # The function is requesting the storyline for room Forest4
        if User.Forest4 == False:  # The user has not been in this room before
            return '''After a long hike, you crest a hill to find endless mountains stretching beneath a golden sky. The wind is crisp, the view breathtaking.'''
        else:  # The user has been in this room before
            return '''The wind greets you again as you look out across the vast wilds. Some things never lose their wonder.'''

    # Wizard Tower 1
    elif Room == 'Wizard1':  # The function is requesting the storyline for room Wizard1
        if User.Wizard1 == False:  # The user has not been in this room before
            return '''A crooked stone tower leans impossibly to one side. How it still stands is beyond reason or physics.'''
        else:  # The user has been in this room before
            return '''The tower creaks in the wind, still standing against all odds. You wonder how many more visits it can endure.'''

    # Wizard Tower 2
    elif Room == 'Wizard2':  # The function is requesting the storyline for room Wizard2
        if User.Wizard2 == False:  # The user has not been in this room before
            return '''The second tower is even stranger — half-buried, with missing stones and an angle so steep it defies gravity.'''
        else:  # The user has been in this room before
            return '''Each time you gaze upon this broken tower, you're filled with both dread and awe — magic, no doubt, is involved.'''

    # Mountain Peak
    elif Room == 'Mountain':  # The function is requesting the storyline for room Mountain
        if User.Mountain == False:  # The user has not been in this room before
            return '''You climb higher than you ever have. The biting wind stings your face, but the sight of endless snow is unforgettable.'''
        else:  # The user has been in this room before
            return '''You trudge through the snow again. Nothing has changed — white, cold, endless. Why did you return?'''

    # Final Battle: Goblin King
    elif Room == 'GoblinKing':  # The function is requesting the storyline for room GoblinKing
        Combat(Goblin_King, 'GoblinKing')
        return''
    
def Map(Room):
    global MountainIssue
    if Room == 'Mountain': # If the Room is Mountain
        MountainIssue = True # Mountain Issue is True (This is because the Mountain Emoji's are some of the only emoji's that are 2 character symbols long - But created the issue where it would skew the UI elements, not in the part adjectent to the map, but at the next part Ascii Component)
    else: # If room isn't mountain
        MountainIssue = False # Sets MountainIssue to False

    def pad(symbol, width=2):
        '''This function uses wcswidth to adjust the Emojis to better calculate the width'''
        real_width = wcswidth(symbol)
        return symbol + ' ' * (width - real_width)

    Enemy1 = pad('💀') if Room != 'Enemy1' else pad('██') # If room is Enemy1, changes the Room Icon to the Player Icon
    Enemy2 = pad('💀') if Room != 'Enemy2' else pad('██') # If room is Enemy2, changes the Room Icon to the Player Icon
    Enemy3 = pad('💀') if Room != 'Enemy3' else pad('██') # If room is Enemy3, changes the Room Icon to the Player Icon
    Enemy4 = pad('💀') if Room != 'Enemy4' else pad('██') # If room is Enemy4, changes the Room Icon to the Player Icon
    Village1 = pad('🏠') if Room != 'Village1' else pad('██') # If room is Village1, changes the Room Icon to the Player Icon
    Village2 = pad('🏠') if Room != 'Village2' else pad('██') # If room is Village2, changes the Room Icon to the Player Icon
    Village3 = pad('🏠') if Room != 'Village3' else pad('██') # If room is Village3, changes the Room Icon to the Player Icon
    Forest1 = pad('🌲') if Room != 'Forest1' else pad('██') # If room is Forest1, changes the Room Icon to the Player Icon
    Forest2 = pad('🌲') if Room != 'Forest2' else pad('██') # If room is Forest2, changes the Room Icon to the Player Icon
    Forest3 = pad('🌲') if Room != 'Forest3' else pad('██') # If room is Forest3, changes the Room Icon to the Player Icon
    Forest4 = pad('🌲') if Room != 'Forest4' else pad('██') # If room is Forest4, changes the Room Icon to the Player Icon
    Wizard1 = pad('🔮') if Room != 'Wizard1' else pad('██') # If room is Wizard1, changes the Room Icon to the Player Icon
    Wizard2 = pad('🔮') if Room != 'Wizard2' else pad('██') # If room is Wizard2, changes the Room Icon to the Player Icon
    Mountain = pad('🏔️ ') if Room != 'Mountain' else pad('██') # If room is Mountain, changes the Room Icon to the Player Icon
    GoblinKing = pad('👑') if Room != 'GoblinKing' else pad('██') # If room is GoblinKing, changes the Room Icon to the Player Icon

    def TitleGenerator(Title):
        '''This function creates a centered title for each of the Rooms, being able to adapt to the length of the title''' 
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+' # Math to calculate the Center and have everything fit

    # This returns the Map, with each of the Locations attcaked with their variables - This system - While more complex - is significantly more efficient in creating the map
    return f'''    {TitleGenerator(Room)}
    │                                                       │
    │           ┌──────{Enemy3}          {Forest4} ────┐                 │
    │           │       │           │     │                 │
    │     {Mountain} ───┘       │           │     │                 │
    │                   │           │     └────{Village3}           │
    │               {Enemy2} ─┴────{Wizard1}     │                       │
    │                │              │                       │
    │        ┌───────┴────────┬─────┤                       │
    │        │                │     └───────┐               │
    │ {Forest1}────{Enemy1}      {Village1}       {Forest3}             ├────{Enemy4} ────{GoblinKing}  │
    │        │       │            {Village2} ───────┘               │
    │        └────┬──┴──┬──────────┘                        │
    │             │     │                                   │
    │             │     └──┐                                │
    │             │        │                                │
    │        {Forest2} ──┘        │                             ⬆  │
    │                      └────────────{Wizard2}               N  │
    │                                                       │
    +───────────────────────────────────────────────────────+'''

def EnterVillage(Village):
    '''This function handles the process of creating villagers, and displaying them in the Village'''

    Mort = ArmourSmith('Mort') # Creates an ArmourSmith named Mort
    Alex = AxeSmith('Alex') # Creates an AxeSmith named Alex
    Melvin = Brewer('Melvin') # Creates a Brewer named Melvin
    Zuba = LumberJack('Zuba') # Creates a LumberJack named Zuba

    Bill = Gambler('Bill') # Creates a Gambler named Bill

    Julian = ArmourSmith('Julian') # Creates an ArmourSmith named Julian
    Gloria = SwordSmith('Gloria') # Creates a SwordSmith named Gloria
    Marty = AxeSmith('Marty') # Creates an AxeSmith named Marty
    Kowalski = Brewer('Kowalski') # Creates a Brewer named Kowalski
    Moto = LumberJack('Moto') # Creates a LumberJack named Moto

    Dole = Gambler('Dole') # Creates a Gambler named Dole

    Maurice = ArmourSmith('Maurice') # Creates an ArmourSmith named Maurice
    Rico = SwordSmith('Rico') # Creates a SwordSmith named Rico
    Skipper = Brewer('Skipper') # Creates a Brewer named Skipper
    Milton = LumberJack('Milton') # Creates a LumberJack named Milton

    Doh = Gambler('Doh') # Creates a Gambler named Doh

    while True: # Continuously loop until the player chooses to exit
        os.system('cls') # Clears the terminal screen
        print('Select a Merchant to Interact With!') # Prompts the user to select a merchant
        print() # Prints a blank line for spacing

        Exiting = False # Initializes the exiting flag as False

        def Break():
            '''This function handles when the User wants to exit the Village'''
            nonlocal Exiting # Allows modification of the Exiting variable from the outer scope
            os.system('cls') # Clears the terminal screen
            print() # Prints a blank line for spacing
            print('Select a Merchant to Interact With!') # Re-prompts the user after exiting
            print() # Prints a blank line for spacing
            Exiting = True # Sets the exiting flag to True

        if Village == 'Village1': # If the player is in Village1
            Input_Selection({ # Displays the merchant options for Village1
                'Mort - Armoursmith': lambda: Mort.Inventory_Trading(), # Opens Mort's armour shop
                'Alex - Axesmith': lambda: Alex.Inventory_Trading(), # Opens Alex's axe shop
                'Melvin - Brewer': lambda: Melvin.Inventory_Trading(), # Opens Melvin's potion shop
                'Zuba - LumberJack': lambda: Zuba.ChopWood(), # Starts Zuba's woodcutting activity
                'Bill - Casino Owner': lambda: Bill.Casino(), # Enters Bill's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

        elif Village == 'Village2': # If the player is in Village2
            Input_Selection({ # Displays the merchant options for Village2
                'Julian - Armoursmith': lambda: Julian.Inventory_Trading(), # Opens Julian's armour shop
                'Gloria - Swordsmith': lambda: Gloria.Inventory_Trading(), # Opens Gloria's sword shop
                'Marty - Axesmith': lambda: Marty.Inventory_Trading(), # Opens Marty's axe shop
                'Kowalski - Brewer': lambda: Kowalski.Inventory_Trading(), # Opens Kowalski's potion shop
                'Moto - LumberJack': lambda: Moto.ChopWood(), # Starts Moto's woodcutting activity
                'Dole - Casino Owner': lambda: Dole.Casino(), # Enters Dole's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

        elif Village == 'Village3': # If the player is in Village3
            Input_Selection({ # Displays the merchant options for Village3
                'Maurice - Armoursmith': lambda: Maurice.Inventory_Trading(), # Opens Maurice's armour shop
                'Rico - Swordsmith': lambda: Rico.Inventory_Trading(), # Opens Rico's sword shop
                'Skipper - Brewer': lambda: Skipper.Inventory_Trading(), # Opens Skipper's potion shop
                'Milton - LumberJack': lambda: Milton.ChopWood(), # Starts Milton's woodcutting activity
                'Doh - Casino Owner': lambda: Doh.Casino(), # Enters Doh's casino
                'Exit': lambda: Break() # Allows the user to exit the village
            })

            if Exiting == True: # If the user chose to exit
                break # Exits the loop and village interface

    PrintMainUI(Village) # Returns the user back to the main UI of the current village

def EnterWizardTower(wizard_room):
    '''This Function handles the Wizard Tower Interactions, and Ensuring a Wizard is Intialised'''
    Jake = Wizard('Jake') # Since the Name of the Wizard is Irrelivent for the Wizard function, the rooms can share the same Wizard Object

    Jake.WizardStore(wizard_room) # Runs the Wizard Store function, also providing which room it is happening in, allowing the Function to differenciate between the two rooms

def ClearLines(n):
    '''This function allows me to clear lines by the specified amount'''
    for _ in range(n): # For each of the lines specified in the Parameters
        print("\033[1A\033[2K", end="") # Clear the most recent line

def Exiting():
    '''Handles the Exiting of the Game back to the Titlescreen'''
    global Load_File, User # Globaises the Varibales
    User.Save(Load_File) # Saves the Users Progress
    User = None # Resets the User
    Load_File = 0 # Resets the Load File
    TitleScreen() # Restarts back to the Titlescreen

def Died(DeathCause):
    '''This Function handles the Death of the Player'''
    global Load_File # Globalises the Variables in the Function
    os.system('cls') # Clears the Screen
    # Prints You Died Ascii Art and the Death message
    print(f'''
 ▄· ▄▌      ▄• ▄▌    ·▄▄▄▄  ▪  ▄▄▄ .·▄▄▄▄  
▐█▪██▌▪     █▪██▌    ██▪ ██ ██ ▀▄.▀·██▪ ██ 
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▐█· ▐█▌▐█·▐▀▀▪▄▐█· ▐█▌
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ██. ██ ▐█▌▐█▄▄▌██. ██ 
  ▀ •  ▀█▄▀▪ ▀▀▀     ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀• 

You Died to {DeathCause}
''')
    input('Enter to Delete Save...') # Waits so the user can see

    with open(f'Save{Load_File}.json', 'w') as file: # Opens the Current save file
        json.dump({}, file) # Dumps an empty dictionary to the file - Causing it to get deleted
    
    Load_File = 0

    TitleScreen() # Loads the Titlescreen Program - Restating the Program

def DefeatedGK():
    '''
    This function is called when the player defeats the Goblin King.
    It clears the terminal and displays a heartfelt, cinematic conclusion to the game.
    '''
    global Load_File
    os.system('cls')  # Clears the terminal for a clean ending screen

    # Prints the Victory Message to the Player
    print('''
╔══════════════════════════════════════════════════════════════╗
║                   ✨ VICTORY IN NIADON ✨                    ║
╚══════════════════════════════════════════════════════════════╝

With a final cry, the Goblin King falls — his reign of terror ended,
his crown shattered on the stone floor of his dark throne room.

The skies above Niadon begin to clear for the first time in years.
Sunlight pierces the once-eternal gloom, casting golden light
across the mountains, forests, and forgotten ruins.

Villages rejoice. Children sing your name. Stories of your bravery
echo across every continent, whispered around fires and carved into stone.

You are no longer just a wanderer...

               You are the Hero of Niadon.

Thank you, brave adventurer, for your courage, your sacrifice,
and your unyielding spirit. You restored balance to a world on the brink.

                 May peace follow in your footsteps.

════════════════════════════════════════════════════════════════

                ~ THE END ~     (for now...)

    ''')

    input('Enter to Complete Game (This Resets Save File Information)...')

    with open(f'Save{Load_File}.json', 'w') as file: # Opens the Current save file
        json.dump({}, file) # Dumps an empty dictionary to the file - Causing it to get deleted
    
    Load_File = 0

    TitleScreen() # Loads the Titlescreen Program - Restating the Program

TitleScreen() # Runs the Program from Titlescreen


```


## Final Evaluation Questions
### Explain how you could improve your system in future updates. Analyse the impact these updates could have on the user experience.

My current system was designed with robustness in mind, a stable and expandable foundation for future content, which was chosen to allign with the Agile Design process. While the base game functions well and delivers the core experience, there are several key improvements I would like to implement in future updates to enhance both gameplay depth and user experience.

1. **Expanding Game Content and World Exploration**

One of the most significant improvements would be to add more content to the game. At present, the player’s experience is somewhat limited in terms of exploration, available quests, and meaningful interactions. I would like to add more rooms, unique characters, hidden areas, diverse enemies, and side quests that reward exploration and strategic thinking.

**Impact on User Experience:**

Adding more content would directly improve engagement and replayability. Players would feel more immersed in the game world and more motivated to continue playing. It would also give them a greater sense of progression and accomplishment, reducing repetition and increasing the overall enjoyment of the game.

2. **Enhancing Data Presentation and Gameplay Clarity**

Another key area for improvement is how data is calculated and displayed. Currently, while stats like health, stamina, and damage exist, their calculation and visual representation could be made clearer and more intuitive. For example, showing real-time stat changes after actions, clearer descriptions of effects (e.g. elemental damage multipliers), and more informative UI feedback could help players better understand the consequences of their decisions.

**Impact on User Experience:**

Improved clarity would make the game's core mechanics more accessible, especially for new players. This would reduce confusion, allow for more strategic planning, and ultimately create a smoother, more satisfying experience. It helps players feel in control and capable, which is crucial in an RPG-style system.

3. **Deepening the Magic and Mana System**

Finally, I want to further develop the game’s magic and mana systems. While these elements exist, their current implementation is limited. I aim to introduce more types of magical abilities, enchanted gear that interacts with mana, and even mana-based puzzles or combat effects. Mana would become a key resource players manage carefully, and magic could be customized or leveled up over time.

**Impact on User Experience:**

A more complex and rewarding magic system would provide players with alternative playstyles and enhance combat variety. It encourages creativity and planning, as players can specialize in magical strategies rather than relying solely on weapons or brute force. This added depth also allows for richer character builds and improves overall game balance by providing viable alternatives to physical attacks.

By focusing on expanding content, improving system transparency, and enhancing underused gameplay mechanics like magic, future updates would significantly improve player satisfaction, engagement, and replay value. These changes build upon the current strong foundation and ensure the system continues to grow in complexity and enjoyment.

4. **Better Code Management:**

During the beginning of this task, the original goal was to break up my code, into a variety of files, to allow for more efficient development and performance of the system. Unfortunately, during the creation of the program, too many errors where being produced due to this goal. While I am confident it can be achieved, with my current skill level and abilities, breaking my program down into multiple files would require more time than I had for the task.

**Impact on User Experience:**

Breaking the program down into multiple files would have a larger focus on the developers side of the program, allowing them to find and solve errors faster and more efficiently. However, this still would impact the users experience. It would mean their problems would be solved faster, and more effectively.

### Evaluate the system in terms of how well it meets the requirements and specifications.

**Functional Requirements**

Evaluation of the System Against Requirements and Specifications
My system effectively meets the functional and non-functional requirements outlined in its initial design, offering a responsive, accessible, and feature-complete gameplay experience. Each requirement is addressed through thoughtful design decisions, and the system performs reliably across its key mechanics.

**Functional Requirements:**

The system meets all data retrieval expectations. Players can view essential statistics such as health, stamina, mana, inventory, and gold, at any point via the main UI. This is achieved through consistent updates and clear terminal output, ensuring users have constant updates on statistics and events.

The user interface uses ASCII art and emojis to deliver an engaging experience. Elements like hearts (❤️), and custom coloured terminal outputs allow for quick visual recognition, while intuitive command inputs (e.g.1–X) ensure fluid interaction. Scene transitions are clean and formatted, aligning with expectations for clarity and immersion.

To meet my data display criteria, the system successfully communicates in-game events through descriptive narration and clear outcomes. Players are notified during encounters, and combat sequences include multiple turns and second-chance mechanics, enhancing decision-making without overwhelming the user.

**Non-Functional Requirements:**

Performance is consistently strong. As a turn-based text system, transitions between actions are near-instant, with room and combat scenes loading in under half a second. Furthermore, the inclusion of timed text output ("swipe-style") maintains user attention without overloading the player, balancing speed with readability.

The system demonstrates high reliability through using a variety of functions and processes, key systems such as stats, combat, and inventory are isolated into separate functions and classes. This avoids unintended side effects and allows each system to function predictably and independently.

Usability and accessibility are clearly prioritized. The interface uses high-contrast text, minimalistic design, and a simplified input model to accommodate users with varied needs. Command options are consistently labeled, and help prompts ensure that players can navigate without confusion.

**Functional Specifications:**

The system meets all outlined user requirements, including access to stats, real-time feedback on in-game actions, and the ability to interact meaningfully through movement, combat, trading, and magic. While the magic system is currently basic, it satisfies initial specifications and lays groundwork for future expansion.

Inputs and outputs are handled gracefully. Valid inputs trigger appropriate actions (movement, combat, etc.), while invalid ones prompt corrective feedback. This ensures users stay informed and engaged, even when errors occur.

All core systems—combat, movement, inventory, trading, and magic—are implemented and functional. These mechanics are interconnected and support overall progression through exploration, decision-making, and character growth. The system responds appropriately to each input, contributing to a seamless player experience.

User interaction is efficient and effective through consistent use of clear text prompts. Even more complex actions during the program are broken down into simple, understandable actions for the USer to make clear and informed decisions.

My program has strong input handling, with my extensive texting finding that no inputs where found to be invalid, or to be processed with incorrect data.

**Non-Functional Specifications:**

The program delivers strong performance, loading each new game state in an effecive and efficient manner. This is strongly due to my efficient a through use of functions and loops throughout the program, that reduce redundent code, and increase the efficiency of the program.

In terms of accessibility, the system meets its goals by using terminal input, high-contrast visuals, and straightforward commands. These choices make it approachable for a broad audience, including users with low vision or limited technical familiarity.

Lastly, reliability is achieved through validation, input constraints, and modular control of data flow. The program avoids critical errors and, when issues do occur, informs the player how to correct them, through the use of Meaningful Error Messages, best seen in the Casino program.

**Conclusion:**

Overall, the system cohesively fulfills its design intentions. It is reliable, accessible, and functionally complete, offering an engaging and responsive experience to players. All specified requirements are met, with particular strengths in modularity, clarity of interaction, and performance. Areas like the magic system are identified for future enhancement but already meet baseline expectations. The foundation is solid, scalable, and ready for further development.

### Evaluate your processes in terms of project management.

For this project, the Use of the Agile sprint method as opposed to the waterfall method provided a strong curveball in terms of time management. This was the first project I have done with this approach, and it has had a strong impact on the project's time management. The first key difference with the Agile methods time management, is that I found it difficult to estimate the length tasks would take. Such as implimenting a movement system, or adding a inventory. As I have experienced with my other tasks, my estimations for how long implimenting features would take was generally accurate, allowing me to stay on schedule in those tasks. However, in this task, I found time management siginificantly more difficult, with my estimations being extremely wrong, and tasks taking either significantly longer or shorter that I first would have expected. This also meant sticking to the Gantt chart was difficult. My progress does allign with the Gantt charts general direction, but towards the end, my progress does come up a little short, and their is a heavy load of work that was pushed towards the end of the task.

These reasons the resulted in my time management for the task to be quite poor, and being left with significant work to accomplish, very close to the deadline. I'm confident that as I progress with tasks similar to this, using the Agile method, my ability to time manage these projects will improve, but as of now, my skill in the Agile Method, and this task specifically has a lot to work on to get it to the same level of time management I have for my other workflows.

### Evaluate your project in relation to peer feedback.

**Barry:** Miles’s system clearly meets all of his planned criteria and specifications. Core features like movement, combat, inventory, and stat tracking are functional and reliable, and the use of ASCII art and emoji adds friendlyness to the terminal-based interface. However, the biggest weakness is the lack of content. While the foundation is strong, there isn’t much variety in the world, enemies, or interactions, which can make the gameplay feel repetitive after a while. The magic and mana system is also underused and could be expanded to add more depth and strategy. Overall, it’s a well-built system that would really benefit from more content to keep players engaged longer.

**Yyoung:** One of the first things I noticed about Miles’s game is how smooth it runs. There’s no lag between actions, and the text-based UI is clean and easy to follow. I really liked how emojis and ASCII were used to make everything clearer and more interesting, especially for things like stats and the map. The system also does a good job handling user inputs, even when you enter something wrong, it doesn’t crash and instead helps guide you back on track. But after playing for a bit, I found myself getting board of the content. The core mechanics like movement and combat are solid, but it felt like I was doing similar things over and over again. It would be cool to see more random events, characters with actual dialogue, or even decisions that change what happens next. The magic system was there but didn’t really have much of a role, which was a bit of a letdown since it could make combat more interesting. Still, the structure of the game was good, and with a bit more content and uniqueness to each run, it could definately be a fun and engaging game.

**Riley:** Miles's game is a polished and fun text adventure that is interactive experience with a good story and characters.  I really enjoyed the variety of things you can do in this world and the diffrent ways you can level up and upgrade your gear. I particularly enjoyed the UI which was very polished and made the game experience more enjoyable. While Miles's game is very detailed in his game world, there is a lack of variety and content as the player can only face the same type of enemy. The villages and map remains the same on all of the story lines. The polished UI outweighs the simple map and the fun nature of making your choices about what to do allow crativity to shine. Overall the fun and interactive world outwieghs the repetitve nature of the same game world and allows to use their creativity in this charming world. It's defeintely an amazing game that I would play in my own time!

One of Barry, Yyoung's, and Riley's key pieces of feedback was the lack of content in the game, and I completely agree with that observation. Even though my game has a good range of features and mechanics, such as movement, combat, inventory, and magic, I didn’t really use them to their full potential. Because of that, the game can feel a bit empty or repetitive after a while. There are systems in place, but not enough interesting things happening with them, so the player doesn’t always feel like they’re progressing or discovering new things. In future versions of this project, or even in new projects, I want to spend more time making sure that the features I add actually get used in meaningful ways. That would help the game feel more complete and enjoyable overall.

I was glad that both Barry and Yyoung mentioned the ASCII art in a positive way, as I too feel it contributes positively to the program. I also appricated Yyoungs comment of the imput handling, and it being about to handle a varity of inputs, right or wrong, and still continue. For future projects however, I would like to attempt at a more organised way of dealing with error handling - i.e Giving each error a Unique Code as seen in larger software packages, to make error messagers more meaningful, and solveable. I also think this will increase the productivity of me developing it, as I will have a more thorough process of finding where problems are occuring, and allow me to spend more time working on them.


### Justify your use of OOP class features
Throughout the development of my game, I made strong use of Object-Oriented Programming (OOP) principles to structure and manage the different parts of my system. Using classes allowed me to separate different types of data and behavior into logical groups, which made the code more organised, easier to read, and much easier to update or expand in the future. Each class I created had a clear purpose, and I used key OOP features like encapsulation, attributes, and methods to make the game systems work smoothly.

One of the main classes in my game was the Player class. This class held all of the player’s important data like health, stamina, mana, gold, inventory, and current location. By storing all this in one class, I could easily pass around the player as a single object between different parts of the program. It also made for much more efficient processing of saving data, with every Player Specific Variable being tied to the Player itself, making it easier to load and unload data forr ecah save. I also included methods inside the Player class that impacted the player specifically, such as the combat and saving system. This follows good OOP practice because it keeps both the data and the functions that affect that data in one place, making it easier to control and understand.

Another important class was the Enemy class. This class had attributes like name, type (Fire, Water, Nature), health, and attack damage. I also added an elemental type system, where enemies had strengths and weaknesses based on the weapon used against them. This made use of class inheritance and logic within the methods to calculate damage correctly based on enemy type. Having enemies as a class made it easier to generate different types of enemies and keep their logic consistent, especially when I needed to check their stats or run combat functions.

I also used a Weapon and Armour class to manage equipment. Weapons had attributes like base damage and elemental type, while armour had protection. These classes were used when calculating combat results, so the player’s equipped gear directly affected how much damage they dealt or took. Again, having gear in their own classes made it easy to switch items, store them in inventories. I could also expand these classes easily later on with special effects or unique traits, without changing how the rest of the system works, highlighting the key modularity for Object Oriented Programs.

To handle interactions with non-playable characters, I implemented a flexible Villager class structure, which played a crucial role in maintaining code modularity and scalability. The base Villager class contained shared attributes such as name, profession, and inventory, along with the Universal Method `Inventory_Trading()`. This structure allowed me to define general behaviors and properties common to all villagers in one place, reducing redundancy and improving code clarity. More importantly, it ensured that any enhancements to basic villager functionality, such as adding UI formatting to their dialogue, could be applied globally without needing to modify multiple parts of the codebase. This demonstrates strong use of encapsulation, as each villager's data and behavior are cleanly wrapped inside a single object, making debugging and future expansion significantly easier.

To introduce variety in the game world and support different types of interactions, I extended the base class through subclassing, creating specialized versions like Brewer, Swordsmith, and Armoursmith. Each subclass inherited all the shared functionality from Villager, but also introduced unique logic tailored to its role—for example, the Brewer sold consumables like potions, while the Swordsmith handled weapon sales. These subclasses could also contain custom inventories and context-specific dialogue or logic, all while maintaining compatibility with systems expecting a general Villager object. This use of inheritance and method specialization made the codebase more organized and flexible, enabling new types of NPCs to be added with minimal rework. It also aligns with OOP best practices by separating concerns: the parent class manages what’s shared, and the children manage what’s unique. Without this structure, introducing multiple types of NPCs would have required repeated code or long conditional blocks—slowing development and increasing the risk of errors.