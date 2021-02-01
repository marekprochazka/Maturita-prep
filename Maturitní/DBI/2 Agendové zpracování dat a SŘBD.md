# 2. Agendové zpracování dat a SŘBD

##

**INFORMAČNÍ SYSTÉM** 
* přehledná organizace dat, aby se s nimi "dobře pracovalo"
* Může se jednat o SW-systém, ale i o informační tabuli na úřadě
 
# Struktura tabulky
* struktura tabulky = seznam sloupců v dané tabulce

### V každém sloupci musí být ve struktuře uvedeno alespoň
* **Název** sloupce - bez mezer, obvykle i bez diakritiky
* **Datový typ** sloupce - existují 4 základní:

    * 1. text, znakový typ, string, character, char/varchar
    * 2. číslo, number, numeric, decimal
    * 3. datum (+čas), date, datetime
    * 4. logická hodnota, boolean, logical (ano/ne, pravda/nepravda)
    * každý SŘBD nabízí většinou i řadu dalších datových typů, často se však jedná o různé varianty uvedených 4 základních

* **Velikost** sloupce

    * u textů se uvádí v počtu znaků/sloupce
    * u numerického datového typu se udává nejčastěji v podobě 2 čísel - celkový počet znaků (včetně případné desetinné tečky a znaménka mínus) a počet desetinných míst (z toho)
    * u některých datových typů se velikost neuvádí, neboť je pevně dána (např. datum, logická hodnota)
    



Přiklad:
![alt text][obrazek]

[obrazek]: https://i.imgur.com/1Raj8wv.png