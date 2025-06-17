#--- Imports ---
import os
import random
import time
import json
import math
from wcwidth import wcswidth



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

        self.Enemy1 = Save['Enemy1']
        self.Enemy2 = Save['Enemy2']
        self.Enemy3 = Save['Enemy3']
        self.Enemy4 = Save['Enemy4']
        self.Village1 = Save['Village1']
        self.Village2 = Save['Village2']
        self.Village3 = Save['Village3']
        self.Forest1 = Save['Forest1']
        self.Forest2 = Save['Forest2']
        self.Forest3 = Save['Forest3']
        self.Forest4 = Save['Forest4']
        self.SeenW1 = Save['SeenW1']
        self.SeenW2 = Save['SeenW2']
        self.Wizard1 = Save['Wizard1']
        self.Wizard2 = Save['Wizard2']
        self.Mountain = Save['Mountain']
        self.GoblinKing = Save['GoblinKing']
        self.RareFlower = Save['RareFlower']
        self.RareRune = Save['RareRune']

        self.Enemies = {'G': Save['Enemies']['G'], 'O': Save['Enemies']['O'], 'D': Save['Enemies']['D'], 'Og': Save['Enemies']['Og']}

        Load_Enemies(Save['Enemies']['G'], Save['Enemies']['O'], Save['Enemies']['D'], Save['Enemies']['Og'])

    def Save(self, Save):
        # Only save essential information for each item (name and level) for compatibility with Load_Items()

        Player_Stats = {
            'Player_Name': self.Player_Name,
            'Health': self.Health,
            'Stamina': self.Stamina,
            'Mana': self.Mana,
            'WeaponSlot': {'Name': self.WeaponSlot.name, 'Level': self.WeaponSlot.level, 'Multiplyers': self.WeaponSlot.multiplyers},
            'HelmetSlot': {'Name': self.HelmetSlot.name, 'Level': self.HelmetSlot.level, 'Multiplyers': self.HelmetSlot.multiplyers},
            'ChestplateSlot': {'Name': self.ChestplateSlot.name, 'Level': self.ChestplateSlot.level, 'Multiplyers': self.ChestplateSlot.multiplyers},
            'BootSlot': {'Name': self.BootSlot.name, 'Level': self.BootSlot.level, 'Multiplyers': self.BootSlot.multiplyers},
            'OtherSlot1': {'Item': self.OtherSlot1['Item'].name, 'Qty': self.OtherSlot1['Qty']},
            'OtherSlot2': {'Item': self.OtherSlot2['Item'].name, 'Qty': self.OtherSlot2['Qty']},
            'OtherSlot3': {'Item': self.OtherSlot3['Item'].name, 'Qty': self.OtherSlot3['Qty']},
            'OtherSlot4': {'Item': self.OtherSlot4['Item'].name, 'Qty': self.OtherSlot4['Qty']},
            'Location': self.Location,
            'Gold': self.Gold,

            'Enemy1': self.Enemy1,
            'Enemy2': self.Enemy2,
            'Enemy3': self.Enemy3,
            'Enemy4': self.Enemy4,

            'Village1': self.Village1,
            'Village2': self.Village2,
            'Village3': self.Village3,

            'Forest1': self.Forest1,
            'Forest2': self.Forest2,
            'Forest3': self.Forest3,
            'Forest4': self.Forest4,

            'SeenW1': self.SeenW1,
            'SeenW2': self.SeenW2,

            'Wizard1': self.Wizard1,
            'Wizard2': self.Wizard2,
            'Mountain': self.Mountain,
            'GoblinKing': self.GoblinKing,

            'RareFlower': self.RareFlower,
            'RareRune': self.RareRune,

            'Enemies': {'G': Goblin.health, 'O': Orc.health, 'D': Druid.health, 'Og': Ogre.health}
        }

        with open(f'Save{Save}.json', 'w') as f:
            json.dump(Player_Stats, f)

    def Attacking(self, Target):
        Target.Player_Attacked()

    def Attacked(self, Damage, Type):
        self.Health['Health'] -= round(Damage / ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3))

class Item():
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Weapons(Item):
    def __init__(self, name, level, type, damage, multiplyers=None):
        super().__init__(name, level)
        self.type = type
        self.damage = damage
        
        if multiplyers is None:
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1}
        else:
            self.multiplyers = multiplyers

    def setmultiplyers(self, Multiplyers):
        self.multiplyers = Multiplyers

