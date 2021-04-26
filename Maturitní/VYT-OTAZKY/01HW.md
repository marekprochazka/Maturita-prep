# 1. HW - základní deska a její části


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

### Chlazení:
- Teplovodivá pasta
- Pasivní chlazení:
    - kovová nepohyblivá součástka, která má na sobě navařená žebra pro zajištění co největší plochy z důvodu lepšího předávání tepla okolnímu vzduchu (vyrobeny buď z mědi(dražší) nebo z hliníku (levnější))
- Aktivní chlazení:
    - Proudícím vzduchem - rotující ventilátor vhání pomocí vhodně tvarovaných lopatek vzduch na pasivní část chladiče, která je v přímém kontaktu s chlazenou komponentou a odvádí od ní teplo (nejčastěji používáno jako doplněk pasivního chlazení)
    - Vodní chlazení - tvoří uzavřený okruh ve kterém chladící médium, v tomto případě voda, obíhá; na jedné stran se přenáší teplo z chlazené komponenty do kapaliny a na druhé straně tuto kapalinu ochlazujeme; voda dokáže odvést více tepla než vzduch

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
    - ISA - starší typ pasivní sběrnice, šířka 8 nebo 16 bitů; systémová sběrnice pro připojení rozšiřujících karet do základní desky; používá paralelní přenos dat; přenos oběma směry; nabízí plug and play
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

### Paměti ROM:
- PROM:
    - pomocí speciálního zařízení (programátor) si ji naprogramuje uživatel, poté nelze změnit
- EPROM:
    - informaci zapsanou v paměti je možné vymazat UV zářením a znovu přeprogramovat (uložení dat, která nejsou potřeba měnit, např. řízení mikrovlnky)
- EEPROM:
    - mazání probíhá pomocí elektrického impulsu, počet zápisů je omezen cca 100 000
- Flash ROM
    - elektricky programovatelná paměť; uchovává informace v paměťových buňkách; informace zachovává i po odpojení od elektrického napájení (SD karty)

### Paměti RAM:
- SRAM (statická RAM):
    - velmi rychlá paměť a  vyžaduje menší proud než paměť dynamická
- DRAM (dynamická RAM):
    - je nutné ji periodicky obnovovat
    - SIMM – už má kontakty a výhodou byla snadnější instalace oproti SIPP
    - DIMM – všechny novější paměti (SDRAM, DDR, DDR2, DDR3) jsou umístěny na těchto modulech DIMM; šířka sběrnice je 64 bitů
    - SO-DIMM – nejčastěji určeny pro notebooky
- Cache – vyrovnávací paměť umístěna mezi dvě zařízení, která nepracují stejnou přenosovou rychlostí; několik druhů L1, L2, L3 od rychlejší po nejpomalejší


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
