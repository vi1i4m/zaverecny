from tkinter import *
from tkinter import messagebox
import random

okno = Tk()
okno.geometry('500x700')
okno.title('Kvíz')

def over_meno():
    '''
    funkcia načíta meno a skontroluje, či nie je príliš dlhé alebo neobsahuje nepovolené znaky (ak áno - vyskočí okno s chybovou správou), potom hodnotu vo vstupe vymaže
    '''
    m = meno.get()
    s_znaky = '@_-ß°{()}#*&[]\;|?><:~,€/ŁłĐđ÷×¤$'
    for i in s_znaky:
        if i in m:
            messagebox.showwarning('Pozor!', 'Meno obsahuje nepovolené znaky!')
            meno.set('')
    if len(m) >= 30:
        messagebox.showwarning('Pozor!', 'Meno je príliš dlhé!')
        meno.set('')
    #treba este nastavit prekliknutie na kviz

def nacitaj_otazky(subor):
    '''
    funkcia, ktorá spracuje súbor s otázkami a vráti pseudonáhodnú otázku
    '''
    with open(subor, 'r', encoding="utf-8") as f:
        otazka = f.read().splitlines()
    return random.choice(otazka)



Label(okno, text='Zadajte meno').grid(row=1, column=1)
meno = StringVar()
Entry(okno, textvariable=meno).grid(row=2,column=1)
Button(okno, text='Začať kvíz', command=over_meno).grid(row=3, column=1)

okno.mainloop()