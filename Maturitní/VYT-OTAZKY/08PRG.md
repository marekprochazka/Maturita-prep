# 8. Programování - Proměnné, datové typy, operace 

----

# Proměnné:

> https://www.itnetwork.cz/python/zaklady/python-tutorial-promenne-zakladni-datove-typy-a-funkce


- Proměnná je nějaká dočasná entita, kterou můžeme v proběhu programu měnit a pracovat s ní, není statická; v paměti PC vydrží do ukončení programu
- V názvu proměnné se mohou používat je znaky ENG abecedy, podtržítka, pomlčky a číslice (ale název proměnné nesmí číslem začínat)
- Velikost proměnné je omezena pouze velikostí paměti PC, neexistuje pevně daný limit velikosti

- V programování existjí 2 základní typy deklarování proměnných:
- **Dynamický typový systém**
  - Ve své hluboké podstatě proměnná nemá žádný typ (int, string,...)
  - Proměnné se velmi často nemusí deklarovat a mohou svůj typ měnit v průběhu programu
- **Statický typový systém**
  - proměnné jsou zde striktně definované a mají pevný datový tap, který se nemění.
  - Díky tomu běží program rychleji, protože může jen jednou vyhodnotit, že nějaká proměnná má nějaký datový typ a do konce s tím může počítat.
    U dynamického typového systému to tak nejde.
- Proměnné v pythonu se řadí do dynamického typového systému
- V kontextu proměnných stojí za zmínku rozdíl mezi kompilací a interpretací:
  - **Kompilace**: celý kód se zároveň přeloží do strojového kódu, zkompilovaná verze se spouští => nutný statický typový systém, protože kompilátor si
    nedokáže uhlídat, jestli se nějaké proměnné mění a jak. Potřebuje to mít pevně danné.
  - **Interpretace**: intepret postupně překládá a spoští program => možnost dynamického typového systému, protože interpreter si s tím poradí.

### Dynamický typový systém (Python)

```python
variable = 10
another_variable = "ahoj"

variable = "tak a ted uz nejsem cislo"
another_variable = ["no a ze me je list", 123]
```

### Statický typový systém (C++)

```c++
char pismenko;
float cislo;
int jiny_cislo = 12;

pismenko = "a";

pismenko = 1; => NELZE 
```

---

# Datové typy

- textové: str
- numerické: int, float, complex
- sekvenční: list, tuple, range
- mapovací: dict
- sety: set, frozenset
- booelovské: bool
- binární: bytes, bytearray, memoryview

## Nejvýznamnější datové typy

- celé číslo, integer, int -> celé číslo jehož velikost je limitována pouze pamětí počítače
- definje se jako obyčejné číslo

```python
>>> x = 1
>>> isinstance(x, int)
    True 
>>> y = "ahoj"
>>> isinstance(y, int)
    False
```

- desetinné číslo, float ->uchovává v paměti desetinné číslo, není však neomezeně přesné.
  U desetinných čísel se nepíše čárka, ale tečka. Čísla začínající nulou se dají psát bez nuly. Např. 0.25 se dají psát jako .25.
- definuje se jako int akorát s desetinnou tečkou

```python
>>> x = 0.25
>>> isinstance(x, float)
    True 
>>> y = .25 
>>> isinstance(y, float)
    True 
>>> z = 2
>>> isinstance(z, float)
    False
>>> zz = "aaa"
>>> isinstance(zz, float)
    False
```

