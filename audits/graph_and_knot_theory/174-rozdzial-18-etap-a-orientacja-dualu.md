# Audyt 174 — drukowany rozdział 18, etap A (stabilizacja)

Data: 2026-11-24. Kontynuacja 173, plan 118.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.
Commit źródłowy 5598a1a21fba5efdcbf5dc4634b77a2f3446e654; blob 6b1432759c141023f49a64fde0b16d9e8af1653a.
Commit regresji 848ae3f2770383c77840229d1a7d44b35b11e1f9.

## Korekty stabilizacyjne
- Ustalono dodatni porządek sigma przy wierzchołkach, obchód sigma alpha z wnętrzem ściany po prawej i jego relację z dodatnim brzegiem komórkowym.
- Przy oznaczeniu dualnych półkrawędzi przez prawe boki pierwotnych: zachowanie orientacji daje sigma*= (sigma alpha)^(-1), sigma**=alpha sigma alpha; po zmianie etykiet przez alpha odtwarzamy pierwotny układ. Odwracanie orientacji przy każdej dualizacji daje sigma*=sigma alpha, sigma**=sigma. Poprzednia formuła wymagała jawnego określenia konwencji.
- Rozwinięto dowód komórkowości dualu przez rozcięcie dysków charakterystycznych i sklejenie sektorów wokół pierwotnego wierzchołka; uwzględniono jednokrawędziowy obchód.
- Poprawiono sformułowanie kryterium mostu i znaki dodatniego brzegu.
- Ponownie sprawdzono argument całkowitej redukcji po drzewie dualnym: zmiana konwencji nie narusza surjektywności operatora różnic ani niezależności bazy.
- Bez rozszerzania zakresu; 43 poprawnie zagnieżdżone pary środowisk, 14 etykiet. Ponowny odczyt potwierdził blob.

## Rzeczywiste regresje
GKT-18-ORIENT-01, test_gkt18_dual_orientation.js, blob 0cab4cf8db92f35c060f7e66e836d18f10ec0cf2: PASS total=2546, connected=2221, signChecks=6177. Sprawdzono obie konwencje podwójnego dualu, odpowiedniość cykli i wierzchołków, znaki i ciągłość dodatnich obchodów oraz d1 d2=0.
Po dwóch konfliktach HTTP 409 przy próbie aktualizacji TC-01 zachowano go bez zmian i zapisano osobny test. Oba pliki potwierdzono odczytem; wyniki TC-01 nie są dowodem znaków nowej konwencji, za które odpowiada ORIENT-01.
Ponowiono wszystkie cztery zapisane funkcje testowe w JS po pobraniu z gałęzi, z zastąpieniem wyłącznie końcowego logu zwracaniem wyniku, a w BRIDGE-01 także importu Node równoważną asercją.
- BRIDGE-01: PASS 1067 mostów.
- ROT-01: PASS 7776 + 64 rotacje.
- TC-01: PASS 2546 prób, 2221 spójnych, 4442 rozkłady, 8996 elementów bazy, 12354 relacje.
- ORIENT-01: PASS jak wyżej.
Nie sumować nakładających się prób. Nie jest to formalizacja Lean ani dowód geometryczny.

## CI i PDF
Poprzedni pełny przebieg 45491866148 (commit 2c580a4) zakończył się SUCCESS. Nie dotyczy nowego blobu.
Nowy pełny przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45493653876 dla 5598a1a jest in_progress. Terminologia polska 45493653790 SUCCESS. Nie pobrano i nie obejrzano PDF z nowego commitu.
Etap A pozostaje otwarty. Następnie: kontrola geometrycznego dowodu komórkowości i znaku orientacji na konkretnych przykładach oraz weryfikacja CI i rzeczywistego PDF, bez rozbudowy zakresu. Po spełnieniu bramki etap B.
