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
        Target.self.effect[self.effect] += self.strength
        if Target.self.effect[self.effect] > Target.self.effect[f'Max_{self.effect}']:
            Target.self.effect[self.effect] = Target.self.effect[f'Max_{self.effect}']


class Spells(Item):
    def __init__(self, name, level, type, mana_cost, damage):
        super().__init__(name, level)
        self.type = type
        self.mana_cost = mana_cost
        self.damage = damage


#--- Weapons ---
# Swords
Stick = Weapons('Stick', 1, 'Sword', 2)

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

# Armour
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

Bread = Item('Bread', 1) # Used to restore Stamina
Carrot = Item('Carrot', 1) # Used to restore Stamina
Potato = Item('Potato', 1) # Used to restore Stamina


# Spells
Fireball = Spells('Fireball', 1, 'Fir', 10, 5)
Lightning_Blast = Spells('Lightning_Blast', 1, 'Wat', 10, 5)
Water_Blast = Spells('Water_Blast', 1, 'Wat', 10, 5)
Vine_Grap = Spells('Vine_Grab', 1, 'Nat', 10, 5)
Unstable_Concoction = Spells('Unstable_Concoction', 1, 'Nat', 10, 5) # Doubles the Damage of your Next turn