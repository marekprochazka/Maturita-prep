# 11. Programování - Cyklus while 

Cyklus while opakuje blok příkazů, dokud platí určená podmínka.

```python 
while podmínka:
    blok_příkazů
else:
    blok_příkazů
```

spolupracující syntaxe:
- break: vyskočí z cyklu
- continue: přeskočí zbytek cyklu a začne další "kolo"  
- range() : využívá se za syntaxí in (dosazuje do proměnné postupnou řadu čísel)
- porovnávací operátory viz [1. lekce](../01-promenne-dat_typy-operace/content.md)

```python 
x = 0
while x != 26:
    x += 1 
    if x = 10:
        break
```

Když dáme za while "True", tak vznikne nekonečný cyklus, který jde ukončit jen za pomocí "break" (nebo tvrdým ukončením programu)

```python 
while True:
    print("Běžím pořád dokokola jak hňup a mega rychle samozřejmě")
```