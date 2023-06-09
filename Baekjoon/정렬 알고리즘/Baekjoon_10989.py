import sys

n = int(input())
arr = [0] * 10000

for i in range(n): arr[int(input()) - 1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]) : sys.stdout.write(str(i + 1) + '\n')

# n = int(input())
# arr = []
# for i in range(n): arr.append(int(input()))

# cnt = [0] * (max(arr) + 1)
# for i in arr: cnt[i] += 1
# for i in range(1, len(cnt)): cnt[i] += cnt[i - 1]

# res = [0] * len(arr)

# for i in arr:
#     res[cnt[i] - 1] = i
#     cnt[i] -= 1

# for i in range(n): print(res[i])