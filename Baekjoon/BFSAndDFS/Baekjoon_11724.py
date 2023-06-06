"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.


입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.


예제 입력
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력
2

예제 입력
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력
1
"""

def dfs(tmaps, node) :
    for i in range(len(tmaps[node])) :
        if visited[tmaps[node][i] - 1] == False :
            visited[tmaps[node][i] - 1] = True
            dfs(tmaps, tmaps[node][i] - 1)

answer = 0
node, edge = map(int, input().split())
maps = [[] for _ in range(node)]
visited = [False for _ in range(node)]

for i in range(edge) :
    n, e = map(int, input().split())
    maps[n - 1].append(e)
    maps[e - 1].append(n)

for i in range(node) :
    if visited[i] == False :
        visited[i] = True
        dfs(maps, i)
        answer += 1

print(answer)