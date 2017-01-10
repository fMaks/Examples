from tkinter import *
import sys

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.txt = Text(self)
        self.txt.pack(side='top')
        self.btn = Button(self, text="Click me", command=self.say_hi)
        self.btn.pack(side='top')
        self.quit = Button(self, text='Quit', fg='red',
                           command=root.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        txt = self.txt.get('insert')
        print('hi there', '0x{:x}:"{}"'.format(ord(txt[0]), txt))

root = Tk()
app = App(root)
if sys.platform != 'linux2':
    root.wm_state('zoomed')
else:
    root.wm_attributes('-zoomed', True)
app.mainloop()
