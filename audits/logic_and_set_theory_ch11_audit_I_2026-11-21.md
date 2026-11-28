# Logika matematyczna i teoria mnogości — rozdział 11, audyt I

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** istniejący rozdział `11-formal-proofs-and-natural-deduction.tex` w Bibliotece matematycznej, 695 wierszy.  
**Cel:** audyt wszystkich istniejących wyników i integracja w książce modularnej, bez dodawania twierdzeń ani przykładów.

## Inwentarz

W źródle występuje **5 twierdzeń i 5 dowodów, 7 definicji, 16 przykładów oraz 8 uwag**. Zachowano **21 etykiet i 7 odsyłaczy**, nie dodano ani nie usunięto środowiska matematycznego. Schematy reguł i drzew znajdują się w środowiskach matematycznych, rozdział nie ma osobnego środowiska `figure`.

## Znalezione usterki i ich poprawa

1. **Warunek świeżości w `∃E` a nieskończony kontekst.** Stara definicja wymagała zmiennej `y` nieobecnej w całym zbiorze założeń `Γ`, który może być nieskończony i zawierać wszystkie nazwy zmiennych. Jest to zbyt mocne ograniczenie systemu. W poprawionym schemacie zmienna musi być świeża względem `φ` i `θ` oraz niewolna we wszystkich *rzeczywiście użytych otwartych założeniach* obu gałęzi, poza rozładowywanym założeniem `[φ[x:=y]]^i`. Dzięki skończoności drzewa zawsze można znaleźć świeżą nazwę. Zachowano dostateczny silniejszy warunek całkowitej nieobecności w `φ` i `θ`.
2. **Przykład `ex:nd-exists-major-premise-fresh-46` wcześniej nie dowodził tego, co zapowiadał tytuł.** Jego pierwsza część dotyczyła naruszenia świeżości w *innym otwartym założeniu*, a nie w przesłance głównej. Ten sam przykład, bez zmiany etykiety i liczby przykładów, zawiera obecnie dwa precyzyjne kontrmodele. W pierwszym `R` jest określonym zdaniem `∀z P(z)`: z `∃x P(x)` i `P(y)→R` nie wolno wnioskować `R` poprzez niedozwoloną regułę `∃E` z ustaloną `y`. W drugim przesłanka główna `∃x ¬(x=y)` jest prawdziwa w uniwersum dwuelementowym, podczas gdy użycie `y` jako świadka prowadziłoby z fałszywego założenia `¬(y=y)` przez `=I`, `¬E` i `⊥E` do fałszywego `∀z ¬(z=z)`. Ten kontrmodel bezpośrednio ilustruje warunek świeżości przesłanki głównej.
3. **Dowód twierdzenia `thm:nd-univ-chain` dopuszczał przechwycenie.** Zwrot „wybierzmy dowolną zmienną `z`” nie zapewniał dopuszczalności podstawienia `x:=z` pod wewnętrznymi kwantyfikatorami; przykładem jest `P(x)=∀z R(x,z)`. Dowód poprawiono przez podstawienie `x:=x`, które jest zawsze dopuszczalne; oba założenia są zewnętrznie skwantyfikowane, więc `∀I` daje bezpośrednio `∀x Q(x)`. Tezy nie zmieniono.
4. **Nieprecyzyjny opis parzystości.** Zdanie o liczbie 6 zastąpiono ogólnym stwierdzeniem, że sama parzystość nie implikuje dodatniości, z kontrprzykładem `−6`.

## Zakres matematycznego audytu

Sprawdzono formalny charakter schematów, odczytywanie kreski i wielokropków, reguły wprowadzenia i eliminacji `∧,∨,→,↔,¬,⊥`, klasyczną regułę `RAA`, prawidłowe rozładowanie oznaczonych wystąpień założeń, twierdzenie o dedukcji, prawo wyłączonego środka, wszystkie cztery reguły kwantyfikatorów wraz z warunkami ubocznymi, reguły równości oraz dowód skończonego użycia przesłanek. Nie stwierdzono dalszej konieczności zmiany ich tez.

## Testy niezależne

W dodatkowej enumeracji sprawdzono:

| Kontrola | Liczba przypadków | Wynik |
|---|---:|---|
| Wartościowania 3 atomów | 8 | PASS |
| Instancje reguł zdaniowych | 75 816 | PASS |
| Semantyczna równoważność twierdzenia o dedukcji | 5 184 | PASS |
| Poprawne użycia `∃E` przy świeżej zmiennej | 22 350 | PASS |
| Kontrmodele dla braku świeżości w przesłance głównej i w innych założeniach | 2 | Oba znaleziono |

Testy potwierdzają zachowanie prawdy dla badanych zastosowań reguł; **nie zastępują ogólnego dowodu poprawności rachunku**, przewidzianego w rozdziale 12. Trwałe kontrole zapisano w `tools/tests/test_logic_and_set_theory_ch11.py`.

## Odsyłacze i integracja

Po imporcie rozdziałów 01–11 oczekuje się **309 unikatowych etykiet**, **119 wystąpień odsyłaczy** oraz jednego udokumentowanego przyszłego celu `ch:zf-axioms`. Bilans rozdziału 11: 5 twierdzeń, 5 dowodów, 7 definicji, 16 przykładów, 8 uwag, 21 etykiet. Zaktualizowano katalog, plik główny książki i dedykowany workflow z kontrolą importów, środowisk TeX, wszystkich odsyłaczy, kompilacją PDF oraz testami regresyjnymi. Wynik CI należy potwierdzić na właściwym commicie.

## Status

**Audyt I zakończony z istotnymi poprawkami matematyczno-redakcyjnymi.** Rozdział 11 pozostaje otwarty do audytu II na poprawionej wersji. Nie rozszerzać zakresu i nie przechodzić do rozdziału 12 przed stabilną, niezależną kontrolą i zielonym CI.
