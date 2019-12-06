#This runs the times.py and makes a GUI that updates every n milliseconds.
import tkinter as tk #imports GUI package
import os # allows you to run commands in command line from a line of code.

n = 1000# <-- change this value to change update time (ms)
#Update Function
def update():
    #set output of times.py to var so I can call later
    times = os.popen('python times.py').read()
    #set times to a string
    l.config(text=str(times))
    #Main update function for GUI
    root.after(n, update)
# define GUI properties and display it
root = tk.Tk()
#Label GUI
l = tk.Label(text='Train Times:')
#Pack info to be displayed
l.pack()
#update after defined number of milliseconds
root.after(n, update)
#start GUI
root.mainloop()