- řetězec, string, str - sled znaků, definuje se pomocí jednoduchých nebo dvojtých uvozovek (",')

```python
>>> retezec = "hrozne zajimavej text"
>>> isinstance(retezec, str)
    True 
>>> neretezec = ["aaa","bbb"]
>>> isinstance(neretezec, str)
    False
```

- seznam, list - definuje se za pomocí hranatých závorek '[ ]' a prvky v něm se oddělují čárkou ','
- můžeme je též tvořit za pomocí funkcí 'list()' a 'range()' jen pozor na funkci range, která vrací vlastní datový typ, který je třeba ještě prohnat funkcí list
- list může obsahovat prakticky jákekoliv datové typy. Obshahuje li seznam více seznamů, tak hovoříme o více rozměrnémseznamu
- k jednotlivým hodnotám seznamu můžeme přistupovat za pomocí indexu
- list lze rozšířit a mazat z něj
- rozšiřuje se pomocí metody append
- mazat lze více způsoby

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

- n-tice, tuple - velmi podobný listu. Jediný rozdíl je, že se do něj nedá zapisovat ani z něj mazat => je rychlejší
- definuje se klasickými závorkami '( )' a prvky v něm se oddělují čárkou ','

```python
>>> ntice = (1,2,3,4,5)
>>> ntice[0]
    1
```

- slovník, dictionary, dict - hodnoty jsou seřazeny do párů: klíč ('key') a hodnota ('value')
- slovníky definujeme složenými závorkami '{ }', párové hodnoty dělíme dvojtečkou ':' a páry mezi sebou čárkou ','
- lze je též definovat funkcí 'dict()'
- hodnoty získáváme pomocí klíče (slovník[klíč] : hodnota )
- zadáme-li neexistující klíč, dostaneme key error

```python
>>> clovek = {"jmeno":"Igor","vek":27,"sporty":["Fotbal","Házená","Kuličky"]}
>>> clovek["jmeno"]
    "Igor"
>>> clovek["sporty"][2]
    "Kuličky"
>>> dict(("m",7), a=6)
    {"m":7,a:6}
```

- bool - pravda/lež, ano/ne, 0/1

```python
>>> pravda = True
>>> nepravda = False
```

- set - seznam, ve kterém se každá hodnota vyskytuje pouze jednou
- definuje se složenými závorakami jako dict ale jen s jednou hodnotou, nebo pomocí funkce 'set()'

```python
>>> my_set = {1,1,1,2,2,3}
>>> my_set
    {1,2,3}
>>> set([1,1,1,2,3])
    {1,2,3}
```

## Další datové typy

```python
>>> cmplx = 1j
>>> type(cmplx)
    <class complex>
>>> frzst = frozenset({1,2,3}) # frozenset => neupravitelný set
>>> bts = b"Hello" # bytes => neměnitelná sekvence bytů (více info: http://howto.py.cz/cap07.htm#2 - kapitola 2)
>>> btarray = bytearray(5) => měnitelná verze bytes
>>> mmrv = memoryview(bytes(5)) => místo, kde se nachází proměnná v paměti

```

## Převodní funkce 
- datové typy se dají převádět splňuje proměnná konkrétního datového typu podmínku datového typu nového. Využívají se následující funkce: 
    - __int()__ – převede na celé číslo, když nemá co převést vyhodí error
    - __float()__ – převede na desetinné číslo
    - __str()__ – převede na string (řetězec)
    - __ord()__ – převede znak na ASCII hodnotu
    - __chr()__ – převede ASCII hodnotu na znak

## Vstup a výstup

- __input()__ – příkaz pro vstup, program čeká na vstup od uživatele, vrací string
- __print()__ – vypíše řetězec, číslo, return funkce... co konzole, každý print je jeden řádek, pomocí end tomu lze zamezit, že se nastaví místo konce řádku jiný znak

---

# Import, použití knihoven:

-příkaz import má 3 podoby
    - import random – základní, v tomto případě se na knihovnu odkazujeme random.randint()
    - from random import randint, from random import * - buď můžeme importovat pouze část knihovny, nebo celou, v obou případech se odkazujeme pouze randint(), v tom případě u * je problém, pokud by ve dvou a více importovaných knihovnách byla stejná funkce, bude způsobovat kolize, použije se ta funkce z knihovny, která se importovala později
    - import random as rn – v tomto případě se na knihovnu random odkazujeme rn.randint()
- __Knihovna math__ – math má spoustu funkcionalit, obsahuje prakticky všechny matematické operace
    - __goniometrické funkce – úhel se jim zadává v radiánech a musí se převádět (to se určitě zeptá)__


# Operace a operátory

- operátory se využívají k provedení operací na proměnných, nebo hodnotách
- python dělí operátory do několika skupin:
  - Aritmetické -> Arithmetic
  - Porovnávací -> Comparison
  - Logické -> Logical
  - "Identitní" -> Identity
  - "Členské" -> Membership
  - Bitové -> Bitwise
  - Řadící/přiřazovací -> Assignment

## Aritmetické operátory

```python
# Sčítání - Addition
x + y
# Odčítání - Substraction
x - y
# Násobení - Multiplication
x * y
# Dělení - Division
x / y
# Modulo (zbytek z celočíselného dělení) - Modulus
x % y
# Umocnění - Expoonentiation
x ** 2
# Celočíselné dělení - Floor Division
x // y
```

## Porovnávací operátory

```python
# Rovnost - Equal
x == y
# Nerovnost - Not equal
x != y
# Větší něž - Greater than
x > y
# Menší než - Less than
x < y
# Větší nebo rovno - Greater than or equal to
x >= y
# Menší nebo rovno - Less than or equal to
x <= y
```

## Logické operátory

```python
# and - Vrací True, pokud jsou obě tvrzení pravdivé 
x < 5 and x < 10 
# or - Vrací True, pokud je aspoň jedno tvrzení pravdivé
x < 5 or x < 10
# not - Obrací výsledek tvrzení (False na True a naopak)
not(x < 5 and x < 10) 
```

## Identitní operátory

```python
# is - Vrací True pokud jsou obě proměnné/hodnoty stejné
x is y
# is not - Vrací True pokud obě proměnné/hodnoty nejsou stejné
x is not y
```

## Členské operátory

```python
# in - Vrátí True, pokud se hodnota nachází v sekvenci
x in y
# not in - Vrátí True, pokud se hodnota nenachází v sekvenci
x not in y
```

## Bitové operátory

```python
# & - AND - logické 'a'
# | - OR - logické 'nebo'
# ^ - XOR
# ~ - NOT
# << - Zero fill left shift
# >> - 	Signed right shift
```

## Řadící/přiřazovací operátory

```python
x = 5
x += 5 => x = x + 5
x -= 3 => x = x - 3
x *= 3 => x = x * 3 
# Platí pro všechny ostatní operátory
```

[Otázka 7](07HW.md)

[seznam otázek](seznam_otazek.md)
                
[Otázka 9](09HW.md)