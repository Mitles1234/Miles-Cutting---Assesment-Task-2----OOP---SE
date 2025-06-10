import UI
import math

def MoveOptions(Room):
    if Room == 'Enemy1':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "East (Dark Forest) (2)": lambda: UI.PrintMainUI('Dark Forest'),
            "South (Village1) (4)": lambda: UI.PrintMainUI('Village1'),
            "West (Forest 1) (2)": lambda: UI.PrintMainUI('Forest1'),
            "North (Enemy 3) (8)": lambda: UI.PrintMainUI('Enemy3'),
        }
    elif Room == 'Enemy2':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "West (Dark Forest) (5)": lambda: UI.PrintMainUI('Dark Forest'),
            "East (Wizard 1) (3)": lambda: UI.PrintMainUI('Wizard1'),
            "South (Forest 2) (6)": lambda: UI.PrintMainUI('Forest2'),
        }
    elif Room == 'Enemy3':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "South East (Wizard Tower) (7)": lambda: UI.PrintMainUI('Wizard1'),
            "South West (Enemy) (7)": lambda: UI.PrintMainUI('Enemy1'),
            "West (Mountain) (20)": lambda: UI.PrintMainUI('Mountain'),
        }
    elif Room == 'Enemy4':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "West (Galamdor City) (6)": lambda: UI.PrintMainUI('Village2'),
            "East (Goblin King) (4)": lambda: UI.PrintMainUI('GoblinKing'),
            "South (Another City) (8)": lambda: UI.PrintMainUI('Village3'),
        }
    elif Room == 'Village1':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "North (Enemy) (8)": lambda: UI.PrintMainUI('Enemy1'),
            "South (Forest) (7)": lambda: UI.PrintMainUI('Forest2'),
            "East (Village) (5)": lambda: UI.PrintMainUI('Village2'),
        }
    elif Room == 'Village2':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "North (Aldwin Village) (8)": lambda: UI.PrintMainUI('Village1'),
            "West (Forest 3) (7)": lambda: UI.PrintMainUI('Forest3'),
            "South (Forest 4) (10)": lambda: UI.PrintMainUI('Forest4'),
            "East (Enemy 4) (6)": lambda: UI.PrintMainUI('Enemy4'),
        }
    elif Room == 'Village3':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "South (Forest 4) (12)": lambda: UI.PrintMainUI('Forest4'),
            "West (Forest 4) (12)": lambda: UI.PrintMainUI('Forest4'),
        }
    elif Room == 'Forest1':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "East (Enemy) (2)": lambda: UI.PrintMainUI('Enemy1'),
        }
    elif Room == 'Forest2':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "North (Forest 1) (4)": lambda: UI.PrintMainUI('Forest1'),
            "East (Wizard 2) (7)": lambda: UI.PrintMainUI('Wizard2'),
            "South (Forest 3) (5)": lambda: UI.PrintMainUI('Forest3'),
            "West (Enemy 1) (5)": lambda: UI.PrintMainUI('Enemy1'),
        }
    elif Room == 'Forest3':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "West (Village1) (9)": lambda: UI.PrintMainUI('Village1'),
            "East (Galamdor City) (7)": lambda: UI.PrintMainUI('Village2'),
            "South (Forest 4) (6)": lambda: UI.PrintMainUI('Forest4'),
            "North (Forest 2) (5)": lambda: UI.PrintMainUI('Forest2'),
        }
    elif Room == 'Forest4':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "North (Forest 3) (6)": lambda: UI.PrintMainUI('Forest3'),
            "East (Another City) (12)": lambda: UI.PrintMainUI('Village3'),
            "West (Galamdor City) (10)": lambda: UI.PrintMainUI('Village2'),
        }
    elif Room == 'Wizard1':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "West (Enemy 2) (3)": lambda: UI.PrintMainUI('Enemy2'),
            "South (Wizard 2) (8)": lambda: UI.PrintMainUI('Wizard2'),
        }
    elif Room == 'Wizard2':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "West (Forest 2) (7)": lambda: UI.PrintMainUI('Forest2'),
            "North (Wizard 1) (8)": lambda: UI.PrintMainUI('Wizard1'),
        }
    elif Room == 'Mountain':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "East (Mountain) (20)": lambda: UI.PrintMainUI('Mountain'),
        }
    elif Room == 'GoblinKing':
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
            "West (Enemy 4) (4)": lambda: UI.PrintMainUI('Enemy4'),
        }
    else:
        return {
            "Inventory": lambda: UI.DisplayInventoryScreen(),
        }

def InputHandling(Room):
    def ReplaceInput():
            print("\033[2A", end="")
            print('Error With Input')
            NextMove = ''
            InputHandling(Room)

    NextMove = input(f'What do You want to do? ')

    if NextMove == '0':
        UI.DisplayInventoryScreen()

    elif Room == 'Forest1':
        if NextMove == '1':
            UI.PrintMainUI('Enemy1')
        else:
            ReplaceInput()

    elif Room == 'Enemy1':
        if NextMove == '1':
            UI.PrintMainUI('Enemy1')
            
        elif NextMove == '0':
            pass
        else:
            ReplaceInput()

def Map(Room):

    def TitleGenerator(Title):
        return f'+{'─'*((27-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{'─'*((28-(math.ceil(len(Title)/2)))-6)}+'
    
    if Room == 'Enemy1':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────██      🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Enemy2':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ██──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Enemy3':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────██          🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Enemy4':
        return f'''        {TitleGenerator('Enemy')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────██─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Village1':
        return f'''        {TitleGenerator('Aldwin Village')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       ██       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
     
    elif Room == 'Village2':
        return f'''        {TitleGenerator('Galamdor City')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            ██────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Village3':
        return f'''        {TitleGenerator('Fay Town')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────██           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Forest1':
        return f'''        {TitleGenerator('Dark Forest')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ ██────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Forest2':
        return f'''        {TitleGenerator('Forgoten Forest')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │        ██ ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Forest3':
        return f'''        {TitleGenerator('Deep Forest')}
        │                                                       │
        │           ┌──────☠️           ██─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Forest4':
        return f'''        {TitleGenerator('Ash Forest')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       ██             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Wizard1':
        return f'''        {TitleGenerator('High Tower')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────██     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Wizard2':
        return f'''        {TitleGenerator('Willow Ward')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────██               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'Mountain':
        return f'''        {TitleGenerator('Mountain')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ██ ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────👑  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''
    
    elif Room == 'GoblinKing':
        return f'''        {TitleGenerator('Goblin King')}
        │                                                       │
        │           ┌──────☠️           🌲─────┐                 │
        │           │       │           │     │                 │
        │     ⛰️  ───┘       │           │     │                 │
        │                   │           │     └────🏠           │
        │               ☠️ ──┴────🔮     │                       │
        │                │              │                       │
        │        ┌───────┴────────┬─────┤                       │
        │        │                │     └───────┐               │
        │ 🌲────☠️       🏠       🌲             ├────☠️ ─────██  │
        │        │       │            🏠────────┘               │
        │        └────┬──┴──┬──────────┘                        │
        │             │     │                                   │
        │             │     └──┐                                │
        │             │        │                                │
        │       🌲  ──┘        │                             ⬆  │
        │                      └────────────🔮               N  │
        │                                                       │
        +───────────────────────────────────────────────────────+'''