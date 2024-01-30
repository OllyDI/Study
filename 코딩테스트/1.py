"""
문제 설명
NX N 크기의 정사각형 격자로 이루어진 도시가 있습니다. 도시에는 서로 다른 격자 칸에 버스 정류 장이 있습니다. 이때, 도시의 모든 격자 칸에 대해 가장 가까운 정류장과의 거리를 계산하려 합니다.
각 칸에서는 상, 하, 좌, 우로만 움직일 수 있으며, 한 칸 이동하는데 거리 1로 계산합니다.
다음은 N = 3이고, 1행 2열에 정류장 한 개가 있는 예시입니다.(정류장이 있는 위치에서는 정류정과의 거리가 0입니다)
도시의 크기 N, 정류장의 위치 정보 bus_stop이 매개변수로 주어질 때, 도시 내 모든 위치에 대해 가 장 가까운 정류장과의 거리를 구해 N x N 크기의 2차원 배열에 담아 return 하도록 solution 함수를 완성해주세요.
제한사항
• N은 1 이상 600 이하의 정수입니다.
• bus._stop은 2차원 배열로, 행 길이는 1 이상 N2 이하이며 열 길이는 항상 2 입니다.
• bus_stop의 각 행은 버스 정류장의 위치가 [행 번호, 열 번호] 순으로 들어있습니다.
• 동일한 버스 정류장 위치가 중복해 주어지지 않습니다.
• 버스 정류장의 행 번호, 열 번호는 1 이상 N 이하의 자연수로만 이루어져 있습니다.
"""

from collections import deque

def bfs(start, distances, N):
    queue = deque([(start[0], start[1], 0)])  # 시작 위치와 거리를 큐에 추가
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 기록하는 배열

    while queue:
        row, col, current_distance = queue.popleft()

        # 방문하지 않았다면 현재 거리를 distances에 갱신하고, 방문 표시 후 인접한 위치를 큐에 추가
        if not visited[row][col]:
            visited[row][col] = True
            distances[row][col] = min(distances[row][col], current_distance)

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    queue.append((nr, nc, current_distance + 1))

# 주어진 위치에서 모든 위치까지의 최단 거리를 BFS로 계산
def solution(N, bus_stop):
    distances = [[float('inf')] * N for _ in range(N)]

    for stop in bus_stop:
        bfs((stop[0] - 1, stop[1] - 1, 0), distances, N)

    return distances

# 예시
N = 3
bus_stop = [[1, 2], [3, 3]]
print(solution(N, bus_stop))