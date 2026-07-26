# -*- coding: utf-8 -*-
"""绘制 y = 4x 的图像"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-10, 10, 200)
y = 4 * x

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, label='y = 4x', color='#1f77b4', linewidth=2)

# 画出经过原点的坐标轴
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_xlim(-10, 10)
ax.set_ylim(-40, 40)
ax.set_aspect('equal')  # 让 x、y 轴单位长度一致，显示真实斜率
ax.set_title('y = 4x 的图像')
ax.legend(loc='upper left')
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig('y_equals_4x.png', dpi=150)
plt.show()
