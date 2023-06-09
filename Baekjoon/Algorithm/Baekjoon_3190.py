from collections import deque

n = int(input())
maps = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    maps[x - 1][y - 1] = 1

l = int(input())
mov = dict()
for _ in range(l):
    t, d = input().split()
    mov[int(t)] = d

snk = deque()
snk.append([0,0])

val= d = x = y = 0
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while True:
    val += 1
    x, y = x + direction[d][0], y + direction[d][1]

    if 0 <= x < n and 0 <= y < n and not [x, y] in snk :
        snk.append([x, y])
        if maps[x][y] == 1 : maps[x][y] = 0
        else : snk.popleft()
        if val in mov.keys() :
            nxt = mov[val]
            if nxt == 'L' : d = (d + 3) % 4
            else : d = (d + 1) % 4
    else : break

print(val)