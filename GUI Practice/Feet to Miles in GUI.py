from tkinter import *
root = Tk()
root.title('Feet to Miles')

def feet_to_miles(feet):
    '''Converts feet into miles'''
    return round(feet/5280, 2)

def enter_feet(entry):
    '''Takes input from entry and returns output as km'''
    ft = float(entry.get())
    miles = feet_to_miles(ft)
    
    txt = '{} feet is {} mile(s)'.format(ft, miles)
    txt += '\nYou walked {} mile(s)!'.format(miles)
    tmp = Label(root, text=txt)
    tmp.pack()

i = Entry(root, width=30, borderwidth=10)
my_label = Label(root, text = 'Enter the number of feet to the number of miles')
button = Button(root, text='Calculate!', padx=50, pady=10, command=lambda: enter_feet(i))

i.pack()
my_label.pack()
button.pack()

root.mainloop()