import variables
import json
import items


class Player():
    def __init__(self, Save):
        with open(f'Save{Save}.json', 'r') as f:
            Player_Data = json.load(f)

        self.Player_Name = Player_Data.get('Player_Name', 'John')
        self.Health = Player_Data.get('Health', {'Health': 100, 'Max_Health': 100})
        self.Stamina = Player_Data.get('Stamina', {'Stamina': 100, 'Max_Stamina': 100})
        self.Mana = Player_Data.get('Mana', {'Mana': 100, 'Max_Mana': 100})
        self.WeaponSlot = getattr(items, Player_Data.get('WeaponSlot', 'Stick'))
        self.HelmetSlot = getattr(items, Player_Data.get('HelmetSlot', 'Bronze_Helmet'))
        self.ChestplateSlot = getattr(items, Player_Data.get('ChestplateSlot', 'Bronze_Chestplate'))
        self.BootSlot = getattr(items, Player_Data.get('BootSlot', 'Bronze_Boot'))
        self.OtherSlot1 = {
            'Item': getattr(items, Player_Data.get('OtherSlot1', {}).get('Item', 'None_Item')),
            'Qty': Player_Data.get('OtherSlot1', {}).get('Qty', 0)
        }
        self.OtherSlot2 = {
            'Item': getattr(items, Player_Data.get('OtherSlot2', {}).get('Item', 'None_Item')),
            'Qty': Player_Data.get('OtherSlot2', {}).get('Qty', 0)
        }
        self.OtherSlot3 = {
            'Item': getattr(items, Player_Data.get('OtherSlot3', {}).get('Item', 'None_Item')),
            'Qty': Player_Data.get('OtherSlot3', {}).get('Qty', 0)
        }
        self.OtherSlot4 = {
            'Item': getattr(items, Player_Data.get('OtherSlot4', {}).get('Item', 'None_Item')),
            'Qty': Player_Data.get('OtherSlot4', {}).get('Qty', 0)
        }
        self.Location = Player_Data.get('Location', 'Forest1')

    def Save(self, Save):
        Player_Stats = {
            'Player_Name': self.Player_Name,
            'Health': self.Health,
            'Stamina': self.Stamina,
            'Mana': self.Mana,
            'WeaponSlot': self.WeaponSlot.name,
            'HelmetSlot': self.HelmetSlot.name,
            'ChestplateSlot': self.ChestplateSlot.name,
            'BootSlot': self.BootSlot.name,
            'OtherSlot1': {'Item': self.OtherSlot1['Item'].name, 'Qty': self.OtherSlot1['Qty']},
            'OtherSlot2': {'Item': self.OtherSlot2['Item'].name, 'Qty': self.OtherSlot2['Qty']},
            'OtherSlot3': {'Item': self.OtherSlot3['Item'].name, 'Qty': self.OtherSlot3['Qty']},
            'OtherSlot4': {'Item': self.OtherSlot4['Item'].name, 'Qty': self.OtherSlot4['Qty']}
        }
        with open(f'Save{Save}.json', 'w') as f:
            json.dump(Player_Stats, f)

    def Attacking(self, Target):
        Target.Player_Attacked(self.WeaponSlot.damage)

    def Attacked(self, Damage, Type):
        self.Health['Health'] -= (Damage / ((self.HelmetSlot.multiplyers[Type] + self.ChestplateSlot.multiplyers[Type] + self.BootSlot.multiplyers[Type]) / 3))

User = Player(1)

#User.Save(1)
