"""
알고리즘 수업 - 피보나치 수 1
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	14010	8091	7188	59.122%
문제
오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드는 다음과 같다.

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
입력
첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.

출력
코드1 코드2 실행 횟수를 한 줄에 출력한다.

예제 입력 1 
5
예제 출력 1 
5 3
예제 입력 2 
30
예제 출력 2 
832040 28
"""

# def fib(n):
#   for i in range(2, n): 
#     arr.append(arr[i - 1] + arr[i - 2])
#   return arr[i]

# n = int(input())
# arr = [1, 1]

# print(fib(n), n - 2)


# 복습 - DP
import sys
input = sys.stdin.readline

def fib1(n):
  global f1

  if n == 1 or n == 2: 
    f1 += 1
    return 1
  else: return fib1(n - 1) + fib1(n - 2)

def fib2(n):
  global f2

  for i in range(2, n):
    li.append(li[i - 1] + li[i - 2])
    f2 += 1
  return li[i]

n = int(input())
li = [1, 1]
f1, f2 = 0, 0
fib1(n)
fib2(n)

print(f1, f2)