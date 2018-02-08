from tkinter import *
import time

def main():

    def sendMsg():
        strMsg = '我' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        txtMsgList.insert(END, strMsg, "greencolor")
        txtMsgList.insert(END, txtMsg.get("0.0", END))
        txtMsg.delete("0.0", END)   # 0.0:文本的开始
    # array.insert(i, x): Insert a new item with value x in the array before position i.


    def cancleMsg():
        txtMsg.delete("0.0", END)

    def sendMsgEvent(event):
        if event.keysym == "Up":
            sendMsg()

    # 创建窗口
    t = Tk()
    t.title("与python聊天中")

    # 创建frame容器
    frmLT = Frame(width=500, height=320, bg="white")    # frame LeftTop
    frmLC = Frame(width=500, height=150, bg="white")    # frame LeftCenter
    frmLB = Frame(width=500, height=30)     # frame LeftButton
    frmRT = Frame(width=200, height=500)    # frame Right

    # 创建控件
    txtMsgList = Text(frmLT)
    txtMsgList.tag_config("greencolor", foreground="#008C00")   # 创建tag
    txtMsg = Text(frmLC)
    txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
    btnSend = Button(frmLB, text = "发 送", width = 8, command=sendMsg)
    btnCancel = Button(frmLB, text="取 消", width = 8, command=cancleMsg)
    imgInfo = PhotoImage(file = "chat.png")
    lblImage = Label(frmRT, image = imgInfo)
    lblImage.image = imgInfo

    # 窗口布局
    frmLT.grid(row=0, column = 0, columnspan=2, padx=1, pady=3)
    frmLC.grid(row=1, column = 0, columnspan=2, padx=1, pady=3)
    frmLB.grid(row=2, column = 0, columnspan=2)
    frmRT.grid(row=0, column = 2, rowspan=3, padx=2, pady=3)

    # 固定大小
    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

    btnSend.grid(row=2, column=0)
    btnCancel.grid(row=2, column=1)
    lblImage.grid()
    txtMsgList.grid()
    txtMsg.grid()

    t.mainloop()

if __name__ == '__main__':
    main()