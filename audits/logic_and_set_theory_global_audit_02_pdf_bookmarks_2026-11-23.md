# Logika matematyczna i teoria mnogości — audyt techniczny 02: kotwice i zakładki PDF

**Data:** 23 listopada 2026 r. (Europe/Warsaw).  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** książka `books/pl/logic_and_set_theory.tex`, jej rzeczywisty PDF i log GitHub Actions, nagłówki rozdziałów 25, 27, 31. Bez rozszerzania materiału matematycznego.

## 1. Zamknięta usterka — zduplikowane kotwice stron

Na commicie `450775573e71c504b466320fd26e9469003c037e` w pliku głównym zastosowano `\\frontmatter` oraz `\\hypersetup{pageanchor=false}` wyłącznie dla strony tytułowej; kotwice włączono ponownie przed spisem treści. [Rzeczywiste CI 45081904405 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081904405). W logu kompilacji występuje **0** ostrzeżeń `destination with the same identifier` (wcześniej były ostrzeżenia `page.1`–`page.9`, a po przejściowej poprawce `page.i`). Otrzymano 337 stron PDF, 0 `Overfull \\hbox`, 0 `Missing character`, brak błędów kompilacji.

Nie zmieniano numeracji rozdziałów, ich etykiet ani odsyłaczy.

## 2. Nowa wykryta usterka — tekst zakładek nawigacyjnych

Na tym samym, pomyślnym przebiegu CI wystąpiło **45 ostrzeżeń** `Package hyperref Warning: Token not allowed in a PDF string (Unicode)` w trzech przebiegach kompilatora `pdflatex`. Log wskazuje tylko sześć unikalnych miejsc:

| Rozdział | Wiersz pierwotny | Nagłówek |
|---|---:|---|
| 25 | 516 | Twierdzenie o rekursji na `$\\omega$` w ZF |
| 27 | 426 | Dlaczego `$\\N$` i `$\\R$` nie są równoliczne? |
| 31 | 218 | Dlaczego definicja `$L$` nie daje jeszcze ZFC? |
| 31 | 239 | Odbicie formuł do poziomu hierarchii `$L$` |
| 31 | 340 | Dowód, że `$L$` spełnia aksjomaty ZF |
| 31 | 540 | Kanoniczny dobry porządek `$L$` i aksjomat wyboru |

Ostrzeżenia wynikają z matematycznego trybu `$` i komend matematycznych w tytułach `\\section`, kopiowanych do zakładek PDF.

**Naprawa minimalna:** do wskazanych sześciu nagłówków dodano `\\texorpdfstring{...}{...}`, podając w drugim argumencie czytelny, zwykły tekst `omega`, `N`, `R`, `L`. Pierwszy argument pozostaje dokładnie tym samym wzorem matematycznym widocznym w składzie rozdziału. Nie zmieniano `\\label`, struktur dowodowych ani żadnej treści.

Zmodyfikowane pliki i aktualne bloby:

- `chapters/pl/logic_and_set_theory/25-aksjomaty-zf-zfc-i-konstrukcje-zbiorowe.tex` — `19c0e18ad9ced232d7346dc19302e7ab8507e2fb`; commit `69a4be17ad6dc1d3af7f62892936db2e0284de3b`.
- `chapters/pl/logic_and_set_theory/27-liczby-kardynalne-i-arytmetyka-mocy.tex` — `e70779db56c87addcaf47d6e8e0bdec9b0a6a9d5`; commit `c7e54397e924a01d276f163e4e4333a8aa2a3103`.
- `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex` — `03dae2a901f115eacdff67058f96717f3323e4f8`; commit `d1d01db3ba9b777c0ed2b2b2f2311aa9c01efd20`.

Po zmianach sprawdzono ponownie źródła: 994, 686, 2537 wierszy; odpowiednio 46, 24, 68 etykiet i 25, 16, 87 odsyłaczy — wszystkie liczby niezmienione. W każdym pliku jedyną edycją były tytuły sekcji w podanych miejscach.

## 3. Kontrola dodatkowa

Przejrzano nagłówki `\\chapter`, `\\section`, `\\subsection`, `\\subsubsection` wszystkich 39 rozdziałów; dokładnie powyższe sześć zawierało matematykę wymagającą osobnej serializacji do zakładki. Bez zmian w pozostałych 36 rozdziałach. W szczególności nie dotykano stabilnych wersji rozdziałów 37–39.

[Nowy CI na końcowym commicie `d1d01db3`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083552034) potwierdził sukces regresji rozdziałów, ale w momencie pierwszego zapisu raportu kompilacja PDF była jeszcze uruchomiona. **Nie ogłaszamy zera ostrzeżeń zakładek, zanim nie zostanie odczytany log tego konkretnego CI.**

## 4. Werdykt etapowy

Naprawa zduplikowanych kotwic stron została potwierdzona pełnym CI. Naprawa zakładek zawiera sześć minimalnych korekt w trzech rozdziałach i oczekuje na weryfikację kompilacją oraz odczytem logu. Zmiany są wyłącznie redakcyjno-techniczne; twierdzenia, dowody i etykiety pozostają nienaruszone. Sukces CI i PDF nie stanowi formalizacji Lean.
