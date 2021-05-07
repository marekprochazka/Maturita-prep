# Unix: Přístupová práva a proces

- **Účel**
- umožnují více uživatelům definovat přístup k souborům půodle uživatelských účtů
- pomáhá chránit údaje uživatelům
- pomáhá bránit systémová data potřebná pro funkci systému

- existují už od 60, 70 let

## Pravidla

- každý soubor má v **i-uzlu (Inode)** uloženy následující informace:
- typ souboru
- vlastníka souboru
- trojice oprávnění pro vlastníka, a ostatní uživatele
1. **r - read**
2. **w - write** (nedovolí mazat soubor)
3. **x - spouštění**


- Při práci s objekty platí:

- nově vytvořený objekt patří uživateli, který ho vytvořil
- oprávnění může měnit autor, nebo superuživatel **root**
- vlastníka může měnit pouze root (někdy majitel)


- operační systém nezasahuje do zapsaných údajů pokud nemusí

## Výpis přístupových práv

- lze zjistit jednoduše příkazem *ls -l*
<br>
drwx------ 2 pepa doma 4096 říj 7 18:54 mc-marek

![prava](https://i.gyazo.com/502e3b1ebbff792ab2440f9b45437c86.png)

- d - adresář
- "-" - běžný soubor
- l - symbolický odkaz
- p - pojmenovaná roura
- c - znakové zařízení
- b - blokové zařízení
- s - socket

- dále je 9 znaků zobrazujících:
- přístupová práva
- počet jmen souborů (2)
- jméno vlástníka (pepa)
- jméno skupiny (doma)
- velikost souboru (4096)
- datum poslední změny
- jméno souboru

## Změna přístupových dat

- provádí se příkazem **chmod** (change mod)

![chmod](https://i.gyazo.com/8dfea0c557e1b1324c08f96cb34201ef.png)

# Speciální přístupová práva

- POV: chceš někomu změnit heslo
- hesla jsou v /etc/passwd - sem může pouze root

- můžeme mít složku kam může každý, např game, každý může přidávat a mazat hry

## Interpretace pro adresáře

- právo **w** - uživatel může vytvářet/ mazat soubory
- právo **r** - může přečíst jméná souborů v adresáři
- právo **x** - může adresářem proplout
- pro normální čtení adresáře uživatel potřebuje **r** i **x**

## Výchozí přístupová práva

- command **umask** (user mask)
- rozhoduje o právech nových souborů

# Procesy

## Proces (program)
- tzv. spuštěný počítačový program
- vypíšeme příkazem **ps**
- vypíšeme příkazem **top** (více možností, jednodušší zorhraní)
- vypíšeme příkazem **htop** (vylepšený, barevnější top)
- umístěn v operační paměti a vykonáváný procesorem
- jeden program může běžet jako více procesů

- správu procesů vykonává **Task Manager**

- **Procesy se dělí na Popředí a pozadí**

- **Je nesmysl dávat na pozadí programy, které s uživatelem interaktivně komunikují**

![procoes](https://i.gyazo.com/c1163a320b7bd4ab0e0926922031aea6.png)

## Command kill

![as](https://i.gyazo.com/832d858ac567daa5d603f9df7f5287b1.png)

## Klávesové zkratky

- CTRL C - proces který je právě v popředí bude ukončen
- CTRL Z - proces ktery je právě v popředí bude pozastaven

# Commands

![asd](https://i.gyazo.com/8ac378fa07f6d98f6f3c435667450cb8.png)










