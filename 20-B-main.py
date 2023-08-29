from danamic import shortest_path

length_graph = {
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
special_graph = {
    '1': {'15': 1, '12': 1, '27': 1},
    '12': {'15': 1, '27': 1},
    '15': {'27': 1},
    '27': {}
}
weight = {'water': 2, 'food': 3}
value = {'water': 10, 'food': 5}
consumption = {
    'normal': {'water': 7, 'food': 5},
    'high_temp': {'water': 6, 'food': 8},
    'sandstorm': {'water': 10, 'food': 10},
}
weight_graph = {
    '1': {'15': weight, '12': weight, '27': weight},
    '12': {'15': weight, '27': weight},
    '15': {'27': weight},
    '27': {}
}
value_graph = {
    '1': {'15': value, '12': value, '27': value},
    '12': {'15': value, '27': value},
    '15': {'27': value},
    '27': {}
}
weather = [1, 1, 0, 2, 0, 1, 2, 0, 1, 1, 2, 1, 0, 1, 1, 1, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 0, 0, 1, 1]
consumption_graph = value_graph
special_path = {}
count = 0
for start_node, connections in special_graph.items():
    tmp, special_path[start_node] = shortest_path(length_graph, start_node, '27')
    for end_node, distance in connections.items():
        special_graph[start_node][end_node] = tmp[end_node]
        consumption_graph[start_node][end_node] = consumption['normal']
        count += 1
print(special_graph)
print(special_path)
print(consumption_graph)
