"""
가장 긴 증가하는 부분 수열
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	142544	56583	37450	37.678%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
"""

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [1] * n

# for i in range(1, n):
#     for j in range(i):
#         if arr[i] > arr[j]: 
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))


# 복습 - DP
# 점화식 이해 필요 - i = 1 ~ n / 0 부터 i - 1번째 수를 비교해서 li[i]가 li[j]보다 크면 부분수열 가능 -> dp = dp[i]와 dp[j] + 1 중 큰 수를 삽입

import sys
input = sys.stdin.readline

a = int(input())
li = list(map(int, input().split()))
dp = [1] * a

for i in range(1, a):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))