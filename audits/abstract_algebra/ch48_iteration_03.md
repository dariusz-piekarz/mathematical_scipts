# AA-48 — audyt III: końcowa stabilizacja pierwszej gałęzi algorytmu Kovacica dla dowolnego potencjału wymiernego

**Data:** 23 listopada 2026 r. **Werdykt: AA-48 STABILNY w ściśle określonym zakresie.**
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/abstract_algebra/48-wymierna-galaz-kovacica-dla-potencjalow-wymiernych.tex.
**Blob SHA rozdziału:** 85ba5bd7f2d4c0de04f1184f3fb0c3602c9b9785.
**Blob SHA testów SymPy:** f88cf2427e33467b883b05b4a5cc4e69f6cef903.
**Blob SHA testów niezależnych Fraction:** d498de536d015fe42cce8f52df6bd32169c1d951.
**Dokument zakresu:** docs/pl/zakres_aa48_kovacic_wymierny.md.
**Poprzedni stabilny rozdział:** AA-47 — algorytmy Rischa i Kovacica.

## 1. Wykonane trzy audyty merytoryczne i rzeczywiste poprawki

- **Audyt I:** audity/abstract_algebra/ch48_iteration_01.md (faktyczna ścieżka: audits/abstract_algebra/ch48_iteration_01.md). Przygotowanie pełnego dowodu pierwszej gałęzi Kovacica przy q∈C(x); niezależne przypadki skończonych biegunów oraz trzy przypadki przy nieskończoności. W trakcie pierwszej kontroli doprecyzowano lemat o pierwiastkach wielokrotnych: do jego poprawności potrzebna jest regularność **obu** funkcji u i q w badanym punkcie; commit 248882b5b634b24374f1cccc240bba06b32aa65b.
- **Audyt II:** audits/abstract_algebra/ch48_iteration_02.md. Niezależnie przeliczono lokalne szeregi Laurenta, wpływ R na stopień n, przypadek q=0, dodatnie i negatywne przypadki wysokich biegunów oraz dodatkowe warunki P(a)≠0 dla każdego bieguna q.
- **Rzeczywiste uzupełnienie po audycie II:** dodano przykład z biegunem ustalonym i ruchomym: q=x²−8x+23−16/(x−1)+2/(x−1)², u=x−4+2/(x−1), P=x−2, r=u+P'/P. Sprawdzono dokładnie r'+r²=q i P(1)≠0 oraz dodano test SymPy. Commit e7e60105f9db8e73f0b42525a297ad5ef004dfd3.
- **Audyt III:** ponownie oceniono wszystkie wnioski po poprawkach oraz wyniki pełnego CI i ostatecznego PDF, już po ujednoliceniu statusu na stronie tytułowej.

## 2. Kontrola wszystkich głównych zobowiązań dowodowych

