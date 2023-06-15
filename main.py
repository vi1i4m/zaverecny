from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.geometry('500x700')
okno.title('Kvíz')

def over_meno():
    m = meno.get()
    s_znaky = '@_-ß°{()}#*&[]\;|?><:~,€/ŁłĐđ÷×¤$'
    for i in s_znaky:
        if i in m:
            messagebox.showwarning('Pozor!', 'Meno obsahuje nepovolené znaky')
            meno.set('')
            


Label(okno, text='Zadajte meno').grid(row=1, column=1)
meno = StringVar()
Entry(okno, textvariable=meno).grid(row=2,column=1)
Button(okno, text='Začať kvíz', command=over_meno).grid(row=3, column=1)

okno.mainloop()