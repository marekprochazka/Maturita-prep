
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

[Otázka 23](23HW.md)

[seznam otázek](seznam_otazek.md)
                                
[Otázka 25](25HW.md)