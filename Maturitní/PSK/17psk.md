# Šifrování a elektronický podpis

Kryptografie se dělí na:
- Symetrickou kryptografii
- Asymetrickou kryptografii

- pomocí šifrování se nezabezpečená data zašifrují pomocí kryptografie a jsou dešifrovatelná jen pomocí klíče

- slouží k ochraně a proti zjištění cizí osobou

- **klíč** - veklé náhodné číslo 
- v praxi to může být např zachycený šum na A/D převodníku, nebo snímání náhodných pohybů myší uživatele

## Symetrická kryptografie
- používá k dešifrovaní jediný klíč
- klíč je stejný na obou stranách

![asd](https://mamut.spseol.cz/nozka/psk/172-sifrovani_I/symetricka_sifra.png)

![asd](https://mamut.spseol.cz/nozka/psk/172-sifrovani_I/sifrovani.png)

- výhodou je nízká výpočetní náročnost
- asymetrické šifry můžou být 100x pomalejší
- **nevýhodou** asymetrického klíče je, že se obě strany musí na klíči domluvit, což může být nemožné

## Asymetrická kryptografie

- vytvoří keypair (public key, private key)

- To co zašifruje veřejný klíč, rozšifruje pouze soukromý klíč. Toho se využívá při šifrování zpráv.
- To co zašifruje soukromý klíč rozšifruje pouze veřejný klíč. Toho se využívá u elektronického podpisu.

![asd](https://mamut.spseol.cz/nozka/psk/172-sifrovani_I/Public-key-crypto-cs.png)

- **Názvosloví** 

-klíč = private key
- certifikát = public key

- **Šifrování zpráv**

- kdokoli může hodit dopis do schránky ale jen jedna osoba má od schránky klíč

- bob zašifruje zprávu aliččeným veřejným klíčem a alice si zprávu dešifruje pomocí jejího privátního klíče

![sd](https://mamut.spseol.cz/nozka/psk/172-sifrovani_I/Public_key_encryption-cs.png)

- **Elektronický podpis**

- Opačný problém

- Alice musí potvrdit že tuto zprávu psala ona, udělá to svým privátním klíčem a každý si může oveřit veřejným klíčem že to byla opravdu ona

![podpis](https://mamut.spseol.cz/nozka/psk/172-sifrovani_I/Public_key_signing-cs.png)

## Shrnutí 

![ads](https://mamut.spseol.cz/nozka/psk/172-sifrovani_I/Public_key_encryption_signing-cs.png)

## Hybridní systémy

- Symetrické šifry se použijí s asymetrickými a využijí tak výhod obou systémů

- odpadá problém distribuce klíčů a systém je dostatečně rychlý

- zašifruje se náhodným symetrickým, poté veřejným asymetrickým

- dešifrovat může pouze majitel tajného klíče

- **funguje jako bezpečný kanál pro přenos symetrického klíče**

- po každé zprávě se vygeneruje nový symetrický klíč

# Hashovací funkce (Hash, Otisk, Fingerprint)

- mat. funkce pro převod do malého čísla

- Nejznámější funkce jsou MD5, CRC, SHA

- hashovací funkce jsou bezpečné pokud je nemožné 
1. najít zprávu, která odpovídá svému otisku
2. najít 2 rozdílné zprávy, které mají stejný otisk

![asd](https://i.gyazo.com/f584353f9946d32e4663f37e194b9693.png)

- jestliže mají 2 zprávy stejný hash nejpíše se shodují
- používá elektrojického podpisu pro ověření pravosti klíče

## Problémy výměny klíčů

- Každý, kdo systém používá si musí být jistý identitou veřejných klíčů
- **jinak receno**
- musím si být jistý, že klíč na kterém je jmenovka Alice, opravdu patří Alici
- kdyby to nebyj jejich klíč, mohla by do konverzace vstoupit třetí osoba

- Tento problém se označuje jako **Man in The Middle**

- nabízel se problém že si klíče lidé předají z ruky do ruky, ale to může být odposoucháváno též

* **Řešení**
- ověření identity pomocí Hashe -- fingerprintu
- používá se síť důvěry nebo certifikační autorita

## Software

- Prvním sowtwarem byl používán **PGP- Pretty good privacy**, byl považován jako zbraň

- OpenPGP

- oba využívají **Web of trust**

## Jak funguje elektronický podpis

![asd](https://mamut.spseol.cz/nozka/psk/176-sifrovani_II/podpis.png)

1. Ze zprávy se vygeneruje hash
2. hash se zašifruje pomocí privatního klíče a zašifruje se ke zprávě
3. Na přijímací straně se hash pomocí public key rozšifruje
4. Na přijímací se znovu vytovří hash
5. Přijatý a přenesený hash **se porovnají**








# QR code








