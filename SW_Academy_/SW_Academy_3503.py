T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    
    lst = sorted(map(int, input().split()))
    m = 0

    for i in range(number - 2) :
        if abs(lst[i] - lst[i + 2]) > m : m = abs(lst[i] - lst[i + 2])
    if abs(lst[0] - lst[1]) > m : m = lst[0] - lst[1]
    if abs(lst[number - 2] - lst[number - 1]) > m : m = abs(lst[number - 2] - lst[number - 1])

    print("#{} {}".format(test_case, m))