# Algebra abstrakcyjna — AA-21, audyt III (stabilizacyjny)

**Rozdział:** „Zanurzenia ciał, automorfizmy i rozszerzenia Galois”.

## Weryfikacja matematyczna

Ponownie sprawdzono wszystkie 10 dowodów, 7 twierdzeń, 5 przykładów i 3 definicje, w tym:

- Konstrukcję domknięcia algebraicznego przez niezależne zmienne, ideał właściwy i lemat Kuratowskiego–Zorna; sprawdzenie skończoności podrozszerzeń i przechodniości algebraiczności.
- Jednoznaczność przedłużenia zanurzenia na rozszerzenie proste i istnienie przedłużenia na rozszerzenie skończone.
- Liczbę zanurzeń, jej związek z rozdzielczością oraz obie implikacje twierdzenia.
- Indukcyjny dowód jednoznaczności ciała rozkładu wielomianu.
- Kryterium normalności: wszystkie trzy warunki oraz kwantyfikatory i założenia.
- Przykłady rozszerzeń rozdzielczych nienormalnych i normalnych nierozdzielczych.
- Konstrukcję i jednoznaczność ciał skończonych, grupy ich automorfizmów i rząd Frobeniusa.

**Wynik:** brak nowych błędów, nieuzasadnionych wzorów i luk; źródło pozostało bez zmian względem audytu II. Nie dodawano twierdzeń, lematów ani nowych przykładów.

SHA-256 aktualnego źródła i źródła audytu II: `47aa789109d00379d0cb9c2c3bba23e0426c00416d38f868ab6b360f4953ec82`.

## Walidacja lokalna

- **74/74 testy PASS:** 35 testów z audytu I, 15 z audytu II i 24 nowe kontrole niezależne.
- Wersje przenośne tych trzech zestawów testów sprawdzono również w strukturze katalogów odpowiadającej repozytorium: **74/74 PASS**.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **PASS**.
- Samodzielny PDF: **5 stron**, bez ostrzeżeń LaTeX, `Overfull`, `Underfull` i odsyłaczy niezdefiniowanych.
- **20 unikatowych etykiet**, **18 odsyłaczy** (wewnętrznych i do wcześniej opracowanych rozdziałów).
- Kontrola wizualna wszystkich stron: **PASS**; brak nachodzących elementów.
- Samodzielny podgląd wykorzystuje pomocnicze etykiety wcześniejszych rozdziałów, nie stanowi pełnej kompilacji książki.

## Publikacja

Po ustabilizowaniu rozdziału opublikowano go na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6`, bez tworzenia nowej gałęzi. Zaktualizowano plik główny książki, katalog rozdziałów, README i workflow testów regresyjnych; dodano trzy pliki testów i niniejszy raport.

**Granica weryfikacji:** wynik uruchomienia push-triggered GitHub Actions pozostaje niepotwierdzony, jeżeli nie uda się odczytać jego zakończonego statusu. Wynik lokalnej kompilacji pojedynczego rozdziału nie jest dowodem przejścia pełnego CI książki.

**Stan:** AA-01–AA-21 stabilne matematycznie, łącznie 69 iteracji audytowych. Następny: AA-22, audyt I.
