n = int(input())

time, price = [0 for i in range(n + 1)], [0 for i in range(n + 1)]

for i in range(n):
    t, p = map(int, input().split())
    time[i], price[i] = t, p
 
mPrice = [0 for i in range(n + 1)]
 
for i in range(len(time) - 2, -1, -1) :
    if time[i] + i <= n : mPrice[i] = max(price[i] + mPrice[i + time[i]], mPrice[i + 1])   
    else : mPrice[i] = mPrice[i + 1]

print(mPrice[0])