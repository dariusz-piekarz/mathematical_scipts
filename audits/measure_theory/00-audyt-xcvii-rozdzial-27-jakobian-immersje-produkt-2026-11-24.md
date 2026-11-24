# Audyt XCVII (97) — rozdział 27: jakobian, immersje i produkt

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt startowy e1e6712d59e6ecae05a12cf1bf65bb1479e590b7, raport XCVI.

## Kontrola i zmiany
- Ujednolicono argument macierzy metryki: G_x(u) jest macierzą w punkcie x^{-1}(u). Poprawiono definicję lokalną, dowód regularności oraz przykład gęstości.
- Doprecyzowano hipotezy twierdzeń zamiast odwołań do poprzedniego tekstu.
- Obrazy immersji C^1: osobno przypadek k=0; dla k>0 odwracalny minor i twierdzenie o odwzorowaniu odwrotnym dają wykres ciągłej funkcji w gładkiej mapie celu. Borelowskość wykresu i zerowe przekroje pionowe pozwalają zastosować Tonellego bez utożsamiania map C^1 z gładkim atlasem.
- Wyprowadzono wzór jakobianu przez macierze przejścia P,Q, tożsamości P^T GP=I i Q^T HQ=I oraz A=Q^{-1}DP; uzasadniono ciągłość, dodatniość i odwrotny jakobian.
- W produkcie: jawna całka na prostokątach, konwencja 0 razy nieskończoność, jednoznaczność lokalna i rozłączny podział przeliczalnego pokrycia.
- Pozostałe dowody: kryterium zerowości z uzupełnieniem, Radon–Nikodym i rozkład Lebesgue'a, rozłączny podział w zamianie zmiennych oraz przykład konforemny nie wykazały nowych luk w tym przeglądzie. Brak rysunków.
- Zachowano wszystkie 11 etykiet w tej samej kolejności (sprawdzono automatycznie podczas przygotowania zmiany).

## Bramka techniczna
Dodano pięć testów źródłowych i skończonych modeli oraz workflow rozdziału 27, wzorowany na działającej bramce 26, z kompilacją całego tomu i osobnego rozdziału, importem odsyłaczy, renderowaniem wszystkich stron i publikacją statusów.
Dla wcześniejszego commitu źródłowego 3b05e481b8e3b302d9899372f4d8478afbcb9f10 API potwierdziło jedynie sukces testów aplikacji i terminologii, nie kompilację rozdziału. Nowych testów, kompilacji i oględzin PDF jeszcze nie potwierdzono.

## Werdykt
NIESTABILNY. Wymagany niezależny przegląd nowej wersji, wynik CI i oględziny PDF. Nie przechodzić do 28. Bez rozszerzania zakresu.
