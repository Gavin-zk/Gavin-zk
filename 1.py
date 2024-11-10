#!/usr/bin/python3
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 各部分所占比例
sizes = [0.2073, 0.3659, 0.2439, 0.0976, 0.0854]
# 颜色
colors = ['red', 'blue', 'green', 'yellow', 'orange']
# 标签
labels = ['算法开发实车平台', 'AI算力支撑测试平台', '多域在环开发平台', '交通场景数据系统', '开发工具链']

# 绘制饼图
plt.pie(sizes, colors = colors, labels = labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()