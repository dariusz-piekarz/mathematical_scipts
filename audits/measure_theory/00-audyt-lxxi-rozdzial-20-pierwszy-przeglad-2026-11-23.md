# Audyt LXXI (71) — rozdział 20: pierwszy przegląd regularności i miar Radona

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts. Gałąź: biblioteka-matematyczna-iteracja-6.

## Bramka wejścia

Rozdział 19 zamknięto po audytach LXVIII–LXX na dokładnym blobie 7571e99edac729831e83e8061377757874cfb7bc. Przebieg CI 45273447471 potwierdził 8+4 testy, obie kompilacje PDF, a oględziny rzeczywistego PDF potwierdziły integralność nowego przykładu jądra warunkowego. Raport zamknięcia: audits/measure_theory/00-audyt-lxx-rozdzial-19-zamkniecie-2026-11-23.md, commit 4ef5bae9102be9bbf14d343a6182238e05a851df.

## Pierwszy niezależny audyt matematyczny rozdziału 20

Kanoniczny plik: chapters/pl/measure_theory/20-miary-borelowskie-regularnosc-i-miary-radona.tex.
Blob po poprawkach: b7eaf3a8c6fc2aa5576203018f5d8eb44dccceff.

Przeanalizowano cały rozdział, w szczególności:
1. Lokalna skończoność i skończoność na zbiorach zwartych na lokalnie zwartych przestrzeniach Hausdorffa.
2. Rozdzielenie regularności zewnętrznej, regularności wewnętrznej względem zbiorów zwartych i domkniętych, ciasności oraz przyjętą definicję miary Radona.
3. Dowód aproksymacji zbiorów borelowskich przez domknięte i otwarte dla skończonej miary w dowolnej przestrzeni metrycznej (klasa zbiorów aproksymowalnych jest sigma-algebrą).
4. Ciasność miar skończonych na przestrzeniach polskich, przez skończone pokrycia na kolejnych skalach i kompletny, całkowicie ograniczony zbiór przekrojowy.
5. Przejście od lokalnej skończoności i ośrodkowości do sigma-skończoności i regularności na lokalnie zwartych przestrzeniach metrycznych.
6. Kontrprzykład na nieprzeliczalnej przestrzeni dyskretnej oraz rozróżnienie miary i jej topologicznego nośnika.
7. Funkcje odcinające w C_c, jednoznaczność miary Radona poprzez całki i gęstość C_c(X) w Lp dla p<∞.

## Zmiany zapisane w źródle

Commit 10963b5bb46bbce6392dd31824f1c0682e893f84: skorygowano nazwę własności na „spełnia drugi aksjomat przeliczalności” w tytule i tezie twierdzenia o nośniku, a „skończoność na kompaktach” zastąpiono „skończonością na zbiorach zwartych”.
Commit bb82144c91f2a8fd596e2f13fce2123e5ae30fae: ten sam standard zastosowano w dowodzie o ośrodkowej przestrzeni metrycznej.
Commit 63afe4f0b9c663adc10ec48fff8019ec9c2973fb: usunięto niepoprawne utożsamienie topologicznego nośnika funkcji Lp ze zbiorem, na którym funkcja nie jest zerowa. Dla obcięcia f_n=f chi_{1/n<|f|≤n} wskazano A_n={|f|>1/n}, na którym f_n może nie znikać, i jawnie oszacowano μ(A_n)≤n^p∫|f|^p dμ<∞. Topologiczne domknięcie zbioru A_n nie musi mieć skończonej miary, toteż wcześniejsze uzasadnienie wymagało korekty.

Struktura źródła po poprawkach: 20/20 różnych etykiet, 18 bezpośrednich referencji (w tym dwa odsyłacze poza rozdział, do 17 i 23), 38 poprawnie zagnieżdżonych par środowisk.

## Testy i bramka CI

Dodano tools/tests/test_measure_theory_ch20.py, 8 modeli i testów: przestrzenie dyskretne, ciasność geometrycznego rozkładu atomowego, sigma-skończoność na modelach licznikowych, atomowy nośnik gęsty, konstrukcja funkcji odcinającej, rozróżnianie miar przez C_c, skończony model gęstości C_c w Lp oraz kontrola struktury, zależności i terminologii. Test dodano w commicie 48408191fd4ab13a426c1873afcc0998f30faa29. Nazwę kanonicznego pliku rozdziału 23 poprawiono w commicie 8066d1014d1e4a53a91526eb76f7721608e2ad39. W commicie ce4620dd75c97592eb90a24ff38e08d08f4d5981 poprawiono wybór ściśle dodatnich wag o zaniku kwadratowym, żeby uniknąć możliwego numerycznego underflow dla długiej listy punktów wymiernych.
Obecny blob testu: 1cd21fce6f81471c9b6075e14914833f7d05b146.

Utworzono .github/workflows/measure-theory-ch20.yml, commit 395f36135911ae30f2b13821582e43d8b88da1d8, blob 25a6bc60dd30954ab88b859f54b80fdb580cfecc. Workflow uruchamia 8 przypadków rozdziału oraz 4 globalne przypadki integralności książki, buduje pełny tom i izolowany rozdział 20 (numeracja 20), importuje wymagane etykiety z AUX całej książki i publikuje statusy measure-theory/ch20-regressions oraz measure-theory/ch20-pdf.

Pierwszy rzeczywisty przebieg workflow dla commitu jego utworzenia: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45275914785. Statusy tests i pdf = success, wszystkie trzy joby completed/success. Ten przebieg dotyczy wcześniejszych blobów źródła i testu i NIE poświadcza późniejszej poprawki dowodu, ani poprawki wag testu.

## Werdykt

Rozdział 20: PIERWSZY PRZEGLĄD WYKONANY, W STABILIZACJI. Poprawki źródła, regresje i workflow zapisane na istniejącej gałęzi. Pełne zaliczenie wymaga rzeczywistego wykonania CI na commicie 63afe4f0b9c663adc10ec48fff8019ec9c2973fb lub późniejszym, który obejmuje poprawki, odczytu logów 8+4 przypadków, pobrania i kontroli obu finalnych PDF-ów oraz drugiego niezależnego przeglądu matematycznego. Nie rozpoczynać rozdziału 21 przed zamknięciem rozdziału 20.
