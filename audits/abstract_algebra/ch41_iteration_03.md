# AA-41 — audyt III (niezależny audyt potwierdzający)

**Data:** 2026-11-22  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/abstract_algebra/41-reprezentacje-grup-i-twierdzenie-maschkego.tex`  
**Blob źródła:** `05d87a9b95117069879b58e5c6ea40d71ad4a29c` (bez zmian względem audytu II).

## Zakres niezależnej weryfikacji matematycznej

1. **Definicje reprezentacji.** Sprawdzono, że `\rho(g)W\subseteq W` wraz z niezmienniczością wobec `g^{-1}` daje `\rho(g)W=W`; zastosowanie w dowodzie uśredniania projekcji jest poprawne.
2. **Reprezentacja permutacyjna `S_3` nad `\mathbb Q`.** Podane wektory `a=e_1-e_2`, `b=e_2-e_3` stanowią bazę płaszczyzny o sumie współrzędnych równej 0; macierz trójcyklu i wielomian `T^2+T+1` są poprawne. Brak wymiernych pierwiastków wyklucza właściwe niezerowe podreprezentacje dwuwymiarowe.
3. **Maschke.** Uśredniona projekcja ma obraz równy `W`, ograniczenie do `W` jest identycznością, operator jest idempotentny i komutuje z działaniem grupy; jądro jest niezmienniczym dopełnieniem. Indukcja po wymiarze jest poprawna, w tym przypadek zerowy.
4. **Ostrość warunku.** Kierunek `3 => 2` jest poprawny: obrazy prostych składników w ilorazie są zerowe albo proste; maksymalna rodzina obrazów o sumie prostej daje równoważny ilorazowi podmoduł. W kontrapozycji dla `3 => 1` niezerowy niezmienniczy wektor `u=\sum_g[g]` w module regularnym nie może być obrazem żadnego `G`-równoważnego rzutu na `Ku` przy `|G|\cdot1_K=0`. Nie ma błędnego wniosku wyprowadzanego z samego istnienia nilpotentów w pierścieniu nieprzemiennym.
5. **Dodatnia charakterystyka.** `C_3` nad `\mathbb F_2` spełnia założenia Maschkego; generator w dwuwymiarowym składniku ma wielomian charakterystyczny `T^2+T+1` bez pierwiastków, więc składnik jest nieprzywiedlny. Przeciwnie, dla `C_2` nad `\mathbb F_2` dopełnienie linii stałej nie istnieje.
6. **Operator Reynoldsa.** Dowód działa także w przestrzeni nieskończenie wymiarowej (uśredniane jest skończenie wiele operatorów). Równości `\operatorname{im} R_G=V^G`, `R_G^2=R_G`, `R_G\rho(h)=R_G` są poprawne.
7. **Dokładność niezmienników.** Dla ciągu krótkiego surjektywność ograniczenia na wektory niezmiennicze wynika z uśrednienia dowolnego podniesienia; w złej charakterystyce augmentacja `\varepsilon:K[G]\to K` jest poprawnym kontrprzykładem.

## Nowa kontrola arytmetyczna

Wykonano **1673 niezależne sprawdzenia tożsamości** w osobnej implementacji JavaScript (nie uruchamiano ponownie modułów `unittest`). Obejmowały:
- uśrednianie w reprezentacjach permutacyjnych `C_n` dla `2\le n\le7` i `p\in\{2,3,5,7,11\}`, z wykluczeniem `p\mid n`, oraz rozkład wektora na część stałą i jądro;
- sprawdzenie rzędu generatora i braku niezmienniczej prostej dla dwuwymiarowego modułu `C_3` nad `\mathbb F_2`;
- zanikanie augmentacji na wektorach stałych przy `p\mid n`;
- rozkład przez `(I\pm T)/2` dla inwolucji w charakterystykach 3, 5, 7, 11.

Wszystkie powyższe 1673 kontrole zakończono bez błędów.

## Integracja, zależności i skład

- **19 unikatowych etykiet** i **10 wystąpień lokalnych odsyłaczy**; wszystkie cele lokalne istnieją.
- Sprawdzono domknięcie i właściwe zagnieżdżenie środowisk `begin/end` (37 kroków kontrolnych łącznie z kontrolami struktury i integracji).
- Rozdział jest obecny zarówno w `books/pl/abstract_algebra.tex`, jak i jako 41. pozycja w `catalog/books.json`.
- Definicję `K[G]` zestawiono z ogólniejszą konstrukcją `R[G]` w AA-15: rozdział AA-41 wykorzystuje jej szczególny przypadek, a nie sprzeczne założenia.
- Źródło AA-41 pozostawiono bez zmian; nie wykonano w tym audycie nowej lokalnej kompilacji `latexmk` ani osobnej kontroli renderów PDF.

## Stan pełnego CI

Zdalny przebieg workflow **Abstract algebra AA-01 to AA-41 validation**:  
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068795118  
**GitHub Actions: completed / success** na commicie `d00aacc5a8d45afdd0ac150ae96e2adbff5b49dd`.

Porównano commit przebiegu z późniejszym HEAD `17c5052f071047e3174d75b802b2ce08cbbdb2f1`: w zakresie ścieżek AA jedyną zmianą było dodanie raportu audytu II; kod źródłowy AA-41 oraz workflow walidacyjny nie zmieniły się. Blob źródła na commicie CI był zgodny z badanym blobem.

**Werdykt:** AA-41 stabilny po audytach II i III oraz pozytywnym zdalnym CI. Brak nowych zmian w pliku TeX. Następny rozdział AA-42 nie występuje jeszcze w wykazie `chapters/pl/abstract_algebra/`; nie należy deklarować jego audytu bez źródła.
