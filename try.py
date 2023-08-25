import sympy as sp

# 定义符号变量
x = sp.symbols('x')

# 定义函数表达式
f = x**3 + 2*x**2 + x + 1

# 计算导数
df = sp.diff(f, x)

# 将数值代入导数计算结果
x_value = 2  # 给定的数值
df_value = df.subs(x, x_value)

# 打印导数计算结果
print("在 x = {} 时的导数值：".format(x_value), df_value)