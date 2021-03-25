from collections import defaultdict

def no_idea():
    return 'unknown'

if __name__ == '__main__':
    creatures = defaultdict(no_idea)
    creatures['A'] = 'Abominable Snowman'
    creatures['B'] = 'Basilisk'
    print(creatures['A']) # 'Abominable Snowman'
    print(creatures['B']) # 'Basilisk'
    print(creatures['C']) # 'unknown'
    print(creatures)


