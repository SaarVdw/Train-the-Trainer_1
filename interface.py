from tkinter import *
from tkinter import font

app = Tk()
app.title("LEUKHEIDSMETER")
app.geometry="400x400"
app.configure(bg='#f0c71e')

def info():
    lettertype = font.Font(family='Braggadocio', name='appletterype', size=25, weight='normal', underline=1)
    info = Label(app, text='Leukste Team', font=lettertype, fg='#690f2d', bg='#f0c71e')
    info.grid(row=2, column=5)

DIT = Button(app, text="Data interventieteam", width=25, bg='#690f2d', fg='#ff6699', borderwidth=10, command=info)
DIT.grid(row=2, column=2)

highlightFont = font.Font(family='Chalkboard', name='appHighlightFont', size=25, weight='normal', underline = 1)
Cool = Label(app, text="Super leuk label", font = highlightFont, height=10, width=20, bg='#ff6699', fg="#0f0c63")
Cool.grid(row=4,column=3)

input = Entry(app, width=30, borderwidth=10)
input.grid(row=8,column=3)

namenlijst = StringVar(app)
namenlijst.set("kies de leukheid")
Menutje = OptionMenu(app, namenlijst, 'Leuk', 'Leuker', 'Leukst')
Menutje.grid(row=1,column=2)

box = Checkbutton(app, text='BERE NICE', bg='#ff6699', fg='#690f2d')
box.grid(row=5,column=2)

app.mainloop()