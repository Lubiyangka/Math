def floyd(graph):
    n = len(graph)  # 节点的数量
    print(n)

    # 初始化距离矩阵
    dist = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = w

    # 逐步更新距离矩阵
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# 测试
graph = [(0, 1, 3), (0, 2, 6), (1, 2, 2), (1, 3, 1), (2, 3, 1), (2, 4, 10), (3, 0, 1), (3, 4, 5), (4, 1, 4), (4, 3, 7)]
shortest_paths = floyd(graph)

# 输出最短路径距离矩阵
for row in shortest_paths:
    print(row)