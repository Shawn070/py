# 计算三角形周长
import math
def square(x):
    return x * x
def distance(x1, y1, x2, y2):
    dist = math.sqrt(square(x1 - x2) + square(y1 - y2))
    return dist
def isTriangle(x1, y1, x2, y2, x3, y3):
    flag = ((x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)) != 0
    return flag
def main():
    print("Please enter (x, y) of three points in turn:")
    # 获取用户输入的三个坐标点
    x1, y1 = eval(input("Point1: (x, y) ="))
    x2, y2 = eval(input("Point2: (x, y) ="))
    x3, y3 = eval(input("Point3: (x, y) ="))
    # 判断三个点是否构成三角形
    if(isTriangle(x1, y1, x2, y2, x3, y3)):
        # 计算三角形周长
        perim = (distance(x1, y1, x2, y2)
                + distance(x2, y2, x3, y3)
                + distance(x1, y1, x3, y3))
        print("The perimeter of the triangle is: {0:0.2f}".format(perim))
    else:
        print("Kidding me? This is not a triangle!")
main()