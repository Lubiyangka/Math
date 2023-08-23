import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import plotly.graph_objects as go

node_list = pd.read_csv('附件1.csv', encoding='gbk')
node_code = node_list['节点编号']
node_x = np.array(node_list['X坐标（米）'])
node_y = np.array(node_list['Y坐标（米）'])
node_z = np.array(node_list['Z坐标（米）'])

node_r1 = np.sqrt(node_x ** 2 + node_y ** 2 + node_z ** 2)
R = np.average(node_r1)
F = 0.466 * R
tan_fai = 150 / ((math.sqrt(3) / 2 - 0.534) * R)
fai = math.atan(tan_fai)
node_seita = np.arccos(node_z / node_r1)

# 将零替换为自定义极小值
custom_epsilon = 1e-2
node_x[node_x == 0] = custom_epsilon

node_fai = np.arctan(node_y / node_x)

lenth = len(node_x)


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


G_line = []
for i in range(len(node_x) - 1):
    # print(i)
    G_line.append(distance(node_x[i], node_y[i], node_z[i], node_x[i + 1], node_y[i + 1], node_z[i + 1]))

for xi in np.arange(-0.6, 0.6, 0.01):
    for seita in np.arange(-0.5 / math.sqrt(fai), 0.5 / math.sqrt(fai), 0.01):
        node_r2 = (2 * F * np.cos(node_seita) + 2 * np.sqrt(
            F ** 2 * np.cos(node_seita) ** 2 + F * (R + seita + xi) * np.sin(node_seita) ** 2)) / np.sin(
            node_seita) ** 2

        node_x2 = node_r2 * np.sin(node_seita) * np.cos(node_fai)
        node_y2 = node_r2 * np.sin(node_seita) * np.sin(node_fai)
        node_z2 = node_r2 * np.cos(node_seita)
        G_line2 = []
        for i in range(len(node_x2) - 1):
            G_line2.append(distance(node_x2[i], node_y2[i], node_z2[i], node_x2[i + 1], node_y2[i + 1], node_z2[i + 1]))
        delta_r = np.absolute(node_r2 - node_r1)

        lam = np.array(G_line2) / np.array(G_line) - 1

        print(lam)
