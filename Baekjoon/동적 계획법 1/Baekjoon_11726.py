"""
2×n 타일링
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	155375	59908	44373	36.480%
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
9
예제 출력 2 
55
"""

# import sys
# input = sys.stdin.readline

# n = int(input())
# num1 = 1
# num2 = 2
# res = 0

# if n == 1: print(num1)
# elif n == 2: print(num2)
# else:
#     for i in range(2, n):
#         res = num1 + num2
#         num1 = num2
#         num2 = res
#     print(res % 10007)

# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [0, 1, 2]

# for i in range(3, n + 1): dp.append(dp[i - 1] + dp[i - 2])
# print(dp[n] % 10007)


# 복습 문제를 n = 1 부터 풀어서 보면 dp[n] = dp[n - 1] + dp[n - 2]가 됨

import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 2]

for i in range(3, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[n] % 10007)