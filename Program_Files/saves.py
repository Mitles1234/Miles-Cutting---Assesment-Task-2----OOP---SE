"""import variables
import json
import items
#import combat

User = None  # Global variable to hold the player instance

class Player():
    def __init__(self, Save):
        self.Player_Name = Save['Player_Name']

        self.Health = {'Health': Save['Health']['Health'], 'Max_Health': Save['Health']['Max_Health']}
        self.Stamina = {'Stamina': Save['Stamina']['Stamina'], 'Max_Stamina': Save['Stamina']['Max_Stamina']}
        self.Mana = {'Mana': Save['Mana']['Mana'], 'Max_Mana': Save['Mana']['Max_Mana']}

        self.WeaponSlot = Save['WeaponSlot']
        self.HelmetSlot = Save['HelmetSlot']
        self.ChestplateSlot = Save['ChestplateSlot']
        self.BootSlot = Save['BootSlot']

        self.OtherSlot1 = {'Item': Save['OtherSlot1']['Item'], 'Qty': Save['OtherSlot1']['Qty']}
        self.OtherSlot2 = {'Item': Save['OtherSlot2']['Item'], 'Qty': Save['OtherSlot2']['Qty']}
        self.OtherSlot3 = {'Item': Save['OtherSlot3']['Item'], 'Qty': Save['OtherSlot3']['Qty']}
        self.OtherSlot4 = {'Item': Save['OtherSlot4']['Item'], 'Qty': Save['OtherSlot4']['Qty']}
        
        self.Location = Save['Location']
        self.Gold = Save['Gold']

    def Save(self, Save):
        Player_Stats = {
            'Player_Name': self.Player_Name,
            'Health': self.Health,
            'Stamina': self.Stamina,
            'Mana': self.Mana,
            'WeaponSlot': self.WeaponSlot,
            'HelmetSlot': self.HelmetSlot,
            'ChestplateSlot': self.ChestplateSlot,
            'BootSlot': self.BootSlot,
            'OtherSlot1': self.OtherSlot1,
            'OtherSlot2': self.OtherSlot2,
            'OtherSlot3': self.OtherSlot3,
            'OtherSlot4': self.OtherSlot4,
            'Location': self.Location
        }

        with open(f'Save{Save}.json', 'w') as f:
            def make_serializable(obj):
                '''This function converts objects to a serializable format (Because json's cant handle items from other classes)'''
                if hasattr(obj, '__dict__'):
                    return obj.__dict__
                return obj
            json.dump(Player_Stats, f, default=make_serializable)

    def Attacking(self, Target):
        Target.Player_Attacked(self.WeaponSlot.damage)

    def Attacked(self, Damage, Type):
        self.Health['Health'] -= (Damage / ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3))

def load(Player_Data, SaveNum):
    global User
    if len(Player_Data) == 0:
        CreateCharacter(SaveNum)
    else:
        User = Player(Player_Data)

def leave():
    global User
    if variables.Load_File != 0:
        User.Save(variables.Load_File)
        quit()

    else:
        quit()

def CreateCharacter():
    global User
    print('Welcome New Adventurer!')
    while True:
        Name_Input = input("What's your Name Adventurer? ")

        if len(Name_Input) == 0:
            pass
        else:
            print(f'Welcome {Name_Input}, This is where your Journey Begins!')
            break

    Player_Data = {
        'Player_Name': Name_Input,

        'Health': {'Health': 100, 'Max_Health': 100},
        'Stamina': {'Stamina': 100, 'Max_Stamina': 100},
        'Mana': {'Mana': 100, 'Max_Mana': 100},

        'WeaponSlot': items.Stick,
        'HelmetSlot': items.None_Helmet,
        'ChestplateSlot': items.None_Chestplate,
        'BootSlot': items.None_Boot,
        
        'OtherSlot1': {'Item': items.None_Item, 'Qty': 0},
        'OtherSlot2': {'Item': items.None_Item, 'Qty': 0},
        'OtherSlot3': {'Item': items.None_Item, 'Qty': 0},
        'OtherSlot4': {'Item': items.None_Item, 'Qty': 0},

        'Location': 'Forest1',
        'Gold': 10
    }

    User = Player(Player_Data)

"""

