# Audyt XLIX — rozdział 15: Dualność, wypukłość i słaba zbieżność w przestrzeniach Lp (I)

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Status: W STABILIZACJI.**

## Wznowienie i zakres

Przed rozpoczęciem pobrano bieżącą listę raportów audits/measure_theory i ostatnie commity gałęzi. Ostatni ukończony raport to **48-rozdzial-14-audyt-II-stabilizacja-2026-11-23.md**, commit **420f6ea813b19542a117b5d49787480e6c8226b1**: R14 jest formalnie stabilny. W katalogu raportów nie było audytu R15. Jedyny audytowany rozdział: **chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex**, blob **6cfb80433e293edfdbd713036493bdb78349c113**. Odczytano AGENTS.md i docs/pl/standardy_terminologiczne.md; books/pl/measure_theory.tex i books/pl/integration_theory.tex wyłącznie dla kontekstu struktury. Żadnego innego rozdziału nie audytowano ani nie zmieniano.

## Kontrola matematyczna — 12/12 dowodów

Źródło ma **506 wierszy, 7 sekcji, 8 twierdzeń, 3 lematy, 2 definicje, 1 wniosek, 2 przykłady, 3 uwagi i 12 środowisk proof**.

1. **Izometryczne zanurzenie Lq→(Lp)*:** dla 1<p<∞ funkcja normująca \overline g|g|^{q-2} daje równość Höldera bez sigma-skończoności; dla p=1 wykorzystano sigma-skończoność, by znaleźć zbiór dodatniej skończonej miary. Uwaga o nieskończonej masie punktu jest poprawnym kontrprzykładem.
2. **Nierówności punktu środkowego:** dla p≥2 sprawdzono punktową nierówność Clarksona; dla 1<p<2 kontrolowano najmniejszą wartość własną hesjanu, całkowalną osobliwość przy zerze oraz właściwe wykładniki Höldera 2/p i 2/(2-p). Przypadek S=0 jest osobno określony.
3. **Jednostajna wypukłość:** obie gałęzie p≥2 i 1<p<2 wynikają z poprzedniego lematu; epsilon>2 daje pusty warunek, a c_p=p(p-1)/32 jest bezpiecznym, choć nieoptymalnym oszacowaniem.
4. **Minimum energii:** koercywność J, ograniczenie ciągu minimalizującego, kontrola różnicy środkowej i zupełność Lp zapewniają istnienie minimizatora bez uprzedniego użycia refleksywności.
5. **Reprezentacja dualna Lp:** pochodna kierunkowa jest zmajoryzowana przez (|u|+|v|)^{p-1}|v|, całkowalną przez Höldera. Kierunek iv odzyskuje część urojoną; g=\overline u|u|^{p-2} należy do Lq. Jedyność wynika z izometrii.
6. **Dualność L1:** skonstruowana waga w>0 prawie wszędzie daje skończoną miarę P; T:L²(P)→C jest ciągły. Przypomniany dowód rzutu w Hilbercie jest niezależny; ograniczenie |g|≤||Λ|| wynika z testowania znakiem zespolonym na zbiorach mierzalnych. Obcięcia h_n=f/w na skończonej mierze P należą do L² i zbiegają w L¹(P). Uwaga o funkcjonale granicy na ℓ∞ jest poprawna.
7. **Ostrość Höldera:** normalizacja funkcji normującej i tożsamość (q-1)p=q są poprawne.
8. **Refleksywność:** podwójne zastosowanie reprezentacji Lp i Lq identyfikuje kanoniczne zanurzenie z surjekcją.
9. **Kryterium słabej zbieżności:** wynika z reprezentacji wszystkich funkcjonałów, nie tylko ich podrodziny.
10. **Dolna półciągłość normy:** przejście do liminf jest poprawne; Hahn–Banach daje funkcjonał normujący, a dla Lp dostępny jest niezależny dowód.
11. **Podciąg słabo zbieżny:** diagonalizacja na gęstym zbiorze Lq, jednoznaczne przedłużenie na jego powłokę i reprezentacja dualna dają słabą zbieżność. Separowalność jest jawnie założona; nie przypisano jej wszystkim przestrzeniom Lq.
12. **Minimum wypukłej energii:** ścisła wypukłość na klasach funkcji zapewnia jednoznaczność, pochodna kierunkowa prowadzi do jawnego minimizatora, a |f*|^p=α^{-q}|g|^q jest całkowalne.

**Wynik:** 12/12 dowodów bez wykrytej błędnej implikacji. Sprawdzono 2/2 przykłady: normę funkcjonału z wagą x^{-α} i funkcje Rademachera (zbieżność słaba bez normowej). Sprawdzono 3/3 uwagi, w tym kontrprzykłady dla p=1 i L∞.

## Niezależna regresja numeryczna

W lokalnym Pythonie/NumPy **uruchomiono 10500 prób** punktowych i ważonych nierówności środka na skończonych przestrzeniach atomowych z wartościami zespolonymi. Wykładniki p∈{1.2,1.5,1.9,2,2.5,4,8}, po 1500 niezależnych prób dla każdego p. **10500/10500 PASS**. Test nie stanowi dowodu dla dowolnych przestrzeni z miarą.

## LaTeX, odsyłacze i język

Zliczono **17 etykiet, 17 użyć \ref/\eqref**, w tym trzy cele w R14: ch:przestrzenie-lp, thm:holder-14, thm:riesz-fischer-14. Wszystkie pozostałe odsyłacze celują w etykiety wewnętrzne R15; wcześniejsze trzy wymagają sprawdzenia w pełnym składzie. Nie znaleziono w R15 alternatywnych symboli funkcji charakterystycznej, słów „indykator”, „unia zbiorów” ani nazwy „zbieżność zdominowana”; użyto \chi_A i „zbieżność zmajoryzowana”. Rozdział nie zawiera środowisk TikZ.

**Ograniczenia techniczne:** w tej iteracji **nie uruchomiono kompilacji pdflatex ani CI** i **nie oglądano wyrenderowanego PDF**. Nie należy na tej podstawie oznaczać technicznego PASS. Pozostaje także mechaniczna kontrola pełnych referencji i ostrzeżeń logu LaTeX. Nie dokonano zmian w tekście R15, ponieważ nie znaleziono udowodnionej usterki wymagającej poprawki.

## Decyzja i otwarte sprawy

**R15: W STABILIZACJI, nie STABILNY.** Wykonano pierwszy szczegółowy audyt matematyczny i niezależne testy, lecz wymagane są: pełna kompilacja izolowana i książkowa, sprawdzenie odsyłaczy i logów, oględziny PDF oraz dodatkowy czysty, niezależny audyt na niezmienionym źródle. R01–R14 zachowują wcześniejszy status; R16–R31 nietknięte. Nie scalano z integration_theory.tex.

**Następna iteracja: audyt L / R15 II**, wyłącznie rozdziału 15. Nie przechodzić do R16 przed formalną stabilizacją R15.

**Propozycja do zatwierdzenia (nie wprowadzona):** dodać osobny przykład różnicy między słabą a słabą-* zbieżnością w przestrzeni dualnej, aby zilustrować rozróżnienie z definicji.
