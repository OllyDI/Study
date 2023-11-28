"""
로마 숫자 만들기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	5667	3143	2508	54.380%
문제
로마 숫자에서는 수를 나타내기 위해서 I, V, X, L을 사용한다. 각 문자는 1, 5, 10, 50을 의미하고, 이 문제에서 다른 문자는 사용하지 않는다.

하나 또는 그 이상의 문자를 이용해서 수를 나타낼 수 있다. 문자열이 나타내는 값은, 각 문자가 의미하는 수를 모두 합한 값이다. 예를 들어, XXXV는 35, IXI는 12를 의미한다.

실제 로마 숫자에서는 문자의 순서가 중요하지만, 이 문제에서는 순서는 신경쓰지 않는다. 예를 들어, 실제 로마 숫자에서 IX는 9를 의미하지만, 이 문제에서는 11을 의미한다.

로마 숫자를 N개 사용해서 만들 수 있는 서로 다른 수의 개수를 구해보자.

입력
첫째 줄에 사용할 수 있는 문자의 개수 N (1 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 로마 숫자 N개를 사용해서 만들 수 있는 서로 다른 수의 개수를 출력한다.

예제 입력 1 
1
예제 출력 1 
4
I, V, X, L을 만들 수 있다.

예제 입력 2 
2
예제 출력 2 
10
2, 6, 10, 11, 15, 20, 51, 55, 60, 100을 만들 수 있다.

예제 입력 3 
10
예제 출력 3 
244
"""

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [1, 5, 10, 50]
# li = []
# res = set()

# def dfs(depth, n, idx):
#     if depth == n:
#         res.add(sum(li))
#         return
#     else:
#         for i in range(idx, 4):
#             li.append(arr[i])
#             dfs(depth + 1, n, i)
#             li.pop()

# dfs(0, n, 0)
# print(len(res))

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n = int(input())
arr = [1, 5, 10, 50]
res = set()

for i in combinations_with_replacement(arr, n): res.add(sum(i))
print(len(res))