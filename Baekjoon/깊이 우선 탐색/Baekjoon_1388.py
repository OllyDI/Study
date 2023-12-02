"""
바닥 장식
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	6584	4224	3469	67.438%
문제
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. 둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. N과 M은 50 이하인 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
4 4
----
----
----
----
예제 출력 1 
4
예제 입력 2 
6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-
예제 출력 2 
31
예제 입력 3 
7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------
예제 출력 3 
13
예제 입력 4 
10 10
||-||-|||-
||--||||||
-|-|||||||
-|-||-||-|
||--|-||||
||||||-||-
|-||||||||
||||||||||
||---|--||
-||-||||||
예제 출력 4 
41
예제 입력 5 
6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-
예제 출력 5 
19
"""

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [input().rstrip() for _ in range(n)]
# visit = [list(True for _ in range(m)) for _ in range(n)]
# res = 0

# def dfs(i, j):
#     global res
    
#     visit[i][j] = False

#     if arr[i][j] == "-":
#         if j + 1 < m and arr[i][j + 1] == "-" and visit[i][j + 1]:
#             dfs(i, j + 1)
#     elif arr[i][j] == "|":
#         if i + 1 < n and arr[i + 1][j] == "|" and visit[i + 1][j]:
#             dfs(i + 1, j)
 
# for i in range(n):
#     for j in range(m):
#         if visit[i][j]: 
#             dfs(i, j)
#             res += 1
# print(res)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
res = 0

def dfs(i, j):
    global res
    
    if arr[i][j] == "-":
        if j + 1 < m and arr[i][j + 1] == "-":
            dfs(i, j + 1)
    elif arr[i][j] == "|":
        if i + 1 < n and arr[i + 1][j] == "|":
            dfs(i + 1, j)
            
    arr[i][j] = "1"

for i in range(n):
    for j in range(m):
        if arr[i][j] == "-" or arr[i][j] == "|": 
            dfs(i, j)
            res += 1
print(res)