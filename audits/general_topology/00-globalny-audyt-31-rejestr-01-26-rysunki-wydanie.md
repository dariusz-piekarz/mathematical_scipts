# Topologia ogólna — audyt globalny 31: kompletny rejestr 01–26, rozbieżność ilustracji i najnowsze wydanie

**Data pomiaru:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Wspólny commit wszystkich 26 źródeł:** `e7ff9254923fd87f9cad05301b15704e7038befd`.
Po zapisaniu raportów 29 i 30 porównano ponownie SHA wszystkich 26 źródeł na aktualnej głowicy `c3ab0f7f921897546e2967b412532af9dcda1aa7`: **wszystkie pozostały identyczne**.

## I. Inwentarz na jednej wersji źródła

W tabeli `Proof` oznacza **liczbę środowisk** `\\begin{proof}`, `Figure` — liczbę środowisk `\\begin{figure}`, a `TikZ` — liczbę środowisk `\\begin{tikzpicture}`. Zliczenia nie są certyfikatem prawdziwości dowodów.

| Rozdział | Blob źródła | Proof | Figure | TikZ | Labels | Refs |
|---|---|---:|---:|---:|---:|---:|
| 01 — Przestrzenie topologiczne | `1e8ee853eb9915d96913e5a0a8cdb5e32f2ec5f6` | 9 | 2 | 2 | 50 | 7 |
| 02 — Operacje topologiczne na zbiorach | `53a8dc7e62590a9011bd5858eedb4141c5f38162` | 12 | 1 | 1 | 35 | 0 |
| 03 — Odwzorowania ciągłe | `b571753b5ab9a8777424fc32f6c4a54a4048af77` | 15 | 0 | 0 | 39 | 1 |
| 04 — Konstrukcje przestrzeni | `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` | 17 | 2 | 2 | 40 | 3 |
| 05 — Aksjomaty oddzielania | `462acd8f3e1e350478d921429118ec19ac7f4ca8` | 16 | 5 | 6 | 43 | 15 |
| 06 — Zbieżność topologiczna | `365204000d0d5b21f213132e58b71aa48db3910e` | 18 | 2 | 2 | 45 | 16 |
| 07 — Zwartość | `0c31028e8fd301d805781b676c6713a2572501cf` | 18 | 2 | 2 | 37 | 23 |
| 08 — Spójność | `51b5cd2adf19a0345510bd14d5c0ac318cef3ae1` | 15 | 2 | 2 | 42 | 19 |
| 09 — Aksjomaty przeliczalności | `f483271af93842198c094c95f73a68584e835215` | 10 | 2 | 2 | 33 | 10 |
| 10 — Metryzowalność | `1bc0fb72953cb70bcec7c60d3c2fc222ba1851c6` | 14 | 1 | 1 | 29 | 11 |
| 11 — Zupełność i twierdzenie Baire'a | `8f13420add065dca19d2653c86b0e5781aef2fe7` | 8 | 1 | 1 | 21 | 4 |
| 12 — Przestrzenie jednostajne | `13597073db07742089b82ae3fc9878733dea5e88` | 14 | 1 | 1 | 34 | 12 |
| 13 — Zupełność jednostajna i uzupełnienia | `c9078636452731e42a56196e84b5ed9831120e6b` | 9 | 0 | 0 | 24 | 5 |
| 14 — Zwartość lokalna | `24ca61f0e19fe6674719fc76e53073aa82cc755c` | 7 | 0 | 0 | 18 | 4 |
| 15 — Parazwartość | `82e0fb5be75489017c8ea1844c698c87ce580901` | 7 | 0 | 0 | 21 | 4 |
| 16 — Funkcje ciągłe i uzwarcenia | `1c2fcb925d62120feaea468400e48842a508a062` | 7 | 0 | 0 | 18 | 0 |
| 17 — Uzwarcenia Aleksandrowa i Čecha–Stone'a | `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4` | 10 | 0 | 0 | 20 | 3 |
| 18 — Przestrzenie odwzorowań | `f7340514548ed3dfb5d98793bf7068fd84276c30` | 9 | 0 | 0 | 18 | 1 |
| 19 — Przestrzenie polskie | `dd05dd723a4e92756d1e339309079c68a4580485` | 9 | 0 | 0 | 23 | 1 |
| 20 — Zbiory analityczne i operacja Suslina | `2607376331f94935063107dee49148b45cc1679f` | 11 | 0 | 0 | 23 | 23 |
| 21 — Topologie na rodzinach podzbiorów | `a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b` | 15 | 1 | 1 | 31 | 9 |
| 22 — Zbieżność zbiorów | `33765c2bb1b3065f4ad32596795c3d1981b48dda` | 11 | 1 | 1 | 28 | 20 |
| 23 — Wymiar topologiczny | `9dc1ed4784d929b405d00a3216865418f240a37c` | 20 | 1 | 1 | 40 | 23 |
| 24 — Grupy topologiczne | `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6` | 21 | 1 | 1 | 41 | 14 |
| 25 — Continua | `7b772123870296af95d3ce951ccddb65685af7aa` | 14 | 1 | 1 | 35 | 15 |
| 26 — Twierdzenie Hahna–Mazurkiewicza | `161d04d779ae86554f81c11bb24daa842c8dd363` | 9 | 1 | 1 | 22 | 19 |
| **SUMA 01–26** | — | **325** | **27** | **28** | **810** | **262** |

