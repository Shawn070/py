# 连续点击10次鼠标返回坐标值
from graphics import *
def main():
    win = GraphWin("Click me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:({0},{1})".format(p.getX(), p.getY()))
        print("You clicked at:", p.getX(), p.getY())

if __name__ == '__main__':
    main()