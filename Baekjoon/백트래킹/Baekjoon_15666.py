"""
N과 M (12)
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	17386	13863	12026	80.852%
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4
예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 1
1 7
1 9
7 7
7 9
9 9
예제 입력 3 
4 4
1 1 2 2
예제 출력 3 
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2
"""

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# stack = []

# def backtracking(depth):
#     if len(stack) == m:
#         print(*stack)
#         return
    
#     tmp = 0
#     for i in range(depth, n):
#         if tmp != arr[i]:
#             tmp = arr[i]
#             stack.append(arr[i])
#             backtracking(i)
#             stack.pop()

# backtracking(0)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []
res = []

def backtracking(depth):
    if len(stack) == m:
        res.append(tuple(stack))
        return
    
    tmp = 0
    for i in range(depth, n):
        if tmp != arr[i]:
            tmp = arr[i]
            stack.append(arr[i])
            backtracking(i)
            stack.pop()

backtracking(0)

for i in sorted(list(set(res))): print(*i)