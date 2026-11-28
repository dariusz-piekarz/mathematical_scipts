# Algebra liniowa — rozdział 05: audyt stabilizacyjny II (korekta precyzji)

**Data:** 22 listopada 2026. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Plik:** \`chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex\`.
**SHA przed zmianą:** \`f94bdf0b4a35730e858c50cb7fb7288b117facf6\`.
**SHA po zmianie:** \`c238cb3232b69fb19d0dfe1062af05a2a0d8ddb8\`.

## Wykryta niedokładność i rzeczywista korekta

W dowodzie kryterium zgodności (Twierdzenie \`thm:lin5-zgodnosc\`) poprzedni ostatni fragment brzmiał:
> Warstwa nie jest na ogół podprzestrzenią, jeżeli \(b\ne0_{K^m}\).

Sformułowanie „na ogół” było niepotrzebnie słabe. Dla **każdego** zgodnego układu liniowego \(Ax=b\) przy \(b\ne0_{K^m}\) zbiór rozwiązań \(x_0+\ker A\) nie jest podprzestrzenią \(K^n\): nie zawiera wektora zerowego, bo \(A0_{K^n}=0_{K^m}\ne b\). Nowy tekst wypowiada ten ścisły wniosek i uzasadnia go wprost. Nie zmieniono tezy twierdzenia, jego pozostałych założeń, żadnego indeksu ani odsyłacza.

## Niezależna kontrola pozostałych kluczowych fragmentów

1. Wierszowa równoważność zachowuje **jądro**, ale obraz przenosi przez izomorfizm \(P\); jest to poprawnie odróżnione od niezmienniczości samego obrazu.
2. W algorytmie Gaussa element wiodący jest wybierany tylko spośród niezerowych skalarów; przenoszenie pivotu, normalizacja i zerowanie zachowują wcześniej osiągniętą strukturę. Przy \(m=0\) lub \(n=0\) wynik jest zredukowany bez operacji.
3. W dowodzie \(r=\operatorname{rk}A\) liczba niewiodących kolumn \(n-r\) jest liczbą niezależnych parametrów jądra. Projekcja na te współrzędne ma poprawnie wykazane: liniowość, istnienie i jednoznaczność.
4. W twierdzeniach o bazach jądra i obrazu sprawdzono, że współczynniki \(-R_{if}\) rzeczywiście spełniają równania \(Rx=0\); wybrane bazowe kolumny **oryginalnej** macierzy \(A\) powstają z pivotowych kolumn \(R\) pod działaniem \(P^{-1}\).
5. RREF: niezmiennikiem jest przestrzeń wierszy \(H\), nie przestrzeń kolumn macierzy. Wyznacza ona pozycje pivotów oraz wszystkie współrzędne każdego zredukowanego wiersza, również przy rzędzie zero. Rachunki w przykładowych układach i odwracaniu macierzy \((2\ 1;1\ 1)\) są zgodne z rozdziałem LA-04.

## Kontrole i decyzja

- Testy dokładne \`tools/test_linear_algebra_ch05.py\` na wszystkich **1553** macierzach i **12558** parach \((A,b)\) przeszły lokalnie oraz jako krok CI [45006576953](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006576953); pełne CI dla poprawionej wersji źródła należy zweryfikować osobno.
- Wersja źródła po korekcie ma ten sam zestaw 27 etykiet rozdziału 05, 16 odsyłaczy do prawidłowych celów, 10 pełnych dowodów i cztery przykłady; wprowadzone zdanie nie zmienia składni i wymaga ponownego PDF/CI wyłącznie ze względu na możliwe łamanie wierszy.
- **Audyt II wykrył i naprawił jedno doprecyzowanie. Nie zalicza się jako czysty przebieg.** Do stabilizacji potrzeba dwóch kolejnych czystych audytów na blobie \`c238cb3...\`, końcowego CI oraz wizualnego sprawdzenia renderingu po poprawce.
