"""
N과 M (9)
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	37067	18472	14000	49.364%
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
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
1 7
1 9
7 1
7 9
9 1
9 7
9 9
예제 입력 3 
4 4
1 1 1 1
예제 출력 3 
1 1 1 1
"""

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# visited = [False] * n
# stack = []
# res = []

# def backtracking():
#     if len(stack) == m:
#         res.append(tuple(stack))
#         return
    
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             stack.append(arr[i])
#             backtracking()
#             visited[i] = False
#             stack.pop() 

# backtracking()
# for i in sorted(list(set(res))): print(*i)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
stack = []

def backtracking():
    if len(stack) == m:
        print(*stack)
        return
    
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp != arr[i]:
            visited[i] = True
            stack.append(arr[i])
            tmp = arr[i]
            backtracking()
            visited[i] = False
            stack.pop() 

backtracking()