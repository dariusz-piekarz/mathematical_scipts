# Algebra liniowa — rozdział 29, audyt VI

**Data:** 21 listopada 2026  
**Poprzedni blob:** `23803e63f9834a86b591a1cb570b6e2c351c81f8`.

## Rozróżnienie immersji i osadzenia

W dotychczasowym tekście zatytułowano twierdzenie „Zanurzenie Plückera”, choć dowód wykazuje zarazem iniektywność różniczki (immersję) oraz homeomorfizm na obraz (osadzenie topologiczne). Łącznie te własności dowodzą **gładkiego osadzenia**. Zgodnie z precyzyjną terminologią zamieniono nazwę i konkluzję na „Osadzenie Plückera”, nie zmieniając wzorów ani odsyłaczy.

## Niezależna kontrola rachunków
- **175** dokładnych testów wymiary 2+2: obliczenie rzutowania na wykres A przez T(T*T)^(-1)T*, idempotentność, odzyskanie A z bloków rzutowania i gładka zmiana map przy zmianie P⊕Q — PASS.
- Weryfikacja map wykresowych obejmuje przypadki, gdy minor w nowej mapie jest odwracalny. Warunek dziedziny przejścia jest dokładnie warunkiem odwracalności D_A z tekstu.
- Przy osadzeniu Plückera wzór L={w: w∧ξ=0} pozwala odzyskać L, lokalne współrzędne przez minory dają lewą odwrotność różniczki, a zwartość grassmannianu i Hausdorff celu zapewniają osadzenie topologiczne.

## Decyzja
Audyt VI wykrył i poprawił ważną nieprecyzyjność nazwy i tezy, zatem **nie jest czysty**. Potrzebne dwa kolejne czyste audyty źródła oraz końcowa kontrola CI/PDF.
