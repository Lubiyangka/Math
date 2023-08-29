import numpy as np
'''测试数据'''
'''
# 定义图的数据结构
graph = {
    '1': {'2': 1, '25': 1},
    '2': {'3': 1},
    '3': {'4': 1, '25': 1},
    '4': {'24': 1, '5': 1},
    '5': {'24': 1, '6': 1},
    '6': {'24': 1, '23': 1, '7': 1},
    '7': {'22': 1, '8': 1},
    '8': {'22': 1, '9': 1},
    '9': {'22': 1, '17': 1, '15': 1, '10': 1},
    '10': {'11': 1, '15': 1, '13': 1},
    '11': {'13': 1, '12': 1},
    '12': {'13': 1, '14': 1},
    '13': {'15': 1, '14': 1},
    '14': {'15': 1, '16': 1},
    '15': {'16': 1},
    '16': {'17': 1, '18': 1},
    '17': {'18': 1, '21': 1},
    '18': {'20': 1, '19': 1},
    '19': {'20': 1},
    '20': {'21': 1},
    '21': {'22': 1, '23': 1, '27': 1},
    '22': {'23': 1},
    '23': {'24': 1, '26': 1},
    '24': {'25': 1, '26': 1},
    '25': {'26': 1},
    '26': {'27': 1},
    '27': {}
}

# 定义起点和终点
start_node = '1'
end_node = '15'
path = []
'''


def shortest_path(graph, start_node, end_node):
    # 初始化最短路径字典和已经访问的节点集合
    shortest_distance = {}
    visited_nodes = set()
    front = {}
    path = []
    # 初始化最短路径字典，起点到自己的距离为0，其余节点的距离为无穷大
    for node in graph:
        shortest_distance[node] = np.inf
    shortest_distance[start_node] = 0

    # 开始遍历所有节点，求解最短路径
    while len(visited_nodes) != len(graph):
        # 选择当前未访问节点中距离起点最近的节点
        current_node = None
        for node in graph:
            if node not in visited_nodes:
                if current_node is None:
                    current_node = node
                elif shortest_distance[node] < shortest_distance[current_node]:
                    current_node = node

        # 遍历当前节点的邻居节点，更新最短路径
        for neighbor_node, distance in graph[current_node].items():
            if neighbor_node not in visited_nodes:
                tentative_distance = shortest_distance[current_node] + distance
                if tentative_distance < shortest_distance[neighbor_node]:
                    shortest_distance[neighbor_node] = tentative_distance
                    front[neighbor_node] = current_node
        # 将当前节点标记为已访问
        visited_nodes.add(current_node)
    a = end_node
    cnt = 0
    while a != start_node:
        cnt += 1
        path.insert((cnt + 1), a)
        a = front[a]
    path.insert((cnt + 2), a)

    # 结果输出
    print("节点{}到节点{}的最短路长:{}".format(start_node, end_node, shortest_distance[end_node]), end="路径为：")
    for i in range(len(path) - 1, -1, -1):
        if i == 0:
            print(path[i], end="\n")
        else:
            print(path[i], end="->")
    # 返回起点到终点的最短路径距离
    return shortest_distance, path

# 测试数据
# shortest_distance = shortest_path(graph, start_node, end_node)  # 求解最短路径
