from tkinter import *




root=Tk()
root.geometry("390x305")
root.configure(bg='#B3BF55')
e=Entry(root,width=50, borderwidth=5, bg='#FA8072')
e.grid(row=0,column=0, columnspan=5, padx=10, pady=10)
def button_add(number):
  currentnum= e.get()
  e.delete(0,END)
  e.insert(0, currentnum + str(number))


def button_clear():
    e.delete(0,END)

def button_equal():
    second_number= e.get()
    e.delete(0,END)

    if math == "addition":
     e.insert(0,float(fnum)+ float(second_number))
    if math == "subtraction":
     e.insert(0,float(fnum)- float(second_number))
    if math == "multiplication":
     e.insert(0, float(fnum)* float(second_number))
    if math == "division":
     e.insert(0, float(fnum)/ float(second_number))


def button_plus():
    firstnum= e.get()
    global math
    global fnum
    fnum= int(firstnum)
    e.delete(0,END)
    math = "addition"
def button_divide():
    firstnum= e.get()
    global fnum
    global math
    fnum= int(firstnum)
    e.delete(0,END)
    math = "division"
def button_multiply():
    firstnum= e.get()
    global fnum
    global math
    fnum= int(firstnum)
    e.delete(0,END)
    math = "multiplication"
def button_minus():
    firstnum= e.get()
    global fnum
    global math
    fnum= int(firstnum)
    e.delete(0,END)
    math = "subtraction"
button1= Button(root,text="1",font='Digital-7',padx=40, pady=20, command= lambda: button_add(1))
button2= Button(root,font='Digital-7',text="2",padx=40, pady=20, command=lambda:button_add(2))
button3= Button(root,font='Digital-7',text="3",padx=40, pady=20, command=lambda:button_add(3))
button4= Button(root,font='Digital-7',text="4",padx=40, pady=20, command=lambda:button_add(4))
button5= Button(root,font='Digital-7',text="5",padx=40, pady=20, command=lambda:button_add(5))
button6= Button(root,font='Digital-7',text="6",padx=40, pady=20, command=lambda:button_add(6))
button7= Button(root,font='Digital-7',text="7",padx=40, pady=20, command=lambda:button_add(7))
button8= Button(root,font='Digital-7',text="8",padx=40, pady=20, command=lambda:button_add(8))
button9= Button(root,font='Digital-7',text="9",padx=40, pady=20, command=lambda:button_add(9))
button0= Button(root,font='Digital-7',text="0",padx=40, pady=20, command=lambda:button_add(0))

buttonC= Button(root,font='Digital-7',text="C",padx=40, pady=20, command=button_clear)

buttonPlus= Button(root,font=("Digital-7", 12,'bold'),text="+",padx=39, pady=20, command=lambda:button_plus())
buttonMinus= Button(root,font=("Digital-7", 12,'bold'), text="-",padx=40,pady=20, command=button_minus)

buttonEqual= Button(root,font=("Digital-7", 12,'bold'),text="=",padx=40, pady=20, command=button_equal)
buttonDivide= Button(root,font=("Digital-7", 11,'bold'), text="%",padx=40,pady=20, command=button_divide)
buttonMultiply= Button(root,font=("Digital-7", 12,'bold'), text="*",padx=40,pady=20, command=button_multiply)


button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

button0.grid(row=4,column=4)
buttonC.grid(row=3,column=4)
buttonPlus.grid(row=2,column=4)
buttonMinus.grid(row=5,column=2)
buttonEqual.grid(row=5,column=3,columnspan=8)

buttonDivide.grid(row=5,column=0)
buttonMultiply.grid(row=5,column=1)







root.mainloop()