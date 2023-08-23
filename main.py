import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize


def distance(args):
    GG = 0.0
    for i in range(len(args)):
        GG += np.square(args[i][1] - args[i][0])
    return np.sqrt(GG)


def _distance_():
    return


def _theta_(args):
    sum = 0
    for i in range(0, 3):
        sum += np.square(args[i])
    r_i = np.sqrt(sum)
    theta = np.arccos(args[2] / r_i)
    return theta, r_i


def _varphi_(args):
    return np.arctan(args[1]/args[0])


def _F_():
    return lambda x: F + x[0] + x[1]


def _r_():
    return


def fun(args):
    X, Y, Z = (args[i] for i in range(0, 3))
    GG_1 = distance(args)
    theta = _theta_(args[:, 0])[0]
    varphi = _varphi_(args[:, 0])
    v = lambda x: -(np.sqrt(np.square((2*((F+x[0]+x[1])*np.cos(theta)+np.sqrt(np.square((F+x[0]+x[1])*np.cos(theta))+(F+x[0]+x[1])*(R+x[0]+x[1])*np.square(np.sin(theta))))/np.square(np.sin(theta)))*np.sin(theta)*np.cos(varphi)-args[0][1])+np.square((2*((F+x[0]+x[1])*np.cos(theta)+np.sqrt(np.square((F+x[0]+x[1])*np.cos(theta))+(F+x[0]+x[1])*(R+x[0]+x[1])*np.square(np.sin(theta))))/np.square(np.sin(theta)))*np.sin(theta)*np.sin(varphi)-args[1][1])+np.square((2*((F+x[0]+x[1])*np.cos(theta)+np.sqrt(np.square((F+x[0]+x[1])*np.cos(theta))+(F+x[0]+x[1])*(R+x[0]+x[1])*np.square(np.sin(theta))))/np.square(np.sin(theta)))*np.cos(theta)-args[2][1]))/GG_1-1)
    return v


def con(args):
    theta, r_i = _theta_(args[:, 0])
    varphi = _varphi_(args[:, 0])
    cons = ({'type': 'ineq', 'fun': lambda x: -np.abs((2*((F+x[0]+x[1])*np.cos(theta)+np.sqrt(np.square((F+x[0]+x[1])*np.cos(theta))+(F+x[0]+x[1])*(R+x[0]+x[1])*np.square(np.sin(theta))))/np.square(np.sin(theta)))-r_i)+0.6})
    return cons


def solve(args):
    # args_s = np.array([[1, 4],
    #                    [1, 2],
    #                    [1, 3]])
    delta_lim = (np.sqrt(3)/2-0.534)*R/300
    bnds = ((-0.6, 0.6), (-delta_lim, delta_lim))
    x0 = np.asarray((0.5, 0.5))
    res = minimize(fun(args), x0, method='SLSQP', constraints=con(args), bounds=bnds)
    return -res.fun


node_list = pd.read_csv('附件1.csv', encoding='gbk')
node_code = node_list['节点编号']
node_x = np.array(node_list['X坐标（米）'])
node_y = np.array(node_list['Y坐标（米）'])
node_z = np.array(node_list['Z坐标（米）'])
node_r = np.sqrt(node_x**2+node_y**2+node_z**2)
# 将零替换为自定义极小值
custom_epsilon = 1
node_x[node_x == 0] = custom_epsilon
#
# fig = plt.figure(figsize=(30,30))
# ax = plt.axes(projection='3d')
# ax.scatter(node_x, node_y, node_z, c=node_z, cmap='viridis', marker='.')
#
# ax.set_zlabel('Z')
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# ax.view_init(180, 0)
# ax.mouse_init()
# plt.show()

R = np.average(node_r)
F = 0.466*R
Lambda = np.zeros(len(node_x))
for i in range(len(node_x)-1):
    args_s = np.array([[node_x[i], node_x[i + 1]],
                       [node_y[i], node_y[i + 1]],
                       [node_z[i], node_z[i + 1]]])
    Lambda[i] = solve(args_s)
result = np.min(Lambda)
