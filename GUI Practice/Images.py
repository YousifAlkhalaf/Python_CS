from tkinter import *
root = Tk()
root.title('Doge.com')
root.iconbitmap('C:/Users/Computer Science ~ B/Pictures/doge.ico')

button_quit = Button(root, text='Exit Program', command = root.quit)
button_quit.pack()
root.mainloop()