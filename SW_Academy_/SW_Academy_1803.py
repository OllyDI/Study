from heapq import heappush, heappop

T = int(input())

for test_case in range(1, T + 1):
    vertex, edge, start, end = map(int, input().split())
    graph = [[] for _ in range(vertex + 1)]
    distance = [float('inf')] * (vertex + 1)

    for _ in range(edge) :
        vStart, vEnd, weight = map(int, input().split())
        graph[vStart].append([vEnd, weight])
        graph[vEnd].append([vStart, weight])
 
    distance[start] = 0
    queue = []
    heappush(queue,[0,start])
    while queue :
        val = heappop(queue)[1]

        for v in graph[val] :
            if distance[val] + v[1] < distance[v[0]]:
                distance[v[0]] = distance[val] + v[1]
                heappush(queue,[distance[val] + v[1], v[0]])


    print("#{}".format(test_case), distance[end])