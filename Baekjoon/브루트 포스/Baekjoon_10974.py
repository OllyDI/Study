"""
모든 순열
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	28063	18027	13807	65.023%
문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

예제 입력 1 
3
예제 출력 1 
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

import sys
from itertools import permutations
input = sys.stdin.readline

# n = int(input())
# arr = [i for i in range(1, n + 1)]
# res = list(permutations(arr, n))

# for i in res: print(*i)


n = int(input())
arr = []

def dfs():
    if len(arr) == n:
        print(*arr)
        return
    else:
        for i in range(1, n + 1):
            if i not in arr:
                arr.append(i)
                dfs()
                arr.pop()
dfs()