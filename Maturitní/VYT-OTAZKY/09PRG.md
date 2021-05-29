# 9. Programování - Větvení, výjimky 

> https://www.itnetwork.cz/java/zaklady/java-tutorial-podminky-vetveni-if-switch

- Větvení je pro programování důležité, jelikož dává programu možnost "rozhodovat" se a "reagovat" na dané situace.
- Větvení většinou využívá logické operátory
- V Pythonu celkově, tedy i u větvení je velmi důležité konzistentní odsazování (to může být jakékoli, klidně i jen jedna mezera, ale v praxi se používá buď tab, nebo 4 mezery)
- Ve vývojovém diagramu se podmínka značí kosočtvercem

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
## Syntaxe
Při vyhodnocování podmínek využíváme porovnávací operátory viz [1. lekce](../01-promenne-dat_typy-operace/content.md)

- základní věcí je if; tím samotné větvení, neboli podmínky začínají
    - v if je uvedena nějaká podmínka, která se buď splní nebo nesplní; pokud se splní, provede se blok programu, který je v podmínce
- další větvení může probíhat pomocí příkazu elif; ten se vykoná, pokud nebyla splněna první podmínka a zároveň platí podmínka, která je u něj uvedena
- poslední možností je příkaz else; ten se splní vždy, když se nesplní žádná předchozí podmínka (pokrývá všechny zbylé možnosti)
- podmínky se zde porovnávají pomocí porovnávacích operací, tzn. ==, != …, aby se to nepletlo s běžným přiřazováním do proměnné

- Vysvětlení syntaxe výše: Pokud máme v podmínce pouze proměnnou beze porovnávacích operátorů, tak podmínku python chápe 
následujícím způsobem: Pokud má proměnná hodnotu, což znamená, že **není** **0**, nebo **None**, tak se podmínka vyhodnotí jako 
**True**, pokud **má** proměnná hodnotu **0**, nebo **None**, tak se vyhodnotí jako **False**

## Výjimky 
- výjimky slouží k ošetřování chyb programu, nejčastěji způsobených chybným vstupem od uživatele
- Značí se párovou syntaxí **try/except** 
- Funguje tak, že pokud se v bloku Try vyskytne error, tak místo konce programu s návratovou hodnotou danného erroru se 
soustí blok except. V bloku except můžeme také určit jaký konkrétní druh erroru bude "chytat"
- chyba se dá i uměle vyvolat příkazem raise, do něj se dají vyvolat vyloženě typ erroru, který se má vyvolat, např. NameError, používá se spíš k otestování except bloku

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

- Méně používané jsou u výjimek ještě else a finally – else se provede, pokud se provede blok try, tzn. nenastal žádný error; blok finally se provede vždy
- Základní chyby v Pythonu:
    - SyntaxError – chyba ve zdrojovém kódu, nejčastěji chyba v syntaxi (špatné odsazení, překlep…)
    - ZeroDivisionError – dělení nulou
    - TypeError – nesprávné použití datových typů - např. sčítání řetězce a čísla apod.
    - ValueError – nesprávná hodnota
    - IndexError – chyba v indexu

[Otázka 8](08PRG.md)

[seznam otázek](seznam_otazek.md)
                    
[Otázka 10](10PRG.md)