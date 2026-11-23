# AA-44 — audyt III: końcowa stabilizacja matematyczna i techniczna

**Data:** 23 listopada 2026 r.
**Werdykt: AA-44 STABILNY.**
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/abstract_algebra/44-twierdzenie-liouvillea-o-calkowaniu-elementarnym.tex.
**Zweryfikowany blob SHA źródła:** f750ccc0e673e0e7467973d878f75401374813ec.
**Commit ostatecznej zmiany źródła:** 9edced10d90537b7466f9bf2d94f4b9a439b63eb.

## 1. Zakres i pełna kontrola twierdzenia

Sformułowano i udowodniono obie implikacje twierdzenia Liouville'a dla ciała różniczkowego K charakterystyki zero, przy zachowaniu ciała stałych C w elementarnym rozszerzeniu. Warunek to istnienie v w K, niezerowych u_j w K oraz c_j w C, dla których f=Dv+sum_j c_j Du_j/u_j. Nie założono algebraicznej domkniętości C; dzięki hipotezie braku nowych stałych nie jest ona potrzebna do przeprowadzonych argumentów.

Weryfikacja matematyczna obejmowała:
1. Jednoznaczną formalną część wielomianową pp_t(R), z dowodem zachowania właściwości funkcji wymiernej przez D w przypadkach Dt=a oraz Dt=ht.
2. Części wielomianowe pochodnej logarytmicznej dla unormowanych wielomianów p i q: Db/b (krok pierwotny) oraz Db/b+(deg p-deg q)h (krok wykładniczy).
3. Algebraiczne zejście dla skończonych rozszerzeń nierozdzielonych? Nie: w charakterystyce zero każde skończone rozszerzenie jest rozdzielcze. Użyto poprawnych wzorów na ślad i normę, bez wymagania normalności, oraz dzielenia przez niezerowy stopień rozszerzenia.
4. Logarytmiczne zejście z rozbiciem na stopień wielomianu m=0, m=1 i m>=2. W ostatnim przypadku sprzeczność wynika z nowej stałej t-w.
5. Wykładnicze zejście: każdy dodatni współczynnik p_k prowadziłby do nowej stałej p_k t^k; pozostały wyraz A Da jest dokładną pochodną.
6. Przejście indukcyjne po całej wieży, z użyciem kroku algebraicznego także dla algebraicznych generatorów spełniających jednocześnie warunek logarytmiczny lub wykładniczy.
7. Dostateczność przez selektywne dołączanie tylko tych funkcji pierwotnych Du_j/u_j, których nie ma jeszcze na danym piętrze. Z lematu AA-43 wynika wtedy zachowanie stałych. Sprawdzono n=0, współczynniki zerowe i powtarzające się logarytmy.
8. Rozróżnienie dodatnich części wielomianowych i ujemnych potęg szeregów Laurenta. Nie użyto nieprawdziwego twierdzenia, że pochodne logarytmiczne nie mają ujemnych potęg.
9. Kontrprzykład dla Q(x) i 1/(x^2+1): reszta 1/(2i) przy x=i nie może powstać z wymiernych kombinacji pochodnych logarytmicznych funkcji z Q(x). Dopuszczenie i wymaga nowych stałych i nie przeczy twierdzeniu.

## 2. Audyty i poprawki

Raporty ch44_iteration_01.md i ch44_iteration_02.md dokumentują dwa przeglądy matematyczno-redakcyjne, w tym niezależną analizę przypadków brzegowych. W trakcie audytów:
- Usunięto tautologiczne sprawdzenia z niezależnego zestawu testów i zastąpiono je nietrywialnymi rachunkami derywacji na wymiernych liczbach, bez SymPy.
- Dodano przykład pokazujący znaczenie zachowania ciała stałych, gdy C nie jest algebraicznie domknięte.
- Zachowano wszystkie hipotezy, kwantyfikatory oraz oddzielone kroki dowodu obu implikacji.

## 3. Rzeczywista walidacja GitHub Actions

**Końcowy przebieg:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45151940204
**Head SHA przebiegu:** 9edced10d90537b7466f9bf2d94f4b9a439b63eb.
**Wynik:** completed / success, 79/79 zakończonych sukcesem kroków zadania.

Potwierdzone w krokach i logu:
- AA-44 matematyczne testy SymPy: 9/9 unittest PASS;
- AA-44 niezależne testy wielomianowe na fractions.Fraction: 5/5 unittest PASS;
- bramka integralności źródeł AA-01–AA-44: PASS — 44 rozdziały w prawidłowej kolejności, 884 unikalne etykiety, 0 duplikatów, 399 wystąpień odsyłaczy, 261 różnych celów, 0 brakujących; 410 dowodów i 282 przykłady łącznie w książce;
- historyczne przekrojowe pokrycie audytów AA-01–AA-42 zachowano (11 raportów); AA-43 i AA-44 mają oddzielne audyty;
- pełna kompilacja książki latexmk: success;
- końcowa weryfikacja PDF i odsyłaczy: success;
- archiwizacja artefaktu: success.

Przejściowe ostrzeżenia o niezdefiniowanych odsyłaczach z pierwszego przebiegu LaTeX zostały usunięte przez kolejne przebiegi latexmk. Nie są ostrzeżeniami końcowego logu.

## 4. Rzeczywisty PDF i przegląd stron

Artefakt końcowy z udanego workflow:
**nazwa:** abstract-algebra-aa01-aa44;
**ID:** 14806487797.
W oryginalnym archiwum GitHub Actions:
- abstract_algebra.pdf: 281 stron, 2 087 778 B, SHA-256 9bd48750efe5c445815a5864bc663b70506b00ee556973fb62ba578322ef91c0;
- abstract_algebra.log: 45 581 B, SHA-256 0d0858cd93fc8cb1ded0711b0280eabefb75f8bc94c7702e6f26f6c52bcf2e5f.

Sprawdzono końcowy log: 0 błędów LaTeX, 0 ostrzeżeń LaTeX, 0 overfull/underfull, 0 ostrzeżeń hyperref i 0 nierozwiązanych odsyłaczy.

AA-44 zajmuje sześć kolejnych stron PDF 276–281 (drukowane 267–272). Wyrenderowano wszystkie sześć stron i sprawdzono ich układ; strony nie zawierają obcięć, kolizji tekstu ani przenikania bloków matematycznych. Analiza pozycji tekstowych wykazała 0 fragmentów poza granicami stron. Ostatnia strona jest rzadsza typograficznie, lecz poprawna; nie stwierdzono usterki wymagającej modyfikacji źródła.

## 5. Decyzja i granice

**AA-44 STABILNY** w badanym zakresie: poprawność sformułowań i dowodów, dwa niezależne zestawy regresyjne, integralność katalogu i książki, pełny zielony CI, finalny PDF i przegląd każdej nowej strony. Testy obliczeniowe nie są przedstawiane jako formalny dowód twierdzenia.

AA-01–AA-42 pozostają zamkniętym historycznym zestawem audytów, AA-43 zachowuje status stabilny. **Następnym rozdziałem jest AA-45 — kryteria hiperwykładnicze i całki nieelementarne; jego prace mogą rozpocząć się dopiero po niniejszym zamknięciu AA-44.** AA-46 — teoria Picarda–Vessiota — pozostaje kolejnym etapem.
