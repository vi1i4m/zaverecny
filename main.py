from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.geometry('500x700')
okno.title('Kvíz')
okno.rowconfigure(50)
okno.columnconfigure(50)

def nacitaj_otazky(subor):
    '''
    funkcia, ktorá spracuje súbor s otázkami a vráti pseudonáhodnú otázku
    '''
    with open(subor, 'r', encoding="utf-8") as f:
        otazka = f.read().splitlines()
    return otazka[0]

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
            return
    if len(m) >= 30:
        messagebox.showwarning('Pozor!', 'Meno je príliš dlhé!')
        meno.set('')
        return
    if len(m) == 0:
        messagebox.showwarning('Pozor!', 'Meno je prázdne!')
        meno.set('')
        return

    meno_label.destroy()
    meno_entry.destroy()
    zacat_button.destroy()

    spusti_kviz()

def spusti_kviz():
    otazka = nacitaj_otazky('otazky.txt')
    otazka_label.config(text=otazka)
    odpoved1_button.config(text='Odpoveď 1')
    odpoved2_button.config(text='Odpoveď 2')
    odpoved3_button.config(text='Odpoveď 3')
    odpoved4_button.config(text='Odpoveď 4')

    #Zobrazenie odpovedových tlačidiel
    odpoved1_button.grid()
    odpoved2_button.grid()
    odpoved3_button.grid()
    odpoved4_button.grid()

meno_label = Label(okno, text='Zadajte meno')
meno_label.grid(row=1, column=1)
meno = StringVar()
meno_entry = Entry(okno, textvariable=meno)
meno_entry.grid(row=2, column=1)
zacat_button = Button(okno, text='Začať kvíz', command=over_meno)
zacat_button.grid(row=3, column=1)

otazka_label = Label(okno, text='')
otazka_label.grid(row=4, column=1, columnspan=2)

odpoved1_button = Button(okno, text='', command=lambda: print('Odpoveď 1'))
odpoved1_button.grid(row=5, column=1)
odpoved1_button.grid_remove() #Skrytie tlačidla

odpoved2_button = Button(okno, text='', command=lambda: print('Odpoveď 2'))
odpoved2_button.grid(row=5, column=2)
odpoved2_button.grid_remove()

odpoved3_button = Button(okno, text='', command=lambda: print('Odpoveď 3'))
odpoved3_button.grid(row=6, column=1)
odpoved3_button.grid_remove()

odpoved4_button = Button(okno, text='', command=lambda: print('Odpoveď 4'))
odpoved4_button.grid(row=6, column=2)
odpoved4_button.grid_remove()

okno.mainloop()
