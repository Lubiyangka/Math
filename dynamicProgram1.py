import numpy as np

qua = np.array((0, 1, 2, 3))  # 4种类型的特殊点：0-> 起点； 1-> 村庄；2 ->矿山; 3-> 终点
dist = np.array(((0, 6, 8, 3), # 表示4个特殊点之间的距离
                 (6, 0, 2, 3),
                 (8, 2, 0, 5),
                 (3, 3, 5, 0)))
f = np.array(((0, 1, 1, 1),  # 判断4中特殊点之间的关系，是否直达
              (0, 0, 1, 1),
              (0, 1, 0, 1),
              (0, 0, 0, 0)))
wea = np.array((2, 2, 1, 3, 1,  # 30天内的天气
                2, 3, 1, 2, 2,
                3, 2, 1, 2, 2,
                2, 3, 3, 2, 2,
                1, 1, 2, 1, 3,
                2, 1, 1, 2, 2))
mx, my = 3, 2  # 水和食物的重量
cx, cy = 5, 10  # 水和食物的价格
sx = np.array((0, 5, 8, 10))  # 第i种天气的水消耗量
sy = np.array((0, 7, 6, 10))  # 第i种天气的食物消耗量

n = 4  # 特殊点个数

maxm = 1200  # 背包容量
coins = 10000  # 初始资金
base = 1000  # 基础收益
date = 30  # 最晚期限
costx = np.zeros((32, 4, 4))  # 第k天从i到j的水消耗量
costy = np.zeros((32, 4, 4))  # 第k天从i到j的事食物消耗量
days = np.zeros((32, 4, 4), dtype=int)  # 第k天从i到j需要多长时间
ans = 0  # 最后的资金
act = np.empty(32)  # 每天的行为：2-> 挖矿；1-> 在矿山休息；0-> 村庄购买食物
rec = np.empty(32)  # 记录每天在哪里

# ansx、ansact记录最优路径上的信息
ansx = np.empty(32)
ansact = np.empty(32)
ansg, ansh = 0, 0  # 记录最优的初始水和食物


