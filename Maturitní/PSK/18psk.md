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

- cd
- pwd
- man
- mv
- mkdir
- rmdir
- top - vypise procesy lip
- ps - vypise procesy
- cat - precte soubor - editor


- dlouhé přepínače se píší s dvěma **--** pomlčkami např. **--all**

- **Manuál** 
- man jmenoprogramu
- Vypíše všechny možnosti a vysvětlení příkazu

## Expanze jmen souborů
- tzv. WildCard charactery

![wildcar](https://i.gyazo.com/77bddb320feba7e877611efbcd5bbf0c.png)

- Znak **-** - zahrne čísla mezi vypsanými např(0-9)
- Znak **^** - Slouží jako negace

- Zda chceme použít nějaký **metaznak**, jako je **mezera nebo hvězdička** přiřadíme zpětné lomítko \

## Expanze speciálních konstrukcí

**Roznásovení**<br>
ls adresar{1,2,3}
- vypíše adresar1, adresar2, adresar3

**Výstup jiného příkazu**
- POV: chceme si pojmenovat složku podle datumu
mkdir $(date +%Y_%m_%d)<br>
nebo

![asd](https://i.gyazo.com/677e8672b10120e76cf6af704c908b5d.png)

- nebo si chceme datum uložit do proměnné
- datum=$(date +%Y_%m_%d)


**Matematický výraz** lze zapsat pomocí konstrukce $[výraz]

![amakt](https://i.gyazo.com/5bce10a004400c9c29ea9397593d7960.png)

## Návratová hodnota příkazu

- pomocí příkazu **echo $?** zjistíme zda program měl 0 chyb nebo více (vypíše v čísle 1,2,3)

## Oddělení příkazů

- POV: chceme napsat více příkazů na 1 řádku
- Oddělíme pomocí **;**

- **&&** slouží jako **AND**

- **Vyjímka** - příkad cp se povede jen pokud se složka vytvoří uspěšmě
- mkdir texty && cp *.txt texty

- **||** se použije jen pokud první příkaz nevjde
- cd dddata || pwd

## Vyhledání spustitelného souboru

- POV: chci pustit svůj program v aktuálním adresáři
- zkusím **program.py** - nebude fungovat!
- je nutné shellu říct cestu k programu takže:
- **./program.py**
- nebo
- **/home/uzivatel/bin/program.py**

## Aliasy

- definuje zkratku pro jiný (dlouhý) příkaz

- alias ls='ls -F --color=auto'
- alias ll='ls -l'

## ls přepínače

- -l - long format
- -F * - spustitelné soubory
- -F / - adresáře
- -F 1 - symbolický odkaz
- -a - zobrazí i soubory začínající tečkou(skryté)
- ls -R ~ - vypíše všechny soubory v domovském adresáři
- -d - vypíše informace o adresáři/odkazu
- -t - seřadí podle času (od nejnovějšího) 
- -X - seřadí podle přípony souboru
- -h - vypíšel velikost v čitelném formátu (1K, 5G)

## Výstup příkazu ls -l

drwx------ 2 pepa doma 4096 říj 7 18:54 mc-marek

- d - adresář
- "-" - běžný soubor
- l - symbolický odkaz
- p - pojmenovaná roura
- c - znakové zařízení
- b - blokové zařízení
- s - socket

## příkaz cp

- -v - příkaz bude (ukecaný)říkat co právě dělá
- -i - interaktive (bude se ptát)
- f - nebude se ptát (force)
- -R -r 

## Odkazy 

- **Pevný odkaz**
- přidává další jméno 
- může ho vytvořit jen superuživatel(root)

- **Symbolický odkaz**
- zástupce souboru
- odkaz na původní

## další příkazy

![asd](https://i.gyazo.com/8146fbd36ab643c18a86a59b2880cfc9.png)

![asd](https://i.gyazo.com/4ee4f2fa7a2ea4d1a35eae00e0b4a9a4.png)
