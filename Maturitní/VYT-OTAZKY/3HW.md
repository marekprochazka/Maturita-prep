# 3. HW - Vnější paměti s elektromagnetickým záznamem


### Princip

- součást nebo zařízení, které umožňuje uložit obsah informace (zápis do paměti), uchovat ji po požadovanou dobu a znovu ji získat pro další použití
- informace je obvykle vyjádřena jako číselná hodnota 0 nebo 1; pro uchování informace tedy stačí signál (např. el. napětí), který má dva rozlišitelné stavy, není tedy třeba znát přesnou velikost signálu
- základní jednotkou je bit
- logická hodnota bitu může být reprezentována různými fyzikálními veličinami:
    - přítomnost el. náboje
    - stav el. obvodu, např. v tranzistoru
    - různou propustností nebo odrazivostí světla v optických pamětech
    - bite [bajt] – 8 bitů, např. 1 kB = 1024 bajtů
- RAID – zabezpečení, kdy jsou stejná data ukládána na několik na sobě nezávislých disků (selže jeden != ztráta dat)

### Typy:
- HDD:
    - velkokapacitní paměťové zařízení s pohyblivou magnetickou vrstvou, informace zde zůstanou uloženy i po odpojení od napájení
    - Princip: jednotlivé B jsou převedeny na proud bitů, tento proud je následně převáděn na změny proudu v záznamové hlavě
    - Adresace:
        - data jsou rozdělena do soustředných kružnic (stopy), každá stopa obsahuje určitý počet sektorů (sektor je nejmenší adresovatelnou jednotkou na disku)
        - Adresa fyzického sektoru na disku se skládá z čísla stopy (cylindru) pro vystavení hlav, z čísla povrchu pro přepnutí hlavy a konečně čísla sektoru, které určuje latenci (čekání, než se disk pootočí do žádané polohy).
        - Pro přístup k datům disku se používala starší metoda adresace disku Cylindr-Hlava-Sektor (CHS), která disk adresuje podle jeho geometrie. Hlavní nevýhodou byla u osobních počítačů IBM PC omezená kapacita takto adresovaného disku (8 GB) a software musel rozlišovat různé geometrie disků.
        - U disků vyšších kapacit na rozhraní ATA již adresa sektoru neodpovídá skutečné fyzické geometrii disku (implementaci). Tato novější metoda adresování disku se označuje jako LBA a sektory se číslují průběžně. Není třeba znát geometrii disku, je možné adresovat až 144 PB (144 miliónů GB). Rozhraní SCSI používá lineární číslování sektorů disku již od své první verze, ostatní novější rozhraní také již obdobnou metodu používají.
    - Struktura:
        - Elektromechanické části: disková hlava, hřídel, diskové kotouče, vystavovací mechanismus, pohony
        - Elektronické části – deska s plošnými spoji (řadič, ROM, Cache) konektory, jumpery
        - Software – geometrie disku (stopy, cylindry, sektory, hlavy); logická struktura, souborové systémy
    - Elektromechanické části pevného disku:
        - Disková hlava – umístěna na pohyblivém raménku a má plošku aerodynamického tvaru; indukční hlavu používá pouze pro zápis, pro čtení se používá prvek založený na změně elektrického odporu při vystavení magnetickému poli; hlava pohybující se nad rotujícím diskem zapíše bity informace jako zmagnetizované oblasti ve stopách, které jsou později čteny MR-senzorem
        - Osa disku (pohon disku) – na společné hřídeli je umístěno několik diskových kotoučů; na pohonu disku je závislá průměrná čekací doba; čím jsou otáčky menší tím je čekací doba menší; čím více otáček tím horší provozní podmínky – tvorba tepla uvnitř disku
        - Diskové kotouče (plotny) – nejdůležitější částí disku, protože na nich jsou uložena data; dnešní velikosti jsou 3.5 a 2.5 palců; menší průměr vede ke snížení kapacity disku; zpravidla 1 – 3 plotny; každá plotna má dva povrchy a každý z nich má vlastní čtecí a zapisovací hlavu; čím víc ploten tím hlučnější provoz; jsou vyrobeny z hliníkových slitin
    - Elektronické části HDD
        - Hlavními funkcemi elektroniky jsou: kontrola rychlosti otáčení disku, kontrola přesunu hlav nad plotnami, zprostředkování všech operací čtení nebo zápis, překlad geometrie disku, spravování vyrovnávací paměti; doplnění pokročilých funkcí pro zvýšení rychlosti; řízení toku informací disku
        - Řadič – jeho úkolem je na základě požadavků řídit čtení/zápis dat na HDD; koordinuje činnost všech částí HDD
        - ROM – uložen miniaturní OS pevného disku (firmware), řízení pohonu, kódování a dekódování dat
        - RAM (CACHE) – statická RAM, která obecně slouží k dočasnému uložení dat mezi částmi počítače, které pracují různou rychlostí, jejím úkolem je urychlení přenosu dat
    - Geometrie pevného disku
        - Před zápisem jakýchkoliv dat je nutné pevný disk nejprve naformátovat 
        - Stopa – je oblast pro ukládání dat ve tvaru soustředné kružnice, kterých může být až 10 000
        - Sektor – je část jedné stopy ohraničená na začátku i konci identifikačními značkami určujícími mimo jiné jeho číslo, polohu, začátek a konec
        - Cylindr – sada stop se stejným číslem na různých stranách ploten, musí se nadcházet nad sebou 
        - Cluster – nejmenší použitelné množství dat pohromadě
    - oproti SSD je levnější a může mít mnohem vyšší kapacitu (až 16 TB), ale je pomalejší při čtení /zápisu (100-200 MB/s) a také obsahuje mechanické pohybující se části – vyšší pravděpodobnost rozbití

- SSD:
    - neobsahuje pohybující se části, takže je mechanicky mnohem odolnější, ale je oproti HDD dražší
    - využívají flash paměť pro uložení dat – ta je organizována po blocích
    - stejné rozhraní SATA jako HDD
    - oproti HDD mají nižší spotřebu el. energie, vyšší rychlost čtení i zápisu a lehčí a menší (využití v ntb)

- Disketa:
    - data jsou podobně jako u HDD organizována do stop a sektorů (jejich seznam je uložen v alokační tabulce)
    - v 21. století byly postupně vytlačeny novějšími technologiemi (Flash disky, HDD…)
    - skládá se z plastového obalu a vnitřního nosiče s magnetickou vrstvou; uvnitř obalu je výstelka, která chrání magnetickou vrstvu proti poškrábání
    - pro čtení se používala FDD mechanika

### Rozhraní pro připojení pevných disků:
- IDE:
    - připojení diskových jednotek pomocí 40-žilového kabelu
    - novější verze vyžadují 80-žilový kabel, kvůli rušení signálu elmag. polem
- ATA (PATA):
    - starší rozhraní
    - Sada příkazů pro univerzální ovládání všech disků
    - několik generací - ATA1 až ATA6
- SATA:
    - aktuálně používané rozhraní
    - jednoduchý propojovací kabel, na rozdíl od paralelní komunikace nedochází k přeslechům
    - komunikace probíhá sériově na vysoké frekvenci (až 6000 MHz)
    - jedná se o kabel se sedmi vodiči (4 datové a 3 GND)
    - obousměrný přenos
    - eSATA (externí SATA):
        - jedná se o SATA kabel s integrovaným napájením, využívá se u externích disků kde díky redukci na USB není potřeba další zdroj napájení






