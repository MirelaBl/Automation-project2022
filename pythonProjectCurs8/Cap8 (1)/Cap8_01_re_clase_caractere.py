"""
801 Module
Modulul re - clase de caractere utilizate
PF - 27.06.2021 v6
"""  #


# Documentatie     https://docs.python.org/3.9/library/re.html

# Clase de caractere utilizate in REGEX
"""
- ^   de la inceputul liniei (sinonim \A),
- $   sfarsitul liniei (sinonim \Z)
- .   inlocuieste orice caracter
- \d  orice caracter decimal
- \D  orice caracter nondecimal (opusul \d)
- \w  orice caracter alfanumeric
- \W  orice caracter nonalfanumeric
- *   repeta de zero sau mai multe ori expresia de dinainte de semn
- *?  repeta un caracter de 0 sau 1 data (non-greedy - pana la prima aparitie a car de sfarsit)
- \s  spatiu
- \S  fara spatii
- ?  repeta un caracter O DATA sau de mai multe ori (non-greedy - pana la prima aparitie a car de sfarsit)
- +  o data sau de mai multe ori expresia dinainte de semn

- [aeiou]     un singur caracter din lista
- [^xyz]      un singur caracter cu exceptia celor mentionate
- [0-9a-f]     oricare cifre din interval una cate una (cu + scoate si grupuri)
- [a-zA-Z]       oricare litere din interval una cate una (cu + scoate si grupuri
- (   unde incepe expresia
- )   unde se termina expresia
- {n}         exact n aparitii ale expresiei de dinainte, cu {n} n sau mai multe
- {n,m}       intre n si m aparitii
- |           desparte mai multe secvente de cautare in aceeasi expresie
"""
