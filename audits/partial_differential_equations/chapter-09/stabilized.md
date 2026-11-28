# PDE — rozdział 09 — stabilizacja, iteracja 147

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.
Rozdział: chapters/pl/partial_differential_equations/09-przestrzenie-sobolewa.tex.
Zatwierdzony blob: 30091fad12a19e8bc03c3067f84f30c847e43dfe, commit e7f5fbf9495709d859c7dd06a84feb2485478251. Odczyt bieżącej gałęzi potwierdził ten sam blob.

## Bramka matematyczna
Pierwsza i druga lektura 81 kryteriów udokumentowane w tests/mathematical/partial_differential_equations/chapter-09/regression.md. Trzecia lektura kontrolna 81/81 udokumentowana w iteracjach 143–146. Brak otwartych usterek w dowodach; poprawki kontrolne obejmowały geometrię rysunku, oznaczenia, interpunkcję i jawny zakres p skończonego w uwadze. Kontrola semantyczna nie stanowi recenzji innej osoby ani formalizacji Lean.

## Bramka techniczna
Run 45615511704 oraz końcowy run 45615805562: success. Job 139210762460: wszystkie kroki success. Z logu odczytano pięć testów zakończonych ok (025, 028, 066, 076, 079–080), Ran 5 tests, 81 criterion anchors verified (not executed proofs), 37 distinct labels; 64 resolved reference occurrences. Etykiety i odsyłacze zgodne co do kolejności z blobem b14ed2a90f238b9b1429b49712f6b933b1075bf4; stos środowisk poprawny.
Końcowy artefakt 15021558919: SHA-256 ee792fd52c166fad831517b214c2a1b0acd1c5d0b63a6487fbc33e404a7f39ed zgodny z API. PDF 25 stron A4.
Porównanie z renderami artefaktu 15021323855: 22/25 stron identyczne pikselowo. Zmienione: 9 (oznaczenia rysunku), 17 (interpunkcja), 21 (hipoteza uwagi); wszystkie trzy obejrzano w pełnym renderze. Poprawione oznaczenia czytelne i bez kolizji, układ tekstu i wzorów poprawny. Brak krytycznych diagnostyk LaTeX: niezdefiniowanych odsyłaczy, brakujących znaków, overfull hbox, niezdefiniowanych poleceń. Pozostaje 25 ostrzeżeń hyperref o pustych celach odsyłaczy zewnętrznych w izolowanym PDF i jedno Underfull hbox (badness 1142), nieblokujące dla audytu rozdziałowego.

## Decyzja
Rozdział 09 zamknięty jako ustabilizowany w zakresie audytu rozdziałowego. Wszystkie wymagane bramki dla tego zakresu zakończone. Nie potwierdzono pełnej kompilacji książki, globalnego CI aplikacji ani Lean; nie przypisujemy im statusu PASS na podstawie tego przebiegu.
Link CI: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45615805562
Następna iteracja 148: rozdział 10 — Zanurzenia i zwartość Sobolewa, inwentaryzacja i pierwsza lektura matematyczna, szczególnie jawne hipotezy, twierdzenia o przedłużaniu, dowody nierówności i zależności od rozdziału 09.
