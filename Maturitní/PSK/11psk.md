# Zdrojové a kanálové kódování, princip komprese dat

## Zdrojové kódování
**1. Digitální přenosový řetězec**<br>
**2. Bezztrátová komprese**

## Digitální přenosový řetězec

![digi](https://mamut.spseol.cz/nozka/psk/110-zdrojove_kodovani/blokschema.png)

**Zdroj** - Hudba, Hlas, info počasí..<br>
**Převodník** - hlas > mp3 (A/D Převodník, mikrofon..)<br>
**Komprese dat/ Zdrojový kod** -  (**ztrátové/bezztrátové**)<br>
**Kanálový koder** - zabezpečuje data proti chybám
**Přenosové médium** - Optický kabel, elektromagnetická vlna...

# Kanálový kodér

## Kanálový kodér
* zabezpečuje data proti chybám
* přenášeným datům se přidají další data, která zprávu zabezpečují => zvýší se **redundance**

(
**Chyby**
* ojedinělé chyby
* shluky chyb
* chyba vytvoří další chybu

**Zabezpečení**
* detekční kódy
* samoopravitelné kódy
)

Řešení:<br>
**Paritní kód**
* doplní jeden bit na konec bytu tak aby počet jedniček byl sudý

10011011  1<br>
00110111  1<br>
01101001  0<br>
00011000  0

* selže jen pokud vzniknou 2 chyby zároveň

**Kódy K z N**
* n -pocet míst
* k -pocet jednicek
* kontrola spociva ve spocitani jednicek
* nelze oddělit data od zabezpečení

**Hash** (fingerprint)
* opakovatelná metoda
* pouziva se na hesla
* např **MD5 A SHA**

## Kódy pro detekci a opravu chyb

* v některých situacích je chyb tolik, že se musí používat kody které chybu vetšinou dokážou detekovat a opravit

![chyba](https://mamut.spseol.cz/nozka/psk/126-kanalove_kodovani/opravach.png)

* Černé tečky jsou stavy povolené
* šedé tečky jsou stavy zakázané

* některé se zaokrouhlí do nejpodobnějšího, některé jsou chybné neopravitelné

**Blokové lineární kódy**
* data jsou kódována a dekódována po blocích
* vytvoří "matici", pošle, zkontroluje podle "matice"

# Multiplexování

* Frekvenční dělení přenosového pásma -- FDMA

![s](https://mamut.spseol.cz/nozka/psk/130-multiplexovani/frekvencni-deleni.png)

* Časové dělení přenosového pásma -- TDMA

![asd](https://mamut.spseol.cz/nozka/psk/130-multiplexovani/casove-deleni.png)

* **Linkový kodér**

Non Return to zero NZR<br>

![fa](https://mamut.spseol.cz/nozka/psk/130-multiplexovani/NRZcode.png)

* chyba: pokud bude více 1 nebo 0 za sebou přijímač nerozezná kolik jedniček to bylo

Return to zero RZR<br>

![asd](https://mamut.spseol.cz/nozka/psk/130-multiplexovani/RZcode.png)

AMI<br>

![ami](https://i.gyazo.com/3c8c9c26b2e5ed6eaafe3ce1634ca6b0.png)


Kodovani Manchester<br>

![asd](https://mamut.spseol.cz/nozka/psk/130-multiplexovani/manchester_encoding.png)
* rostoucí 1, klesající 0

# Bezztrátová komprese

* Odstraňuje pouze nadbytečné informace = **REDUNDANCE**
* Redundance = znaky které se opakují

* např.: **Morseova abeceda**
* nejpoužívanější písmena obsahují nejméně dat

## Huffmanovo kódování
* každé písmeno má svou frekvenci
* Nejpoužívanější obsahují nejméně informací

https://www.youtube.com/watch?v=dM6us854Jk0

**0 ukončí charakter**

![hsad](https://i.gyazo.com/10e6950c100adc1c05949820522c654a.png)

# Ztrátová komprese

**Kompresní poměr** - jak moc smaže komprese dat oproti původu

* odstraní méně dúležité data (na obloze odstraní některé odstíny modré)
* nakonec se použijí i bezztrátové komprese

* **Využívá nedokonalosti lidského zraku/sluchu**

## Běžně používané kompresní formáty počítačových souborů

![KOMPRES](https://i.gyazo.com/49086015f91e51d85a1de45466692e3a.png)