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

.	E   	. . . .	H<br>
-	T	- . . -	X<br>
. .	I	- -. .	Z<br>
. -	A	- . - -	Y

## Huffmanovo kódování
* každé písmeno má svou frekvenci
* Nejpoužívanější obsahují nejméně informací

https://www.youtube.com/watch?v=dM6us854Jk0

**Bez huffmanova algoritmu** - 176 bitů<br>

![hufgf](https://i.imgur.com/4eaRSMW.png)

**Huffmanův algoritmus** - 146 bitů<br>

![shughf](https://i.gyazo.com/f9c48a88730851249ca5ea45a284798a.png)

![hsad](https://i.gyazo.com/10e6950c100adc1c05949820522c654a.png)

