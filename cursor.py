from tkinter import *
import tkinter 

window = Tk() 
B1 = Button(window, text = "circle", relief = RAISED, cursor = "circle",fg="green") 
B1.place(x=80,y=20)
B2 = Button(window, text = "plus", relief = RAISED, cursor = "plus",fg="red") 
B2.place(x=80,y=50)
B3 = Button(window, text = "dotbox", relief = RAISED, cursor = "dotbox",fg="blue") 
B3.place(x=80,y=80)


window.geometry('200x200')
window.mainloop()