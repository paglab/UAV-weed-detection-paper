<<<<<<< HEAD
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 加载数据
data_path = r'C:\Users\38492\ultralytics\seg_evaluate\data2.txt'  # 替换为你的数据文件路径
data = pd.read_csv(data_path, delimiter='\t')

# 重命名列名以便访问
data.columns = ['Plot', 'Weed_control', 'Nitrogen', 'Potato_area', 'Weed_area', 'Yield']

# 对Potato_area和Weed_area进行回归分析
X = data[['Potato_area', 'Weed_area']]
y = data['Yield']
X = sm.add_constant(X)  # 添加常数项到自变量

model = sm.OLS(y, X).fit()
print(model.summary())

# 3D可视化回归结果
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(data['Potato_area'], data['Weed_area'], data['Yield'], c='blue', marker='o')

# 创建网格以绘制回归平面
x_surf, y_surf = np.meshgrid(np.linspace(data['Potato_area'].min(), data['Potato_area'].max(), 100),
                             np.linspace(data['Weed_area'].min(), data['Weed_area'].max(), 100))
z_surf = model.params[0] + model.params[1] * x_surf + model.params[2] * y_surf

# 绘制回归平面
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5, rstride=100, cstride=100)

# 设置轴标签
ax.set_xlabel('Potato Area')
ax.set_ylabel('Weed Area')
ax.set_zlabel('Yield (dt/ha)')

plt.title('3D Regression Analysis: Potato Area and Weed Area vs Yield')
plt.show()
=======
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 加载数据
data_path = r'C:\Users\38492\ultralytics\seg_evaluate\data2.txt'  # 替换为你的数据文件路径
data = pd.read_csv(data_path, delimiter='\t')

# 重命名列名以便访问
data.columns = ['Plot', 'Weed_control', 'Nitrogen', 'Potato_area', 'Weed_area', 'Yield']

# 对Potato_area和Weed_area进行回归分析
X = data[['Potato_area', 'Weed_area']]
y = data['Yield']
X = sm.add_constant(X)  # 添加常数项到自变量

model = sm.OLS(y, X).fit()
print(model.summary())

# 3D可视化回归结果
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(data['Potato_area'], data['Weed_area'], data['Yield'], c='blue', marker='o')

# 创建网格以绘制回归平面
x_surf, y_surf = np.meshgrid(np.linspace(data['Potato_area'].min(), data['Potato_area'].max(), 100),
                             np.linspace(data['Weed_area'].min(), data['Weed_area'].max(), 100))
z_surf = model.params[0] + model.params[1] * x_surf + model.params[2] * y_surf

# 绘制回归平面
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5, rstride=100, cstride=100)

# 设置轴标签
ax.set_xlabel('Potato Area')
ax.set_ylabel('Weed Area')
ax.set_zlabel('Yield (dt/ha)')

plt.title('3D Regression Analysis: Potato Area and Weed Area vs Yield')
plt.show()
>>>>>>> 94c54e4f848ace37bf7c1afad41b08a90af25c23
