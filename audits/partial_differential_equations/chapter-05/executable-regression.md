# PDE-05 — iteracja 62: testy wykonywalne i CI

Data: 2026-11-25. Źródło rozdziału: b6c21985b026f03f51fd6626a26ae488d347d793; rejestr 32 kryteriów: ed311aa18cd940652b35edf12a9e17f0c599a8bc.

Dodano tests/mathematical/partial_differential_equations/chapter-05/test_wave.py (commit a8a959b4e790c1cf94b4b7af25cba6fa63c492d8, blob 233f3d7fcc8d7bdb3080b8e98534b3d06094c45d), 9 metod unittest:
- d'Alembert dla wielomianów, rachunek strumienia lokalnej energii w arytmetyce wymiernej;
- Darboux dla wielomianu radialnego, momenty drugiego rzędu na sześciu punktach osiowych, rachunki Kirchhoffa;
- kwadratura po podstawieniu radialnym w wadze Poissona, normalizacja i drugi moment;
- całka Duhamela dla wielomianowego wymuszenia, energia pojedynczego modu struny;
- klasyfikacja pierwiastków CFL, rekurencja w arytmetyce wymiernej dla poprawnie zainicjalizowanych modów, w tym oba podwójne pierwiastki;
- rekurencja okresowa w przestrzeni fizycznej, oszacowanie normy na skończonym przedziale i zasięg impulsu.

Są to skończone kontrole rachunkowe; nie parsują treści dowodów w TeX, nie dowodzą ogólnych twierdzeń, nie uruchamiają Lean.

Dodano .github/workflows/partial-differential-equations-ch05.yml (commit f36032f97ec279dc654692f78af3bd8454509d63, blob b1b7b5aa4209088da8c0740142040e4fc894924f). Workflow sprawdza testy, strukturę i kotwice kryteriów, manifest i kolejność rozdziałów, kanoniczne listingi, zewnętrzne odsyłacze thm:dalembert i chap:pde-heat. Numer pierwszego wyprowadza z licznika wspólnego środowisk twierdzeniowych, numer drugiego z pozycji w księdze. Odsyłacze do nieobecnych rozdziałów w izolowanej kompilacji mają wyłącznie numery, bez aktywnego celu. Workflow kompiluje rozdział z preambułą księgi, sprawdza diagnostykę, renderuje strony i publikuje artefakt.

Stan rzeczywiście sprawdzony w przebiegu 45566181241, job 139041424519: in_progress, conclusion=null. Kroki:
- Set up job: completed / success
- Run actions/checkout@v4: completed / success
- Run executable regression checks: completed / success
- Check references and prepare standalone chapter: completed / success
- Compile standalone chapter with canonical preamble: in_progress / brak wyniku
- Inspect diagnostics and render pages: pending / brak wyniku
- Upload compiled chapter and diagnostics: pending / brak wyniku
- Post Run actions/checkout@v4: pending / brak wyniku

Nie wykonano niezależnego lokalnego uruchomienia testów; wyniki pochodzą z CI. Nie przeprowadzono ręcznej kontroli wizualnej ani formalizacji Lean. Rozdział pozostaje otwarty. Następny etap: weryfikacja końcowego wyniku CI, oględziny rzeczywistego PDF, ewentualne poprawki i niezależny audyt 8 sekcji.
