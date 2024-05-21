from tkinter import *
from Function import *

root = Tk()
root.title("My Test GUI")

#lbl_1 = Label(text="โปรแกรมทดสอบ",fg="White",font=40,bg="Black").pack()
#lbl_2 = Label(text="หัวข้อ1",font=20).place(x=0,y=40)
lbl_1 = Label(text="โปรแกรมทดสอบไพธอน",font=("Angsana New", 30),padx=30,pady=20).grid(row=0,columnspan=3)
lbl_3 = Label(text="ตัวเลข",font=20,padx=5,pady=5).grid(row=2,column=0,sticky=W)
et1=Entry(font=20,width=10)
et1.grid(row=2,column=1,sticky=W)
btn_3 = Button(text="ส่งค่า",font=20,width=8,command=printtest,padx=5,pady=5).grid(row=2,column=2)

lbl_4 = Label(text="ทดสอบ",font=20,pady=5).grid(row=3,column=0,sticky=W)
et2=Entry(font=20,width=30)
et2.grid(row=3,column=1)

lbl_5 = Label(text="ทดสอบการดับเบิ้ลคลิก",font=20,pady=5).grid(row=4,column=0,columnspan=2)
btn_1 = Button(text="คลิก",font=20,width=8,command=doubleClick,pady=2).grid(row=4,column=2)
btn_2 = Button(text="Close",font=("Angsana New", 20),command=lambda: close_window(root),pady=5).grid(row=5,column=0,columnspan=3)

root.geometry("500x300+700+0")
root.mainloop()