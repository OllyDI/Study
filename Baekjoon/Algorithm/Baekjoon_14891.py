from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
orders = deque(list(map(int,input().split())) for _ in range(int(input())))

while orders :
    num, direction = orders.popleft()
    num -= 1
    t_bak1, t_bak2 = gear[num][2], gear[num][6]
    gear[num].rotate(direction)
    tempDir = direction
    

    direction = tempDir
    for i in range(num - 1 , 0 - 1 , -1) :
        if gear[i][2] != t_bak2 :
            t_bak2 = gear[i][6]
            gear[i].rotate(direction * -1)
            direction *= -1
        else : break

    direction = tempDir
    for i in range(num + 1 , 4) :
        if gear[i][6] != t_bak1 :
            t_bak1 = gear[i][2]
            gear[i].rotate(direction * -1)
            direction *= -1
        else : break

ans = 0
for i in range(4) :
    if gear[i][0] == 1: ans += (2 ** i)
print(ans)