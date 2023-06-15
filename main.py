from tkinter import *

okno = Tk()
okno.geometry('500x700')
okno.title('Kvíz')




Label(okno, text='Zadajte meno').grid(row=1, column=1)
meno = StringVar()
Entry(okno, textvariable=meno).grid(row=2,column=1)

okno.mainloop()