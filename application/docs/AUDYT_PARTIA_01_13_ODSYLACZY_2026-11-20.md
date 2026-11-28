# Biblioteka matematyczna — audyt odsyłaczy, partia 01 (13 wystąpień)

**Stan odniesienia:** gałąź `biblioteka-matematyczna-iteracja-6`, commit `38daaeb1831734dc237399ba148336046231686e` (przed raportem); indeks 355 rozdziałów; `reference_provenance_audit_355.json` (odczytano 13 pierwszych wystąpień); 20 XI 2026.

**Zakres:** porównanie kontekstu cytowania z treścią odpowiednich `\label` w *kanonicznych* plikach `chapters/pl/` na GitHubie. Jest to **audyt integralności odsyłaczy**, **nie** scalenie skryptów, nie automatyczna deduplikacja i nie pełny audyt matematyczny tych rozdziałów. Żaden oryginalny plik TeX ani dowód nie został zmieniony.

**Zasada rozstrzygania:** gdy dwa skrypty mają to samo twierdzenie, preferowany jest cel w obrębie skryptu cytującego — o ile definicja i teza rzeczywiście odpowiadają cytowanemu użyciu. Powtórzenie twierdzenia nie upoważnia do jego usunięcia. Rozstrzygnięcie robocze wymaga późniejszej weryfikacji pojęć i zakresu zależności oraz kompilacji `xr-hyper`. `propozycja` nie jest wykonaną zmianą etykiety.

## Przypadki 1–13

| # | Cytujące miejsce | Etykieta | Wynik audytu i uzasadnienie | Proponowane działanie | Status |
|---|---|---|---|---|---|
| 1 | `ALG-10:240` | `tw:ga10-weak` | Dowód prostospójności gładkiej hiperpowierzchni w $\mathbb P^3$ wymaga homotopijnej wersji twierdzenia Lefschetza, dającej izomorfizm $\pi_1(S)\cong\pi_1(\mathbb P^3)$. W aktualnym indeksie brak deklaracji tej etykiety; samo twierdzenie nie może być zastąpione jego homologicznym odpowiednikiem. | Odszukać dokładne twierdzenie homotopijne (z założeniami) w materiale geometrii algebraicznej; jeśli jest, dopiero wtedy dodać/zmienić **odnośnik**, bez zmiany dowodu. | **nierozstrzygnięte** |
| 2 | `ALG-10:385` | `thm:xvii-blowup` | Uwaga wskazuje niezależny dowód wzoru $\chi(\widetilde S)=\chi(S)+1$ przez Mayera–Vietorisa. W aktualnym indeksie brak docelowej etykiety; rachunek przez addytywność charakterystyki jest odrębnym wariantem dowodu. | Odszukać dokładny wariant Mayera–Vietorisa i odtworzyć poprawny odsyłacz; **zachować oba rozumowania**. | **nierozstrzygnięte** |
| 3 | `DG-02:238` | `thm:poincare-hopf-16` | Oba cele, `DG-17:2236` i `TOP-11:2186`, mają tezę Poincarégo–Hopfa: suma indeksów izolowanych zer pola równa $\chi(M)$ (przy podanych założeniach). Użycie dotyczy braku pola nigdzie niezerowego na $S^2$; wystarczy wersja z tego samego skryptu. | **Preferować `DG-17`** jako docelowy rozdział w skrypcie geometrii różniczkowej. Rozważyć nazwę etykiety jednoznaczną w obrębie całej Biblioteki w przyszłym etapie integracji; dziś nie zmieniać źródeł. | **propozycja lokalna** |
| 4 | `DG-03:141` | `thm:modul-izomorfizm` | `DG-05:1183` zawiera pierwsze twierdzenie o izomorfizmie modułów z dowodem; `TOP-03:35` zawiera przypomnienie z odesłaniem do innych rozdziałów. Uwaga o faktoryzacji przez iloraz wymaga dokładnie izomorfizmu $M/\ker f\cong\mathrm{im} f$. | **Preferować `DG-05`**, gdzie twierdzenie jest szczegółowiej umotywowane i udowodnione; nie utożsamiać $F/R$ z obrazem bez $R=\ker L$. | **propozycja lokalna** |
| 5 | `DG-05:21` | `thm:van-kampen` | Wprowadzenie do prezentacji grup zapowiada twierdzenie van Kampena. `DG-07:1047` i `TOP-04:734` podają wersję dla dwóch zbiorów otwartych. | **Preferować `DG-07`** (przyszły rozdział tego samego skryptu); sprawdzić odsyłacz w kompletnym tomie, bez przenoszenia dowodu. | **propozycja lokalna** |
| 6 | `DG-05:406` | `thm:van-kampen` | Własność uniwersalna iloczynu wolnego jest używana w sformułowaniu van Kampena, a `DG-07` zawiera jego odpowiednią wersję. | **Preferować `DG-07`**, zachowując osobny dowód własności uniwersalnej w `DG-05`. | **propozycja lokalna** |
| 7 | `DG-05:514` | `thm:van-kampen` | Prezentacja $\pi_1(T^2)$ przez komutator krawędzi jest zapowiedzianym zastosowaniem van Kampena. Oba cele odpowiadają tej metodzie. | **Preferować `DG-07`**; dodatkowo sprawdzić w jego przykładzie torusa zgodność punktu bazowego i relacji. | **propozycja lokalna** |
| 8 | `DG-05:730` | `app:grupy-algebry-macierzowe` | Przykład klasyfikuje izometrie euklidesowe i kieruje do dodatku o grupach macierzowych. W aktualnym indeksie etykieta dodatku nie istnieje. Nie wiadomo, czy dodatek został przeniesiony, przemianowany, czy jest planowany. | **Nie tworzyć fikcyjnego dodatku**; znaleźć istniejącą sekcję z grupami Liego/macierzy lub zaznaczyć brak w spisie przyszłych uzupełnień. | **nierozstrzygnięte** |
| 9 | `DG-06:19` | `sec:moduly` | `DG-05:953` wprowadza pierścień, moduły, homomorfizmy i ilorazy w ramach tego samego skryptu; `TOP-03:16` jest skrótowym przypomnieniem; raport wskazuje także `ALG-04`. Kontekst wymaga dokładnie ustalenia $R$-modułów i $\operatorname{Hom}_R$. | **Preferować `DG-05`**. Nie usuwać wersji topologiczno-algebraicznej; weryfikować lokalnie definicję pierścienia przemiennego z jedynką. | **propozycja lokalna** |
| 10 | `DG-06:85` | `thm:modul-izomorfizm` | Z dokładności $0\to A\xrightarrow i B\xrightarrow p C\to0$ wynika $\ker p=i(A)$ i $p$ jest surjekcją. Zatem pierwsze twierdzenie o izomorfizmie daje $B/i(A)\cong C$, jak w `DG-05:1183`; odpowiednik `TOP-03:35` także działa. | **Preferować `DG-05`**; przy przyszłym audycie wyraźnie nazwać utożsamienie $A\simeq i(A)$ wymagające iniektywności $i$. | **propozycja lokalna** |
| 11 | `DG-06:1659` | `def:torsja` | Wzór $H_{n-1}(C)[m]=\{x:mx=0\}$ używa dokładnie $m$-torsji. Obie definicje: `DG-05:1000` oraz `TOP-03:24`, rozróżniają torsję całkowitą od $m$-torsji. | **Preferować `DG-05`**; zachować warunek $m\ge2$ tam, gdzie odsyłacz do tej definicji jest używany. | **propozycja lokalna** |
| 12 | `DG-07:5` | `ch:algebra-homologiczna` | Zdanie odwołuje się wprost do wcześniej wprowadzonego kompleksu łańcuchowego. Kandydaci `DG-06` i `TOP-03` obejmują ten sam temat; `DG-06:1–14` jest poprzednim rozdziałem skryptu geometrii. | **Preferować `DG-06`**, bez przenoszenia ani skracania wywodu w `TOP-03`. | **propozycja lokalna** |
| 13 | `DG-07:16` | `def:homotopia-lancuchowa` | `DG-06:965` i `TOP-03:818` definiują homotopię łańcuchową przez $f-g=\partial h+h\partial$. W cytowanym zdaniu przeciwstawiono ją homotopii topologicznej, więc oba pojęcia muszą pozostać rozdzielone. | **Preferować `DG-06`**; podczas przyszłego audytu zachować indeksowanie i rozróżnienie homotopii topologicznej od łańcuchowej. | **propozycja lokalna** |

