# Algebra liniowa — rozdział 01, audyt 9

Data: 21 listopada 2026  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Plik rozdziału: `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`  
Commit aktualnego rozdziału: `6b51a0e7f4c82fa82dbdebc4c2bfd6f2647ad112`

## Zakres

Ponownie sprawdzono całość rozdziału po audycie 8: warunki podprzestrzeni, przecięcia, skierowane unie, niezależność rodzin indeksowanych, rozpinanie, algorytm usuwania zbędnych generatorów, wymianę Steinitza, równoważne kryteria skończonego wymiaru, podprzestrzenie skończenie wymiarowe, współrzędne skończone i współrzędne Hamela, lemat Zorna oraz przykłady.

Kontrola obejmowała ścisłość kwantyfikatorów, jawność definicji przed ich użyciem, przypadki \(I=\varnothing\), \(\mathcal C=\varnothing\) i pustych relacji liniowych, rozróżnienie **zbioru** od **rodziny indeksowanej** i od **podprzestrzeni**, jakość języka, etykiety i odsyłacze.

## Usterki znalezione i poprawione

### 1. Sformułowanie w lemacie o unii łańcucha zbiorów niezależnych

Użytkownik wskazał zdanie „Zawiera on wszystkie \(v_j\), a jest niezależny”. Litera „a” była spójnikiem, nie symbolem matematycznym ani indeksem \(i\). Samo zdanie było stylistycznie niejasne i pomijało formalne rozpatrzenie relacji pustej.

Przepisano dowód lematu `lem:lin-lancuchy`:
- dla \(\mathcal C=\varnothing\) unia jest zbiorem pustym i jest niezależna;
- dla niepustego łańcucha bierze się dowolną nietrywialną relację o skończonej długości \(m\ge1\), z parami różnymi \(v_j\);
- dla każdego \(v_j\) wybiera się zbiór \(S_j\in\mathcal C\);
- ponieważ łańcuch jest liniowo uporządkowany przez zawieranie, skończona niepusta rodzina \(S_1,\ldots,S_m\) ma element największy \(S_{\max}\);
- wszystkie \(v_j\) należą do \(S_{\max}\), który jest **liniowo niezależnym zbiorem** (nie musi być podprzestrzenią);
- niezależność \(S_{\max}\) daje \(a_1=\cdots=a_m=0_K\).
Wyodrębniono także trywialną relację pustą \((m=0)\).

### 2. Dowód twierdzenia o przecięciu dowolnej rodziny podprzestrzeni

Poprzedni dowód zaczynał od stwierdzenia „każde \(W_i\) zawiera zero, zatem przecięcie jest niepuste”, co wymaga oddzielnego komentarza dla \(I=\varnothing\).
Obecnie argument rozdziela:
- dla \(I=\varnothing\) przyjęto przecięcie równe \(V\), stąd podprzestrzeń;
- dla \(I\neq\varnothing\) jawnie pokazano obecność \(0_V\) w przecięciu oraz domknięcie na \(au+bv\).

### 3. Przedwczesne użycie pojęcia bazy w przykładzie nad różnymi ciałami

Przykład \(\mathbb C\) jako przestrzeni nad \(\mathbb C\) i \(\mathbb R\) formalnie nazywał \((1)\) i \((1,i)\) bazami przed zdefiniowaniem pojęcia bazy. Obecna wersja najpierw podaje jednoznaczne rozkłady każdego \(z\in\mathbb C\), a następnie zapowiada formalną kwalifikację jako bazy z odsyłaczem do `def:lin-baza`.

## Kontrola techniczna

- 69 unikalnych lokalnych etykiet `\\label`, bez powtórzeń.
- Wszystkie lokalne cele `\\ref` i `\\eqref` istnieją.
- Środowiska `\\begin` / `\\end` są zrównoważone.
- Nie zmieniano dwóch rysunków TikZ ani nie dodano zależności od zewnętrznych plików.
- CI dla poprzedniej wersji (audyt 8): [44892908046](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44892908046) — sukces.
- CI dla bieżącej wersji: [44893173506](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44893173506) — **success**. Zakończono pomyślnie wszystkie kroki sprawdzające rozdział, pełną kompilację LaTeX, odsyłacze i eksport PDF. Aktualna książka liczy **16 stron**. Końcowy `linear_algebra.log` nie zawiera `LaTeX Warning`, `Overfull`, `Underfull`, `Undefined control sequence` ani `Missing character`. Wizualnie sprawdzono strony **3, 5 i 13** nowego PDF (w tym poprawiony lemat i rysunek): nie stwierdzono kolizji tekstu ani błędów składu.

Odrębne 24 niezgodności globalnej walidacji Biblioteki (importy i niezgodne kopie plików innych skryptów) nie zostały tu rozwiązane. Nie deklarujemy ich naprawienia.

## Stan i dalszy plan

**Audyt 9 zakończony z poprawkami, rozdział 01 pozostaje otwarty.** Przed jego zamknięciem należy przeprowadzić audyt 10 obejmujący ponowną kontrolę całego dowodu lematu o łańcuchu zbiorów niezależnych, spójność terminologii i rezultat końcowego CI. Rozdziału 02 jeszcze nie rozpoczynamy.
