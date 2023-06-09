n = int(input())
maps=[[0] * (n + 1)] + [[0] + list(map(int,input().split())) for _ in range(n)]
total, val = 0, 1000000000

def solve(x, y, d1, d2) :
    temp=[[0] * (n + 1) for _ in range(n + 1)]
    temp[x][y] = 5
    for i in range(1, d1 + 1) : temp[x + i][y - i] = temp[x + d2 + i][y + d2 - i] = 5
    for i in range(1, d2 + 1) : temp[x + i][y + i] = temp[x + d1 + i][y - d1 + i] = 5

    one, two, three, four = 0, 0, 0, 0
    for i in range(1, x + d1) :
        for j in range(1, y + 1) :
            if temp[i][j] == 5 : break
            one += maps[i][j]
    for i in range(1, x + d2 + 1) :
        for j in range(n, y, -1):
            if temp[i][j] == 5 : break
            two += maps[i][j]
    for i in range(x + d1, n + 1) :
        for j in range(1, y - d1 + d2) :
            if temp[i][j] == 5 : break
            three += maps[i][j]
    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y - d1 + d2 - 1, -1):
            if temp[i][j] == 5 : break
            four += maps[i][j]

    five = total - one - two - three - four
    maxV = max(one, two, three, four, five)
    minV = min(one, two, three, four, five)
    return maxV - minV

total = sum(map(sum, maps))
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if x + d1 + d2 > n : continue
                if 1 > y - d1 : continue
                if y + d2 > n : continue
                val = min(val, solve(x, y, d1, d2))
print(val)