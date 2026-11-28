# Analiza funkcjonalna — rozdział 07 — audyt 02 (niezależna kontrola)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex`.  
**SHA źródła:** `914059e1b20f1a9a3a8766a899659cde32109fb7`, zgodny z audytem 07/01.  
**Werdykt:** **CZYSTY audyt 07/02, 1/2** kolejnych czystych audytów; rozdział **NIE STABILNY**. Nie zmieniono źródła.

## Ustalenie aktualnego punktu

Odczytano rzeczywisty katalog `audits/functional_analysis` na wskazanej gałęzi. Rozdział 06 jest zamknięty raportem `06-audyt-4.md` (2/2), a najnowszy raport rozdziału 07 to `07-audyt-1.md`, który zawiera poprawki i reset licznika 0/2. Przed rozpoczęciem tej iteracji nie było raportu `07-audyt-2.md`. Odczytano ponownie źródło 07, testy `tools/tests/test_functional_analysis_ch07.py` i workflow `.github/workflows/functional-analysis-ch07.yml`.

## Niezależna kontrola wszystkich 11 dowodów

1. **Reprezentacja rzeczywiście liniowego funkcjonału przez część rzeczywistą:** `F(x)=ell(x)-i ell(ix)`; sprawdzono zespoloną liniowość, ciągłość i jednoznaczność.
2. **Niesymetryczny funkcjonał Minkowskiego:** jawne uzasadnienie `x∈rV` dla `r>p_V(x)`, dodatniej jednorodności, podaddytywności i równości `V={p_V<1}`. Ciągłość wymaga obu otoczeń `epsilon V` i `-epsilon V`; oba występują w tekście.
3. **Separacja otwartego zbioru od punktu:** `p_V(-a)≥1` i `g(t(-a))=t` dla dodatnich i ujemnych `t` uzasadniają dominację, zaś `ell(d-a)<1` daje ścisłą nierówność punktową, nie jednolitą lukę.
4. **Separacja dwóch zbiorów:** otwartość `A-B`, wypukłość i brak zera oraz ograniczenia `sup_A ell` i `inf_B ell` wynikają z ustalenia punktów w przeciwnych zbiorach.
5. **Wspólne otoczenie zbioru zwartego:** kontrola `W_k+W_k⊂V_k`, skończonego podpokrycia i wyboru wspólnego `U`. Zwartość nie wymaga metryzowalności.
6. **Silna separacja:** niezerowość `ell` i otwartość `U` gwarantują `u_0∈U` z `ell(u_0)>0`; przejście od nierówności dla wszystkich punktów do supremum/infimum jest poprawne.
7. **Punkt poza domkniętym zbiorem wypukłym:** zastosowanie poprzedniego wyniku do zwartego singletonu i niepustego domkniętego zbioru.
8. **Hiperpłaszczyzna podpierająca:** `(1-t)x+tg_0∈int C` dla `0<t≤1`, dzięki `x_t+tV⊂C`; granica dla `t↓0` daje nierówność nieostrą.
9. **Własności polary:** antymonotoniczność, równość polar po absolutnie wypukłej otoczce, zawieranie `A⊂A°°`, wypukłość, zrównoważenie i domkniętość jako przecięcia poziomic.
10. **Twierdzenie bipolarne:** sprawdzono zastosowanie silnej separacji do `C=cl(aco A)`, reprezentację `ell=Re F`, równość supremów po zrównoważonym `C` oraz oddzielne normalizacje przy `m>0` i `m=0`. Przypadek `A=∅` obsługuje konwencja `aco(∅)={0}`.
11. **Zgodność domknięć wypukłych:** półprzestrzeń określona przez `Re F` jest otwarta w `sigma(X,X')`; osobno przypadek pustego zbioru.

**Wynik przeglądu matematycznego: 11/11 dowodów bez wykrytej usterki.** Kontrola ma charakter matematycznej lektury, nie formalnej weryfikacji dowodów.

## Kontrola 4 przykładów

1. `A=(-1,0)`, `B={0}`: ścisła separacja punktowa bez dodatniej luki.
2. Polara kuli `ell^1` w `R²`: supremum funkcjonału równe normie `ell^infty`; diagram TikZ zachowany.
3. Produkt `K^N`: ciągłe funkcjonały o skończonym nośniku, supremum skończonych sum modułów, domknięcie przez obcięcia.
4. `L^p([0,1])`, `0<p<1`: trywialna przestrzeń sprzężona, kontrprzykład do twierdzenia bipolarnego bez lokalnej wypukłości.

**Wynik lektury przykładów: 4/4 bez wykrytej usterki.**

## Odsyłacze, LaTeX, CI

- Audyt 07/01 udokumentował 17 unikatowych etykiet i 12 odsyłaczy z rozpoznanymi celami w rozdziałach 01–07; obecne źródło ma ten sam blob SHA.
- W workflow jest 16 testów regresyjnych oraz budowa dokumentu kontekstowego 01–07, kompilacja LaTeX, sprawdzenie logu/odsyłaczy/PDF i zapis artefaktu.
- **Zweryfikowano bezpośrednio GitHub API:** [run 45182375122](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45182375122), `status=completed`, `conclusion=success`, `head_sha=50e5191a39bd78408513ac4ae8d954375bf51b20`, `updated_at=2026-11-23T13:19:07Z`. Dla job `audit-ch07` każdy etap: testy, przygotowanie dokumentu, kompilacja, walidacja PDF i odsyłaczy, archiwizacja — **conclusion=success**.
- **Nie uruchomiono w tej iteracji nowych testów ani kompilacji** i **nie przeprowadzono nowej wizualnej inspekcji stron PDF**. Sukces kroku automatycznej walidacji PDF nie jest tożsamy z oglądem wizualnym.

## Werdykt

**Audyt 07/02 czysty: 11/11 dowodów i 4/4 przykłady sprawdzone; 1/2 czystych audytów po poprawkach 07/01.** Brak podstaw do modyfikacji źródła lub resetu licznika. Następna iteracja: **niezależny audyt 07/03**, z kontrolą aktualnego SHA, wyniku CI i — jeśli możliwe — stron PDF; dopiero po drugim czystym audycie i wymaganych kontrolach można uznać rozdział za stabilny. Nie rozpoczynać rozdziału 08.
