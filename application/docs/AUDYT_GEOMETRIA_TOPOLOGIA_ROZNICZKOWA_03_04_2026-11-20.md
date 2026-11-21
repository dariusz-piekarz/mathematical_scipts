# Audyt DG-03–04 — Geometria i topologia różniczkowa
Data: 2026-11-20  
Gałąź: `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`)  
Repozytorium: `dariusz-piekarz/mathematical_scipts`

## Zakres

Audyt obejmuje dwa kolejne pliki kanoniczne:
- `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` — algebra tensorowa i zewnętrzna;
- `chapters/pl/differential_geometry_and_topology/04-grassmanniany-algebra-clifforda-i-spinory.tex` — grassmanniany, algebra Clifforda i spinory.

Weryfikowano precyzję definicji, założenia twierdzeń i rolę kwantyfikatorów, kluczowe kroki dowodów, normalizacje algebraiczne i znaki, motywację, rozwiązane przykłady, spójność terminologii, etykiety, odsyłacze, rysunki jako źródła TikZ i brak zewnętrznych plików zależnych. Punktem odniesienia jest szczegółowość pierwszego rozdziału geometrii różniczkowej; nie zastępowano istniejących dowodów krótkimi deklaracjami.

## DG-03 — ustalenia matematyczne

Przejrzano konstrukcję i jednoznaczność iloczynu tensorowego (własność uniwersalna), wyprowadzenie bazy i wymiaru, izomorfizm `V ⊗ W* ≅ Hom(W,V)`, kontrakcję i ślad, algebry symetryczną i zewnętrzną, relację między ilorazem tensorowym a antysymetryzatorem, potęgi zewnętrzne odwzorowań, wyznacznik, minory, wzór Cauchy'ego–Bineta, dualne formy alternujące oraz cofnięcie i pochodną Liego tensorów.

Wykryta potrzeba uzupełnienia: używane są dwie zgodne, lecz łatwe do pomylenia normalizacje: reprezentant `j_k` i formy `E_k=k! j_k`. Stary tekst wyjaśniał mechanizm, ale nie dawał w tym miejscu liczbowego testu współczynnika. Dodano **`prz:normalizacja-wedge-form`**: dla `α=e¹∧e²`, `β=e³` prześledzono dokładnie dwie nieznikające permutacje, wynik `(α∧β)(e₁,e₂,e₃)=1`, normalizację `Alt₃(α⊗β)=1/3` i błędną wartość `2` po pominięciu dzielnika `2!1!`. Zachowano pierwotne odsyłacze i wszystkie wcześniejsze przykłady.

Dwa odsyłacze w DG-03 prowadzą **do rozdziału 05**, a nie do rozdziałów 01–04: `thm:modul-izomorfizm` i `ch:algebra-abstrakcyjna`. Oba cele istnieją w kanonicznym rozdziale 05; nie są błędami.

## DG-04 — ustalenia matematyczne

Przejrzano atlasy wykresowe grassmannianu i ich topologię, opis przestrzeni stycznej i wiązki tautologicznej, orientację, odwzorowanie Plückera i jego relację dla `Gr₂(R⁴)`, odwzorowanie Gaussa, konstrukcję algebry Clifforda i dowód bazy, odbicia, pokrycia `Pin/Spin`, reprezentacje zespolone i półspinory, model Pauliego, klasyfikację struktur spinowych torusa i kryterium podnoszenia wiązki.

Wykryta luka dotycząca **samodzielności wykładu**: klasa `w₂(E)∈H²(M;Z/2)` pojawiała się przed definicją używanej w tym miejscu kohomologii Čech. Dodano:
1. konstrukcję grupy kołańcuchów `C^q(𝒰;Z/2)` na dobrym pokryciu i dokładny wzór kobrzegu;
2. sprawdzenie `δ²=0` przez dwukrotne wystąpienie każdej pary usuniętych indeksów;
3. definicję `H²(𝒰;Z/2)=ker δ₂ / im δ₁` oraz weryfikację, że `ε_{ijk}` jest dwukocyklem i zmiana podniesień daje kobrzeg;
4. jawne kryterium `E` spinowa `⇔ w₂(E)=0` dla zorientowanej wiązki euklidesowej rzędu co najmniej 2.

Oddzielono dowiedzioną bezpośrednio część kryterium od standardowego twierdzenia utożsamiającego kohomologię Čech dobrego pokrycia z kohomologią przestrzeni. Nie usuwano uprzedniego dowodu przez funkcje przejścia.

## Kontrola strukturalna i regresje

Po zapisaniu zmian ponownie odczytano pliki z gałęzi:
- DG-03: **87** etykiet, **90** użyć odsyłaczy, **8** otoczeń `figure`;
- DG-04: **61** etykiet, **60** użyć odsyłaczy, **6** otoczeń `figure`;
- łącznie w rozdziałach 01–05: **318** etykiet, **0** powieleń;
- **0** nierozwiązanych odsyłaczy w rozdziałach 03–04 po uwzględnieniu rozdziałów 01–05;
- liczby `\begin{…}` i `\end{…}` w audytowanych plikach są zgodne dla wszystkich występujących otoczeń;
- **0** wywołań zewnętrznych `\input`, `\include` i `\includegraphics` w DG-03 i DG-04;
- nie znaleziono zakazanych form terminologicznych z rodziny „tensorowanie”, „sekwencyjny”, „seskwiliniowy” i „zbieżność zdominowana” w tych dwóch plikach.

Dodano `application/tests/test_differential_geometry_ch03_04.py` z kontrolą włączeń książki, etykiet, odsyłaczy, otoczeń i braku plików zewnętrznych, a także dwoma testami matematycznymi. Niezależnie obliczono normalizację iloczynu zewnętrznego oraz sprawdzono **64/64** konfiguracji 1-kołańcuchów na czterech wierzchołkach: `δ²=0`.

## Ograniczenia potwierdzenia

W tej iteracji **nie przeprowadzono pełnej kompilacji LaTeX całej książki**, dwukrotnego przebiegu odsyłaczy ani wizualnej inspekcji wyrenderowanych stron PDF. Sprawdzenie obecności rysunków TikZ i bilansu otoczeń **nie jest** równoznaczne z wizualnym audytem ich rozmieszczenia i podpisów. Nie należy raportować tych kontroli jako zaliczonych. Dodane testy regresyjne są zapisane w repozytorium; pełny wynik ich uruchomienia w środowisku projektu wymaga CI lub lokalnego uruchomienia.

## Kontynuacja

Następna para chronologiczna w aktualnym tomie: **DG-05–06** — podstawy algebry abstrakcyjnej i algebra homologiczna. Przed edycją zweryfikować także nakładanie się z analogicznymi kanonicznymi modułami topologii algebraicznej; zachować etykiety i nie scalać treści bez porównania dowodów oraz przykładów.
