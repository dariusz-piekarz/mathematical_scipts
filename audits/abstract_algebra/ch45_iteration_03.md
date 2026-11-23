# AA-45 — audyt III: stabilizacja matematyczna, CI i PDF

**Data:** 23 listopada 2026 r. **Werdykt: AA-45 STABILNY**.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/abstract_algebra/45-kryteria-hiperwykladnicze-i-calki-nieelementarne.tex.
**Blob SHA rozdziału:** 56604f97c634d04423664e53ae9cc6eeca19fc2d.
**Bloby SHA testów:** SymPy 5705d23d11f2ae79971b7a7ec812883769f4997b; niezależny Fraction b7a18726da731a3a7be1b97750ef9f7547194b5f.

## 1. Weryfikacja matematyczna (audyty I i II)

1. **Przestępność i stałe:** dla niestałego wielomianu p nad C udowodniono, że e^{p(x)} jest przestępny nad C(x) i nie wprowadza nowych stałych. Wzór na normę i ślad wymuszałby niemożliwą równość pochodnej logarytmicznej funkcji wymiernej z niezerowym wielomianem.
2. **Kryterium st:** s(x)t ma elementarną funkcję pierwotną wtedy i tylko wtedy, gdy w C(x) istnieje rozwiązanie równania r'+hr=s (Dt=ht). Konieczność: twierdzenie Liouville'a i porównanie współczynnika przy t w formalnej części wielomianowej. Dostateczność: D(rt)=st.
3. **Skończone sumy Laurenta:** osobno udowodniono r_k'+khr_k=s_k dla k>0 oraz k<0, po przejściu do w=t^{-1}, Dw=-hw. Współczynnik k=0 jest wymierny i ma elementarną funkcję pierwotną. Nie zakładano niezależności t i t^{-1}.
4. **Przeszkody wymierne:** dla h regularnego w a i s z biegunem prostym r'+hr=s nie może mieć rozwiązania wymiernego, bo r' ma wyższy rząd bieguna niż hr; założenie o h jest konieczne. Przy h i s wielomianowych udowodniono ponadto przeszkodę stopnia z przypadkiem r=0.
5. **Całka Gaussa:** równanie r'-2xr=1 nie ma rozwiązania wymiernego. Niezależny rachunek całki oznaczonej √π/2 obejmuje zbieżność, twierdzenie Tonellego i zmianę na współrzędne biegunowe.
6. **Całka sinusowa:** przy t=e^{ix}, bez traktowania t i t^{-1} jako niezależnych, wymuszona jest niemożliwa tożsamość r'+ir=1/(2ix). Obliczenie całki Dirichleta uzasadnia granicę ε↓0 przez jednostajne względem ε oszacowanie ogonów 2/A.
7. **Logarytm całkowy i Ei:** brak wymiernego rozwiązania r'+r=1/x przez biegun prosty; podstawienie x=e^u w hipotetycznej pierwotnej 1/log x prowadzi do elementarnej pierwotnej e^u/u, dając sprzeczność.
8. **Całka eliptyczna:** dla K=C(x,y), y²=1-x⁴, jawnie wyprowadzono lokalne współrzędne we wszystkich punktach skończonych i dwóch punktach nad nieskończonością. Forma ω=dx/y jest niezerowa i nie ma biegunów. W K każda funkcja bez biegunów jest stała (dowód przez inwolucję y↦-y i analizę A(x)+B(x)y). Z Liouville'a otrzymujemy ω=dv+∑ c_j du_j/u_j; wyższe rzędy biegunów usuwają dv, a całkowite residua i niezależność współczynników c_j nad Q usuwają całą część logarytmiczną. Sprzeczność ω=0. Nie wykorzystywano fałszywego stwierdzenia, że sam brak residuów wymusza zerowość formy.
9. **Przykłady dodatnie i granice:** podano elementarne funkcje pierwotne dla x e^{-x²}, x e^{x²}, e^x(1/x-1/x²), 1/(x log x) oraz ogólnie dla funkcji wymiernych; pokazano niedopuszczalność automatycznego pomijania hipotezy o stałych.

