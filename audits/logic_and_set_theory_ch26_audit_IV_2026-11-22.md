# Logika matematyczna i teoria mnogości — rozdział 26, audyt IV

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex`

## Ostatnie poprawki uzasadnień

1. **Porządek na $H(A)$.** Poprzedni dowód powoływał się na lemat porównania dobrych porządków w celu stwierdzenia, że relacja na typach porządkowych jest ścisłym porządkiem liniowym. Z lematu wynika rozłączność i porównywalność przypadków; **przechodniość** wymaga jeszcze złożenia izomorfizmu odcinka początkowego $U$ w $V$ z izomorfizmem $V$ na odcinek początkowy $W$. Dodano ten krok i wyjaśniono, że obraz pozostaje właściwym odcinkiem początkowym.
2. **Konstrukcja łańcucha maksymalnego.** Przy przejściu od górnego ograniczenia $u$ łańcucha $C$ do sprzeczności z jego maksymalnością dodano jawny argument, że każdy $v>u$ musi leżeć poza $C$ (inaczej z definicji ograniczenia górnego wynikałoby $v\le u$). Analogiczne uzasadnienie dodano w dowodzie implikacji Hausdorff $\Rightarrow$ Zorn.
3. Zmiany nie wprowadzają nowych twierdzeń, definicji ani przykładów. Utrzymano inwentarz 5 definicji, 10 przykładów, 1 lematu, 8 twierdzeń, 1 wniosku, 2 uwag, 10 dowodów; 20 etykiet i 18 odsyłaczy.
4. Dodano odrębne asercje regresyjne, które chronią oba uzasadnienia. Wstępne uruchomienie testów rozdziału 26 w CI: **PASS** (run `45005482287`), pełna kompilacja na etapie przygotowania raportu w toku.

## Ponowny przegląd matematyczny

Przeanalizowano kolejność zależności:
- **ZF:** porównywanie dobrych porządków, zbiór typów Hartogsa, wybór z rodziny skończonej;
- **AC $\Rightarrow$ Zermelo:** jedna funkcja wyboru na niepustych podzbiorach $A$ i twierdzenie Hartogsa;
- **Zermelo $\Rightarrow$ Zorn:** przegląd elementów w dobrym porządku i budowa maksymalnego łańcucha;
- **Zorn $\Rightarrow$ AC:** funkcje częściowe uporządkowane przez przedłużanie;
- **Zorn $\Leftrightarrow$ Hausdorff:** dwa dowody przez ograniczenia górne i maksymalność;
- **AC $\Leftrightarrow$ przekroje surjekcji $\Leftrightarrow$ transwersale:** wybór z włókien i indeksowana suma rozłączna;
- **Zorn $\Rightarrow$ baza:** maksymalny liniowo niezależny podzbiór i jego powłoka liniowa.

W żadnym miejscu dowodzącym Hartogsa w ZF nie zakłada się globalnego dobrego uporządkowania ani AC.

**Werdykt:** audyt IV wykrył dwie brakujące eksplikacje w argumentach i usunął je; kolejna iteracja ma być czystym audytem stabilizacyjnym po pełnym CI, logu i kontroli wizualnej PDF.
