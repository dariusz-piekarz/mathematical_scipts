# Teoria kategorii — mapa ponownego wykorzystania materiału

Stan źródeł: 3d4dfef0b1b457c2faddbdc5ca0e05eb282c4667. Plan integracji, nie potwierdzenie wykonanych importów.

## Zasady

1. Przed pierwszym audytem rozdziału CAT sprawdzić poniższe źródła oraz raporty i testy. Nie rozszerzać zakresu po rozpoczęciu stabilizacji.
2. Zachować oryginalne etykiety przy przenoszeniu fragmentów; sprawdzić kolizje i zależności. Preferować jedno źródło kanoniczne i odsyłacze albo współdzielone fragmenty, jeśli uzasadnione, zamiast dwóch niezależnych kopii.
3. Rozdzielić wynik dowiedziony w źródle od wyniku zewnętrznego. Dowód elementowy dla modułów nie jest automatycznie dowodem w dowolnej kategorii abelowej.
4. Każde przeniesienie sprawdzić w kontekście CAT: hipotezy, notacja, odsyłacze, kompletność, testy regresyjne i kompilacja. Nie usuwać materiału z tomów źródłowych bez odrębnej decyzji.
5. Nie zmieniać kolejności aktualnych audytów CAT-00–15. Nowe części po stabilizacji podstaw.

## Mapa tematów

| Cel CAT | Źródło | Tryb |
|---|---|---|
| 02, 05–07, 09, 14: morfizmy i uniwersalność | AA-16, AA-18, ALG-04 | przykłady wolnego modułu, lokalizacji, tensor–Hom; odsyłacze i adaptacja dowodów |
| 07: iloczyn włóknisty | DG-15 | przykład transwersalności z hipotezami; nie twierdzić, że wszystkie pullbacki rozmaitości istnieją |
| 08: granice | AT-10, AT-29 | przykłady granic odwrotnych, solenoid, brak dokładności, lim^1; rozwinąć teorię ogólną |
| 03–04, 13: funktory, naturalność, równoważności | DG-10, ALG-09 | cofnięcie form, de Rham; GAGA jako wynik zewnętrzny z zakresem |
| Kategorie monoidalne i domknięte | AA-18, DG-03 | konstrukcje tensorowe, jednostka, symetria, łączność, Hom; dodać aksjomaty koherencji |
| Kategorie addytywne i abelowe | AA-16, AT-03, DG-06 | uogólnienie jąder, kojąder, biproduktów, rozszczepień i lematu pięciu |
| Algebra homologiczna | AT-03 i DG-06 (porównać duplikaty), AA-16 i AA-18 | kompleksy, homotopie, długie ciągi, rzutowość, płaskość; rozwinąć injektywność, rezolucje, Ext/Tor |
| Kategorie pochodne | AT-25, AT-27, AT-29 | stożki, lokalizacja, przesunięcia, przykłady pochodne; uzupełnić konstrukcje abstrakcyjne |
| Presnopy i snopy | ALG-04, AT-23 | definicje, kiełki/źdźbła, sklejanie, dokładność; dodać usnopowienie i ogólne topologie Grothendiecka |
| Zmiana bazy i sześć operacji | AT-27 | przykłady sprzężeń i wzoru projekcji; nie importować wyników jako dowodów bez sprawdzenia zakresu |
| Toposy, Kan, końce/kokońce, Beck, kategorie wzbogacone, wyższe | nie potwierdzono kompletnego pokrycia w sprawdzonym zbiorze | opracować brakujący aparat po dokładniejszym przeszukaniu |

## Raporty audytowe odczytane

- audits/abstract_algebra/ch16_iteration_03.md (raport stabilizacji, 62/62 lokalnie)
- audits/abstract_algebra/ch18_iteration_04.md (raport stabilizacji, 64/64 lokalnie)
- audits/abstract_algebra/cross_18_aa14_aa16_aa18_nakayama_projective_flat_2026-11-23.md
- audits/algebraic_geometry/2026-11-22-ALG-04-iteration-04.md
- audits/algebraic_geometry/2026-11-22-ALG-GLOBAL-iteration-04.md
- .github/workflows/algebraic-topology-audit-ch03-04.yml (konfiguracja, nie wynik CI)

Nie potwierdzono obecnego wyniku CI ani indywidualnych raportów stabilizacji wszystkich rozdziałów AT/DG. Porównać identyfikatory blobów z raportami przed przenoszeniem.

## Identyfikatory źródeł

- `chapters/pl/abstract_algebra/08-grupy-abelowe-torsja-i-iloczyn-tensorowy.tex` — blob `d6de6b6cb0e01449c8f976b662960cd0425abd90`
- `chapters/pl/abstract_algebra/12-pierwiastniki-idealow-i-lokalizacja-pierscieni.tex` — blob `f64ec91a7fcc58557dba8b13f75b74f6b2ca788d`
- `chapters/pl/abstract_algebra/16-moduly-homomorfizmy-ciagi-dokladne-i-moduly-rzutowe.tex` — blob `319cbac9af83a819e0d375fc282284c62638c3ac`
- `chapters/pl/abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex` — blob `faaa972f8d1a7625d42c856d78c6f58ee7ad3564`
- `chapters/pl/algebraic_geometry/04-algebra-przemienna-snopy-i-krzywe-algebraiczne.tex` — blob `ab1344ed93a02bb757e5a78cb3833d6c4a18079c`
- `chapters/pl/algebraic_geometry/09-geometria-algebraiczna-a-analiza-zespolona-analityfikacja-chow.tex` — blob `32ebab6fc0b6a27855615716b63fa9f58c57ba0c`
- `chapters/pl/algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex` — blob `03ee5b773493ee95746413aabd760d54b6a640e6`
- `chapters/pl/algebraic_topology/10-homologia-i-kohomologia-c-echa-od-pokryc-do-granic-przestrzeni.tex` — blob `7f797b880d63de77dcf1713117ab9cc48f4dc4d3`
- `chapters/pl/algebraic_topology/23-kohomologia-snopow-z-nosnikami-i-podstawy-dualnosci-verdiera.tex` — blob `e83fc3e26de4fc347543e35c976549cd8bc03141`
- `chapters/pl/algebraic_topology/25-kategorie-pochodne-struktury-hodge-a-cykle-zanikajace-i-monodr.tex` — blob `ee73c4fe52c7520a101a151f5473062b71dd4bd4`
- `chapters/pl/algebraic_topology/27-szesc-operacji-snopowych-dualnosc-verdiera-i-cykle-specjalizac.tex` — blob `1ac64447ca790eb81b72e4c3198e80cc9fe6cdbb`
- `chapters/pl/algebraic_topology/29-dalsze-narzedzia-homotopii-granice-odwrotne-przeszkody-operacj.tex` — blob `a860202ab911195bffe564097289e7cd4c28f553`
- `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` — blob `7ab3f15ced06e8233f978471c779e343ac5902ca`
- `chapters/pl/differential_geometry_and_topology/06-algebra-homologiczna-kompleksy-i-kohomologie.tex` — blob `ace6d6101ec1dbd3999607ff14e0da1c72e7366e`
- `chapters/pl/differential_geometry_and_topology/10-formy-rozniczkowe-orientacja-i-kohomologia-de-rhama.tex` — blob `858d30abdfb27335f8194740f2304ee98d5ca15a`
- `chapters/pl/differential_geometry_and_topology/15-twierdzenie-sarda-i-transwersalnosc.tex` — blob `f6d6ab60598e1ec5b39f7acea37c4953f5565c4b`
