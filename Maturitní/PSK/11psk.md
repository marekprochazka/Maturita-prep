# Zdrojové a kanálové kódování, princip komprese dat

## Zdrojové kódování
**1. Digitální přenosový řetězec**<br>
**2. Bezztrátová komprese**

## Digitální přenosový řetězec

![digi](https://mamut.spseol.cz/nozka/psk/110-zdrojove_kodovani/blokschema.png)

**Zdroj** - Hudba, Hlas, info počasí..<br>
**Převodník** - hlas > mp3 (A/D Převodník, mikrofon..)<br>
**Komprese dat** - Zdrojové kodování (**ztrátové/bezztrátové**)<br>
**Přenosové médium** - Optický kabel, elektromagnetická vlna...

## Bezztrátová komprese

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
