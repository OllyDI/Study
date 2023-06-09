def dfs(sx, sy, dirs, sum) :
    global answer, maps
    mbak = [[[]] * 4 for _ in range(4)]
    for i in range(4) :
        for j in range(4) : mbak[i][j] = maps[i][j][:]
    moveFish()

    if answer < sum : answer = sum

    for i in range(1, 4) :
        snx, sny = sx + direction[dirs][0] * i, sy + direction[dirs][1] * i
        if snx < 0 or snx >= 4 or sny < 0 or sny >= 4 : break
        if maps[snx][sny][0] == 0 : continue
        tfish = maps[snx][sny][:]
        maps[sx][sy][0], maps[snx][sny][0] = 0, -1
        dfs(snx, sny, maps[snx][sny][1], sum + tfish[0])
        maps[sx][sy][0], maps[snx][sny][0] = -1, tfish[0]
        
    for i in range(4) :
        for j in range(4) : maps[i][j] = mbak[i][j][:]

def moveFish() :
    for i in range(1, 17) :
        isM = False
        for j in range(4) :
            for k in range(4) :
                if not isM and maps[j][k][0] == i :
                    for l in range(8) :
                        newDir = (maps[j][k][1] + l) % 8
                        nj, nk = j + direction[newDir][0], k + direction[newDir][1]
                        if nj < 0 or nj >= 4 or nk < 0 or nk >= 4 : continue
                        if maps[nj][nk][0] == -1 : continue
                        maps[j][k][1] = newDir
                        maps[nj][nk], maps[j][k] = maps[j][k], maps[nj][nk]
                        isM = True
                        break

maps = [[[]] * 4 for _ in range(4)]
direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

for i in range(4) :
    lst = list(map(int,input().split()))
    for j in range(4) : maps[i][j] = [lst[j * 2], lst[j * 2 + 1] - 1]

answer = 0
shark = maps[0][0][:]
maps[0][0][0] = -1
dfs(0, 0, shark[1], shark[0])
print(answer)
