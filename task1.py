class team:
    wins = 0
    losses = 0
    games = 0
    results = {}

    def points(self):
        return
    
    def record(self):
        return

    def win(self):
        self.wins+=1
        return
    
    def loss(self):
        self.losses+=1
        return
    
    def __init__(self,wins):
        pass

teams = {}
teams["A"] = team("Ants")
teams["B"] = team("Bears")
teams["C"] = team("Cougars")
teams["D"] = team("Doges")
teams["E"] = team("Elephants")
teams["F"] = team("Foxes")
teams["G"] = team("Giants")


print(teams['A'].wins)

gameData = [
    {'t1': 'A', 's1': 2, 't2': 'B', 's2': 3}, 
    {'t1': 'A', 's1': 4, 't2': 'C', 's2': 3}, {'t1': 'A', 's1': 1, 't2': 'D', 's2': 0}, {'t1': 'A', 's1': 0, 't2': 'E', 's2': 2}, {'t1': 'A', 's1': 4, 't2': 'F', 's2': 2}, {'t1': 'A', 's1': 2, 't2': 'G', 's2': 4}, {'t1': 'B', 's1': 2, 't2': 'A', 's2': 1}, {'t1': 'B', 's1': 2, 't2': 'C', 's2': 1}, {'t1': 'B', 's1': 3, 't2': 'D', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'E', 's2': 0}, {'t1': 'B', 's1': 3, 't2': 'F', 's2': 1}, {'t1': 'B', 's1': 2, 't2': 'G', 's2': 0}, {'t1': 'C', 's1': 0, 't2': 'A', 's2': 2}, {'t1': 'C', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'C', 's1': 3, 't2': 'D', 's2': 4}, {'t1': 'C', 's1': 1, 't2': 'E', 's2': 1}, {'t1': 'C', 's1': 3, 't2': 'F', 's2': 4}, {'t1': 'C', 's1': 3, 't2': 'G', 's2': 1}, {'t1': 'D', 's1': 1, 't2': 'A', 's2': 3}, {'t1': 'D', 's1': 2, 't2': 'B', 's2': 0}, {'t1': 'D', 's1': 4, 't2': 'C', 's2': 4}, {'t1': 'D', 's1': 2, 't2': 'E', 's2': 2}, {'t1': 'D', 's1': 3, 't2': 'F', 's2': 3}, {'t1': 'D', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'E', 's1': 2, 't2': 'A', 's2': 0}, {'t1': 'E', 's1': 4, 't2': 'B', 's2': 2}, {'t1': 'E', 's1': 0, 't2': 'C', 's2': 2}, {'t1': 'E', 's1': 3, 't2': 'D', 's2': 1}, {'t1': 'E', 's1': 0, 't2': 'F', 's2': 4}, {'t1': 'E', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'F', 's1': 2, 't2': 'A', 's2': 1}, {'t1': 'F', 's1': 3, 't2': 'B', 's2': 3}, {'t1': 'F', 's1': 1, 't2': 'C', 's2': 4}, {'t1': 'F', 's1': 0, 't2': 'D', 's2': 1}, {'t1': 'F', 's1': 0, 't2': 'E', 's2': 1}, {'t1': 'F', 's1': 2, 't2': 'G', 's2': 2}, {'t1': 'G', 's1': 4, 't2': 'A', 's2': 2}, {'t1': 'G', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'G', 's1': 1, 't2': 'C', 's2': 2}, {'t1': 'G', 's1': 0, 't2': 'D', 's2': 3}, {'t1': 'G', 's1': 4, 't2': 'E', 's2': 3}, {'t1': 'G', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'G', 's1': 2, 't2': 'F', 's2': 3}, {'t1': 'G', 's1': 2, 't2': 'E', 's2': 2}, {'t1': 'G', 's1': 4, 't2': 'D', 's2': 2}, {'t1': 'G', 's1': 3, 't2': 'C', 's2': 3}, {'t1': 'G', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'G', 's1': 0, 't2': 'A', 's2': 0}, {'t1': 'F', 's1': 1, 't2': 'G', 's2': 4}, {'t1': 'F', 's1': 2, 't2': 'E', 's2': 3}, {'t1': 'F', 's1': 1, 't2': 'D', 's2': 3}, {'t1': 'F', 's1': 0, 't2': 'C', 's2': 1}, {'t1': 'F', 's1': 4, 't2': 'B', 's2': 2}, {'t1': 'F', 's1': 4, 't2': 'A', 's2': 4}, {'t1': 'E', 's1': 4, 't2': 'G', 's2': 1}, {'t1': 'E', 's1': 3, 't2': 'F', 's2': 0}, {'t1': 'E', 's1': 0, 't2': 'D', 's2': 0}, {'t1': 'E', 's1': 0, 't2': 'C', 's2': 4}, {'t1': 'E', 's1': 3, 't2': 'B', 's2': 3}, {'t1': 'E', 's1': 4, 't2': 'A', 's2': 0}, {'t1': 'D', 's1': 0, 't2': 'G', 's2': 2}, {'t1': 'D', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'D', 's1': 2, 't2': 'E', 's2': 1}, {'t1': 'D', 's1': 3, 't2': 'C', 's2': 3}, {'t1': 'D', 's1': 4, 't2': 'B', 's2': 1}, {'t1': 'D', 's1': 3, 't2': 'A', 's2': 0}, {'t1': 'C', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'C', 's1': 1, 't2': 'F', 's2': 3}, {'t1': 'C', 's1': 4, 't2': 'E', 's2': 4}, {'t1': 'C', 's1': 4, 't2': 'D', 's2': 3}, {'t1': 'C', 's1': 1, 't2': 'B', 's2': 1}, {'t1': 'C', 's1': 3, 't2': 'A', 's2': 1}, {'t1': 'B', 's1': 3, 't2': 'G', 's2': 3}, {'t1': 'B', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'E', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'D', 's2': 1}, {'t1': 'B', 's1': 4, 't2': 'C', 's2': 2}, {'t1': 'B', 's1': 0, 't2': 'A', 's2': 1}, {'t1': 'A', 's1': 2, 't2': 'G', 's2': 4}, {'t1': 'A', 's1': 1, 't2': 'F', 's2': 0}, {'t1': 'A', 's1': 4, 't2': 'E', 's2': 3}, {'t1': 'A', 's1': 4, 't2': 'D', 's2': 2}, {'t1': 'A', 's1': 1, 't2': 'C', 's2': 2}, {'t1': 'A', 's1': 4, 't2': 'B', 's2': 0}]

for i in gameData:

    t1 = i['t1']
    s1 = i['s1']
    t2 = i['t2']
    s2 = i['s2']

    if s2 > s1:
        team(i['t2']).win()
        team(i['t1']).loss()
        print(t2, "win")

    elif s1 > s2:
        team(i['t1']).win()
        team(i['t2']).loss()
        print(t1, "win")


for i in teams:
    print(team[i])