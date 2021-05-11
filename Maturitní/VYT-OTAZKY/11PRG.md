# 11. Programování - Cyklus while 

- Cyklus – v pythonu existují dva typy cyklů, while a for, umožňuje nám opakovat určitý blok kódu, tak dlouho jak potřebujeme
    - while je řízený podmínkou, dokud platí tak se bude plnit
    - for je řízený počtem prvků v dané množině
- while je nejjednodušší cyklus v pythonu, i celkově ve většině programovacích jazyků
- while cyklus provádí blok příkazů tak dlouho, dokud platí podmínka (používá se, když neznáme přesný počet opakování)
- stejně jako for, může obsahovat i nepovinný blok else, ten se provede, když podmínka neplatí
- blok else se neprovede, přerušíme-li cyklus příkazem break nebo return
- Ve vývojovém diagramu se značí stejně jako podmínka (kosočtverec), avšak se k němu ještě přidá návratová šipka

```python 
while podmínka:
    blok_příkazů
else:
    blok_příkazů
```

- spolupracující syntaxe:
    - break: vyskočí z cyklu
    - continue: přeskočí zbytek cyklu a začne další "kolo"  
    - range() : využívá se za syntaxí in (dosazuje do proměnné postupnou řadu čísel)
    - porovnávací operátory viz [1. lekce](../01-promenne-dat_typy-operace/content.md)
- Nekonečný cyklus:
    - ten nastává pouze u while
    - nejčastěji nastane, když dáme za while True
    - využití je třeba při komunikaci s uživatelem
    - lze ukončit pouze break, vypnutím programu, nebo v konzoli stisknutím Ctrl + C
```python 
x = 0
while x != 26:
    x += 1 
    if x = 10:
        break
```


```python 
while True:
    print("Běžím pořád dokokola jak hňup a mega rychle samozřejmě")
```

## Náhodná čísla:

- používá se importovaná (můžu se o importování rozkecat) knihovna random, ta generuje pseudonáhodná čísla, ale pro použití v programu stačí
- Tři nejvyužívanější funkce jsou:
    - randint(start, stop) – generuje náhodné číslo z rozmezí, které jí dovolíme, např. randint(0, 10) bude generovat čísla čísla 0 (včetně) až 10 (včetně), pokud nezadáme první hodnotu, tak začíná od 0
    - randrange(start, stop, step) – generuje náhodný prvek z rozmezí start až stop, když nezadáme start tak začíná na 0, např. randrange(1, 10) vrací čísla 1 až 9 (10 už ne), hodí se používat i step, to specifikuje o kolik se má posunout výběr, např. randrange(0, 10, 2) vrací čísla z hodnot 0, 2, 4, 6… až 9 (10 ne, tzn. max číslo bude 8)
    - choice(sequence) – tato funkce vrací náhodný prvek ze seznamu, řetězce, n-tice, slovníku…