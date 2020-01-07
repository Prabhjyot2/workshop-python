from tkinter import *
win = Tk()
win.title("FUTURE PLANS")
win.geometry("500x400+250+250")

def f1():
    res = s.get()
    selection=''
    if res == 1:
        selection = "JOB"
    elif res == 2:
        selection = "MS"
    elif res == 3:
        selection = "MBA"
    else:
        selection = "MTECH"
     
    from tkinter import messagebox
    messagebox.showinfo("selection",selection)
            
s = IntVar()
s.set(1)

rbjob = Radiobutton(win,text="Job",font=("arial",18,"bold"),variable=s,value=1).grid(sticky='w')
rbMs = Radiobutton(win,text="Ms",font=("arial",18,"bold"),variable=s,value=2).grid(sticky='w')
rbMba = Radiobutton(win,text="Mba",font=("arial",18,"bold"),variable=s,value=3).grid(sticky='w')
rbMtech = Radiobutton(win,text="Mtech",font=("arial",18,"bold"),variable=s,value=4).grid(sticky='w')
btnSubmit = Button(win,text="SUBMIT",font=("arial",18,"bold"),command=f1).grid()

win.mainloop()