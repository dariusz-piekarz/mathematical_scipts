# RRC 13 — iteracja 210: druga lektura 001–014

Źródło przed d9bc075e12576bb8fdd7613f60e568a1529791c9, po 66bf1ecc9a6bbe45d60d194d4ded5d49a2dbf37e; commit 7cff30cde5e035c5556dd57f6f2b3db5ad982092. Ponownie odczytano pierwsze trzy sekcje.

| Kryterium | Wynik drugiej lektury |
|---|---|
| PDE-13-001 | Wspólny zbiór pełnej miary poprawny; jawnie ograniczono cały rozdział do rzeczywistych przestrzeni i niepustego obszaru. |
| PDE-13-002 | Rachunek części antysymetrycznej i ograniczoność norm współczynników poprawne. |
| PDE-13-003 | Doprecyzowano konwencję symbolu oraz znaczenie zamrożonej macierzy dla mierzalnych współczynników. |
| PDE-13-004 | Zweryfikowano hipotezy reguły iloczynów z p=q=2 na kulach; przejście do lokalnego L² i znak zmienionego dryfu poprawne. |
| PDE-13-005 | Obie całki przez części i stały strumień poprawne. |
| PDE-13-006 | Rozpisano dowód, że delta nie jest generowana przez funkcję L², przez testy psi(nx); brak H² i zależność iloczynu od reprezentanta poprawne. |
| PDE-13-007 | Jawne nierówności między normą energetyczną i pełną oraz odpowiadającymi normami funkcjonałów. |
| PDE-13-008 | Dziedzina formy H¹×H¹ i oszacowanie M poprawne. |
| PDE-13-009 | Uzasadniono iniektywność L²→V* przez jednoznaczność dystrybucji regularnej. |
| PDE-13-010 | Jawna stała oszacowania na testach o nośniku w K i rząd dystrybucji co najwyżej jeden. |
| PDE-13-011 | Obie implikacje równoważności słabej i dystrybucyjnej poprawne. |
| PDE-13-012 | Znaki, wybór parametru Younga i stała Gamma poprawne. |
| PDE-13-013 | Koercywność po przesunięciu, ograniczoność, Lax–Milgram i oszacowanie poprawne. |
| PDE-13-014 | Usunięto pozostałe mylenie L+mu I z L+mu J:V→V*. Wyjaśniono warunek małości z RRC 11, przeliczenie stałej koercywności i parowanie z jądrem operatora transponowanego. |

7 zamian blokowych. Zachowano 40 etykiet w kolejności. 92/92 wystąpienia odsyłaczy (49 różnych celów) rozwiązane jednoznacznie w RRC 06,07,09,10,11,12,13. Stos środowisk poprawny. 81/81 pomocniczych kontroli skalarnych nierówności Gårdinga po przesunięciu; nie są dowodem ani testami CI. Źródło 1283 wiersze. Odczytano hipotezy twierdzeń RRC 09 o iloczynach i zupełności oraz RRC 11 o członach dolnego rzędu i Laxie–Milgramie.

Pierwsza lektura: 64/64; druga: 14/64. Następna: 015–028, Dirichlet, szczególnie lemat o komutacji śladu z częściami dodatnią i ujemną oraz kontrola przejścia granicznego w W^{1,1}. Nie wykonano kompilacji, dedykowanego CI, kontroli PDF ani Lean.