1. **Klasyfikacja lokalna.** Dla r'+r²=q, biegun r rzędu m≥2 wymusza biegun q rzędu 2m, gdyż r² ma część wiodącą z^{-2m}, a r' ma rząd m+1<2m. Dla prostego bieguna r współczynnik z^{-2} wynosi c(c−1); w punktach regularności q niezerowe c musi być równe 1.
2. **Wysokie bieguny.** Każdy biegun q nieparzystego rzędu ≥3 wyklucza wymierne r. Dla q o biegunie parzystym 2m≥4 możliwe części główne r mają co najwyżej dwa znaki wiodącego współczynnika. Wszystkie kolejne współczynniki wyznacza jednoznacznie trójkątna rekurencja, ponieważ mnożnik niewiadomej wynosi 2c_{−m}≠0. Dla bieguna q rzędu 1 część główna r to dokładnie (x−a)^{-1}; dla rzędu 2 rozwiązujemy równanie kwadratowe c(c−1)=β.
3. **Rozkład globalny.** Po odjęciu skończonych części głównych R ze wszystkich biegunów q, pozostałe bieguny r leżą w punktach regularności q, mają rząd 1 i residuum 1, zatem tworzą pochodną logarytmiczną P'/P, gdzie P jest unormowany, bez pierwiastków wielokrotnych i nie ma zer na zbiorze S biegunów q. Pozostała część r jest wielomianem ω.
4. **Linearyzacja.** Z r=ω+R+P'/P po podstawieniu i skasowaniu kwadratów pochodnych logarytmicznych wynika dokładnie równanie liniowe P''+2uP'+(u'+u²−q)P=0, gdzie u=ω+R. Jego poprawność sprawdzono w obie strony.
5. **Nieskończoność.** Gdy wielomianowa część q ma stopień dodatni, koniecznie parzysty 2d, możliwe są dwa wielomiany ω stopnia d; z asymptotyki P'/P=n/x+O(x^{-2}) otrzymujemy n przez porównanie przy x^{d−1}, z uwzględnieniem składnika R. Gdy q ma niezerową granicę c, ω=±√c i n wynika z współczynnika przy x^{-1}. Gdy q→0, ω=0, koniecznie q=O(x^{-2}), a n jest nieujemnym całkowitym rozwiązaniem (n+ρ)(n+ρ−1)=β.
6. **Warunek nietrywialny na P.** Dla danej gałęzi dodatkowo trzeba wymagać P(a)≠0 w punktach S. Samo liniowe ODE nie wystarcza: dla q=2/x², u=−1/x, P=x³ spełnia ODE, lecz zeruje się w 0. Natomiast P=x³+1 także spełnia ODE i nie zeruje się w 0, więc jest dopuszczalny. Test ogólny sprowadza wybór do usunięcia skończonej sumy właściwych hiperpłaszczyzn z afinicznej przestrzeni rozwiązań; nad nieskończonym ciałem nie pokrywają one całej przestrzeni.
7. **Zupełność.** Wszystkie wymierne r wchodzą do jednej z enumerowanych list części głównych i do jednej z możliwości (ω,n); odpowiadające im P spełnia rozpatrywany układ i wymagane nierówności. Każda dodatnia gałąź daje rzeczywiste rozwiązanie r'+r²=q. Procedura kończy się po skończenie wielu rozgałęzieniach algebraicznych, równaniach kwadratowych i skończonych liniowych układach.
8. **Granice interpretacji.** Pełne rozstrzygnięcie dotyczy wyłącznie **wymiernych** r∈C(x). Nie należy z negatywnego wyniku tej gałęzi wyciągać wniosku o braku wszystkich rozwiązań liouvillowskich: kontrprzykład q=x+5/(16x²), r=√x−1/(4x) ma rozwiązanie algebraiczne stopnia drugiego. Pozostałe gałęzie Kovacica stopni 2, 4, 6, 12 nadal pozostają osobnym, cytowanym wynikiem ogólnym (AA-47).

**Rozdział AA-48 po ostatniej poprawce:** 6 środowisk dowodu, 6 przykładów, 23 etykiety. Wnioski te opierają się na dowodach matematycznych; skończone regresje nie zastępują dowodów.

## 3. Końcowe potwierdzenie GitHub Actions

**Ostateczny przebieg na źródłach oraz z właściwą stroną tytułową:**
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45172784971

**Head SHA przebiegu:** 666027e7fd7764ade14c38fc5ac8518b4f04bf4d.
**Status:** completed / success, **88/88 zakończonych sukcesem kroków**.

- AA-48 regresje symboliczne (SymPy): **12/12 PASS**;
- AA-48 niezależny dokładny model Laurenta (fractions.Fraction): **9/9 PASS**;
- bramka AA GLOBAL 01–48: **PASS** — 48 kanonicznych rozdziałów; 992 unikatowe etykiety, 0 duplikatów; 501 wystąpień odsyłaczy, 314 różnych celów, 0 brakujących celów; 441 środowisk dowodu i 306 przykładów;
- historyczne przekrojowe 11 raportów AA-01–AA-42 pozostają odrębne od cyklu AA-43–AA-48;
- pełne testy narzędzi repozytorium: PASS; kompilacja latexmk całej książki: PASS; weryfikacja PDF i archiwizacja: PASS.

## 4. Ostateczny artefakt PDF i oględziny

**Artefakt ostatecznego CI:** abstract-algebra-aa01-aa48, ID **14816773809**.
- PDF: **310 stron**, **2 246 332 B**, SHA-256 **51248ef9f1e3b5e628994a97bcb58682d7a8eaa7b10abd7bf69e8db1dc77284c**.
- Log: **46 453 B**, SHA-256 **58b70794751d633561a49cc6421045ea6553a3e17e8fc28360cbfa990c675fd6**.
- Ostateczny log: **0** błędów LaTeX, **0** ostrzeżeń LaTeX, **0** hyperref warnings, **0** Overfull/Underfull hbox/vbox, **0** nierozwiązanych odsyłaczy.
- Nowy AA-48 obejmuje **6 stron PDF: 305–310**, drukowane 295–300. Każda z sześciu stron została wyrenderowana i obejrzana w pełnej książce. Bez kolizji napisów, obcięć, problemów ze wzorami lub nieprawidłowego składu.
- W całej książce analizowano położenie **159 387 wyrazów**; **0** poza granicami stron.
- Porównanie artefaktu po korekcie strony tytułowej z ostatnim przebiegiem sprzed korekty: **309/310 stron tekstowo identycznych**. Zmieniono wyłącznie stronę 1 z opisem stanu książki; treść rozdziałów nie była po tej weryfikacji modyfikowana.
- Porównanie poprzedniej stabilnej wersji AA-01–AA-47 (304 strony) z AA-01–AA-48: **302/304 dotychczasowych stron tekstowo identyczne**; różnice to strona tytułowa i spis treści, co jest naturalnym skutkiem dołączenia nowego rozdziału.

## 5. Ostateczny werdykt

**AA-48 STABILNY w przyjętym, w pełni udowodnionym zakresie.** Zakończono audyty I–III, poprawki wynikłe z nich, 21 testów w dwóch odrębnych modelach, globalną integralność, pełny zielony CI, log i wizualną kontrolę wszystkich sześciu stron. Pełne algorytmy Kovacica stopni wyższych niż 1 nie są objęte tym werdyktem.

**AA-49 NIEOTWARTY.** Jego zakres wymaga odrębnej decyzji; nie uruchamiać automatycznie następnego rozdziału.
