from tkinter import *
# 模板：
# from tkinter import *
# tk = Tk()
# # 此处添加控件代码
# ...
# tk.mainloop()

# tk = Tk()
# label = Label(tk, text = "Welcome to Python Tkinter!")
# button = Button(tk, text = "Click Me")
# label.pack()
# button.pack()
# tk.mainloop()

def processOK():    # 回调函数
    print("OK button is clicked")

def processCancel():    # 回调函数
    print("Cancel button is clicked")

def main():
    tk = Tk()
    btnOK = Button(tk, text = "OK", fg = "red",
        command = processOK)
    btnCancel = Button(tk, text = "Cancel", bg = "yellow",
        command = processCancel)
    btnOK.pack()
    btnCancel.pack()

    tk.mainloop()

if __name__ == '__main__':
    main()