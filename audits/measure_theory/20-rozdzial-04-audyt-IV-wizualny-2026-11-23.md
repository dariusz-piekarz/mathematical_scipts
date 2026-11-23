# Miara i całka — rozdział 04, audyt IV wizualno-techniczny (iteracja globalna XX)

**Data:** 2026-11-23. **Istniejąca gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Wyłączny przedmiot merytoryczny:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.  
**Punkt wyjścia:** raport XIX, rozdział R04 o blobie `77e4ad8551f55a2ff579aa171761ccdd01aaa918`; raport XX przed rozpoczęciem iteracji nie istniał. Na gałęzi nie znaleziono późniejszych raportów o R04. Działania wobec R01–R03 i R05–R31 ograniczają się do wcześniejszego kontekstu odsyłaczy, bez audytu lub edycji.

## Usterka wykryta rzeczywistą inspekcją obrazu

Odczytano kod TikZ R04 (pierwsze cztery etapy konstrukcji Cantora), dokładnie skopiowano go wraz z podpisem do jednorazowego izolowanego dokumentu TeX z tym samym zestawem istotnych pakietów i rozmiarem papieru A4, następnie **dwukrotnie skompilowano pdflatex** i wyrenderowano PNG w rozdzielczości 160 dpi.

**Usterka potwierdzona wzrokowo:** po `\end{tikzpicture}` następowało jedynie `\smallskip`, które nie kończy akapitu. Pierwsze słowa podpisu były składane w tym samym wierszu co dolny znacznik osi „1”, w bezpośrednim sąsiedztwie znaku; dalsza część podpisu przechodziła do kolejnego wiersza. Podpis nie znajdował się konsekwentnie pod rysunkiem.

## Poprawka i niezależna kontrola po zmianie

Wprowadzono jedynie `\par\smallskip` pomiędzy zakończeniem środowiska TikZ i podpisem, zachowując wszystkie liczby, położenia punktów, kolor, podpis, matematykę i etykiety. Commit poprawki **`01aea6c7f0e4c75febccf220b4acdc99dedd56a7`**. Nowy blob R04 **`84b6300e8939fee9874ff4872862e7604dd4c1aa`**, potwierdzony przez odczyt z GitHub po zapisie.

Dokument testowy po zmianie dwukrotnie pomyślnie skompilowano; w logu figury brak komunikatów `Overfull`, `Undefined` i `Warning`. Po renderze podpis był osobnym, wyśrodkowanym akapitem **poniżej** obu etykiet osi, bez kolizji. W PDF A4: słowo „1” przy prawym końcu osi zajmowało w przybliżeniu przedział pionowy 154.84–165.75 pt, pierwszy wyraz podpisu 179.08–189.89 pt; dodatnia pionowa przerwa między nimi wynosiła ponad 13 pt. Przejrzano gotowy obraz, nie tylko ramki tekstu.

**Granice kontroli:** był to dokument zawierający autentyczny rysunek, jego autentyczny podpis i główne ustawienia typograficzne, lecz **nie pełny PDF całego rozdziału w rzeczywistym przepływie stron książki**. Pozostaje sprawdzić, czy umiejscowienie rysunku w R04 nie powoduje problemów z paginacją i sąsiednimi akapitami.

## Dodatkowe niezależne sprawdzenia rachunkowe

Lokalnie uruchomiono niezależną implementację kontroli odpowiadających skryptowi `tools/test_measure_theory_ch04_geometry.py`:
- **262 144** uporządkowane pary zbiorów z algebry dziewięciu komórek — monotoniczność, podaddytywność i addytywność dla rozłącznych zbiorów: PASS.
- **11** etapów klasycznej konstrukcji Cantora — dokładne długości przedziałów i ich suma: PASS.
- **10** etapów konstrukcji Smitha–Volterry–Cantora — dodatniość długości i dokładna suma: PASS.
- **14** etapów kontroli przyrostów funkcji Cantora i **9** oszacowań pola pokrycia wykresu Lipschitzowskiego — PASS. Ostatnie oszacowanie przy N=256 i L=3/2: 0,011841058731079102.

Kontrole te są regresją skończonych przykładów i rachunków, nie dowodzą ogólnych twierdzeń.

## Workflow / blokery certyfikacji

Na gałęzi istnieje już `.github/workflows/measure-theory-ch04.yml` z osobnym zadaniem dokładnych testów i zadaniem kompilacji odizolowanego R04 oraz całej książki. Po zmianie źródła R04 workflow powinien zostać wywołany przez regułę push. Wykorzystany endpoint do odczytu workflow dla commitu zwrócił pustą listę, ponieważ obsługuje uruchomienia związane z PR; nie daje to podstaw do stwierdzenia ani sukcesu, ani porażki przebiegu push. Także statusy commitu nie zawierały potwierdzonych wyników. **Pełnego GitHub CI nie potwierdzono.**

W tej iteracji nie skontrolowano wszystkich stron rozdziału, nie pobrano PDF z GitHub Actions ani nie dokonano niezależnego pełnego audytu merytorycznego rozdziału po nowej zmianie graficznej. Istniejące pozytywne audyty XVII–XIX zachowują swoją wartość, lecz nie zastępują kontroli wersji po ostatniej zmianie.

## Rozstrzygnięcie

**R04: nadal NIESTABILNY / NIEZATWIERDZONY.** Wykryto i poprawiono rzeczywistą usterkę podpisu; niezależna lokalna kompilacja i inspekcja rysunku po poprawce jest czysta. Nie ma powodu zmieniać zatwierdzonego zakresu matematycznego. Nie wolno jednak deklarować ostatecznej stabilizacji bez wyników CI, pełnego PDF i niezależnego audytu po poprawce.

**Następna iteracja:** wyłącznie R04. Ustalić ostateczny wynik workflow dla aktualnego SHA, pobrać i przejrzeć całe PDF R04 oraz wykonać kolejną czystą kontrolę. Dopiero potem rozważyć przejście do R05.
