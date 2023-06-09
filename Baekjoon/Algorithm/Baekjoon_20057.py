def push(d, sn, x, y):
    global maps, val, n
    first = sn
    left = [(-1, 0, 0.07), (-2, 0, 0.02),
                (1, 0, 0.07), (2, 0, 0.02),
                (-1, 1, 0.01), (1, 1, 0.01),
                (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)]
    right = [(-1, 0, 0.07), (-2, 0, 0.02),
                (1, 0, 0.07), (2, 0, 0.02),
                (-1, -1, 0.01), (1, -1, 0.01),
                (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05)]
    up = [(-1, -1, 0.1), (-1, 1, 0.1),
                (0, 1, 0.07), (0, -1, 0.07),
                (1, -1, 0.01), (1, 1, 0.01),
                (-2, 0, 0.05), (0, -2, 0.02), (0, 2, 0.02)]
    down = [(-1, -1, 0.01), (-1, 1, 0.01),
                (0, -1, 0.07), (0, 1, 0.07),
                (0, -2, 0.02), (0, 2, 0.02),
                (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)]
    move_list = [up, down, right, left]
    last_move = [(-1, 0, 1),(1, 0, 1),(0, 1, 1),(0, -1, 1)]

    for i in move_list[d]:
        tx, ty = x + i[0], y + i[1]
        temp = int(first*i[2])
        sn -= temp
        if(tx < 0 or tx >= n or ty < 0 or ty >= n) :
            val+= temp
            continue
        maps[tx][ty] += temp

    lx, ly = x+last_move[d][0], y+last_move[d][1]
    if(lx >= n or lx < 0 or ly >= n or ly < 0) : val += sn
    else : maps[lx][ly] += sn


n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
val = 0
fn = [n // 2, n // 2]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(n - 1) :
    if(i % 2 == 0) :
        for _ in range(i+1) :
            fn[0], fn[1] = fn[0] + direction[3][0], fn[1] + direction[3][1]
            temp = maps[fn[0]][fn[1]]
            maps[fn[0]][fn[1]] = 0
            push(3, temp, fn[0], fn[1])

        for _ in range(i + 1) :
            fn[0], fn[1] = fn[0]+direction[1][0], fn[1]+direction[1][1]
            temp = maps[fn[0]][fn[1]]
            maps[fn[0]][fn[1]] = 0
            push(1,temp,fn[0],fn[1])

    else:
        for _ in range(i + 1) :
            fn[0], fn[1] = fn[0]+direction[2][0], fn[1]+direction[2][1]
            temp = maps[fn[0]][fn[1]]
            maps[fn[0]][fn[1]] = 0
            push(2, temp, fn[0], fn[1])


        for _ in range(i + 1) :
            fn[0], fn[1] = fn[0]+direction[0][0], fn[1]+direction[0][1]
            temp = maps[fn[0]][fn[1]]
            maps[fn[0]][fn[1]] = 0
            push(0, temp, fn[0], fn[1])

for _ in range(n) :
    fn[0], fn[1] = fn[0] + direction[3][0], fn[1] + direction[3][1]
    temp = maps[fn[0]][fn[1]]
    maps[fn[0]][fn[1]] = 0
    push(3, temp, fn[0], fn[1])

print(val)