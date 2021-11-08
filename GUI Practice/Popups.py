from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Boxes')
root.iconbitmap('C:/Users/Computer Science ~ B/Pictures/doge.ico')
root.resizable(0, 0)

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion('This is my Popup!', 'Hello World!')
    Label(root, text=response).pack()
    if response == 'yes':
        Label(root, text='You clicked Yes').pack()
    else:
        Label(root, text='You clicked No').pack()

Button(root, text='Popup', command=popup).pack()


root.mainloop()