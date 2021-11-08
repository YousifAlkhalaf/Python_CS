from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math

root = Tk()
root.title('Shipping Charges')
root.iconbitmap('C:/Users/Computer Science ~ B/Pictures/doge.ico')
root.resizable(0, 0)

def clicked(value):
    '''Sets radiobutton value to value'''
    myLabel = Label(root, text=value)
    myLabel.pack

def calculate(weight, distance):
    '''Calculates cost and outputs a label with the cost rounded to 2 decimal places'''
    if weight == 1:
        cost = 1.10 * math.ceil(distance/500)
    elif weight == 2:
        cost = 2.20 * math.ceil(distance/500)
    elif weight == 3:
        cost = 3.70 * math.ceil(distance/500)
    elif weight == 4:
        cost = 3.80 * math.ceil(distance/500)
    cost = round(cost, 2)
    
    output = messagebox.showinfo('Shipping Charges', f'Cost is ${cost:.2f}')

frame = LabelFrame(root, padx=10, pady=10)
instructions = Label(frame, text='Choose the package weight and enter a distance\nto find the shipping charges.')

wt = IntVar()
weight = LabelFrame(root, padx=10, pady=10)

Radiobutton(weight, text='2 pounds or less', variable=wt, value=1, command=lambda: clicked(wt.get())).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
Radiobutton(weight, text='Over 2 pounds, but less than 6 pounds', variable=wt, value=2, command=lambda: clicked(wt.get())).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
Radiobutton(weight, text='Over 6 pounds, but less than 10 pounds', variable=wt, value=3, command=lambda: clicked(wt.get())).grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
Radiobutton(weight, text='10 pounds or more', variable=wt, value=4, command=lambda: clicked(r.get())).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

distance = LabelFrame(root, padx=10, pady=10)
miles = Entry(distance)
mileLabel = Label(distance, text='Enter distance (miles): ')

button = Button(text='Calculate charges', pady=10, command=lambda: calculate(float(wt.get()), float(miles.get())))

frame.grid(padx=10, pady=10, row=0)
weight.grid(padx=10, pady=10, row=1)
distance.grid(padx=10, pady=10, row=2)
button.grid(padx=10, pady=10, row=3)

instructions.pack()
mileLabel.grid(column=0, row=0)
miles.grid(column=1, row=0)
root.mainloop()