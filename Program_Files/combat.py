import saving

class Enemy():
    def __init__(self, name, health, damage, type, level):
        self.name = name
        self.health = health
        self.damage = damage
        self.type = type
        self.level = level

    def Attacking(self, Target):
        Target.Attacked(self.damage, self.type)

    def Player_Attacked(self):
        self.healthh -= (User.WeaponSlot.damage * User.WeaponSlot.multiplyers[self.type])

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

