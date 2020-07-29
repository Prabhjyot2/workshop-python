from tkinter import *
root = Tk()
root.title("Color Me")
root.geometry("500x400+250+250")

def f1(num):
	if num == 1:
		root.configure(background='red')
	elif num == 2:
		root.configure(background='green')
	else:
		root.configure(background='blue')

btnRed = Button(root,text="Red",font=("arial",18,"bold"),width=10,command=lambda:f1(1))
btnGreen = Button(root,text="green",font=("arial",18,"bold"),width=10,command=lambda:f1(2))
btnBlue = Button(root,text="blue",font=("arial",18,"bold"),width=10,command=lambda:f1(3))

btnRed.pack(pady=10)
btnGreen.pack(pady=10)
btnBlue.pack(pady=10)

root.mainloop()