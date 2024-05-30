###############################################################################
##
##  PYTHON GUI DEMO -- Copyright Michel Pasquier, 2013-2018
##


## This demo using Tkinter is part of section 01 (Introduction to Python).
## When executing a .py file (e.g. by double-clicking it) a Python shell is
## created that interprets the code, and quits - unless the user is prompted
## or a GUI is launched (that must be manually closed via a menu or button).


import tkinter as tk

class tkConvert(tk.Frame):          # feet-to-meter unit conversion calculator
                                    # (using a 2x3 grid / geometry manager)
    def __init__(self):
        root = tk.Tk()
        root.title("Feet to Meters")
        tk.Frame.__init__(self,root)
        tk.Button(root, text="Calculate",  # function ref, defined below
                  command=self.calculate).grid(row=0,column=0,sticky=tk.W)
        self.feet = tk.StringVar()
        self.feet.set("3")
        feet_entry = tk.Entry(textvariable=self.feet, width=8)
        feet_entry.grid(row=0,column=1,sticky=(tk.W,tk.E))
        feet_entry.bind('<Key-Return>',self.calculate)
        tk.Label(root, text="feet").grid(row=0,column=2,sticky=tk.W)
        tk.Label(root, text="is equivalent to").grid(row=1,column=0,sticky=tk.E)     
        self.meters = tk.StringVar()
        tk.Label(root, textvariable=self.meters).grid(row=1,column=1,
                                                      sticky=(tk.W,tk.E))
        tk.Label(root, text="meters").grid(row=1,column=2,sticky=tk.W)

    def calculate(self,*args):
        try:
            value = float(self.feet.get())
            self.meters.set(round((0.3048 * value * 10000.0 + 0.5)/10000.0,6))
        except ValueError:
            print("Please enter a number and press calculate / return")

tkConvert().mainloop()              # run the GUI (until window is closed)


# Many more examples can be found in the Graphics and GUI Extensions section.



##
##  END
##
