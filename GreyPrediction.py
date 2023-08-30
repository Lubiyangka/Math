import numpy as np
import matplotlib.pyplot as plt


y_str = input('请输入数据，以空格分隔：')
y = np.array(y_str.split(), dtype=float)
n = len(y)
yy = np.ones(n)
yy[0] = y[0]
for i in range(1, n):
    yy[i] = yy[i - 1] + y[i]

B = np.ones((n - 1, 2))
for i in range(n - 1):
    B[i, 0] = -(yy[i] + yy[i + 1]) / 2
    B[i, 1] = 1

BT = B.T


YN = y[1:]

YNT = YN.T

A = np.linalg.inv(BT @ B) @ BT @ YNT
a = A[0]
b = A[1]
t = b / a
t_test = int(input('输入需要预测的个数'))
i = np.arange(1, t_test + n + 1)
yys = (y[0] - t) * np.exp(-a * i) + t  # 得出预测值
yys = np.insert(yys, 0, y[0])
ys = np.zeros(n + t_test)
for j in range(n + t_test - 1, 0, -1):
    ys[j] = yys[j] - yys[j - 1]
x = np.arange(1, n + 1)
xs = np.arange(2, n + t_test + 1)
yn = ys[1: n + t_test]
plt.plot(x, y, '^r', xs, yn, '*-b')
det = 0
for i in range(1, n):
    det += np.abs(yn[i] - y[i])

det /= n - 1
print("百分绝对误差为：", det, '%')
print("预测值为：", ys[n: n + t_test])

    # y_str = input('请输入数据，以空格分隔：')
    # y = np.array(y_str.split(), dtype=float)
    # n = len(y)
    # yy = np.ones(n)
    # yy[0] = y[0]
    # for i in range(1, n):
    #     yy[i] = yy[i - 1] + y[i]
    #
    # B = np.ones((n - 1, 2))
    # for i in range(n - 1):
    #     B[i, 0] = -(yy[i] + yy[i + 1]) / 2
    #     B[i, 1] = 1
    #
    # BT = B.T
    # YN = y[1:]
    # YNT = YN.T
    #
    # A = np.linalg.inv(BT @ B) @ BT @ YNT
    # a = A[0]
    # b = A[1]
    # t = b / a
    #
    # t_test = int(input('请输入需要预测的个数：'))
    # i = np.arange(1, t_test + n + 1)
    # yys = (y[0] - t) * np.exp(-a * i) + t
    # yys[0] = y[0]
    # ys = np.zeros(n + t_test + 1)
    # for j in range(n + t_test - 1, 2, -1):
    #     ys[j] = yys[j] - yys[j - 1]
    #
    # x = np.arange(1, n + 1)
    # xs = np.arange(2, n + t_test + 1)
    # yn = ys[1: n + t_test]
    #
    # plt.plot(x, y, '^r', xs, yn, '*-b')
    #
    # det = 0
    # for i in range(1, n):
    #     det += np.abs(yn[i] - y[i])
    # print('百分绝对误差为：', det, '%')
    # print('预测值为：', ys[n + 1:n + t_test + 1])
    #
    # plt.show()
