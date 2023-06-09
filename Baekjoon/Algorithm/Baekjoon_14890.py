def check(lst):
    i, s = 0, 1
    arr = lst[i]

    while i < n-1 :
        i += 1
        d = arr - lst[i]
        if d > 1 or d < -1 : return False
        elif d == 1 :
            if i+l > n : return False
            for j in range(i+1, i+l) :
                if arr - lst[j] != 1 : return False
            s = 1-l
        elif d == -1 :
            if i-l < 0 or s < l : return False
            s = 1
        else : s += 1
        arr = lst[i]

    return True

n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

val = 0
for row in maps:
    if check(row): val += 1

for y in range(n):
    for x in range(n):
        if x > y: maps[y][x], maps[x][y] = maps[x][y], maps[y][x]

for row in maps:
    if check(row) : val += 1

print(val)