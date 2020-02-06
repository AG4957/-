import tkinter as tk
from tkinter import *
import win32clipboard as w
import win32con
import win32gui
import time

window = tk.Tk()

#禁止窗口缩放
window.resizable(False, False)

window.title('QQ信息连续发送')
window.geometry('425x200')
e1 = tk.Label(window, text='纯属娱乐，不要恶搞！', bg='green', font=('Arial', 20)).grid(row=0, column=0,columnspan=2,ipadx=45)
e3 = tk.Label(window, text='请输入循环次数', font=('Arial', 14)).grid(row=1, column=0)
e4 = tk.Label(window, text='请输入QQ备注名', font=('Arial', 14)).grid(row=2, column=0)
e5 = tk.Label(window, text='请输入发送内容', font=('Arial', 14)).grid(row=3, column=0)
e8 = tk.Label(window,text='禁止用于商业使用，软件使用中涉及到的所有法律问题及后果自负与作者无关！',font=('Arial', 7)).grid(row=5, column=0,columnspan=2)

def sleeptime(hour,min,sec):#创建时间组
    return hour*3600 + min*60 + sec
second = sleeptime(0,0,0.1)

def hit_me():
    n = int(N.get())  # 请输入循环次数
    # print(a)
    name =Name.get()  # 请输入QQ备注名
    mgs =Mgs.get()  # 请输入发送内容

    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, mgs)
    w.CloseClipboard()
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, name)

    for i in range(0,n):
        #限制发送次数
        if i >=100:
            break
        # 填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        # 回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        time.sleep(second)


N = StringVar()
Name = StringVar()
Mgs = StringVar()

e2 = tk.Entry(window, textvariable=N, font=('Arial', 12)).grid(row=1, column=1,)# 显示成明文形式
e6 = tk.Entry(window, textvariable=Name, font=('Arial', 12)).grid(row=2, column=1)
e7 = tk.Entry(window, textvariable=Mgs, font=('Arial', 12)).grid(row=3, column=1)

b = tk.Button(window, text='开始', font=('Arial', 14), width=10, height=1, command=hit_me).grid(row=4, column=1)

window.mainloop()
