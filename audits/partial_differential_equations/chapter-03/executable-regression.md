# PDE-03 — testy wykonywalne i CI (iteracja 37, 2026-11-24)

Źródło rozdziału: blob 697407ee628ed254cfc86a38cac5a13e72a721e5; bez zmian w tej iteracji.
Rejestr: 28 kryteriów semantycznych (blob 85a64b9f2f345b1f979d1deb055f05f761aae602).

## Rzeczywiste wykonanie

Plik tests/mathematical/partial_differential_equations/chapter-03/test_laplace_poisson.py, commit c989c4cef546f54708f1335b503d5a782f03a640, blob ab010d105b9a731d56ad5c7f61be52171270328f. Lokalna kopia sprawdzona przez git hash-object: ten sam SHA. Uruchomiono python test_laplace_poisson.py -v: Ran 7 tests, OK (0.015 s).
- Radialny laplasjan i strumień: 28 kombinacji.
- Poprawka Greena dla współliniowych punktów (w tym biegun 0): 36 kombinacji.
- Jądro Poissona na dysku: 12 profili, 48 porównań zespolonych modów (kwadratura 1024 węzłów).
- Harnack: 140 kombinacji.
- Bariera kwadratowa: 21 kombinacji.
- Majoranta analityczności: 15 wymiarów.
- Przekłuta kula: 84 kombinacje.
Są to kontrole skończone wzorów, nie dowody, nie parser źródła i nie Lean.

## CI

Workflow .github/workflows/partial-differential-equations-ch03.yml, commit ebf04422839f991e6a08dbf9778a82edb1510646. Uruchamia 7 testów, sprawdza etykiety, odsyłacze, kotwice oraz ID (w tym sufiksy), zagnieżdżenie środowisk, zgodność kolejności manifestu z książką i kanoniczny blok listings; kompiluje izolowany rozdział z preambułą książki, renderuje strony i publikuje PDF, log, tekst i PNG. Diagnostyka ma odrzucać m.in. niezdefiniowane odsyłacze i overfull hbox.
Trzy cele zewnętrzne zweryfikowane w źródłach rozdziałów 01 i 19. Numer twierdzenia słabej zasady maksimum wyznaczony z rzeczywistych deklaracji wspólnego licznika i 23 wystąpień odpowiednich środowisk do etykiety; w izolowanym PDF 1.23, odsyłacze do rozdziałów 1 i 19. Odsyłacze zewnętrzne są tylko numerami, bez docelowych stron/hiperłączy. Nie jest to kompilacja całej książki.
W chwili sprawdzenia API listy przebiegów nie zwróciło jeszcze przebiegu nowego workflow; nie potwierdzono wykonania CI, kompilacji ani renderowania. Audyt wizualny i niezależne przebiegi stabilizacyjne pozostają otwarte. Lean nie uruchomiono.
