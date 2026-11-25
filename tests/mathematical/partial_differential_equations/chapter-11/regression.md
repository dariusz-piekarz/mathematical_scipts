# Rozdział 11 — trwały rejestr kryteriów regresyjnych

Kryteria semantyczne są punktami ręcznego audytu matematycznego, a nie formalnymi dowodami wykonywanymi przez CI. Pierwsza lektura, następnie druga stabilizacyjna i niezależna trzecia, testy wykonywalne tam, gdzie mają sens, kontrola strukturalna oraz kompilacja i kontrola PDF.

| ID | Kotwica | Kryterium | Typ |
| --- | --- | --- | --- |
| PDE-11-001 | sec:pde11-weak | Rzeczywiste przestrzenie, ograniczony obszar Lipschitzowski, V=H_0^1, jawna stała Poincarégo, dodatnia określoność iloczynu energetycznego. | semantyczna |
| PDE-11-002 | sec:pde11-weak | Równoważność norm i zupełność przez domkniętość H_0^1 w H^1; zależności z rozdziałów 09 i 10. | semantyczna |
| PDE-11-003 | def:pde11-dual | Ograniczoność a ciągłość funkcjonału, norma supremum, dodatnia określoność, jednorodność i nierówność trójkąta. | semantyczna |
| PDE-11-004 | def:pde11-dual | Słabe rozwiązanie i norma H^{-1} względem normy energetycznej; poprawny kierunek obu nierówności porównania norm funkcjonału. | semantyczna |
| PDE-11-005 | def:pde11-dual | Iniektywne ograniczenie funkcjonałów H^{-1} do dystrybucji, oszacowanie na testach o wspólnym zwartym nośniku, gęstość. | semantyczna |
| PDE-11-006 | ex:pde11-poisson-weak | C² na otoczeniu domknięcia, H¹ i zerowy ślad przez gładkie odcięcie, splot, zbieżność jednostajną i ciągłość śladu. | semantyczna |
| PDE-11-007 | ex:pde11-poisson-weak | Całkowanie przez części dla testów, oba oszacowania ciągłości, aproksymacja w V i przejście do granicy. | semantyczna |
| PDE-11-008 | ex:pde11-poisson-weak | Równość dystrybucyjna -Delta u=f z poprawnym znakiem, interpretacja ogólnego F, zerowy ślad oraz rozróżnienie istnienia i regularności. | semantyczna |
| PDE-11-009 | lem:pde11-projection | Skończone infimum, ciąg minimalizujący, wypukłość, tożsamość równoległoboku, Cauchy, domkniętość i jednoznaczność. | semantyczna |
| PDE-11-010 | lem:pde11-projection | Charakterystyka rzutu nierównością wariacyjną w obie strony; ortogonalność przy podprzestrzeni. | semantyczna |
| PDE-11-011 | thm:pde11-riesz | F=0, domknięte właściwe jądro F niezerowego, rzut x na jądro i niezerowy wektor prostopadły, F(e) != 0. | semantyczna |
| PDE-11-012 | thm:pde11-riesz | Konstrukcja reprezentanta przez odjęcie składowej e; jednoznaczność przez podstawienie różnicy, równość norm, liniowość i surjektywność izometrii. | semantyczna |

## Iteracja 167 — pierwsza lektura 001–012
Odczytano aktualny rozdział 11 (966 wierszy przed zmianami), potwierdzono włączenie do książki na pozycji 11. Nie znaleziono dotychczasowego rejestru chapter-11/regression.md (404). Źródło przed b06d7b5554c8b06dc80c53dea0050681bc971f61, po f0e5cde93e447288a38ec2d86bc32a12968138cd, commit c9f1a3afb35242d756013126e8d7734e2cc86126. Czternaście dokładnych zmian w pierwszych dwóch sekcjach: norma energetyczna i jej zupełność, norma funkcjonału oraz konwencja H^{-1}, dystrybucje, przynależność klasycznego rozwiązania do H_0^1, przejście przez gęstość, znak dystrybucyjnego laplasjanu, pełna charakterystyka rzutu i dowód Riesza. Zachowano 36 etykiet (unikatowe) w tej samej kolejności, 24 wystąpienia odsyłaczy rozwiązane w 09, 10, 11, 13; odsyłacz thm:pde13-nonhom rzeczywiście istnieje, jego użycie merytoryczne będzie kontrolowane we właściwej sekcji. Stos środowisk poprawny, treść od sekcji Laxa–Milgrama bez zmian. Nie uruchamiano testów wykonywalnych, CI, kompilacji ani Lean. Następna iteracja: twierdzenie Laxa–Milgrama, przypadek H={0}, konstrukcja kontrakcji i oszacowanie stabilności, następnie formy eliptyczne. Rejestr 12 kryteriów pierwszej lektury; ostateczna liczba kryteriów rozdziału jeszcze nieustalona.
