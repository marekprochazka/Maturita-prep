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


# 22. 24. CAD - práce ve 3D
### Náčrt:
* náčrtem se začíná rýsování v Inventoru
* můžeme vybrat ze tří rovin
* nejčastěji se používá 2D náčrt ale existuje i 3D
* má podobné vlastnosti a modifikace jako AutoCAD 2D
* **Úsečka** – nakreslí rovnou čáru, je zde na výběr i křivka atd.
* **Kružnice** – vytvoří kružnici, můžeme zadat poloměr a střed, poloměr a dva body…, do toho je zahrnuta i elipsa
* **Oblouk** – Vytváří oblouk, znovu můžeme zadávat vícero možnostmi
* **Obdélník** – zadáváme obdélník (dvěma body), nebo polygon (kolik má stran a jestli je opsaný nebo vepsaný kružnici), nebo drážku atd.
  
### Modifikace náčrtu:
* **Přesunout** – posune objekt
* **Otočit** – otočí objekt o zadaný počet stupňů
* **Zrcadlit** – Zrcadlí objekt podle zadané osy
* **Měřítko** – zvětší nebo zmenší objekt podle zadaného měřítka
* **Oříznout** – ořízne objekt vždy k nejbližší čáře
* **Prodloužit** – prodlouží danou křivku, čáru, úsečku o zadanou vzdálenost
* **Zaoblit** – zaoblí objekt podle zadaného poloměru (úhly nebo radiány, pozor na to)
* **Zkosení** – zkosí hranu podle úhlu nebo vzdálenosti
* **Pole** – vytvoří pole stejných prvků, čtvercové, křivkové, kruhové, zadáváme počet prvků, popřípadě středovou osu
* **Odsazení** – odsadí objekt o předem daný počet mm
* pravým tlačítkem můžeme zadávat základní operace, ukončovat rýsování atd.
* **Vazby** – kóty – fungují podobně jako ve 2D, znovu můžeme použít formát kóty (nahoře *fx*)
  * na rozdíl od 2D si Inventor sám zjistí co je to za kótu (poloměr, délka…); dokud objekt nezavazbíme (nezakótujeme) tak se bude při posunování rozbíjet, tzn. budou se měnit jeho rozměry
  * ve vazbách se dá nastavit spousta věcí, např že dvě čáry mají být kolmé,  rovnoběžné, tečna…
* **Formát** – ve formátu můžeme měnit úsečky na osy a tak
* spodní lišta má ještě různé možnosti jako zobrazit v řezu, zobrazení vazeb…
  
### Vytvoření 3D modelu:
* Vysunutí – základní operace, která z 2D náčrtu vytvoří 3D objekt
  * pokud máme už náčrt na jiném 3D objektu, tak se zapojí **booleovské operace:**
    * **Sjednocení** – příkaz sjednocení a následně provede sjednocení prvků do jednoho
    * **Průnik** – ponechá pouze společný prostor
    * **Rozdíl** – ponechá jen to, co není společné 
  * nastavujeme odkud a od kterých náčrtů se týká, směr a kolik mm
* **Rotace** – používá se při vytváření kruhového objektu z načrtnutého řezu, např. kolo u auta (uděláme řez a provedeme rotaci)
* **Šablonování** – slouží k vytvoření přechodového tvaru mezi dvěma objekty (máme dva objekty a mezi nimi vyrobí nějaký propojení)
* Další operace jako tažení, spirála, žebro… moc jsme nepoužívali, kdyžtak dám z hlavy

### Modifikace 3D objektu:
* **Díra** – pro tvorbu díry musíme mít středový bod, poté stačí jen jak hluboká a průměr
* **Zaoblení** – Poloměr a hranu vybrat
* **Zkosení** – vzdálenost a hranu vybrat
* **Závit** – vyrábí se v díře, musí se vybrat typ, velikost, povrch v díře, hloubka, pokud má být závit atd.
* **Kombinovat** – provede booleovskou operaci, ale s již vytvořenými tělesy
* **Pole** – vytváří pole, do pole můžeme mít i náčrt, který se poté provede v celém poli
* **Zrcadlit** – bude zrcadlit objekt
* pak existují ještě nějaký operace co jsme moc nepoužívali a nějaký úpravy povrchů, to nevím vůbec nedělali jsme
* **Materiál** – volí se nahoře na kartě, základní je Výchozí

### Sestava:
* v sestavě se dají dohromady spojovat různé 3D modely do fungujícího celku
* dá se i nastavit animace, aby se sestava hýbala (otáčení pomocí vazby -> úhel)
* **Obsahové centrum** – obsahuje šroubky, matice, podložky, kabely, součásti hřídele, trubky, konstrukční prvky…
* objekty se zde spojují pomocí Vazeb, pokud je chceme i hýbat tak Spoj
  
### Vizualizace dat:
* Inventor v základu používá formát ipt, sestava formát iam
* modelování probíhá v nekonečném prostoru
* je možné si soubor exportovat v PDF, jako obrázek…
* jeden z nejvyužívanějších exportů je do souboru STL pro 3D tiskárnu: Záložka Systémové prostředí -> 3D tisk -> exportovat STL; zde se také můžeme podívat na poměr velikosti objektu a podložek různých 3D tiskáren

