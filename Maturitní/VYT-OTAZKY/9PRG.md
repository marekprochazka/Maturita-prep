# 9. Programování - Větvení, výjimky 

> https://www.itnetwork.cz/java/zaklady/java-tutorial-podminky-vetveni-if-switch

Větvení je pro programování důležité, jelikož dává programu možnost "rozhodovat" se a "reagovat" na dané situace.


## Podmínky

### Syntaxe 
```python
if x == "Hej hou":
    pass
elif y: # vysvětlení níže
    pass
else:
    pass
```

Při vyhodnocování podmínek využíváme porovnávací operátory viz [1. lekce](../01-promenne-dat_typy-operace/content.md)

Vysvětlení syntaxe výše: Pokud máme v podmínce pouze proměnnou beze porovnávacích operátorů, tak podmínku python chápe 
následujícím způsobem: Pokud má proměnná hodnotu, což znamená, že **není** **0**, nebo **None**, tak se podmínka vyhodnotí jako 
**True**, pokud **má** proměnná hodnotu **0**, nebo **None**, tak se vyhodnotí jako **False**

## Výjimky 
Značí se párovou syntaxí **try/except** 
Funguje tak, že pokud se v bloku Try vyskytne error, tak místo konce programu s návratovou hodnotou danného erroru se 
soustí blok except. V bloku except můžeme také určit jaký konkrétní druh erroru bude "chytat"

```python
try:
   int("x") # zkouším vyrobit číslo z písmena x, dostávám value error
except:
    print("Nahoře musí být číslo")

try:
    nejakej_seznam = [1,2,3]
    print(nejakej_seznam[8]) # dotazujeme se na hodnotu na indexu, který neexistuje (v našem případě máme jen 0,1,2), dostáváme index error
except IndexError: # Vyjímka chytá pouze index error
    print("Neplatnej index")

```