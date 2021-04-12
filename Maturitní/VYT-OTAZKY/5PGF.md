# 5. Počítačová grafika - obecné pojmy


WIP 

Základní rozlišení (výška X šířka), Dpi -> jak se to počítá? 
dpi -> body na palec
mám obraz co máx 1000 na výšku a 400 na šířku a 300 dpi, jakou má velikost v cm
1 palec je 2,4 cm
=> vydělím šířku dpi a převedu palce na cm
=> to samo šířka

### Rastrová grafika:
- Bitmapový obrázek je tvoře pravidelnou mřížkou z bodů, přičemž každý bod má přiřazenou určitou barvu
- každy bitmapový obrázek je tedy definován svou velikostí (šířkou a výškou), rozlišením (hustotou barevných bodů) a barevnou hloubkou (počet možných barev, kterých může každý bod nabývat
- Bitmapový obrázek je soubor malých čtverečků zvaných pixely, které dohromady vytvářejí obrázek
- Tato grafika je náročná na paměť z tohoto důvodu se používá komprese, která umožňuje velikost obrázku zmenšit tím, že stejné nebo velmi podobné body se spojí v jeden celek
- Nevýhodou této grafiky je nemožnost měnit velikost obrázku, aniž by tím došlo ke zhoršení jeho kvality
- Výhodou této grafiky je snadnost pořízení obrázku pomocí fotoaparátu nebo skeneru
- Rozlišení obrázku – počet bodů na jednotku vzdálenosti; používaná jednotka DPI popisuje potřebné množství bodů na délku jednoho palce; hustota barevných bodů
- Rozlišení monitoru – počet pixelů, které může být zobrazeno na obrazovce, uvádí se jako počet sloupců x počet řádků
- Barevná hloubka – každý z jednotlivých bodů může nabývat jednu z barev zvolené barevné palety (RGB), která obsahuje 16,7 milionu barev; na webu se nejčastěji setkáváme s paletou 256 barev
- Formáty rastrových obrázků – dnes existuje více než 50 rozšířených formátů
    - JPEG – v dnešní době je používán nejčastěji; i při kompresi zachovává dostatek informací v obrázku, ztráta kvality není tak postřehnutelná; vhodný pro plynule přechody mezi barvami na obrázku, každým dalším uložením dochází ke komprimaci obrázku a tím zhoršení kvality
    - GIF – jeden z nejoblíbenějších a nejstarších formátů; velké zmenšení obejmu dat; více obrázků v jednom souboru; vhodný pro přenos obrázku po síti; vhodný pro ostré hrany; lze použít i pro malé a krátké animace; maximální počet barev je 256 v jednom obrázku, průhledné pozadí
    - PNG – primárně zaměřen na přenos obrazu v síti; schopen ukládat obraz v mnoha barevných rozlišeních; bezztrátově ukládat obrazy v barevném rozlišení true color; dosažený kompresní poměr není tak výrazný jako u JPEG, 48 bitů/pixel
    - BMP – nejstarší a nejjednodušší formát bitmapového obrázku; použitelnost na webu je poměrně špatná a tento formát se již v podstatě na stránkách nepoužívá; velmi velké výsledné soubory a mnohdy nepomůže ani zmíněná komprese
    - PCX, DCX – formát firmy Zsoft, ma. rozlišení 65536x65536 pixelů, ukládá se buď bez nebo s kompresí
- Adobe Photoshop, Zoner Photo studio, Gimp, Adobe Lightroom
### Vektorová grafika:
- Obraz je reprezentován pomocí geometrických objektů – body, přímky, křivky, polygony
- Práce s objekty, které jsou samostatné a matematicky definované
- Základem vektorové grafiky je matematika – obrázek je tvořen z vektorů (křivek) – Bézierovy křivky
- Řídící body – křivky deformují směrem a velikostí
- Výhodou je její nezávislost na rastru – při zvětšování objektů nedochází ke zkreslení
- Velikost souborů je výrazně menší než u rastrové
- Je v podstatě bezztrátová – nepodléhá žádné kompresi; je možné ji libovolné zmenšování bez ztráty kvality
- Používá se, když potřebujeme vysokou přesnost – tvorba vizitek, log, diagramů, grafů, reklamních materiálů


- Formáty vektorových obrázků:
    - SVG – umožňuje zobrazovat dvourozměrnou grafiku s podporou interaktivity animací; myšlen nejprve pro použití na webu; je založen na XML proto je možné v souborech vyhledávat, indexovat a komprimovat je; jelikož je XML textový soubor, lze tvořit a upravovat SVG grafiku i v obyčejném textovém editoru
    - PostScript - .ps .eps – je značkovací jazyk a formát vektorové grafiky, který je programovací jazyk určeny ke grafickému popisu tisknutelných dokumentů; považován za standard pro dražší tiskárny; dnes nahrazen formátem PDF
    - WMF – vektorový grafický formát, spolehlivý černobíle grafice a není vhodný pro barevnou grafiku, lze do něj umístit Bitmapy, což patří k jeho přednostem 
    - .ai, .cdr, .zmf – jsou koncovkami projektů, které lze tvořit v grafických programech; Adobe illustrator .ai; Corel .cdr; Zoner callisto .zmf; je nutné zkontrolovat správnost grafiky
- CorelDRAW, Inkscape, Zoner Callisto, Adobe Illustrator
# Barevné modely:
- Aditivní model (sčítání):		Subtraktivní model (odčítání): 
 
- RGB:
    - aditivní model (sčítání)
    - monitor používá 3 základní složky – R (červená), G (zelená), B (modrá)
    - mezi jednotlivými barvami vznikají barvy k nim doplňkové
    - všechny tři barvy dohromady tvoří bílé světlo
    - počáteční bod (0, 0, 0) je černá barva
    - v modelu RBG se barvy kódují pomocí tří hexadecimálních čísel, každé v rozsahu 00 – FF(0 – 255); někdy se hodnoty udávají v dekadické soustavě; každé číslo uvádí podíl barevné složky ve výsledné barvě v pořadí Red Green Blue
    - využití na monitorech, kódování barev pro webové stránky
- CMY(K):
    - subtraktivní model (odčítání)
    - používá se při tisku, v praxi se přidává ještě černá barva (K v názvu modelu)
    - funguje velmi podobně jako RGB model, akorát převráceně
    - základní barvy jsou azurová (kyan), purpurová (magenta), žlutá (yellow); černá (blacK)
- HSV (HSB):
    - RGB je model vhodný pro míchání barev, HSV model více odráží vnímání barev člověkem
    - Hue, Saturation, Value; Hue Saturation, Brightness
    - Hue – barevný tón, neboli odstín, popisuje čistou, nasycenou barvu
    - Saturation – sytost, popisuje, jak moc je v barvě přimícháno bílého světla, zmenšujeme-li nasycení barvy, dostaneme až barvu bílou
    - Value, Brightness – jas, popisuje absenci světla, tj. jak moc je barva tmavá; zmenšujeme-li jas, dostaneme barvu černou
    - čisté (nasycené) barvy najdeme na obvodu podstavy kužele
    - směrem k vrcholu klesá jas barev
    - směrem ke středu podstavy klesá nasycení barev
    - barvy jednoho barevného odstínu najdeme v trojúhelníku, jehož vrcholy jsou střed podstavy, vrchol a bod na obvodu podstavy
- HSL:
    - Hue, Saturation, Lightness
    - Hue – barevný tón, neboli odstín, popisuje čistou, nasycenou barvu
    - Saturation – sytost, popisuje, jak moc je v barvě přimícháno bílého světla, zmenšujeme-li nasycení barvy, dostaneme až barvu bílou
    - Lightness – světlost
    - je velmi podobný modelu HSV
    - tvar modelu odpovídá skutečnosti – schopnost rozlišování barevných odstínů skutečně klesá se ztmavováním a zesvětlováním základní čiré barvy, zvyšování a snižování světlosti barvy skutečně spočívá v přidávání světlého nebo tmavého pigmentu 

linky:
https://docs.google.com/document/d/1Eutjnk2llzziIhUjZ6ddwVI5c35zgV5jEHSKNfppcbg/edit