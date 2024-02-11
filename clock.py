from tkinter import*
from tkinter.ttk import*
from time import strftime,time
a=Tk()
a.title("PYTHON CLOCK")
def clocktime():
    millis = int(round(time() * 1000,5))
    string=strftime('%H:%M:%S:{} %p'.format(str(millis)[-3:-1]))
    label.config(text=string)
    label.after(1,clocktime)
label=Label(a,font=("ds-digital",100),background="black",foreground="orange")
label.pack(anchor='center')
clocktime()
mainloop()
