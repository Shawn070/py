# 寻找一组数中的最大值
def main():
    #方法一：
    n = eval(input("How many numbers are there?"))
    max = eval(input("Enter a number>>"))
    for i in range(n-1):
        x = eval(input("Enter a number>>"))
        if x > max:
            max = x
        print("The largest value is", max)
    #方法二：
    # x1, x2, x3 = eval(input("Please enter three values:"))
    # print("The largest value is", max(x1, x2, x3))

main()