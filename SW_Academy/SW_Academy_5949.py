T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    lst1, lst2, val = [], [], 0

    for i in range(len(str1)) :
        if str1[i] == 'a' : lst1.append(i)
        if str2[i] == 'a' : lst2.append(i)
    
    if len(lst1) == len(lst2) :
        for i in range(len(lst1)) : val = val + abs(lst1[i] - lst2[i])
    else : val = -1

    print("#{} {}".format(test_case, val))