from tkinter import *
from time import strftime

window = Tk()
window.title('Clock')


def time():
    time_str = strftime('%H:%M:%S:%Y %p')
    Label.config(text=time_str)
    Label.after(1000, time)


Label = Label(window, background='black', foreground='blue', font=('Arial', 50))
Label.pack(anchor='center')

time()

window.mainloop()
