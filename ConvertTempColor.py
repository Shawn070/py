from graphics import *

def convert(input):
    celsius = eval(input.getText())     # celsius(摄氏)
    fahrenheit = 9.0/5.0 *celsius + 32  # fahrenheit(华氏)
    return  fahrenheit

def colorChange(win, input):
    cnum = eval(input.getText())
    weight = cnum / 100
    newcolor = color_rgb(int(255*weight), int(66+150*(1-weight)), int(255*(1-weight)))
    win.setBackground(newcolor)

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0, 0, 3, 4)
    # 绘制输入接口
    Text(Point(1, 3), "Celsius Tmperature:").draw(win)
    Text(Point(2, 2.7), "(Please input 0.0-100.0)").draw(win)
    Text(Point(1, 1), "Fahrenheit Tmperature:").draw(win)
    input = Entry(Point(2, 3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2, 1), "")
    output.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
    # 等待鼠标点击
    win.getMouse()
    result = convert(input)     # 转换输入
    output.setText(result)      # 显示输出
    colorChange(win, input)     # 改变颜色
    button.setText("Quit")      # 改变按钮字
    # 等待点击事件，退出程序
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()