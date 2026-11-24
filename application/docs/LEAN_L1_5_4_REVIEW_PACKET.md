# L1.5.4 — pakiet niezależnego odbioru parsera

Kandydat: `7c719440a33d51216d2fafeb0c20fb9bba11fb47`. [Seria 2+1](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445). Stan przy sporządzeniu: 2/3 pełnych rund, workflow in_progress/pending. Dokument jest materiałem dla recenzenta, nie zatwierdzeniem.

## Zakres i pochodzenie

[Porównanie z rozszerzonym AST L1.5.3](https://github.com/dariusz-piekarz/mathematical_scipts/compare/47e1956d25124132a66efc53ae4a78fbb67bf1ff...7c719440a33d51216d2fafeb0c20fb9bba11fb47) wykazuje w application nowy lekser (150 linii), parser (313), testy leksera (107), testy parsera (292), kontrakt gramatyki (128), dziennik i konfigurację. Nie zmieniono kodu AST w tym porównaniu. Odbiór dotyczy kontrolowanego formatu pilota, nie pełnej transkrypcji twierdzenia, dowodu ani kodu Lean.

## Dowody techniczne

| Runda | Aplikacja | Windows | Linux | Lean/Mathlib |
|---|---|---|---|---|
| 1 | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138378246271) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138378246527) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138378246614) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138378246462) |
| 2 | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138382607751) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138382608286) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138382608463) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138382608233) |
| 3 | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138385464107) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138385464414) | [success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138385464320) | [in_progress](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138385464338) |

Trzy raporty aplikacji mają identyczne pełne mapy 796 testów: 786 passed, 10 sklasyfikowanych skipów, 14/14 metod parsera. Artefakty 14910608253, 14910239414, 14910564840, sumy w dzienniku. 18/18 [sceptycznych testów bramki](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45374833445/job/138385385177). Po zakończeniu sprawdzić artefakt atlas-validation-status i pełny SHA. Nie mylić technicznej kontroli bramki z niezależnym odbiorem.

## Lista kontrolna recenzenta

1. Porównać ślad Unicode i źródłowy SHA z dokładnym wejściem; segmenty rozłączne, uporządkowane i pokrywające wszystkie tokeny. Nierozpoznana proza, komentarz, makro albo luka musi blokować cały wynik. Sprawdzić dzielenie poleceń i granice segmentów.
2. Sprawdzić zakresy kwantyfikatorów, cieniowanie nazw, różne ID wiązań, brak wycieku z założeń, zachowanie powtórzonych założeń. Niezależnie wyprowadzić drzewa dla P→Q→R, (P→Q)→R, ∀x:Real,∃x:Real,x=x i (∀x:Real,x=x)∧x=x przy parametrze x:Real.
3. Sprawdzić, że Eq Prop nie jest Iff, > i ≥ odwracają argumenty z zachowaniem śladu, typy literałów są jawne, brak koercji i niejawnego odejmowania w Nat. Nie uznawać poprawnego AST za prawdziwość zdania.
4. Sprawdzić ograniczenia źródła 32 KiB, 8192 tokenów, 64 poziomy składni i AST, 2048 węzłów, 128 wiązań i 128 KiB JSON. Odrzucenie przy przekroczeniu musi nie zwracać częściowego AST jako kompletnego.
5. Porównać 210 wektorów oracle z kontraktem, w tym łączenie operatorów. Sprawdzić negatywne przykłady z LST: równoważność syntaktycznych formuł, jednoznaczne istnienie, wiele klauzul i predykaty w dowolnej dziedzinie. Nie przypisywać parserowi obsługi, której nie ma.
6. Zweryfikować, że brak sieci, subprocess, generacji kodu Lean i zapisów kanonicznych w tym module; wynik ma certificate=false, candidate_status=not_generated, proof_status=not_run, statement_status=unreviewed. Kontrola nie dotyczy przyszłego izolowanego runnera.
7. Rozliczyć wszystkie pominięcia: 5 natywnych Windows i 2 realne testy Mathlib potwierdzone osobno; test Lean core, delegowany cgroup i pełny test lokalnej deklaracji TeX nadal bez potwierdzenia na tym SHA. Część kompilacyjna TeX wykonana lokalnie. Uzasadnić, dlaczego pozostałe testy nie są wymagane dla samej gramatyki, albo zażądać wykonania. Nie zmieniać ich statusu na passed.

## Decyzja i identyfikacja

PR #7 jest zbiorczym PR całej iteracji VI, z ruchomym HEAD. Nie wystarcza aprobata dowolnej wersji tego PR. Niezależny uprawniony recenzent, odrębny od autora, powinien jawnie wskazać pełny SHA kandydata, zakres L1.5.4, wyniki kontroli, ryzyka i decyzję. Przed zatwierdzeniem zweryfikować ukończoną agregację i tożsamość recenzenta w GitHub; nie generować deklaracji independent=true w imieniu recenzenta. Do tego czasu status stabilizing, certificate=false. Nie rozpoczynać L1.5.5 automatycznie.
