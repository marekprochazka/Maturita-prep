# Cyklus for
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
- range() : využívá se za syntaxí in (dosazuje do proměnné postupnou řadu čísel)

```python
for promenna in range(10):  # promenna bude dosahovat hodnot (0 až 9 v celých číslech)
    print(promenna)
    if promenna == 5:
        break               # cyklus končí ve chvíli, kdy promenna dosáhne hodnoty 5
```

* No a teď jsem u maturity asi v hajzlu protože fakt nevím co víc k tomu dodat