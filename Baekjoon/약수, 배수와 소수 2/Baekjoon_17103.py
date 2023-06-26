"""
골드바흐 파티션
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	14847	5852	4430	37.530%
문제
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

입력
첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

출력
각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

예제 입력 1 
5
6
8
10
12
100
예제 출력 1 
1
1
2
1
6
"""

import math

def isPrime(num):
    arr = [True for _ in range(num + 1)]

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(num) + 1)):     
        if arr[i]:
            for j in range(i + i, num + 1, i): arr[j] = False
    return arr

t = int(input())
n = [int(input()) for _ in range(t)]
prime = isPrime(max(n))

print(prime)
for i in n:
    cnt = 0

    for j in range(2, (i//2) + 1):
        if prime[j] and prime[i - j]: cnt += 1
    print(cnt)