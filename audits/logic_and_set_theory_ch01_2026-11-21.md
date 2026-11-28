# Audyt rozdziału 01 — Zdania i spójniki logiczne

Data: 21 listopada 2026. Bazą jest kompletne archiwum iteracji 79 z Biblioteki, nie pliki w starszym repozytorium.

## Zakres

Trzy przebiegi: analiza merytoryczna, poprawki i audyt sceptyczny; weryfikacja składni, semantyki, tablic prawdy, reguł wnioskowania, języka, przykładów, definicji, dowodów, etykiet, odsyłaczy i składu PDF. Bez nowego twierdzenia, lematu i bez poszerzenia pokrycia.

## Poprawki

1. Rozróżniono abstrakcyjne litery zdaniowe, formuły, wartościowania i zdania w interpretacji.
2. Doprecyzowano zamknięcie indukcyjnej definicji formuł i jednoznaczność ich rozbioru.
3. Naprawiono niepoprawną nazwę „pusta przesłanka” w przykładzie z fałszywym poprzednikiem implikacji.
4. Ustalono oznaczenie liczby w przykładzie negowania zdania złożonego.
5. Sprecyzowano warunek wystarczający i konieczny oraz umowę dotyczącą nawiasów.
6. Nazwano rozszerzenie wartościowania na formuły, wyjaśniono jego jednoznaczność.
7. Usunięto niejednoznaczność konwencji `\mathbb N` dla przypadku `n=0` w już istniejącym twierdzeniu.

## Weryfikacja

- 44 rozdziały w pełnym skrypcie: `latexmk` dwukrotnie przeszedł, 375 stron, bez błędów/ostrzeżeń LaTeX.
- Etykiety rozdziału 01: 31, zachowane nazwy i kolejność. Odsyłacze rozdziału: 7; łącznie w pełnym wydaniu 1075 etykiet i zero duplikatów; brak odsyłaczy bez celu.
- Sprawdzono semantykę spójników przez enumerację wartościowań i kryteria wynikania dla listy pustej i niepustej; wszystkie testy zaliczone.
- Brak zewnętrznych zasobów graficznych i skryptowych: rysunki TikZ w źródle.
- Obejrzano strony 15 i 16 PDF, schematy są czytelne.

## Uwaga integracyjna

W rozdziale jest oryginalny odsyłacz `\ref{ch:syntax-fol}` do rozdziału 09. W pełnym skrypcie działa. Przy publikacji wyłącznie rozdziału 01 w repozytorium pozostanie do czasu audytu i importu rozdziału 09 jako przyszły odsyłacz; nie zmieniać stabilnej etykiety.

## Status

Rozdział 01: stabilny po trzecim przebiegu audytu, bez stwierdzonych nowych luk wymagających modyfikacji. Integracja w GitHub i CI wymaga osobnej weryfikacji wykonania na nowym commicie.