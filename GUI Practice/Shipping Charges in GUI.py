from tkinter import *

root = Tk()
root.title('Shipping Charges')
root.iconbitmap('C:/Users/Computer Science ~ B/Pictures/doge.ico')

frame = LabelFrame(root, padx=10, pady=10)
instructions = Label(frame, text='Choose the package weight and enter a distance\nto find the shipping charges.')

wt = IntVar

weight = LabelFrame(root, padx=10, pady=10)
Radiobutton(weight, text='2 pounds or less', variable=wt, value=1)


frame.pack(padx=10, pady=10)
weight.pack()

instructions.pack()

root.mainloop()