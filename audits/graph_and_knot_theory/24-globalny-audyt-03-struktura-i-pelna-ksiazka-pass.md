# Teoria grafów i węzłów — audyt globalny 03: zamknięcie pierwszej iteracji

Data: 2026-11-23.
Kontrolowany commit źródeł i walidatorów:
[d29365be8d44523bcaf12634f1d35306eb6a861d](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d29365be8d44523bcaf12634f1d35306eb6a861d).

## Status

**PASS: struktura wszystkich 44 plików i rzeczywista pełna kompilacja książki.**
**PASS: niezależne regresje matematyczne historycznych rozdziałów 01–03 w wskazanym zakresie.**
**W TOKU: globalny audyt matematyczny wszystkich 44 rozdziałów**; zbadanie składni, etykiet i kompilacji PDF nie dowodzi poprawności 377 twierdzeń i 342 zapisanych dowodów.

W tej iteracji rzeczywiście utworzono i uruchomiono dwa nowe narzędzia:
\`tools/tests/test_graph_and_knot_global.py\` oraz
\`tools/tests/test_graph_and_knot_foundations.py\` przez workflow
\`.github/workflows/graph-and-knot-global-audit.yml\`.

## Pozytywne wyniki CI

[Pełna książka — GitHub Actions 45155023287](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45155023287):
- \`structural-audit = success\` (kontrola struktury plus historia 01–03);
- \`full-book-pdf = success\` (trzy pełne przebiegi \`pdflatex\`).

[Algorytmy teorii grafów — 45155023297](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45155023297): **success**.

[Terminologia polska — 45155023246](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45155023246): **success**.

## Inwentaryzacja

Wszystkie 44 źródła zgadzają się ze spisem \`\\input\`
w \`books/pl/graph_and_knot_theory.tex\` i wpisem
\`graph_and_knot_theory\` w \`catalog/books.json\`.
Zidentyfikowano:
- 377 środowisk twierdzeń, lematów, stwierdzeń i wniosków;
- 342 środowiska \`proof\`;
- 105 wystąpień środowisk \`figure\` i \`tikzpicture\` (częściowo dotyczących tego samego rysunku);
- 565 etykiet \`\\label\` i 145 odsyłaczy.
Nie ma zduplikowanych etykiet, niezdefiniowanych odsyłaczy
ani błędów dopasowania środowisk \`\\begin\`/\`\\end\`.

Po usunięciu kodu TikZ z analizy powtórzeń oraz identyfikatorów \`\\label\`
z kontroli angielskiego słowa „dual”, nie wykryto naruszeń
zakazanych form terminologicznych ani identycznych 18-wyrazowych
fragmentów przekraczających ustalony próg wykrycia.
Ten wynik nie wyklucza parafraz lub powtórzeń matematycznie równoważnych.

## Poprawki rzeczywiście wdrożone

1. Strona tytułowa została skorygowana z niepotwierdzonej
   deklaracji „po audycie globalnym” na „globalny audyt w toku”.
2. W rozdziale 01 ujednolicono konwencję \`n=0\`:
   skończony graf prosty może mieć pusty zbiór wierzchołków,
   natomiast graf spójny wymaga zbioru wierzchołków niepustego.
   Jest to zgodne z przypadkami brzegowymi w rozdziałach
   Mantela/Turána i \`G(n,p)\` oraz ze standardem definiowania drzew.
3. W rozdziale 26 wyrażenie „po tensorowaniu z \`Q\`”
   zastąpiono precyzyjną formułą o kompleksie łańcuchowym
   ze współczynnikami wymiernymi.
4. W rozdziale 41 tytuł sekcji o \`R(3,3)\` otrzymał
   \`\\texorpdfstring\`, usuwając dwa ostrzeżenia
   zakładek \`hyperref\`.
5. Audytor odróżnia identyfikatory etykiet od terminologii w prozie
   i nie zgłasza identycznego kodu konstrukcji TikZ
   jako powielonego wywodu matematycznego.
6. Workflow pełnej książki odrzuca ostrzeżenia LaTeX,
   przepełnienia oraz niepełną kompilację.

## Pełny PDF

Pierwszy przebieg dał **262 strony A4** z dwoma
ostrzeżeniami \`hyperref\`.
Po poprawkach drugi niezależny przebieg
dał również **262 strony A4** oraz
**zero ostrzeżeń w końcowym logu**
(\`LaTeX Warning\`, \`Package ... Warning\`,
\`Overfull\`, \`Underfull\`).
Kompilacja wykonuje **trzy pełne przebiegi**.
PDF i dzienniki są dostępne w artefakcie workflow.

Wizualnie skontrolowano niskorozdzielczą mapę całych 262 stron
oraz przykładowe strony z początkowej teorii grafów,
ekspanderów, zagadnień spektralnych, operacji na rozmaitościach
i zakończenia książki. Nie znaleziono szerokiej usterki marginesów
lub masowego nakładania się rysunków. Audyt wzrokowy
każdej figury i każdego wzoru w powiększeniu
w dalszym ciągu pozostaje zadaniem otwartym.

## Historyczne rozdziały 01–03: niezależne modele

Nowe \`test_graph_and_knot_foundations.py\` sprawdziło
**1099** grafów prostych o 1–5 wierzchołkach
oraz **3413** ciągów stopni.
Zakres:
- lemat o uściskach dłoni, dopełnienia i stopnie;
- kryterium cykli nieparzystych i dwudzielność;
- kryterium Havla–Hakimiego porównane z pełną enumeracją grafów;
- rząd macierzy incydencji nad \`F_2\`, liczba cyklomatyczna i lasy;
- kryterium mostu i alternatywnej ścieżki;
- warunki Eulera przez niezależne wyszukiwanie szlaków
  przechodzących po każdej krawędzi dokładnie raz;
- twierdzenie Robbinsa przez enumerację silnie spójnych orientacji
  grafów do czterech wierzchołków.
Wszystkie kontrole przeszły.

To są niezależne przypadki skończone, nie automatyczna
weryfikacja dowodu dla dowolnego \`n\`.

## Nierozwiązane zadania pedagogiczne i merytoryczne

1. Trzy poprawne, ale skierowane do przodu zależności:
   23→24 \`thm:tg-star-seifert\`,
   24→25 \`lem:tg-kirby-slam-dunk\`,
   28→29 \`ch:tg-sw-analiza\`.
   Należy ocenić, czy nie wymaga to uprzedniego wprowadzenia założeń.
2. Matematyczna zależność rozdziału 43 (Laplasjan znormalizowany
   \`I-A/d\`) i później umieszczonego rozdziału 08
   (Laplasjan kombinatoryczny \`D-A\`) wymaga
   redakcyjnego mostu, zwłaszcza że źródła \`37–43\`
   wstawiono pomiędzy \`05\` i \`06\`.
3. Rozdziały o zanurzeniach grafów na powierzchniach,
   wielomianie Tutte'a, grafach Taita, ułamkach łańcuchowych
   i chirurgii wymiernej mają blisko powiązane treści,
   które trzeba sprawdzić na poziomie definicji, dowodów
   i przykładów, nie tylko podobieństwa tekstu.
4. Kolejny blok szczegółowej kontroli merytorycznej:
   **historyczne rozdziały 04–06** (Menger/przekroje/przepływy,
   Hall/skojarzenia/Hamilton oraz macierze incydencji).
   Potem przechodzić do następnych rozdziałów
   i dokumentować każdy audyt osobno.

## Werdykt

Zakończono **pierwszą mierzalną iterację audytu globalnego**:
spójność korpusu, pełny PDF bez ostrzeżeń i niezależne testy podstaw.
Nie nadano globalnego statusu „cały skrypt matematycznie stabilny”,
ponieważ audyty 04–36 wymagają dalszych iteracji.
