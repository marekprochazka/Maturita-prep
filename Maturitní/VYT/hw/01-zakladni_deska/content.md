## základní deska a její části (procesory, sběrnice, BIOS, rozhraní, ROM a RAM)


- Základní deska (anglicky mainboard či motherboard) 
představuje základní hardware většiny počítačů. Hlavním 
účelem základní desky je propojit jednotlivé součástky počítače 
do fungujícího celku a rozdělit jim elektrické napájení, které základní 
desce poskytne zdroj. Postupem času se funkce základní desky rozšiřovala 
v tom, že sama začínala obsahovat některé komponenty, které se dříve musely 
připojovat externě.
- Typická základní deska umožňuje zapojení procesoru a operační paměti. 
Další komponenty (např. grafické karty, zvukové karty, pevné disky, mechaniky) 
se připojují pomocí rozšiřujících slotů nebo kabelů, které se zastrkávají do 
příslušných konektorů. Na základní desce je dále umístěna energeticky nezávislá 
paměť Flash, ve které je uložen systém BIOS, který slouží k oživení počítače hned 
po spuštění.

### Procesor:

- Centrální procesorová jednotka (CPU) = hardware počítače, který vykonává 
počítačový program
- Taktovací frekvence určuje rychlost mikroprocesoru a udává se v GHz. Určuje, 
kolik miliard operací vykoná mikroprocesor za 1s. 
- extra info: https://cs.wikipedia.org/wiki/Centr%C3%A1ln%C3%AD_procesorov%C3%A1_jednotka

### Typy konektorů:
1. Napájecí konektor počítače - pro připojení napájecího kabelu, na jehož druhém konci je standardní zásuvka 
2. VGA, DVI,... 
    - VGA: konektor grafické karty - připojení monitoru
    - DVI: taky připojuje monitor, ale narozdíl od VGA, který je veden analogově jsou informace vedeny 
    digitálně
    - HDMI: rychlejší digitální, narozdíl od předešlých kromě videa přenáší i zvuk 
3. PS/2 - starší konektro pro připojení myši a klávesnice 
4. Paralelní port - původně pro připojení tiskáren, skenerů i některé externí mechaniky (dnes se již nepoužívá)
5. Hudební konektory - standardní 3.5mm 'jacky' => vývody zvukové karty. Připojení reproduktorů, mikrofonů a 
jiných hudebních zařízení 
6. USB - je navržen pro připojení všech možných typů externích zařízení a  to dokonce za chodu počítače 
7. SCSI - standardní rozhraní a sada příkazů pro výměnu dat mezi externími nebo interními počítačovými 
zařízeními a počítačovou sběrnicí.
8. RJ45 - dnes nejčastěji používaný typ zapojení síťových kabelů UTP a STP 

### Sběrnice:

- Sběrnice (anglicky bus) je skupina signálových vodičů,
kterou lze rozdělit na skupiny řídicích, adresových a
datových vodičů v případě paralelní sběrnice nebo sdílení
dat a řízení na společném vodiči (nebo vodičích) u sériových
sběrnic. Sběrnice má za účel zajistit přenos dat a řídicích
povelů mezi dvěma a více elektronickými zařízeními. Přenos
dat na sběrnici se řídí stanoveným protokolem.
- Mezi protokoly patří: 
    - ISA - starší typ pasivní sběrnice, šířka 8 nebo 16 bitů
    - PCI - novější typ 'inteligentní' sběrnice, šířka 32 nebo 64 bitů

- extra info: https://cs.wikipedia.org/wiki/Sb%C4%9Brnice

### BIOS:

- BIOS (anglicky Basic Input-Output System) 
implementuje základní vstupně–výstupní 
funkce pro počítače IBM PC kompatibilní a 
představuje vlastně firmware pro osobní počítače. 
Až do příchodu Windows 8 se BIOS používal při startu 
počítače pro inicializaci a konfiguraci připojených 
hardwarových zařízení a následnému spuštění operačního 
systému, kterému je pak předáno další řízení počítače. 
V novějších počítačích (zhruba od druhé dekády 21. století) 
je postupně nahrazován systémem UEFI.
- BIOS zprostředkovává komunikaci mezi HW a SW
- extra info: https://cs.wikipedia.org/wiki/BIOS

### Operační paměť: 

- dočasné uložení informací, které mikroprocesor potřebuje po ruce, aby 
mohl pracovat. při vypnutí se informace vymažou. 
- Velikost se udává v Gb

### Paměti:
- TODO eprom, eeprom, parametry, statické vs dynamické

### Dělení pamětí dle provedení: 
- RAM: 
    - Pamět s libovolným přístupem/operační paměť 
    - Po zapnutí PC se uloží operační systém do paměti RAM 
    - Použítí: operační a vyrovnávací paměti 
- ROM: 
    - Slouží pouze pro čtení
    - Používá se pro BIOS
- HARD DISK: 
    - Hlavní paměťové médium, na kterém jsou uložena všechna data potřebná 
    k činnosti PC. Také se zde ukládají data vytvřená uživatelem počítače.
    - Slouží k trvalému uchování informací v PC.
