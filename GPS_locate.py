from numpy import *
i = 1
c = 0.299792458     # 光速0.299782458km/μs
x = zeros((6, 4))   # 存储6个卫星的(x, y, z, t)参数
while i <= 6:
    print("%s %d" % ("please input (x, y, z, t) of group", i))
    temp = input()      # input str
    x[i-1] = temp.split()   # str to array
    j = 0
    while j < 4:
        x[i-1][j] = float(x[i-1][j])
        j += 1
    i += 1
a = zeros((4, 4))   # 系数矩阵
b = zeros((4, 1))   # 常数项
j = 0
while j < 4:
    a[j][0] = 2 * (x[5][0] - x[j][0])
    a[j][1] = 2 * (x[5][1] - x[j][1])
    a[j][2] = 2 * (x[5][2] - x[j][2])
    a[j][3] = 2 * c * c * (x[5][3] - x[j][3])
    b[j][0] = x[5][0] * x[5][0] - x[j][0] * x[j][0] + \
              x[5][1] * x[5][1] - x[j][1] * x[j][1] + \
              x[5][2] * x[5][2] - x[j][2] * x[j][2] + \
              c * c * (x[5][3] * x[5][3] - x[j][3] * x[j][3])
    j += 1
a = linalg.inv(a)   # 系数矩阵求逆
print(dot(a, b))

'''
I & O:
please input (x, y, z, t) of group 1
3 2 3 10010.00692286
please input (x, y, z, t) of group 2
1 3 1 10013.34256381
please input (x, y, z, t) of group 3
5 7 4 10016.67820476
please input (x, y, z, t) of group 4
1 7 3 10020.01384571
please input (x, y, z, t) of group 5
7 6 7 10023.34948666
please input (x, y, z, t) of group 6
1 4 9 10030.02076857
[[  4.41666667e+00]
 [  1.91666667e+00]
 [  2.75000000e+00]
 [  1.00347463e+04]]

***Repl Closed***
'''