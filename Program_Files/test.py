import saves 

def Inventory_Display():
            return f'''
            +---+{'-'*30}+- Wat -+- Fir -+- Nat -+
            |1  |Weapon Slot: {saves.User.WeaponSlot.name:<16} | {saves.User.WeaponSlot.multiplyers['Wat']:<6}| {saves.User.WeaponSlot.multiplyers['Fir']:<6}| {saves.User.WeaponSlot.multiplyers['Nat']:<6}|
            '''

print(Inventory_Display())