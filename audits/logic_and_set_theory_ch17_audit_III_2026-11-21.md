# Logika matematyczna i teoria mnogości — rozdział 17, audyt III

**Data:** 21 listopada 2026 r.  
**Rozdział:** 17 — *Arytmetyka formalna i kodowanie składni*  
**Podstawa:** `logika_rozdzial_17_audyt_II.tex`.  
**Wynik:** audyt III **z poprawkami**. Bez rozszerzania zakresu twierdzeń i lematów.

## 1. Niezależne sprawdzenie matematyczne

Przejrzano od początku aksjomaty arytmetyki Robinsona Q i Peana PA, oba kierunki opisu skończonych odcinków poniżej numerałów, dowód Σ₁-zupełności Q, kontrmodel przemienności dodawania, rekursję prostą i minimalizację, kodowanie Gödla, programy rejestrowe oraz pierwotnie rekurencyjny weryfikator gotowego dowodu z certyfikatami.

### A. Brakujący przypadek arności zero (usterka matematyczna)

Definicja funkcji pierwotnie rekurencyjnych dopuszczała wyłącznie dodatnie arności k, podczas gdy poniżej w dowodzie funkcji poprzednika korzystano z rekursji prostej **bez dodatkowych parametrów**, tzn. z przypadkiem k=0. Doprecyzowano `\N^0` jako zbiór jednoelementowy, dopuszczono funkcje zeroargumentowe, `Z^0=0` i k=0 w schemacie rekursji. Jawnie wyprowadzono `pd(0)=Z^0=0` oraz `pd(S(y))=P_1^2(y,pd(y))=y`; stała 1 ma postać `S∘Z^0`. Zmiana usuwa niespójność definicji z jej późniejszym zastosowaniem; nie dodaje nowego twierdzenia.

### B. Sprawdzenie kontrmodelu Q (uzupełnienie dowodu)

Przeprowadzono szczegółową kontrolę na `N ⊔ {a,b}` ze stałymi punktami następnika. Uzupełniono tekst o oba przypadki weryfikacji aksjomatów Q5 i Q7: argument standardowy (w tym 0) oraz argument ze zbioru `{a,b}`. Przy `y=n∈N` i `x=c∈{a,b}` otrzymujemy `c+S(n)=c=S(c+n)`, a w Q7 `c·S(0)=c=0+c` oraz dla n≥1 `c·S(n)=c=c+c`. Gdy `y∈{a,b}` jest punktem stałym następnika, Q5 i Q7 również zachodzą, ale `a+b=b≠a=b+a`. Nie ma potrzeby dodawania aksjomatów porządku: symbol `<` został zdefiniowany przez Q8.

### C. Pozostałe wyniki

Ponownie sprawdzono niekolistość uzasadnienia pierwotnej rekurencyjności kodowania w lemacie 6.3 względem lematu 6.5, rozkład na skończone alternatywy i koniunkcje w Σ₁-zupełności, konstrukcję kodów potęg pierwszych, ograniczoną minimalizację oraz certyfikaty pochodzenia aksjomatów teorii wyliczalnej. Nie znaleziono nowych luk w tych wynikach. Poprawiono wyłącznie redakcyjny nagłówek uwagi o intuicji aksjomatów i wygładzono wprowadzenie do definicji p.r.

## 2. Walidacja

- LaTeX: lokalny skrypt 01–17 skompilowany bez błędów i `Overfull \hbox`; 34 unikatowe etykiety w rozdziale 17 i 28 wystąpień odsyłaczy.
- Model Q: testy równań Q1–Q7 dla 32 standardowych argumentów i dwóch dodatkowych punktów; Q8 w modelu obowiązuje na mocy definicji `<`.
- Dodatkowo: testy rekursji bez parametrów, funkcji poprzednika, skończonych odcinków, kodów Gödla, ograniczonej minimalizacji, poprawności i kompletności etykiet.
- Testy stabilizacyjne: **10/10 PASS** (dodatkowo wcześniej 12/12 testów audytu II).
- Osobny PDF: **10 stron**, wszystkie strony wyrenderowane i zweryfikowane. Złożono PDF z uwzględnieniem przygotowanego rozdziału 18 wyłącznie w celu rozstrzygnięcia trzech odsyłaczy przyszłych. Nie dołączono treści rozdziału 18 do artefaktu rozdziału 17.

## 3. Decyzja

Audyt III wykrył potrzebę poprawy definicji, dlatego wymagana jest niezależna iteracja IV. Nie przesuwamy żadnych wyników ani nie tworzymy nowych twierdzeń. Wersja po audycie III nadaje się do audytu stabilizacyjnego.