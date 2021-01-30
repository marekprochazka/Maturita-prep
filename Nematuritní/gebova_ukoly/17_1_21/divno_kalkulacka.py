import tkinter as tk
from tkinter import StringVar

def soucet(a,b,label):
    label["text"] = int(a) + int(b)
def soucin(a,b,label):
    label["text"] = int(a) * int(b)
def podil(a,b,label):
    label["text"] = int(a) - int(b)
def rozdil(a,b,label):
    try:
        label["text"] = int(a) / int(b)
    except ZeroDivisionError:
        label["text"] = "Nesmíš dělit nulou"
def default(label):
    label["text"] = "Nebyla zvolena žádná operace"

def evaluale(operace, a, b, vysledek_label):
    if operace == "součet":
        soucet(a,b,vysledek_label)
    elif operace == "součin":
        soucin(a,b,vysledek_label)
    elif operace == "podíl":
        podil(a,b,vysledek_label)
    elif operace == "rozdíl":
        rozdil(a,b,vysledek_label)
    else:
        default(vysledek_label)


main = tk.Tk()

spin_A = tk.Spinbox(main, from_=-100, to=100)
spin_B = tk.Spinbox(main, from_=-100, to=100)
vysledek = tk.Label(main,text="0", width=5)
hodnoty = ("součet","součin","podíl","rozdíl")
promenna_volitka = StringVar()
volitko = tk.OptionMenu(main,promenna_volitka,*hodnoty)
promenna_volitka.set(hodnoty[0])
tlacitko = tk.Button(main,text="Vypočítej to už", command=lambda: evaluale(promenna_volitka.get(),spin_A.get(),spin_B.get(),vysledek))

elementy = (spin_A,spin_B,vysledek,volitko,tlacitko)

for element in elementy:
    element.pack(fill="both", expand=True)



main.mainloop()