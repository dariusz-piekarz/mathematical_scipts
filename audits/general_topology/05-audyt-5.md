# Topologia ogólna — rozdział 05 — audyt 5

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.4 (zmieniona).  
**Status:** audyt z poprawkami — 0/2 czystych.  
**Źródło SHA-256:** `df9bcff25e15af3ae087a94b03af69d94152b70380a7a74533e43a98b57bb1af`.

## Weryfikacja ścisłości hierarchii

1. $T_0\not\Rightarrow T_1$: przestrzeń Sierpińskiego — obecna, poprawna.
2. $T_1\not\Rightarrow T_2$: nieskończona przestrzeń koskończona — obecna, poprawna.
3. $T_2\not\Rightarrow T_3$: $K$-topologia — obecna, poprawna.
4. $T_3\not\Rightarrow T_{3\frac12}$: przestrzeń Mysiora — dodano
   pełną konstrukcję, szczegółowy dowód $T_3$ i braku całkowitej regularności.
5. $T_{3\frac12}\not\Rightarrow T_4$: płaszczyzna Sorgenfreya — obecna, poprawna.

Dodano schemat $B_x$ w konstrukcji Mysiora i rozpisaną listę odsyłaczy
w końcowym zestawieniu aksjomatów. Pozostałe twierdzenia bez zmian.

## Kontrola

- Testy regresyjne rozdziałów 01–05: PASS.
- Rozdział 05: enumeracja 390 topologii do 4 punktów — PASS.
- Podprzestrzenie: 5931 przypadków — PASS.
- Testy normalności: 4133 przypadki — PASS.
- Testy Tietzego na modelach skończonych: 7688 funkcji — PASS.
- LaTeX: etykiety, odsyłacze i środowiska — PASS.
- Samodzielny PDF: 10 stron — PASS bez ostrzeżeń.
- Cała książka 01–05: 46 stron — PASS bez ostrzeżeń.
- Kontrola wizualna stron PDF, zwłaszcza rysunku Mysiora — PASS.

## Decyzja

Audyt 5 wymagał dodania brakującego kontrprzykładu. Rozdział
nie jest jeszcze stabilny, nadal **0/2 czystych audytów**.
Nie wykonywać GitHub push przed stabilizacją.
