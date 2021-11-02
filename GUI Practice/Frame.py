from tkinter import *

root = Tk()
root.title('Doge.com')
root.iconbitmap('C:/Users/Computer Science ~ B/Pictures/doge.ico')

frame = LabelFrame(root, text='This is my Frame...', padx=50, pady=50)
b = Button(frame, text='DON\'T CLICK ME')
b2 = Button(frame, text='unless...\U0001F97A')

b.grid(row=0, column=0)
b2.grid(row=1, column=0)
frame.pack(padx=10,pady=10)

root.mainloop()