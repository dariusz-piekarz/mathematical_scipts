# Logika matematyczna i teoria mnogości — rozdział 25, audyt I

**Data:** 22 listopada 2026 r.  
**Rozdział:** `chapters/pl/logic_and_set_theory/25-aksjomaty-zf-zfc-i-konstrukcje-zbiorowe.tex`

## Integracja i kontrola zachowania treści
Źródłem był plik `25-zf-zfc-axioms-and-set-constructions.tex` z Biblioteki oraz pełniejsza wersja rozdziału 25 w skrypcie `logika_teoria_mnogosci_iteracja_79.pdf` (strony 187–198). Pierwszy plik kończył się na twierdzeniu Cantora; w nowej wersji przywrócono obszerny materiał o budowie arytmetyki w ZF: definicję liczb von Neumanna, strukturę następnika, aksjomaty Peana, diagram pierwszych liczb, rekursję na `ω`, dodawanie, mnożenie, potęgowanie, porządek, indukcję silną i dzielenie z resztą. Nie zastąpiono pełniejszego tekstu skróconą wersją.

## Audyt matematyczny
1. **Język i aksjomaty ZF:** sprawdzono osobno warunki i kwantyfikatory ekstensjonalności, pustego zbioru, pary, sumy, potęgi, separacji, zastępowania, nieskończoności i ufundowania. Nie użyto nieograniczonego schematu pojmowania zbiorów.
2. **Istnienie konstrukcji:** uzasadniono iloczyn kartezjański przez separację w `P(P(A∪B))`, istnienie `ω` przez minimalność przecięcia rodziny indukcyjnych podzbiorów danego zbioru, a twierdzenie Cantora przez dokładnie określony zbiór diagonalny.
3. **Liczby naturalne:** indukcyjnie wywiedziono przechodniość, brak samoprzynależności, iniekcyjność następnika i opis elementów `ω`; z tych rezultatów uzyskano aksjomaty Peana.
4. **Rekursja:** konstrukcja skończonych przybliżeń `f_n` korzysta z separacji, a jednoznacznie określony wykres `F` z zastępowania. Dla jednoznaczności użyto zasady indukcji, nie aksjomatu wyboru.
5. **Działania:** podstawowe tożsamości oraz łączność, przemienność i rozdzielność wyprowadzono w poprawnej kolejności, bez założeń kołowych. Zdefiniowano potęgowanie i prawo wykładników.
6. **Porządek i dzielenie:** najpierw wykazano zgodność porządku arytmetycznego z `∈` na liczbach von Neumanna, następnie dobry porządek `ω`, indukcję silną, monotoniczność działań i twierdzenie o dzieleniu z resztą. W dowodzie jednoznaczności podano obie nierówności prowadzące do sprzeczności.
7. **Odsyłacze:** nieaktualne odesłanie do paradoksu Skolema (`thm:ls-skolem-paradox`) poprawiono na istniejącą etykietę rozdziału 24 (`thm:skolem-paradox`).
8. **Skład:** dodano skrócony nagłówek bieżący `\chaptermark` bez zmiany pełnego tytułu oraz figurę następników von Neumanna.

## Inwentarz i walidacja
16 definicji, 14 przykładów, 6 lematów, 11 twierdzeń, 2 wnioski, 5 uwag, 19 dowodów oraz 1 rysunek. 46 etykiet i 23 odsyłacze. Nowe testy `tools/tests/test_logic_and_set_theory_ch25.py`: PASS. GitHub Actions `45003169518`: SUCCESS. Cały PDF ma 202 strony, rozdział 25 zajmuje 10 stron; wszystkie jego strony wyrenderowano i przejrzano pod kątem czytelności. Log LaTeX: brak przepełnień i nierozwiązanych odsyłaczy.

**Werdykt:** audyt I zakończony, integracja pełnego materiału zakończona; możliwy drugi audyt stabilizacyjny bez rozszerzania zakresu.
