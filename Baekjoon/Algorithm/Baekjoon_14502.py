import copy

def sVirus(x, y, temp) :
    for i in range(4) : 
        tx, ty = x + direction[i][0], y + direction[i][1]
        if 0 <= tx and tx < n and 0 <= ty and ty < m :
            if temp[tx][ty] == 0 :
                temp[tx][ty] = 2
                sVirus(tx, ty, temp)


def wall(start, depth) :
    global val

    if depth == 3 : 
        temp = copy.deepcopy(maps)
        for i in range(len(virus)) : 
            sVirus(virus[i][0], virus[i][1], temp)

        maxWall = 0
        for i in range(n) :
            for j in range(m) : 
                if temp[i][j] == 0 : maxWall += 1
        val = max(val, maxWall)
    else :
        for i in range(start, n * m) :
            x, y = i // m, i % m
            if maps[x][y] == 0 :
                maps[x][y] = 1
                wall(i + 1, depth + 1)
                maps[x][y] = 0


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
val = 0
virus = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 2 : virus.append([i, j])

wall(0, 0)
print(val)
