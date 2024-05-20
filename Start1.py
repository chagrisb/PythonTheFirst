from tkinter import *
from Function import *

root = Tk()
root.title("My Test GUI")

#lbl_1 = Label(text="โปรแกรมทดสอบ",fg="White",font=40,bg="Black").pack()
#lbl_2 = Label(text="หัวข้อ1",font=20).place(x=0,y=40)
lbl_1 = Label(text="เข้าสู่ระบบ",font=60,padx=30,pady=20).grid(row=0,columnspan=2)
lbl_3 = Label(text="ID: ",font=20,pady=5).grid(row=2,column=0,sticky=W)
et1=Entry(font=20,width=30)
et1.grid(row=2,column=1)

lbl_4 = Label(text="Password: ",font=20,pady=5).grid(row=3,column=0,sticky=W)
et2=Entry(font=20,width=30)
et2.grid(row=3,column=1)

btn_1 = Button(text="Login",font=20,width=8,command=doubleClick,pady=2).grid(row=4,column=0,sticky=E)
btn_2 = Button(text="Cancel",font=20,width=8,command=lambda: close_window(root),pady=2).grid(row=4,column=1,sticky=W)

root.geometry("500x200+700+0")
root.mainloop()