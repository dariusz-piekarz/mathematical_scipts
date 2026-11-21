# Logika matematyczna i teoria mnogości — rozdział 12, audyt I

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `12-soundness-of-first-order-logic.tex` w Bibliotece matematycznej (446 wierszy).  
**Zakres:** niezależny przegląd matematyczny, redakcyjny i techniczny istniejącego rozdziału „Poprawność rachunku dowodowego i konsekwencja logiczna”. **Nie dodawano twierdzeń, lematów, wniosków, definicji ani przykładów.**

## Inwentarz

W istniejącym rozdziale znajdują się **3 twierdzenia, 3 lematy, 2 wnioski, 1 definicja, 4 przykłady, 3 uwagi i 8 dowodów**. Zachowano wszystkie **10 etykiet** i **24 wystąpienia odsyłaczy**.

## Wykryta luka i poprawka dowodu

W dowodzie `thm:soundness`, w przypadku bazowym indukcji po drzewie dedukcji, oryginalny zapis analizował jedynie liść będący otwartym założeniem `γ∈Γ`. Hipoteza indukcyjna została jednak sformułowana dla **każdej poddedukcji**, której otwarte założenia obejmują również **założenia tymczasowe** rozładowywane dopiero w nadrzędnym węźle przez `→I`, `∨E`, `¬I`, `RAA` lub `∃E`. Zatem przypadek bazowy w poprzedniej wersji był niepełny.

Poprawiono istniejący dowód: dla liścia otwartego założenia `γ` dowolnej poddedukcji sprawdzamy wartościowanie spełniające **wszystkie jej aktualne otwarte założenia**, w tym ewentualne założenia tymczasowe; wtedy automatycznie spełnione jest `γ`. Dopiero przy przejściu do korzenia pełnego drzewa korzystamy z tego, że jego pozostałe otwarte założenia należą do `Γ`.

Nie zmieniono tezy twierdzenia ani systemu wnioskowania.

## Doprecyzowania założeń

Doprecyzowano, bez zmiany matematycznego sensu:

1. **Definicję konsekwencji semantycznej dla formuł:** jawnie wskazano język pierwszego rzędu, struktury tego języka, niepuste uniwersum i wartościowania zmiennych w tym uniwersum.
2. **Lemat `lem:soundness-equality`:** jawnie wprowadzono język z równością, strukturę, wartościowanie, zmienną podstawiania `x`, oba termy `t,u` i formułę `θ` przed warunkiem dopuszczalności podstawienia.
3. **Wniosek o kontrmodelu:** samodzielnie wymieniono `L, Γ, φ, A, s` zamiast opierać się na domyślnej notacji z poprzedniego twierdzenia.
4. **Wniosek o niesprzeczności:** określono język, zbiór formuł i pojęcie modelu/spełniania tych formuł przy wartościowaniu.
5. **Semantyczne twierdzenie o dedukcji:** określono wspólny język `L` dla `Γ, α, β`.
6. **Syntaktyczną skończoność wyprowadzalności:** określono język `L`, zbiór założeń i końcową formułę.

Wszystkie poprawki są formalno-redakcyjne lub wypełniają wskazaną lukę w istniejącym dowodzie. Nie usunięto innych elementów.

## Ponowna kontrola pozostałego materiału

- **Lemat o nieistotnej zmiennej:** jego treść jest dokładnym zastosowaniem twierdzenia o zależności spełniania od zmiennych wolnych.
- **Lemat o podstawieniu:** zakłada dopuszczalność podstawienia i korzysta ze sprawdzonego twierdzenia semantycznego rozdziału 10.
- **Lemat o zastępowaniu równych termów:** dwóch kolejnych użyć lematu o podstawieniu dokonuje się pod tym samym wartościowaniem `s[x↦a]`; wystarczają równe wartości `t,u`, nie identyczność ich napisów.
- **Twierdzenie o poprawności:** niezależnie sprawdzono indukcyjne przypadki wszystkich reguł rozdziału 11, także `∀I` i `∃E` z poprawionymi wcześniej warunkami świeżości opartymi na faktycznie użytych otwartych założeniach. W przypadku `∃E` zmienną `y` aktualizuje się po otrzymaniu świadka `a`, korzysta z dopuszczalności podstawienia i zgodności na zmiennych wolnych, a następnie usuwa zależność od `y` w konkluzji.
- **Dwa wnioski z poprawności:** kontrmodel wyklucza formalny dowód wniosku, a spełnialność `Γ` wyklucza formalny dowód `⊥`.
- **Semantyczne twierdzenie o dedukcji:** rozpatrzono obydwa przypadki wartościowania spełniającego `Γ`: `α` fałszywą i `α` prawdziwą. Rozumowanie działa również dla otwartych formuł i dowolnego (potencjalnie nieskończonego) `Γ`.
- **Syntaktyczna skończoność dowodu:** wynika ze skończoności drzewa, nie z semantycznej zwartości. Uwaga o niemożności wyprowadzenia semantycznej zwartości z samej poprawności pozostaje zasadna.
- **Przykłady i odsyłacze:** sprawdzono przykłady kontra modeli, odwołania do rozdziałów 10 i 11 i formalny zapis `Γ⊢φ` wobec `Γ⊨φ`. Rysunków `figure` nie ma.

## Regresja i techniczna integralność

Dodano `tools/tests/test_logic_and_set_theory_ch12.py` z niezależnymi testami na małych strukturach, obejmującymi semantyczne twierdzenie o dedukcji **także dla formuł wolnozmiennych**, podstawowe reguły kwantyfikatorów, zachowanie wartości logicznej przy zastępowaniu równych termów w formule zawierającej kwantyfikator, kontrmodel dla nieuprawnionego `∀I` oraz kontrolę opisu tymczasowych założeń w źródle. Są to testy falsyfikacyjne, nie dowody ogólnej poprawności.

Po imporcie rozdziałów 01–12 książka powinna zawierać dokładnie **319 unikatowych etykiet** i **143 wystąpienia odsyłaczy**, z jednym znanym odsyłaczem do przyszłego rozdziału `ch:zf-axioms`. Weryfikację tego inwentarza i kompilacji PDF przeprowadza dedykowany workflow skryptu. Wprowadzono import w pliku głównym, katalogu i aktualizację workflow z testami rozdziału 12.

## Status

**Audyt I rozdziału 12 zakończony z poprawką istniejącego dowodu i doprecyzowaniem sformułowań.** Rozdział **pozostaje otwarty do audytu II**. Nie rozszerzać materiału, dopóki niezależna kolejna kontrola i CI nie potwierdzą stabilności. Przejście do rozdziału 13 — „Twierdzenie o pełności i konstrukcja Henkina” — dopiero po domknięciu rozdziału 12.
