# 1. Základní pojmy teorie zpracování dat

## Hromadné zpracování dat
= Automatizované zpracování velkého množství údajů o velkém množství objektů
## Proč vzniká problém zpracování dat
* V životě je často zapotřebí evidovat údaje o nějaké skutečnosti. Například o skupině lidí (zaměstnanců, studentů, členů sportovního oddílu apod.), o zvířatech nebo rostlinách (evidence zoologické nebo botanické zahrady apod.)
* V praxi je potřeba mít o těchto objektech přehled, aby se v údajích dobře vyhledávalo, opravovalo, doplňovalo atd.
* To lze řešit i bez počítače, např. pomocí sešitu, kartotéky, apod.

## Co a jak se zpracovává
Objekty (lidi, zvířata, věci, jevy) popisujeme pomocí jejich vlastností.(zaměstnanec firmy má jméno, adresu, funkci, plat;kniha v knihovně má název, autora, rok vydání, cenu, …).
* Při evidencích se pak předem rozhodneme, které vlastnosti potřebujeme sledovat.
* Vybrané vlastnosti budeme nazývat **atributy.**
* I při "ručním" zpracování si atributy pojmenujeme (nadpis sloupce) a zvolíme nějakou formu evidence

**1. Tabulka**  
*na papír či do sešitu nalinkujeme tabulku, sloupce popíšeme názvy vybraných<br>
evidovaných vlastností, celou tabulku pojmenujeme typem evidovaných objektů.*

**PŘÍKLAD 1:** *Evidence dat o zaměstnancích v tabulce. Zaměstnanci jsou zapisováni
v pořadí, jak byli do firmy přijati. Potřebujeme evidovat jejich jméno, adresu, funkci,
plat.<br> Pojmenujeme tuto tabulku Zaměstnanec a její strukturu (= seznam evidovaných
vlastností, atributů) zapíšeme takto: **Zaměstnanec (jméno, adresa, funkce, plat)**

*Tabulka vypadá takto:*<br>
<br>
**Zaměstnanec**
| Jméno           | adresa                  | Plat   | 
| :-------------: |:-------------:          | :-----:|
| Žižka Kamil     | Studená 10, Ostrava 8   | 12000  |
| Bednářová Petra | Růžová 12, Ostrava      |  8000  |
| ...             |                         |        |
| Novák František | Široká 2, Ostrava       |  1700  |

**Kartotéka**
* kartotéční listy, na každém je "formulář" obsahující názvy evidovaných údajů.
* každý objekt je zapsán na jednu evidenční kartu
* všechny listy jsou umístěny do krabice nebo šuplíku<br>

**Výhodou** je<br>
* možnost ukládat listy v nějakém uspořádnání (zaměstnanci abecedně podle jména,knihy podle názvu nebo autora apod.)
* toto uspořádání dodržovat i při všech žměnách, přidávání a rušení karet.
    
# Pojmy

**DATA=UDAJE**
* různé údaje z realného světa (získané měřením, generováním, pozorováním či pouhým zaznamenáním nějaké skutečnosti),které potřebujeme evidovat/zpracovávat

**INFORMACE**
* smysluplné interpretace dat (tzn. to, co se z těch dat dozvíme)

**POLOŽKA**
* nejmenší (dále již logicky nedělitelná) část dat (např. příjmení)

**TABULKA=DATOVÝ SOUBOR**
* množina záznamů o objektech stejného typu (např. studenti)

**DATABÁZE**
* ucelená množina (skupina) tabulek, které spolu logicky souvisí
* typicky jde o tabulky jednoho informačního systému



**INFORMAČNÍ SYSTÉM** 
* přehledná organizace dat, aby se s nimi "dobře pracovalo"
* Může se jednat o SW-systém, ale i o informační tabuli na úřadě
 
