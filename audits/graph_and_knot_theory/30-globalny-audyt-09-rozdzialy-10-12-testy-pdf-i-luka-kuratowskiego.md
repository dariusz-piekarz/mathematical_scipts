# Teoria grafów i węzłów — audyt globalny 09: rozdziały 10–12, wynik regresji i blokada pełnej stabilizacji

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.

## Werdykt

**PASS**: niezależne skończone modele rozdziałów 10–12; kompletna integracja 44 rozdziałów; pełna 263-stronicowa kompilacja PDF bez ostrzeżeń i przepełnień.

**OPEN**: pełna stabilizacja matematyczna rozdziału 10. Trudna implikacja twierdzenia Kuratowskiego pozostaje przyjętym i opisanym faktem z literatury, a nie dowodem opracowanym w skrypcie. W zgodzie z regułą szczegółowych dowodów ten fragment nie może być poświadczony jako samodzielnie zweryfikowany. Kryterium Wagnera jest sformułowane prawidłowo, ale w tekście wyprowadzone dopiero po przyjęciu pełnego twierdzenia Kuratowskiego. Uzupełnienie brakującego pełnego dowodu, z własnym audytem, pozostaje obowiązkowym kolejnym krokiem.

**Nie zmieniono globalnego statusu** 44-rozdziałowej książki: audyt całego tomu nadal trwa.

## Pliki i zmiany

- \`chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex\`: dodano i udowodniono lemat o wierzchołku stopnia ≤2 w grafie zewnętrznie planarnym poprzez triangulację wielokąta i drzewo trójkątów. Wyprowadzono pełne twierdzenie o trzykolorowalności prostych grafów zewnętrznie planarnych. Zdefiniowano przypadek grafu pustego i umieszczono nowe wyniki po definicji poprawnego kolorowania.
- \`chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex\`: skontrolowano genus z układów rotacji, dualność sferyczną i obliczenie rzędu operatorów brzegowych; dowody źródłowe bez koniecznych zmian w tej iteracji.
- \`chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex\`: sprawdzono rekurencję Tutte'a, wzory chromatyczne, dualność Tutte'a i przepływ–kolorowanie; dowody źródłowe bez koniecznych zmian w tej iteracji.
- \`tools/tests/test_graph_and_knot_planar_surface_tutte.py\`: nowy niezależny test dokładnych modeli; włączony do \`.github/workflows/graph-and-knot-global-audit.yml\`.

Commity:
- [13b021bb0b19b38191ede30b8f892ecf5c27b6a4](https://github.com/dariusz-piekarz/mathematical_scipts/commit/13b021bb0b19b38191ede30b8f892ecf5c27b6a4): dowody i pierwsza wersja testów;
- [5aa9304c1d5dbced7b5320448075f30a399b1b50](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5aa9304c1d5dbced7b5320448075f30a399b1b50): korekta niezależnego testu dualności, zachowująca przypisanie \`e ↔ e*\` dla każdej pierwotnej krawędzi.

## Rzeczywiste wyniki CI

[GitHub Actions — końcowy audyt globalny 45161627919](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161627919):
- \`structural-audit = success\`;
- \`full-book-pdf = success\`.

Wszystkie historyczne testy 01–09 przeszły ponownie. Nowy test:
- **1100** grafów prostych (0–5 wierzchołków) dla Tutte'a, specjalizacji drzewa/lasu i porównania rekurencji z enumeracją wszystkich podzbiorów krawędzi;
- **3300** bezpośrednich enumeracji kolorowań, porównanych z włączeniami i wyłączeniami oraz specjalizacją Tutte'a;
- **715** spójnych grafów w przedziale 2–5 wierzchołków o maksymalnie siedmiu krawędziach;
- **5784** orientowalne układy rotacji; kontrola \`∂1∂2=0\`, \`rank ∂1=n−1\`, \`rank ∂2=f−1\`, \`dim H1=2g\`;
- dla **715** wybranych sferycznych osadzeń: dualność \`T_{G*}(x,y)=T_G(y,x)\`, komplementarność drzew rozpinających i równość \`P_{G*}(q)=q F_G(q)\` przy \`q=2,3\`;
- **715** grafów sprawdzonych pod kątem zewnętrznej planarności; wśród nich **644** z osadzeniem zewnętrznie planarnym, zweryfikowana nierówność \`m≤2n−3\` i dokładna trzykolorowalność;
- przypadki kontrolne: theta na sferze/torusie, \`K5\`, \`K3,3\`, \`K4\`, \`K2,3\` i koło z sześcioma wierzchołkami.

Pierwszy przebieg [45161412117](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161412117) **nie przeszedł** z powodu błędu nowego testu: sortowanie sekwencji krawędzi dualnych zmieniało indeksy, przez co test dopełnienia drzew porównywał niewłaściwe pary. Ten problem nie oznaczał kontrprzykładu do twierdzenia o dualnym drzewie rozpinającym. Został jawnie naprawiony w [5aa9304](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5aa9304c1d5dbced7b5320448075f30a399b1b50); ponowny [45161627919](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161627919) przeszedł w całości.

Dla pierwszego commita również:
- [Polish mathematical terminology 45161412070](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161412070): success;
- [Graph and knot theory — algorithms audit 45161412157](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161412157): success;
- [Mathematical library application checks 45161412085](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161412085): success.

## Kontrola rzeczywistego PDF

Pobrano końcowy artefakt GitHub Actions i skontrolowano:
- **263 strony A4** pełnej książki, trzykrotna kompilacja \`pdflatex\`, końcowy plik \`graph_and_knot_full_warnings.txt\` pusty;
- nowo audytowany rozdział 10 na stronach PDF 102–105, rozdział 11 na 106–110 i rozdział 12 na 111–115;
- wygenerowano i obejrzano kontaktowy zestaw stron 103–105, 108–110, 112–115 w powiększeniu umożliwiającym ocenę ogólnego układu;
- w kontrolowanych stronach nie stwierdzono przekroczeń marginesów ani kolizji głównych rysunków i ich podpisów. Ta inspekcja wybranych stron nie stanowi pełnego audytu każdego elementu wszystkich 263 stron.

## Pozostałe wymagania przed pełną lokalną stabilizacją rozdziału 10

1. Przygotować samodzielny, szczegółowy dowód implikacji Kuratowskiego \`(ii) ⇒ (i)\` lub jawnie zatwierdzić inny rygor dowodu dla tej wielkiej klasycznej tezy; domyślną regułą projektu jest pełen dowód.
2. Zweryfikować niezależnie wszystkie nowe lematy użyte w ewentualnym dowodzie oraz jego przypadki rozspójnione, separatory i grafy wielospójne.
3. Ponowić globalny audyt, testy skończone, pełny skład PDF i kontrolę grafiki.

**Następny krok nie powinien pomijać tego otwartego obowiązku**. Matematyka rozdziałów 11–12 przeszła wskazaną kontrolę, lecz blok 10–12 jako całość nie jest jeszcze w pełni ustabilizowany względem przyjętej zasady samodzielnych szczegółowych dowodów.