import variables
import json
import items
import UI
import os

User = None  # Global variable to hold the player instance

class Player():
    def __init__(self, Save):
        self.Player_Name = Save['Player_Name']

        self.Health = {'Health': Save['Health']['Health'], 'Max_Health': Save['Health']['Max_Health']}
        self.Stamina = {'Stamina': Save['Stamina']['Stamina'], 'Max_Stamina': Save['Stamina']['Max_Stamina']}
        self.Mana = {'Mana': Save['Mana']['Mana'], 'Max_Mana': Save['Mana']['Max_Mana']}

        self.WeaponSlot = Save['WeaponSlot']
        self.HelmetSlot = Save['HelmetSlot']
        self.ChestplateSlot = Save['ChestplateSlot']
        self.BootSlot = Save['BootSlot']

        self.OtherSlot1 = {'Item': Save['OtherSlot1']['Item'], 'Qty': Save['OtherSlot1']['Qty']}
        self.OtherSlot2 = {'Item': Save['OtherSlot2']['Item'], 'Qty': Save['OtherSlot2']['Qty']}
        self.OtherSlot3 = {'Item': Save['OtherSlot3']['Item'], 'Qty': Save['OtherSlot3']['Qty']}
        self.OtherSlot4 = {'Item': Save['OtherSlot4']['Item'], 'Qty': Save['OtherSlot4']['Qty']}
        
        self.Location = Save['Location']
        self.Gold = Save['Gold']

    def Save(self, Save):
        Player_Stats = {
            'Player_Name': self.Player_Name,
            'Health': self.Health,
            'Stamina': self.Stamina,
            'Mana': self.Mana,
            'WeaponSlot': self.WeaponSlot,
            'HelmetSlot': self.HelmetSlot,
            'ChestplateSlot': self.ChestplateSlot,
            'BootSlot': self.BootSlot,
            'OtherSlot1': self.OtherSlot1,
            'OtherSlot2': self.OtherSlot2,
            'OtherSlot3': self.OtherSlot3,
            'OtherSlot4': self.OtherSlot4,
            'Location': self.Location
        }

        with open(f'Save{Save}.json', 'w') as f:
            def make_serializable(obj):
                '''This function converts objects to a serializable format (Because json's cant handle items from other classes)'''
                if hasattr(obj, '__dict__'):
                    return obj.__dict__
                return obj
            json.dump(Player_Stats, f, default=make_serializable)

    def Attacking(self, Target):
        Target.Player_Attacked()

    def Attacked(self, Damage, Type):
        self.Health['Health'] -= (Damage / ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3))

def load(Player_Data):
    global User
    if len(Player_Data) == 0:
        CreateCharacter()
    else:
        User = Player(Player_Data)


def leave():
    global User
    if variables.Load_File != 0:
        User.Save(variables.Load_File)
        quit()

    else:
        quit()

def CreateCharacter():
    global User
    print('Welcome New Adventurer!')
    while True:
        Name_Input = input("What's your Name Adventurer? ")

        if len(Name_Input) == 0:
            print("You must enter a name!")
        elif len(Name_Input) > 20:
            print("Your name is too long! Please keep it under 20 characters.")
        else:
            print(f'Welcome {Name_Input}, This is where your Journey Begins!')
            break

    Player_Data = {
        'Player_Name': Name_Input,

        'Health': {'Health': 100, 'Max_Health': 100},
        'Stamina': {'Stamina': 100, 'Max_Stamina': 100},
        'Mana': {'Mana': 100, 'Max_Mana': 100},

        'WeaponSlot': items.Stick,
        'HelmetSlot': items.None_Helmet,
        'ChestplateSlot': items.None_Chestplate,
        'BootSlot': items.None_Boot,
        
        'OtherSlot1': {'Item': items.Health_Potion_Medium, 'Qty': 1},
        'OtherSlot2': {'Item': items.None_Item, 'Qty': 0},
        'OtherSlot3': {'Item': items.None_Item, 'Qty': 0},
        'OtherSlot4': {'Item': items.None_Item, 'Qty': 0},

        'Location': 'Forest1',
        'Gold': 10
    }

    User = Player(Player_Data)

