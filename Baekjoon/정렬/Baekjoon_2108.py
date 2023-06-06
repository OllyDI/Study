from collections import Counter

n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort()
print(round(sum(arr)/n), arr[n//2], sep='\n')

mode = Counter(arr).most_common()
if len(arr) == 1: print(arr[0])
else :
    if mode[0][1] == mode[1][1]: print(mode[1][0])
    else: print(mode[0][0])

print(arr[-1]-arr[0])