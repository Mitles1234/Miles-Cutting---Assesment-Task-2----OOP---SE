import math

def Story(Room):
    if Room == 'Forest1':
        return 'Interesting Story'
    
    elif Room == 'Enemy1':
        return 'You Have Encountered and Enemy!!! You will have to fight'
    
def Title(Room):
    if Room == 'Forest1':
        return TitleGenerator('Dark Forest')


def TitleGenerator(Title):
    return f'''
    +{'-'*64}+
    |{' '*((32-(math.floor(len(Title)/2)))-6)}--==| {Title} |==--{' '*((32-(math.ceil(len(Title)/2)))-6)}|
    +{'-'*64}+
    '''