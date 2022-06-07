import tkinter as tk
from tkinter.ttk import *
from time import strftime
import random
window=tk.Tk()
window.title("XianG测试系统")
window.geometry('800x600')
window.configure(background='Gray')
randomNum=random.randint(0,10000)
round=5
print(randomNum)
tk.Label(window,text="阿巴阿巴系统",font=("ds-digital",10),bg="gray",padx=100,pady=50).pack()
def guess():
    global round
    numInput=int(number.get())
    if(numInput < randomNum):
        round-=1
        result.configure(text="再大一点，还有%d次机会"%round,background="yellow")
    if(numInput > randomNum):
        round-=1
        result.configure(text="再小一点，还有%d次机会"%round,background="yellow")
    if(numInput == randomNum):
        result.configure(text="恭喜！正确数字为%d"%randomNum,background="yellow")
    if round<=0:
        result.configure(text="你输了",background="yellow")
def reset():
    global randomNum
    global round
    result.configure(text="继续猜~",background="yellow")
    round=5
    randomNum=random.randint(1,10000)
    print(randomNum)
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = tk.Label(window, font=("ds-digital", 80),background="gray", foreground="cyan")
label.pack(anchor='center')
time()

window.iconbitmap("Logo.ico")

number_frame=tk.Frame(window)
number_frame.pack(side=tk.TOP)
number_label=tk.Label(number_frame,text='请输入数字')
number_label.pack(side=tk.LEFT)
number=tk.Entry(number_frame)
number.pack(side=tk.LEFT)
result=tk.Label(window)
result.pack()
btn=tk.Button(window,text="提交",font=('Bold',16),width=10,height=1,command=guess)
btn.pack()
rst=tk.Button(window,text="重置",command=reset)
rst.pack()
window.mainloop()
