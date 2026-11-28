# Logika matematyczna i teoria mnogości — rozdział 10, audyt I

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** istniejący plik Biblioteki matematycznej `10-structures-valuations-and-truth.tex`, 710 wierszy.  
**Tryb pracy:** pierwsza kontrola istniejącego materiału, bez dodawania nowych twierdzeń, lematów, definicji lub przykładów.

## Inwentarz i zakres

Zweryfikowano wszystkie **5 twierdzeń, 2 lematy, 1 stwierdzenie, 1 wniosek, 9 dowodów, 8 definicji, 16 przykładów, 3 uwagi** i odsyłacze rozdziału. Zbadano: struktury z niepustym uniwersum, wartościowania, interpretację termów, spełnianie, prawa kwantyfikatorów, lemat o zgodności wartościowań, lemat o podstawieniu, przemianowanie zmiennych związanych, konsekwencję semantyczną oraz semantykę pełną i semantykę Henkina drugiego rzędu.

## Usterka definicyjna i poprawka

W pierwotnej definicji semantyki Henkina wskazano zakres `S_n⊆P(A^n)` kwantyfikatorów relacyjnych, lecz nie narzucono, by **wartościowania wolnych zmiennych relacyjnych** również należały do wskazanych rodzin. To prowadziło do niedookreślenia pojęcia wartościowania w uogólnionym modelu Henkina. Definicję poprawiono: dla każdej zmiennej relacyjnej `X^(n)` wymagamy `s(X^(n))∈S_n`, także przy wystąpieniach wolnych. Kwantyfikatory nadal przebiegają po `S_n`.

Dodatkowo jawnie wskazano sygnaturę, strukturę i uniwersum w definicji spełniania, w twierdzeniu o zgodności wartościowań oraz w definicji konsekwencji semantycznej. Zachowano dotychczasowe tezy, wyniki i przykłady.

**Nie dodano nowej zawartości matematycznej.** Wprowadzono poprawki w **czterech istniejących sformułowaniach**, bez modyfikacji dowodów.

## Kontrola matematyczna

1. **Struktura i wartościowanie:** interpretacja wszystkich symboli o zadanej arności, logiczny charakter równości, istnienie stałego wartościowania przy niepustym uniwersum bez aksjomatu wyboru, rozróżnienie wartości termów od wartości logicznych formuł.
2. **Zgodność i spełnianie:** dowód indukcyjny korzysta z wartości termów zależnych tylko od ich zmiennych, w kwantyfikatorach zgodność po aktualizacji `s[x↦a]`; przypadek zdań o pustym zbiorze zmiennych wolnych.
3. **Prawa kwantyfikatorów:** obie dualności De Morgana oraz możliwość wymiany jednakowych kwantyfikatorów, włącznie z sytuacją identycznych zmiennych `x=y`; brak niepoprawnej wymiany `∀` i `∃`.
4. **Podstawienie:** prawidłowa indukcja dla termów; w formule z kwantyfikatorem rozróżnienie `x=y`, braku wolnego `x` oraz podstawienia bez przechwycenia; użycie zgodności wartościowań do pominięcia aktualizacji zmiennej niewystępującej w termie.
5. **Przemianowanie zmiennych:** warunek „`y` nie występuje w ogóle w `ψ`” jest wystarczający dla poprawności podstawienia i zachowania prawdy; przykład niepoprawnego przemianowania został zachowany.
6. **Konsekwencja semantyczna:** monotoniczność względem zwiększenia zbioru przesłanek i prawdziwość dowolnego następstwa przy braku modeli przesłanek.
7. **Logika drugiego rzędu:** zmienne relacyjne, pełne zakresy `P(A^n)`, ograniczone zakresy `S_n`, modele z i bez pełnej indukcji drugiego rzędu; w przykładzie `A=Z` oraz `S_1={Z}` poprawność rozróżnienia pełnej semantyki od ograniczonego modelu Henkina, bez przypisywania temu modelowi pełnej arytmetyki Peana.

## Niezależna kontrola modeli skończonych

Opracowano niezależne obliczenia semantyczne, odtwarzające wartości termów oraz spełnianie formuł w niepustych modelach z relacjami i funkcjami. W bieżącej iteracji sprawdzono:

| Test | Liczba przypadków |
|---|---:|
| Modele skończone | 78 |
| Wartościowania zmiennych | 1038 |
| Sprawdzenia spełniania formuł | 12 456 |
| Lemat o podstawieniu | 255 348 |
| Prawa kwantyfikatorów | 62 280 |
| Zgodność wartościowań | 37 368 |

Liczba wykrytych kontrprzykładów: **zero**. Dodatkowo zbadano model dwuelementowy o dwóch stałych punktach funkcji następstwa. Zdanie indukcji jest w nim fałszywe przy pełnym zakresie podzbiorów i prawdziwe przy ograniczonej rodzinie Henkina `S_1={A}`. Uzupełniono trwałe testy regresyjne w `tools/tests/test_logic_and_set_theory_ch10.py`, w tym zabezpieczenie poprawionej definicji.

Kontrole skończonych struktur nie stanowią dowodu twierdzeń dla wszystkich modeli.

## Integralność LaTeX i CI

Po imporcie rozdziałów 01–10 oczekuje się **288 unikatowych etykiet, 114 wystąpień odsyłaczy** oraz trzech odsyłaczy w przyszłość: `ch:zf-axioms`, `ch:soundness-fol`, `thm:ls-second-order-categorical`. Zachowano wszystkie **19 etykiet** rozdziału 10. Bilans środowisk i odsyłacze należy potwierdzić przez dedykowany workflow.

Zmieniono import książki, katalog rozdziałów i workflow `.github/workflows/logic-and-set-theory-chapter.yml`, rozszerzając jego zakres o rozdział 10 i testy niezależne. W tym rozdziale nie ma diagramów wymagających korekty.

## Status

**Audyt I: zakończony z poprawką definicyjną i redakcyjną.** Rozdział 10 **pozostaje otwarty** do audytu II, ponieważ modyfikowano jego źródło. Nie przechodzić do rozdziału 11 przed czystą kolejną iteracją i zielonym CI.