class Armour(Item):
    def __init__(self, name, level, type, protection, multiplyers=None):
        super().__init__(name, level)
        self.protection = protection
        self.type = type

        if multiplyers is None:
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1}
        else:
            self.multiplyers = multiplyers

    def setmultiplyers(self, Multiplyers):
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
        # Remove potion from inventory after use
        for slot in [Target.OtherSlot1, Target.OtherSlot2, Target.OtherSlot3, Target.OtherSlot4]:
            if slot['Item'] is self and slot['Qty'] > 0:
                slot['Qty'] -= 1
                if slot['Qty'] == 0:
                    slot['Item'] = None_Item
                break
            
class Enemy():
    def __init__(self, name, health, max_health, damage, type, level):
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
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.items = {}

    def Inventory_Trading(self):
        os.system('cls')

        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     {self.profession:<38}|
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {User.Gold:<6} {'🪙':<31}|
    +---------------------------------------------------------+
    ''')
        count = 1
        print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
        for item in self.items.values():
            print(f"|{count:<3}| {item['Item'].name:<30}   |   Cost: {item['Cost']:<4} 🪙    |   Qty: {item['Qty']:<10} |")
            print(f'+---+{'-'*34}+{'-'*19}+{"-"*19}+')
            count += 1

        lines_printed = (count * 2) + 1  # Gold + header + each item (2 lines per item)
        while True:
            try:
                Puchase_Input = int(input('Enter the number of the item you want to purchase (0 to exit): '))
                if Puchase_Input == 0:
                    ClearLines(lines_printed + 1)  # +1 for the input prompt line
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

class Brewer(Villager):
    def __init__(self, name):
        super().__init__(name, 'Brewer')
        self.items = {
            'Health Potion': {'Item': random.choice([Health_Potion_Small, Health_Potion_Medium, Health_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(3, 12)},
            'Mana Potion': {'Item': random.choice([Mana_Potion_Small, Mana_Potion_Medium, Mana_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(3, 12)},
            'Stamina Potion': {'Item': random.choice([Stamina_Potion_Small, Stamina_Potion_Medium, Stamina_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(3, 12)}
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

class Wizard(Villager):
    def __init__(self, name):
        super().__init__(name, 'Wizard')
    
    def WizardStore(self, Room):
        global User
        os.system('cls')
        if Room == 'Wizard1':
            if User.SeenW1 == False:
                print('''
        Welcome to my Tower!
            
            I can help you enchant your gear, making it stronger against Enemies, but you need to help me first!
                    
            Their is a rare flower in the south forest, bring it to me, and I will help you enchant!
                    ''')
                User.SeenW1 = True
                input('     Enter to Continue...')
                PrintMainUI('Wizard1')
            elif User.SeenW1 == True and User.RareFlower == False:
                print("Have you Brought me my Flower Yet? It's in the South Forest")
                input('Enter to Continue...')
                PrintMainUI('Wizard1')

            elif User.RareFlower == True:
                print()
                print('Thanks for bringing me my flower, what can I help you enchant today?')

                def El():
                    pass
                
                
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
                options['Exit'] = lambda: gdPrintMainUI('Wizard1')
                Input_Selection(options)
                
                # Print the enchanted item and its new multipliers
                item = enchanted_item['item']
                if item is not None:
                    print(f"You enchanted: {item.name}")
                    print("New multipliers:")
                    for key, value in item.multiplyers.items():
                        print(f"  {key}: {value:.2f}")

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
                
                # Print the enchanted item and its new multipliers
                item = enchanted_item['item']
                if item is not None:
                    print(f"You enchanted: {item.name}")
                    print("New multipliers:")
                    for key, value in item.multiplyers.items():
                        print(f"  {key}: {value:.2f}")


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
        os.system('cls')

        print(f'''
    +------------------==| Villager Menu |==------------------+
    |                                                         |
    |   Name:           {self.name:<38}|
    |                                                         |
    |   Profession:     {self.profession:<38}|
    |                                                         |
    +---------------------------------------------------------+
    |   Player Gold:    {User.Gold:<6} {'🪙':<31}|
    +---------------------------------------------------------+

    You can Earn extra money for equipment!
