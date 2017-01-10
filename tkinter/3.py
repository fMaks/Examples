from tkinter import *
from random import random
def button_clicked():
    button['text'] = button['bg'] # показываем предыдущий цвет кнопки
    bg = '#%0x%0x%0x' % (random()*16, random()*16, random()*16)
    button['bg'] = bg
    button['activebackground'] = bg
root=Tk()
button = Button(root, command=button_clicked)
button.pack()
root.mainloop()