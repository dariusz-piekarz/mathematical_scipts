# Globalny audyt 34 — spójność rozdziałów 06, 08, 16, 43

2026-11-24. Pierwsze przejście międzyrozdziałowe po zamknięciu lokalnych audytów 01–43. Gałąź biblioteka-matematyczna-iteracja-6. Baza 0c2ff0745c97e10a4c9a37694a1c214262014204.

## Ustalenia i korekty

- 06: w dowodzie rozkładu ortogonalnego wymieniono najpierw jądro B, następnie obraz transpozycji; wcześniejsza kolejność wymiarów była niespójna z kolejnością składników w formule. Zapisano jawnie obie równości wymiarowe, bez słowa „odpowiednio”. Dla drzewa widać od razu, że wymiar przestrzeni cykli wynosi 0, a przestrzeni gradientów n−1. Zmieniono „adjungowany” na „sprzężony”.
- 08: doprecyzowano relację wartości własnych dla grafu d-regularnego, d≥1: λ_j(L_G)=d λ_j(ℒ). Zasada Rayleigha używa bazy ortonormalnej, nie tylko ortogonalnej, zgodnie z obliczeniem normy.
- 16: wyprowadzono zgodność Δ_1=B^TB dla jednowymiarowego kompleksu ze standardowym iloczynem skalarnym; rozróżniono homologię cyklu od kohomologii, wykazując bezpośrednio równość ker d_1=im d_0 w wypełnionym trójkącie przez wymiary. Poprawiono pisownię Laplasjanu w tytule sekcji.
- 43: jawne powiązanie obu konwencji Laplasjanu i odsyłacz wstecz do rozdziału 08. W twierdzeniu o mieszaniu doprecyzowano potęgę zerową także dla K₂, dla którego czynnik kontrakcji wynosi 0.
- Zweryfikowano matematycznie zgodność energii, jądra i liczby składowych, dodatnich widm BB^T i B^TB, formuły Kirchhoffa i skalowania regularnego Laplasjanu. Nie zmieniano treści zatwierdzonych twierdzeń.

## Regresje

Dodano test tools/tests/test_graph_and_knot_cross_chapter_hodge.py (wszystkie 1099 etykietowanych grafów prostych o 1–5 wierzchołkach, dokładna eliminacja wymierna, kontrola obu Laplasjanów Hodge'a, skalowania regularnego, trójkąta oraz jawnych konwencji źródłowych). Włączono test do globalnego workflow i jego wyzwalaczy. To diagnostyka skończona, a nie dowód ogólnych twierdzeń.

**Status:** korekty źródła przygotowane; stabilizacja wymaga potwierdzenia nowego structural-audit, full-book-pdf i oględzin zmienionych stron. Globalny audyt pozostaje otwarty. Kolejny etap: niezależna kontrola wyniku tej iteracji, a następnie powiązania przekrojów, dualności planarnej, przepływów i skojarzeń.

## Stabilizacja — kontrola po commicie 9bc372b48096c2ef166885544db3c84b12a3927f

Przebieg [45294443694](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45294443694), przypięty do powyższego SHA. Zadanie structural-audit (138111151560) zakończone success. Odczytano rzeczywisty log: PASS: 1099 labelled simple graphs, 22 positive-degree regular graphs, C3 and filled triangle, source conventions. Liczby duplicate_labels, unresolved_references, forbidden_language są równe 0. Artefakt strukturalny 14875358169 istnieje (nie deklarujemy odczytu jego zawartości). Wszystkie wcześniejsze kroki matematyczne tego zadania także mają status success.

### Niezależna kontrola zgodności wzorów

- K₂: B=(-1,1)^T, BB^T ma widmo (0,2), B^TB ma jedną wartość własną 2. Stopień d=1, więc luka znormalizowana wynosi 2 i Q=J/2. Dla t=0 oszacowanie TV wymaga konwencji potęgi zerowej, a od t=1 rozkład jest jednostajny.
- C₃ z cykliczną orientacją: B ma rząd 2, ker B jest rozpięte przez (1,1,1)^T; na 1-kołańcuchach niewypełnionego trójkąta B^TB ma widmo (0,3,3). Po dodaniu 2-sympleksu d₁=(1,1,1), więc d₁^Td₁=J i Δ₁=B^TB+J=3I. Jądro znika, zgodnie z poprawionym przykładem. Na wierzchołkach λ₂(L_G)=3 i λ₂(ℒ)=3/2. Wzór Kirchhoffa daje 3 drzewa, natomiast podstawienie znormalizowanych wartości bez czynnika d^(n−1) dałoby błędnie 3/4. To konkretna kontrola potrzeby rozróżnienia konwencji.
- Doprecyzowanie oceny rozdziału 06: słowo „odpowiednio” można było odczytać zgodnie z kolejnością podprzestrzeni w poprzednim zdaniu dowodu, więc nie jest to dowód fałszywego twierdzenia. Korekta usuwa dwuznaczność względem kolejności składników w formule rozkładu.

Porównanie certyfikowanego SHA z bieżącą gałęzią przy odczycie pokazało tylko zmiany w algebrze abstrakcyjnej i teorii miary, bez zmian źródeł grafowych i ich workflow.

**Bramka jeszcze otwarta:** full-book-pdf (138111151894) podczas odczytu nadal instalował TeX. Nie potwierdzono kompilacji ani wyglądu zmienionych stron. Nie przechodzimy do kolejnego bloku przed stabilizacją.
