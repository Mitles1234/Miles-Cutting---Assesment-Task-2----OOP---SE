import variables
import json
import items

User = None  # Global variable to hold the player instance

class Player():
    def __init__(self, Save):
        self.Player_Name = Save['Name']

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
            'Name': self.Player_Name,
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
    pass

def CreateCharacter(SaveNum):
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
        'Name': Name_Input,

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


