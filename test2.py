import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from scipy import integrate
import sympy as sp
import plotly.graph_objects as go

node_list = pd.read_csv("附件1.csv", encoding="gbk")
node_code = node_list["节点编号"]
node_x = np.array(node_list["X坐标（米）"])
node_y = np.array(node_list["Y坐标（米）"])
node_z = np.array(node_list["Z坐标（米）"])

node_r1 = np.sqrt(node_x**2 + node_y**2 + node_z**2)
R = np.average(node_r1)
F = 0.466 * R
fai = math.atan(150 / ((math.sqrt(3) / 2 - 0.534)) * R)


def func(L, w):
    return (
        -L * math.sin(w) ** 2
        + L
        * math.sqrt(math.sin(w) ** 2 + 2 * (math.cos(w) ** 2 * (0.5 * L + R - F) / L))
        / math.cos(w) ** 2
    )

up = math.pi/2-0.1
print(up)
def search(left, right):
    while right - left > 0.001:
        middle = (left + right) / 2
        L = middle-0.001
        result, _ = integrate.quad(
            lambda w: math.cos(w) * (func(L, w) - R) ** 2, up, math.pi / 2
        )
        print(result,L)
        L = middle+0.001
        Result, _ = integrate.quad(
            lambda w: math.cos(w) * (func(L, w) - R) ** 2, up, math.pi / 2
        )
        if result > Result:
            right = middle
        else:
            left = middle

    return (left + right) / 2

found_L = search(275, 285)
print("搜索到的参数 L 值为:", found_L)