## Licznik i granice weryfikacji

- **13 wystąpień** z pełnego raportu (w tym **3 brakujące** oraz **10 niejednoznacznych**).
- **10 propozycji celu w tym samym skrypcie**, oparte na kontekście i sprawdzonych deklaracjach; nie są automatycznymi zmianami.
- **3 nierozstrzygnięte braki**, których nie wolno naprawiać poprzez zgadywanie nazwy.
- Sprawdzono źródła wywołujące i odpowiednie deklaracje w `chapters/pl/`; **nie** audytowano w tej partii całych dowodów ani nie wykonywano kompilacji TeX.
- Pozostaje **244 wystąpienia** do szczegółowego przeglądu według tej migawki (257 − 13).

## Reguły dalszej pracy i przyjęty plan długoterminowy

1. **Teraz:** kompletować od podstaw wszystkie działy matematyki; prowadzić audyt poprawności odsyłaczy i granularności dowodów *wewnątrz każdego niezależnego skryptu*. Nie scalać obecnie modułów różnych działów, nie deduplikować twierdzeń, nie kasować wariantów dowodów.
2. **Później, po skompletowaniu działów:** zaplanowane przez użytkownika scalanie w kolejności od podstaw matematyki ku kolejnym gałęziom; zachować sumę niepowtarzalnych treści, wszystkie alternatywne dowody, przykłady, rysunki i mapę pochodzenia.
3. **Przy wprowadzaniu zmian etykiet:** sprawdzać nie tylko składnię, ale tożsamość matematyczną cytowanej tezy i dokładne założenia. Zachować standard `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` oraz dokładną granularność wzorcowego rozdziału 01 geometrii różniczkowej.

## Następna partia

Przejrzeć wystąpienia 14–26 pełnego raportu, a po zakończeniu przeglądu przygotować **osobną, kontrolowaną poprawkę nazw odsyłaczy w obrębie skryptów**, tylko dla przypadków jednoznacznie zweryfikowanych matematycznie. Nie mylić tej poprawki z docelowym scalaniem całych działów.