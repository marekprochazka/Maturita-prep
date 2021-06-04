# 10. Programování - Cyklus for

> https://www.itnetwork.cz/python/zaklady/python-tutorial-cykly-while-for-in-funkce-range-a-vyraz-pass
- Cyklus – v pythonu existují dva typy cyklů, while a for, umožňuje nám opakovat určitý blok kódu, tak dlouho jak potřebujeme
    - while je řízený podmínkou, dokud platí tak se bude plnit
    - for je řízený počtem prvků v dané množině
- for cyklus se nejčastěji používá pro procházení seznamů, n-tic, řetězců…, pokud chceme pro každý prvek provést určitou operaci; nebo pokud máme pevně daný počet cyklů, které chceme provést
- používá se v případě, kdy přesně známe počet opakování, je celkově lepší než while, když ho můžeme použít tak ho použijme
- ve vývojovém diagramu má tvar šestiúhelníku
- Cyklus for má párovou syntaxi for…in

 
- příklad: 
```python
seznam = [1,2,3,4]
for hodnota in seznam:
    print(hodnota) # postupně tiskne 1,2,3...
```

- řídící proměnná je zde hodnota
- blok kódu musí být odsazený
- další syntaxe:
    - break – vyskočí z cyklu
    - continue – pokud proběhne, tak přeskočí zbytek cyklu a začne nanovo s další hodnotou
    - range() – dává seznam celých čísel, do závorek se doplní celé číslo, cyklus poté proběhne tolikrát, jaké je číslo; např. range(10) = cyklus proběhne 10x !počítá od 0, nejvyšší číslo bude 9!
        - může se nastavit i range(2, 10) = cyklus začíná na 2 a končí na 9
        - nastavit například range(1, 4, 2), v tomto případě první číslo značí začáteční hodnotu, druhé číslo kde cyklus skončí a třetí po kolika se vypíše, v tomto případě se tedy vypíše 1, 3

```python
for promenna in range(10):  # promenna bude dosahovat hodnot (0 až 9 v celých číslech)
    print(promenna)
    if promenna == 5:
        break               # cyklus končí ve chvíli, kdy promenna dosáhne hodnoty 5
```

else u cyklu for .. in: U tohto cyklu můžeme využít i syntaxe "else", jejíž blok se spustí po projetí cyklu. 
Pokud cyklus skončí dřív za pomocí break, tak else neproběhne. 

```python
for x in range(3):
    pass 
else: 
    print("konec cyklu")
```
## Vnořené cykly
- jedná se o for smyčku ve for smyčce
- celá „vnitřní smyčka“ proběhne pro každý prvek „vnější smyčky“

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) # vždycky se napíše red apple, red banana, red cherry; big apple, big banana...
```

 
## funkce Enumerate 
- chceme-li při iterování například seznamu znát kromě aktuální hodnoty i index (pozoci v seznamu), 
tak můžeme využít funkce enumerate()

```python 
seznam = ["Já", "Ty", "On","Ona", "Ono"] 

for _index, hodnota in enumarate(seznam):
    print(f"{_index}:{hodnota}")
```
Výsledek: <br> 
0:Já <br>
1:Ty <br>
2:On <br>
atd...


## Iterátory
- Když je v Pythonu potřeba iterovat (např. příkazem for) přes nějakou kolekci (seznam, řetězec, soubor, …), použije se iterační protokol, který pracuje se dvěma druhy objektů: s iterovatelnými objekty a s iterátory.
- erovatelné objekty (iterables) se vyznačují tím, že je na ně možné zavolat funkci iter(). Ta vrátí příslušný iterátor:
```python 
>>> iter([1, 2, 3])
<list_iterator object at 0x...>
```
- Na iterátor pak je možné opakovaně volat funkci next(), čímž dostáváme jednotlivé prvky iterace. Po vyčerpání iterátoru způsobuje next() výjimku StopIteration:

```python 
>>> it = iter([1, 2, 3])
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  ...
StopIteration
next(it)
Traceback (most recent call last):
  ...
StopIteration
```

- Cyklus for x in collection: ... tedy dělá něco jako:

```python 
iterator = iter(collection)
while True:
    try:
        x = next(iterator)
    except StopIteration:
        break

    ...  # tělo původního cyklu
```

- Platí, že každý iterátor je iterovatelný: zavoláním iter() na iterátor dostaneme ten stejný iterátor (nikoli jeho kopii) zpět. Naopak to ale obecně neplatí: např. seznamy jsou iterovatelné, ale nejsou samy o sobě iterátory. Každé zavolání iter(seznam) vrací nový iterátor, který má svou vlastní „aktuální pozici“ a iteruje od začátku.

- Iterátor je ve většině případů „malý“ objekt, který si „pamatuje“ jen původní iterovatelný objekt a aktuální pozici. Příklady jsou iterátory seznamů (iter([])), slovníků (iter({})), n-tic nebo množin, iterátor pro range a podobně.

- Iterátory ale můžou být i „větší“: třeba otevřený soubor je iterátor, z něhož next() načítá jednotlivé řádky.

## Generátory

- Asi nejzajímavější druh iterátoru je tzv. generátor: funkce, která umí postupně dávat k dispozici hodnoty. Definuje se pomocí klíčového slova yield: každá funkce, která obsahuje yield, je generátorová funkce (angl. generator function).

```python 
def generate2():
    """generates 2 numbers"""
    print('A')
    yield 0
    print('B')
    yield 1
    print('C')
```

- Zavoláním takové funkce dostáváme generátorový iterátor (angl. generator iterator):

```python 
>>> generate2()
<generator object generate2 at 0x...>
```

- Voláním next() se pak stane zajímavá věc: funkce se provede až po první yield, tam se zastaví a hodnota yield-u se vrátí z next(). Při dalším volání se začne provádět zbytek funkce od místa, kde byla naposled zastavena.

```python 
>>> it = generate2()
>>> next(it)
A
0
>>> next(it)
B
1
>>> next(it)
C
Traceback (most recent call last):
  ...
StopIteration
```

- více o generátorech: https://naucse.python.cz/lessons/advanced/generators/

[Otázka 9](09PRG.md)

[seznam otázek](seznam_otazek.md)
                    
[Otázka 11](11PRG.md)
