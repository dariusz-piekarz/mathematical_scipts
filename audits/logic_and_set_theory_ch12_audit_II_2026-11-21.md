# Logika matematyczna i teoria mnogości — rozdział 12, audyt II

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/12-poprawnosc-logiki-pierwszego-rzedu.tex`.  
**Stan wyjściowy:** Git blob `cb77a711b3dc9afe64d888879aa589f664ae9e49` po audycie I.  
**Zakres:** powtórna, niezależna kontrola istniejącego materiału; bez nowych twierdzeń, lematów, definicji, wniosków ani przykładów.

## Wynik

**Nie znaleziono błędnego twierdzenia ani nowej luki w dowodach.** Audyt II wykrył natomiast nieprecyzyjny tytuł wniosku oraz trzy miejsca, w których warto jawnie wskazać język formuły. Wprowadzono minimalne poprawki redakcyjno-formalne. Ze względu na zmianę źródła rozdział pozostaje otwarty do **audytu III**.

Pełny inwentarz pozostał bez zmian: **3 twierdzenia, 3 lematy, 2 wnioski, 1 definicja, 4 przykłady, 3 uwagi i 8 dowodów**. Zachowano 10 etykiet i 24 wystąpienia odsyłaczy.

## Poprawki

1. **Tytuł `cor:soundness-countermodel`.** Poprzedni tytuł mówił o „braku formalnego dowodu zdania fałszywego w pewnym modelu”, chociaż teza obejmuje również formuły ze zmiennymi wolnymi i wymaga wartościowania. Zmieniono tytuł na **„Kontrmodel wyklucza formalny dowód formuły”**. Treść wniosku i dowód pozostawiono bez zmian.
2. **`lem:soundness-fresh`.** Sprecyzowano, że `φ` jest formułą wskazanego języka pierwszego rzędu.
3. **`lem:soundness-subst`.** Jawnie przyporządkowano zarówno formułę `φ`, jak i term `t` temu samemu językowi `L`.
4. **`thm:soundness`.** W założeniach zapisano explicite, że formuła `φ` należy do wskazanego języka `L`.

Żadna poprawka nie zmieniła znaczenia wcześniejszego twierdzenia, struktury dowodów ani notacji odsyłaczy. Dodano regresję sprawdzającą poprawny tytuł wniosku.

## Przegląd wszystkich dowodów

- **Zgodność wartościowań** (`lem:soundness-fresh`): hipoteza braku wolnej zmiennej daje identyczną interpretację formuły pod wartościowaniami różniącymi się tylko na tej zmiennej. Poprawna.
- **Podstawienie** (`lem:soundness-subst`): dokładne zastosowanie wcześniej udowodnionego twierdzenia semantycznego; wymagana dopuszczalność podstawienia jest jawna. Poprawna.
- **Równość** (`lem:soundness-equality`): równość wartości dwóch termów oraz dwa użycia lematu o podstawieniu uzasadniają `=E` dla dowolnej formuły przy obu dopuszczalnych podstawieniach. Poprawna.
- **Główne twierdzenie `thm:soundness`**: ponownie skontrolowano indukcję po skończonym drzewie, począwszy od każdego liścia otwartego założenia, również tymczasowego, którego wystąpienia będą rozładowane dopiero wyżej w drzewie. Przejście do korzenia opiera się na zawieraniu się pozostałych otwartych założeń w `Γ`. Reguły zdaniowe, sprzeczności i klasyczne `RAA` są objęte hipotezą indukcyjną względem poprawnych kontekstów.
- **`∀E` i `∃I`**: wartościowanie po podstawieniu termu jest połączone z interpretacją za pomocą lematu o podstawieniu; nie ma przechwycenia zmiennych.
- **`∀I`**: zmienna uogólniana nie występuje wolno w żadnym rzeczywiście otwartym założeniu poddedukcji; zatem wszystkie takie założenia są zachowane po dowolnej zmianie jej wartości.
- **`∃E`**: zmienna lokalnego świadka nie występuje w formule kwantyfikowanej ani w końcowym wniosku oraz nie występuje wolno w pozostałych rzeczywiście użytych otwartych założeniach obu gałęzi. Ze świadka `a` powstaje wartościowanie `r=s[y↦a]`; lemat o podstawieniu umożliwia użycie poddedukcji, po czym świeżość `y` pozwala wrócić do wartościowania `s`. Nie zakłada się, że nieskończony zbiór `Γ` omija pewną zmienną.
- **Dwa wnioski**: kontrmodel wyklucza dowodliwość, a spełnialność `Γ` wyklucza wyprowadzenie `⊥`. Poprawne.
- **Semantyczne twierdzenie o dedukcji**: oba kierunki dowodu działają dla dowolnych formuł, także otwartych, ponieważ odnoszą się do tej samej struktury i tego samego wartościowania.
- **Syntaktyczna skończoność wyprowadzalności**: wynika ze skończonego drzewa bez niejawnego stosowania pełności lub semantycznej zwartości.
- **Przykłady**: sprawdzono kontrmodel dla niedozwolonego `∀I`, przypadek pojedynczego modelu, koniunkcję oraz schemat skróconego drzewa. Brak nowego błędu.

## Niezależna falsyfikacja

Ponowna kontrola oparta na niezależnej enumeracji skończonych interpretacji objęła:

| Kontrola | Liczba przypadków | Wynik |
|---|---:|---|
| Struktury z uniwersami 1-, 2- i 3-elementowymi | 489 | bez kontrprzykładu |
| Wartościowania | 3057 | bez kontrprzykładu |
| Reguła `∃E` przy właściwych warunkach świeżości | 91 710 | PASS |
| Reguła `∀I` przy braku zmiennej w otwartym kontekście | 15 285 | PASS |
| Zastępowanie równych wartości w formule z kwantyfikatorem | 76 425 | PASS |
| Dualności De Morgana dla kwantyfikatorów | 30 570 | PASS |

Niezależnie skonstruowano kontrmodele na zbiorach 2- i 3-elementowych dla nieprawidłowego `∀I`, dla `∃E` z użyciem zmiennej występującej w przesłance głównej oraz dla `∃E` ze zmienną występującą wolno w innym otwartym założeniu. Potwierdzają konieczność warunków ubocznych. Nie stwierdzono kontrprzykładów dla poprawnych reguł. Enumeracja skończona nie zastępuje dowodu twierdzenia o poprawności dla wszystkich struktur.

## Integralność i CI

- Zachowano dokładnie **10 etykiet i 24 odsyłacze** rozdziału 12, wszystkie 8 dowodów i cały inwentarz środowisk.
- Modułowa książka z rozdziałami 01–12 nadal oczekuje **319 unikatowych etykiet** i **143 wystąpień odsyłaczy**, z jedynym udokumentowanym przyszłym celem `ch:zf-axioms`.
- Dedykowany workflow [44931142895](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44931142895) po audycie I był zielony: 108 stron PDF, 24 testy regresyjne, poprawne importy, brak nieoczekiwanych brakujących odsyłaczy i przepełnień. Globalny workflow aplikacji [44931142910](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44931142910) również przeszedł.
- Nowy commit po audycie II uruchamia obie walidacje. Ich wynik trzeba osobno sprawdzić, zanim źródło zostanie uznane za gotowe do kolejnego audytu.

## Status

**Audyt II wykonany z minimalnymi poprawkami redakcyjno-formalnymi.** Rozdział 12 **pozostaje otwarty do niezależnego audytu III**. Nie dodawać nowych twierdzeń ani lematów. Po stabilnym, czystym audycie i zielonym CI przejść do rozdziału 13 — „Twierdzenie o pełności i konstrukcja Henkina”.
