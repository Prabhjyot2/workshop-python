from tkinter import *
win = Tk()
win.title("SANDWICH")
win.geometry("500x400+250+250")
lblSelectOption = Label(win,text="select options",font=("arial",18,"bold")).grid()
def f1():
    order =''
    if t.get() == 1:
        order += "TOMATO "
    if o.get() == 1:
        order += "ONION "
    if p.get() == 1:
        order += "POTATO "
    if c.get():
        order += "CHEESE "
     
    from tkinter import messagebox
    if t.get() == 0 | o.get() == 0 | p.get() == 0 | c.get() == 0:
            messagebox.showerror("ERROR","loude select kar")
    else:
        messagebox.showinfo("order",order)
            
t,o,p,c = IntVar(),IntVar(),IntVar(),IntVar()
cbtom = Checkbutton(win,text="TOMATO",font=("arial",18,"bold"),variable=t).grid(sticky='w')
cbonion = Checkbutton(win,text="ONION",font=("arial",18,"bold"),variable=o).grid(sticky='w')
cbpotato = Checkbutton(win,text="POTATO",font=("arial",18,"bold"),variable=p).grid(sticky='w')
cbcheese = Checkbutton(win,text="CHEESE",font=("arial",18,"bold"),variable=c).grid(sticky='w')
btnSubmit = Button(win,text="ORDER",font=("arial",18,"bold"),command=f1).grid()

win.mainloop()