Rozdział AA-45 ma 12 środowisk dowodu, 5 przykładów i 25 etykiet (różnica między danymi bramek AA-44 a AA-45).

## 2. Faktycznie wykonane poprawki

W audytach ch45_iteration_01.md i ch45_iteration_02.md przeprowadzono kontrolę logiczną i niezależną kontrolę przypadków brzegowych. Zastąpiono tautologiczne asercje w testach rzędów rzeczywistymi granicami przy rozgałęzieniach, rachunkami w obu punktach nad nieskończonością oraz kontrolą współczynników residuów względem Q-niezależnych stałych (1,√2). Pozostawiono rozdzielne modele SymPy i Fraction bez zależności od SymPy w drugim zestawie.

## 3. Potwierdzony końcowy przebieg CI

**GitHub Actions:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154562082
**Head SHA:** 9a375ac376c90e04d6ec8b3172a224afd7551572.
**Wynik:** completed / success, 81/81 zakończonych sukcesem kroków zadania.

- Testy AA-45 na SymPy: 10/10 PASS.
- Niezależne testy AA-45 na liczbach wymiernych: 8/8 PASS.
- Bramka AA-GLOBAL 01–45: PASS — 45 rozdziałów, 909 unikatowych etykiet (0 duplikatów), 432 wystąpienia odsyłaczy, 275 unikatowych celów (0 braków), 422 środowiska dowodu i 287 przykładów.
- Historia audytów przekrojowych AA-01–AA-42 pozostała zamknięta (11 raportów); AA-43, AA-44 i AA-45 mają osobne raporty.
- Pełna kompilacja latexmk i weryfikacja PDF: success.

## 4. Końcowy artefakt i oględziny

**Artefakt:** abstract-algebra-aa01-aa45, ID 14808277385.
- PDF: 289 stron, 2 135 269 bajtów; SHA-256 f3612f1289fca7a9ef34d1be26f449058e5a41d52a445cd5d9f0bfd2eaca6e51.
- Log: 45 741 bajtów; SHA-256 2cf4e0f008a447edd23855e45b5ae09880f5b51ab5a0f34e7c7e5927c4f50331.
- Końcowy log: 0 błędów LaTeX, 0 ostrzeżeń LaTeX/hyperref, 0 overfull/underfull, 0 nierozwiązanych odsyłaczy.
- Nowy AA-45 zajmuje strony PDF 282–289 (drukowane 273–280). Każda z ośmiu stron została wyrenderowana i obejrzana; nie wykryto obcięć, nakładania tekstu ani nieprawidłowych bloków wzorów.
- 150 057 słów w całej książce, 0 pozycji poza granicami stron (skan pierwszego zakończonego artefaktu).
- Ostateczny PDF różni się binarnie od pierwszego udanego artefaktu, ale ma 289/289 identycznych warstw tekstowych i 289/289 identycznych stron pikselowo przy renderowaniu 0,7×; ostatnie poprawki testów nie zmieniły składu.
- W porównaniu ze stabilną AA-01–AA-44 stwierdzono 279/281 wcześniejszych stron pikselowo identycznych; zmieniły się wyłącznie strona tytułowa i odpowiednia strona spisu treści.

## 5. Decyzja

**AA-45 STABILNY.** Wszystkie założone warunki osiągnięto: dwa niezależne przeglądy dowodów, rzeczywiste korekty testów, oba zielone zestawy regresji, integralność książki i katalogu, pełny końcowy CI, bezbłędny log i kompletna wizualna kontrola nowych stron. Testy obliczeniowe są regresją, nie formalnym dowodem wszystkich twierdzeń.

**Następny odblokowany rozdział: AA-46 — automorfizmy różniczkowe, rozszerzenia Picarda–Vessiota i grupy Galois równań liniowych.** Zasada pozostaje: jeden rozdział, audyty do stabilizacji, dopiero dalszy numer.
