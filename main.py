import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

node_list = pd.read_csv('附件1.csv', encoding='gbk')
node_code = node_list['节点编号']
node_x = np.array(node_list['X坐标（米）'])
node_y = np.array(node_list['Y坐标（米）'])
node_z = np.array(node_list['Z坐标（米）'])

actuator_list = pd.read_csv('附件2.csv', encoding='gbk')
actuator_codegit = actuator_list['对应主索节点编号']
actuator_x_up = np.array(actuator_list['基准态时上端点X坐标（米）'])
actuator_y_up = np.array(actuator_list['基准态时上端点Y坐标（米）'])
actuator_z_up = np.array(actuator_list['基准态时上端点Z坐标（米）'])

actuator_x_down = np.array(actuator_list['下端点X坐标（米）'])
actuator_y_down = np.array(actuator_list['下端点Y坐标（米）'])
actuator_z_down = np.array(actuator_list['下端点Z坐标（米）'])

fig = plt.figure(figsize=(30,30))
ax = plt.axes(projection='3d')
ax.scatter(node_x, node_y, node_z, c=node_z, cmap='viridis', marker='.')
ax.scatter(actuator_x_up, actuator_y_up, actuator_z_up, c=actuator_z_up, cmap='cool', marker='^')
ax.scatter(actuator_x_down, actuator_y_down, actuator_z_down, c=actuator_z_down, cmap='spring', marker=',')

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.view_init(180, 0)
ax.mouse_init()
plt.show()

# new author
for i in range(5):
  print(i)
