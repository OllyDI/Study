"""
1로 만들기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.15 초 (하단 참고)	128 MB	265923	89259	57029	32.616%
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1 
2
예제 출력 1 
1
예제 입력 2 
10
예제 출력 2 
3
"""

# n = int(input())
# arr = [0] * (n + 1)

# for i in range(2, n + 1):
#     arr[i] = arr[i - 1] + 1

#     if i % 3 == 0: arr[i] = min(arr[i], arr[i // 3] + 1)
#     if i % 2 == 0: arr[i] = min(arr[i], arr[i // 2] + 1)
# print(arr[n])

# 복습

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n + 1

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + 1

    if i % 3 == 0: arr[i] = min(arr[i], arr[i // 3] + 1)
    if i % 2 == 0: arr[i] = min(arr[i], arr[i // 2] + 1)
print(arr[n])