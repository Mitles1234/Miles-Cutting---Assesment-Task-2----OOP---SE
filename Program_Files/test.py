class Weapons():
    def __init__(self, name, damage, multiplyers=None):
        self.name = name
        self.damage = damage

        if multiplyers is None:
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1}
        else:
            self.multiplyers = multiplyers

class Armour():
    def __init__(self, name, protection, multiplyers=None):
        self.name = name
        self.resistance = protection

        if multiplyers is None:
            self.multiplyers = {'Wat': 1, 'Fir': 1, 'Nat': 1}
        else:
            self.multiplyers = multiplyers
            
class Enemy():
    def __init__(self, name, health, damage, type):
        self.name = name
        self.health = health
        self.damage = damage
        self.type = type

    def Attacking(self, Target):
        Target.Attacked(self.damage, self.type)

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


class Player():
    def __init__(self):
        self.Player_Name = 'John'
        self.Health = {'Health': 100, 'Max_Health': 100}
        self.Stamina = {'Stamina': 100, 'Max_Stamina': 100}
        self.Mana = {'Mana': 100, 'Max_Mana': 100}
        self.WeaponSlot = Sword
        self.ArmourSlot = IronArmour
        self.OtherSlot1 = {'Item': None_Item, 'Qty': 0}
        self.OtherSlot2 = {'Item': None_Item, 'Qty': 0}
        self.OtherSlot3 = {'Item': None_Item, 'Qty': 0}
        self.OtherSlot4 = {'Item': None_Item, 'Qty': 0}

    def Attacking(self, Target):
        Target.Player_Attacked(self.WeaponSlot.damage)

    def Attacked(self, Damage, Type):
        self.Health['Health'] -= (Damage / self.ArmourSlot.multiplyers[Type])


Sword = Weapons('Sword', 10, {'Wat': 1, 'Fir': 1.5, 'Nat': 0.5})
IronArmour = Armour('Iron Armour', 5, {'Wat': 1, 'Fir': 0.5, 'Nat': 1.5})
None_Item = None


User = Player()

Enemy1 = Enemy('Goblin', 50, 5, 'Fir')
Enemy2 = Enemy('Water Spirit', 50, 5, 'Wat')
Enemy3 = Enemy('Nature Beast', 50, 5, 'Nat')


print(f'Health: {Enemy1.health}')
print(f'Player Health: {User.Health['Health']}')


Enemy1.Attacking(User)

print(f'Health: {Enemy1.health}')
print(f'Player Health: {User.Health['Health']}')


"""
    def Player_Attacked(self, Damage):
        if self.type == 'Fir':
            self.health -= (Damage * User.ArmourSlot.multiplyers['Fir'])

        elif self.type == 'Wat':
            self.health -= (Damage * User.ArmourSlot.multiplyers['Wat'])

        elif self.type == 'Nat':
            self.health -= (Damage * User.ArmourSlot.multiplyers['Nat'])

        else:
            self.health -= Damage
"""