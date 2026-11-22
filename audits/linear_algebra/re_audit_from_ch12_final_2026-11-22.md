# Algebra liniowa — raport końcowy ponownej sekwencji audytów rozdziałów 12–32

**Data:** 2026-11-22. **Repozytorium:** `dariusz-piekarz/mathematical_scipts`. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Status:** **SEKWENCJA ZAKOŃCZONA**. Według dziennika postępu wszystkie rozdziały **12–32 STABILNE**: co najmniej dwa kolejne czyste audyty po ostatniej zmianie każdego źródła oraz zielone CI dla właściwego bloba. Dla rozdziałów 29–32 przeprowadzono dodatkowe sceptyczne audyty końcowe.

## Ostatnia część sekwencji — dowody zamknięcia

- **LA-28**: dodatkowy audyt na życzenie użytkownika poprawił sformułowania o nośniku ciągu wejść i interpunkcję; po korekcie dwa czyste audyty 05–06. Blob `b9507aa2db7eda554446248996e7c0ae241d4e73`, dedykowane CI 45038348657 success.
- **LA-29**: dwa czyste audyty 01–02 i dodatkowy sceptyczny audyt 03; blob `55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd`, CI 45023597804 success. W dzienniku odnotowano również wizualny przegląd 8-stronicowego PDF.
- **LA-30**: po równoległej korekcie kwantyfikatorów i poprawie napisu TikZ poprzednie audyty 01–02 starego bloba nie były zaliczane. Nowy blob `6d90013dd6c66d347e5ae2ac78b4c1a194aa979e` przeszedł dwa czyste audyty 03–04 i sceptyczny 05; CI 45039107786 success. Nowy poprawiony rysunek skompilowano i obejrzano osobno.
- **LA-31**: źródło `6c1d09b9eaf4083c9ebaa361dbf46fc350eae147`, dwa czyste audyty 01–02 i końcowy sceptyczny 03; 12 976 nowych testów PASS, CI 45039588413 success. Historyczny audyt 03 dokumentuje pełną wizualną kontrolę 14-stronicowego PDF tej samej wersji.
- **LA-32**: wykonano **zatwierdzone przez użytkownika rozszerzenie o Penrose'a** w commicie [d888e899](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d888e8992905ef3faa70414a8681374acc7c666e): lokalna skalarna transformata Penrose'a, jej jednorodność `−2`, dowód równania falowego `□_CΦ=0`, jawny przykład rezydualny `Φ=-1/det X`, oddzielenie od kohomologii `H¹(PT_U,O(-2))` oraz schemat konturu. Korekta rysunku w [commicie 6509cc74](https://github.com/dariusz-piekarz/mathematical_scipts/commit/6509cc74834f6c7a26eaff00d5c1ce41bc897107) usuwa kolizję etykiet. Finalny blob `8aea8bd8db02ca8677fb0547f770c9166fdaef88`, czyste audyty 02–03, dodatkowy sceptyczny audyt 04, **CI 45040651674 completed/success**. W bieżącej iteracji 6183 nowe testy PASS.

## Raporty LA-32

1. [Audyt 01 — rozszerzenie i korekta rysunku](re_audit_from_ch12/32_iteration_01_2026-11-22.md) — nieczysty, reset licznika po korekcie.
2. [Audyt 02 — pierwszy czysty](re_audit_from_ch12/32_iteration_02_2026-11-22.md) — 1/2.
3. [Audyt 03 — drugi czysty](re_audit_from_ch12/32_iteration_03_2026-11-22.md) — 2/2.
4. [Audyt 04 — sceptyczny końcowy](re_audit_from_ch12/32_iteration_04_2026-11-22.md) — czysty, 2+1.

## Zakres rzeczywiście wykonanych kontroli

Dla LA-32 w niezależnych skryptach Python sprawdzono jednorodność i przeskalowania reprezentanta spinorowego, niezmienniczość formy projektowej, pochodne mieszane, całkę rezydualną, odwrócenie orientacji i deformacje konturu bez biegunów, wyznaczniki Segrego/Kleina, incydencję, stereografię `S⁴` oraz strukturę kwaternionową. Skontrolowano 34 etykiety i 13 odsyłaczy, wszystkie rozstrzygnięte, oraz 49 poprawnie zagnieżdżonych par środowisk. **CI zakończyło się sukcesem dla dokładnego bloba.**

Nowy rysunek Penrose'a został skompilowany w pomocniczym jednostronicowym dokumencie i bezpośrednio obejrzany; 0 bloków poza stroną, bez widocznych kolizji. **Nie oglądano jednak wszystkich stron pełnego PDF książki po tym rozszerzeniu**, więc nie należy mylić sukcesu CI z nową, pełną wizualną inspekcją książki.

## Następny etap i reguła zatrzymania

Nowa sekwencja audytów **12–32 jest zamknięta**; **nie wracać automatycznie do 12**, nawet jeśli automatyzacja uruchamia się ponownie. Kolejna praca może dotyczyć osobnego audytu globalnego całego skryptu (spójność krzyżowych odsyłaczy, integracja, powtarzający się materiał, jakość całego PDF), ale powinna być prowadzona pod odrębnym zadaniem i nie oznaczać resetowania zakończonej sekwencji bez konkretnego nowego błędu.

Nie dodawać do zatwierdzonych rozdziałów innych, opcjonalnych tematów bez zgody użytkownika.
