def floyd(graph):
    n = len(graph)  # 节点的数量

    # 初始化距离矩阵和路径矩阵
    dist = [[float('inf')] * n for _ in range(n)]
    path = [[-1] * n for _ in range(n)]
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


graph = [(1, 2, 1),
         (1, 25, 1),
         (2, 3, 1),
         (3, 4, 1),
         (4, 25, 1),
         (4, 5, 1),
         (4, 24, 1),
         (5, 6, 1),
         (24, 6, 1),
         (24, 26, 1),
         (24, 23, 1),
         (6, 23, 1),
         (6, 7, 1), 
         (7, 22, 1),
         (7, 8, 1),
         (8, 9, 1),
         (9, 10, 1),
         (26, 27, 1),
         (23, 21, 1),
         (27, 21, 1),
         (21, 20, 1),
         (20, 19, 1),
         (18, 19, 1),
         (20, 18, 1),
         (21, 22, 1),
         (9, 21, 1),
         (9, 17, 1),
         (9, 16, 1),
         (16, 18, 1),
         (17, 21, 1),
         (9, 15, 1),
         (10, 15, 1),
         (15, 16, 1),
         (16, 17, 1),
         (10, 11, 1),
         (11, 13, 1),
         (13, 15, 1),
         (14, 15, 1),
         (13, 14, 1),
         (14, 16, 1),
         (10, 13, 1),
         (11, 12, 1),
         (12, 13, 1),
         (12, 14, 1),
         (17, 18, 1),
         (3, 25, 1),
         (25, 26, 1),
         (24, 25, 1),
         (5, 24, 1),
         (8, 22, 1),
         (9, 22, 1),
         (22, 23, 1),
         (23, 26, 1)]

new_graph = graph.copy()  # 创建一个副本，避免在循环中修改列表

for i, j, k in graph:
    new_graph.append((j, i, k))

print(new_graph)
shortest_dists, shortest_paths = floyd(new_graph)

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
