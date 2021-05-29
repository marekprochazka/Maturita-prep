# 22. 23. CAD – práce ve 2D
* AutoCAD pracuje s vektorovou grafikou     
### Základní objekty:
* **Úsečka** – nakreslí rovnou čáru
* **Křivka** – vytvoří křivku, dle zadání v konzoli můžeme změnit jakou křivku vyrobí
* **Kružnice** – vytvoří kružnici, můžeme zadat poloměr a střed, poloměr a dva body…
* **Oblouk** – Vytváří oblouk, znovu můžeme zadávat vícero možnostmi
* **Obdélník** – zadáváme obdélník (dvěma body), nebo polygon (kolik má stran a jestli je opsaný nebo vepsaný kružnici)
* **Elipsa** – můžeme zadat vícero možnostmi, nebo jen část elipsy
* **Šrafování** – vytváří šrafování (hustota šrafování, barva, úhel čar…), gradient (přechody, kolik a jaké barvy), nebo hranici
* spousta dalších možností jako konstrukční přímky (používá se jako osa), spirála atd.

### Modifikace objektů:
* **Posun** – posune objekt
* **Otočit** – otočí objekt o zadaný počet stupňů
* **Zrcadlit** – Zrcadlí objekt podle zadané osy
* **Měřítko** – zvětší nebo zmenší objekt podle zadaného měřítka
* **Oříznout** – ořízne objekt vždy k nejbližší čáře
* **Zaoblit** – zaoblí objekt podle zadaného poloměru (úhly nebo radiány, pozor na to)
* **Zkosení** – zkosí hranu podle úhlu nebo vzdálenosti
* **Pole** – vytvoří pole stejných prvků, čtvercové, křivkové, kruhové, zadáváme počet prvků, popřípadě středovou osu
* **Odsazení** – odsadí objekt o předem daný počet mm
* další možnosti jako přerušení čáry, spojování objektů, úprava hladiny…
* **Booleovské operace:**
  * ve 2D je potřeba objekty napřed sloučit do oblasti – provádí se příkazem oblast a vybráním objektů
  * **Sjednocení** – příkaz sjednocení a následně provede sjednocení prvků do jednoho
  * **Průnik** – příkaz průnik, ponechá pouze společný prostor
  * **Doplněk** – ve 2D asi není, jinak ponechá to, co nemají společné
* pravým tlačítkem můžeme zadávat poslední použité operace, bez nutnosti hledání
  
### Práce s textem, kóty:
* můžeme vkládat a upravovat text, ten se poté dá i vytisknout a tak
* **Kóty:**
  * existuje několik typů kót, přímá, šikmá, úhlová, poloměr, průměr…
  * musíme volit ručně na rozdíl od Inventoru
  * jednoduše označíme odkud kam, popřípadě zaoblení a kóta se poté vyrobí
  * kóty se upravují pomocí příkazu kótystyl, v něm se nastavuje velikost písma, šipek, nebo normy
  * kóty jdou nastavovat i pomocí parametrů, např. do kóty se při úpravě napíše d0/2 (to něco provede)

### Hladiny:
* v AutoCADu můžeme pracovat s hladinami, základní hladinou je hladina „0“
* dle potřeby se mohou přidávat nebo ubírat, každé hladině se dá nastavit barva, tloušťka, typ čáry, viditelnost, zamčení…

### Blok:
* blok slouží k uložení nějakého objektu, který poté můžeme vkládat, není potřeba jej kopírovat
* bloku jsou nastavit různé vlastnosti, třeba že se může pohybovat pouze po ose X atd.
  
### Vlastnosti:
* většinou jsou určeny podle hladiny
  
### Modely:
* modely se dají prohazovat vlevo nahoře v pohledu, na výběr jich je asi 10, základní 2D drátový model, realistický, stínový, koncepční…
* častěji se ale s modely pracuje pomocí šablony, ta se vybere před zahájením kreslení vlevo nahoře se dá Nový a ony ty šablony vyskočí a tam si vyberem
  
### Spodní lišta:
* na spodní liště v AutoCAD se nachází spousta funkcí
* nejdůležitější je asi nastavení uchycování, v něm si lze nastavit na co všechno se má přichytávat kurzor
* dále tam je možnost změny zobrazení z 2D na 3D
* a hlavně úplně vpravo všechno dohromady
  
Vizualizace dat:
* AutoCAD v základu používá formát dwg
* modelování probíhá v nekonečném prostoru, do rozvržení se vloží pohled z daného výkresu
* probíhá v rozvržení, funkce jako vložit pohled (výstřižek z modelu)
* je možné si soubor vytisknout, nebo uložit v PDF atd.

[Otázka 22](22CAD.md)

[seznam otázek](seznam_otazek.md)
                                
[Otázka 24](24CAD.md)