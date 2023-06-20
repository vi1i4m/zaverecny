import random
from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title('Kvíz')

# Vyrovnaie okna
window_width = okno.winfo_screenwidth()
window_height = okno.winfo_screenheight()
x_coordinate = int((window_width / 2) - (500 / 2))
y_coordinate = int((window_height / 2) - (700 / 2))
okno.geometry(f"500x600+{x_coordinate}+{y_coordinate}")

def nacitaj_otazky(subor):
    '''
    funkcia, ktorá spracuje súbor s otázkami a vráti zoznam otázok
    '''
    with open(subor, 'r', encoding="utf-8") as f:
        otazky = f.read().splitlines()
    return random.choice(otazky)

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
    if len(m) == 0:
        messagebox.showwarning('Pozor!', 'Meno je prázdne!')
        meno.set('')
        

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
    otazka_odpovede1 = otazka_odpovede[random.randint(1, 4)]
    otazka_odpovede2 = otazka_odpovede[random.randint(1, 4)]
    otazka_odpovede3 = otazka_odpovede[random.randint(1, 4)]
    otazka_odpovede4 = otazka_odpovede[random.randint(1, 4)]
    while otazka_odpovede1 == otazka_odpovede2 or otazka_odpovede1 == otazka_odpovede3 or otazka_odpovede1 == otazka_odpovede4:
        otazka_odpovede1 = otazka_odpovede[random.randint(1, 4)]
    while otazka_odpovede1 == otazka_odpovede2 or otazka_odpovede2 == otazka_odpovede3 or otazka_odpovede2 == otazka_odpovede4:
        otazka_odpovede2 = otazka_odpovede[random.randint(1, 4)]
    while otazka_odpovede1 == otazka_odpovede3 or otazka_odpovede2 == otazka_odpovede3 or otazka_odpovede3 == otazka_odpovede4:
        otazka_odpovede3 = otazka_odpovede[random.randint(1, 4)]
    while otazka_odpovede1 == otazka_odpovede4 or otazka_odpovede2 == otazka_odpovede4 or otazka_odpovede3 == otazka_odpovede4:
        otazka_odpovede4 = otazka_odpovede[random.randint(1, 4)]
    otazka_label.config(text=otazka_odpovede[0])
    odpoved1_button.config(text=otazka_odpovede1, command=lambda: zobraz_novu_otazku())
    odpoved2_button.config(text=otazka_odpovede2, command=lambda: zobraz_novu_otazku())
    odpoved3_button.config(text=otazka_odpovede3, command=lambda: zobraz_novu_otazku())
    odpoved4_button.config(text=otazka_odpovede4, command=lambda: zobraz_novu_otazku())

    # Zobrazenie odpovedových tlačidiel
    odpoved1_button.pack(fill=X)
    odpoved2_button.pack(fill=X)
    odpoved3_button.pack(fill=X)
    odpoved4_button.pack(fill=X)

    aktualna_otazka_index += 1

def zobraz_novu_otazku():
    '''
    Táto funkcia zobrazí novú otázku po kliknutí na odpoveď
    '''
    odpoved1_button.pack_forget()
    odpoved2_button.pack_forget()
    odpoved3_button.pack_forget()
    odpoved4_button.pack_forget()

    if aktualna_otazka_index < len(otazky):
        spusti_kviz()
    else:
        messagebox.showinfo('Kvíz', 'Kvíz skončil')

meno_label = Label(okno, text='Zadajte meno', font=("Arial", 16))
meno_label.pack()
meno = StringVar()
meno_entry = Entry(okno, textvariable=meno, font=("Arial", 14))
meno_entry.pack()
zacat_button = Button(okno, text='Začať kvíz', command=over_meno, font=("Arial", 14))
zacat_button.pack()

otazky = nacitaj_otazky('otazky.txt')
aktualna_otazka_index = 0

otazka_label = Label(okno, text='', font=("Arial", 18))
otazka_label.pack()

odpoved1_button = Button(okno, text='', font=("Arial", 14))
odpoved1_button.pack()
odpoved1_button.pack_forget()  # Skrytie tlačidla

odpoved2_button = Button(okno, text='', font=("Arial", 14))
odpoved2_button.pack()
odpoved2_button.pack_forget()

odpoved3_button = Button(okno, text='', font=("Arial", 14))
odpoved3_button.pack()
odpoved3_button.pack_forget()

odpoved4_button = Button(okno, text='', font=("Arial", 14))
odpoved4_button.pack()
odpoved4_button.pack_forget()

okno.mainloop()
