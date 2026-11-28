# Analiza funkcjonalna — rozdział 11 — audyt 04 (drugi niezależny przegląd stabilizacyjny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (istniejąca, bez tworzenia nowej).  
**Źródło:** `chapters/pl/functional_analysis/11-przestrzenie-frecheta-twierdzenia-o-odwzorowaniu-otwartym-i-wykresie-domknietym.tex`.  
**Blob SHA źródła:** `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2` — niezmieniony względem audytów 11/02 i 11/03.  
**Werdykt:** **CZYSTY 2/2 — rozdział 11 stabilny matematycznie i redakcyjnie, przy zielonej potwierdzonej bramce CI tego samego źródła**. Nie zmieniano źródła, testów ani workflow.

## Odczyt stanu i unikanie powtórzeń

Przed audytem pobrano katalog raportów: najnowszy to `11-audyt-3.md` (CZYSTY 1/2). Sprawdzono `11-audyt-2.md` z poprawkami i pierwszą kompilacją, `11-audyt-3.md` z pierwszą niezależną kontrolą. Odczytano ponownie źródło rozdziału 11 i wszystkie źródła 01–11. Potwierdzono bezpośrednio przez GitHub API rzeczywisty workflow [#45232838912](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45232838912): `completed/success`, commit `913bd489f933b22da4e47e95c902d88330dcb924`, aktualizacja 2026-11-23 17:57:24 UTC. Job `audit-ch11` i wszystkie jego kroki mają `success`: testy, kontekst 01–11, kompilacja LaTeX, kontrola PDF i odsyłaczy, publikacja artefaktu. To **wcześniej zakończone CI**, nie nowy przebieg z tego audytu.

## Druga niezależna kontrola 10 dowodów

1. Metryka Frécheta z przeliczalnej rodziny seminorm: sprawdzono skończoność szeregu, dodatnią określoność przez rozdzielanie punktów, nierówność trójkąta, równoważność zbieżności sieci i warunków Cauchy'ego.
2. Stabilność klasy Frécheta: domknięta podprzestrzeń jest zupełna; dla ilorazu infimum po klasie jest niezależne od reprezentantów i dodatnio określone dzięki domkniętości; wybór reprezentantów Cauchy'ego z summowalnymi odległościami daje granicę; przeliczalny produkt jest zupełny współrzędnie.
3. Lemat Baire'a: surjektywność i pochłanianie dają przeliczalne pokrycie; własność Baire'a wymusza niepuste wnętrze domknięcia; wypukłość i zrównoważenie przenoszą wnętrze do zera.
4. Odwzorowanie otwarte: dla malejących otoczeń `U_n` i `V_n` gęstość obrazów pozwala wybrać korekty `x_n`; reszty dążą do zera; inkluzja `U_n+U_n\subset U_{n-1}` zapewnia Cauchy'ego sum częściowych; zupełność dziedziny i ciągłość operatora kończą argument.
5. Ciągłość odwrotności: otwartość liniowej bijekcji jest dokładnie ciągłością jej odwrotności.
6. Oszacowanie odwrotności Banacha: ograniczoność liniowego operatora ciągłego i wybór dodatniej stałej działają również dla przestrzeni zerowej.
7. Izomorfizm ilorazu: domkniętość jądra, ciągłość operatora indukowanego i kompletność hipotez twierdzenia o odwrotności.
8. Kryterium ciągowe domknięcia wykresu: metryzowalność produktu zapewnia równoważność z zachowywaniem granic ciągów; jawna pełna dziedzina operatora.
9. Twierdzenie o wykresie domkniętym: domknięta podprzestrzeń produktu Frécheta, ciągła bijekcja rzutowania i zastosowanie twierdzenia o odwrotności.
10. Równoważność dwóch zupełnych norm: identyczność między Banachami i ciągłość odwrotności zapewniają oszacowanie w przeciwną stronę.

**Dowody: 10/10 skontrolowanych, bez nowej luki wymagającej korekty.** Kontrola jest matematycznym przeglądem argumentacji, nie formalnym dowodem w Lean.

## Kontrola sześciu przykładów

1. `K^N` i `C^\infty([0,1])`: sprawdzono granice współrzędnych i przejście do granicy pod całką, dające zgodność granic pochodnych.
2. Niezupełna przeciwdziedzina `(\ell^1,\|\cdot\|_2)`: wektory o pierwszych `n` współrzędnych `1/n` dowodzą nieciągłości odwrotności.
3. Niezupełna dziedzina: wykres odwrotnej identyczności jest domknięty przez jednoznaczność granic w `\ell^2`, mimo nieciągłości.
4. Nieograniczona pochodna na `C^1\subset C`: `n^{-1}\sin(nt)` i tożsamość całkowa pokazują nieograniczoność oraz domkniętość wykresu.
5. Pochodna na `C^\infty`: oszacowanie `p_n(Df)\le p_{n+1}(f)`, prawa odwrotność całkowa i jądro funkcji stałych.
6. Gęsty niepełny obraz `\ell^1\hookrightarrow\ell^2`: gęstość `c_{00}`, brak surjektywności przez `(n^{-3/4})`.

**Przykłady: 6/6 skontrolowanych, bez korekt.**

## Niezależne kontrole strukturalne

Ponownie odczytano 11 źródeł. **202 etykiety, 202 unikatowe** w źródłach 01–11. W AA rozdziale 11 (tj. w analizie funkcjonalnej 11): **20 etykiet, 16 odsyłaczy, 0 brakujących celów**. Sparowano: 10 środowisk `proof`, 3 `twierdzenie`, 2 `stwierdzenie`, 1 `lemat`, 4 `wniosek`, 2 `definicja`, 6 `przyklad`, 4 `uwaga`, 1 `tikzpicture`, 1 `center`. Nie wykryto zakazanych terminów „sekwencyjny”, „zwartościowanie”, „tensorowanie”.

PDF (strony 61–66, w tym rysunek TikZ na 65) został już rzeczywiście obejrzany i opisany w audycie 11/02 dla **identycznego SHA źródła**. W tej iteracji nie pobierano ponownie artefaktu ani nie przeprowadzano nowej wizualnej inspekcji.

## Stabilizacja i ograniczenia

Wcześniejszy przebieg CI #45232838912 ma bezpośrednio potwierdzone `completed/success` dla wszystkich etapów. Nie przypisuje się takiego statusu żadnemu nowemu przebiegowi uruchomionemu przez zapis niniejszego raportu, dopóki nie zostanie zakończony i sprawdzony.

**Decyzja: drugi niezależny czysty przegląd 11/04 zamyka 2/2 dla identycznego źródła. Rozdział 11 STABILNY** w zakresie sprawdzonych bramek. Następna jednostka pracy to rozdział 12; nie otwierano go w tym audycie.
