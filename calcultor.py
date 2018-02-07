from tkinter import*
import random
import time
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("calculator")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text="CALCULATOR",fg="Black",bd=8,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Subs():
    root1 = Tk()
    root1.geometry("600x800")
    root1.title("RESULT IS : ")
    Tops=Frame(root1, width=600,relief=SUNKEN)
    Tops.pack(side=TOP)
    f1=Frame(root1,width=800,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)
    
    Numberx=float(Number1.get())
    Numbery=float(Number2.get())
    substraction  = Numberx - Numbery
    subs = str ('%.2f' % substraction)
 #   Total=StringVar()
    SubTotal.set(subs)
    Total.set(subs)
    #Total=StringVar()
    txtTotal=Entry(f1, font=('arial',30,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
    txtTotal.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
    
    Numberx=float(Number1.get())
    Numbery=float(Number2.get())
    sumation= Numberx + Numbery
    Over = str ('%.2f' % sumation)
    SubTotal.set(Over)
    Total.set(Over)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Number1.set("")
    Number2.set("")
    SubTotal.set("")
    Total.set("")

#rand = StringVar()
Number1=StringVar()
Number2=StringVar()
SubTotal=StringVar()
Total=StringVar()

#lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
#lblReference.grid(row=0, column=0)
#txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
#txtReference.grid(row=0,column=1)

lblNumber1= Label(f1, font=('arial', 16, 'bold'),text="Number1",bd=16,anchor="w")
lblNumber1.grid(row=1, column=0)
txtNumber1=Entry(f1, font=('arial',16,'bold'),textvariable=Number1,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNumber1.grid(row=1,column=1)


lblNumber2= Label(f1, font=('arial', 16, 'bold'),text="Number2",bd=16,anchor="w")
lblNumber2.grid(row=2, column=0)
txtNumber2=Entry(f1, font=('arial',16,'bold'),textvariable=Number2,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNumber2.grid(row=2,column=1)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=3, column=0)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=3,column=1)

lblTotal= Label(f1, font=('arial', 16, 'bold'),text="Total cost",bd=16,anchor="w")
lblTotal.grid(row=4, column=0)
txtTotal=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotal.grid(row=4,column=1)

Number1Total=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="+",bg="powder blue",command=Ref).grid(row=7,column=1)

Number2Total=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="-",bg="powder blue",command=Subs).grid(row=7,column=2)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=3)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=8,column=1)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=8,column=2)


root.mainloop()
