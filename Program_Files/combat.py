import saves
import UI

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
        self.healthh -= (saves.User.WeaponSlot.damage * saves.User.WeaponSlot.multiplyers[self.type])

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
    print(f"""You have Encountered a {Enemy.name}

    {Enemy.name}: 
        Health:  ♥️  \033[31m{UI.StatBar(Enemy.health, Enemy.max_health)} ({Enemy.health}/{Enemy.max_health})
        Damage:  ⚔️  \033[34m{Enemy.damage}\033[0m
        Type:    ☯️  \033[33m{Type}\033[0m

    {saves.User.Player_Name}:
        Health:  ♥️  \033[31m{UI.StatBar(saves.User.Health['Health'], saves.User.Health['Max_Health'])} ({saves.User.Health['Health']}/{saves.User.Health['Max_Health']})
        Damage:  ⚔️  \033[34m{saves.User.WeaponSlot.damage}\033[0m
        ELemental Damage:        ☯️  \033[33m{saves.User.WeaponSlot.multiplyers[Enemy.type]}\033[0m
        Elemental Protection:    ☯️  \033[33m{((saves.User.HelmetSlot.multiplyers[Enemy.type])+(saves.User.ChestplateSlot.multiplyers[Enemy.type])+(saves.User.BootSlot.multiplyers[Enemy.type]))/3}\033[0m
""")

    while True:
        if Enemy.health <= 0:
            print(f"You have defeated the {Enemy.name}!")
            saves.User.WeaponSlot['Level'] += Enemy.level/2
        elif saves.User.Health['Health'] <= 0:
            print(f"You have been defeated by the {Enemy.name}!")
        else:
            print(f"Your turn! Choose an action:")
            print("1. Attack")
            print("2. Use Item")

            UI.Input_Selection({
                "Attack": lambda: saves.User.Attacking(Enemy),
                "Use Item": lambda: UI.DisplayInventoryScreen()
            })
            
            Enemy.Attacking(saves.User)


Combat(Goblin)