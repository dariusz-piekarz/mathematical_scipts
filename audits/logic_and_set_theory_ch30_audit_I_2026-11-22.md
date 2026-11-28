# Logika matematyczna i teoria mnogości — rozdział 30, audyt I

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Integracja

Odczytano cały plik biblioteczny `30-infinite-games-and-determinacy.tex` (1423 linie) i porównano z pełniejszą wersją `logika_teoria_mnogosci_iteracja_79.pdf` (fizyczne strony 240–257). Zachowano cały dotychczasowy materiał, obejmujący AD, PD, własność Baire'a, zbiór doskonały, mierzalność, duże liczby kardynalne, model L(R) i hierarchię Wadge'a.

Pełniejszy PDF zawierał **dwa elementy nieobecne w krótszym TeX**:
- przykład gry dwuruchowej z analizą kolejności kwantyfikatorów oraz rysunek drzewa gry;
- lemat o przeliczalnej sumie zbiorów pierwszej kategorii w ZF+AD.

Oba elementy przywrócono. Lemat koduje domknięte zbiory nigdziegęste drzewami skończonych ciągów, zbiera świadectwa małości w zbiory kodów reals i stosuje wcześniej dowiedzioną konsekwencję AD — przeliczalny wybór dla zbiorów liczb rzeczywistych. Nie stosuje niejawnie AC.

## Błędy i luki

1. **Siła założeń.** Pierwotny TeX przypisywał determinację gier otwartych i zamkniętych ZFC. Prawidłowe twierdzenie Gale'a–Stewarta dla ruchów w ω jest dowodliwe już w **ZF**. Poprawiono sformułowania.
2. **Brak twierdzenia o zbiorach doskonałych.** Starszy tekst wielokrotnie odwoływał się do `thm:ad-perfect-set`, ale nie zawierał takiej etykiety ani dowodu. Wprowadzono brakujący dowód tego już przywoływanego wyniku: gra o zbiór doskonały, przeliczalność przy wygrywającej strategii II, ciągła iniekcja przestrzeni Cantora w A przy wygrywającej strategii I, zwartość i brak punktów izolowanych, przeniesienie do przestrzeni Baire'a i na prostą rzeczywistą. Wykorzystano klasyczny schemat z T. Jech, *Set Theory*, rozdział 33, Twierdzenie 33.3(iii), z samodzielnym rozpisaniem kroków i zależności od ZF.
3. **Nieaktualne odsyłacze.** Zastąpiono odesłanie do przyszłego `ch:ad-incomparable-cardinals` poprawnym odesłaniem do twierdzenia już umieszczonego w bieżącym rozdziale. Odesłanie do przyszłego `ch:quotient-choice-paradox` zastąpiono informacją o zakresie przyszłej części skryptu bez udawania obecnego dowodu.

## Ponowny audyt Gale'a–Stewarta

Rozpisano operator etapowy na zbiorze T=ω^{<ω}, jego monotoniczność, pozyskanie ordynału Hartogsa bez AC, rekurencję pozaskończoną i stabilizację. Wykazano istnienie rang w stabilnym zbiorze i kanoniczne wybory najmniejszych ruchów. Dla II przed stabilnym zbiorem użyto supremum rang wszystkich następców. Zmodyfikowano także dowód determinacji gier zamkniętych, bez domniemanego przesuwania kolejności graczy w sposób nieuzasadniony.

**Werdykt:** integracja wykonana, wykryto i naprawiono istotną lukę merytoryczną; wymagane dalsze audyty i kompilacja rozdziału.
