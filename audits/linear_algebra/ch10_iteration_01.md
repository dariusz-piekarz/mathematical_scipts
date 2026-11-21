# Algebra liniowa — rozdział 10, audyt I (utworzenie i kontrola konstrukcji)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/10-algebry-tensorowa-symetryczna-i-zewnetrzna.tex`  
**Zweryfikowany blob:** `4b8a17589043fed24455d1892df155827522eaed`  
**Materiał porównawczy:** `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` (stan bieżącej gałęzi).

## Zakres

Utworzono rozdział 10 „Algebry tensorowa, symetryczna i zewnętrzna” zgodnie z planem 36 rozdziałów: algebra stopniowana, algebra tensorowa i jej uniwersalność, algebra symetryczna i model wielomianowy, algebra zewnętrzna i własności uniwersalne, bazy, współrzędne z minorów, działanie odwzorowań liniowych, wyznacznik, wzór Cauchy'ego--Bineta, formy naprzemienne i iloczyn zewnętrzny form, operatory symetryzacji i alternowania. Nie powielano teorii tensorów prostych i potęg tensorowych z rozdziału 09 ani szczegółów rachunku wyznaczników z rozdziału 06; odwołano się do nich.

## Kontrola matematyczna pierwsza

- Iloczyny potęg tensorowych definiuje kanoniczna konkatenacja `V^{⊗p}⊗V^{⊗q}→V^{⊗(p+q)}`. Łączność wynika z kanonicznych izomorfizmów łączności i rozpiętości przez tensory proste. Własność swobodną `T(V)` udowodniono dla dowolnej łącznej algebry z jedynką.
- Ideały `J=(u⊗v-v⊗u)` i `I=(v⊗v)` są jednorodne. Ich ilorazy pozostają łącznymi algebrami z jedynką. W algebrze zewnętrznej warunek `v∧v=0` jest niezależnie narzucony, co jest konieczne w charakterystyce 2.
- Dowód bazy `S^k(V)` oparto na homomorfizmie do wielomianów; nie użyto średnich po permutacjach. Wzór `dim S^k(V)=binom(n+k-1,k)` obejmuje przypadek n≥1 i dowolną charakterystykę; przypadek n=0 podano osobno.
- Własność uniwersalna `Λ^k(V)` jest sformułowana dla naprzemiennych odwzorowań k-liniowych o wartościach w dowolnej przestrzeni. Faktoryzacja działa, ponieważ forma naprzemienna zeruje relacje `x⊗v⊗v⊗y`.
- Bazę `Λ^k(V)` udowodniono osobno przez rozpiętość i liniową niezależność, korzystając z wyznaczników współrzędnych. Dzięki temu wzory na `binom(n,k)` i minory nie wymagają podzielności przez `k!`.
- Potęgi zewnętrzne operatorów i minory podano w jawnie wybranych bazach. Wzór Cauchy'ego--Bineta wynika z `Λ^k(AB)=(Λ^k A)(Λ^k B)`, włączając k=0 i k>n.
- Identyfikacja `(Λ^k V)^*≅Alt^k(V^*)` pochodzi wprost z własności uniwersalnej; izomorfizm `Λ^k(V^*)≅Alt^k(V^*)` udowodniono w skończonym wymiarze. Iloczyn form wyrażono przez przetasowania, bez nieuprawnionych czynników normalizacyjnych.
- Znormalizowane operatory symetryzacji i alternowania wprowadzono wyłącznie pod założeniem `k!1_K≠0`. W innych charakterystykach ilorazowe definicje `S^k(V),Λ^k(V)` zachowują sens.
- Uwzględniono wymiary zerowe, puste wyznaczniki i przykłady geometryczne; jeden diagram własności uniwersalnej i rysunek zorientowanego równoległoboku wykonano w TikZ.

## Kontrola redakcyjna i techniczna

**`1625` wierszy**, **`42` unikalnych etykiet**, **`27` odsyłaczy** rozdziału 10. Sprawdzono bilans środowisk LaTeX i niepożądane wyrażenia terminologiczne. Rozdział zarejestrowano w pliku głównym, katalogu i dedykowanym workflow. Wynik kompilacji, kontrola wszystkich odsyłaczy i niezależny audyt II są wymagane przed zamknięciem.

**Status:** rozdział 10 otwarty po pierwszym audycie; nie zamykać bez czystej kolejnej iteracji oraz potwierdzenia CI.
