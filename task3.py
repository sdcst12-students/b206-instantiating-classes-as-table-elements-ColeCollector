import random

class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0
    wealth = 0
    randlist = [1,1,1,1,2,2,2,3,3,4]

    def __init__(self):
        return
    

    for i in stats:
        rand1 = random.randint(1,6)
        rand2= random.randint(1,6)
        rand3 = random.randint(1,6)
        stats[i] = rand1+rand2+rand3

    level = randlist[random.randint(0,9)]

    hp = (random.randint(1,10)*level)
    
    if random.randint(1,100) < 30:
        gold = random.randint(0,6)

    if random.randint(1,100) < 50:
        silver = random.randint(3,12)

    if gold == 0:
        if random.randint(1,100) < 75:
            copper = random.randint(4,20)


    print(level,hp,gold,silver)

    