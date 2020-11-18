import tkinter as tk
from tkinter import *
from random import *

window=tk.Tk()
window.geometry('900x600')
window.title("Random password generator")

p_type=""
result=""
hint=""
def getValue(t):
    getValue.p_type=t
    return getValue.p_type
def generate():
    p_type=getValue.p_type
    l=int(pass_len.get())
    result=[]
    h=hint1.get()
    nume="1234567890"
    alph="abcdefghijklmnopqrstuvwxyz"
    mix="abcdefghijklmnopqrstuvwxyz1234567890?@#$%"
    a=["ljust","rjust"]

    if(h==""):
        if(p_type=="numeric"):
            for i in range(l):
                result.append(choice(nume))
                
        elif(p_type=="alphanumeric"):
            for i in range(l):
                result.append(choice(alph))
                
        else:
            for i in range(l):
                result.append(choice(mix))
                
        result=''.join(result)
        
        resultBox.delete(0.0,END)
        resultBox.insert(END, result)
    else:
        wh=choice(a)
        x=l-len(h)
        y=[]
        for i in range(x+1):
            y.append(choice(nume))
        y=''.join(y)
        if(wh=="ljust"):
            result=h+y
        elif(wh=="rjust"):
            result=y+h
        resultBox.delete(0.0,END)
        resultBox.insert(END, result)

title=tk.Label(window,text="Random Password Generator",bg="blue",fg="yellow",justify="center",font=('',40))
title.place(relwidth=1)

lable=tk.Label(window,font=('',20),text="Choose password type")
lable.place(rely=0.2,relx=0.05)

button1=tk.Button(window,text="Numeric",padx=20,pady=15, command=lambda: getValue("numeric"))
button1.config(bg = 'lightgrey')
button1.place(rely=0.3,relx=0.1,relwidth=0.2)
button2=tk.Button(window,text="alphaNumeric",padx=20,pady=15, command=lambda: getValue("alphanumeric"))
button2.config(bg = 'lightgrey')
button2.place(rely=0.4,relx=0.1,relwidth=0.2)
button3=tk.Button(window,text="Mix",padx=20,pady=15, command=lambda: getValue("mix"))
button3.config(bg = 'lightgrey')
button3.place(rely=0.5,relx=0.1,relwidth=0.2)

lable=tk.Label(window,font=('',20),text="Enter the password lenght")
lable.place(rely=0.65,relx=0.05)

pass_len=tk.Entry(window,font=('',20))
pass_len.config(bg = 'lightgrey')
pass_len.place(rely=0.75,relx=0.1,relwidth=0.2)

hint=tk.Label(window, text="Enter keywords", font=('',20), bg="green")
hint.place(relx=0.63, rely=0.2,relwidth=0.25)

hint1=tk.Entry(window,text="text", font=('',20))
hint1.config(bg = 'lightgrey')
hint1.place(rely=0.3,relx=0.55,relwidth=0.4)

resultBox=tk.Text(window, bg="yellow",font=('',20),padx=100,pady=100)
resultBox.place(relheight=0.4, relwidth=0.4, relx=0.55, rely=0.4)

res_but=tk.Button(window, text="Generate", font=('',20), command=generate)
res_but.config(bg='lightgrey')
res_but.place(relwidth=0.2, relx=0.65,rely=0.85)

window.mainloop()