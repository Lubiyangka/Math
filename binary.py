import sympy as sp


def f(x):
    return (x - 45.32) ** 2 + 4


def search(left, right):
    while right - left >= 0.0001:
        middle = (left + right) / 2
        if f(middle-0.0001)<f(middle+0.0001):
            right = middle
        else:
            left = middle
    return left


print(search(30, 50))


# 打印导数计算结果
