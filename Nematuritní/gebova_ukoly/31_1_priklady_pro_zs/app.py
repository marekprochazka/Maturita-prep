import tkinter as tk
from random import randint, choice

aktualni_vysledek = None
spravne_odpovedi = 0
spatne_odpovedi = 0

def zamkni_tlacitka(tlacitka):
    for tlacitko in tlacitka:
        tlacitko.config(state=tk.DISABLED)

def odemkni_tlacitka(tlacitka):
    for tlacitko in tlacitka:
        tlacitko.config(state=tk.NORMAL)

def generuj_plus(cislo1_label,cislo2_label,znameko_label,tlacitka):
    global aktualni_vysledek
    cislo1 = randint(1,100)
    cislo2 = randint(1,100-cislo1)
    aktualni_vysledek = cislo1+cislo2
    cislo1_label.config(text=cislo1)
    cislo2_label.config(text=cislo2)
    znameko_label.config(text="+")
    zamkni_tlacitka(tlacitka)

def generuj_minus(cislo1_label,cislo2_label,znameko_label,tlacitka):
    global aktualni_vysledek
    cislo1 = randint(1,100)
    cislo2 = randint(1,cislo1)
    aktualni_vysledek = cislo1-cislo2
    cislo1_label.config(text=cislo1)
    cislo2_label.config(text=cislo2)
    znameko_label.config(text="-")
    zamkni_tlacitka(tlacitka)

def generuj_krat(cislo1_label,cislo2_label,znameko_label,tlacitka):
    global aktualni_vysledek
    cislo1 = randint(2,10)
    cislo2 = randint(2,10)
    aktualni_vysledek = cislo1*cislo2
    cislo1_label.config(text=cislo1)
    cislo2_label.config(text=cislo2)
    znameko_label.config(text="*")
    zamkni_tlacitka(tlacitka)

def generuj_deleno(cislo1_label,cislo2_label,znameko_label,tlacitka):
    global aktualni_vysledek
    cislo2 = randint(2,10)
    vysledek = randint(2,20)
    cislo1 = cislo2*vysledek
    cislo1_label.config(text=cislo1)
    cislo2_label.config(text=cislo2)
    znameko_label.config(text="/")
    zamkni_tlacitka(tlacitka)

def kontroluj_fce(vstup_vysledek,skore_label,cislo1_label,cislo2_label,znameko_label, tlacitka):
    global aktualni_vysledek, spravne_odpovedi, spatne_odpovedi
    if int(vstup_vysledek.get()) if vstup_vysledek.get() else None == aktualni_vysledek:
        spravne_odpovedi += 1
    else: 
        spatne_odpovedi +=1
    skore_label.config(text=f"{spravne_odpovedi}/{spatne_odpovedi} (správné/špatné)")
    cislo1_label.config(text="")
    cislo2_label.config(text="")
    znameko_label.config(text="")
    vstup_vysledek.delete(0,"end")
    vstup_vysledek.insert(0,"")
    odemkni_tlacitka(tlacitka)

def validuj_cislo(cislo):
    if cislo.isdigit() or cislo == "":
        return True
    return False


hlavni = tk.Tk() 
validacni_prikaz = (hlavni.register(validuj_cislo))


nadpis = tk.Label(hlavni,text="Operace:")
operace_plus = tk.Button(hlavni, text="+")
operace_minus = tk.Button(hlavni, text="-")
operace_krat = tk.Button(hlavni, text="*")
operace_deleno = tk.Button(hlavni, text="/")

tlacitka = (operace_plus,operace_minus,operace_krat,operace_deleno)

cislo1 = tk.Label(hlavni,text="")
znameko = tk.Label(hlavni, text="")
cislo2 = tk.Label(hlavni,text="")
rovnitko = tk.Label(hlavni,text="=")
vstup_vysledek = tk.Entry(hlavni, justify="center", validate="all", validatecommand=(validacni_prikaz,"%P"))

kontroluj = tk.Button(hlavni,text="vyhodnotit")
skore = tk.Label(hlavni, text="0/0")

operace_plus.config(command=lambda: generuj_plus(cislo1,cislo2,znameko,tlacitka))
operace_minus.config(command=lambda: generuj_minus(cislo1,cislo2,znameko,tlacitka))
operace_krat.config(command=lambda: generuj_krat(cislo1,cislo2,znameko,tlacitka))
operace_deleno.config(command=lambda: generuj_deleno(cislo1,cislo2,znameko,tlacitka))
kontroluj.config(command=lambda: kontroluj_fce(vstup_vysledek,skore,cislo1,cislo2,znameko,tlacitka))


nadpis.grid(row=0,column=0)
operace_plus.grid(row=0,column=4, ipadx=6)
operace_minus.grid(row=0,column=5, ipadx=6)
operace_krat.grid(row=0,column=6, ipadx=6)
operace_deleno.grid(row=0,column=7, ipadx=6)

cislo1.grid(row=1,column=0)
znameko.grid(row=1,column=1)
cislo2.grid(row=1,column=2)
rovnitko.grid(row=1,column=3)
vstup_vysledek.grid(row=1,column=4,columnspan=4,ipadx=20)

kontroluj.grid(row=2,column=0)
skore.grid(row=3,column=0,columnspan=3)


hlavni.wm_geometry("400x150")
hlavni.title("Příklady pro ZŠ") #KAŽDEJ ZMĚNIT
hlavni.mainloop()