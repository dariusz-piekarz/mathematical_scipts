# AA-52 — audyt II: modele kwaternionowe i klasyfikacja sprzężenia

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## CI pierwszej wersji
Run 45299991730, job 138129815668, head 2debce4b6d260b4ac42ce4db259651dbeb81dfb5: 114/114 kroków success. Log potwierdza 4576 testów repozytorium (106,119 s), dedykowane AA-52 4/4 + 3/3 PASS, 52 rozdziały, 1070 etykiet, 593 odsyłacze, zero brakujących celów i duplikatów. Kompilacja i kontrola typograficzna success. To CI dotyczy źródła przed audytem II.

## Audyt
Przejrzano argumenty klasyfikacji sprzężenia: iniektywność reprezentacji zachowuje rzędy elementów; w A5 dwa rodzaje śladów cykli długości pięć uzgadnia automorfizm przez nieparzystą permutację; zespolone przeplatanie daje rzeczywiste odwracalne przez wielomian wyznacznika, a rozkład polarny daje ortogonalne, z korektą orientacji w wymiarze trzy. Dodano dokładny odsyłacz do aa:tw:characters-basis oraz wyjaśnienie krotności składników. Uzupełniono usuwanie ujemnych potęg w prezentacji Dic_n, tabelę o kolumnę rzędu 10, nieprzemienność grup wyjątkowych i sformułowanie rozłączności typów.

Dołączono samodzielne utożsamienie kwaternionów jednostkowych z SU(2), wzór macierzy sprzężenia na przestrzeni czysto urojonej oraz dowody, że generatory użyte w niezależnej regresji dają pełne przeciwobrazy grup obrotów. W przypadku 2I przechodniość na 12 wierzchołkach i obrót rzędu 5 dają co najmniej 60 obrotów, a zawieranie w grupie dwudziestościanu daje dokładnie 60. Jądro zawiera -1, więc przeciwobraz ma 120 elementów. Uwzględniono zmianę ortonormalnej bazy przy identyfikacji z nakryciem AA-51.

## Rzeczywiste obliczenia lokalne
W Python/SymPy sprawdzono relacje macierzy A=diag(i,-i), J=[[0,1],[-1,0]], K=AJ: kwadraty -I i antykomutowanie A,J. Dla u=(phi/2,0,(phi-1)/2,1/2), phi=(1+sqrt(5))/2, sprawdzono dokładnie det M(u)=1 i M(u)* M(u)=I. Wzór macierzy obrotu daje R=(1/2)[[phi-1,-phi,1],[phi,1,phi-1],[-1,phi-1,phi]]. Sprawdzono Rv=v i wszystkie pięć tożsamości Rw_i=w_(i+1 mod 5) dla wektorów AA-51. Proces zakończył się kodem 0. To niezależne sprawdzenie konkretnej konstrukcji, nie zastępstwo CI.

## Stan
Commit 528d401474de0d29bf621d006ab713939c7b032a, ponowny odczyt potwierdził blob 9d9dd7bef518f5791bdf7b565daa11e0dc42d65f. Nowy run przy pierwszym odczycie nie był jeszcze widoczny. AA-52 W AUDYCIE; potrzebne CI po zmianach i kontrola PDF, AA-53 nieotwarty. Historyczne rozdziały bez zmian.
