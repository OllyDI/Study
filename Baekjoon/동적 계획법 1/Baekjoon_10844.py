"""
쉬운 계단 수
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	130621	41711	30264	30.247%
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
1
예제 출력 1 
9
예제 입력 2 
2
예제 출력 2 
17
"""

# n = int(input())

# arr = [[0] * 10 for _ in range(n)]
# for i in range(1, 10): arr[0][i] = 1

# for i in range(1, n):
#     for j in range(10):
#         if j == 0: arr[i][j] = arr[i - 1][1]
#         elif j == 9: arr[i][j] = arr[i - 1][8]
#         else: arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j + 1]
# print(sum(arr[n - 1]) % 1000000000)


#복습 - DP -> 문제 이해 안됨 나중에 다시보기
# https://www.youtube.com/watch?v=SPVOKqMDerQ
# 3월 18일 -> n 는 (n - 1) + (n + 1) 개수를 더해주면 구할 수 있음

import sys
input = sys.stdin.readline

n = int(input())
li = [[0] * 10 for _ in range(n)]
for i in range(1, 10): li[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            li[i][j] = li[i - 1][j + 1]
        elif j == 9:
            li[i][j] = li[i - 1][j - 1]
        else:
            li[i][j] = li[i - 1][j - 1] + li[i - 1][j + 1]
print(sum(li[n - 1]) % 1000000000)