# Geometria algebraiczna — ALG-00: kontrola regresyjna 03 (23.11.2026)

**Zakres:** jeden rozdział ALG-00, kanoniczny plik `chapters/pl/algebraic_geometry/00-teoria-pierscieni-od-arytmetyki-do-geometrii-rownan.tex`, blob `daedcd38d31e42c738df7f7d12a66d3994ebda8a`, 1727 wierszy. **Status wcześniejszy:** stabilny / zamknięty, audyt rozdziałowy 15, globalne III i IV bez usterek. Nie otwarto ponownie rozdziału.

**Materiały odczytane:** bieżący STATUS, raport rozdziałowy 15, globalny IV, README, katalog `catalog/books.json`, entrypoint `books/pl/algebraic_geometry.tex`, całe źródło ALG-00 oraz standard **`application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`** (właściwa lokalizacja; wcześniejsze raporty błędnie uznawały go za nieodnaleziony). Porównano semantycznie kryteria dowodów AA-09–AA-12 w obszarach CRT, Bézout, Gauss/UFD i pierwiastników; nie zmieniano źródeł AA.

## Rzeczywiste kontrole

1. Przeanalizowano źródłowe sformułowania i argumenty w częściach dotyczących konstrukcji pierścieni i ilorazów, podzielności, ideałów pierwszych/maksymalnych, pierwiastników, dzielenia wielomianów, ewaluacji, paraboli, dwóch osi, lematu Gaussa i UFD. Weryfikacja szczególnie uwzględniła hipotezy: przemienność, jedynka, dziedzina, nieskończoność ciała, algebraiczna domkniętość i rozróżnienie wielomianu od funkcji. Nie wykryto w przeanalizowanych argumentach jednoznacznej nowej usterki.
2. Sprawdzono konstrukcję mapy `ev_a`, jej jądro i ideał punktu; wzór teleskopowy na `f(x)-f(a)`; `k[x,y]/(y-x²)≅k[t]`; kontrprzykład nad F₂; dzielniki zera w `k[x,y]/(xy)`; argument przeciw główności `(x,y)`; dowód dwumianowy pierwiastnika oraz przejście `K[T]` → `A[T]` w lemacie Gaussa.
3. Wykonano **13 227** własnych, zakończonych bez asercji testów arytmetycznych w lokalnym Python/SymPy: jednostki modulo n dla 2≤n≤150, własności dziedzin F_p dla p∈{2,3,5,7,11,13,17,19,23}, reszty z dzielenia przez x−2 i przypadki brzegowe. To testy skończone, nie formalny dowód.
4. Manifest wymienia dokładnie ALG-00–ALG-10 i wskazuje istniejący entrypoint. Aktualnie sprawdzone ostatnie pięć przebiegów CI miało status completed/success, lecz dotyczyły wcześniejszych SHA niż odczytany HEAD; nie są dowodem kompilacji tego raportu ani bieżącej gałęzi.

## Ograniczenia i decyzja

**To kontrola regresyjna, nie nowy pełny audyt stabilizacyjny.** Nie przeprowadzono w tym przebiegu nowej dwukrotnej kompilacji LaTeX, pełnego niezależnego ponownego odczytu wszystkich 33 dowodów i wizualnego oglądu aktualnego PDF; nie należy raportować ich jako PASS. Dostępny lokalnie `pdflatex` nie miał lokalnej kopii repozytorium, a GitHub był dostępny wyłącznie przez konektor. Nie wprowadzano zmian do `.tex`, ponieważ nie znaleziono uzasadnionej usterki. Zachowano wcześniejszy udokumentowany status STABILNY / ZAMKNIĘTY, bez resetowania licznika stabilizacji. Zapis niniejszego raportu nie jest nowym certyfikatem pełnego audytu.

**Mapowanie reuse:** ALG-00 pierścienie/CRT → AA-09; Bézout/podzielność → AA-10; wielomiany/Gauss/UFD → AA-11; pierwiastniki → AA-12. Przy przyszłych korektach trzeba osobno potwierdzić hipotezy, integrację i PDF.
