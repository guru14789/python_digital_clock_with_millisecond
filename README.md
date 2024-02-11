# python_digital_clock_with_millisecond
## understanding:
1. `from tkinter import *`: This imports all symbols from the tkinter module, allowing you to use Tkinter classes, functions.
2. `from tkinter.ttk import *`: This imports all symbols from the `ttk` submodule of tkinter. `ttk` stands for "themed Tkinter," which provides access to the Tk themed widget set.
3. `from time import strftime, time`: This imports the `strftime` and `time` functions from the Python built-in `time` module. 
4. `a = Tk()`: This creates the main window of the application.
5. `a.title("PYTHON CLOCK")`: This sets the title of the window to "PYTHON CLOCK".
6. `def clocktime():`: This defines a function named `clocktime()`
7. `millis = int(round(time() * 1000, 5))`: This line retrieves the current time in milliseconds and rounds it to 5 decimal places. It's used to display milliseconds.
8. `string = strftime('%H:%M:%S:{} %p'.format(str(millis)[-3:-1]))`: This line formats the current time in the string format "HH:MM:SS:SSS AM/PM"
9. `label.config(text=string)`: This updates the text displayed by the Label widget (`label`) with the formatted time string.
10. `label.after(1, clocktime)`: This schedules the `clocktime` function to be called again after 1 millisecond. This creates a loop where the clock is updated every millisecond.
11. `label = Label(a, font=("ds-digital", 100), background="black", foreground="orange")`: This creates a Label widget (`label`) inside the main window (`a`). It sets the font, background color, and foreground (text) color for the label.
12. `label.pack(anchor='center')`: This packs the label widget into the main window and centers it.
13. `clocktime()`: This initial call starts the clock function to begin updating the clock display.
14. `mainloop()`: This starts the Tkinter event loop, which listens for events such as user input, redraws the GUI, and handles other GUI-related tasks.
## Python code:
```
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
```
## output:
![Screenshot 2024-02-11 192441](https://github.com/guru14789/python_digital_clock_with_millisecond/assets/151705853/c32dc00b-e5ee-46b8-a2c3-3d15506932f7)
