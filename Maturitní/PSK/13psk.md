# Vrstvy TCP/IP

![vrstvy](http://upload.wikimedia.org/wikipedia/commons/1/10/Porovn%C3%A1n%C3%AD_TCPIP_a_modelu_ISOOSI.jpg)

**4 vrstvy**
1. Aplikační vrstva (HTTP, HTTPS, SSH)
2. transortní vrstva (TCP, UTP)
3. Síťová vrstva (IPv4, IPv6)
4. Vrstva síťového rozhraní (Ethernet, Wifi)

Síťová spojení:<br>
![sítovaspojeni](https://mamut.spseol.cz/nozka/psk/134-tcpip_I/Tcpip_vrstvy.png)

**Architektura TCP/IP**

![arch](https://mamut.spseol.cz/nozka/psk/134-tcpip_I/Tcpip_vrstvy.png)<br>

* Architektura umožňuje výměnu protokolů jedné vrstvy bez dopadu na ostatní<br>

![as](https://mamut.spseol.cz/nozka/psk/134-tcpip_I/paralela.png)

* každá nižsí vrstva přiřadí hlavičku, patičku (provozní data)

![ads](https://mamut.spseol.cz/nozka/psk/134-tcpip_I/tcpip_zapouzdreni.png)

# Vrstva síťového rozhraní

* **Zabezpečí komunikaci v lokální síti**

* Dělí se na
1. Fyzickou vrstvu
2. Linkovou vrstvu

* **Fyzická vrstva**
* definuje fyzikální a elektrické vlastnosti zařízení
* stanovuje způsob přenosu jedniček a nul

* **Linková vrstva**
* Spojuje systémy dohromady
* Uspořádává data do frames (logické celky)
* oznamuje neopravitelné chyby
* přiloží **FYZICKOU ADRESU (MAC)**

* **MAC - 9E:28:94:CE:53:0C**

* **Síťové prvky**
* Hub - opakovač
* Bridge
* Switch

# Síťová vrstva

* poskytuje IP
* cílem je doručit data po celém internetu

* Př: IPv4, IPv6, ICMP

# Transportní vrstva

* **TCP**

* přenost dat se zárukami, které vyžadují aplikace
* zachová pořadí
* odstraní duplikace
* odesílá se po TCP segmentech 

* **UTP**
* přenost dat bez záruk
* ztráty řeší snížením kvality /opakovani dotazu

* **Každá aplikace používá jiný port**

# Aplikační vrstva

* poskytuje přístup a umožňuje spolupráci













