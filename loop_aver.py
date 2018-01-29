# 交互式循环
def main():
    sum = 0.0
    count = 0

    # 交互式循环：
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >>"))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)?")
    print("\nThe average of the number is", sum/count)

    # 哨兵循环1：
    x = eval(input("Enter a number (negative to quit) >>"))
    while x >= 0:
        sum = sum + x
        count = count + 1
        x = eval(input("Enter a number (negative to quit) >>"))
    print("\nThe average of the number is", sum / count)

    # 哨兵循环2：
    xStr = input("Enter a number  (<Enter> to quit) >>")
    while xStr !="":
        x = eval(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number  (<Enter> to quit) >>")
    print("\nThe average of the number is", sum/count)

    # 文件循环：
    fileName = input("What file are the numbers in?")
    infile = open(filename, 'r')
    sum = 0
    count = 0
    # for
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the number is", sum/count)
    # while
    line = infile.readline()    # 将文件的一行读取到字符串中
    while line !="":            # ""是换行符，而非空字符
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the number is", sum / count)

    # 循环嵌套：
    for xStr in line.split(","):
        sum = sum + eval(xStr)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the number is", sum / count)

main()