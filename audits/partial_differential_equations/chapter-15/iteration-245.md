# RRC 15 — iteracja 245: pierwsza lektura 001–012

Źródło przed dc6a563828084666ec50b3ba0c0ee6136cf84019 (584 wiersze), po bc36c10758a5f47b5594b407aff0162558f4f482 (673 wiersze); commit 0cc7e6672717306cc00777ac0e1d6af3177290c8.

Plan 64 kryteriów: 001–012 model, ilorazy i kryterium; 013–024 regularność wewnętrzna H²; 025–029 Caccioppoli z prawą stroną; 030–036 bootstrap i gładkość; 037–043 spłaszczanie; 044–051 pochodne styczne; 052–058 globalna regularność, normalna i dane brzegowe; 059–062 kontrprzykłady; 063–064 podsumowanie i struktura. Szczegółowo odczytano sekcje 1–2 i tezy zależności RRC 07,09; dalsze sekcje zinwentaryzowano.

| Kryterium | Wynik pierwszej lektury |
|---|---|
| 001 | Dodano rzeczywistą konwencję dla funkcji i testów. |
| 002 | Jawny zbiór pełnej miary i mierzalność U; rozróżniono ograniczoność i eliptyczność. |
| 003 | Rozpisano rozszerzenie tożsamości słabej na H¹ o zwartym nośniku z lematu RRC 09, wraz z dwiema nierównościami ciągłości. |
| 004 | Zdefiniowano U_h, odległość od dopełnienia i przypadek U=R^d. |
| 005 | Rozpisano rachunek dla funkcji gładkiej także dla h<0, Cauchy–Schwarz, Tonelli i translację miary. |
| 006 | Zwarty zbiór całych odcinków, lokalne wygładzanie RRC 09 i jawne oszacowanie normy różnicy ilorazów przy ustalonym h. |
| 007 | Poprawiono hipotezy dyskretnego całkowania przez części: v lokalnie L² bez zwartego nośnika, w o zwartym nośniku K i K+h e_j zawartym w U. |
| 008 | Wykazano istnienie całek i dokładną zamianę zmiennych z przedłużeniem testu przez zero. |
| 009 | Rozpisano trzy równości dla testu gładkiego dowodzące komutacji z pochodną słabą. |
| 010 | Kryterium: ustalono K,K' i V, ograniczony ciąg w L²(V), wybór słabo zbieżnego podciągu. |
| 011 | Wykazano jednostajną i L² zbieżność ilorazów testu z kontrolą wspólnego nośnika, identyfikację pochodnej i półciągłość normy. |
| 012 | Sklejenie reprezentantów na przeliczalnym podpokryciu oraz skończone pokrycie zwartych podzbiorów. |

23 etykiety zachowane w kolejności, 21/21 odsyłaczy do 16 celów jednoznacznie rozwiązanych w sprawdzonych plikach RRC 07,09,12,13,15; poprawny stos środowisk. Pierwsza lektura 12/64, z poprawkami. Nie wykonano kompilacji PDF, dedykowanego CI ani globalnego CI. W kolejnych sekcjach do szczegółowej kontroli: dziedziny przesunięć i lokalne normy, testy przy płaskim brzegu, odzyskanie pochodnej normalnej bez mnożenia dowolnej dystrybucji przez współczynnik Lipschitzowski. Następna iteracja 246: kryteria 013–024.