''')
        print('Chop Wood!')
        for i in range(0, 5):
            print()
            print('CHOP')
            print()
            time.sleep(random.randint(10, 20) / 10)
        print('Good Job, Heres a piece of Gold!')
        User.Gold += 1
        time.sleep(2)

class Gambler(Villager):
    def __init__(self, name):
        super().__init__(name, 'Gambler')

    def Casino(self):
        CasinoNumber = random.randint(1,5)

        print("Welcome to the Casino")
        print()
        print("If you win you'll get 5 times what you put in, if you lose, we just keep what you bet")
        print()

        while True:
            try:
                Betting = int(input(f"How Much Gold would you Like to Bet? (0 to Not Bet) Current Balance: {User.Gold} "))
                if Betting > User.Gold or Betting < 0:
                    print("You don't have that Much Gold")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                Guess = int(input("Put your Bet on a Number 1-5 "))
                if 1 <= Guess <= 5:
                    break
                else:
                    print('Not an Option')
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        if Guess == CasinoNumber:
            User.Gold += 4*Betting

        else:
            print("It'll seem you've lost, maybe next time you'll think twice about going up against the house")
            User.Gold -= Betting

        print()
        print(f"The Number was: {CasinoNumber}")
        print()
        print(f"Current Balence: {User.Gold}")

        input('Enter to Continue...')

def Load_Items(Name, Level, Multipliers):
    # Weapons
    if Name == 'Stick':
        return Weapons('Stick', Level, 'Stick', 2, Multipliers)

    elif Name == 'Wooden_Sword':
        return Weapons('Wooden_Sword', Level, 'Sword', 4, Multipliers)
    elif Name == 'Bronze_Sword':
        return Weapons('Bronze_Sword', Level, 'Sword', 5, Multipliers)
    elif Name == 'Iron_Sword':
        return Weapons('Iron_Sword', Level, 'Sword', 6, Multipliers)
    elif Name == 'Platinum_Sword':
        return Weapons('Platinum_Sword', Level, 'Sword', 8, Multipliers)

    elif Name == 'Wooden_Axe':
        return Weapons('Wooden_Axe', Level, 'Axe', 4, Multipliers)
    elif Name == 'Bronze_Axe':
        return Weapons('Bronze_Axe', Level, 'Axe', 5, Multipliers)
    elif Name == 'Iron_Axe':
        return Weapons('Iron_Axe', Level, 'Axe', 6, Multipliers)
    elif Name == 'Platinum_Axe':
        return Weapons('Platinum_Axe', Level, 'Axe', 8, Multipliers)

    elif Name == 'Wooden_Mace':
        return Weapons('Wooden_Mace', Level, 'Mace', 4, Multipliers)
    elif Name == 'Bronze_Mace':
        return Weapons('Bronze_Mace', Level, 'Mace', 5, Multipliers)
    elif Name == 'Iron_Mace':
        return Weapons('Iron_Mace', Level, 'Mace', 6, Multipliers)
    elif Name == 'Platinum_Mace':
        return Weapons('Platinum_Mace', Level, 'Mace', 8, Multipliers)

    # Armour
    elif Name == 'None_Helmet':
        return Armour('None_Helmet', 0, 'Helmet', 0, Multipliers)
    elif Name == 'Leather_Helmet':
        return Armour('Leather_Helmet', Level, 'Helmet', 1, Multipliers)
    elif Name == 'Bronze_Helmet':
        return Armour('Bronze_Helmet', Level, 'Helmet', 2, Multipliers)
    elif Name == 'Iron_Helmet':
        return Armour('Iron_Helmet', Level, 'Helmet', 3, Multipliers)
    elif Name == 'Platinum_Helmet':
        return Armour('Platinum_Helmet', Level, 'Helmet', 4, Multipliers)

    elif Name == 'None_Chestplate':
        return Armour('None_Chestplate', 0, 'ChestPlate', 0, Multipliers)
    elif Name == 'Leather_Chestplate':
        return Armour('Leather_Chestplate', Level, 'ChestPlate', 1, Multipliers)
    elif Name == 'Bronze_Chestplate':
        return Armour('Bronze_Chestplate', Level, 'ChestPlate', 2, Multipliers)
    elif Name == 'Iron_Chestplate':
        return Armour('Iron_Chestplate', Level, 'ChestPlate', 3, Multipliers)
    elif Name == 'Platinum_Chestplate':
        return Armour('Platinum_Chestplate', Level, 'ChestPlate', 4, Multipliers)

    elif Name == 'None_Boot':
        return Armour('None_Boot', 0, 'Boot', 0, Multipliers)
    elif Name == 'Leather_Boot':
        return Armour('Leather_Boot', Level, 'Boot', 1, Multipliers)
    elif Name == 'Bronze_Boot':
        return Armour('Bronze_Boot', Level, 'Boot', 2, Multipliers)
    elif Name == 'Iron_Boot':
        return Armour('Iron_Boot', Level, 'Boot', 3, Multipliers)
    elif Name == 'Platinum_Boot':
        return Armour('Platinum_Boot', Level, 'Boot', 4, Multipliers)

    # General Item
    elif Name == 'None':
        return Item('None', 0)

    # Potions
    elif Name == 'Health_Potion_Small':
        return Potion('Health_Potion_Small', Level, 'Health', 10)
    elif Name == 'Health_Potion_Medium':
        return Potion('Health_Potion_Medium', Level, 'Health', 25)
    elif Name == 'Health_Potion_Large':
        return Potion('Health_Potion_Large', Level, 'Health', 50)

    elif Name == 'Stamina_Potion_Small':
        return Potion('Stamina_Potion_Small', Level, 'Stamina', 10)
    elif Name == 'Stamina_Potion_Medium':
        return Potion('Stamina_Potion_Medium', Level, 'Stamina', 25)
    elif Name == 'Stamina_Potion_Large':
        return Potion('Stamina_Potion_Large', Level, 'Stamina', 50)

    elif Name == 'Mana_Potion_Small':
        return Potion('Mana_Potion_Small', Level, 'Mana', 10)
    elif Name == 'Mana_Potion_Medium':
        return Potion('Mana_Potion_Medium', Level, 'Mana', 25)
    elif Name == 'Mana_Potion_Large':
        return Potion('Mana_Potion_Large', Level, 'Mana', 50)

    else:
        raise ValueError(f"Unknown item name: {Name}")

def Load_Enemies(G, O, D, Og):
    global Goblin, Orc, Druid, Ogre
    # Enemies
    Goblin = Enemy('Goblin', G, 10, 5, 'Fir', 1)
    Orc = Enemy('Orc', O, 20, 7, 'Wat', 8)
    Druid = Enemy('Druid', D, 20, 12, 'Nat', 16)
    Ogre = Enemy('Ogre', Og, 50, 10, 'Fir', 20)

#--- Variables ---
User = None

Load_File = 0

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
None_Helmet = Armour('None_Helmet', 0, 'Helmet', 0)

Leather_Helmet = Armour('Leather_Helmet', 1, 'Helmet', 1)
Bronze_Helmet = Armour('Bronze_Helmet', 3, 'Helmet', 2)
Iron_Helmet = Armour('Iron_Helmet', 6, 'Helmet', 3)
Platinum_Helmet = Armour('Platinum_Helmet', 10, 'Helmet', 4)

# ChestPlate
None_Chestplate = Armour('None_Chestplate', 0, 'ChestPlate', 0)

Leather_Chestplate = Armour('Leather_Chestplate', 1, 'ChestPlate', 1)
Bronze_Chestplate = Armour('Bronze_Chestplate', 3, 'ChestPlate', 2)
Iron_Chestplate = Armour('Iron_Chestplate', 6, 'ChestPlate', 3)
Platinum_Chestplate = Armour('Platinum_Chestplate', 10, 'ChestPlate', 4)

# Boot
None_Boot = Armour('None_Boot', 0, 'Boot', 0)

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

#--- Functions ---

# Combat
def Combat(Enemy, Room):
    global Exited

    if Enemy.type == 'Fir':
        Type = 'Fire'
    elif Enemy.type == 'Wat':   
        Type = 'Water'
    elif Enemy.type == 'Nat':
        Type = 'Nature'
    print(f"""You have Encountered a {Enemy.name}""")

    while True:
        Exited = False
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
        """)
        if Enemy.health <= 0:
            print()
            ClearLines(18)
            print(f"You have defeated the {Enemy.name}!")
            User.WeaponSlot.level += Enemy.level/2
            globals()[Room] = True
            break
            
        elif User.Health['Health'] <= 0:
            print()
            print(f"You have been defeated by the {Enemy.name}!")
            quit()
        else:
            Input_Selection({
                "Attack": lambda: (User.Attacking(Enemy)),
                "Use Item": lambda: (DisplayInventoryScreen())
                })
            
            if Exited == False:
                Enemy.Attacking(User)
            else:
                pass
        ClearLines(20)

# UI
def PrintMainUI(Room):
    Exited = False
    os.system('cls')
    
    User.Location = Room
    # Set the current room flag to True for the user
    

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

        map_width = wcswidth(map_line)
        padding = max(0, 60 - map_width)
        print(map_line + ' ' * padding + side_line)
    
    print()

    print(Story(Room))
    
    print()
    while True:
        if Exited == False:
            setattr(User, Room, True)
            Input_Selection(MoveOptions(Room))
            ClearLines(len(MoveOptions(Room)) + 3)
            
        else:
            break

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
│   Mana:    {f'💠 \033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}' if MountainIssue == True else f'💠\033[34m{StatBar(User.Mana['Mana'], User.Mana['Max_Mana'])} \033[0m {f'({User.Mana['Mana']}/{User.Mana['Max_Mana']})':<12}'}│
│                                       │
+───────────────────────────────────────+'''

