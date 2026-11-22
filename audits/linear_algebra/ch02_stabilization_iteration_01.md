# Algebra liniowa — rozdział 02: audyt stabilizacyjny I

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`, blob `1e59c0d13379ee7851f3a6386172640b02f9fa75` (bez zmian w tej iteracji).

## Lektura matematyczna, krok po kroku

Przeczytano wszystkie **1089 wierszy**, **16 dowodów**, definicje, stwierdzenia, przykłady i kontrprzykłady. Weryfikacja obejmowała:
- **Wymiar nieskończony.** Uzasadnienie jednoznaczności nośnika z rozdziału 01, kodowanie elementów skończonych zbiorów przez \(I\times\mathbb N_0\), dwie nierówności kardynalne i Cantora–Bernsteina. Twierdzenia zależne od AC mają je wskazane; brak odejmowania kardynałów nieskończonych.
- **Sumy algebraiczne.** Równość \(\sum U_i=\operatorname{span}(\bigcup U_i)\), pusta rodzina, operacje na podprzestrzeniach oraz wzór \(\dim(U+W)+\dim(U\cap W)=\dim U+\dim W\). Przy ostatnim sprawdzono, że \(C\cup A\cup D\) z rozszerzeń wspólnej bazy jest niezależna i rozpina; osobny argument skończony nie używa AC.
- **Sumy proste.** Trzy równoważne kryteria, rozkłady o skończonym nośniku, warunek dla pustej rodziny, kontrprzykład trzech prostych o zerowych przecięciach parami, zewnętrzna suma prosta i jądro sumowania oraz sumowanie wymiarów kardynalnych.
- **Warstwy i ilorazy.** Dwa zawierania potrzebne do równości warstw, dobrze określona struktura liniowa na warstwach, jądro i surjekcja \(\pi_U\), przypadki skrajne oraz pełny dowód własności uniwersalnej.
- **Dopełnienia i izomorfizmy.** Przejście od rozszerzenia bazy do dopełnienia, równość \(\dim V=\dim U+\dim(V/U)\) (i jej skończona postać), dobrze określony i bijektywny naturalny izomorfizm \(U/(U\cap W)\simeq(U+W)/W\).
- **Przykłady.** Sprawdzono przestrzenie nad \(\mathbb R\), \(K[X]\), rozkład na parzyste i nieparzyste stopnie (także w charakterystyce 2), niejednoznaczność dopełnienia i poziome warstwy w \(\mathbb R^2\).

## Kontrole techniczne i redakcyjne
- Wszystkie odsyłacze z rozdziału 02 wskazują na istniejące etykiety rozdziałów 01–02; brak własnych powtórzonych etykiet. Globalne zakazy terminologiczne bez naruszeń w prozie. Nie dodano twierdzeń ani nowych zagadnień.
- Porównano szczegółowość z plikiem rozdziału 01 geometrii różniczkowej (ponad 6400 wierszy; standard dowodów i przykładów, nie wymóg sztucznego zwiększania długości).
- Z istniejącego zakończonego sukcesem CI dla commitu `246eb9a` pobrano **całą książkę, 315 stron**, i wyodrębniono rozdział 02: **10 stron A4**. Sprawdzono każdą stronę i rysunek warstw; brak pustych stron i bloków tekstu wychodzących poza format, log nie zawiera `Overfull`, `Underfull`, błędów brakujących znaków ani niezdefiniowanych odsyłaczy.
- Dodano `tools/test_linear_algebra_ch02.py` i krok workflow weryfikujące dokładnie wszystkie podprzestrzenie \(\mathbb F_2^4\) i \(\mathbb F_3^3\) (odpowiednio 67 i 28), wzory wymiarowe, ilorazy, sumy proste i izomorfizm kanoniczny. **Status nowego CI: do potwierdzenia po uruchomieniu**; nie nazywamy tego PASS przed wynikiem.

## Wniosek
Nie znaleziono usterki matematycznej wymagającej poprawki źródła. **Iteracja I wykonana, źródło bez zmian; jeszcze dwie niezależne czyste kontrole i CI dla nowego testu do ostatecznej stabilizacji.**
