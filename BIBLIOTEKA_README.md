# Biblioteka matematyczna — iteracja I

Modularna wersja 12 dostarczonych skryptów matematycznych, zachowująca wszystkie rozdziały i sekcje bez redakcji treści. Starszy plik `geometria_i_topologia_rozniczkowa.tex` pozostał nietknięty.

## Struktura
- `skrypty/*.tex` — pliki główne książek wykorzystujące `\\input` do kolejnych rozdziałów.
- `rozdzialy/<nazwa>/*.tex` — poszczególne rozdziały (w dokumentach `article`: sekcje).
- `zrodla/` — kopie oryginalnych 12 plików, żeby możliwe było porównanie i odtworzenie.
- `manifest.json` — spis treści, kolejność, długości i skróty SHA-256.
- `narzedzia/sprawdz_podzial.py` — kontrola integralności rozdzielenia.
- `narzedzia/buduj_wszystkie.ps1` — budowanie wszystkich skryptów w PowerShell.

Kompiluj z katalogu `skrypty/`: `latexmk -pdf -interaction=nonstopmode teoria_kategorii.tex`.
Alternatywnie z katalogu głównego: `latexmk -cd -pdf skrypty/teoria_kategorii.tex`.

## Kolejna iteracja
Dokonać audytu nakładek tematycznych, odróżnić powtórzenia konieczne dydaktycznie od duplikatów, a następnie scalać wspólne treści bez utraty dowodów, przykładów, zadań, kodu i rysunków. Nie zmieniać znaczenia odsyłaczy ani systemu makr.