def DisplayInventory():
    return f'''+──────────────────────────────────--==| Inventory |==--──────────────────────────────────+
│   {'🪙  Gold':<12} -   {User.Gold:<68} │
│   {'Weapon':<12} -   {User.WeaponSlot.name:<25} {'Chestplate':<12} -   {User.ChestplateSlot.name:<25} │
│   {'Helmet':<12} -   {User.HelmetSlot.name:<25} {'Boots':<12} -   {User.BootSlot.name:<25} │
+{'─'*89}+ 
│   {User.OtherSlot1['Item'].name:<28} -   {User.OtherSlot1['Qty']:<9} {User.OtherSlot2['Item'].name:<28} -   {User.OtherSlot2['Qty']:<9} │
│   {User.OtherSlot3['Item'].name:<28} -   {User.OtherSlot3['Qty']:<9} {User.OtherSlot4['Item'].name:<28} -   {User.OtherSlot4['Qty']:<9} │
+{'─'*89}+'''

def DisplayMapKey():
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
        
    x = 6 + len(options)
    ClearLines(x)

def TitleScreen():
    def OverWrite():
        print('Which save do you you want to overwrite?')
        print()
        options = {}
        if Player_Data_1:
            options['Save 1'] = lambda: (load({}, 1))
        if Player_Data_2:
            options['Save 2'] = lambda: (load({}, 2))
        if Player_Data_3:
            options['Save 3'] = lambda: (load({}, 3))
        if Player_Data_4:
            options['Save 4'] = lambda: (load({}, 4))
        options['Exit'] = lambda: TitleScreen()
        Input_Selection(options)
                
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
    |Name: {Player_Data_1.get('Player_Name', 'None'):<20}|    |Name: {Player_Data_2.get('Player_Name', 'None'):<20}|    |Name: {Player_Data_3.get('Player_Name', 'None'):<20}|    |Name: {Player_Data_4.get('Player_Name', 'None'):<20}|
    |Room: {Player_Data_1.get('Location', 'None'):<20}|    |Room: {Player_Data_2.get('Location', 'None'):<20}|    |Room: {Player_Data_3.get('Location', 'None'):<20}|    |Room: {Player_Data_4.get('Location', 'None'):<20}|
    +--------------------------+    +--------------------------+    +--------------------------+    +--------------------------+


    ''')
    Input_Selection({
         'Save 1': lambda: (load(Player_Data_1, 1)),
         'Save 2': lambda: (load(Player_Data_2, 2)),
         'Save 3': lambda: (load(Player_Data_3, 3)),
         'Save 4': lambda: (load(Player_Data_4, 4)),
         'OverWrite Save': lambda: OverWrite(),
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
        ClearLines(2)  # Move cursor up 2 lines
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
def load(Player_Data, Save):
    global User, Load_File

    Load_File = Save

    # Manually reconstruct the data for Player()
    


    if len(Player_Data) == 0:
        CreateCharacter()
    else:
        Data = {
        'Player_Name': Player_Data['Player_Name'],
        'Health': Player_Data['Health'],
        'Stamina': Player_Data['Stamina'],
        'Mana': Player_Data['Mana'],
        'Location': Player_Data['Location'],
        'Gold': Player_Data['Gold'],

        'WeaponSlot': Load_Items(Player_Data['WeaponSlot']['Name'], Player_Data['WeaponSlot']['Level'], Player_Data['WeaponSlot']['Multiplyers']),
        'HelmetSlot': Load_Items(Player_Data['HelmetSlot']['Name'], Player_Data['HelmetSlot']['Level'], Player_Data['HelmetSlot']['Multiplyers']),
        'ChestplateSlot': Load_Items(Player_Data['ChestplateSlot']['Name'], Player_Data['ChestplateSlot']['Level'], Player_Data['ChestplateSlot']['Multiplyers']),
        'BootSlot': Load_Items(Player_Data['BootSlot']['Name'], Player_Data['BootSlot']['Level'], Player_Data['BootSlot']['Multiplyers']),

        'OtherSlot1': {'Item': Load_Items(Player_Data['OtherSlot1']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot1']['Qty']},
        'OtherSlot2': {'Item': Load_Items(Player_Data['OtherSlot2']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot2']['Qty']},
        'OtherSlot3': {'Item': Load_Items(Player_Data['OtherSlot3']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot3']['Qty']},
        'OtherSlot4': {'Item': Load_Items(Player_Data['OtherSlot4']['Item'], 1, 1), 'Qty': Player_Data['OtherSlot4']['Qty']},

        # === Game State Flags ===
        'Enemy1': Player_Data['Enemy1'],
        'Enemy2': Player_Data['Enemy2'],
        'Enemy3': Player_Data['Enemy3'],
        'Enemy4': Player_Data['Enemy4'],

        'Village1': Player_Data['Village1'],
        'Village2': Player_Data['Village2'],
        'Village3': Player_Data['Village3'],

        'Forest1': Player_Data['Forest1'],
        'Forest2': Player_Data['Forest2'],
        'Forest3': Player_Data['Forest3'],
        'Forest4': Player_Data['Forest4'],

        'SeenW1': Player_Data['SeenW1'],
        'SeenW2': Player_Data['SeenW2'],

        'Wizard1': Player_Data['Wizard1'],
        'Wizard2': Player_Data['Wizard2'],
        'Mountain': Player_Data['Mountain'],
        'GoblinKing': Player_Data['GoblinKing'],

        'RareFlower': Player_Data['RareFlower'],
        'RareRune': Player_Data['RareRune'],

        'Enemies': Player_Data['Enemies']
        }

        

        User = Player(Data)

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
        'Gold': 100000,

        'Enemy1': False,
        'Enemy2': False,
        'Enemy3': False,
        'Enemy4': False,

        'Village1': False,
        'Village2': False,
        'Village3': False,

        'Forest1': False,
        'Forest2': False,
        'Forest3': False,
        'Forest4': False,


        'SeenW1': False,
        'SeenW2': False,
        
        'Wizard1': False,
        'Wizard2': False,
        'Mountain': False,
        'GoblinKing': False,

        'RareFlower': False,
        'RareRune': False,

        'Enemies': {'G': 10, 'O': 20, 'D': 20, 'Og': 50}
    }

    User = Player(Player_Data)

# Magic
def Enchantment(item, type=None):
    os.system('cls')
    
    
    Level = item.level

    Multiplyer = (random.randint(0, round(Level)+10)/10)

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
    global User

    def RemoveStamina(Stamina):
        User.Stamina['Stamina'] -= Stamina

    Leave = {
        "Inventory": lambda: DisplayInventoryScreen(),
        "Exit": lambda: Exiting()
    }

    def RoomOptions():
        if Room == 'Enemy1':
            return {
                "North East (Enemy2) (6)": lambda: (RemoveStamina(6), PrintMainUI('Enemy2')),
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),
                "East (Vilage1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),
                "West (Forest1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Forest1')),
            }
        elif Room == 'Enemy2':
            return {
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),
                "South East (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),
                "South West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),
                "East (Wizard1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Wizard1')),
            }
        elif Room == 'Enemy3':
            return {
                "South East (Wizard1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Wizard1')),
                "South West (Enemy2) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy2')),
                "West (Mountain) (20)": lambda: (RemoveStamina(20), PrintMainUI('Mountain')),
            }
        elif Room == 'Enemy4':
            return {
                "North West (Forest4) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),
                "East (GoblinKing) (4)": lambda: (RemoveStamina(4), PrintMainUI('GoblinKing')),
                "West (Village2) (8)": lambda: (RemoveStamina(8), PrintMainUI('Village2')),
            }
        elif Room == 'Village1':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village1')),
                "South (Forest2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest2')),
                "East (Village2) (5)": lambda: (RemoveStamina(5), PrintMainUI('Village2')),
                "West (Enemy1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),
            }
        elif Room == 'Village2':
            return {
                "Enter Village": lambda: (ClearLines(8), EnterVillage('Village2')),
                "South East (Wizard2) (7)": lambda: (RemoveStamina(7), PrintMainUI('Wizard2')),
                "East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),
                "West (Village1) (2)": lambda: (RemoveStamina(2), PrintMainUI('Village1')),
            }
        elif Room == 'Village3':
            return {
                "Enter Village": lambda: (ClearLines(5), EnterVillage('Village1')),
                "North West (Forest4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Forest4')),
            }
        elif Room == 'Forest1':
            return {
                "East (Enemy) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy1')),
            }
        elif Room == 'Forest2':
            if User.SeenW1:
                User.RareFlower = True
                print('''
        You found a Rare Flower!
                ''')
            return {
                "North East (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),
                "North West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),
            }
        elif Room == 'Forest3':
            return {
                "North East (Forest4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Forest4')),
                "North West (Enemy2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy2')),
                "East (Enemy4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),
                "West (Enemy1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy1')),
            }
        elif Room == 'Forest4':
            return {
                "South East (Enemy4) (5)": lambda: (RemoveStamina(5), PrintMainUI('Enemy4')),
                "South West (Forest3) (6)": lambda: (RemoveStamina(6), PrintMainUI('Forest3')),
                "East (Village3) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village3')),
            }
        elif Room == 'Wizard1':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard1'),
                "North (Enemy3) (3)": lambda: (RemoveStamina(3), PrintMainUI('Enemy3')),
                "West (Enemy2) (2)": lambda: (RemoveStamina(2), PrintMainUI('Enemy2')),
            }
        elif Room == 'Wizard2':
            return {
                "Enter Wizard Tower": lambda: EnterWizardTower('Wizard2'),
                "North East (Village2) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village2')),
                "North West (Village1) (4)": lambda: (RemoveStamina(4), PrintMainUI('Village1')),
            }
        elif Room == 'Mountain':
            if User.SeenW2:
                User.RareRune = True
                print('''
        You found a Rare Rune!
                ''')
            return {
                "East (Enemy3) (10)": lambda: (RemoveStamina(10), PrintMainUI('Enemy3')),
            }
        elif Room == 'GoblinKing':
            return {
                "West (Enemy 4) (4)": lambda: (RemoveStamina(4), PrintMainUI('Enemy4')),
            }
        else:
            return {}

    options = {}
    options.update(Leave)
    options.update(RoomOptions())
    return options

def Story(Room):
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
    if Room == 'Mountain':
        MountainIssue = True
    else:
        MountainIssue = False
    # Helper to pad all map symbols to 2 spaces for alignment
    def pad(symbol, width=2):
        real_width = wcswidth(symbol)
        return symbol + ' ' * (width - real_width)

    Enemy1 = pad('💀') if Room != 'Enemy1' else pad('██')
    Enemy2 = pad('💀') if Room != 'Enemy2' else pad('██')
    Enemy3 = pad('💀') if Room != 'Enemy3' else pad('██')
    Enemy4 = pad('💀') if Room != 'Enemy4' else pad('██')
    Village1 = pad('🏠') if Room != 'Village1' else pad('██')
    Village2 = pad('🏠') if Room != 'Village2' else pad('██')
    Village3 = pad('🏠') if Room != 'Village3' else pad('██')
    Forest1 = pad('🌲') if Room != 'Forest1' else pad('██')
    Forest2 = pad('🌲') if Room != 'Forest2' else pad('██')
    Forest3 = pad('🌲') if Room != 'Forest3' else pad('██')
    Forest4 = pad('🌲') if Room != 'Forest4' else pad('██')
    Wizard1 = pad('🔮') if Room != 'Wizard1' else pad('██')
    Wizard2 = pad('🔮') if Room != 'Wizard2' else pad('██')
    Mountain = pad('🏔️ ') if Room != 'Mountain' else pad('██')
    GoblinKing = pad('👑') if Room != 'GoblinKing' else pad('██')

    def TitleGenerator(Title):
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+'

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
    Mort = ArmourSmith('Mort')
    Alex = AxeSmith('Alex')
    Melvin = Brewer('Melvin')
    Zuba = LumberJack('Zuba')

    Bill = Gambler('Bill')

    Julian = ArmourSmith('Julian')
    Gloria = SwordSmith('Gloria')
    Marty = AxeSmith('Marty')
    Kowalski = Brewer('Kowalski')
    Moto = LumberJack('Moto')

    Dole = Gambler('Dole')

    Maurice = ArmourSmith('Maurice')
    Rico = SwordSmith('Rico')
    Skipper = Brewer('Skipper')
    Milton = LumberJack('Milton')

    Doh = Gambler('Doh')


    while True:
        os.system('cls')
        print('Select a Merchant to Interact With!')
        print()

        Exiting = False
        def Break():
            nonlocal Exiting
            os.system('cls')
            print()
            print('Select a Merchant to Interact With!')
            print()
            Exiting = True

        if Village == 'Village1':
            Input_Selection({
                'Mort - Armoursmith': lambda: Mort.Inventory_Trading(),
                'Alex - Axesmith': lambda: Alex.Inventory_Trading(),
                'Melvin - Brewer': lambda: Melvin.Inventory_Trading(),
                'Zuba - LumberJack': lambda: Zuba.ChopWood(),
                'Bill - Casino Owner': lambda: Bill.Casino(),
                'Exit': lambda: Break()
            })

            if Exiting == True:
                break
            
        elif Village == 'Village2':
            Input_Selection({
                'Julian - Armoursmith': lambda: Julian.Inventory_Trading(),
                'Gloria - Swordsmith': lambda: Gloria.Inventory_Trading(),
                'Marty - Axesmith': lambda: Marty.Inventory_Trading(),
                'Kowalski - Brewer': lambda: Kowalski.Inventory_Trading(),
                'Moto - LumberJack': lambda: Moto.ChopWood(),
                'Dole - Casino Owner': lambda: Dole.Casino(),
                'Exit': lambda: Break()
            })

            if Exiting == True:
                break

        elif Village == 'Village3':
            Input_Selection({
                'Maurice - Armoursmith': lambda: Maurice.Inventory_Trading(),
                'Rico - Swordsmith': lambda: Rico.Inventory_Trading(),
                'Skipper - Brewer': lambda: Skipper.Inventory_Trading(),
                'Milton - LumberJack': lambda: Milton.ChopWood(),
                'Doh - Casino Owner': lambda: Doh.Casino(),
                'Exit': lambda: Break()
            })

            if Exiting == True:
                break

    PrintMainUI(Village)

def EnterWizardTower(wizard_room):
    Jake = Wizard('Jake')

    Jake.WizardStore(wizard_room)

def ClearLines(n):
    for _ in range(n):
        print("\033[1A\033[2K", end="")

def Exiting():
    global Load_File
    User.Save(Load_File)
    TitleScreen()

def Died(DeathCause):
    os.system('cls')
    print(f'''
 ▄· ▄▌      ▄• ▄▌    ·▄▄▄▄  ▪  ▄▄▄ .·▄▄▄▄  
▐█▪██▌▪     █▪██▌    ██▪ ██ ██ ▀▄.▀·██▪ ██ 
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▐█· ▐█▌▐█·▐▀▀▪▄▐█· ▐█▌
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ██. ██ ▐█▌▐█▄▄▌██. ██ 
  ▀ •  ▀█▄▀▪ ▀▀▀     ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀• 

You Died to {DeathCause}
''')
    input('Enter to Delete Save...')

    with open(f'Save{Load_File}.json', 'w') as file:
        json.dump({}, file) # Dumps an empty dictionary to the file

    TitleScreen()


TitleScreen()


