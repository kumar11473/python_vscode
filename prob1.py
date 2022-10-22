from tkinter import *
import tkinter
window=Tk()

txt=Entry(window,width=15)
txt.place(x=120, y=50)
def clicked():
    res="welcome "+txt.get()
    label.configure(text=res)
btn=Button(window, text="Greet", fg='blue',command=clicked)
btn.place(x=140, y=80)
label=Label(window,text="",font=10,fg="red")
label.place(x=90, y=100)
window.geometry("300x200+10+10")

window.mainloop()