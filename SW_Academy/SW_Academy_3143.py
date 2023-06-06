T = int(input())

for test_case in range(1, T + 1):
    str1, str2 = input().split(" ")

    print("#{} {}".format(test_case, len(str1) - len(str2)*str1.count(str2) + str1.count(str2)))