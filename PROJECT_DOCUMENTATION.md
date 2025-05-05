# 11SE Task 2 - OOP - Text Adventurer
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
    - To make the program run effectively, I will use 