# PDE-04 — stabilizacja, iteracja 54

Data: 2026-11-24. Rozdział: Równanie ciepła. Gałąź biblioteka-matematyczna-iteracja-6.

## Zamrożone źródło i zakres

- Źródło chapters/pl/partial_differential_equations/04-rownanie-ciepla.tex: blob abd8dc9eca604f7105a6649cfd961547ef7968c5, ostatnia poprawka 8a39dc7458d5e78de4e0965a962f097b1cf23cf0.
- Rejestr tests/mathematical/partial_differential_equations/chapter-04/regression.md: blob 18e4fb12dba0c352b9bc00e238badd5a919a54f3, 36 kryteriów semantycznych i jedno wizualne.
- Pierwsza pełna lektura matematyczna: iteracje 42–49, wszystkie 10 sekcji. Testy i CI: iteracja 50; kontrola renderu: iteracja 51.
- Druga pełna lektura (niezależny audyt stabilizacyjny): iteracje 52 (4.1–4.3), 53 (4.4–4.6) i 54 (4.7–4.10). Są to trzy części jednego ponownego audytu, nie trzy osobne pełne audyty. Źródło pozostaje identyczne od iteracji 49.

## Iteracja 54 — ponowna lektura 4.7–4.10

- 4.7 (025–028): różniczkowanie energii na zbiorze skończonej miary, założenia pierwszej tożsamości Greena i osobny przypadek n=1, zerowy wyraz brzegowy, ciągłość energii i całki gradientu, jednoznaczność z zerowej normy i ciągłości. W dowodzie Poincarego sprawdzono mierzalność W, końce wszystkich składowych przekroju, również na ścianach sześcianu, zerowanie całki na całych składowych i bezwzględną zbieżność przy przeliczalnie wielu składowych. Zatem reprezentacja całkowa V i absolutna ciągłość nie wymagają skończonej liczby przedziałów. Cauchy–Schwarz i Tonelli dają 4L². Ponownie przeliczono wykładniki -kappa t/(2L²) dla energii i -kappa t/(4L²) dla normy. Zweryfikowano mody Dirichleta, wartości własne i oba rachunki norm; brak nieuzasadnionego wniosku dla szeregu nieskończonego.
- 4.8 (029–031): poprawność aproksymacji L² przez dane gładkie o zwartym nośniku i wyboru czasu zależnego od aproksymacji; potęgi zaniku z oszacowań jądra. Dylatacja h_R zachowuje normę L², czas w tożsamości skalowania jest t/R², więc dla ustalonego t norma operatorowa wynosi 1, mimo silnego zaniku. Masa i norma L¹ nie są utożsamiane z normą supremum. Ortogonalność modów na (0,pi), diagonalna bijekcja S→S, dokładne normy profili końcowych i początkowych oraz nieograniczoność odwrotności w obu normach. Nieciągłość odróżniona od niejednoznaczności i braku algebraicznej odwrotności.
- 4.9 (032–035): sprawdzono obliczenie Re(1/z²) ≥ 128/(625t²), dysk nie zawiera zera, współczynnik k!(4/t)^k, oszacowanie ilorazu silni z przypadkiem k=0 oraz rekurencję Q_m. Majoranty Weierstrassa na dowolnych zwartych prostokątach dodatnich czasów uzasadniają różniczkowanie. Dla t≤c/(8B²) wykładnik jest ≤-c/(2t²); zanik o(t^N) dominuje ustalony czynnik wielomianowy. Przedłużenie przez zero i ilorazy różnicowe dla wszystkich U_{p,q} dają ciągłe pochodne wszystkich rzędów na R². Przesunięcie indeksu k→j+1 w u_xx, niezerowa wartość u(t,0)=h(t), sprzeczność z jednoznacznością ograniczonych rozwiązań na każdym pasku. Brak analityczności czasowej w zerze nie przeczy analityczności przestrzennej splotu.
- 4.10 (036): podsumowanie zachowuje zakres twierdzeń, klasy danych, warunkowość wyników na obszarach ograniczonych, różnicę pomiędzy silnym zanikiem a normą operatorową i znaczenie nieodwracalności.

Nie wykryto nowych istotnych luk w tym zakresie. W połączeniu z raportami iteration-52.md i iteration-53.md zakończono ponowną lekturę 10/10 sekcji bez zmian źródła.

## Weryfikacja techniczna

CI 45486214130, job 138772180199, commit aa8c7b82bf7ea4e1475c39971c629ba2f0da16da: wszystkie kroki zakończone success. Sprawdzono w bieżącej iteracji tożsamość wszystkich dziewięciu blobów wejściowych (rozdział 04, rozdział 03, rejestr, test, workflow, księga, manifest, listings, preambuła Atlasu) z tym commitem. Ponownie sprawdzono 45 unikatowych etykiet, 44 wystąpienia odsyłaczy, jeden zewnętrzny cel eq:pde3-green1 obecny dokładnie raz w rozdziale 03, 37 kolejnych ID i ich kotwice, zagnieżdżenie środowisk i 10 sekcji. Wyszukanie starego zapisu różniczki w całkach nie wykazało wystąpień poza poprawnym zapisem pochodnej d/dt.

Testy: 9 metod unittest w test_heat.py, blob d584e5591216dc527bc1b0acb0fa767668f0d051, zakończony krok CI success. Są to skończone kontrole rachunkowe, nie formalizacja dowodów. Nie uruchomiono ich ponownie lokalnie.

Kontrola wizualna: raport iteracji 51, artefakt 14964405026 z przebiegu 45483410218, izolowany PDF A4 20 stron; obejrzano ogólny układ i rysunek na stronie 3. Od tego czasu źródło i pozostałe wejścia wpływające na skład nie zmieniły się; zmiana rejestru dodała kryterium wizualne 037, a CI ponownie przeszedł. Nie powtórzono oględzin w iteracji 54. Ostrzeżenie hyperref o pustym celu wynika z izolowanego odsyłacza do rozdziału 03; nie jest dowodem poprawności pełnego składu książki.

## Decyzja

Rozdział 04 ustabilizowany w zakresie audytu matematycznego, trwałych kryteriów regresyjnych, wykonanych testów CI, izolowanej kompilacji i kontroli wizualnej. Brak otwartych istotnych usterek w tym zakresie. Nie przeprowadzono formalizacji Lean ani kompilacji całego tomu; status nie oznacza formalnego poświadczenia twierdzeń. Przy zmianie źródła lub zależności należy ponownie sprawdzić odpowiednie kryteria i CI.

Następny rozdział: 05 — Równanie falowe, chapters/pl/partial_differential_equations/05-rownanie-falowe.tex. Najpierw preflight i audyt pierwszych sekcji. Postęp: 4/33 rozdziałów ustabilizowanych.
