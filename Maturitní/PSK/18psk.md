# Unix shell, práce v příkazovém řádky, skriptování

- hned po spuštění se uživateli pustí Příkazový řádek ve zkratce **CMD** Command line, jinak Shell

- ve většině linuxů je nastaven **Bash** ale existují i C shell, Z shell..

## Unixový shell

- poskytuje uživateli textové rozhraní

- komunikuje s uživatelem

- interpretuje jeho pžíkazy

- spouští programy


- je to skriptovací jazyk
- umožnuje příkazům udávat parametry, seskupovat je, slučovat příkazy
- myslím si , že v některých situacích je toto rozhraní příjemnější než grafické rozhraní

## Příkazy

- ls - list files
- může mít přepínače které ovlivňují chování příkazu (-l, --all, -i, a, -s)
- **mezera** slouží jako oddělovač parametrů a přepínačů

- dlouhé přepínače se píší s dvěma **--** pomlčkami např. **--all**

- **Manuál** 
- man jmenoprogramu
- Vypíše všechny možnosti a vysvětlení příkazu

## Expanze jmen souborů
- tzv. WildCard charactery

![wildcar](https://i.gyazo.com/77bddb320feba7e877611efbcd5bbf0c.png)

- Znak **-** - zahrne čísla mezi vypsanými např(0-9)
- Znak **^** - Slouží jako negace

- Zda chceme použít nějaký **metaznak**, jako je **mezera nebo hvězdička** přiřadíme zpětné lomítko \ (\ ,\*)

## Expanze speciálních konstrukcí

**Roznásovení**<br>
ls adresar{1,2,3}
- vypíše adresar1, adresar2, adresar3

**Výstup jiného příkazu**
- POV: chceme si pojmenovat složku podle datumu
mkdir $(date +%Y_%m_%d)<br>
nebo<br>
mkdir `date +%Y_%m_%d`<br>

- nebo si chceme datum uložit do proměnné
- datum=$(date +%Y_%m_%d)


**Matematický výraz** lze zapsat pomocí konstrukce $[výraz].





