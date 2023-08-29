import cvxpy as cp

# 定义问题的变量和目标函数数量
num_variables = 2
num_objectives = 2

# 定义变量
variables = cp.Variable((num_variables,))

# 定义目标函数
objective_functions = [
    0.6 * variables[0] + 0.7 * variables[1],  # 目标函数1：甲种产品的利润
    -(0.001 * variables[0]**2 + 0.002 * variables[1]**2 )  # 目标函数2：负向化成本
]

# 定义约束条件
constraints = [
    variables[0] + variables[1] == 1000,  # 原材料消耗约束
    variables[0] >= variables[1]  # 设备占用约束
]

# 定义目标规划问题
problem = cp.Problem(
    cp.Maximize(cp.sum(objective_functions)),
    constraints
)

# 求解目标规划问题
problem.solve()

# 输出结果
if problem.status == "optimal":
    print("Optimal solution found")
    print("Objective values:")
    for i in range(num_objectives):
        print("Objective", i+1, "Value:", objective_functions[i].value)
    print("Variables:")
    print(variables.value)
else:
    print("Optimal solution not found")
