# PDE-06 — iteracja 79: druga lektura 6.1–6.2

Data: 2026-11-25. Źródło rozdziału: 4adf037b29fc0e09a95fb435557bde958b761d09 (niezmienione względem CI 45571887161 i kontroli wizualnej). Ponowna lektura od wprowadzenia do końca 6.2; zakres bez rozszerzania.

| ID | Wynik drugiej kontroli semantycznej | Uzasadnienie |
|---|---|---|
| PDE-06-001 | PASS | Zmiana miary mnoży kwadrat normy przez (2pi)^d; inkluzja L² w L¹ przy masie 1; odcinek ma zwykłą miarę. |
| PDE-06-002 | PASS | Różnica całkowitych częstości daje zerową całkę poza przekątną; reszta ortogonalna do skończonej podprzestrzeni. Bessel bez założenia zupełności. |
| PDE-06-003 | PASS | Rozwinięcie kwadratu modułu liczy pary, współczynnik zerowy 1, dolne ograniczenie mianownika poza łukiem delta daje zanik masy; N=0 i punkty 2pi Z poprawne. |
| PDE-06-004 | PASS | Zmiana zmiennej odwraca granice z odpowiednim znakiem, całka po pełnym okresie niezmienna; masa 1 i jednostajna ciągłość dają oszacowanie niezależne od x. |
| PDE-06-005 | PASS | Regularność miary daje K i O wewnątrz odcinka; zwartość K zapewnia dodatnią odległość od dopełnienia O; błąd kwadratowy ograniczony miarą O bez K; przypadek pustego K poprawny. Okresowa aproksymacja jest ciągła. |
| PDE-06-006 | PASS | Wielomian należy do przestrzeni rzutu od pewnego N; Pitagoras i ciągłość normy dają Parsevala, bez wniosku o zbieżności punktowej. |
| PDE-06-007 | PASS | Znak (ik)^(-1) prawidłowy, wyrazy brzegowe znikają, wybór m co najmniej r+2 daje sumowalność, wyraz zerowy rozpatrzony oddzielnie; granica L² i ciągłość identyfikują pochodne. |
| PDE-06-008 | PASS | Tożsamość energii dla zespolonego X wymusza dodatnią rzeczywistą lambda; rozwiązanie ODE i oba warunki brzegowe dają dokładnie dodatnie indeksy, normalizacja sinusów L/2 poprawna. |
| PDE-06-009 | PASS | Skalowanie x=L theta/pi i nieparzyste przedłużenie zachowują zbieżność L²; c_-n=-c_n, c_n=-i/L razy całka sinusowa; grupowanie daje współczynnik 2/L. |
| PDE-06-010 | PASS | Pochodna kosinusa daje minus, całkowanie przez części drugi minus; Bessel dla ortonormalnych kosinusów nie wymaga zupełności. Pierwszy sinus osiąga równość. |

Sprawdzono również odniesienie do elementarnej nierówności Poincarégo w rozdziale 04 (lem:pde4-poincare): stała z osadzenia odcinka w sześcianie jest większa od ostrej stałej w 6.2. Nie wykryto nowych błędów matematycznych ani istotnych luk dowodowych w kontrolowanych sekcjach.

Wykryto jeden błąd formatowania rejestru: surowe pionowe kreski w zapisie modułu k rozbijały kolumny Markdown w PDE-06-003. Poprawiono na zapis słowny, bez zmiany kryterium; commit ddbeb74dd3a8c5e6154095ecd04aa9750cf261af, blob 6293e2798c2b66b9a7fd126670bea0988b76ba00. Wszystkie 42 wiersze mają cztery kolumny i zachowane ID. Źródło TeX, plik testów (ccbb8b39902904365b1403df5eefa10ff40d2134) i workflow (80e96a751f7cbc8418bd364888e2c17037b080b0) niezmienione. Wynik wykonania 10/10 z CI 45571887161 dotyczy tych samych wersji źródła i testów; nie uruchomiono ich ponownie w tej iteracji, nie potwierdzono jeszcze nowego CI po zmianie Markdown.

Druga lektura 2/9 sekcji, 10/42 kryteriów. Następna iteracja 80: 6.3–6.4, w szczególności periodyzacja Gaussa, dane L² i energia zespolonego równania falowego. Stabilizacja i audyt kontrolny otwarte. Nie wykonano Lean.
