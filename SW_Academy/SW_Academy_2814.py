T = int(input())

def dfs(index, length) :
    global val
    if length > val : val = length
    check[index] = 1
    for i in range(len(graph[index])) :
        if not check[graph[index][i]]: dfs(graph[index][i], length + 1)
    check[index] = 0

for test_case in range(1, T + 1):
    vertex, edge = map(int, input().split())
    graph = [[] for _ in range(vertex + 1)]
    check = [0 for _ in range(vertex + 1)]
    val = 0
    
    for _ in range(edge) :
        vStart, vEnd = map(int, input().split())
        graph[vStart].append(vEnd)
        graph[vEnd].append(vStart)

    for i in range(1, vertex + 1) : dfs(i, 1)
    print("#{} {}".format(test_case, val))