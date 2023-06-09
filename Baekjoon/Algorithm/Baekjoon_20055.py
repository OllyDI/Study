n, k = map(int, input().split())
belt = list(map(int,input().split()))

rt = 0
robot = [0] * (n * 2)

while belt.count(0) < k :
    rt += 1
    belt.insert(0, belt.pop())
    robot.insert(0, robot.pop())
    robot[(n * 2) // 2 - 1] = 0  # 내리는 위치에 있는 로봇을 삭제

    temp = []
    for i in range(n * 2) :
        if robot[i] > 0 : temp.append((robot[i], i))
    temp = sorted(temp)
    
    for (t1, t2) in temp :
         if robot[t2 + 1] == 0 and belt[t2 + 1] > 0 :
            robot[t2], robot[t2 + 1], belt[t2 + 1] = 0, t1, belt[t2 + 1] - 1
    robot[(n * 2) // 2 - 1] = 0 

    if belt[0] > 0 : belt[0], robot[0] = belt[0] - 1, rt + 1

print(rt)