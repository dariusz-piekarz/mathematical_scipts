# Topologia ogólna — rozdział 11: audyt regresji 07 po wydzieleniu lokalnej zwartości

Data: 2026-11-22; gałąź `biblioteka-matematyczna-iteracja-6`.

## Zakres zmiany i zachowanie treści

Usunięto z `chapters/pl/general_topology/11-zupelnosc-i-twierdzenie-bairea.tex` wyłącznie sekcję `sec:topog-baire-lokalnie-zwarte`, obejmującą definicję `def:topog-baire-lokalna-zwartosc`, lemat `lem:topog-baire-zwarte-domkniecie` i twierdzenie `thm:topog-baire-lokalnie-zwarte`. Treść wraz z dowodami umieszczono w nowym rozdziale `chapters/pl/general_topology/14-zwartosc-lokalna.tex`, zachowując etykiety. Zmieniono jedynie tytuł sekcji w docelowym pliku i dodano wprowadzenie. Wstęp rozdziału 11 wskazuje teraz, że wersja lokalnie zwarta twierdzenia Baire’a będzie w rozdziale 14.

## Ponowna kontrola matematyczna rozdziału 11

1. Definicje ciągów Cauchy'ego, zupełności i zupełnej metryzowalności są samodzielne i nie zakładają lokalnej zwartości.
2. Dowód twierdzenia Baire'a w przestrzeni metrycznej opiera się wyłącznie na istnieniu zstępujących kul domkniętych o promieniach mniejszych od `2^{-n}` i zbieżności skonstruowanego ciągu Cauchy'ego. Nie wykorzystuje istnienia zwartych otoczeń ani lematów z rozdziału 14.
3. Wniosek dla przestrzeni zupełnie metryzowalnych wykorzystuje tylko metryczną wersję twierdzenia Baire'a.
4. Przykłady: `Q` jako zbiór gęsty i pierwszej kategorii, `Q` jako zbiór niebędący `G_δ`, otwarte podprzestrzenie przestrzeni Baire'a i niezupełny przedział pozostają w rozdziale 11 z samodzielnymi dowodami.
5. Wszystkie odwołania przez `\\ref` w samym rozdziale 11 rozwiązują się w rozdziale 11; żadna teza nie wymaga twierdzeń z rozdziału 14.
6. Rysunek zstępujących kul pozostał nietknięty, zachowano wcześniej zatwierdzone pozycje etykiet.

## Testy regresji

Test `test_general_topology_ch11.py` zaktualizowano, aby oczekiwał tylko twierdzeń rzeczywiście należących do rozdziału 11. Nowy `test_general_topology_ch14.py` weryfikuje obecność przeniesionych etykiet dokładnie raz w rozdziale 14, ich brak w rozdziale 11 oraz poprawność odsyłaczy w całej książce. Zmodyfikowano także katalog i CI do kompilacji rozdziału 14.

## Status

| Obszar | Wynik |
| --- | --- |
| Matematyczna niezależność rozdziału 11 od lokalnej zwartości | PASS |
| Zachowanie metrycznej wersji twierdzenia Baire'a | PASS |
| Etykiety i odsyłacze w źródle | PASS |
| Przeniesienie materiału bez utraty definicji/lematu/twierdzenia | PASS |
| Regresja kompilacji PDF na nowej gałęzi | PASS — workflow 45007367845 |
| Status stabilności po zmianie | **STABILNY — audyt regresyjny zamknięty** |

Następna czynność zgodnie z kolejnością użytkownika: po końcowej walidacji rozdziału 11 ponowna kontrola rozdziału 13.

## Zamknięcie kontroli technicznej

GitHub Actions `45007367845` zakończył się `completed/success` bez nieudanych kroków: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45007367845 . Pobrano artefakt `14747584273` z rzeczywistych kompilacji. PDF rozdziału 11 ma **4 strony A4**; rozdział 14 ma **1 stronę A4** z przeniesioną sekcją. Logi obu rozdziałów i rozdziału 13 nie zawierają `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence` ani `Fatal error`. Wykonano render i kontrolę wizualną wszystkich stron rozdziału 11 oraz strony rozdziału 14: bez ucięć, nakładających się etykiet lub nieczytelnych rysunków. Rozdział 11 zachowuje rysunek zstępujących kul w dobrym układzie.

**Werdykt: rozdział 11 pozostaje stabilny po zmianie struktury.**
