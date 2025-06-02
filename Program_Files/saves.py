import variables
import json

savestats = {
    'Health': 98,
    'Max_health': 100,
    'Stamina': 65,
    'Max_Stamina': 100,
    'Mana': 23,
    'Max_Mana': 100,
    'Gold': 5,

    'Room': 'Dark Forest',
    'Inventory': {
            'Player_Name': variables.Name,
            'WeaponSlot': variables.Wooden_Sword, 
            'HelmetSlot': variables.None_Helmet, 
            'ChestplateSlot': variables.None_Chestplate,
            'BootSlot': variables.None_Boot,
            'OtherSlot1': {'Item': variables.None_Item, 'Qty': 0},
            'OtherSlot2': {'Item': variables.None_Item, 'Qty': 0},
            'OtherSlot3': {'Item': variables.None_Item, 'Qty': 0},
            'OtherSlot4': {'Item': variables.None_Item, 'Qty': 0}
    }
}


def Load(Save):
    with open(f'{Save}.json', 'w') as f:
        json.dump(savestats, f)


Load('Save1')