n = int(input())
arr = []
for i in range(n):
    a, b = map(str, input().split())
    arr.append([int(a), b])
    
arr.sort(key=lambda x: x[0])
for i in arr: print(i[0], i[1])