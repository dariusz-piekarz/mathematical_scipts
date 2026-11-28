# Algebra abstrakcyjna — AA-37, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026  
**Rozdział:** Algebraiczna niezależność i bazy transcendencji  
**Wynik audytu:** **STABILNY** — nie wprowadzono żadnej poprawki do źródła po audycie I.  
**Źródło:** `AA-37-audyt-II-zrodlo.tex`, SHA-256 `6680a4aa75680566cbdf58630cb77634e95f423de03d7232b73121ff00decb60`.

## Zakres niezależnego przeglądu matematycznego

1. **Baza a maksymalność niezależności:** sprawdzono usuwanie mianowników i niezerowość otrzymanej relacji wielomianowej; argument działa również dla pustej bazy.
2. **Istnienie:** sprawdzono skończony charakter relacji algebraicznych, domknięcie rodziny niezależnej przy sumie łańcucha i poprawne zastosowanie lematu Zorna, z jawnym uwzględnieniem aksjomatu wyboru.
3. **Wymiana algebraiczna:** sprawdzono niezerowość wielomianu `Q(U,x)` z transcendentalności `x` nad odpowiednim ciałem; poprawne jest przejście od algebraiczności nad `F(b)` do algebraiczności `b` nad `F(x)`.
4. **Nierozkładalność po dołączeniu nowego parametru:** poprawnie stosowany jest lemat Gaussa i równość stopni wielomianu względem parametru transcendentalnego; nie jest wymagane założenie o charakterystyce.
5. **Zmienna istotna:** sprawdzono równość przecięcia ciał funkcji wymiernych, wykorzystując algebraiczną niezależność `d` od pozostałych zmiennych. Istnieje skończony nośnik dowolnej funkcji wymiernej.
6. **Równość mocy baz:** zbadano podstawianie elementów przy zachowaniu poprzednio wybranych parametrów oraz przejście do nieskończonych mocy przez skończone nośniki, przechodniość algebraiczności i arytmetykę kardynalną z aksjomatem wyboru.
7. **Wieże rozszerzeń:** potwierdzono niezależność `U ∪ V` i algebraiczność `L/K(U ∪ V)` także dla nieskończonych baz.
8. **Przykłady:** zweryfikowano `K(u,v)/K(u+v,uv)`, wymianę `u → u+v²`, przeliczalnie nieskończone bazy, równanie `T^p-t^p` i stopień czysto nierozdzielczego rozszerzenia `K(t)/K(t^p)`.

Nie stwierdzono nowych luk wymagających zmiany dowodu, definicji ani przykładu.

## Testy niezależne i regresyjne

- **79/79 PASS:** ponownie uruchomiono zestaw z audytu I, obecnie dostosowany do modułowego układu repozytorium: `tools/tests/test_abstract_algebra_ch37.py`.
- **101/101 PASS:** nowy zestaw `tools/tests/test_abstract_algebra_ch37_independent.py`, w tym niezależność elementarnych funkcji symetrycznych w charakterystykach 2, 3, 5, 7; odwracalne podstawienia wielomianowe w różnych wymiarach; kontrola klas reszt wykładników modulo `p`; przykłady rozszerzeń algebraicznych, zmian baz i funkcji wymiernych; kontrola struktury LaTeX.
- **180/180 PASS** razem; uruchomienie w strukturze `tools/tests` z katalogiem `chapters/pl/abstract_algebra`.
- Jedno początkowe niepowodzenie nowego zestawu wynikało z błędnego porównywania dwóch równoważnych zapisów ułamka wymiernego. Naprawiono asercję testową bez zmieniania źródła AA-37.
- Testy obliczeniowe **nie** zastępują matematycznych dowodów twierdzeń dla nieskończonych zbiorów i wyników zależnych od aksjomatu wyboru.

## LaTeX, odsyłacze i publikacja

- Źródło w audycie II jest **identyczne bajtowo** ze źródłem po audycie I.
- **15/15 etykiet unikatowych**, wszystkie siedem środowisk `proof` i siedem przykładów zachowano.
- Jedyny zewnętrzny odsyłacz `aa:tw:fundamental-symmetric` sprawdzono w już opublikowanym AA-31.
- Samodzielny montaż kompilacyjny: **5 stron A4**, bez ostrzeżeń LaTeX i przepełnień. Kontrola wszystkich pięciu wyrenderowanych stron: brak widocznych kolizji i uciętych wzorów.
- Opublikowano rozdział, dwa zestawy testów i zaktualizowano `books/pl/abstract_algebra.tex`, `catalog/books.json` (AA-01–AA-37) i `.github/workflows/abstract-algebra-chapter.yml`.
- Zdalny workflow CI AA-01–AA-37: **uruchomiony; wynik pełnego przebiegu należy sprawdzić oddzielnie** (nie należy wnioskować o sukcesie ze skonfigurowania workflow).

## Decyzja

**AA-37 STABILNY po audycie II.** Następnym rozdziałem do audytu I jest **AA-38 — lemat normalizacyjny Noether**.
