from itertools import combinations

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

chicken = [[i,j] for i in range(n) for j in range(n) if maps[i][j] == 2]
home = [[i,j] for i in range(n) for j in range(n) if maps[i][j] == 1]

c_list = list(combinations(chicken, m))

def bfs(home, chicken):
    min_dist = 1000000000
    
    for i in chicken:
        dist = abs(i[0] - home[0]) + abs(i[1] - home[1])
        min_dist = min(min_dist, dist)
        
    return min_dist

val = []
for i in c_list:
    distance = 0
    for j in home : distance += bfs(j, i)
    val.append(distance)

print(min(val))