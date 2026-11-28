# Teoria grafów i węzłów — audyt globalny 02: pełny skład, zależności i korekty

Data: 2026-11-23.
Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
**Status: audyt całej książki w toku.** Ten raport dokumentuje zakończoną globalną kontrolę struktury i pierwszą kompilację, nie wszystkie matematyczne dowody 44 rozdziałów.

## Wynik pierwszej walidacji 44 plików

[GitHub Actions — pełna książka 45153907527](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45153907527):
- \`structural-audit\`: success;
- \`full-book-pdf\`: success;
- **44/44** źródła w głównej książce, katalogu Atlasu i katalogu plików (ten sam zbiór w tej samej kolejności);
- **565** etykiet, **145** odsyłaczy, brak etykiet powtórzonych, brak odsyłaczy niezdefiniowanych;
- **377** środowisk twierdzeń, lematów, stwierdzeń i wniosków oraz **342** środowiska dowodu; różnica nie jest automatycznie błędem: część wyników zewnętrznych jest przyjmowana z literatury;
- **105** wystąpień środowisk ilustracji \`figure\` i \`tikzpicture\` (są liczone oddzielnie, często obejmują tę samą figurę);
- brak niezgodności par \`\\begin\`/\`\\end\`;
- trzy odsyłacze do późniejszych rozdziałów: 23→24 (\`thm:tg-star-seifert\`), 24→25 (\`lem:tg-kirby-slam-dunk\`), 28→29 (\`ch:tg-sw-analiza\`). Są poprawnie zdefiniowane i dostępne w kompletnym wydruku, ale wymagają uwagi pedagogicznej.

## Pierwsza pełna kompilacja PDF

Trzykrotny \`pdflatex\` rzeczywistej książki \`books/pl/graph_and_knot_theory.tex\` zakończył się poprawnie.
Otrzymano **262 strony A4** (plik około 1.9 MB). Brak przepełnień i niezdefiniowanych odsyłaczy.
W końcowym logu pozostały dwa ostrzeżenia \`hyperref\`:
\`Token not allowed in a PDF string (Unicode): removing math shift\` w tytule sekcji
\`\\section{Dokładna wartość $R(3,3)$}\` (rozdział 41, linia 353).
Korekta: jawne \`\\texorpdfstring{$R(3,3)$}{R(3,3)}\`.

Przygotowano niskorozdzielczą wizualną mapę wszystkich 262 stron i skontrolowano przykładowe strony tytułowe, fragmenty początkowe, partie spektralne, części rozmaitościowe i końcowe strony bibliograficzne. Obraz ogólny nie wskazuje globalnego problemu z przekraczaniem marginesów. To **nie** jest równoważne indywidualnej kontroli wszystkich diagramów w powiększeniu.

Po korekcie workflow zaczyna traktować każdy wpis \`LaTeX Warning\`,
\`Package ... Warning\`, \`Overfull\` lub \`Underfull\` na trzecim przebiegu jako **błąd CI**.
Nie wolno zatem ogłosić czystego wydruku, zanim nowy przebieg nie potwierdzi braku ostrzeżeń.

## Znaleziska dotyczące terminologii

Zidentyfikowano w rozdziale 26 zdanie „a po tensorowaniu z \`\\mathbb Q\` również ...”.
Zastąpiono je precyzyjniejszym:
„a po rozpatrzeniu tego samego kompleksu łańcuchowego
ze współczynnikami w \`\\mathbb Q\` również ...”.
Równości homologicze i dowód pozostają bez zmian.

Wstępna kontrola tekstowa niepotrzebnie oznaczyła jako niedopuszczalne słowo „dual” w etykietach typu \`sec:tg-dual\` oraz wykryła fragmenty wspólnego kodu TikZ jako możliwe powtórzenia wywodów. Poprawiono audytor: etykiety i odsyłacze nie podlegają testowi angielskiego słowa w prozie, a zawartość \`tikzpicture\` nie wchodzi do analizy powielonych fragmentów literackich. Wciąż należy ręcznie badać ewentualne prawdziwe dublowanie tematów; słownikowy audyt nie porównuje logicznej równoważności dowodów.

## Ważna niespójność merytoryczno-definicyjna

Historyczny rozdział 01 określał skończony graf prosty przez **niepusty**
zbiór wierzchołków, podczas gdy późniejsze stabilizowane rozdziały Mantela/Turána i model \`G(n,p)\` świadomie rozpatrują \`n=0\`.
Ujednolicono konwencję: **graf prosty może mieć pusty zbiór wierzchołków**,
natomiast graf **spójny musi być niepusty** i każdy dwa jego wierzchołki muszą być połączone. Zachowuje to dotychczasową definicję drzewa jako grafu niepustego i zapewnia sens przypadków brzegowych \`n=0\`.
Wymaga niezależnego przetestowania historycznych kryteriów — przygotowano w tym celu \`test_graph_and_knot_foundations.py\`.

## Plan regresji historycznych 01–03

Dodano niezależną enumerację grafów 1–5-wierzchołkowych i ciągów stopni, sprawdzając:
- lemat o uściskach dłoni, dopełnienie, kryterium cykli nieparzystych;
- kryterium Havla–Hakimiego względem enumeracji wszystkich możliwych ciągów stopni;
- rząd macierzy incydencji nad \`F_2\`, liczbę cyklomatyczną, mosty;
- warunki Eulera z niezależnym przeszukiwaniem wszystkich dopuszczalnych szlaków;
- twierdzenie Robbinsa przez enumerację orientacji małych grafów.

Dalsze zadania: uruchomić test historyczny i nową pełną kompilację; poprawić ewentualne błędy i wydać raport wyniku. Następnie przejść do matematycznego audytu rozdziałów 04–06, po nich kolejnych, bez deklarowania stabilizacji całego tomu przed rzeczywistym sprawdzeniem wszystkich.
