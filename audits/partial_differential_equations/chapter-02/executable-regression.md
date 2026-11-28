# PDE-02 — testy wykonywalne i CI (iteracja 19, 2026-11-24)

Aktualne źródło rozdziału: blob 8d8f7eeba02165411ad2a74b1df692b52aebaa0d, bez zmian w tej iteracji. 19 kryteriów semantycznych pozostaje w regression.md.

Dodano [test_characteristics.py](../../../tests/mathematical/partial_differential_equations/chapter-02/test_characteristics.py), commit b8ad88938d18618db3388c48ad1431ef3e293b01. Lokalnie wykonano python test_characteristics.py -v: 6/6 OK; SHA Git blob pliku lokalnego i wersji repozytorium identyczne: 805ac866415f304d7df385a0c0d4530db0a25c92.

| Test | Kryteria | Zakres |
|---|---|---|
| Dylatacja | 004–006 | 27 kombinacji a,d,t, dodatniość i granice J, gęstości ze znakiem, normy |
| Burgers | 009 | 20 kombinacji t,xi, dodatniość X_xi, tożsamość gradientu |
| Fala rozrzedzenia | 010 | 15 przypadków, dokładna całka funkcji odcinkami liniowej, oszacowanie śladu |
| Rankine–Hugoniot | 011 | 42 pary różnych stanów, wkłady brzegowe i zmiana prędkości |
| Charpit | 012–013 | 343 kombinacje p,dx,dp dla F=p²+u-x, zachowanie F i R |
| Hamilton | 017–018 | 21 kombinacji t,xi i 3 wartości r, PDE i brak ciągłego przedłużenia |

Są to skończone kontrole wzorów na wybranych przykładach, nie dowody twierdzeń ani testy bezpośrednio parsujące wszystkie formuły źródłowe.

Dodano [workflow](../../../.github/workflows/partial-differential-equations-ch02.yml), commit 64921e6aea062fadc97125321bd6111b9d19e4c9. Zawiera uruchomienie testów, kontrolę etykiet, odsyłaczy, środowisk, ciągłości ID i kotwic kryteriów, kolejności manifestu i kanonicznego listings w obu preambułach PDE, samodzielną kompilację rozdziału 02 z właściwym numerem, diagnostykę i renderowanie. Zewnętrzny cel chap:pde-code jest sprawdzany w rzeczywistym rozdziale 33, a jego numer wyznaczany z kolejności wejść książki; w izolowanym PDF nie odtwarza się numeru strony ani działającego hiperłącza do nieobecnego rozdziału.

Stan CI w chwili sprawdzenia: 45424483056: in_progress/brak wyniku.
Nie potwierdzono jeszcze wykonania nowego workflow ani pełnej kompilacji i renderowania aktualnego rozdziału. Lean nie uruchomiono. Nie zamykano rozdziału.
