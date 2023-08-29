import cvxpy as cp

# 定义问题的变量和目标函数数量
num_variables = 2
num_objectives = 2

# 定义变量
variables = cp.Variable((num_variables,))

# 定义目标函数系数
objective_coefficients = [
    [70, 0],  # 甲种产品的利润系数
    [0, 120]  # 乙种产品的利润系数
]

# 定义目标函数
objective_functions = [
    cp.sum(cp.multiply(objective_coefficients[i], variables)) for i in range(num_objectives)
]

# 定义约束条件
constraints = [
    cp.multiply(4 * variables[0] + 5 * variables[1], 1) <= 2000,  # 原材料消耗约束
    cp.multiply(3 * variables[0] + 10 * variables[1], 1) <= 3000,  # 设备占用约束
]

# 定义软限制惩罚项
penalty = 1000  # 惩罚项权重
soft_constraints = [
    cp.pos(200-variables[0]),  # >=0
    cp.pos(variables[1]-250),
    cp.pos(9*variables[0]+4*variables[1]-3600),
   cp.abs(70*variables[0]+120*variables[1]-50000)
]

# 定义目标规划问题
problem = cp.Problem(
    cp.Maximize(cp.sum(objective_functions) - penalty * cp.sum(soft_constraints)),
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
