import tkinter as tk
from tkinter import *
import math
import calculator

#Create window
window = tk.Tk()
window.title("Calculator")
window.columnconfigure(0, weight=1)


#Create frames
topFrame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
topFrame.grid(row=0, column=0, sticky="ew")
topFrame.columnconfigure(0, weight=1)

bottomFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=3)
bottomFrame.grid(row=1, column=0, sticky="ew")
bottomFrame.columnconfigure(0, weight=1)


#Create entry field
entry = tk.Entry(master = topFrame, bg="grey", width=10, justify="right")
entry.grid(row=0, column=0, sticky="ew")

#Create calculator 
calc = calculator.Calculator()

#Callback function
def calcFunction(buttonVal):
    if buttonVal.isdigit() or buttonVal==".":
        if (calc.getLastButtonClicked() in ["=", "M+"]):
            entry.delete(0, END)
        entry.insert("end", buttonVal)
    elif buttonVal == "MC":
        calc.clearMemory()
        calc.clearWorkingMemory()
        entry.delete(0, END)
    elif buttonVal == "M+":
        calc.addToMemory(entry.get())
        entry.delete(0, END)
        entry.insert("end", calc.getMemory())
        calc.clearWorkingMemory()
    elif buttonVal == "÷":
        calc.divide(entry.get())
        entry.delete(0, END)
    elif buttonVal == "X":
        calc.multiply(entry.get())
        entry.delete(0, END)
    elif buttonVal == "-":
        calc.substract(entry.get())
        entry.delete(0, END)
    elif buttonVal == "+":
        calc.add(entry.get())
        entry.delete(0, END)
    elif buttonVal == "=":
        calc.addToWorkingMemory(entry.get())
        entry.delete(0, END)
        entry.insert("end", calc.equals())
        calc.clearWorkingMemory()
    else:
        pass
    calc.changeLastButtonClicked(buttonVal)

#Create Buttons
buttons = ["MC", "M+", "÷", "X", "7", 
            "8", "9", "-", "4", "5", 
            "6", "+", "1", "2", "3", 
            "=", "0", "."
            ]

for i, val in enumerate(buttons):
    row = math.floor(i/4)
    column = i % 4
    
    calcButton = Button(master=bottomFrame, text=val, width=1, command=lambda buttonVal=val: calcFunction(buttonVal))
    
    if val == "0":
        calcButton.grid(row=row,column=column, columnspan=2, sticky="nesw" )
    elif val == "=":
        calcButton.grid(row=row,column=column, rowspan=2, sticky="nesw")
    elif val == ".":
        calcButton.grid(row=row,column=column+1, sticky="nesw")
    else:
        calcButton.grid(row=row,column=column, sticky="nesw")

#Run main event loop
window.resizable(False, False) 
window.mainloop()