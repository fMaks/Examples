from tkinter import *
root=Tk()
frame1=Frame(root,width=100,heigh=100,bg='green',bd=50)
frame2=Frame(root,width=150,heigh=75,bg='red',bd=5)
button1=Button(frame1,text=u'Первая кнопка')
button2=Button(frame2,text=u'Вторая кнопка')
frame1.pack()
frame2.pack()
button1.pack()
button2.pack()
root.mainloop()