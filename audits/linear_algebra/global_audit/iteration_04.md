# Globalny audyt algebry liniowej — iteracja 04/09

**Data:** 22 listopada 2026, ok. 04:00 CET.  
**Wejściowy HEAD:** `b98e9cc4970120244e7da9f58d2290a44119d17f`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** rozdziały 13–16.  
**Odczytano:** `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raporty 01–03, `status.md` oraz cztery źródła LaTeX. Porównanie szczegółowości z DG-01 pozostaje pośrednie, bez niezależnego odczytu pełnego źródła DG-01.

## Rzeczywisty zakres weryfikacji

Pełne źródła mają odpowiednio 1303, 1689, 1782 i 887 wierszy. W rozdziałach występuje 15, 17, 13 i 12 środowisk `proof` (łącznie 57). Sprawdzono ich strukturę, założenia i odsyłacze, a szczegółowo następujące argumenty:

- **13:** dopełnienia ortogonalne bez założenia skończonego wymiaru całego V, rozkład dla skończenie wymiarowego U, poprawną konwencję liniowości drugiego argumentu, równania normalne, rzut na (ker A)^⊥ i jednoznaczność rozwiązania minimalnej normy. Weryfikacja: w dowodzie najmniejszej normy rozkład x_0=k_0+u_0 i równość norm wynikają z ortogonalności, a nie z nieudowodnionego założenia.
- **14:** rozkład Schura z indukcją na kompresji do e_1^⊥; iloraz Rayleigha i warunki równości; jednoczesna unitarna triangularizacja przemiennych S,T przez wspólny wektor własny, iloraz i flagę niezmienniczą. Zapis S=U^*G_SU przy U=Q^* jest poprawny. W przypadku n=0 dopisano uzasadnienie.
- **15:** indukcyjny LU przez dopełnienie Schura, w tym niezerowe wiodące minory; PLU dla osobliwych macierzy i zerowej pierwszej kolumny; oszacowanie operatorowe i Frobeniusa w dowodzie Eckarta--Younga; kanoniczny rozkład biegunowy z W^*W=P_(ker A)^⊥. Wykryto nieokreślone symbole σ_j dla j>r we wzorze sumującym do p; poprawiono przez jawną konwencję zerowych wartości osobliwych.
- **16:** dowód Cayleya--Hamiltona przez porównanie współczynników, a nie nieuprawnione podstawianie macierzy do tożsamości nieprzemiennej; rozkład na jądra czynników względnie pierwszych, stabilizacja uogólnionych przestrzeni własnych i kryterium diagonalizowalności. Przypadek V=0 jest obsłużony.

## Korekty zapisane w tej iteracji

1. **Rozdział 15, Twierdzenie Eckarta--Younga:** po zdefiniowaniu tylko dodatnich σ_1,…,σ_r wzór na minimum w normie Frobeniusa sumował do p=min(m,n), używając σ_{r+1},…,σ_p bez definicji. Dodano konwencję σ_j=0 dla r<j≤p, obejmującą także A=0 i k≥r. To rzeczywista usterka formalna w sformułowaniu twierdzenia.
2. **Rozdział 15, Cholesky dla n=0:** zamiast słowa „oczywista” jawnie wskazano jedyny pusty czynnik i pusty warunek na przekątną.
3. **Rozdział 15, pseudoodwrotność:** uzasadniono implikację Av=0 ⇒ XAv=0, zastępując nieuzasadnione „oczywista”.
4. **Rozdział 14, jednoczesna triangularizacja dla n=0:** jawnie wyjaśniono, że pusta macierz jednostkowa jest unitarna, a macierz pusta jest górnotrójkątna.

W rozdziałach 13 i 16 nie zmieniano źródeł. Nie dodano nowych twierdzeń ani rozdziałów; zachowano wszystkie etykiety i odsyłacze.

## Terminologia, rysunki i CI

Przeszukano cztery rozdziały pod kątem niedopuszczonych wyrazów „unia”, samodzielnego „dual”, „rozszczepienie” i „tensorowanie”; nie znaleziono ich w treści. Pozorne dopasowania „sekwenc” występują wewnątrz poprawnego słowa „konsekwencja”. Rozdział 13 ma jeden rysunek TikZ, pozostałe nie mają rysunków TikZ. **Nie wykonano wizualnej kontroli jego strony w PDF**, więc brak kolizji graficznych nie jest potwierdzony.

Ostatni zakończony przebieg workflow `Linear algebra chapter validation` przed zapisem: [run 44974206393](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44974206393), SHA `9d9cfb24f52da38ae4b25d1e8201b81f4a2e01ab`, **success**. To wynik poprzedniego commitu, nie dowód sukcesu nowej zmiany. CI dla niniejszej iteracji i osobny PDF 13–16 **nie są jeszcze potwierdzone**. Ponowna kontrola po korektach pozostaje otwarta; nie oznaczamy iteracji jako czystej.

## Status

Iteracja 04 jest wykonana i udokumentowana; blok 13–16 wymaga kontroli po poprawkach i wizualnej inspekcji PDF. Bloki 01–12 mają nadal niezakończone kontrole wizualne. Następny blok to 17–20.
