import tkinter
root=tkinter.Tk()
listbox1=tkinter.Listbox(root,height=5,width=15,selectmode=tkinter.EXTENDED)
listbox2=tkinter.Listbox(root,height=5,width=15,selectmode=tkinter.SINGLE)
list1=["Москва","Санкт-Петербург","Саратов","Омск"]
list2=["Канберра","Сидней","Мельбурн","Аделаида"]
for i in list1:
    listbox1.insert(tkinter.END,i)
for i in list2:
    listbox2.insert(tkinter.END,i)
listbox1.pack()
listbox2.pack()
root.mainloop()
