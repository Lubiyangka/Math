def floyd(graph):
    n = len(graph)  # 节点的数量

    # 初始化距离矩阵和路径矩阵
    dist = [[float('inf')]*n for _ in range(n)]
    path = [[-1]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = w
        path[u][v] = u

    # 逐步更新距离矩阵和路径矩阵
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    return dist, path


# 测试
graph = [(0, 1, 3), (0, 2, 6), (1, 2, 2), (1, 3, 1), (2, 3, 1), (2, 4, 10), (3, 0, 1), (3, 4, 5), (4, 1, 4), (4, 3, 7)]
shortest_dists, shortest_paths = floyd(graph)

# 输出最短路径距离矩阵和具体路径
for i in range(len(shortest_dists)):
    for j in range(len(shortest_dists[i])):
        print(f"节点 {i} 到节点 {j} 的最短路径距离为 {shortest_dists[i][j]}")
        if shortest_dists[i][j] != float('inf'):
            path = []
            k = j
            while k != i:
                path.append(k)
                k = shortest_paths[i][k]
            path.append(i)
            path.reverse()
            print(f"节点 {i} 到节点 {j} 的最短路径为 {path}")
        print()
