#--- Imports ---
import os
import random
import time
import json
import math

#--- Classes ---
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

class Item():
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Weapons(Item):
    def __init__(self, name, level, type, damage, multiplyers=None):
        super().__init__(name, level)
        self.damage = damage
        
        if multiplyers is None:
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1}
        else:
            self.multiplyers = multiplyers

class Armour(Item):
    def __init__(self, name, level, type, protection, multiplyers=None):
        super().__init__(name, level)
        self.protection = protection
        self.type = type

        if multiplyers is None:
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1}
        else:
            self.multiplyers = multiplyers


    def set_Multiplyers(self, Multiplyers):
        self.multiplyers = Multiplyers
            
class Potion(Item):
    def __init__(self, name, level, effect, strength):
        super().__init__(name, level)
        self.effect = effect
        self.strength = strength

    def Use_Potion(self, Target):
        getattr(Target, self.effect)[self.effect] += self.strength
        if getattr(Target, self.effect)[self.effect] > getattr(Target, self.effect)[f'Max_{self.effect}']:
            getattr(Target, self.effect)[self.effect] = getattr(Target, self.effect)[f'Max_{self.effect}']

class Spells(Item):
    def __init__(self, name, level, type, mana_cost, damage):
        super().__init__(name, level)
        self.type = type
        self.mana_cost = mana_cost
        self.damage = damage

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

class Villager:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.items = {}

    def Inventory_Trading(self):
        count = 1
        print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
        for item in self.items.values():
            print(f"|{count:<3}| {item['Item'].name:<30}   |   Cost: {item['Cost']:4} 🪙    |   Qty: {item['Qty']:<10} |")
            print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
            count += 1

        while True:
            try:
                Puchase_Input = int(input('Enter the number of the item you want to purchase (0 to exit): '))

                if Puchase_Input == 0:
                    print("Exiting the trading menu.")
                    break
                elif 1 > Puchase_Input > count:
                    print('Not a Valid Number')
                elif 1 <= Puchase_Input < count:
                    selected_item = list(self.items.values())[Puchase_Input - 1]
                    if selected_item['Qty'] > 0:
                        print(f"You bought 1x {selected_item['Item'].name} for {selected_item['Cost']} 🪙.")
                        selected_item['Qty'] -= 1
                    else:
                        print("Sorry, this item is out of stock.")

            except:
                print("Invalid input. Please enter a number.")

