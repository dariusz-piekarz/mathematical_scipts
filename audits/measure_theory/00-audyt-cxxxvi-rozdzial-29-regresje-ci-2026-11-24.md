# Audyt CXXXVI (136) — regresje i CI rozdziału 29
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia a543bb58a6ad7a6e6a0776face436809e4bc911b. Źródło rozdziału: blob 89115c4b293c7c5a9a0ab9b2b16967cf97504d54 (3753 wiersze, 37 etykiet), nie zmieniano.
## Zmiany
- Commit 05b8db436e164556c5c2321facb4dce06fce05e4: tools/tests/test_measure_theory_ch29.py. 12 testów, dokładne modele wymierne (znaki pochodnej i brzegu prądu, pełny i ważony koobszar funkcji schodkowych, translacja, średnie, znoszenie gradientów, stałe stożkowe, skalowanie, atomowe miary wektorowe, wyczerpanie) oraz regresje etykiet, odsyłaczy i istotnych fragmentów dowodów.
- Commit 73484b82f17fcb3b6864c61f480aea99550f1d40: .github/workflows/measure-theory-ch29.yml, na podstawie CI rozdziału 28, z limitami czasu instalacji i kompilacji, kompilacją pełnego skryptu, importem zewnętrznych odsyłaczy do izolowanego rozdziału, kontrolą logów i renderowaniem wszystkich stron. Numer rozdziału 29.
## Weryfikacja
Run https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45370276374, job 138362478676 zakończony success. Logi potwierdzają 12 testów rozdziału i 4 testy integralności całego skryptu, wszystkie OK. Testy modeli nie zastępują dowodów ani kontroli PDF.
Stan zadania PDF przy ostatniej kontroli: in_progress, wynik: jeszcze niedostępny. Nie wykonano oględzin PDF.
## Otwarte
Zweryfikować zakończenie zadania PDF i logi, pobrać rzeczywisty artefakt i obejrzeć wszystkie strony, w razie potrzeby poprawić źródło. Rozdział 29 pozostaje otwarty, 28/31 ustabilizowanych.