Zapis wymiarów bloków:
- **01–06:** 87 środowisk proof, 12 figure, 13 tikzpicture, 252 etykiety, 42 odsyłacze (rejestr globalny 27, uzupełniony w tej iteracji o bezpośrednie liczenie figure).
- **07–12:** 79 proof, 9 figure, 9 tikzpicture, 196 etykiet, 79 odsyłaczy (rejestr globalny 28).
- **13–18:** 49 proof, 0 figure, 0 tikzpicture, 119 etykiet, 17 odsyłaczy (nowy rejestr globalny 29).
- **19–23:** 66 proof, 3 figure, 3 tikzpicture, 145 etykiet, 76 odsyłaczy (nowy rejestr globalny 30).
- **24–26:** 44 proof, 3 figure, 3 tikzpicture, 98 etykiet, 48 odsyłaczy (bezpośrednie odczyty źródeł).

**Rozdziały 01–23:** **281 proof, 24 figure, 25 tikzpicture, 712 etykiet, 214 odsyłaczy**.
**Rozdziały 01–26:** **325 proof, 27 figure, 28 tikzpicture, 810 etykiet, 262 odsyłacze**.
Stara liczba 261 dowodów dotyczy innego, historycznego zestawu źródeł — nie należy jej stosować do aktualnego wydania.

## II. Uzgodnienie 24/27 ilustracji oraz 27/28 diagramów

W samym zakresie 01–23 są **24** podpisane rysunki, a w pełnym 01–26 jest ich **27**: rozdziały 24, 25 i 26 dodają po jednym.
W pełnej książce znajduje się **28 środowisk tikzpicture**, lecz tylko **27 środowisk figure**, ponieważ **pierwsze figure rozdziału 05 (podpis Rysunek 5.1) zawiera dwa odrębne diagramy TikZ pod wspólnym podpisem**. Nie jest prawdą, że dodatkowe TikZ występuje poza środowiskiem figure.
Powyższą różnicę zweryfikowano wprost z pełnego źródła rozdziału 05: pozostałe cztery figure zawierają po jednym tikzpicture. Wszystkie 28 środowisk TikZ jest wewnątrz 27 podpisanych figure.

## III. Nowy artefakt PDF z tego samego commitu

Bezpośrednio sprawdzony workflow: [General topology chapter validation #45129914798](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45129914798), commit `e7ff9254923fd87f9cad05301b15704e7038befd`, **completed/success**; job `137542804303` również `completed/success`.
Z GitHub Actions pobrano rzeczywisty artefakt **14797512262** `general-topology-ch01-ch26`: archiwum zawiera **26 PDF** (jedną pełną książkę i osobne rozdziały 02–26) oraz 26 logów LaTeX, razem 52 pliki.
- **Pełna książka: 188 stron A4.**
- Z tekstu PDF wydobyto **27 różnych podpisów Rysunek**: od 1.1, 1.2, przez 2.1, 4.1–4.2, 5.1–5.5, 6.1–6.2, 7.1–7.2, 8.1–8.2, 9.1–9.2, 10.1, 11.1, 12.1, po 21.1–26.1.
- Strony zawierające podpisane rysunki: **9, 15, 20, 33, 34, 39, 41, 43, 46, 48, 50, 52, 59, 64, 69, 73, 79, 81, 86, 92, 96, 144, 150, 160, 170, 180, 186**.
- W logach całej książki i wszystkich dostępnych rozdziałów nie znaleziono `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` ani `Fatal error`.
- Wykonano trzy plansze zbiorcze z wycinkami stron wokół wszystkich 27 rysunków i je obejrzano. Nie znaleziono oczywistych kolizji, obciętych diagramów ani przesłaniających je podpisów **na tym poziomie przeglądu**. Nie zastępuje to pełnorozdzielczej inspekcji każdego rysunku i wszystkich 188 stron.

Log najnowszego workflow potwierdza rzeczywiste uruchomienie kontroli globalnych: `PASS topology dependencies: 28 cross-chapter references, 810 labels...`; `PASS chapter 13 ... labels=810, refs=262` i `PASS chapter 15 ... labels=810, refs=262`. Testy weryfikują brak zduplikowanych etykiet i rozwiązywalność referencji na całym aktualnym katalogu; dodatkowe ręcznie sprawdzone relacje między rozdziałami 13–23 opisuje raport globalny 30.

## IV. Status matematyczny i otwarte warunki zakończenia

Wcześniejsze audyty indywidualne istnieją dla wszystkich rozdziałów 01–26; raporty globalne 15–25 odrębnie badają każdy dowód 14–23, a 13 ma udokumentowane 2+1 po korekcie. **Inwentarz 325 środowisk proof nie jest sam w sobie dowodem ich 325 niezależnych audytów.** W szczególności przed ogłoszeniem globalnego PASS trzeba jeszcze skorelować każdą pozycję dowodową z konkretnym raportem na tym samym blobie (szczególnie 01–12 i 24–26) oraz wykonać niezależny dodatkowy audyt matematyczno-redakcyjny finalnego zbioru. Zielony CI po każdej zmianie raportowej też trzeba odczytać oddzielnie; sukces workflow 45129914798 dotyczy zamrożonego commitu przed raportami 29–31.

**Wykonane:** pełny wspólny rejestr 01–26, wyjaśnienie wszystkich historycznych różnic liczników, rzeczywisty PDF z najnowszego pozytywnego CI i kontrola 27 podpisanych rysunków na planszach.
**Pozostaje:** macierz konkretnych dowodów → raportów wraz z SHA, ewentualne kontrole matematyczne bez pokrycia, pełna końcowa inspekcja ilustracji, niezależny audyt potwierdzający całości i CI finalnego HEAD. Automatyzacja ma pozostać aktywna.