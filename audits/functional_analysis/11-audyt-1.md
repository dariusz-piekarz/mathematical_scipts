# Analiza funkcjonalna — rozdział 11 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/11-przestrzenie-frecheta-twierdzenia-o-odwzorowaniu-otwartym-i-wykresie-domknietym.tex`.  
**SHA blob:** `ac11608f7af7af32c893cb5e77a3400d1fb7f993`.  
**Werdykt:** pierwszy przegląd merytoryczny bez wykrytej usterki; **0/2 potwierdzonych czystych audytów stabilizacyjnych**, ponieważ nie potwierdzono CI i kompilacji dla rozdziału 11.

## Ustalenie punktu kontynuacji

Przed audytem odczytano katalog raportów: ostatni istniejący raport dotyczył rozdziału 10 (`10-audyt-4.md`), nie było raportu 11. Raport 10/04 potwierdza dwa czyste audyty 10/03–10/04 i dwa ukończone sukcesem przebiegi CI, w tym #45224548863. Niezależny odczyt API dla #45224548863 potwierdził `completed/success` (23 listopada 2026, 17:11:32 UTC). Ten przebieg **nie jest dowodem przejścia testów rozdziału 11**.

## Przegląd merytoryczny

Odczytano całe źródło rozdziału 11 (19 535 znaków). Skontrolowano **10 środowisk proof** i **6 środowisk przyklad**:

1. Metryka z przeliczalnej rodziny seminorm: nierówność trójkąta, rozdzielanie punktów, równoważność topologii i jednostajnych warunków Cauchy'ego.
2. Domknięte podprzestrzenie i ilorazy Frécheta: niezależność metryki ilorazowej od reprezentantów, otwartość rzutowania, konstrukcja podciągu Cauchy'ego i jego podnoszenia; zupełność produktów.
3. Krok Baire'a: pochłanianie i wypukłość, przejście od niepustego wnętrza domknięcia do otoczenia zera.
4. Odwzorowanie otwarte: wybór malejących otoczeń `U_n`, `V_n`, rekurencja reszt, szereg w zupełnym `E`, inkluzja granicy do `U` i otwartość obrazu.
5. Ciągłość odwrotności z otwartości bijekcji.
6. Oszacowanie normy odwrotności Banacha.
7. Izomorfizm ilorazu przez jądro surjekcji.
8. Kryterium sekwencyjne domknięcia wykresu w metryzowalnym produkcie.
9. Twierdzenie o wykresie domkniętym przez bijekcję rzutowania wykresu na `E`.
10. Równoważność dwóch zupełnych norm porównywalnych.

Sześć przykładów sprawdzono pod kątem hipotez i obliczeń: `K^N` i `C^infty`; bijekcja `ell^1` z normą `ell^2` w przeciwdziedzinie; odwrotna identyczność z domkniętym wykresem; pochodna na `C^1` jako operator nieograniczony o domkniętym wykresie; ciągła i surjektywna pochodna na `C^infty`; gęsty właściwy obraz `ell^1 -> ell^2`. W szczególności wektor z pierwszymi `n` współrzędnymi `1/n` ma normy `1` i `n^{-1/2}`; dla `f_n=n^{-1}sin(nt)` normy funkcji dążą do zera, a normy pochodnych wynoszą 1.

**Nie wykryto błędu wymagającego korekty matematycznej w tym przeglądzie.** Nie należy interpretować tego jako niezależnego formalnego dowodu wszystkich twierdzeń.

## Struktura, terminologia, odsyłacze

Skryptowa kontrola aktualnego pliku: 10/10 par `proof`, 2/2 `definicja`, 3/3 `twierdzenie`, 2/2 `stwierdzenie`, 1/1 `lemat`, 4/4 `wniosek`, 6/6 `przyklad`, 4/4 `uwaga`. W rozdziale **20 etykiet, bez lokalnych duplikatów; 16 odsyłaczy**, wszystkie cele znaleziono w źródłach rozdziałów 01–11 pobranych z bieżącej gałęzi. W tekście zachowano polskie terminy „przestrzeń sprzężona”, „ciąg”, „sieć” i „zbieżność jednostajna na zbiorach zwartych”. Rysunek TikZ schematu wykresu domkniętego jest obecny; **nie wykonano wizualnej inspekcji PDF**.

## Bramki techniczne i dalsze kroki

Nie uruchomiono w tej iteracji testów regresyjnych rozdziału 11 ani kompilacji LaTeX; brak zweryfikowanego zakończonego CI dla bieżącego źródła 11. Nie deklaruje się PASS dla testów, kompilacji ani PDF. W następnej iteracji należy zidentyfikować i uruchomić testy 11, skontrolować workflow i rzeczywiście wygenerowany PDF (w tym schemat TikZ), a następnie wykonać niezależny audyt stabilizacyjny na niezmienionym źródle. Rozdział 12 pozostaje zablokowany.

**Zmiany w źródle:** brak; **zmiany w testach:** brak. Ten raport jest jedynym plikiem dodanym w iteracji.
