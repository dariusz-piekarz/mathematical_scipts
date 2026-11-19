# Biblioteka matematyczna — iteracja I

Zbiór 12 dostarczonych skryptów matematycznych. Każdy skrypt ma własny plik główny w `skrypty/`, a treść poszczególnych rozdziałów / sekcji znajduje się w `rozdzialy/<nazwa_skryptu>/`. Oryginały są zachowane w `zrodla/`, również gdy mają sufiksy `(1)` / `(2)`.

## Układ

- `skrypty/` — pliki główne LaTeX; każda książka odwołuje się do rozdziałów przez `\input`.
- `rozdzialy/` — pliki pojedynczych rozdziałów dla klas `report`/`book`, a pojedynczych sekcji dla klasy `article`.
- `zrodla/` — nietknięte oryginały przesłane przez użytkownika.
- `manifest.json` — nazwy, kolejność, sumy kontrolne oraz mapowanie źródeł.
- `narzedzia/sprawdz_podzial.py` — weryfikacja integralności z podziałem.
- `narzedzia/buduj_wszystkie.ps1` — kompilacja w PowerShell w Windows.

## Kompilacja

Uruchom z katalogu `skrypty`, np. `pdflatex -interaction=nonstopmode teoria_kategorii.tex` lub `latexmk -pdf -interaction=nonstopmode teoria_kategorii.tex`. Z katalogu głównego można użyć `latexmk -cd -pdf skrypty/teoria_kategorii.tex` (przełącza katalog roboczy na katalog pliku głównego). Wynika to z faktu, że ścieżki `\input` są ustawione względem `skrypty/`.

Część oryginałów może mieć własne błędy kompilacji i zależności systemowe — pierwszy etap nie ingeruje w treść matematyczną ani nie zmienia pakietów lub konstrukcji. Wynik kompilacji nie jest gwarantowany dla wszystkich 12 książek.

## Zasada redakcyjna

**Iteracja I:** wyłącznie rozdzielenie, bez zmieniania treści. **Iteracja II:** audyt pokrywających się fragmentów wewnątrz książek i między książkami, ustalenie modułów wspólnych, scalanie powtórzeń i naprawa odsyłaczy po scaleniu. Przed merge zachować historię, sprawdzić, czy powtórzenie wynika z celowej samodzielności tomu.

## Iteracja II: audyt i wspólne moduły

- `wspolne/slabe_twierdzenie_lefschetza.tex` jest współdzielony przez dwa rozdziały.
- `manifest_integracji.json` opisuje dwie kontrolowane zamiany tekstu na `\input`.
- `narzedzia/sprawdz_integracje.py` kontroluje 12 źródeł, 236 rozdziałów i zakres zmian.
- `audyt/raport_nakladek_iteracja_2.md` zawiera audyt merytoryczny i priorytety.
- `audyt/macierz_nakladek.csv` zawiera ranking podobieństw rozdziałów.

Uruchom: `python narzedzia/sprawdz_podzial.py` (automatycznie wybiera kontrolę integracji) albo `python narzedzia/sprawdz_integracje.py`. Twierdzenie wspólne jest włączane automatycznie z obu skryptów.
