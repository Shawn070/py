#TempCovert.py
for i in range(3):
    val = input("请输入带温度表示的温度值（例如：32C）：")
    if val[-1] in ['C', 'c']:
        f = 1.8 * float(val[0:-1]) + 32     # val[0,-1]:获取除最后一个字符的字符串
        print("转换够的温度为：%.2fF" %f)    # val[0,2]:[0,2)子区间
    elif val[-1] in ['F', 'f']:
        c = (float(val[0:-1] - 32)) / 1.8
        print("转换后的温度为：%.2fC" %c)
    else:
        print("输入有误")