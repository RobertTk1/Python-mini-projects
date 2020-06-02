from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import numpy as  np
import matplotlib.pyplot as plt
root = Tk()
root.title('Weather App')
root.iconbitmap("iconx.ico")
root.geometry('200x70')

def graph():
    hprices = np.random.normal(20000, 25000, 5000)
    plt.polar(hprices)
    plt.show()

btn = Button(root, text='Graph', command=graph)
btn.pack()
root.mainloop()