# 6. Vektorový editor 

## Vektorová grafika 

- Vektorová grafika je jeden ze dvou základních způsobů reprezentace obrazových informací v počítačové grafice.
- Vektorový obrázek je složen z přesně definovaných útvarů, jako jsou body, přímky, křivky a mnohoúhelníky.
- Využívá se nejčastěji pro nefotorealistsické obrázky

## Výhody vektorové grafiky 

- Je v ní možné libovolné zmenšování nebo zvětšování obrázku beze ztráty kvality
- Je možné pracovat s každým objektem v obrázku odděleně.
- Výsledná paměťová náročnost obrázku je u jednolitých barevných obrázků menší, než při použití rastrového zápisu 

## Nevýhody vektorová grafiky 

- proti rastrové grafice zpravidla složitější pořízení obrázku. V rastrové grafice lze obrázek snadno pořídit pomocí fotoaparátu nebo skeneru.
- Překročí-li složitost grafického objektu určitou mez, začne být vektorová grafika náročnější na operační paměť a procesor než grafika bitmapová.
- Nehodí se na zápis složitých barevných ploch, například fotografi

## Využití vektorové grafiky 

- Vektorová grafika se používá zejména pro počítačovou sazbu, tvorbu ilustrací, diagramů, logotypů, nebo při tvorbě flashových animací. Pro práci s vektorovou grafikou se používají vektorové editory 
(např. Adobe Illustrator, CorelDRAW, Inkscape nebo Zoner Callisto 5).

## Formáty vektorové grafiky 

- .eps, .ps – PostScript.
- .pdf – Portable Document Format.
- .ai – Adobe Illustrator Artwork.
- .cdr – Corel Draw.
- .svg – Scalable Vector Graphics.
- .zmf – Zoner Callisto.

## Inkscape 
- Inkscape je open-source grafický vektorový editor, používá se pro vytváření nebo úpravě vektorové grafiky, jako jsou ilustrace, diagramy, perokresby, ale i složité obrazce a loga
- základní formát pro práci v Inkscape je SVG, jakýkoli jiný formát musí být na SVG převeden, pokud jej chceme upravovat
- Inkscape umožňuje také export G-code formátu pro CNC stroje
- Je dostupný pro platformy s Windows, Mac i Linux

### Základní nástroje: (lišta vlevo)
- __Nástroj obdélníky a čtverce__: vytváří obdélníky a čtverce, rohy čtverců a obdélníků lze zaoblit.
- __Nástroj tvorba kvádrů__: vytváří třírozměrné útvary, které mají nastavitelné perspektivy XYZ a konfigurovatelné hodnoty pro úběžníky. 3R pole jsou ve skutečnosti skupiny cest a po zrušení seskupení je lze dále upravovat.
- __Nástroj kruhů, elips a oblouků__: kruhy a elipsy lze transformovat na oblouky (např. otevřený půlkruh) a segmenty (např. uzavřený půlkruh).
- __Nástroj hvězdy a mnohoúhelníky__: K napodobení spirografu lze vytvořit vícebodové (3 až 1 024 bodů) hvězdy se dvěma ovládacími úchyty (základní a špičkový)
    - Mnohoúhelník s jedním ovládacím (základním) úchytem lze použít k vytváření položek na základě počtu šestiúhelníků, pětiúhelníků atd.
- __Nástroj tvorba spirál__: vytváří spirály, které mají konfigurovatelný počet otáček (obrátek)
    - rozdílnost (hustota / rozprostření vnějších závitů)
    - vnitřní poloměr (vytažení ze středu)
- __Nástroj tužka (cesty)__: který umožňuje kreslení čar od ruky.
- __Kresba béziérových křivek__: vytváří Bézierovu křivku uzel po uzlu nebo úsečky na stejné cestě.
- __Kaligrafický nástroj (vesty)__: vytváří kaligrafické či štětcové tahy od ruky, nástroj může volitelně používat údaje o tlaku a náklonu z grafického tabletu.
- __Textový nástroj__: vytváří texty, které lze použít některý z operačních systémů (OS) osnovy a Unicode fontů, včetně podpory psaní zprava doleva
    - Jsou implementovány nástroje převod textu na cesty, normální, tučné, kurzíva, zúžené a rozšířené písmo, zarovnání (vlevo, vpravo, na střed, do bloku), horní index, dolní index, vertikální a horizontální text
    - Všechny textové objekty lze transformovat pomocí řádkování (rozestupy mezi účařími), prostrkávání písmen, mezislovních mezer, vodorovného párování znaků, svislého posunutí a otočení znaků buď ručně, nebo prostřednictvím přednastavené nabídky
    - Text může být umístěn podél cesty (text i cesta zůstávají upravitelné), může proudit do kontrolovaného tvaru nebo lze zkontrolovat pravopis textu
    - K verzi 0.91 nejsou k dispozici odrážkové seznamy, číslované seznamy, odsazení a podtržený text.
- __Nástroj nástřik objektů__: vytváří kopie nebo klony jedné nebo několika položek, vyberte položku (položky), poté na položku nástřik klikněte na plátno, pohněte myší nebo posouvejte kolečkem myši.
- __Nástroj vyplnění prostoru__: vyplní ohraničenou oblast daného objektu (vektoru). Nástroj vyplnění prostoru funguje spíše opticky než geometricky, zaplňuje veškerý prázdný prostor, který může obsáhnout, a může pomoci s trasováním obrazu.
- __Nástroj diagramové spojky__: vytváří propojené cesty založené na objektech, často se používá ve vývojových diagramech, diagramech nebo schématech.

### Specializované nástroje:

- __Rastrová grafika__: Inkscape podporuje export bitmapových obrázků (jako PNG obrázek) celé kresby (všechny objekty), aktuálního výběru, objektů uvnitř obrysu stránky a vlastní souřadnice. Importuje bitmapové obrázky, volba Soubor> Import umožňuje uživateli vybrat buď „vložit“, nebo „propojit“ obrázek do souboru. Vkládání obrázků do Inkscape automaticky vkládá obrázky do souboru. Inkscape podporuje import a vkládání PNG, JPEG a BMP. Inkscape podporuje trasování obrazu, aneb proces získání vektorové grafiky z rastrových zdrojů.
- __Klony__: klony jsou podřízené objekty původního nadřazeného objektu (objektů), které mohou mít jiné transformace než transformace rodičovského objektu. Klony lze vytvořit pomocí kopií, nástroje nástřik nebo rozhraní nabídky. Transformace zahrnují; velikost, poloha, rotace, rozostření, neprůhlednost, barva a symetrie (rozložení). Klony se okamžitě aktualizují, kdykoli se změní nadřazený objekt.
- __Vykreslení> Rozšíření> Vykreslení (nabídka)__ vykreslí objekty na plátno. Mezi příklady vykreslování patří čárové kódy, kalendáře, mřížky, ozubená kola, spirografy, koule a další.
- ___Symboly> Objekty> Symboly (z nabídky)__ umožňují kopírovat a vkládat symboly z editovaného dokumentu a z knihoven symbolů, což je funkce ve verzi 0.91


### Užitečný odkazy: http://www.ivt.mzf.cz/grafika/inkscape/

[Otázka 5](05HW.md)

[seznam otázek](seznam_otazek.md)
            
[Otázka 7](07HW.md)
            