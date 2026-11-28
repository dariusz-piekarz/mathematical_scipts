# PDE-07 — iteracja 94: wykonywalne testy regresyjne i CI

Data: 2026-11-25. Źródło bez zmian: ccabfced1d41d4b25f2853aed43dff90c70b8ea6. Rejestr 70 kryteriów semantycznych: fcc405f47ecf73ad1f8e4cdf611fa984a2b3a546.

Dodano test_distributions.py w tests/mathematical/partial_differential_equations/chapter-07, commit c0972bac19ea2d38aece68e4404f29c3b903dbc3, blob 62d0d08e95f35533ba82eb199e8d1e3fdc8fecf6. Lokalny git hash-object zgodny z pobranym blobem. Faktycznie uruchomiono python test_distributions.py -v: Ran 10 tests in 0.057s, OK.

| Test | Kryteria | Wynik lokalny |
|---|---|---|
| test_scaled_test | 010, 019 | PASS |
| test_heaviside_and_absolute_value | 018 | PASS |
| test_jump_sign | 021, 023 | PASS |
| test_reflected_kernel | 035 | PASS |
| test_delta_scaling | 030, 069 | PASS |
| test_mollifier_heaviside | 038 | PASS |
| test_radial_laplace | 050–053 | PASS |
| test_heat_initial_trace | 055, 058 | PASS |
| test_heat_operator | 055 | PASS |
| test_radial_averaging | 062 | PASS |

Są to skończone testy numeryczne, nie dowody ani automatyczna walidacja treści TeX. Kryteria semantyczne wymagają osobnej drugiej lektury.

Dodano .github/workflows/partial-differential-equations-ch07.yml, commit f3e018e1c64efb8abe7700751ee5fe0dc0d60128, blob 27e2b20c2357a473a5ba24a62d91c697ddab2dcd. Workflow sprawdza testy, etykiety, odsyłacze, kotwice kryteriów, zagnieżdżenie środowisk, zgodność kolejności z manifestem i wspólny blok listingów. Przygotowuje izolowany rozdział z kanoniczną preambułą, oblicza numery zewnętrznych odsyłaczy według liczników (osobna kontrola dwuwierszowego align dla eq:pde3-green2); zewnętrzne odsyłacze w izolowanym PDF są tylko liczbowe. Kompiluje, sprawdza log, renderuje strony i udostępnia PDF, log, tekst oraz PNG.

Stan przebiegów dla commitu workflow w chwili kontroli: [{"id":45577455405,"name":"PDE - chapter 07 audit","status":"in_progress","conclusion":null}]. Nie zweryfikowano logów, kompilacji, numeracji wygenerowanej przez workflow ani renderu. Nie wykonano Lean ani pełnej kompilacji tomu. Następna iteracja 95: odczyt faktycznego wyniku CI i logów, korekty ewentualnych błędów kompilacji/numeracji/układu, oględziny PDF. Następnie druga lektura i audyt kontrolny. Zakres merytoryczny zamknięty.
