# Analiza funkcjonalna — rozdział 04 — audyt 03 (kontrola potwierdzająca)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex`.  
**SHA obiektu Git źródła:** `589a27c647ffbc9e3de07c482d9e63a73cb7c040` — niezmieniony od audytu 04/02.  
**Wynik:** **CZYSTY audyt 04/03, STABILIZACJA rozdziału 04 (2/2 kolejnych czystych audytów).**

## Metoda

Ponowne samodzielne sprawdzenie pełnego tekstu rozdziału, bez wprowadzania zmian w źródle. Kontrola sformułowań wszystkich twierdzeń, 9 dowodów, 5 przykładów, ograniczoności i równociągłości, topologii operatorów, metryki łańcuchowej, warunków Hausdorffa, pustych zbiorów/rodzin, wymiaru zero, terminologii, referencji oraz PDF.

## Kontrola dowodów — 9/9 PASS

1. **Ciągowe kryterium ograniczoności:** ograniczoność implikuje zbieżność `λ_n x_n→0` przez zrównoważone otoczenie; odwrotnie wybiera się `x_n∈B\nU` i `λ_n=1/n` przy nieograniczonym B. Wymagana tylko struktura TVS.
2. **Operacje na zbiorach ograniczonych:** suma zbiorów i ich suma algebraiczna, mnożenie przez skalar, podzbiory i domknięcie. W domknięciu oszacowanie `cl(V)⊆V+V⊆U` wymaga otwartości i symetrii V; oba warunki są jawnie zrealizowane.
3. **Lokalna ograniczoność:** z ograniczonego otoczenia zera otrzymuje się zrównoważone ograniczone U i bazę jego dodatnich homotetii; odwrotna implikacja wynika bez dodatkowych założeń.
4. **Równociągłość rodzin:** jedno U działa jednocześnie dla wszystkich operatorów T, a ograniczoność B daje wspólne skalowanie t. Wniosek o punktowej ograniczoności bez założenia zupełności jest poprawny.
5. **Rodziny operatorów między normowanymi przestrzeniami:** wspólne oszacowanie norm operatorowych uzyskuje się z jednolitej kontroli na kuli; odwrotnie normy ograniczone zapewniają wspólną kulę. Dla rodziny pustej jawnie przyjęto wartość supremum 0.
6. **Topologie `τ_s` i `τ_b`:** dla punktowej użyto zanurzenia w `Y^X`; dla jednostajnej na ograniczonych — bazy otoczeń `N(B,V)`, zrównoważenia, sumy W+W i ciągłości łącznej mnożenia skalarnego opartej na ograniczoności obrazu `T_0(B)`. Właściwość Hausdorffa i `τ_b⊇τ_s` są poprawne.
7. **Ograniczoność rodzin operatorów:** `τ_s` sprowadza się do ograniczoności współrzędnych/ewaluacji, `τ_b` do ograniczoności jednoczesnych obrazów wszystkich ograniczonych B; skończone przecięcia nie zmieniają kwantyfikatorów.
8. **Topologia normy operatorowej:** kula jednostkowa i oszacowanie `B⊆R B_X` dają równoważność `τ_b` z normową. W skończonym wymiarze stała C pochodzi z dodatniego minimum na zwartej powierzchni `max|a_i|=1`; przypadek `dim X=0` rozpatrzono osobno.
9. **Metryzowalność TVS:** przy rodzinie `U_n` spełniającej `U_{n+1}+U_{n+1}+U_{n+1}⊆U_n` konstrukcja infimum wag łańcuchów jest skończona, symetryczna, spełnia nierówność trójkąta i jest niezmiennicza względem przesunięć. W lemacie o łańcuchach wybór odcinka przecinającego połowę sumy wag daje lewy i prawy podłańcuch o wagach mniejszych od połowy progu; przypadki podłańcucha pustego i łańcucha jednoodcinkowego zostały jawnie uzasadnione. Z inkluzji `U_{n+1}⊆B_d(0,2^{-n})⊆U_{n-1}` wynika dodatnia określoność, zgodność topologii i kanonicznej struktury jednostajnej. **PASS**.

## Przykłady — 5/5 PASS

1. **`L^p`, `0<p<1`:** uśrednienie n rozłącznych funkcji o p-masie 1 prowadzi do p-masy `n^{1-p}→∞`, więc otoczka wypukła kuli ograniczonej nie jest ograniczona. Oznaczenia `χ_A` zgodne ze standardem.
2. **Produkt `K^N` i `L^p`:** pierwszy nie jest lokalnie ograniczony, drugi jest lokalnie ograniczony i nienormowalny.
3. **`T_nx=n x_n` na `c_{00}`:** punktowa ograniczoność nie zapewnia równociągłości bez dodatkowych warunków.
4. **`τ_s` kontra `τ_b`:** `T_n→0` punktowo, lecz nie jednostajnie na zbiorze `{e_n}`, ograniczonym w `c_{00}`.
5. **`K^N` z metryką `Σ2^{-n} min(1,|x_n-y_n|)`:** topologia produktowa, zupełność i brak normowalności.

## Próby obalenia i kontrola techniczna

- Niezależnie przetestowano niedomknięty/nienormowalny `L^p` dla `p<1`, rodzinę operatorów na niezupełnej `c_{00}`, puste rodziny i `dim X=0`.
- Test łańcuchowy na `Z/16Z` sprawdza niezmienniczość translacyjną, trójkąt, dodatniość i inkluzje kul; dokładna arytmetyka ułamków zapewnia ścisłe oszacowania ogona szeregu. Są to testy pomocnicze — nie zastępują argumentu ogólnego.
- Zachowano **15 unikatowych etykiet, 9 dowodów, 5 przykładów** oraz odsyłacze do rozdziału 01 i przykładu lokalnego. Brak powrotu do słów „sekwencyjne” i „pierwszoprzeliczalna”; użyto „ciągowe”, „spełnia pierwszy aksjomat przeliczalności” i `χ_A`.
- Dedykowany [przebieg GitHub Actions 45159541057](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159541057) zakończył się **pełnym SUCCESS**: 15/15 testów, kompilacja LaTeX z rozdziałami 01–05, kontrola PDF i odsyłaczy, artefakt PDF.
- Poprzedni [przebieg 45158968331](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45158968331) również przeszedł pełny CI na identycznym źródle. Wizualnie obejrzane strony 22–27 dokumentu kontrolnego, w tym wzory metryzowalności na stronach 25–26, nie wykazały kolizji tekstu ani ucięć. Źródło nie zostało od tego momentu zmienione.

## Decyzja

**Drugi kolejny czysty audyt po ostatnich zmianach w źródle. Rozdział 04: STABILNY (2/2).** Można rozpocząć audyt rozdziału 05 „Przestrzenie lokalnie wypukłe i seminormy” bez naruszania ustabilizowanego rozdziału 04.
