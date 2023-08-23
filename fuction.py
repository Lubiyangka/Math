import sympy

# 定义变量
r, theta, F_0, R, xi = sympy.symbols('r theta F_0 R xi')

# 定义方程
equation = (r * sympy.sin(theta)) ** 2 - 4 * F_0 * sympy.cos(theta) * r - 4 * F_0 * (R+xi)

# 解方程
solutions = sympy.solve(equation, r)
print(sympy.latex(solutions))