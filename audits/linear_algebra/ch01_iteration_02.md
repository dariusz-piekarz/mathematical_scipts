# Algebra liniowa, rozdział 01 — audyt, iteracja 2

Data: 2026-11-21  
Gałąź docelowa: \`biblioteka-matematyczna-iteracja-6\`  
Rozdział: \`chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex\`

## Ponowny audyt matematyczny

Prześledzono kolejność założeń i dowodów: aksjomaty przestrzeni; przykłady nad ogólnym ciałem, \(\mathbb R\), \(\mathbb C\), \(\mathbb F_2\); podprzestrzenie i kryterium ich rozpoznawania; rozpinanie; niezależność rodziny indeksowanej; baza; usuwanie generatorów; wymianę Steinitza; uzupełnianie do bazy; współrzędne; bazy Hamela i lemat Zorna. Kontrolowano przypadki brzegowe \(V=\{0\}\), \(n=0\), rodzinę pustą i zależność od ciała skalarów.

### Usterki i uzupełnienia wprowadzone do rozdziału

1. **Brak ważnego twierdzenia o wymiarze podprzestrzeni.** Dodano i udowodniono: jeśli \(W\leq V\), \(\dim_KV<\infty\), to \(W\) ma skończony wymiar, \(\dim_KW\leq\dim_KV\), a równość zachodzi dokładnie dla \(W=V\). Dowód konstruuje bazę \(W\) bez używania lematu Zorna.
2. **Brak kanonicznego przykładu bazy macierzy i pełnego dowodu bazy \(K^n\).** Dodano obliczenia dla \((e_1,\ldots,e_n)\), baz \((E_{ij})\) przestrzeni macierzy i uzasadnienie wymiaru \(mn\).
3. **Zbyt skrótowy dowód minimalności bazy jako zbioru rozpinającego.** Jawnie uzasadniono, dlaczego istnienie \emph{jakiegokolwiek} właściwego podzbioru rozpinającego prowadziłoby do możliwości usunięcia jednego elementu.
4. **Język:** usunięto niepotrzebny termin „suma zbiorowa” przy opisie unii podprzestrzeni.

### Kontrola struktury

Po poprawkach: 57 unikalnych etykiet; wszystkie \`ref\`/\`eqref\` prowadzą do etykiet wewnątrz rozdziału; brak niedomkniętych środowisk \`begin\`/\`end\`; rysunek jest osadzony w TikZ. Rozdział został zapisany i zatwierdzony na docelowej gałęzi Biblioteki.

### Kontrola CI — rozróżnienie zaległości globalnych

Pierwotny wariant testu \`linear-algebra-chapter.yml\` kończył się przed kompilacją wskutek **24 błędów historycznych repozytorium** (brakujące importy w innych działach i rozbieżności kopii źródeł). Zmieniono test tak, aby najpierw sprawdzał nowy rozdział i wpis w katalogu, następnie raportował osobno istniejące błędy globalne z \`continue-on-error\`, a po tym uruchamiał pełną kompilację LaTeX. Globalnych błędów nie uznano za naprawione ani nie usunięto ich z dziennika.

### Status

**Audyt 2: poprawki merytoryczne naniesione, rozdział nadal otwarty.**
Kolejna iteracja: audyt 3, dokładne sprawdzenie wariantów dowodów, jakości przykładów, składu rysunku i wyniku kompilacji CI.
