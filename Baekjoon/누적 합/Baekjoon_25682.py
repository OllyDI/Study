"""
체스판 다시 칠하기 2
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	4821	1927	1434	39.439%
문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

제한
1 ≤ N, M ≤ 2000
1 ≤ K ≤ min(N, M)
예제 입력 1 
4 4 3
BBBB
BBBB
BBBW
BBWB
예제 출력 1 
2
예제 입력 2 
8 8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
예제 출력 2 
1
예제 입력 3 
10 13 10
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
예제 출력 3 
30
예제 입력 4 
9 23 9
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBWWWWWWWW
예제 출력 4 
40
"""

import sys
input = sys.stdin.readline

# 시간 초과
# n, m, k = map(int, input().split())
# arr = list(list(input().rstrip()) for _ in range(n))
# res = []

# for i in range(n - k + 1):
#     for j in range(m - k + 1):
#         black, white = 0, 0
#         for a in range(i, i + k):
#             for b in range(j, j + k):
#                 if (a + b) % 2 == 0:
#                     if arr[a][b] == "B": black += 1
#                     if arr[a][b] == "W": white += 1
#                 else:
#                     if arr[a][b] == "W": black += 1
#                     if arr[a][b] == "B": white += 1 
#         res.append(black)
#         res.append(white)

# print(min(res))

# 정답
n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
res = []

for color in ["B", "W"]:
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                if arr[i][j] == color: val = 1
                else: val = 0
            else:
                if arr[i][j] == color: val = 0
                else: val = 1
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + val

    temp =  4000000
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            temp = min(temp, dp[i + k - 1][j + k - 1] - dp[i + k - 1][j - 1] - dp[i - 1][j + k - 1] + dp[i - 1][j - 1])
    res.append(temp)
            
print(min(res))