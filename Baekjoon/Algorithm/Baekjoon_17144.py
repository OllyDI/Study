direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

time = 0
maps, cln, cdic = [], [], {}

r, c, t = map(int, input().split())
for i in range(r) :
    lst = list(map(int, input().split()))

    for j in range(c) :
        if lst[j] == -1 :
            cln.append((i, j))
            cdic[(i, j)] = True
    maps.append(lst)

while time < t :
    maps2 = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                count = 0
                for d in range(4):
                    nx, ny = i + direction[d][0], j + direction[d][1]
                    if -1 < nx < r and -1 < ny < c and cdic.get((nx, ny)) is None:
                        count += 1
                        maps2[nx][ny] += maps[i][j] // 5
                maps2[i][j] += maps[i][j] - count * (maps[i][j] // 5)

    for i in range(2):
        temp1, temp2, d = 0, 0, 0
        if i == 0:
            reDir1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            x, y = cln[0][0], cln[0][1] + 1
            while x != cln[0][0] or y != cln[0][1]:
                temp2 = maps2[x][y]
                maps2[x][y] = temp1
                temp1 = temp2
                if 0 > x + reDir1[d][0] or x + reDir1[d][0] > r - 1 or y + reDir1[d][1] < 0 or y + reDir1[d][1] > c - 1 : d += 1
                x += reDir1[d][0]
                y += reDir1[d][1]
        else:
            reDir2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            x, y = cln[1][0], cln[1][1] + 1
            while x != cln[1][0] or y != cln[1][1]:
                temp2 = maps2[x][y]
                maps2[x][y] = temp1
                temp1 = temp2
                if 0 > x + reDir2[d][0] or x + reDir2[d][0] > r - 1 or y + reDir2[d][1] < 0 or y + reDir2[d][1] > c - 1 : d += 1
                x += reDir2[d][0]
                y += reDir2[d][1]
    maps = maps2
    time += 1

val = 0
for i in range(r) :
    for j in range(c) :
        if maps[i][j] > 0 : val += maps[i][j]
print(val)