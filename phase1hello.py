from tkinter import *

import random

root = Tk()

list = ['hi', 'hello', 'wassup']


def click():
    ni = random.choice(list)
    mylabel = Label(root, text= ni + ' ' + e.get())
    mylabel.pack()


hii = Label(root, text='Hello what is your name')

hii.pack()
e = Entry(root)
e.pack()
mybutton = Button(root, text='Click here', command=click)

mybutton.pack()

root.mainloop()