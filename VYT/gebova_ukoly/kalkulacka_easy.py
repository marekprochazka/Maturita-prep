from tkinter import *

# úkol 14_2

"""

Funkce, které se volají u jednotlivých tlačítek.
Na vstupu vždy berou 2 čísla a místo (label), kam se má zapsat výsledek.
Pokud uživatel napíše něco jinýho, jak 2 čísla, tak program dostane ValueError, 
který se zachytí exceptem (ValueError vzniká na řádku, kde probíhá výpočet a 
konverze čísla na float v základu je totiž string)
zápis do labelu se dělá za pomocí klíčového argumentu 'text' 

"""
def scitani(prvni, druhy, label):
    try:
        vysledek = float(prvni) + float(druhy)
        label["text"] = f"Výsledek: {vysledek}"
    except ValueError:
        label["text"] = "Neplatný zápis!"

def odcitani(prvni, druhy, label):
    try:
        vysledek = float(prvni) - float(druhy)
        label["text"] = f"Výsledek: {vysledek}"
    except ValueError:
        label["text"] = "Neplatný zápis!"

def nasobeni(prvni, druhy, label):
    try:
        vysledek = float(prvni) * float(druhy)
        label["text"] = f"Výsledek: {vysledek}"
    except ValueError:
        label["text"] = "Neplatný zápis!"

def deleni(prvni, druhy, label):
    try:
        vysledek = float(prvni) / float(druhy)
        label["text"] = f"Výsledek: {vysledek}"
    except ValueError:
        label["text"] = "Neplatný zápis!"
    except ZeroDivisionError:
        label["text"] = "Nulou nelze dělit!"

# def deleni(prvni, druhy, label):
#     try:
#         if int(druhy) == 0:
#             label["text"] = "Nulou nelze dělit!"
#         else:
#             vysledek = int(prvni) / int(druhy)
#             label["text"] = f"Výsledek: {vysledek}"
#     except ValueError:
#         label["text"] = "Neplatný zápis!"


# HLavní okono a nastavení jeho rozměrů
main = Tk()
main.geometry("500x60")

# Definice prvků
cislo_1 = Entry(main,width=100)
cislo_2 = Entry(main,width=100)
vysledek = Label(main,text="Výsledek: ")
"""

Definice tlačítek
Tlačítka musí být až jako poslední, protože do nich dáváme Entryes a Label,
které už musí být definovány.
Tlačítka mají svůj command podle operace. 
Command se určuje pomocí lambdy (definice funkce na jednom řádku/ náhrada syntaxe s 'def').
Kdyby tam nebyla lambda, ale jenom normální funkce se závorkama a hodnotama v ní (znamená, že se volá),
tak by se spustila hned při spuštění programu. Lambda tomu zabraňuje a funkce se spustí opravdu jen po stisku tlačítka.
Hodnoty čísel se získavají z Entryes za pomocí funkce 'get()', která vrací hodnotu ve stringu.

"""
plus = Button(main,text="+",width=4, command=lambda: scitani(cislo_1.get(),cislo_2.get(),vysledek))
minus = Button(main,text="-",width=4, command=lambda: odcitani(cislo_1.get(),cislo_2.get(),vysledek))
krat = Button(main,text="*",width=4, command=lambda: nasobeni(cislo_1.get(),cislo_2.get(),vysledek))
deleno = Button(main,text="/",width=4, command=lambda: deleni(cislo_1.get(),cislo_2.get(),vysledek))

# Nastavení velikosti a fontu pro výsledek
vysledek.config(font=("Courier", 16))

"""

'Vkládání' prvků/elementů do okna.
Využit způsob gridu.
V prvním řádku vše, kromě výsledku.
padx/paddy = padding na ose x/y (mezery/odstupy/odsazení)

výsledek má columnspan, to znamená, že zabýrá 6 sloupců => roztáhne se po celé šířce
"""

cislo_1.grid(row=0,column=0,padx=6,pady=3)
plus.grid(row=0 ,column=1,padx=2,pady=3)
minus.grid(row=0 ,column=2,padx=2,pady=3) 
krat.grid(row=0 ,column=3,padx=2,pady=3)
deleno.grid(row=0 ,column=4,padx=2,pady=3)
cislo_2.grid(row=0 ,column=5,padx=6,pady=3)
vysledek.grid(row=1 ,column=0, columnspan=6)

"""
sloupce 0 a 5 (Entryes) dostávají větší 'váhu' => více se roztáhnou
"""
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(5, weight=1)


main.mainloop()

