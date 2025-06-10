"""import saves 

def EnchantmentDisplay():
            x = 1.23123453
            return f'''
            +---+{'-'*39}+- Wat -+- Fir -+- Nat -+
            | 1 | Weapon Slot:     {saves.User.WeaponSlot.name:<20} | {saves.User.WeaponSlot.multiplyers['Wat']:<3.3f} | {saves.User.WeaponSlot.multiplyers['Fir']:<3.3f} | {saves.User.WeaponSlot.multiplyers['Nat']:<3.3f} |
            | 2 | Helmet Slot:     {saves.User.HelmetSlot.name:<20} | {saves.User.HelmetSlot.multiplyers['Wat']:<3.3f} | {saves.User.HelmetSlot.multiplyers['Fir']:<3.3f} | {saves.User.HelmetSlot.multiplyers['Nat']:<3.3f} |
            | 3 | Chestplate Slot: {saves.User.ChestplateSlot.name:<20} | {saves.User.ChestplateSlot.multiplyers['Wat']:<3.3f} | {saves.User.ChestplateSlot.multiplyers['Fir']:<3.3f} | {saves.User.ChestplateSlot.multiplyers['Nat']:<3.3f} |
            | 4 | Boot Slot:       {saves.User.BootSlot.name:<20} | {saves.User.BootSlot.multiplyers['Wat']:<3.3f} | {saves.User.BootSlot.multiplyers['Fir']:<3.3f} | {saves.User.BootSlot.multiplyers['Nat']:<3.3f} |
            +---+{'-'*39}+-------+-------+-------+'''

print(Inventory_Display())


"""

def Input_Selection(options: dict):
    def ReplaceInput():
        print("\033[2A", end="")  # Move cursor up 2 lines
        print('Error With Input')
        return get_input()  # Re-prompt
    
    def get_input():
        try:
            SaveSelection = input('Choice: ')

            SaveSelection = int(SaveSelection)
            if 1 <= SaveSelection <= len(option_list):
                option_list[SaveSelection - 1][1]()  # Call the corresponding function
            else:
                ReplaceInput()
        except (ValueError, IndexError):
            ReplaceInput()

    # Print options
    option_list = list(options.items())
    print("Select an option:")
    for i, (name, _) in enumerate(option_list, start=1):
        print(f"{i}. {name}")
    print()
    get_input()

def Forest():
    print("You enter the forest.")

def Battle():
    print("You encounter an enemy!")

TitleSelection({
    "Go to Forest": Forest,
    "Fight Enemy": Battle,
    "0": quit
})