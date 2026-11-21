# Audyt I rozdziału 02 — „Kwantyfikatory i podstawowe metody dowodzenia”

Data: 21 listopada 2026. Źródło: najnowsza wersja z Biblioteki matematycznej `/Biblioteka matematyczna/skrypty/logic_and_set_theory/chapters/02-quantifiers-and-proofs.tex` (wersja 4). Audyt dotyczy wyłącznie **poprawności istniejącego materiału**. Nie dodawano nowych twierdzeń, lematów ani przykładów. Przejrzano wszystkie sekcje, twierdzenia, dowody, przykłady i uwagi.

## I. Poprawione usterki (bez zmian tezy)

1. W początkowej definicji zaznaczono, że w tym intuicyjnym ujęciu dziedzina rozważań może być pusta, co jest ważne dla późniejszych przykładów ograniczonych kwantyfikatorów.
2. W definicji predykatu dwuargumentowego jawnie określono obie dziedziny, `D` i `E`; poprzednio `E` pojawiało się bez wprowadzenia. Przykład `R(x,y)` oparty na nierówności przypisano explicite do `D=E=\N`.
3. Zmienną wolną `x` nazwano zmienną wolną, zamiast używać mylącego określenia „wolny parametr”; doprecyzowano, kiedy ustalenie pozostałych wartości jest potrzebne.
4. W przykładzie z `x^2\ge 0` nad liczbami zespolonymi rozróżniono **brak ustalonej interpretacji `\ge`** od wartości logicznej **fałsz**.
5. W kontrprzykładzie pokazującym przechwycenie zmiennej poprawiono opis błędnej zamiany: obejmuje ona zarówno zewnętrzny kwantyfikator, jak i podlegające mu wystąpienie `x`.
6. Usunięto błędne dopasowanie rodzaju w „$D$ jest pusty” i we fragmencie o parzystości liczb `n` i `n+2`.
7. W dowodzie rozwinięcia `\exists!` poprawiono określenie miejsca, w którym występuje koniunkcja: jest w zakresie **kwantyfikatora egzystencjalnego**.
8. W introdukcji do indukcji uściślono, że **skończony** dowód nie może polegać na sprawdzeniu każdego z nieskończenie wielu przypadków oddzielnie.
9. Drobne ujednolicenie sformułowania początku dowodu jednoznacznego istnienia.

## II. Kontrola matematyczna

Sprawdzono wszystkie **6 twierdzeń**: przemianowanie zmiennej związanej (warunek świeżości nazwy), prawa de Morgana dla kwantyfikatorów (w tym pusta dziedzina), zamianę kwantyfikatorów jednego typu, jednostronną zamianę kwantyfikatorów różnych typów, rozwinięcie jednoznacznego istnienia oraz zasadę indukcji. Pierwszych pięć posiada w rozdziale dowody; zasada indukcji jest jawnie wprowadzona jako przyjęta własność `\N` z wyraźnie wskazanym przyszłym uzasadnieniem teoriomnogościowym. Nie znaleziono brakujących istotnych kroków w dowodach tych pięciu twierdzeń. Sprawdzono 28 przykładów i 12 uwag oraz 5 definicji.

Zewnętrzna zależność od elementarnej arytmetyki (dzielenie z resztą, skracanie ułamka, istnienie dodatniego pierwiastka z 2) pozostaje jawnie opisana jako używana wiedza, a nie wynik logiki. Dwukrotnie odróżniono puste zakresy kwantyfikatorów ograniczonych od niepustego uniwersum standardowej semantyki pierwszego rzędu.

## III. Sprawdzenia automatyczne i TeX

- Zachowano **39/39 etykiet**, bez duplikatów, **6/6 twierdzeń**, 5/5 definicji, 28/28 przykładów, 12/12 uwag oraz 5/5 dowodów. Żadna etykieta nie została przemianowana.
- Testy enumeracyjne: **689** kombinacji dziedzin i predykatów dla twierdzeń o zamianie kwantyfikatorów, **127** przypadków negacji kwantyfikatorów i **127** rozwinięcia `\exists!` (rozmiary dziedzin 0–6), 301 przypadków arytmetycznych. Wszystkie testy pozytywne. Sprawdzono również kontrprzykłady dla implikacji odwrotnej (201 przypadków).
- Kompilacja pełnego skryptu **44 rozdziałów**: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — kod 0, PDF **376 stron**. Łącznie 1075 unikatowych etykiet, 866 odsyłaczy, **0 brakujących** i **0 zdublowanych** etykiet, 0 `Overfull \hbox`. Trzy ostrzeżenia `Underfull \hbox` w pełnym skrypcie nie blokują kompilacji.
- Kompilacja lokalnego wydania z rozdziałami **01–02** na preambule repozytorium — kod 0, 20 stron, bez `Overfull \hbox`. Oczekiwane nierozwiązane odsyłacze do rozdziałów **09** (`ch:syntax-fol`) i **10** (`ch:semantics-fol`) dotyczą wyłącznie częściowo zaimportowanego repozytorium; w pełnej książce rozwiązują się poprawnie.
- Oględziny wszystkich **9 stron** wyciętego z pełnego składu PDF rozdziału 02: brak zauważonych nałożeń napisów i wad układu. Rozdział nie wymaga plików graficznych, wygenerowanego kodu ani innych zewnętrznych plików źródłowych.

## Status po iteracji I

Pierwszy audyt rozdziału 02 zakończony; znalezione błędy naprawiono. Weryfikacja nie stwierdziła dalszych znanych luk w istniejącym zakresie materiału. **Nie oznacza to jeszcze zamknięcia rozdziału**: zgodnie z ustalonym stylem pracy przeprowadzimy kolejne iteracje tego samego rozdziału, zanim przejdziemy do 03. Dodatkowo po wypchnięciu należy zweryfikować GitHub Actions (parser CLI, testy aplikacji i przeglądarkowe).