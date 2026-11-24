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
