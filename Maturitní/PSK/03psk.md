# Digitalizace signálu

* **VZORKOVÁNÍ**
* **KVANTOVÁNÍ**
* **ALIASING**

## Vzorkování / Digitalizace

* Spočívá v odebrání vzorků ze signálu v určitých předem stanovených časových okamžicích.

*pochází z anglického **Sample Vzorek**
<br>
![vzorkov](https://mamut.spseol.cz/nozka/psk/025-vzorkovani/vzorky.png)
**vzorkovací perioda T**

**Šířka vzorkovacího impulzu**

* Ideálně by měla být co nejmenší

* čím je vzorkovací impulz širší tím rychleji dochází ke strátě informace<br>
![sapler](https://mamut.spseol.cz/nozka/psk/025-vzorkovani/vzorkyFS1.png)

**Obnova původního signálu**

* Obnovit můžeme pomocí dolní propusti vybrat jen část spektra, která odpovídá původnímu signálu. (**podle zeleně vyznačeného**)
<br>
![obnova](https://mamut.spseol.cz/nozka/psk/025-vzorkovani/obnova.png)

## Aliasing

**Vzorkovací teorém (theorem)**
Aby nedošlo ke ztrátě dat musí být maximální frekvence vzorkovaného signálu menší než je polovina vzorkovací frekvence, protože v každé periodě vzorkovaného signálu musíme vzít alespoň dva vzorky.

* Proto se v praxi vzorkovací frekvence volí dvakrát větší než je maximální požadovaná přenášená frekvence (plus ještě malá rezerva)

**Aliasing vzniká nedodržením Vzorkovacího theoremu**<br>
![aliasnig](https://mamut.spseol.cz/nozka/psk/028-aliasing/aliasing.png)

**Anti-aliasing**
* Jde opět o dolní propust s mezním kmitočtem nastaveným pod polovinu vzorkovacího kmitočtu:<br>
![antialiasnign](https://mamut.spseol.cz/nozka/psk/028-aliasing/antialiasing.png)

* Anti aliasing v grafice
https://www.youtube.com/watch?v=hqi0114mwtY

## Kvantování
* "**zaokrouhlování** *hodnot signálu*"
* Většinou následuje v procesu digitalizace signálu hned za vzorkováním.
<br>
![zaokrouhlovani](https://mamut.spseol.cz/nozka/psk/031-kvantovani/kvantovani.png)

**Pulzně kodová modulace**
* každé kvantovací hladině přidělíme číslo
* místo času uvedeme pořadí<br>
![digi](https://mamut.spseol.cz/nozka/psk/031-kvantovani/pcm.png)

Poměr mezi počtem kvantovacích hladin a počtem bitů:
**Počet hladin=2^Počet bitů**

*Př: při volání telefonem se používá 8 bitů => **2^8** = **256***

**Kvantovací šum**
*ztráta informace*
* Více kvantovacích hladin = méně šumu

## A/D PŘEVODNÍK
* realizuje kvantování
* ke každé hladině přiřadí číslo ve dvojkové soustavě

## Číslicový signál
x=[ 1, 2, 1.4, 3.1, 1.1, 2, 1, 0, -3.1, -2, -0.9, -2.8, -1.5 ]<br>
![cisleciovysignalgraf](https://mamut.spseol.cz/nozka/psk/034-cislicove_zpracovani_signalu/xn.png)

**Číslicový filtr**
* bere vstupní vzorky, jednotlivé vzorky váhuje vynásobí a sečte

**Impulzní charakteristika**
* vezme se jen platné (1), a zbytek se vynásobí nulou

## Průchod signálu filtrem (Číslicový filtr, Impulzní)
**Průchod filtru:** budeme násobit vždy vzorky, které jsou pod sebou a postupovat doprava 
viz. https://mamut.spseol.cz/nozka/psk/034-cislicove_zpracovani_signalu/#prchodsignlufiltrem

