# Algebra liniowa — rozdział 28, audyt I

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/28-uklady-z-wymuszeniem-i-funkcje-przejscia.tex`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`

## Weryfikacja matematyczna

1. **Założenia:** n,m,p≥1, A,B,C,D mają jawne rozmiary. Rozróżniono stan początkowy, odpowiedź swobodną i odpowiedź na wymuszenie oraz człon bezpośredni D.
2. **Wariacja stałych:** wyprowadzenie przez v(t)=exp(-tA)x(t); sprawdzono pochodną całki, warunek początkowy i jednoznaczność. Dla wejść w L¹ poprawnie wskazano rozwiązanie absolutnie ciągłe i równanie prawie wszędzie.
3. **Model dyskretny:** dowód indukcyjny uwzględnia k=0 i sumę pustą. Indeksy splotu i impulsu są poprawne.
4. **Transformaty:** tożsamości Laplace'a i Z uzasadniono zbieżnością dla odpowiednich s/z, integracją przez części i zbieżnym szeregiem Neumanna. W modelu ciągłym G(s)=D+C(sI-A)^{-1}B; w dyskretnym identyczny wzór z z. Odwrotność w otoczeniu nieskończoności daje poprawne CA^kB.
5. **Parametry Markowa:** równość G i równość D,CA^kB jest dwukierunkowa; dla ciągłego jądra odpowiedzi uzasadniona szeregiem wykładniczym.
6. **Bieguny:** wskazano tylko implikację „biegun G ⇒ wartość własna A”; przykład ukrytego niestabilnego stanu prawidłowo przeczy implikacji odwrotnej.
7. **Realizacja towarzysząca:** policzono (ζI−A)v=p(ζ)e_n, pełną rangę Kalmana, jednowymiarowość przestrzeni wektorów własnych dla danego λ oraz kryterium PBH. Dla przypadku skalarnego minimalność ⇔ gcd(p,q)=1. Zweryfikowano także n=1 i q=0.
8. **Stabilność:** podano dokładne warunki Hurwitza/Schura i oszacowania potęg/wykładników przez postać Jordana; wyprowadzono oszacowania odpowiedzi dla wymuszeń ograniczonych.
9. **Przykłady:** odpowiedź skokowa, nieminimalna realizacja z ukrytym stanem, rozwinięcie (2s+3)/(s²+3s+2) na ułamki proste, a następnie splot dla wejścia stałego — rachunki spójne.

## Testy, PDF i poprawki

- GitHub Actions [run 44952985571](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44952985571): **SUCCESS**, obejmuje walidację struktury, odsyłaczy, języka, wszystkie dotychczasowe testy, nowy test 625 realizacji towarzyszących i 243 ciągów wymuszeń, pełną kompilację bez ostrzeżeń i eksport aktualnego rozdziału.
- Samodzielny PDF: **7 stron**, wszystkie zawierają tekst. Obejrzano wszystkie strony na montażu; brak widocznych kolizji lub uciętych wzorów. PyMuPDF: **0** bloków tekstowych poza obszarem stron.
- **Usterka redakcyjna I.1 (naprawiona w tym commicie):** zmieniono niegramatyczne „będzie przedziałami ciągła i miała zwarty nośnik” na „będzie funkcją przedziałami ciągłą o zwartym nośniku” w twierdzeniu o transformacie Laplace'a.
- Dodana poprawka zmienia źródło po uruchomieniu powyższego CI; wymaga ponownej walidacji.
- **Opcjonalne rozszerzenie do osobnej decyzji:** schemat blokowy A–B–C–D z rozdzieleniem odpowiedzi swobodnej i wymuszonej; nie dodano, bo nie jest konieczny dla poprawności.

## Decyzja

**Audyt I z jedną poprawką redakcyjną, nie jest czysty.** Rozdział 28 pozostaje w audycie; wymaga ponownej walidacji CI, kontroli PDF i co najmniej dwóch kolejnych czystych audytów przed stabilizacją.
