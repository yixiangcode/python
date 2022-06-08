import tkinter as tk
from tkinter.ttk import *
from time import strftime
window=tk.Tk()
window.title("XianG测试系统")
window.geometry('800x600')
window.configure(background='Gray')
tk.Label(window,text="上课系统",font=("ds-digital",10),bg="gray",padx=100,pady=50).pack()

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = tk.Label(window, font=("ds-digital", 80),background="gray", foreground="cyan")
label.pack(anchor='center')
time()
PIC=tk.PhotoImage(file="check.gif")
tk.Label(window,image=PIC).pack()
nameList=["a","b","c"]
nameListBox=tk.Listbox(window,justify=tk.RIGHT,width=30,selectmode=tk.SINGLE)#MULTIPLE
for name in nameList:
    nameListBox.insert(0,name)
nameListBox.pack()
#window.iconbitmap("tenor.ico")
frame=tk.Frame(window).pack(side=tk.TOP)
tk.Label(frame,text='名字').pack(side=tk.LEFT)
tk.Entry(frame).pack(side=tk.LEFT)
tk.Label(window).pack()
tk.Button(window,text="提交").pack()
window.mainloop()
