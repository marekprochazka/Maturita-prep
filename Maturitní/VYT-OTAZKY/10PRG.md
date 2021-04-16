# 10. Programování - Cyklus for

> https://www.itnetwork.cz/python/zaklady/python-tutorial-cykly-while-for-in-funkce-range-a-vyraz-pass
* správně by to mělo být cyklus for .. in, ale to ti dementi samozřejmě neví...

Cyklus má parovou syntaxi for .. in 
příklad 
```python
seznam = [1,2,3,4]
for hodnota in seznam:
    print(hodnota) # postupně tiskne 1,2,3...
```

spolupracující syntaxe:
- break: vyskočí z cyklu
- continue: přeskočí zbytek cyklu a začne další "kolo"  
- range() : využívá se za syntaxí in (dosazuje do proměnné postupnou řadu čísel)

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
#### Vnořené cykly
- jedná se o for smyčku ve for smyčce
- celá „vnitřní smyčka“ proběhne pro každý prvek „vnější smyčky“

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) # vyždycky se napíše red apple, red banana, red cherry; big apple, big banana...
```
* No a teď jsem u maturity asi v hajzlu protože fakt nevím co víc k tomu dodat

 
