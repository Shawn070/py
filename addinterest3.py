print("This program plots the growth of a 10-year investment.")
# 输入本金和利率
principal = eval(input("Enter the initial principal:"))
apr = eval(input("Enter the annualized interest rate:"))
# 建立一个图标，绘制每一年银行账户的增长数据
for year in range(1, 11):
    principal = principal * (1 + apr)
    print("%2d" %year, end='')      # end=' '意思是末尾不换行，加空格
    # 计算星号的数量
    total = int(principal*4/1000)
    print("*" * total)
print("0.0K    2.5K    5.0K    7.5K    10.0K")