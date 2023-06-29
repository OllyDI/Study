"""
이항 계수 1
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	51923	33618	29057	64.677%
문제
자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
\(N\)과 
\(K\)가 주어진다. (1 ≤ 
\(N\) ≤ 10, 0 ≤ 
\(K\) ≤ 
\(N\))

출력
 
\(\binom{N}{K}\)를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
"""

def factorial(num):
    if num == 0 or num == 1: return 1
    else: return num * factorial(num - 1)

n, k = map(int, input().split())
print(int(factorial(n)/(factorial(n - k) * factorial(k))))