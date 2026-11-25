# RRC 13 — iteracja 214: druga lektura 055–064 i podglądy rysunków Atlasu

Źródło RRC 13 przed a4fff04a3e8411265b94d3b76a68221dc6593971, po 0d043dbb12a1667ff75ffed3d3415a55566983c6; commit cbd40c94c4e7aceec0b21ab533e8124f8bcea8b5.

| Kryterium | Wynik drugiej lektury |
|---|---|
| PDE-13-055 | Jawnie rozwiązano układ dla C,D. |
| PDE-13-056 | Sprawdzono obie wartości końcowe i ciągłość strumienia. |
| PDE-13-057 | Rozpisano całkowanie przez części z członem skoku u oraz warunek zerowego śladu i jednoznaczność. |
| PDE-13-058 | Wyprowadzono maksimum x=-3/10, u=49/200; dane TikZ zgodne z rachunkiem. |
| PDE-13-059 | Rozpisano znak i współczynnik delty w u'', rozróżniono pochodną strumienia. |
| PDE-13-060 | Uporządkowano tezę jako równoważność równania globalnego z trzema warunkami, bez zakładania z góry kawałkami H². |
| PDE-13-061 | Ślady jednostronne i absolutna ciągłość poprawne. |
| PDE-13-062 | Oba kierunki równoważności i znaki brzegowe poprawne. |
| PDE-13-063 | Globalna regularność H¹ strumienia poprawna. |
| PDE-13-064 | Jawny warunek zgodności niejednorodnego Dirichleta w przypadku niekoercywnym oraz niezależność od przedłużenia. |

6 zamian blokowych. 1449 wierszy; 40 etykiet; 101/101 wystąpień odsyłaczy (50 różnych celów), jednoznaczne w RRC 06,07,09,10,11,12,13. Stos środowisk poprawny. Druga lektura 64/64; pierwsza 64/64. Nie deklarujemy stabilizacji.

## Zgłoszenie: brak rysunku RRC 02 w aplikacji

Odczytano źródło RRC 02 (blob cede0206acd0e122be62c5bd6af78df97fcf8eeb). Dwa bloki tikzpicture: krzywa początkowa i charakterystyki (wiersz 528) oraz zbliżanie się charakterystyk Burgersa (wiersz 784). W application/frontend/app.js funkcja simplifiedText usuwa znaczniki środowisk innych niż matematyczne, a renderMathPreview wywołuje KaTeX. KaTeX nie wykonuje TikZ. To jest konkretna przyczyna braku obsługi tych rysunków w podglądzie uproszczonym, niezależna od kompilacji książki. Nie stwierdzono awarii konkretnego komputera ani nie uruchomiono lokalnej instancji użytkownika.

Dodano cztery statyczne SVG odtworzone z geometrii i wzorów źródłowych, nie eksporty z kompilatora TikZ: pde02-characteristics.svg (2a95e366d5ed43aa6ebe137b2455f0d2e57a816a), pde02-burgers.svg (7a7808907a8a262a06da801fb54d256de162881e), pde13-interface.svg (c7181bc236775aeb72d6f383183becd9de919e40), pde13-solution.svg (42e87372f487fa455b2f4d01e847002b62e6915f), w application/frontend/figures/.

Commit 25aba40b5df27669eb04c93a4594e4e91f080170: pełny tekst bloku TikZ mapowany na jawnie dozwolony lokalny SVG; zachowanie wzorów przed i po rysunku; nieznany/zmieniony blok oraz błąd wczytania pliku pokazują rozwijalne źródło; brak uruchamiania TeX i brak innerHTML. Zgodność mapowania 4/4 z bieżącymi źródłami potwierdzona programowo. Rozwiązanie celowo ograniczone do czterech rysunków; pozostałe TikZ wymagają osobnych podglądów lub ogólnego procesu generowania.

Commit 1f363f3d684fc0dd3850b1fdeec3095a1816730e: rozszerzony rzeczywisty test Chromium w application/tests/browser_ci_e2e.py pobiera pełne rozdziały PDE-02 i PDE-13 przez API, sprawdza po dwa obrazy, dekodowanie i zachowanie KaTeX, a także fallback nieznanego rysunku. Przebiegi 45701105125 i 45701105079 były queued w chwili kontroli. Nie ma jeszcze potwierdzonego wyniku nowego testu przeglądarkowego. Nie wykonano kompilacji rozdziału 13, inspekcji PDF ani formalizacji Lean.

Następny etap: trzecia lektura 001–026 i odczyt wyniku CI aplikacji; przy niepowodzeniu najpierw naprawić regresję. Kontynuować inwentaryzację rysunków RRC, bez zastępowania ich surowego TikZ.
