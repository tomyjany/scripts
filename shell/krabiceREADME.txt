Při tvorbě vánoční krabice, jsem postupoval následovně:
rozhodl jsem se krabici tisknout pomocí while loopů, protože se mi s němi pracuje více intuitivně, než s for loopy. 
Proto použivám promenou "i" pro radky a promennou "j" pro sloupce. (podle zadani radky = vyska, sloupce = sirka)

Cyklus pro i projede od 0 do poctu radku-1
V cyklu pro i, je cyklus pro j=0 do pocet sloupcu-1

v cyklu pro j, se provadi samotny tisk, kde promenne tisk vždy přiřadím požadovaný tisknutý znak.

Tisknute znaky určuji pomocí následujících podmínek
-----------------------------------------------------------
pokud i = 0 nebo i = pocet radku-1 tak:
	pokud j = 0 nebo j = poctu sloupcu -1
		tisknu tecku {roh}
	
	jinak: tiskni "-" {horni nebo dolni stena}
jinak 
	
	pokud j = 0 nebo j = poctu sloupcu -1
		tiskni "|" {leva nebo prava stena}
	jinak
		pokud je ravdepodobnost je mensi nez i
			tiskni"O"
		jinak
			tiskni mezeru`
----------------------------------------------------------
promennou pravdepodobnosti si vygeneruji pomoci randomu
pravdepodobnost=$(($RANDOM % $1)) //Generuji od 0 do počtu řádků
Tato proměnná slouží k určení, zdali na dané pozici i,j bude kolečko nebo ne.
Proměnná je generována od 0 do počtu řádků, takže abychom dosáhli hustějšího tisku koleček ve spodní části, stačí nám, abychom vždy porovnali hodnotu "i"
s proměnnou pravdepodobnost a pokud bude pravdepodobnost mesni nez hodnota i, tak kolečko vytiskneme. 

Je to intuitvní, protože začínáme 1. radkem a pravděpodobnost, že se nám tam kolečko vytiskne je jedna/řádek (i bude 1 a pravdepodobnost musi být 0). 
Pokud budeme na konci, tak to bude řádek-1/řádek (nemusí to být úplně zaplněné).

tento ukol byl zabavny :)

poznamka: Tento úkol jsem psal na svém stroji (ne na perunu), takže kdyby Váš script tvdil, že jsem nezkoušel program zpouštět, tak to asi bude tím.
Kdyby byla potřeba, log mám uložený a jsem ochoten ho poskytnout.


