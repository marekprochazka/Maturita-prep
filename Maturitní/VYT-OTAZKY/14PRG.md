# 14. Programování - Funkce, moduly

> metody jako nic ? Ajo... oni vlastně neví co je to OOP... 

## Funkce
- Nechceme-li psát programy imperativně (= tak, že se čtou od shora dolů), je třeba využít funkcí. 
- Taková metoda programování se logicky nazívá funkcionální 
- Funkce se dá v programu opakovat a za pomocí vstupních argumentů se dá i na různých místech diverzifikovat možný výstup funkce
- Funkce obvykle přijímá argumenty (data, která zpracuje) a něco vrací - nějakou výslednou hodnotu apod. (ale taky nemusí vracet nic jako např. funkce print()).
### Základní syntaxe

```python
# definice funkce
def mocnina(cislo): 
    cislo = cislo ** 2
    return cislo

# volání funkce
promenna = mocnina(4)
print(mocnina(3))
```
- def = syntax značící definici funkce
- mocnina = název funkce 
- hodnoty v závorce - (cislo) = argumenty funkce, které se zadávájí při volání funkce
- return = hodnota, kterou program "vrátí" => můžeme ji například uložit do proměnné, nebo vytisknout jako v příkladu

### argumenty
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

## Moduly
- Python modulem můžeme nazvat python soubor, ze kterého za pomocí syntaxe 'import' importujeme funkce, proměnné, nebo třídy
- Python má své základní moduly jako například math, random, uuid, sqlite, které jsou součástí základní instalace pythonu
- Za využití syntaxe pip v příkazové řádce je možno stáhnout jiné moduly, které nejsou součástí základního pythonu
- Uživatel si také může jednoduše vytvářet své vlastní moduly (stačí si někde definovat funkci a tu funkci importnout do jiný souboru a wuala... Modul...)

sauce:
> https://www.itnetwork.cz/python/zaklady/python-tutorial-funkce-a-vyjimky <br>
> https://naucse.python.cz/lessons/beginners/modules/ 