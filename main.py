from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.geometry('500x700')
okno.title('Kvíz')
okno.rowconfigure(50)
okno.columnconfigure(50)

def nacitaj_otazky(subor):
    '''
    funkcia, ktorá spracuje súbor s otázkami a vráti zoznam otázok
    '''
    with open(subor, 'r', encoding="utf-8") as f:
        otazky = f.read().splitlines()
    return otazky

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
    '''
    Táto funkcia spustí kvíz po zadaní mena s použitím global indexovania z otázok
    '''
    global aktualna_otazka_index
    otazka_odpovede = otazky[aktualna_otazka_index].split('-')
    otazka_label.config(text=otazka_odpovede[0])
    odpoved1_button.config(text=otazka_odpovede[1], command=lambda: zobraz_novu_otazku())
    odpoved2_button.config(text=otazka_odpovede[2], command=lambda: zobraz_novu_otazku())
    odpoved3_button.config(text=otazka_odpovede[3], command=lambda: zobraz_novu_otazku())
    odpoved4_button.config(text=otazka_odpovede[4], command=lambda: zobraz_novu_otazku())

    #Zobrazenie odpovedových tlačidiel
    odpoved1_button.grid()
    odpoved2_button.grid()
    odpoved3_button.grid()
    odpoved4_button.grid()

    aktualna_otazka_index += 1

def zobraz_novu_otazku():
    '''
    Táto funkcia zobrazí novú otázku po kliknutí na odpoveď
    '''
    odpoved1_button.grid_remove()
    odpoved2_button.grid_remove()
    odpoved3_button.grid_remove()
    odpoved4_button.grid_remove()

    if aktualna_otazka_index < len(otazky):
        spusti_kviz()
    else:
        messagebox.showinfo('Kvíz', 'Kvíz skončil')

meno_label = Label(okno, text='Zadajte meno')
meno_label.grid(row=1, column=1)
meno = StringVar()
meno_entry = Entry(okno, textvariable=meno)
meno_entry.grid(row=2, column=1)
zacat_button = Button(okno, text='Začať kvíz', command=over_meno)
zacat_button.grid(row=3, column=1)

otazky = nacitaj_otazky('otazky.txt')
aktualna_otazka_index = 0

otazka_label = Label(okno, text='')
otazka_label.grid(row=4, column=1, columnspan=2)

odpoved1_button = Button(okno, text='')
odpoved1_button.grid(row=5, column=1)
odpoved1_button.grid_remove() #Skrytie tlačidla

odpoved2_button = Button(okno, text='')
odpoved2_button.grid(row=5, column=2)
odpoved2_button.grid_remove()

odpoved3_button = Button(okno, text='')
odpoved3_button.grid(row=6, column=1)
odpoved3_button.grid_remove()

odpoved4_button = Button(okno, text='')
odpoved4_button.grid(row=6, column=2)
odpoved4_button.grid_remove()

okno.mainloop()
