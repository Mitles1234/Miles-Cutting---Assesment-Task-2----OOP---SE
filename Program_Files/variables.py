import items

Health = 98
Max_Health = 100
Stamina = 65
Max_Stamina = 100
Mana = 23
Max_Mana = 100

Gold = 5

Name = 'John'
Room = 'Dark Forest'

#--- Weapons ---
Stick = items.Weapons('Stick', 'Sword', 1, 2, 1, 1, 1)
Wooden_Sword = items.Weapons('Wooden_Sword', 'Sword', 1, 4, 1, 1, 1)
Iron_Sword = items.Weapons('Iron_Sword', 'Sword', 1, 6, 1, 1, 1)

#--- Helmets ---
None_Helmet = items.Armour('None', 'Helmet', 0, 0, 1, 1, 1)

#--- ChestPlate ---
None_Chestplate = items.Armour('None', 'ChestPlate', 0, 0, 1, 1, 1)

#--- Boot ---
None_Boot = items.Armour('None', 'Boot', 0, 0, 1, 1, 1)

#--- Item ---
None_Item = items.Item('None', 'None')

Inventory = {
            'Player_Name': Name,
            'WeaponSlot': Wooden_Sword, 
            'HelmetSlot': None_Helmet, 
            'ChestplateSlot': None_Chestplate,
            'BootSlot': None_Boot,
            'OtherSlot1': {'Item': None_Item, 'Qty': 0},
            'OtherSlot2': {'Item': None_Item, 'Qty': 0},
            'OtherSlot3': {'Item': None_Item, 'Qty': 0},
            'OtherSlot4': {'Item': None_Item, 'Qty': 0}
    }