from graphics import *

win = GraphWin("Celsius Converter", 400, 300)
win.setCoords(0, 0, 3, 4)
# 绘制接口
Text(Point(1, 3), "Celsius Tmperature:").draw(win)
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
# 转换输入
celsius = eval(input.getText())
fahrenheit = 9.0/5.0 * celsius + 32.0
# 显示输出，改变按钮
output.setText(fahrenheit)
button.setText("Quit")
# 等待相应鼠标点击，退出程序
win.getMouse()
win.close()