from tkinter import *
root = Tk()
root.title('Seconds Converter')

def seconds_convert(num):
    '''Converts num seconds into hours, minutes, & seconds'''
    
    hr = num//3600
    min = (num%3600)//60
    sec = num % 60
    
    l2 = '{} hour(s), {} minute(s), {} second(s)'.format(hr, min, sec)
    l1 = '{} seconds is'.format(num).center(len(l2))
    return l1 + '\n' + l2

def send_input(entry):
    '''Sends entry input to seconds_convert method'''
    num = int(entry.get())
    out = Label(text=seconds_convert(num))
    out.pack()

label = Label(text='Enter the number of seconds')
entry = Entry(root, text='Enter the number of seconds', width = 30, borderwidth = 10)
button = Button(root, text='Calculate!', padx=50, pady=10, command=lambda:send_input(entry))

label.pack()
entry.pack()
button.pack()


root.mainloop()