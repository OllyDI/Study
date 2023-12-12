"""
Bookshelf 2 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	453	198	157	46.176%
문제
Farmer John recently bought another bookshelf for the cow library, but the shelf is getting filled up quite quickly, and now the only available space is at the top.

FJ has N cows (1 <= N <= 20) each with some height of H_i (1 <= H_i <= 1,000,000 - these are very tall cows). The bookshelf has a height of B (1 <= B <= S, where S is the sum of the heights of all cows).

To reach the top of the bookshelf, one or more of the cows can stand on top of each other in a stack, so that their total height is the sum of each of their individual heights. This total height must be no less than the height of the bookshelf in order for the cows to reach the top.

Since a taller stack of cows than necessary can be dangerous, your job is to find the set of cows that produces a stack of the smallest height possible such that the stack can reach the bookshelf. Your program should print the minimal 'excess' height between the optimal stack of cows and the bookshelf.

입력
Line 1: Two space-separated integers: N and B
Lines 2..N+1: Line i+1 contains a single integer: H_i
 

출력
Line 1: A single integer representing the (non-negative) difference between the total height of the optimal set of cows and the height of the shelf.
 

예제 입력 1 
5 16
3
1
3
5
6
예제 출력 1 
1
힌트
Here we use cows 1, 3, 4, and 5, for a total height of 3 + 3 + 5 + 6 = 17. It is not possible to obtain a total height of 16, so the answer is 1.
"""

# 시간 초과
# import sys
# input = sys.stdin.readline

# n, b = map(int, input().split())
# cows = [int(input()) for _ in range(n)]
# visited = [False] * n
# res = 10000000000001

# def dfs(idx, s):
#     global res

#     if s >= b:
#         if res > s: res = s
#         return
#     if idx >= n: return

#     for i in range(n):
#         if visited[i] == False:
#             visited[i] = True
#             dfs(idx + 1, s + cows[i])
#             visited[i] = False

# dfs(0, 0)
# print(res - b)


# from itertools import combinations
# import sys
# input = sys.stdin.readline

# n, b = map(int, input().split())
# cows = [int(input()) for _ in range(n)]
# res = 10000000000001

# for i in range(1, n + 1):
#     for j in combinations(cows, i):
#         s = sum(j)
#         if s >= b: res = min(res, s)
# print(res - b)


import sys
input = sys.stdin.readline

n, b = map(int, input().split())
cows = [int(input()) for _ in range(n)]
res = 10000000000001

def dfs(idx, s):
    global res

    if s >= b:
        if res > s: res = s
        return
    if idx >= n: return

    dfs(idx + 1, s)
    dfs(idx + 1, s + cows[idx])

dfs(0, 0)
print(res - b)