from tkinter import *
root = Tk()

# Creating a Label Widget
#myLabel1 = Label(root, text = 'Hello World!').grid(row=0, column=0)
#myLabel2 = Label(root, text = 'My Name Is John Elder').grid(row=1, column=0)
myLabel1 = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text = 'My Name Is John Elder')
myLabel3 = Label(root, text = ' ')
# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row = 1, column=5)
myLabel3.grid(row = 1, column = 1)

root.mainloop()