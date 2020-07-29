from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("KAMAL CLASSES")
root.geometry("500x400+300+300")

def f1():
    fb, mat = " "," "
    if s1.get()==1:
        fb += "FANTASTIC"
    elif s1.get()==2:
        fb += "EXCELLENT"
    else:
        fb += "SUPERB"
        
    if n.get()==n:
        mat += "NOTES"
    if s.get()==s:
        mat += "SOFTWARE"
    if c.get()==c:
        mat += "CERTIFICATE"
    
    msg = "FEEDBACK" + fb + "\n" + "MATERIALs" + mat
    messagebox.showinfo("result",msg)
    
    to = "kamalsir@ymail.com"
    subject="feedback+materials by PRABHJYOT"
    text=msg
    import smtplib
    sender = 'prabhjyotsinghtrt@gmail.com'
    password = ''
    message = 'Subject: {}\n\n{}'.format(subject,text)
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(sender,password)
    print("logged in")
    try:
        server.sendmail(sender,to,message)
        print("enter emai")
    except:
        print('error sending email')
    server.quit
        
s1 = IntVar()
s1.set(1)
    
lblfeed = Label(root,text="FEEDBACK",font=("arial",18,"bold")).grid()
rbFant = Radiobutton(root,text="FANTASTIC",font=("arial",18),variable=s1,value=1).grid(sticky='w')
rbExce = Radiobutton(root,text="EXCELLENT",font=("arial",18),variable=s1,value=2).grid(sticky='w')
rbSupe = Radiobutton(root,text="SUPERB",font=("arial",18),variable=s1,value=3).grid(sticky='w')

n,s,c = IntVar(),IntVar(),IntVar()

lblMate = Label(root,text="MATERIALS",font=("arial",18,"bold")).grid()
cbnote = Checkbutton(root,text="NOTES",font=("arial",18),variable=n).grid(sticky='w')
cbSoft = Checkbutton(root,text="SOFTWARE",font=("arial",18),variable=s).grid(sticky='w')
cbcert = Checkbutton(root,text="CERTIFICATE",font=("arial",18),variable=c).grid(sticky='w')
btnSubmit = Button(root,text="EMAIL",font=("arial",18,"bold"),command=f1).grid()

root.mainloop()