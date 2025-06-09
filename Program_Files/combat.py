import variables
"""
class Player():
    def __init__(self):
        self.name = variables.Name
        self.inventory = variables.Inventory
        self.health = variables.Health
        self.protection = (variables.Inventory['HelmetSlot'].protection) + (variables.Inventory['ChestplateSlot'].protection) + (variables.Inventory['BootSlot'].protection)
        #self.watpro = self.resistance*(((variables.Inventory['HelmetSlot'].firpro) + (variables.Inventory['ChestplateSlot'].firpro) + (variables.Inventory['HelmetSlot'].firpro))/3)
        #self.firpro = self.resistance*(((variables.Inventory['HelmetSlot'].firpro) + (variables.Inventory['ChestplateSlot'].firpro) + (variables.Inventory['HelmetSlot'].firpro))/3)
        #self.natpro = self.resistance*(((variables.Inventory['HelmetSlot'].firpro) + (variables.Inventory['ChestplateSlot'].firpro) + (variables.Inventory['HelmetSlot'].firpro))/3)

    def Attack(self, x):
        Damage = variables.Inventory['WeaponSlot'].damage
        WatDmg = variables.Inventory['WeaponSlot'].Watdmg
        FirDmg = variables.Inventory['WeaponSlot'].Firdmg
        NatDmg = variables.Inventory['WeaponSlot'].Natdmg

        x.Attacked(Damage, WatDmg, FirDmg, NatDmg)
    

class Enemy():
    def __init__(self, name, type, damage, health, resistance):
        self.name = name
        self.type = type
        self.damage = damage
        self.health = health
        self.resistance = resistance

    def Attacked(self, Damage, Wat, Fir, Nat):
        if self.type == 'Fir':
            self.health -= (Damage * Fir)

        elif self.type == 'Wat':
            self.health -= (Damage * Wat)

        elif self.type == 'Nat':
            self.health -= (Damage * Nat)

        else:
            self.health -= (Damage)

        print(self.health)



def Dead():
    pass

def PlayerTurn():
    pass

Char = Player()
Bill = Enemy('Bill', 'Fir', 8, 1, 1)

Char.Attack(Bill)

"""


class Enemy():
    def __init__(self, name, type, damage, health):
        self.name = name
        self.type = type
        self.damage = damage
        self.health = health

    def Attacked(self, Damage, Wat, Fir, Nat):
        if self.type == 'Fir':
            self.health -= (Damage * Fir)

        elif self.type == 'Wat':
            self.health -= (Damage * Wat)

        elif self.type == 'Nat':
            self.health -= (Damage * Nat)

    def Attacking(self):
       if self.type == 'Fir':
            variables.Health -= (Damage * Fir)

        elif self.type == 'Wat':
            self.health -= (Damage * Wat)

        elif self.type == 'Nat':
            self.health -= (Damage * Nat) 