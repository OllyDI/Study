n = int(input())
li = list(map(int, input().split()))
tmp = sorted(set(li))
dic = {}
for i in range(len(tmp)): dic[tmp[i]] = i
for i in li: print(dic[i], end=' ')