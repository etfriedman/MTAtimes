import tkinter as tk
import random
import os
def update():
    times = os.popen('python times.py').read()
    l.config(text=str(times))
    root.after(1000, update)

root = tk.Tk()
l = tk.Label(text='Train Times:')
l.pack()
root.after(1000, update)
root.mainloop()
