import numpy as np
from matplotlib.pyplot import *

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(X*X), np.sin(X)
plot(X, C, "ro", label = "$sin(x)$")
plot(X, S, label = "$cos(x^2)$")
xlabel("xlabel")
ylabel('ylabel')
legend()    # 描述每条曲线的标签
title("This is Title")
show()