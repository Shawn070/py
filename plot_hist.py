import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)     # 正态分布
plt.hist(x, 50, normed = 1, facecolor = 'g')    # 50:直条个数，normed:布尔值，1：将直方图归一化，纵轴显示概率
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])    # x:40~160; y:0~0.03
plt.show()