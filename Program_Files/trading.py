import items
import random
import magic

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
            'Health Potion': {'Item': random.choice([items.Health_Potion_Small, items.Health_Potion_Medium, items.Health_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(1, 4)},
            'Mana Potion': {'Item': random.choice([items.Mana_Potion_Small, items.Mana_Potion_Medium, items.Mana_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(1, 4)},
            'Stamina Potion': {'Item': random.choice([items.Stamina_Potion_Small, items.Stamina_Potion_Medium, items.Stamina_Potion_Large]), 'Cost': random.randint(3, 10), 'Qty': random.randint(1, 4)}
        }

class SwordSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'SwordSmith')
        self.items = {
            'Wooden Sword': {'Item': items.Wooden_Sword, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Sword': {'Item': items.Bronze_Sword, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Sword': {'Item': items.Iron_Sword, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Sword': {'Item': items.Platinum_Sword, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class AxeSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'AxeSmith')
        self.items = {
            'Wooden Axe': {'Item': items.Wooden_Axe, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Axe': {'Item': items.Bronze_Axe, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Axe': {'Item': items.Iron_Axe, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Axe': {'Item': items.Platinum_Axe, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class MaceSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'MaceSmith')
        self.items = {
            'Wooden Mace': {'Item': items.Wooden_Mace, 'Cost': random.randint(5, 15), 'Qty': random.randint(1, 3)},
            'Bronze Mace': {'Item': items.Bronze_Mace, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 3)},
            'Iron Mace': {'Item': items.Iron_Mace, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Mace': {'Item': items.Platinum_Mace, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class ArmourSmith(Villager):
    def __init__(self, name):
        super().__init__(name, 'ArmourSmith')
        self.items = {
            'Leather Helmet': {'Item': items.Leather_Helmet, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Helmet': {'Item': items.Bronze_Helmet, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Helmet': {'Item': items.Iron_Helmet, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Helmet': {'Item': items.Platinum_Helmet, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Chestplate': {'Item': items.Leather_Chestplate, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Chestplate': {'Item': items.Bronze_Chestplate, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Chestplate': {'Item': items.Iron_Chestplate, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Chestplate': {'Item': items.Platinum_Chestplate, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)},
            'Leather Boot': {'Item': items.Leather_Boot, 'Cost': random.randint(5, 10), 'Qty': random.randint(1, 2)},
            'Bronze Boot': {'Item': items.Bronze_Boot, 'Cost': random.randint(10, 20), 'Qty': random.randint(1, 2)},
            'Iron Boot': {'Item': items.Iron_Boot, 'Cost': random.randint(15, 30), 'Qty': random.randint(1, 2)},
            'Platinum Boot': {'Item': items.Platinum_Boot, 'Cost': random.randint(20, 40), 'Qty': random.randint(1, 2)}
        }

class Farmer(Villager):
    def __init__(self, name):
        super().__init__(name, 'Farmer')
        self.items = {
            'Bread': {'Item': items.Bread, 'Cost': random.randint(1, 5), 'Qty': random.randint(1, 10)},
            'Carrot': {'Item': items.Carrot, 'Cost': random.randint(1, 5), 'Qty': random.randint(1, 10)},
            'Potato': {'Item': items.Potato, 'Cost': random.randint(1, 5), 'Qty': random.randint(1, 10)}
        }

class Wizard(Villager):
    def __init__(self, name):
        super().__init__(name, 'Wizard')
        self.items = {
            'Enchanting': magic.Enchantment(),
            'Fireball Spell': {'Item': items.Fireball_Spell, 'Cost': random.randint(10, 30), 'Qty': random.randint(1, 2)},
            'Lightning Bolt Spell': {'Item': items.Lightning_Bolt_Spell, 'Cost': random.randint(15, 40), 'Qty': random.randint(1, 2)},
            'Healing Spell': {'Item': items.Healing_Spell, 'Cost': random.randint(20, 50), 'Qty': random.randint(1, 2)}
        }