def dfs(day: int, now: int, nm: int, c: int, x: int, y: int, type: int) -> None:
    # dfs是一个深度优先搜索函数的定义，它接受七个参数：当天日期(day，整数类型)、当
    # 前所在位置(now，整数类型)、剩余物品重量(nm，整数类型)、剩余资金(c，整数类型)、剩余
    # 水量(x，整数类型)、剩余食物量(y，整数类型)和行为类型(type，整数类型)。该函数不返回任何结果（None类型）。
    act[day] = type
    rec[day] = now
    global ans, ansg, ansh # 声明为全局变量，用于保存最优结果

    if qua[now] == 3: # 如果到了终点
        if ans <= c+x*cx+y*cy: # 剩余资金和剩余食物和水的价值比已经记录的最优结果还要高
            ansg = g
            ansh = h
            ans = c+x*cx+y*cy # 保存最优解的相关数据
            for i in range(date+1):
                ansx[i] = rec[i]
                ansact[i] = act[i] # 记录最优解的行为和路径
        act[day] = -1   # act[day] = -1：将当前日期的行为类型重置为-1。
        rec[day] = -1   # 将当前日期的所在位置重置为-1。
        return

    if day >= date: # 达到最晚期限
        act[day] = -1
        rec[day] = -1
        return

    if qua[now] == 1: # 如果当前位置为村庄
        nm = maxm - mx*x - my*y # 计算剩余可盛物品的质量

    for i in range(n):
        if f[qua[now]][qua[i]]: # f用于表示两个位置之间是否是可达的
            tx = costx[day][now][i]
            ty = costy[day][now][i] # 计算购买物品所需的代价：tx表示购买水的数量，ty表示购买食物的数量。
            ucost = c
            um =nm # 计算更新后的成本和剩余物品重量：ucost为更新后的总成本，um为更新后的剩余物品重量。
            if x >= tx:
                ux = x - tx
            else:
                ux = 0
                ucost -= 2*(tx-x)*cx
                um -= (tx - x)*mx
            if y >= ty:
                uy = y - ty
            else:
                uy = 0
                ucost -= 2*(ty - y)*cy
                um -= (ty - y)*my
            # 计算执行后剩余的参数值

            if ucost < 0 or um < 0:
                continue
            dfs(day+days[day][now][i], i, um, ucost, ux, uy, 0) # type=0表示在村庄购买食物

    if qua[now] == 2: # 如果位置为矿山
        attday = day
        tx = sx[wea[attday]]
        ty = sy[wea[attday]]
        attday += 1
        if x > tx:
            x -= tx
            tx = 0
        else:
            tx = tx - x
            x = 0
        if y >= ty:
            y -= ty
            ty = 0
        else:
            ty = ty - y
            y = 0
        # 计算剩余的资源量
        nm -= tx*mx + ty*my # 剩余可承载质量减去消耗量
        c -= 2*tx*cx + 2*ty*cy #剩余的金钱
        if nm >= 0 and c >= 0:
            dfs(attday, now, nm, c, x, y, 1) # 在矿山休息type =1

        attday = day
        tx = sx[wea[attday]]*2
        ty = sy[wea[attday]]*2
        attday += 1
        if x >= tx:
            x -= tx
            tx = 0
        else:
            tx = tx - x
            x = 0
        if y >= ty:
            y -= ty
            ty = 0
        else:
            ty = ty -y
            y = 0
        nm -= tx*mx + ty*my
        c -= 2*tx*cx + 2*ty*cy
        c += base
        if nm >= 0 and c >= 0:
            dfs(attday, now, nm, c, x, y, 2) # type=2表示在矿山挖矿个

    rec[day] = -1
    act[day] = -1

if __name__ == '__main__':
    for d in range(date+1):
        rec[d] = -1
        act[d] = -1
    # 进行每天数据的初始化

    for d in range(date): #遍历日期路径
        for i in range(n): #遍历所有可能的起始位置
            for j in range(n): # 遍历所有可能的目标位置
                if f[qua[i]][qua[j]]: # 如果是可到达的
                    now, count, sumx, sumy = 0, 0, 0, 0 #初始化
                    while count < dist[i][j]:
                        if wea[now+d] != 3:
                            count += 1
                            sumx += 2*sx[wea[now+d]]
                            sumy += 2*sy[wea[now+d]]
                        else:
                            sumx += sx[wea[now+d]]
                            sumy += sy[wea[now+d]]
                        # 存储第d天从i到j的消耗

                        now += 1
                        if now + d >= date:
                            break
                    if count < dist[i][j]:
                        sumx = sumy = 20000
                        now = 30
                    # 如果计数器仍然小于起始位置到目标位置的距离，说明无法在规定日期内到达目标位置。
                    # 将总水量和总食物量置为一个很大的值（20000）。
                    # 将当前位置设置为一个足够大的值（30）。
                    costx[d][i][j] = sumx
                    costy[d][i][j] = sumy
                    days[d][i][j] = now
    print(type(days[0,0,0]))

    dic = {} # 创建一个空字典，用于记录已经搜索过的组合。
    for i in range(maxm+1): # 遍历所有可能的最大质量
        g = i // mx # 计算最大购买水的数量
        h = (maxm-i)//my # 计算最大购买食物的数量
        # print(g, h)
        dic.setdefault((g,h), 0) # dic.setdefault((g,h), 0)：将(g,h)作为键加入字典dic，如果该键不存在则将其对应的值初始化为0。
        if not dic[(g,h)]: # 如果没有标记那么说明该未进行搜索，就调用dfs进行搜索
            print((g,h))
            dfs(0, 0, 0, coins-g*cx-h*cy, g, h, -1)
        dic[(g, h)] = 1

    print(ans)