class Enemy():
    def __init__(self, name, health, damage, type, level):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.type = type
        self.level = level

    def Attacking(self, Target):
        Target.Attacked(self.damage, self.type)

    def Player_Attacked(self):
        self.health -= (User.WeaponSlot.damage * User.WeaponSlot.multiplyers[self.type])

    def Attacked(self, Damage, Type):
        if self.type == 'Fir' and Type == 'Wat': # Strong < Weak
            self.health -= (Damage * 1.5)

        elif self.type == 'Wat' and Type == 'Fir': # Strong > Weak
            self.health -= (Damage * 0.5)

        elif self.type == 'Nat' and Type == 'Fir': # Strong < Weak
            self.health -= (Damage * 1.5)

        elif self.type == 'Fir' and Type == 'Nat': # Strong > Weak
            self.health -= (Damage * 0.5)

        elif self.type == 'Wat' and Type == 'Nat': # Strong < Weak
            self.health -= (Damage * 1.5)
        
        elif self.type == 'Nat' and Type == 'Wat': # Strong > Weak
            self.health -= (Damage * 0.5)
        
        else:
            self.health -= Damage

Goblin = Enemy('Goblin', 10, 5, 'Fir', 1)
Orc = Enemy('Orc', 20, 10, 'Wat', 2)

def Combat(Enemy):

    if Enemy.type == 'Fir':
        Type = 'Fire'
    elif Enemy.type == 'Wat':   
        Type = 'Water'
    elif Enemy.type == 'Nat':
        Type = 'Nature'
    print(f"""You have Encountered a {Enemy.name}""")

    while True:
        #os.system('cls')
        print(f"""
+-----------------------------------------------+
|{' '*21}Enemy{' '*21}|
+-----------------------------------------------+
    {Enemy.name}: 
        Health:  ♥️  \033[31m{UI.StatBar(Enemy.health, Enemy.max_health)} ({Enemy.health}/{Enemy.max_health})
        Damage:  ⚔️  \033[34m{Enemy.damage}\033[0m
        Type:    ☯️  \033[33m{Type}\033[0m

    {User.Player_Name}:
        Health:  ♥️  \033[31m{UI.StatBar(User.Health['Health'], User.Health['Max_Health'])} ({User.Health['Health']}/{User.Health['Max_Health']})
        Damage:  ⚔️  \033[34m{User.WeaponSlot.damage}\033[0m
        ELemental Damage:        ☯️  \033[33m{User.WeaponSlot.multiplyers[Enemy.type]}\033[0m
        Elemental Protection:    ☯️  \033[33m{((User.HelmetSlot.multiplyers[Enemy.type])+(User.ChestplateSlot.multiplyers[Enemy.type])+(User.BootSlot.multiplyers[Enemy.type]))/3}\033[0m
    """)
        if Enemy.health <= 0:
            print(f"You have defeated the {Enemy.name}!")
            User.WeaponSlot.level += Enemy.level/2
            break
            
        elif User.Health['Health'] <= 0:
            print(f"You have been defeated by the {Enemy.name}!")
            break
        else:
            UI.Input_Selection({
                "Attack": lambda: User.Attacking(Enemy),
                "Use Item": lambda: UI.DisplayInventoryScreen()})
            
            Enemy.Attacking(User)


CreateCharacter()

Combat(Goblin)