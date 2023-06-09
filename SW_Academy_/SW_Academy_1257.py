T = int(input())

for test_case in range(1, T + 1):
    index = int(input())
    str1 = input()
    str2 = []
    length = len(str1)
    count = 0

    while True :
        for i in range(len(str1)-count) : 
            if count == 0 : str2.append(str1[i])
            else : str2.append(str1[i:count+1+i])
        count += 1
        if count >= length : break
    
    str2 = sorted(list(set(str2)))
    str2.sort()
    if index <= len(str2) : print("#{}".format(test_case), str2[index - 1])
    else : print("#{} none".format(test_case))
    