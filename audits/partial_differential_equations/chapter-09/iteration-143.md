# PDE — rozdział 09 — iteracja 143: walidacja rysunku i audyt kontrolny 001–022

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: blob b14ed2a90f238b9b1429b49712f6b933b1075bf4, commit korekty 9c038ce99e782076460e1ea49b74f8c3d0cce393.

## CI i PDF
Run 45612339952: success, head 9c038ce99e782076460e1ea49b74f8c3d0cce393. Artefakt 15020293358 pobrany; lokalny SHA-256 14eb322e0162e17cab09079fb5f7e195132848a00883722e2bfd14ac10859016 zgodny z metadanymi API.
PDF 25 stron A4. Porównano obrazy wszystkich stron z artefaktem 15020078686 przez ImageChops.difference: 24 strony identyczne pikselowo; jedyna różnica na stronie 9, bbox (570,884,623,914) w renderze 120 dpi. Obejrzano poprawioną stronę 9: etykieta B_epsilon(x) czytelna, wewnątrz U, bez kolizji. Brak krytycznych diagnostyk LaTeX z listy workflow; 25 ostrzeżeń hyperref (puste cele linków zewnętrznych w izolowanym rozdziale), jedno Underfull hbox, badness 1142. Pełnej książki nie kompilowano.

## Niezależna lektura kontrolna (bez zmian źródła)
| Kryteria | Wynik i uzasadnienie |
| --- | --- |
| 001–003 | Bez zmian. Zakres hipotez, klasy a.e., znaki wielowskaźnikowe i końce zakresu p, aksjomaty normy, przypadek k=0 sprawdzone. Definicja def:pde7-weak odczytana w źródle rozdziału 07 i zgodna. |
| 004–006 | Bez zmian. Restrykcja przez przedłużenie testów, przeliczalne sklejanie z rozłącznymi A_n, skończone podpokrycie i identyfikacja na U zawierającym nośnik testu; W_0 tylko dla p skończonego, bez identyfikacji z jądrem śladu. |
| 007 | Bez zmian. Stałe równoważności norm i czynnik (2pi)^(-d), równość dla k=0,1; sprawdzono treść thm:pde8-Hs (punkt 4) i konwencję Plancherela w aktualnym źródle 08. |
| 008 | Bez zmian. Odczytano ex:pde7-heaviside: delta_0 i 2 delta_0 z właściwym znakiem, brak regularności; ograniczoność abs(x) i sign(x) na I. |
| 009–012 | Bez zmian. Rachunki radialne: ap<d, (a+1)p<d, przypadki równości; wewnętrzna normalna -x/abs(x), wyraz brzegowy epsilon^(d-1-a) zanika przy hipotezie wystarczającej; konieczność przez restrykcję poza singletonem, nie przez nieudowodnione globalne różniczkowanie. |
| 013–015 | Bez zmian. Zupełność przez skończony produkt L^p, granice na testach także dla p=1,infty; iloczyn skalarny i zamkniętość pojedynczej pochodnej na naturalnej dziedzinie. |
| 016 | Bez zmian. Testy z eta o całce 1 i psi(0)=1, wspólne zwarte otoczenie, kurczące się pasy i absolutna ciągłość całki; błąd gładkiej aproksymacji skoku. |
| 017–018 | Bez zmian. Pierwotna U absolutnie ciągła i ograniczona, słaba pochodna przez iloczyn z testem; thm:pde7-constant sprawdzone w źródle 07, dotyczy przedziału i dokładnie jednej stałej; odwrotna implikacja oraz jednoznaczność również na końcach. |
| 019–020 | Bez zmian. Minimum modułu i stałe z długością przedziału, ewaluacje liniowe przez jednoznaczność, przypadek p=infty, najlepsza stała Lipschitza. |
| 021–022 | Bez zmian. Przykład potęgowy dla dowolnego gamma>0, funkcja Cantora: zbiór wyjątkowy miary zero i sprzeczność z przyrostem; poprawny zakres włożenia w W^1,1. |

Bilans: 22/22 kryteria skontrolowane w trzeciej lekturze, 0 nowych usterek w tym zakresie, bez zmian źródła. Kontrola jest semantyczna i nie stanowi formalizacji Lean ani niezależnej recenzji przez inną osobę.
Następna iteracja 144: lektura kontrolna od PDE-09-023. Nie zamykać rozdziału przed kontrolą pozostałych 59 kryteriów.
