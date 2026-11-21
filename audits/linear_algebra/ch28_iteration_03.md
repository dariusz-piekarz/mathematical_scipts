# Algebra liniowa — rozdział 28, audyt III (pierwszy czysty)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/28-uklady-z-wymuszeniem-i-funkcje-przejscia.tex`  
**Blob źródłowy:** `945b4ecd36bfa2f0ccbffe9c4236d3ba2eafdbf0` — bez modyfikacji w tej iteracji.

## Niezależna kontrola matematyczna
1. **Wariacja stałych i regularność.** Wzór na stan wynika z różniczkowania `exp(-tA)x(t)`. W dowodzie zwrotnym jawnie użyto reguły Leibniza, a dla wymuszeń L¹ osobno rozwiązania absolutnie ciągłego; żaden krok nie wymaga ciągłości tego wejścia.
2. **Model dyskretny i splot.** Indukcja obejmuje k=0. Splot dyskretny ma h₀=D, hₖ=CA^(k−1)B dla k≥1. W modelu ciągłym człon bezpośredni jest oddzielony od jądra h(t)=Ce^(tA)B; impuls Diraca nie jest utożsamiany z funkcją zwykłą.
3. **Transformata Laplace'a.** Przy wymuszeniu przedziałami ciągłym o zwartym nośniku otrzymuje się oszacowanie ||x(t)||≤K exp(t||A||). Stąd dla Re s>||A|| całkowanie przez części jest uprawnione, a rezolwenta istnieje. Stwierdzenie ogranicza się do tego zakresu i nie przypisuje fałszywej globalnej zbieżności.
4. **Transformata Z i parametry Markowa.** Szereg Neumanna dla (zI−A)⁻¹ jest zbieżny przy |z|>||A||; rozdzielenie współczynnika D i wyrazów CA^kB jest jednoznaczne. Wniosek o porównaniu dwóch układów poprawnie podaje niezależne wymiary stanu n₁,n₂ i wspólne m,p.
5. **Racjonalność oraz bieguny.** Wzór na macierz odwrotną uzasadnia stopień mianownika i brak biegunów poza widmem A. Kontrprzykład z A=diag(1,−1), B=(0,1)^T i C=(0,1) prawidłowo usuwa niestabilny, nieobserwowalny i nieosiągalny tryb z transmitancji.
6. **Realizacja towarzysząca.** Mnożenie (zI−A)(1,z,…,z^(n−1))^T=p(z)eₙ zostało sprawdzone. Triangularność macierzy sterowalności wynika indukcyjnie z A e_j=e_(j−1)−a_(j−1)eₙ. Kryterium obserwowalności PBH nie zakłada prostych pierwiastków p, gdyż wektory własne przy danym λ zawsze stanowią przestrzeń jednowymiarową. Dopuszczono q=0 i n=1.
7. **BIBO.** Z oszacowań bloków Jordana i sumy/całki geometrycznej wynika podana zależność od ||u||∞. Tekst ostrożnie podaje wyłącznie kryteria dostateczne oraz rozróżnia stabilność wejście–wyjście od stabilności ukrytego stanu.

## Niezależne testy i poprawność składu
- SymPy: **150** przypadków realizacji towarzyszących o rozmiarach 1–5, z porównaniem wymiernej transmitancji, macierzy sterowalności, obserwowalności i współczynników Laurenta — wszystkie PASS.
- **500** osobnych testów dokładnego wzoru na odpowiedź dyskretną z wymuszeniem, na ułamkach wymiernych — PASS.
- Istniejący zestaw w CI (625 przypadków współczynników, 243 przypadki wymuszeń) ukończony PASS.
- GitHub Actions: [run 44953371224](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44953371224), **SUCCESS** dla bieżącego bloba, wraz z pełnym PDF, kontrolą referencji, ostrzeżeń LaTeX i katalogu.
- Zweryfikowano 7 stron eksportowanego PDF, żadna nie jest pusta, **0** bloków tekstu poza granicami strony; wizualny montaż nie wykazał nakładania się elementów.

## Wynik
**Audyt III czysty.** Nie stwierdzono uchybień, nie zmieniono źródła. Potrzebny jest drugi niezależny czysty audyt IV i ostateczna walidacja przed stabilizacją.
