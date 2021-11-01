from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Errands')
root.iconbitmap('C:/Users/Computer Science ~ B/Pictures/doge.ico')

def total_time(n1, n2, n3):
    '''Starts at 3:00. Returns starting time plus n1, n2, and n3 minute values'''
    hr = 3
    min = 0
    
    errand_time = int(n1)+int(n2)+int(n3)
    hr += errand_time//60
    min += errand_time%60
    
    txt = 'You will come home at {}:{}'.format(hr, min)
    out = Label(text=txt)
    out.grid(row=4, column=0, columnspan=2)


l1 = Label(text='Enter time for errand 1, in minutes: ')
l2 = Label(text='Enter time for errand 2, in minutes: ')
l3 = Label(text='Enter time for errand 3, in minutes: ')

e1 = Entry(width=10, borderwidth = 5)
e2 = Entry(width=10, borderwidth = 5)
e3 = Entry(width=10, borderwidth = 5)

button = Button(borderwidth=3, text='Click to see total time', command=lambda: total_time(e1.get(), e2.get(), e3.get()))

l1.grid(row=0, column=0, padx=10, pady=10)
l2.grid(row=1, column=0, padx=10, pady=10)
l3.grid(row=2, column=0, padx=10, pady=10)
e1.grid(row=0, column=1, padx=5)
e2.grid(row=1, column=1, padx=5)
e3.grid(row=2, column=1, padx=5)
button.grid(row=3, column=0, columnspan=2, padx=70)

root.mainloop()