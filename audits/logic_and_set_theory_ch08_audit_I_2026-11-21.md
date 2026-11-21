# Audyt I — rozdział 08 „Obrazy, przeciwobrazy i działania na funkcjach”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** istniejący rozdział `08-images-preimages-and-composition.tex` w Bibliotece matematycznej, 680 wierszy, nawiązujący do audytu XLIV (20 listopada).  
**Zakres:** ponowny audyt istniejącego materiału i przeniesienie do kanonicznego katalogu skryptów; bez nowych twierdzeń, lematów, definicji ani przykładów.

## Kontrola matematyczna

Ponownie sprawdzono 20 twierdzeń i 20 dowodów, 6 definicji, 16 przykładów, 1 uwagę oraz 1 diagram TikZ. Szczególną uwagę zwrócono na:
- zachowywanie sum, przecięć i różnic przez obraz/przeciwobraz, kryteria iniekcyjności i dokładny warunek zachowywania ustalonego przecięcia przez włókna;
- indeksowane rodziny, w tym **pustą rodzinę przecięć**: `f[A]=B` jest wymagane do równości obrazów przy pustym indeksowaniu, podczas gdy iniekcja wystarcza dla niepustego indeksowania;
- adjunkcję `f[S]⊆T ↔ S⊆f⁻¹[T]`, nasycenie zbioru przez włókna, przypadki `S=∅`, `T=∅`;
- składanie i przeciwobrazy złożeń, zestawianie funkcji, ich iloczyn kartezjański i jego przypadki z pustą dziedziną lub przeciwdziedziną;
- sklejanie dwóch funkcji oraz dowolnej indeksowanej rodziny, w tym pustego zbioru indeksów, i brak ukrytego zastosowania aksjomatu wyboru;
- ograniczanie i przedłużanie funkcji w znaczeniu teoriomnogościowym;
- faktoryzację przez iloraz i bijekcję `A/∼_f → f[A]`, także dla `A=∅`.

**Wynik:** nie znaleziono fałszywego twierdzenia ani luki dowodowej wymagającej zmiany matematycznej.

## Korekty tekstu

1. W twierdzeniu `thm:image-preimage-adjunction` poprawiono nieprecyzyjne sformułowanie „pierwsza/druga równość”: poprzedzające je wzory są **zawieraniami**, których równość charakteryzuje odpowiednio iniekcję i surjekcję.
2. W twierdzeniu `thm:gluing-functions` wypisano jawnie `X,B,A_1,A_2,f_1,f_2`, dzięki czemu twierdzenie jest samodzielne, bez konieczności odgadywania zakresu obiektów z poprzedniej definicji.
3. W przykładzie reszt modulo `m` dodano brakujące założenie `m∈N` obok `m≥2`.
4. W kontrprzykładzie sklejania półosi podano pełne dziedziny i przeciwdziedziny obu funkcji.

Nie zmieniono żadnego wyniku ani jego etykiety. Zachowano **27 istniejących etykiet** rozdziału 08.

## Kontrola skończonych modeli

Nowa, niezależna enumeracja przeprowadzona podczas audytu:
- 60 funkcji `A→B` dla `0≤|A|,|B|≤3`;
- 2556 par podzbiorów oraz prawa obrazów, przeciwobrazów, adjunkcji i nasycenia;
- 22 356 indeksowanych rodzin podzbiorów długości `0–3`, z weryfikacją przecięć i niepustego/pustego indeksowania;
- 1678 zgodnych par funkcji dla składania i obrazów/przeciwobrazów złożeń;
- 121 iloczynów funkcji (czynniki o rozmiarze `0–2`);
- 729 par funkcji częściowych na zbiorze `{0,1,2}` z wartościami w `{0,1}`, sprawdzając kryterium sklejania;
- 60 przypadków ilorazu przez równość wartości.

**Liczba wykrytych kontrprzykładów: zero.** Testy na zbiorach skończonych nie zastępują dowodu w ogólnym ZF. Nowe przypadki ujęto w `tools/tests/test_logic_and_set_theory_ch08.py`.

## Struktura i rysunek

Sprawdzono bilans środowisk LaTeX (20 twierdzeń i 20 dowodów, 6 definicji, 16 przykładów, 1 uwaga, 1 rysunek), brak duplikacji etykiet i zachowanie odsyłaczy. Obraz diagramu `fig:preimage-image-xliv` skontrolowano na stronie PDF 81 pełnej książki iteracji 79; napisy nie nakładają się na diagram, a grafika nie jest obcięta.

Po włączeniu rozdziału 08 do katalogu i pliku głównego książka 01–08 powinna obejmować 250 unikatowych etykiet, 91 odsyłaczy i tylko trzy udokumentowane odsyłacze do jeszcze niezaimportowanych rozdziałów (09, 10 i 25): `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`. Kompilację PDF i kontrolę logów należy ocenić na wynikach dedykowanego GitHub Actions, a nie zakładać z góry sukcesu.

## Wniosek

Audyt I ujawnił jedynie nieścisłości formalno-redakcyjne. Rozdział 08 po imporcie **pozostaje otwarty do audytu II**, ponieważ zmieniono jego źródło. Nowej treści matematycznej nie wprowadzano.
