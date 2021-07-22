#Psalm 13: 5,6
#Finding the winner of the Football League
n = int(input())
nm = (n*(n-1))//2
dic = {}
tab = []
for i in range(nm):
    team = input().split(" ")
    score = list(map(int,team[2].split("-")))
    team.remove(team[2])
    team.extend(score)
    tab.append(team)
    dic[team[0]] = 0
    dic[team[1]] = 0

for i in range(len(tab)):
    if(tab[i][2] > tab[i][3]):
        dic[tab[i][0]] += 3
    elif(tab[i][3] > tab[i][2]):
        dic[tab[i][1]] += 3
    else:
        dic[tab[i][0]] += 1
        dic[tab[i][1]] += 1

keys = list(dic.keys())
vals = list(dic.values())

pos = vals.index(max(vals))
print(keys[pos])
print(max(vals))