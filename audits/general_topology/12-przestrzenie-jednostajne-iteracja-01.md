# Topologia ogólna — rozdział 12: audyt iteracja 01

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Źródło: `chapters/pl/general_topology/12-przestrzenie-jednostajne.tex`.

## Wyniki

| Warstwa | Status |
| --- | --- |
| Poprawność definicji i aksjomatów relacji | sprawdzono |
| Lematy o symetrycznych otoczeniach | sprawdzono |
| Konstrukcja topologii i kryterium Hausdorffa | sprawdzono |
| Struktury pseudometryczne | sprawdzono |
| Podprzestrzenie i produkty | sprawdzono |
| Ciągłość jednostajna i Heine--Cantor | sprawdzono |
| Sieci, ciągi i filtry Cauchy'ego | sprawdzono |
| Skończone modele struktur od relacji równoważności | **PASS: 24 modele, rozmiary 0--4** (nie dowodzi przypadków nieskończonych) |
| Środowiska LaTeX i własne etykiety | **PASS: 33 etykiety po dodaniu rysunku, bez duplikatów** |
| Zależności między rozdziałami | **PASS: 451 etykiet, 119 odsyłaczy po dodaniu rysunku, brak brakujących celów** |
| Terminologia: uzwarcenie i zbieżność jednostajna na zbiorach zwartych | **PASS** w rozdziałach 01--12 |
| Samodzielny punkt wejścia i katalog | utworzone i zaktualizowane |
| Rysunek pasma wokół przekątnej | dodany; oględziny gotowego PDF **wymagane** |
| Uruchomienie testów Pythona w rzeczywistym CI | **niepotwierdzone** |
| Kompilacja PDF samodzielna i całej książki | **niepotwierdzone** |
| Stabilność rozdziału | **OTWARTA** |

## Kontrola kluczowych kroków

1. **Struktura jednostajna.** W lemacie o symetrycznym otoczeniu
   trzeba przeciąć relację z jej odwrotnością, aby zapewnić
   $F=F^{-1}$, oraz stosować monotoniczność składania relacji.
   Obie czynności zostały ujęte w dowodzie.
2. **Topologia indukowana.** Przekroje $E[x]$ nie muszą być otwarte.
   Tekst dowodzi, że zawierają pewne otwarte otoczenie $x$,
   korzystając z warunku $F\circ F\subseteq D$.
   Nie ma nieuprawnionego utożsamienia baz otoczeń z bazą otwartą.
3. **Hausdorff.** Rozłączność przekrojów $F[x]$ i $F[y]$
   wynika z symetrii i $F\circ F\subseteq E$.
   Aby dostać rozłączne *otwarte* otoczenia, wykorzystano poprzednie
   twierdzenie o topologii indukowanej.
4. **Pseudometryki.** Równość dwóch topologii następuje z
   porównania baz otoczeń, a rozdzielanie punktów jest równoważne
   dodatniej określoności pseudometryki.
5. **Produkty.** Weryfikacja zgodności topologii obejmuje obie
   inkluzje baz otoczeń, a warunek Cauchy'ego w produkcie wykorzystuje
   skończoność liczby kontrolowanych współrzędnych.
6. **Heine--Cantor.** Dowód sekwencyjny jawnie korzysta ze zwartości
   ciągowej zwartej przestrzeni metrycznej (rozdział 07).
7. **Filtr ogonów.** Skierowanie indeksów zapewnia bazowość ogonów;
   oba kierunki równoważności sieci i filtra Cauchy'ego są rozpisane.
8. **Kontrprzykłady.** Metryki $d$ i $e$ indukują tę samą topologię,
   lecz różne struktury jednostajne. Ciąg $(n)$ jest Cauchy'ego
   względem $e$, ale nie względem $d$.

## Kolejny krok

Uruchomić `python tools/tests/test_general_topology_ch12.py` oraz
`bash tools/validate_general_topology_ch12.sh` na rzeczywistym
checkout gałęzi; obejrzeć rysunek i strony PDF. Dopiero po
potwierdzeniu tych wyników zamknąć audyt. W obecnej iteracji
nie przypisujemy statusu PASS kompilacji ani CI bez dowodu ich wykonania.
