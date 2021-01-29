# N-tice, slovníky, řetězce

## n-tice

- N-tice je datový typ, jenž uchovává své prvky v určitém pořadí. Vytváří se následovně:

```python 
prazdna = ()
prazdna_2 = tuple()
jina = (1, 2, 3)
jina_2 = tuple(range(3))
```

- N-tici vytvoříme tak, že její prvky dáme do kulatých závorek a jednotlivé prvky oddělíme čárkou. Výraz tuple() umí převést i jiné datové typy na n-tice (pokud to lze), například výsledek funkce range().

```python 
licha = tuple(range(1, 10, 2))
suda = tuple(range(0, 10, 2))
```

- N-tice je pevný datový typ. Ve chvíli, kdy N-tici vytvoříme, tak ji již nemůžeme upravovat

- Možné operace:
    - n-tice lze spojovat (+), replikovat (*) a testovat, zda-li se určitá hodnota nachází uvnitř n-tice

```python
>>> moje = (1,2,3)
>>> jina = ("a","b","c")
>>> moje * 2
(1,2,3,1,2,3)
>>> moje + jina
(1,2,3,"a","b","c")
>>> 4 in moje
False
>>> "a" in jina
True
```
- n-ticí lze iterovat za pomocí cyklu for

```python
moje = (1,2,3)
for hodnota in moje:
    print(hodnota)

output:
1
2
3
```


## slovníky 

- Podobně jako n-tice, slovníky v sobě obsahují další hodnoty. Na rozdíl od n-tic, ve kterých jsou všechny prvky uspořádané do jedné sekvence, 
    ve slovnících máme dva druhy prvků: takzvaný klíč (angl. key) a hodnotu (angl. value). Každému klíči je přiřazena jedna hodnota.
- Slovníky se dají také využít, když máme různé informace, ale chceme s nimi pracovat jako s jedním celkem (v někteřých jazycích, jako je například javascript se proto slovníkům říká objekt)
- Příklady slovníků (z první kapitoly):

```python
>>> clovek = {"jmeno":"Igor","vek":27,"sporty":["Fotbal","Házená","Kuličky"]}
>>> clovek["jmeno"]
    "Igor"
>>> clovek["sporty"][2]
    "Kuličky"
>>> dict(("m",7), a=6)
    {"m":7,a:6}
```

- U slovníků můžeme testovat, zda-li se určitá hodnota nachází uvnitř a to jak na pozici klíče, tak na pozici hodnoty.

```python
>>> dct1 = {1:2,3:4}
>>> 1 in dct1 
True # operátor in se primárně dívá na klíče
>>> 2 in dct1
False
>>> 1 in dct1.values() 
False # pro hledání v hodnotách je za potřebí zavolat na slovník vnitřní metodu values()
>>> 2 in dct1.values()
True

```

## řetězce
- Seznam nám poskytuje způsob, jak ukládat větší množství hodnot přehledně a na jedno místo.
- Má velice podobné vlastnosti jako N-tice, rozdíl je však v tom, že hodnoty uvnitř řetězce lze upravit.
- Značí se jinými závorakmi jak n-tice '[]', funkce pro tvorbu se jmenuje list()

- příklad z první lekce

```python
# práce s indexy
>>> muj_seznam = [1,2,3,4,5]
>>> muj_seznam[0] 
    1
>>> muj_seznam[2]
    3
>>> muj_seznam[-1]
    5
>>> muj_seznam[:2]
    [1,2]
>>> muj_seznam[2:]
    [3,4,5]
>>> muj_seznam[2:4]
    [3,4]

# funkce list a range
>>> list("abc") 
    ["a","b","c"]
>>> range(20)
    range(0,20)
>>> list(range(0,20))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] # POZOR není číslo 20, jede podle indexů

# Mazání/přidávání
>>> seznam = ["a","b","c"]
>>> seznam.append("d")
>>> seznam
    ["a","b","c","d"]
>>> seznam.pop(0) # podle indexu
    ["b","c","d"]
>>> seznam.remove("b") # podle předmětu
    ["c","d"]
>>> del seznam[0] # alternativa podle indexu
    ["d"]
```

* práce s indexy je stejně uplatnitelná také u n-tice