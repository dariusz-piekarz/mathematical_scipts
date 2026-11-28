# Audyt I — rozdział 04 „Pary uporządkowane i relacje”

**Data:** 21 listopada 2026 r.  
**Źródło:** aktualny plik Biblioteki matematycznej `04-ordered-pairs-and-relations.tex` (wersja 4).  
**Zakres:** kontrola wyłącznie istniejących definicji, twierdzeń, lematów, dowodów, przykładów, odsyłaczy, terminologii i rysunków; bez dodawania nowego materiału.

## Naprawione nieścisłości

1. **Samodzielność założeń w twierdzeniach i lemacie.** W 13 miejscach (w tym w twierdzeniu o monotoniczności iloczynu kartezjańskiego, o obrazach relacji, o składaniu relacji, w lemacie o monotoniczności składania, w twierdzeniu o łączności i relacjach identycznościowych oraz w lemacie o potęgach relacji) jawnie zadeklarowano zbiory `A, B, C, D`, ewentualnie zbiór indeksów `I`, zanim zaczęto używać ich w tezach i definicjach. Nie zmieniono warunków ani żadnych wzorów matematycznych.
2. **Wyjaśnienie antysymetrii.** W uwadze o relacji `\le` na `\R` dwukrotnie występował identyczny warunek `x\le x`, co nie wyjaśniało różnicy między antysymetrią i asymetrią. Zastąpiono ten fragment jasnym objaśnieniem przypadku `x=y`, w którym oba warunki z przesłanki antysymetrii są prawdziwe, a relacja zwrotna jest dopuszczalna.
3. **Redakcja definicji przeciwobrazu.** Poprawiono rozdzielenie słów i skład wyróżnienia `\emph{istnienie}`, bez zmiany definicji (egzystencjalnego przeciwobrazu dowolnej relacji).

Wszystkie zmiany są lokalne. **Liczba i treść twierdzeń, lematów oraz przykładów pozostają niezmienione.** Nie dodano żadnego twierdzenia, lematu ani nowej konstrukcji.

## Weryfikacja matematyczna

- Zbadano **12 twierdzeń, 3 lematy i wszystkie 15 dowodów**, 11 definicji, 17 przykładów i 6 uwag. W szczególności: kodowanie par Kuratowskiego i jego jednoznaczność; istnienie iloczynu kartezjańskiego; jednoznaczność włókien relacji a zachowywanie przecięć; odwracanie i łączność składania; sześć podstawowych własności relacji; potęgi, ścieżki i minimalne domknięcia; relację równoważności generowaną przez relację; kodowanie relacji macierzami zero-jedynkowymi.
- Niezależna enumeracja skończonych zbiorów (rozmiary 0–3) i relacji oraz potrójnego składania na zbiorze dwuelementowym sprawdziła **187 714 przypadków**, wszystkie zaliczone. Testy obejmowały m.in. puste zbiory, brak krawędzi, zamknięcia, tożsamości, odwracanie, obrazy i przeciwobrazy. Testy nie zastępują formalnych dowodów dla dowolnych zbiorów, które sprawdzono ręcznie.
- Nie stwierdzono błędów w tezie ani przejściach dowodowych istniejących 15 twierdzeń i lematów. Zachowano **35 oryginalnych etykiet** i wszystkie odwołania.

## Kompilacja i integracja

- Pełny skrypt: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — kod 0, **44 rozdziały, 376 stron**. Łącznie **1075 unikatowych etykiet**, **866 odsyłaczy**, **0 duplikatów i 0 brakujących celów**. Brak ostrzeżeń `Overfull \hbox`; pozostają trzy nieblokujące `Underfull \hbox` w innych miejscach pełnego skryptu.
- Książka w formacie repozytorium z rozdziałami 01–04: kod 0, **41 stron**. Odsyłacze do rozdziałów 07, 09, 10 i 25 nie rozwiązują się *wyłącznie* w częściowym imporcie, ale cele istnieją w pełnym skrypcie. Nie zmieniano etykiet `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol` i `ch:zf-axioms`.
- Obejrzano **10 stron PDF** rozdziału 04 (strony 42–51 pełnego składu), w tym obie ilustracje TikZ. Nie widać obciętego tekstu ani nachodzących na siebie etykiet i rysunków.
- Rozdział zawiera samodzielny kod TikZ; nie wymaga zewnętrznych plików obrazów ani kodu wykonywalnego.

## Status

**Audyt I zakończony.** Wykryte nieścisłości zredagowano, istniejący materiał matematyczny pozostał niezmieniony i przeszedł kontrole. Zgodnie z przyjętą procedurą **rozdział 04 pozostaje otwarty** do kolejnych niezależnych audytów przed zamknięciem.
