"""
순서쌍의 곱의 합
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	256 MB	7751	2463	2013	33.472%
문제
N개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합을 구하라.

예를 들어 N = 3이고 주어진 정수가 2, 3, 4일 때, 두 수를 뽑는 모든 경우는 (2, 3), (2, 4), (3, 4)이며 이때 각각의 곱은 6, 8, 12이다. 따라서 총합은 26이다.

입력
첫 번째 줄에는 입력 받을 정수의 개수 N(2 ≤ N ≤ 100,000)

두 번째 줄에는 N 개의 정수가 주어진다. 이때 입력 받는 정수들의 범위는 0이상 10,000 이하이다.

출력
모든 경우의 곱의 합을 출력한다.

예제 입력 1 
3
2 3 4
예제 출력 1 
26
예제 입력 2 
4
1 2 3 4
예제 출력 2 
35
예제 입력 3 
4
2 3 2 4
예제 출력 3 
44
"""

# 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# res = 0

# for i in range(0, n - 1):
#     for j in range(i + 1, n):
#         res += (arr[i] * arr[j])
# print(res)



import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sums = sum(arr)
res = 0

for i in arr:
    sums -= i
    res += sums * i
print(res)