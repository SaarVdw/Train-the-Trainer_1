from tkinter import *
from tkinter import ttk
from tkinter import font

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def greeting():
    ttk.Label(mainframe, text="Hi, happy calculating!", font=lettertype, style="PP.TLabel").grid(column=1, row=5, sticky=(S, E))


def finished():
    ttk.Label(mainframe, text="Please select how you feel about this calculator: ", font=funfont, style="CC.TLabel").grid(column=1, row=6, sticky=(W, N), padx=5, pady=15)
    choices = ["nice lay-out", "ugly", "nice enough", "such fun!", "not inspiring", "great!"]
    choicesvar = StringVar(value=choices)
    l = Listbox(mainframe, listvariable=choicesvar, height=6).grid(column=2, row=6)
    choicesvar.set(choices)

root = Tk()
root.title("Feet to Meters")
root.iconbitmap(r"C:\Users\vandewsa\Downloads\png-clipart-red-fox-drawing-fox-mammal-child.ico")

style = ttk.Style()
style.configure("BW.TLabel", foreground="#f52c6b", background="#fddfee")

style = ttk.Style()
style.configure("PP.TLabel", foreground="#4c8ff7", background="#fddfee")

style = ttk.Style()
style.configure("CC.TLabel", foreground="#FFFFFF", background="#D52366")

lettertype = font.Font(family="Garamond", size=20, slant="italic", underline=1)

funfont = font.Font(family="Baskerville", size=10)

mainframe = ttk.Frame(root, padding="3 3 12 12", style="BW.TLabel")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="welcome to the calculator", font=lettertype, style="PP.TLabel").grid(column=1, row=1, sticky=(N, W))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters, style="BW.TLabel").grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Button(mainframe, text="click me", command=greeting).grid(column=1, row=4, sticky=(S, E))

ttk.Label(mainframe, text="feet", style="BW.TLabel").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="is equivalent to", style="BW.TLabel").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="meter", style="BW.TLabel").grid(column=3, row=3, sticky=W)

ttk.Button(mainframe, text="Finished?", command=finished).grid(column=3, row=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()