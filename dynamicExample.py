def dynamic_p() -> list:
    # 物品栏
    items = [
        {"name": "水", "weight": 3, "value": 10},
        {"name": "书", "weight": 1, "value": 3},
        {"name": "食物", "weight": 2, "value": 9},
        {"name": "小刀", "weight": 3, "value": 4},
        {"name": "衣服", "weight": 2, "value": 5},
        {"name": "手机", "weight": 1, "value": 10}
    ]
    # 约束条件
    max_capacity = 6
    dp = [[0] * (max_capacity + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items)+1):
        for j in range(1, max_capacity+1):
            weight = items[i-1]["weight"]
            value = items[i-1]["value"]
            if weight>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(value+dp[i-1][j-weight], dp[i-1][j])
    return dp


dp = dynamic_p()
for i in dp:
    print(i)
# 最优解
print(dp[-1][-1])