n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort()
for i in arr: print(i[0], i[1])