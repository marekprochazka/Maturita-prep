# 14. Programování - Funkce, moduly


## Funkce
- Nechceme-li psát programy imperativně (= tak, že se čtou od shora dolů), je třeba využít funkcí. 
- Taková metoda programování se logicky nazívá funkcionální 
- Funkce se dá v programu opakovat a za pomocí vstupních argumentů se dá i na různých místech diverzifikovat možný výstup funkce
- Funkce obvykle přijímá argumenty (data, která zpracuje) a něco vrací - nějakou výslednou hodnotu apod. (ale taky nemusí vracet nic jako např. funkce print()).
## Základní syntaxe

```python
# definice funkce
def mocnina(cislo): 
    cislo = cislo ** 2
    return cislo

# volání funkce
promenna = mocnina(4)
print(mocnina(3))
```
- funkce obvykle přijímá argumenty (data, která zpracuje) a něco vrací – výslednou hodnotu; funkce taky nemusí vracet nic (př. funkce print())

## Syntaxe:
- def – syntax značící definici funkce
- mocnina – název funkce
- hodnoty v závorce (cislo) – Parametry funkce, které se zadávají při volání funkce; může jich být samozřejmě více
    - Povinné – když je uživatel nedosadí, tak funkce neproběhne a program vyhodí chybu (v příkladu je to cislo)
    - Implicitní (defaultní) – parametry, které jsou již předdefinované, ale dají se při volání funkce změnit, např. def fce(cislo, n=1)
    - Nepovinné – např. def fce(*y), y bude n-tice o libovolné délce, tzn. nemusí se zadat žádné parametry ale taky hodně úplně
- return – (návratová) hodnota, kterou funkce vrátí – může se uložit do proměnné, nebo vytisknout; pokud ve funkci chybí return a například jen něco tiskneme, tak se první vytiskne hodnota None, poté to co chceme, většinou se píše na konec, pokud return napíšeme někam doprostřed tak se funkce přeruší (prakticky to funguje jako break), může být ve funkci i vícekrát, ale pak je vhodné to nějak upravit pomocí if
- celou funkci lze ukončit příkazem break

## argumenty
- argumenty jsou hodnoty, které zadáváme při volání funkce
- argumenty musíme určit v definici funkce 
- argumenty mohou mít nastavenou základní hodnotu, která se používá, pokud není při volání zadána hodnota jiná
- při volání můžeme argumenty zadat 2 způsoby:
    - poziční: nezadává se jméno argumentu, ale pouze se vkládá hodnota na správnou pozici
    - klíčové: zadává se název argumetnu a jeho určená hodnota
- pokud má funkce přijmout neurčitý počet argumentů nebo klíčových argumentů, tak se používá syntaxe
 '*' a '**', tyto znaky se napíší před název proměnné. Do proměnné se poté uloží argumenty ve formě seznamu
  u pozičních a ve formě slovníku u klíčových (běžně se používají názvy 'args' a 'kwargs')
- příklad:

```python
def zakladni(prvni, druhy, treti):
    ...

def s_defaultem(prvni=1,druha=2,treti): # základní hodnota určená u prvních dvou argumentů
    ...

def argumenty(*args): # bere neurčitý počet pozičních argumentů, pak je postupně vypíše
    for arg in args:
        print(arg)

def k_argumenty(**kwargs): # bere neurčitý počet klíčových argumentů, pak postupně vypíše všechny páry (klíč,hodnota)
    for kwarg_key, kwarg_value in kwargs.items():
        print(kwarg_key, kwarg_value)

zakladni(1,2,3) # zadávání argumentů pozičně

zakladni(treti=3, prvni=1,druhy=2) # zádávání arkumentů klíčově (díky tomu je možno zadávat argumenty v různém pořadí, ale nedporučuju to)

```

### rekurze
- Rekurze označuje když funkce volá sama sebe. Lze ji použít například na výpočet faktoriálu.

```python
def faktorial(cislo):
    if cislo > 0:
        return faktorial(cislo - 1) * cislo
    else:
        return 1
```
- Lokální a globální proměnné:
    - lokální proměnné vznikají ve funkci, tzn. jsou použitelné pouze v té samotné proměnné, tzn. můžeme mít v programu třeba dvě proměnné x, jednu ve funkci a druhou mimo ni a jedná se o dvě nezávislé proměnné
    - pokud ve funkci ale použijeme global x, tak se sjednotí a bude existovat již pouze jedna proměnná x
- Volání funkce komponentou:
    - knihovna Tkinter, komponentou je třeba tlačítko
    - ke komponentě doplníme command, a do něho dáme pouze název (adresu) funkce (ne závorky, ne parametry), tím se fce spustí až poté, co se na tlačítko klikne
- Lambda funkce:
    - jednoduše to je definice funkce na jediném řádku
    - oproti normální funkci jí chybí název, nedá se zavolat
    - výhodou je šetření místa, nevýhodou horší přehlednost
    - používá se pro krátké, jednorázové operace, např. v Tkinteru


## Moduly
- Python modulem můžeme nazvat python soubor, ze kterého za pomocí syntaxe 'import' importujeme funkce, proměnné, nebo třídy
- Python má své základní moduly jako například math, random, uuid, sqlite, které jsou součástí základní instalace pythonu
- Za využití syntaxe pip v příkazové řádce je možno stáhnout jiné moduly, které nejsou součástí základního pythonu
- Uživatel si také může jednoduše vytvářet své vlastní moduly (stačí si někde definovat funkci a tu funkci importnout do jiný souboru a wuala... Modul...)

sauce:
> https://www.itnetwork.cz/python/zaklady/python-tutorial-funkce-a-vyjimky <br>
> https://naucse.python.cz/lessons/beginners/modules/ 