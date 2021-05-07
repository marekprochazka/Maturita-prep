# Protokoly IP, TCP, UDP

## IPv4

* Jednoznačná adresa
* nejrozšířenější verze
* 32 bitů, 8 x 4

195.113.190.100<br>

* dekadicky, oddělené tečkou
* hodnoty 0 až 255

* každá adresa patří do skupiny adres podsíť / **subnet**

* zakryje IP adresu (Maska síťe)
* 11111111.11111111.11111111.11000000
* maska ze dá zapsat podle počtu 1, takže 26


* Z **IP adresy** a **masky** lze provést výpočet:

1. **Adresy sítě** (Network)
* maska se předloží přes IP adresu, tam kde jsou v masce jedničky se IP opisuje, tam kde nuly se čísla v IP nahradí nulou
* první adresou v podsíťi

2. **Všesměrovou adresu** (broadcast)
*  Maska se přeloží přes IP adresu, tam kde jsou v masce binární jedničky se IP opisuje a tam kde jsou v masce binární nuly píší se naopak samé jedničky
* poslední adresou v podsíťi
* nesmí být používané pro žádné zařízení

## IPv6

* větší adresní prosotor
* 128 bitů
* 2x delší
* skládá se z:
**prefix** - 64 bitů<br>
část hosta/ rozhraní 64 bitů<br>

* 2001:0db8:85a3:08d3:1319:8a2e:0370:7334.
* 4 nuly, nebo 8 atd mohou být vynechány, a zapsány jako :(nic):

Všechny tyto adresy jsou tedy platné a rovnocenné:<br>
<br>
2001:0db8:0000:0000:0000:0000:1428:57ab<br>
2001:0db8:0000:0000:0000::1428:57ab<br>
2001:0db8:0:0:0:0:1428:57ab<br>
2001:0db8:0:0::1428:57ab<br>
2001:0db8::1428:57ab<br>
2001:db8::1428:57ab<br>

* ale 3 dvojtečky **:::** nejsou platné

**Druhy IPv6 adres**<br>

1. Unicast
* odešle jednomu počítači

2. Multicast
* multicast adresy mají prefix FF00
* více počítačům

3. Anycast
* doručí nejbližšímu počítači

## TCP - Transmission Control Protocol

* přenost dat se zárukami, které vyžadují aplikace
* zachová pořadí
* odstraní duplikace
* odesílá se po TCP segmentech
* více dat 

* TCP na straně příjemce posílá potvrzení, že vše přišlo v pořádku
* jestli odesílateli nic nepřijde do urč. času odešlou se znovu
* před odesíláním si data zkontroluje, vytvoří paket a zkontroluje znovu podle původního


**Navázání - Three Way Handshake**

 * obě strany se dohodnou na **čísle sekvence** a **potvrzovacím čísle** (na potvrzovacím čísle vždy přičtou 1)

* Číslo sekvence se náhodně generuje, aby se nemohl připléci jiný packet (opožděný)

![tcp](https://mamut.spseol.cz/nozka/psk/156-tcp_udp/Tcp-handshake.png)

* jak se handshake povede strany jsou navázané do konce procesu (může se zneužít na útoky)


**Ukončení spojení**

![ackfin](https://mamut.spseol.cz/nozka/psk/156-tcp_udp/Tcp-termination.png)

## User Datagram Protocol

* přenost dat bez záruk
* ztráty řeší snížením kvality /opakovani dotazu
* nezaručuje doručení

* **UDP pouze přidává kontrolní součty a schopnost roztřiďovat mezi více aplikací na stejném počítači**

![udp](https://i.gyazo.com/454f61d6a045fb4fcea3a4907fcab53b.png)

* vhodný pro DNS, LAN, protože je jednoduchý
* počítá se se ztrátou


