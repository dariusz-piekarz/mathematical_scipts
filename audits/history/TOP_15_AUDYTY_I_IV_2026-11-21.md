# Topologia algebraiczna — TOP-15, audyty I–IV

**Data:** 2026-11-21  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`; nie tworzono nowej gałęzi ani nie modyfikowano `main`.  
**Rozdział:** `chapters/pl/algebraic_topology/15-operacje-kohomologiczne-naturalnosc-iloczyny-i-relacje.tex`.  
**Stan po poprawkach:** źródło blob `0ccb9d64de7e086d5f04cd01bef99249b49ec3fb` (634 wiersze), 12 zachowanych etykiet.  
**Zasada:** audyt istniejącego materiału bez nowych twierdzeń, lematów i tematów; poprawność matematyczna, domknięcie dowodów, język, rysunki, LaTeX, odsyłacze, testy i CI.

## Audyt I — kompletna lektura oraz wzór Whitney’a

Odczytano cały wcześniejszy TOP-15 i raport `TOP_15_16_ITERACJA_18_2026-11-21.md`, upewniając się, że wcześniejsze scalenie zachowało przykład Bocksteina na RP², rysunek, przykład niezerowej relacji Adema, argument dla ΣCP² oraz całą część o klasach Thoma i Whitney’a.

W dowodzie wzoru Whitney’a brakowało jawnego zdefiniowania iloczynu względnych klas Thoma. Zastąpiono dwuzdaniowy skrót dowodem przez produkt włóknisty dysków, produkt zewnętrzny względnych klas, naturalność kwadratów Steenroda i wreszcie różnowartościowość izomorfizmu Thoma. Wskazano zgodność identyfikacji par z bezpośrednią sumą wiązek. Uwzględniono także **wiązki rzędu zero**: `D^0={*}`, `S^{-1}=∅`, `U=1_B`; brakujące założenie byłoby błędem, ponieważ twierdzenie jawnie dopuszcza `r=0`. Poprawiono błąd gramatyczny w definicji redukcji modulo 2.

**Commit źródła:** `f25dc09a547c9707e6af710631a439705bcae96a`.

## Audyt II — Bockstein, iloczyn kubkowy, nieorientowalna wiązka

Sprawdzono przykład komórkowy RP²: sam operator brzegowy `∂₂=2` dowodzi jedynie niezerowości klasy Bocksteina, a nie identyfikuje jej *jako iloczynu kubkowego*. Dopisano przejście przez znany pierścień `H^*(RP²;F₂)=F₂[t]/(t³)`. W twierdzeniu o całkowitym kwadracie jawnie sprawdzono zachowanie jedynki `Sq(1)=1`.

W dowodzie istnienia mod-2 klasy Thoma wskazano przyczynę braku założenia orientowalności: automorfizmy `H^r(D^r,S^{r-1};F₂)=F₂` są trywialne, zatem lokalny system orientacji po zmianie współczynników na `F₂` jest stały. Niestabilność operacji w kohomologii względnej doprecyzowano przez przejście do zredukowanej kohomologii ilorazu i osobno do przypadku rzędu zero.

**Commit źródła:** `dfbb56d87399518b1c236e5c9df82a866e7fbe7c`.

## Audyt III — terminologia i osobne testy obliczeniowe

Usunięto przestarzały komentarz redakcyjny „Iteracja VIII”, bez naruszania matematycznej treści. Uzupełniono testy regresyjne w `application/tests/test_topology_chapters_15_16.py` o:
- sprawdzenie wzoru Whitney’a w rodzinie tożsamości wielomianowych `(1+t)^r(1+t)^s=(1+t)^{r+s}` modulo 2, w tym `r=0` i `s=0`;
- niezależne porównanie komórkowego Bocksteina i `Sq¹` dla `RP^N`, `1≤N≤23`;
- algorytmiczne przekształcenie 775 słów długości od dwóch do czterech, z indeksami w `{1,…,5}`, do sumy dopuszczalnych słów przez relacje Adema. Algorytm uwzględnia redukcję współczynników modulo 2 i sprawdza brak niedopuszczalnych par, zachowanie sumy indeksów oraz nierosnącą długość.

Weryfikacja redukcji 775 słów została również wykonana w niezależnym obliczeniu testowym (775 przypadków, zero niezgodności); **nie** traktuje się jej jako zastępstwa uniwersalnego dowodu twierdzenia.

**Commity:** `f8265f6b59d4fb5f44521f0a5d46a43344b3010f`, `e4b06e8ab10c60c6935f85ab51148228463cd006`, `7166ac69a589f9090bcf35be429cb46d88d10365`.

## Audyt IV — czysta ponowna kontrola aktualnego źródła

Ponownie pobrano najnowsze źródło i plik testów bez korzystania z tekstu aktualizującego:
- **634 wiersze, 12 historycznych etykiet, wszystkie unikalne**;
- dokładna kontrola stosu środowisk `\begin`/`\end`: bez niezgodności;
- 1 diagram TikZ i wszystkie historyczne odsyłacze zachowane;
- kontrola terminologii: bez „tensorowania”, „sekwencji”, „injekcji”, „unii” oraz komentarzy iteracyjnych;
- obecność uzupełnionych wzorów i wszystkich trzech nowych grup testów potwierdzona;
- przejrzano twierdzenie o Bocksteinie, obie relacje Adema z przykładów, redukcję dopuszczalną, konstrukcję ΣCP² i klasę Thoma z wzorem Whitney’a. Nie znaleziono kolejnej luki wymagającej modyfikacji źródła.

## GitHub Actions

Wcześniejsze przebiegi po źródłowym commicie `dfbb56d87399518b1c236e5c9df82a866e7fbe7c` przeszły wszystkie trzy kontrole. Po ostatnich zmianach (usunięcie komentarza i dołożenie testów) końcowy zestaw CI dla commita `7166ac69a589f9090bcf35be429cb46d88d10365` jest weryfikowany. Po uzyskaniu wyników należy dopisać ostateczne adresy przebiegów i status rozdziału.

**Wniosek matematyczny:** audyt IV czysty. Status formalny: **oczekuje na potwierdzenie ostatniego CI**, po którym możliwe jest zamknięcie TOP-15 jako stabilnego. Następny w kolejności jest TOP-16. Automatyzacje nadal są wyłączone.
