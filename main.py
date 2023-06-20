import random
from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title('Kvíz')
okno.config(bg='#46178f')
photo = PhotoImage(file = 'ikonka.png')
okno.wm_iconphoto(False, photo)

# Vyrovnaie okna
window_width = okno.winfo_screenwidth()
window_height = okno.winfo_screenheight()
x_coordinate = int((window_width / 2) - (500 / 2))
y_coordinate = int((window_height / 2) - (700 / 2))
okno.geometry(f"500x650+{x_coordinate}+{y_coordinate}")

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
    checker = True
    for i in s_znaky:
        if i in m:
            messagebox.showwarning('Pozor!', 'Meno obsahuje nepovolené znaky!')
            meno.set('')
            checker = False
    if len(m) >= 30:
        messagebox.showwarning('Pozor!', 'Meno je príliš dlhé!')
        meno.set('')
        checker =  False
    if len(m) == 0:
        messagebox.showwarning('Pozor!', 'Meno je prázdne!')
        meno.set('')
        checker = False
    if checker == True:
        meno_label.destroy()
        meno_entry.destroy()
        zacat_button.destroy()
        spusti_kviz()
    else:
        meno.get()

def spusti_kviz():
    '''
    Táto funkcia spustí kvíz po zadaní mena s použitím global indexovania z otázok
    '''
    global aktualna_otazka_index
    global counter

    # Zobrazenie odpovedových tlačidiel
    otazka_label.pack()
    odpoved1_button.pack(fill=X)
    odpoved2_button.pack(fill=X)
    odpoved3_button.pack(fill=X)
    odpoved4_button.pack(fill=X)

    def body1():
        if odpoved1_button["text"] == otazka_odpovede[1]:
            global counter
            counter += 1
    def body2():
        if odpoved2_button["text"] == otazka_odpovede[1]:
            global counter
            counter += 1
    def body3():
        if odpoved3_button["text"] == otazka_odpovede[1]:
            global counter
            counter += 1
    def body4():
        if odpoved4_button["text"] == otazka_odpovede[1]:
            global counter
            counter += 1

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
    otazka_label.config(text=otazka_odpovede[0], pady=10, bg='#46178f', fg='white')
    odpoved1_button.config(text=otazka_odpovede1, height=3,command=lambda: (body1(), zobraz_novu_otazku()), bg='#e21a3c', fg='white', font=('Arial', 20))
    odpoved2_button.config(text=otazka_odpovede2, height=3, command=lambda: (body2(), zobraz_novu_otazku()), bg='#1368CE', fg='white', font=('Arial', 20))
    odpoved3_button.config(text=otazka_odpovede3, height=3, command=lambda: (body3(), zobraz_novu_otazku()), bg='#26890C', fg='white', font=('Arial', 20))
    odpoved4_button.config(text=otazka_odpovede4, height=3, command=lambda: (body4(), zobraz_novu_otazku()), bg='#FFA502', fg='white', font=('Arial', 20))
    counter_label.config(text=f'Body: {counter}', height=3, font=('Arial', 15), fg='white')

    counter_label.pack()
    counter_label.config(bg='#46178f')
    aktualna_otazka_index += 1

def zobraz_novu_otazku():
    '''
    Táto funkcia zobrazí novú otázku po kliknutí na odpoveď
    '''
    def close():
        okno.destroy()
    def percenta():
        vysledok = 100 // len(otazky) * counter
        return vysledok
    odpoved1_button.pack_forget()
    odpoved2_button.pack_forget()
    odpoved3_button.pack_forget()
    odpoved4_button.pack_forget()
    counter_label.pack_forget()

    if aktualna_otazka_index < len(otazky):
        spusti_kviz()
    else:
        otazka_label.pack_forget()
        end_button = Button(okno, text='Skončiť program', command=lambda: close(), font=('Arial', 14))
        end_button.pack()
        messagebox.showinfo('Kvíz', f'{meno.get()} získal si {counter} z {len(otazky)} bodov. ({percenta()}%)')

meno_label = Label(okno, text='Zadajte meno', font=("Arial", 16), bg='#46178f', fg='white')
meno_label.pack(pady=10)
meno = StringVar()
meno_entry = Entry(okno, textvariable=meno, font=("Arial", 14), fg='black', bg='white', bd=0)
meno_entry.pack()
zacat_button = Button(okno, text='Začať kvíz', command=over_meno, font=("Arial", 14), bg='#864cbf', fg='white')
zacat_button.pack(pady=20)

otazky = nacitaj_otazky('otazky.txt')
aktualna_otazka_index = 0
counter = 0

otazka_label = Label(okno, text='', font=("Arial", 18))
otazka_label.pack()
otazka_label.forget()

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

counter_label = Label(okno, text='')
counter_label.pack()
counter_label.pack_forget()

okno.mainloop()
