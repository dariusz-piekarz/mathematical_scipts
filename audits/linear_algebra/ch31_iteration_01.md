# Algebra liniowa — rozdział 31, integracja i audyt I

**Data:** 21 listopada 2026  
**Źródło pierwotne:** `chapters/pl/differential_geometry_and_topology/04-grassmanniany-algebra-clifforda-i-spinory.tex` (blob `b6b8d669ab9b59d893de889eab90a1c79b644f7a`).  
**Rozdział:** `chapters/pl/linear_algebra/31-grupy-pin-spin-i-spinory.tex`.

## Integracja z geometrią różniczkową
- Przeniesiono w całości materiał o grupach Pin/Spin, spinorach zespolonych, klasyfikacji algebr Clifforda nad \(\C\), półspinorach, sferze Blocha, wiązkach spinorowych, strukturach spinowych i przeszkodzie \(w_2\), włącznie ze szczegółowymi dowodami, przykładami i diagramami TikZ.
- Źródło DG-04 pozostaje bez zmian. Etykietom w LA-31 nadano jednoznaczny prefiks `lin31-` i poprawiono odsyłacze do LA-30.
- Zamiast odsyłacza do rozdziału DG o rozmaitościach dodano dowód gładkości \(\mathrm O(n)\) przez surjektywność różniczki \(A\mapsto A^TA-I\).
- W konstrukcji wiązki głównej dopisano bezpośrednie uzasadnienie sklejania z lokalnych funkcji przejścia i odsyłacz do definicji wiązki z LA-29.
- Usunięto odsyłacz `hyperref` do nieistniejącego w LA rozdziału o koneksji spinorowej, zachowując wskazanie pojęciowe. Poprawiono pisownię „iniektywność”.
- Dodano do preambuły bibliotekę TikZ `decorations.markings` potrzebną do strzałek na rysunku nakrycia spinowego.
- Zarejestrowano rozdział w książce, katalogu i CI oraz dodano niezależne testy macierzy Pauliego, grup Spin(2)/Spin(3), reprezentacji \(SU(2)\), półspinorów i sfery Blocha.

## Kontrole wstępne
- Sprawdzono lokalne i globalne odsyłacze: brak nieprzeniesionych etykiet DG. Liczba nowych etykiet: 33.
- Wstępna weryfikacja terminologiczna, struktury rozdziału i zależności LA-29/30 zakończona bez problemów.

## Status
**Iteracja I jest etapem integracji i nie jest czystym audytem.** Wymagane pełne CI, oględziny samodzielnego PDF oraz kolejne niezależne audyty matematyczne, zwłaszcza twierdzeń o nakryciu Spin, klasyfikacji kompleksowej, nieredukowalności półspinorów i przeszkodzie \(w_2\).
