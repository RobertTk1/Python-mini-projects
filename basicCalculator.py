from tkinter import *


root = Tk()

root.title('simple Calculator')
e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,current + str(number))

def clear():
    e.delete(0,END)

def add_up():
    global f_num
    global math
    math = 'addition'
    f_num = int(e.get())
    e.delete(0, END)

def equal():
    sec_num = e.get()
    e.delete(0, END)
    #total = int(f_num) + int(sec_num)

    if math == 'addition':
        e.insert(0, int(f_num) + int(sec_num))

    if math == 'subtraction':
        e.insert(0, int(f_num) - int(sec_num))
    if math == 'multiplication':
        e.insert(0, int(f_num) * int(sec_num))
    if math == 'division':
        e.insert(0, int(f_num) / int(sec_num))



def sub():
    global f_num
    global math
    math = 'subtraction'
    f_num = int(e.get())
    e.delete(0, END)

def multi():
    global f_num
    global math
    math = 'multiplication'
    f_num = int(e.get())
    e.delete(0, END)

def div():
    global f_num
    global math
    math = 'division'
    f_num = int(e.get())
    e.delete(0, END)


but1 = Button(root, text='1', padx=30, pady=20, command=lambda: button_add(1))
but2 = Button(root, text='2', padx=30, pady=20, command=lambda: button_add(2))
but3 = Button(root, text='3', padx=30, pady=20, command=lambda: button_add(3))
but4 = Button(root, text='4', padx=30, pady=20, command=lambda: button_add(4))
but5 = Button(root, text='5', padx=30, pady=20, command=lambda: button_add(5))
but6 = Button(root, text='6', padx=30, pady=20, command=lambda: button_add(6))
but7 = Button(root, text='7', padx=30, pady=20, command=lambda: button_add(7))
but8 = Button(root, text='8', padx=30, pady=20, command=lambda: button_add(8))
but9 = Button(root, text='9', padx=30, pady=20, command=lambda: button_add(9))
but0 = Button(root, text='0', padx=30, pady=20, command=lambda: button_add(0))
but_add = Button(root, text='+', padx=30, pady=20, command=add_up)
but_equal = Button(root, text='=', padx=70, pady=20, command= equal)
but_clear = Button(root, text='C', padx=70, pady=20, command=clear)

but_sub = Button(root, text='-', padx=32, pady=20, command=sub)
but_multi = Button(root, text='*', padx=32, pady=20, command=multi)
but_div = Button(root, text='/', padx=32, pady=20, command=div)

but0.grid(row=4, column=0)

but1.grid(row=3, column=0)
but2.grid(row=3, column=1)
but3.grid(row=3, column=2)

but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)

but7.grid(row=1, column=0)
but8.grid(row=1, column=1)
but9.grid(row=1, column=2)

but_add.grid(row=5, column=0)
but_equal.grid(row=5, column=1, columnspan=2)
but_clear.grid(row=4, column=1, columnspan=2)

but_sub.grid(row=6, column=0)
but_multi.grid(row=6, column=1)
but_div.grid(row=6, column=2)


root.mainloop()