class Brewer(Villager):
    def __init__(self, name):
        super().__init__(name, 'Brewer')
        self.items = {
            'Health Potion': {'Item': random.choice([Health_Potion_Small, Health_Potion_Medium, Health_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(1, 4)},
            'Mana Potion': {'Item': random.choice([Mana_Potion_Small, Mana_Potion_Medium, Mana_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(1, 4)},
            'Stamina Potion': {'Item': random.choice([Stamina_Potion_Small, Stamina_Potion_Medium, Stamina_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(1, 4)}
        }

class SwordSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'SwordSmith')
        self.items = {
            'Wooden Sword': {'Item': Wooden_Sword, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Sword': {'Item': Bronze_Sword, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Sword': {'Item': Iron_Sword, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Sword': {'Item': Platinum_Sword, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class AxeSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'AxeSmith')
        self.items = {
            'Wooden Axe': {'Item': Wooden_Axe, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Axe': {'Item': Bronze_Axe, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Axe': {'Item': Iron_Axe, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Axe': {'Item': Platinum_Axe, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class MaceSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'MaceSmith')
        self.items = {
            'Wooden Mace': {'Item': Wooden_Mace, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Mace': {'Item': Bronze_Mace, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Mace': {'Item': Iron_Mace, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Mace': {'Item': Platinum_Mace, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

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

class Farmer(Villager):
    def __init__(self, name):
        super().__init__(name, 'Farmer')
        self.items = {
            'Bread': {'Item': Bread, 'Cost': random.randint(1, 5), 'Qty': random.randint(1, 10)},
            'Carrot': {'Item': Carrot, 'Cost': random.randint(1, 5), 'Qty': random.randint(1, 10)},
            'Potato': {'Item': Potato, 'Cost': random.randint(1, 5), 'Qty': random.randint(1, 10)}
        }

class Wizard(Villager):
    def __init__(self, name):
        super().__init__(name, 'Wizard')
        self.items = {
            'Enchanting': Enchantment(),
            #'Fireball Spell': {'Item': Fireball_Spell, 'Cost': random.randint(10, 30), 'Qty': random.randint(1, 2)},
            #'Lightning Bolt Spell': {'Item': Lightning_Bolt_Spell, 'Cost': random.randint(15, 40), 'Qty': random.randint(1, 2)},
            #'Healing Spell': {'Item': Healing_Spell, 'Cost': random.randint(20, 50), 'Qty': random.randint(1, 2)}
        }

#--- Variables ---
User = None

Load_File = 0

#--- Has the Player been in Room ---
Enemy1 = False
Enemy2 = False
Enemy3 = False
Enemy4 = False
Village1 = False
Village2 = False
Village3 = False
Forest1 = False
Forest2 = False
Forest3 = False
Forest4 = False
Wizard1 = False
Wizard2 = False
Mountain = False
GoblinKing = False

#--- Items ---
Stick = Weapons('Stick', 1, 'Stick', 2)

# Swords
Wooden_Sword = Weapons('Wooden_Sword', 3, 'Sword', 4)
Bronze_Sword = Weapons('Bronze_Sword', 6, 'Sword', 5)
Iron_Sword = Weapons('Iron_Sword', 12, 'Sword', 6)
Platinum_Sword = Weapons('Platinum_Sword', 16, 'Sword', 8)

# Axes
Wooden_Axe = Weapons('Wooden_Axe', 3, 'Axe', 4)
Bronze_Axe = Weapons('Bronze_Axe', 6, 'Axe', 5)
Iron_Axe = Weapons('Iron_Axe', 12, 'Axe', 6)
Platinum_Axe = Weapons('Platinum_Axe', 16, 'Axe', 8)

# Maces
Wooden_Mace = Weapons('Wooden_Mace', 3, 'Mace', 4)
Bronze_Mace = Weapons('Bronze_Mace', 6, 'Mace', 5)
Iron_Mace = Weapons('Iron_Mace', 12, 'Mace', 6)
Platinum_Mace = Weapons('Platinum_Mace', 16, 'Mace', 8)

#--- Armour ---
# Helmet
None_Helmet = Armour('None', 0, 'Helmet', 0)

Leather_Helmet = Armour('Leather_Helmet', 1, 'Helmet', 1)
Bronze_Helmet = Armour('Bronze_Helmet', 3, 'Helmet', 2)
Iron_Helmet = Armour('Iron_Helmet', 6, 'Helmet', 3)
Platinum_Helmet = Armour('Platinum_Helmet', 10, 'Helmet', 4)

# ChestPlate
None_Chestplate = Armour('None', 0, 'ChestPlate', 0)

Leather_Chestplate = Armour('Leather_Chestplate', 1, 'ChestPlate', 1)
Bronze_Chestplate = Armour('Bronze_Chestplate', 3, 'ChestPlate', 2)
Iron_Chestplate = Armour('Iron_Chestplate', 6, 'ChestPlate', 3)
Platinum_Chestplate = Armour('Platinum_Chestplate', 10, 'ChestPlate', 4)

# Boot
None_Boot = Armour('None', 0, 'Boot', 0)

Leather_Boot = Armour('Leather_Boot', 1, 'Boot', 1)
Bronze_Boot = Armour('Bronze_Boot', 3, 'Boot', 2)
Iron_Boot = Armour('Iron_Boot', 6, 'Boot', 3)
Platinum_Boot = Armour('Platinum_Boot', 10, 'Boot', 4)

# Items
None_Item = Item('None', 0)

# Potions
Health_Potion_Small = Potion('Health_Potion_Small', 1, 'Health', 10)
Health_Potion_Medium = Potion('Health_Potion_Medium', 3, 'Health', 25)
Health_Potion_Large = Potion('Health_Potion_Large', 5, 'Health', 50)

Stamina_Potion_Small = Potion('Stamina_Potion_Small', 1, 'Stamina', 10)
Stamina_Potion_Medium = Potion('Stamina_Potion_Medium', 3, 'Stamina', 25)
Stamina_Potion_Large = Potion('Stamina_Potion_Large', 5, 'Stamina', 50)

Mana_Potion_Small = Potion('Mana_Potion_Small', 1, 'Mana', 10)
Mana_Potion_Medium = Potion('Mana_Potion_Medium', 3, 'Mana', 25)
Mana_Potion_Large = Potion('Mana_Potion_Large', 5, 'Mana', 50)

# Food
Bread = Item('Bread', 1) # Used to restore Stamina
Carrot = Item('Carrot', 1) # Used to restore Stamina
Potato = Item('Potato', 1) # Used to restore Stamina

#--- Spells ---
Fireball = Spells('Fireball', 1, 'Fir', 10, 5)
Lightning_Blast = Spells('Lightning_Blast', 1, 'Wat', 10, 5)
Water_Blast = Spells('Water_Blast', 1, 'Wat', 10, 5)
Vine_Grap = Spells('Vine_Grab', 1, 'Nat', 10, 5)
Unstable_Concoction = Spells('Unstable_Concoction', 1, 'Nat', 10, 5) # Doubles the Damage of your Next turn

#--- Functions ---

# Combat
def Combat(Enemy):

    if Enemy.type == 'Fir':
        Type = 'Fire'
    elif Enemy.type == 'Wat':   
        Type = 'Water'
    elif Enemy.type == 'Nat':
        Type = 'Nature'
    print(f"""You have Encountered a {Enemy.name}""")

    while True:
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
        ELemental Damage:        ☯️  \033[33m{User.WeaponSlot.multiplyers[Enemy.type]}\033[0m
        Elemental Protection:    ☯️  \033[33m{((User.HelmetSlot.multiplyers[Enemy.type])+(User.ChestplateSlot.multiplyers[Enemy.type])+(User.BootSlot.multiplyers[Enemy.type]))/3}\033[0m
    """)
        if Enemy.health <= 0:
            print()
            print(f"You have defeated the {Enemy.name}!")
            User.WeaponSlot.level += Enemy.level/2
            break
            
        elif User.Health['Health'] <= 0:
            print()
            print(f"You have been defeated by the {Enemy.name}!")
            break
        else:
            Input_Selection({
                "Attack": lambda: User.Attacking(Enemy),
                "Use Item": lambda: DisplayInventoryScreen()})
            
            Enemy.Attacking(User)

            print("\033[20A", end="")

# UI
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

    print(Story(Room))
    Input_Selection(MoveOptions(Room))

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

def DisplayStats():
    return f'''+───────────--==| Stats |==--───────────+
│                                       │
│   Health:  ♥️  \033[31m{StatBar(User.Health['Health'], User.Health['Max_Health'])} \033[0m {f'({User.Health['Health']}/{User.Health['Max_Health']})':<12}│
│   Stamina: 🔋 \033[32m{StatBar(User.Stamina['Stamina'], User.Stamina['Max_Stamina'])} \033[0m {f'({User.Stamina['Stamina']}/{User.Stamina['Max_Stamina']})':<12}│
│   Mana:    💠 \033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}│
│                                       │
+───────────────────────────────────────+'''

def DisplayInventory():
    return f'''+────────────────────────--==| Inventory |==--────────────────────────+
│   {'🪙  Gold':<12} -   {User.Gold:<48} |
│   {'Weapon':<12} -   {User.WeaponSlot.name:<15} {'Chestplate':<12} -   {User.ChestplateSlot.name:<15} │
│   {'Helmet':<12} -   {User.HelmetSlot.name:<15} {'Boots':<12} -   {User.BootSlot.name:<15} │
+─────────────────────────────────────────────────────────────────────+
│   {User.OtherSlot1['Item'].name:<18} -   {User.OtherSlot1['Qty']:<9} {User.OtherSlot2['Item'].name:<18} -   {User.OtherSlot2['Qty']:<9} │
│   {User.OtherSlot3['Item'].name:<18} -   {User.OtherSlot3['Qty']:<9} {User.OtherSlot4['Item'].name:<18} -   {User.OtherSlot4['Qty']:<9} │
+─────────────────────────────────────────────────────────────────────+ '''

def DisplayMapKey():
    return f'''+─────────────────────────--==| Map Key |==--─────────────────────────+
│   ██ - You              🔮 - Wizard Tower                           │
│   🏠 - Village          ☠️  - Enemy            👑 - Goblin King      │
│   🌲 - Forest           ⛰️  - Mountain                               │
+─────────────────────────────────────────────────────────────────────+'''

def DisplayInventoryScreen():
    print('''
    Which Item would you like to use?
    ''')
    
    Input_Selection({
        User.OtherSlot1['Item'].name: (lambda: User.OtherSlot1['Item'].Use_Potion(User), print("\033[10A", end="")) if User.OtherSlot1['Item'].name != 'None' else None,
        #User.OtherSlot2['Item'].name: (lambda: User.UseItem(User.OtherSlot2)) if User.OtherSlot2['Item'].name != 'None' else None,
        #User.OtherSlot3['Item'].name: (lambda: User.UseItem(User.OtherSlot3)) if User.OtherSlot3['Item'].name != 'None' else None,
        #User.OtherSlot4['Item'].name: (lambda: User.UseItem(User.OtherSlot4)) if User.OtherSlot4['Item'].name != 'None' else None,
        'Exit': lambda: ''
    })

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
         'Save 1': lambda: (load(Player_Data_1)),# setattr(variables, 'Load_File', 1)),
         'Save 2': lambda: (load(Player_Data_2)), #setattr(variables, 'Load_File', 2)),
         'Save 3': lambda: (load(Player_Data_3)), #setattr(variables, 'Load_File', 3)),
         'Save 4': lambda: (load(Player_Data_4)), #setattr(variables, 'Load_File', 4)),
         'Exit': lambda: leave()
    })

    PrintMainUI(User.Location)

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
            | 1 | Weapon Slot:     {User.WeaponSlot.name:<20} | {User.WeaponSlot.multiplyers['Wat']:<3.3f} | {User.WeaponSlot.multiplyers['Fir']:<3.3f} | {User.WeaponSlot.multiplyers['Nat']:<3.3f} |
            | 2 | Helmet Slot:     {User.HelmetSlot.name:<20} | {User.HelmetSlot.multiplyers['Wat']:<3.3f} | {User.HelmetSlot.multiplyers['Fir']:<3.3f} | {User.HelmetSlot.multiplyers['Nat']:<3.3f} |
            | 3 | Chestplate Slot: {User.ChestplateSlot.name:<20} | {User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
            | 4 | Boot Slot:       {User.BootSlot.name:<20} | {User.BootSlot.multiplyers['Wat']:<3.3f} | {User.BootSlot.multiplyers['Fir']:<3.3f} | {User.BootSlot.multiplyers['Nat']:<3.3f} |
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

# Player Functions
def load(Player_Data):
    global User
    if len(Player_Data) == 0:
        CreateCharacter()
    else:
        User = Player(Player_Data)

def leave():
    global User
    if Load_File != 0:
        User.Save(Load_File)
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

        'WeaponSlot': Stick,
        'HelmetSlot': None_Helmet,
        'ChestplateSlot': None_Chestplate,
        'BootSlot': None_Boot,
        
        'OtherSlot1': {'Item': Health_Potion_Medium, 'Qty': 1},
        'OtherSlot2': {'Item': None_Item, 'Qty': 0},
        'OtherSlot3': {'Item': None_Item, 'Qty': 0},
        'OtherSlot4': {'Item': None_Item, 'Qty': 0},

        'Location': 'Forest1',
        'Gold': 10
    }

    User = Player(Player_Data)

# Magic
def Enchantment(item, type=None):
    Level = item.level

    Multiplyer = (random.randint(0, Level+10)/10)

    print(Multiplyer)

    if type == None:
        return {'Wat': (1+((Multiplyer)/4)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1+((Multiplyer)/4))}
    else:
        if type == 'Fir':
            return {'Wat': (1-((Multiplyer)/4)), 'Fir': (1+(Multiplyer)), 'Nat': (1+((Multiplyer)/4))}
        
        elif type == 'Wat':
            return {'Wat': (1+(Multiplyer)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1-((Multiplyer)/4))}
        
        elif type == 'Nat':
            return {'Wat': (1+((Multiplyer)/4)), 'Fir': (1-((Multiplyer)/4)), 'Nat': (1+(Multiplyer))}

# Movement
def MoveOptions(Room):
    if Room == 'Enemy1':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "East (Dark Forest) (2)": lambda: PrintMainUI('Dark Forest'),
            "South (Village1) (4)": lambda: PrintMainUI('Village1'),
            "West (Forest 1) (2)": lambda: PrintMainUI('Forest1'),
            "North (Enemy 3) (8)": lambda: PrintMainUI('Enemy3'),
        }
    elif Room == 'Enemy2':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "West (Dark Forest) (5)": lambda: PrintMainUI('Dark Forest'),
            "East (Wizard 1) (3)": lambda: PrintMainUI('Wizard1'),
            "South (Forest 2) (6)": lambda: PrintMainUI('Forest2'),
        }
    elif Room == 'Enemy3':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "South East (Wizard Tower) (7)": lambda: PrintMainUI('Wizard1'),
            "South West (Enemy) (7)": lambda: PrintMainUI('Enemy1'),
            "West (Mountain) (20)": lambda: PrintMainUI('Mountain'),
        }
    elif Room == 'Enemy4':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "West (Galamdor City) (6)": lambda: PrintMainUI('Village2'),
            "East (Goblin King) (4)": lambda: PrintMainUI('GoblinKing'),
            "South (Another City) (8)": lambda: PrintMainUI('Village3'),
        }
    elif Room == 'Village1':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "North (Enemy) (8)": lambda: PrintMainUI('Enemy1'),
            "South (Forest) (7)": lambda: PrintMainUI('Forest2'),
            "East (Village) (5)": lambda: PrintMainUI('Village2'),
        }
    elif Room == 'Village2':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "North (Aldwin Village) (8)": lambda: PrintMainUI('Village1'),
            "West (Forest 3) (7)": lambda: PrintMainUI('Forest3'),
            "South (Forest 4) (10)": lambda: PrintMainUI('Forest4'),
            "East (Enemy 4) (6)": lambda: PrintMainUI('Enemy4'),
        }
    elif Room == 'Village3':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "South (Forest 4) (12)": lambda: PrintMainUI('Forest4'),
            "West (Forest 4) (12)": lambda: PrintMainUI('Forest4'),
        }
    elif Room == 'Forest1':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "East (Enemy) (2)": lambda: PrintMainUI('Enemy1'),
        }
    elif Room == 'Forest2':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "North (Forest 1) (4)": lambda: PrintMainUI('Forest1'),
            "East (Wizard 2) (7)": lambda: PrintMainUI('Wizard2'),
            "South (Forest 3) (5)": lambda: PrintMainUI('Forest3'),
            "West (Enemy 1) (5)": lambda: PrintMainUI('Enemy1'),
        }
    elif Room == 'Forest3':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "West (Village1) (9)": lambda: PrintMainUI('Village1'),
            "East (Galamdor City) (7)": lambda: PrintMainUI('Village2'),
            "South (Forest 4) (6)": lambda: PrintMainUI('Forest4'),
            "North (Forest 2) (5)": lambda: PrintMainUI('Forest2'),
        }
    elif Room == 'Forest4':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "North (Forest 3) (6)": lambda: PrintMainUI('Forest3'),
            "East (Another City) (12)": lambda: PrintMainUI('Village3'),
            "West (Galamdor City) (10)": lambda: PrintMainUI('Village2'),
        }
    elif Room == 'Wizard1':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "West (Enemy 2) (3)": lambda: PrintMainUI('Enemy2'),
            "South (Wizard 2) (8)": lambda: PrintMainUI('Wizard2'),
        }
    elif Room == 'Wizard2':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "West (Forest 2) (7)": lambda: PrintMainUI('Forest2'),
            "North (Wizard 1) (8)": lambda: PrintMainUI('Wizard1'),
        }
    elif Room == 'Mountain':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "East (Mountain) (20)": lambda: PrintMainUI('Mountain'),
        }
    elif Room == 'GoblinKing':
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
            "West (Enemy 4) (4)": lambda: PrintMainUI('Enemy4'),
        }
    else:
        return {
            "Inventory": lambda: DisplayInventoryScreen(),
        }

def InputHandling(Room):
    def ReplaceInput():
            print("\033[2A", end="")
            print('Error With Input')
            NextMove = ''
            InputHandling(Room)

    NextMove = input(f'What do You want to do? ')

    if NextMove == '0':
        DisplayInventoryScreen()

    elif Room == 'Forest1':
        if NextMove == '1':
            PrintMainUI('Enemy1')
        else:
            ReplaceInput()

    elif Room == 'Enemy1':
        if NextMove == '1':
            PrintMainUI('Enemy1')
            
        elif NextMove == '0':
            pass
        else:
            ReplaceInput()

def Map(Room):

    def TitleGenerator(Title):
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+'
    
    if Room == 'Enemy1':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────██      🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Enemy2':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ██──┴────🔮     │                       │
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
    
    elif Room == 'Enemy3':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────██          🌲─────┐                 │
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
    
    elif Room == 'Enemy4':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────██─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Village1':
        return f'''        {TitleGenerator('Aldwin Village')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       ██       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
     
    elif Room == 'Village2':
        return f'''        {TitleGenerator('Galamdor City')}
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
        │        │       │            ██────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Village3':
        return f'''        {TitleGenerator('Fay Town')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────██           │
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
    
    elif Room == 'Forest1':
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
    
    elif Room == 'Forest2':
        return f'''        {TitleGenerator('Forgoten Forest')}
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
        │        ██ ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Forest3':
        return f'''        {TitleGenerator('Deep Forest')}
        │                                                       │
        │           ┌──────☠️           ██─────┐                 │
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
    
    elif Room == 'Forest4':
        return f'''        {TitleGenerator('Ash Forest')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       ██             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Wizard1':
        return f'''        {TitleGenerator('High Tower')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────██     │                       │
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
    
    elif Room == 'Wizard2':
        return f'''        {TitleGenerator('Willow Ward')}
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
        │                      └────────────██               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Mountain':
        return f'''        {TitleGenerator('Mountain')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ██ ───┘       │           │     │                 │
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
    
    elif Room == 'GoblinKing':
        return f'''        {TitleGenerator('Goblin King')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────██  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
# Story
def Story(Room):
    if Room == 'Enemy1':
        if Enemy1 == False:
            input('Press Enter to Continue...')
            Combat(Goblin)
            return f'You defeated the enemy!'
        else:
            return f'''You See the remains of a battle fought here. The ground is scorched, and the air is heavy with the scent of burnt wood and blood.'''
    
    elif Room == 'Enemy2':
        if Enemy2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Enemy3':
        if Enemy3 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Enemy4':
        if Enemy4 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Village1':
        if Village1 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Village2':
        if Village2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Village3':
        if Village3 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Forest1':
        if Forest1 == False:
            return f'''Your Eyes flutter open...'''
        else:
            return f'''You return to the Dark Forest, where you first awoke. The trees are still as dark and foreboding as ever, but you feel a sense of familiarity here.'''
    
    elif Room == 'Forest2':
        if Forest2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Forest3':
        if Forest3 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Forest4':
        if Forest4 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Wizard1':
        if Wizard1 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Wizard2':
        if Wizard2 == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'Mountain':
        if Mountain == False:
            return f'''None'''
        else:
            return f'''None'''
    
    elif Room == 'GoblinKing':
        if GoblinKing == False:
            return f'''None'''
        else:
            return f'''None'''



Goblin = Enemy('Goblin', 10, 5, 'Fir', 1)
Orc = Enemy('Orc', 20, 10, 'Wat', 2)

TitleScreen()