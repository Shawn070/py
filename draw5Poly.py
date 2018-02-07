# 交互式绘制五边形
from graphics import *

def main():
    win = GraphWin("Draw a polygon", 300, 300)
    win.setCoords(0, 0, 300, 300)
    message = Text(Point(150, 20), "Click on five points")
    message.draw(win)
    # 获取多边形的5个点
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)
    # 使用Polygon对象绘制多边形
    polygon = Polygon(p1, p2, p3, p4, p5)
    polygon.setFill("peachpuff")
    polygon.setOutline("black")
    polygon.draw(win)
    win.getMouse()

if __name__ == '__main__':
    main()