# Geometria algebraiczna — ALG-00: dodatkowy sceptyczny cykl kontrolny 04 (23.11.2026)

**Źródło:** `chapters/pl/algebraic_geometry/00-teoria-pierscieni-od-arytmetyki-do-geometrii-rownan.tex`, blob `daedcd38d31e42c738df7f7d12a66d3994ebda8a` (1727 wierszy). **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Stan odziedziczony:** ALG-00–ALG-10 STABILNE/ZAMKNIĘTE, globalne III–IV bezusterkowe; nie resetowano licznika stabilizacji i nie otwierano nowego rozdziału.

## Przebieg i źródła

Odczytano najnowszy rejestr `audits/algebraic_geometry/STATUS.md`, raport ALG-00/15, globalny IV i kontrolę regresyjną 03; README, `catalog/books.json`, `books/pl/algebraic_geometry.tex`, standard `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, całe źródło ALG-00 oraz kanoniczne AA-09–AA-12. Zgodnie z zasadą reuse przyjęto wcześniejsze audyty AA jako podstawę dla argumentów algebraicznych, osobno kontrolując zastosowanie hipotez w ALG-00. Nie zmieniano AA.

**Kontrola konstruktywna:** sprawdzono strukturę rozdziału od definicji pierścienia i ilorazu przez Bézouta, CRT, pierwszość/maksymalność ideałów, pierwiastnik, dzielenie wielomianów, ideały punktów, parabolę i dwie osie aż po lemat Gaussa i UFD. Weryfikowano m.in. konwencję pierścienia zerowego, wyłączenie go z definicji dziedziny i ciała, poprawność sklejania ilorazu, brak domniemanego Nullstellensatzu nad ciałem niealgebraicznie domkniętym, brak identyfikacji funkcji wielomianowych z formalnymi wielomianami nad ciałem skończonym oraz szczególny przypadek F=0 w końcowej uwadze. Nie wykryto w przeczytanych fragmentach jednoznacznej nowej usterki.

**Niezależna kontrola sceptyczna:** ponownie wyprowadzono kluczowe przejścia w dowodzie Gaussa: pierwotność iloczynu przez redukcję modulo element pierwszy, redukcję mianownika w K[T] i wykazanie, że pierwotne czynniki nierozkładalne w A[T] pozostają nierozkładalne w K[T]. Skontrolowano argument, że izomorfizm k[x,y]/(y-x²) ≅ k[t] jest izomorfizmem formalnych pierścieni także nad F₂; zweryfikowano niezależnie jądro podstawienia do punktu przez teleskopowanie i kontrprzykład k[x,y]/(xy) z niezerowymi dzielnikami zera. Sprawdzono, że klasyfikacja maksymalnych ideałów punktowych nie jest niejawnie użyta przed słabym twierdzeniem Hilberta o zerach. Wcześniej zatwierdzone mapowanie reuse: ALG-00 CRT/ideały→AA-09; Bézout/PID→AA-10; wielomiany/Gauss/UFD→AA-11; pierwiastniki→AA-12. Nie ma podstaw do kopiowania kanonicznych rozdziałów.

## Testy i integracja

W lokalnym Python/SymPy uruchomiono **15 311 zakończonych pomyślnie asercji**: kryterium jednostek modulo n dla 2≤n≤120, skończone ciała i liczności zbiorów xy=0 oraz y=x², kongruencje, bijekcję CRT modulo 12, wielomianowe dzielenie przez y−x² i kombinatoryczny warunek w dowodzie pierwiastnika. To niezależne skończone regresje, nie dowód ogólny ani Lean.

Aktualny manifest zawiera dokładnie 11 rozdziałów ALG-00–ALG-10; entrypoint istnieje. Aktualne pięć ostatnio zwróconych przez GitHub Actions przebiegów na tej gałęzi miało `completed/success`, ale dotyczyły **innych commitów i workflow**, więc nie są bieżącym testem LaTeX ALG-00. Starszy dedykowany audyt ALG-00/15 dokumentuje 22-stronicowy PDF i dwukrotny skład dla wcześniejszego źródła, a globalny IV dokumentuje dwa 184-stronicowe PDF na niezmienionym źródle. **Nie pobrano nowego PDF ani nie wykonano teraz dwóch nowych przebiegów LaTeX.** Próba `git ls-remote` z lokalnego kontenera zakończyła się błędem DNS `Could not resolve host: github.com`; sam `pdflatex` jest zainstalowany, ale brak lokalnej kopii repozytorium. Nie wolno uznać tego za nowy pełny odbiór składu lub wizualny PASS.

## Wynik, ograniczenia i statusy

**Wynik tej kontroli:** nie wykryto uzasadnionej nowej korekty .tex; źródło pozostawiono bez zmian. To rzeczywista kontrola regresyjna i niezależne testy, **nie nowy pełny audyt stabilizacyjny**, ponieważ nie wykonano aktualnej dwukrotnej kompilacji ani oglądu stron PDF. Wcześniejsze decyzje o stabilności zachowano bez deklarowania nowego PASS. Liczba czystych pełnych audytów od ostatniej poprawki nie zwiększa się w tej iteracji. Osobny audyt końcowy globalny IV pozostaje udokumentowany.

| Rozdział | Udokumentowany status przed kontrolą | Status po kontroli |
| --- | --- | --- |
| ALG-00 | STABILNY/ZAMKNIĘTY, audyt 15 + globalne III–IV | bez zmian; kontrola 04 bez nowej usterki |
| ALG-01–ALG-04 | STABILNE/ZAMKNIĘTE | bez zmian; poza zakresem |
| ALG-05–ALG-07 | STABILNE/ZAMKNIĘTE | bez zmian; poza zakresem |
| ALG-08–ALG-10 | STABILNE/ZAMKNIĘTE | bez zmian; poza zakresem |

**Następny krok:** tylko rzeczywiste nowe regresje lub audyt przekrojowy; nie otwierać ALG-00 dla ponownego dowodzenia AA-09–AA-12 bez wskazania konkretnej wady. Przy dostępności artefaktu PDF sprawdzić na nowo wszystkie strony ALG-00, w tym sześć diagramów TikZ, i wykonać dwa przebiegi LaTeX na identycznym SHA.
