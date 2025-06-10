import random
import items

def Enchantment(item, type=None):
    Level = item.level

    Multiplyer = (random.randint(0, Level+10)/10)

    print(Multiplyer)

    if type == None:
        return {'Wat': (1+((Multiplyer)/4)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1+((Multiplyer)/4))}
    else:
        if type == 'Fir':
            return {'Wat': (1-((Multiplyer)/4)), 'Fir': (1+(Multiplyer)), 'Nat': (1+((Multiplyer)/4))}
        
        elif type == 'Wat':
            return {'Wat': (1+(Multiplyer)), 'Fir': (1+((Multiplyer)/4)), 'Nat': (1-((Multiplyer)/4))}
        
        elif type == 'Nat':
            return {'Wat': (1+((Multiplyer)/4)), 'Fir': (1-((Multiplyer)/4)), 'Nat': (1+(Multiplyer))}
    