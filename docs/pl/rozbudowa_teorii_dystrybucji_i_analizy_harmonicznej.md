# Rozbudowa teorii dystrybucji i analizy harmonicznej — 2026-11-28

## Ustalenie zakresu po migracji

DT jest kanonicznym skryptem teorii dystrybucji, analizy Fouriera (także numerycznej), transformat całkowych i całek osobliwych. AM II zachowuje ogólne całkowanie, rachunek granic i wartość główną w elementarnym ujęciu; RRC zachowuje zastosowania do równań, ME konstrukcje miar, twierdzenia pokryciowe i różniczkowanie miar. Nie dublować pełnych dowodów; usuwać powtórzenia z innych skryptów dopiero po porównaniu wyników, dowodów i etykiet. Normalizacja Fourier w DT unitarna, w RRC nieunitarna; każdorazowo kontrolować stałe.

## Cross-check — pierwsza kontrola rzeczywistych źródeł

| Źródło | Zakres | DT / decyzja |
|---|---|---|
| RRC-06 | Ortogonalność, Bessel, Fejér, Parseval, zanikanie współczynników; ciepło, fala, Sturm–Liouville | DT-13 zawiera te same podstawy. Dodać zbieżność punktową i w Lp, uzupełnić szereg wielowymiarowy i zastosowania Fourier pozostawić w RRC. |
| RRC-07 | Testy, dystrybucje, lokalne oszacowanie, pochodne, nośniki, splot, skoki, słabe pochodne, rozwiązania fundamentalne, Weyl | DT-01–07 i 18 obejmują większość podstaw; do osobnej kontroli aproksymacja lokalna Lp, zerowa pochodna, ogólna teoria rozwiązań fundamentalnych. Zastosowania do PDE pozostają w RRC. |
| RRC-08 | Schwartz, Fourier, Riemann–Lebesgue, Gauss, odwrócenie, Parseval–Plancherel, S', mnożniki, Bessel, nieoznaczoność | DT-01,07,14–16; w DT-07 dodano brakujące pełne ujęcie L1. Sprawdzić wszystkie reguły i rozdzielenie wyników ogólnych od zastosowań ciepło/fala/Poisson/Helmholtz. |
| RRC-16 | Hessian Newtona, CZ, Marcinkiewicz, oszacowania lokalne i Schauder | DT-18–19 zawierają teorię ogólną w Lp; rozszerzyć o obcięcia maksymalne, główne wartości p.w., Hilbert/Riesz, oszacowania Höldera dla jąder. Regularność PDE i lokalizacja pozostają w RRC. |
| ME-23–25 | Haar, splot, pokrycia, operator maksymalny, różniczkowanie miar | DT-12,17; odsyłacze do konstrukcji ME, rozszerzenie analizy harmonicznej na grupach i zastosowań maksymalnych. |
| AMII-09,10,27,28,32,36 | Szeregi funkcyjne, przechodzenie pod całką, wartość główna, parametry, szeregi potęgowe | AMII-09 już zapowiada teorię szeregów Fouriera w osobnym skrypcie. Nie znaleziono aktywnych samodzielnych rozdziałów o Fouriera, Laplace'a ani FFT. Zachować ogólny rachunek AMII; rozwinąć szczególne zastosowania do transformat w DT. |

Kontrola dotyczy wymienionych jednostek i nagłówków twierdzeń, nie pełnej równoważności dowodów ani kompletnego repozytorium. Przed usunięciem powtórzeń sporządzić mapę etykiet RRC/ME i porównać hipotezy oraz szczególne przypadki.

## Kolejność rozbudowy

1. DT-01–11: pełny audyt teorii dystrybucji (lokalność, rząd, nośniki i nośniki osobliwe, partycje jedności, sklejanie, zbieżność i topologie, działania, splot i kryteria jego istnienia, transformata dystrybucji o zwartym nośniku i twierdzenie Paleya–Wienera–Schwartza; iloczyny/pullback tylko z odpowiednimi hipotezami, wprowadzenie do zbiorów falowych i rachunku mikrolokalnego). Rozwiązania fundamentalne operatorów o stałych współczynnikach: teoria ogólna, twierdzenie Malgrange'a–Ehrenpreisa z pełnym dowodem lub jasno oznaczonymi prerekwizytami. 
2. Fourier całkowy: L1, L2 i S' (rozpoczęte DT-07), transformata miar, jednoznaczność, Hausdorff–Young z twierdzeniem Riesza–Thorina, Young z ogólnymi wykładnikami, charakterystyka przestrzeni Sobolewa, transformaty radialne, przykłady rzeczywiste i zespolone, zależność między zanikiem i regularnością.
3. Fourier okresowy: postać rzeczywista i zespolona, Dirichlet–Jordan, Dini, Fejér w Lp, sumowanie Abela i jądro Poissona, Riemann–Lebesgue, zjawisko Gibbsa, normy jąder Dirichleta, granice zbieżności jednostajnej i punktowej (Carleson–Hunt wymaga osobnego zaawansowanego modułu), twierdzenie M. Riesz o sumach częściowych w Lp, szeregi wielowymiarowe i dystrybucje okresowe.
4. DFT i FFT: dyskretna ortogonalność, odwrotność i Parseval, splot cykliczny oraz liniowy przez dopełnienie zerami, algorytm Cooleya–Tukeya radix-2 z dowodem i złożonością, dowolne długości, normalizacje bibliotek NumPy/Julia, próbkowanie, twierdzenie Shannona przy jawnych hipotezach, aliasing i przeciek widma, okna, analiza błędów; przykłady obliczeniowe i rysunki Plotly.
5. Transformata Laplace'a: jednostronna i dwustronna, obszar zbieżności i holomorficzność, różniczkowanie względem czasu i parametru, przesunięcia, splot, jednoznaczność, wzór odwrócenia Bromwicha z warunkami, związek z Fouriera, dystrybucje o nośniku jednostronnym, zastosowania do ODE i równań całkowych. Dalsze transformaty: Mellina, Hankela i Radona (zakres według zależności); transformata Z jako dyskretny odpowiednik Laplace'a.
6. Analiza harmoniczna: operator maksymalny, interpolacja rzeczywista i zespolona, transformata Hilberta, transformaty Riesza, jądra jednorodne, ogólna teoria CZ, maksymalne obcięcia i zbieżność głównych wartości prawie wszędzie i w Lp, mnożniki Mihklina–Hörmandera, potencjały Riesza i Hardy–Littlewood–Sobolew, oszacowania Höldera; przestrzenie Hardy'ego i BMO, teoria wag A_p oraz Littlewooda–Paleya jako rozszerzenia po podstawach. Analiza na grupach abelowych i dualność Pontriagina po teorii Haara.
7. Porównanie całej zawartości z RRC/ME/AM II, migracja etykiet, odsyłacze w obie strony, testy, kompilacja i audyty rozdziałowe do stabilizacji. Bez nowych automatyzacji. Kolejność rozdziałów zmieniać dopiero ze spójną aktualizacją katalogu, testów i manifestu; nie usuwać historycznych etykiet.

## Wykonane w pierwszej iteracji
DT-07: transformacja L1 do C0, lemat Riemanna–Lebesgue'a, reguły translacji/modulacji/skalowania/splotu i różniczkowania, zgodność L1–L2–S', regularyzacja Gaussa, odwrócenie i jednoznaczność L1, pary prostokąt/sinc i wykładnicza/Lorentz oraz porównanie normalizacji RRC. Wszystkie nowe wyniki mają dowody; kompilacja i audyt kontrolny pozostają wymagane.

## Struktura docelowa — etap restrukturyzacji

Plan przyjęto po porównaniu zależności wszystkich 19 aktywnych jednostek. Docelowe identyfikatory pozostają robocze. Zmieniono kolejność: teoria zwartego nośnika poprzedza splot, transformacja dystrybucji temperowanych poprzedza istniejący dowód Plancherela, a M. Riesz i Carleson–Hunt stanowią rozdział 58 po teorii całek osobliwych. Podstawowe średnie Fouriera w Lp pozostają w części IV. To zapewnia porządek dowodów zamiast odsyłania do przyszłych twierdzeń.

### Część 1. Podstawy teorii dystrybucji

1. Przestrzenie funkcji gładkich i przestrzeń Schwartza
2. Funkcje testowe i ścisłe granice induktywne
3. Dystrybucje i topologie przestrzeni dystrybucji
4. Lokalność, nośniki, rząd i sklejanie dystrybucji
5. Pochodne dystrybucyjne i transpozycja operatorów
6. Dystrybucje o zwartym nośniku
7. Splot dystrybucji i regularyzacja
8. Skoki, iloczyny dystrybucji i ograniczenia rachunku

### Część 2. Transformacja Fouriera

9. Transformacja Fouriera w przestrzeniach Schwartza i L1
10. Dystrybucje temperowane i ich transformacja Fouriera
11. Transformacja Fouriera w L2 i twierdzenie Plancherela
12. Splot funkcji i nierówność Younga
13. Interpolacja zespolona i nierówność Hausdorffa–Younga
14. Transformacja Fouriera miar
15. Transformacja funkcji radialnych i funkcje Bessela
16. Transformata dystrybucji o zwartym nośniku i twierdzenie Paleya–Wienera–Schwartza

### Część 3. Struktura topologiczna i dalsza teoria dystrybucji

17. Przestrzenie Montela i nuklearne
18. Topologiczne iloczyny tensorowe
19. Twierdzenie o jądrze Schwartza
20. Induktywne iloczyny tensorowe przestrzeni testowych
21. Rozwiązania fundamentalne i twierdzenie Malgrange'a–Ehrenpreisa
22. Dystrybucje na rozmaitościach i operacje geometryczne
23. Zbiory falowe i podstawy analizy mikrolokalnej

### Część 4. Szeregi Fouriera

24. Układy ortogonalne i współczynniki Fouriera
25. Jądro Dirichleta i zbieżność punktowa
26. Jądra Fejéra i Poissona, metody sumowalności i Parseval
27. Zbieżność jednostajna, zjawisko Gibbsa i rozbieżność
28. Sumowalność i zbieżność średnich w Lp
29. Wielowymiarowe szeregi Fouriera i dystrybucje okresowe

### Część 5. Dyskretna i numeryczna analiza Fouriera

30. Dyskretna transformacja Fouriera
31. Algorytmy szybkiej transformacji Fouriera
32. Splot dyskretny i jego obliczanie
33. Próbkowanie i twierdzenie Shannona
34. Analiza widmowa, aliasing i funkcje okienkowe

### Część 6. Pozostałe transformacje

35. Transformacja Laplace'a jednostronna i dwustronna
36. Odwracanie transformacji Laplace'a i całka Bromwicha
37. Transformacja Laplace'a dystrybucji
38. Transformacje Mellina i Hankela
39. Transformacja Radona
40. Transformacja Z

### Część 7. Całki osobliwe i klasyczna analiza harmoniczna

41. Operator maksymalny Hardy'ego–Littlewooda
42. Interpolacja rzeczywista i twierdzenie Marcinkiewicza
43. Wartości główne, jądra całek osobliwych i mnożniki L2
44. Transformacja Hilberta
45. Transformaty Riesza
46. Rozkład i teoria Calderóna–Zygmunda
47. Maksymalne obcięcia i zbieżność wartości głównych
48. Mnożniki Fouriera i twierdzenie Michlina–Hörmandera
49. Potencjały Riesza i twierdzenie Hardy'ego–Littlewooda–Sobolewa
50. Potencjały Bessela, przestrzenie Sobolewa i zasada nieoznaczoności

### Część 8. Zaawansowana analiza harmoniczna

51. Przestrzenie Lorentza i przestrzenie interpolacyjne
52. Przestrzenie Hardy'ego
53. Przestrzeń BMO i dualność z H1
54. Wagi Muckenhoupta i ważone przestrzenie Lp
55. Teoria Littlewooda–Paleya
56. Przestrzenie Besowa i Triebel–Lizorkina
57. Analiza harmoniczna na grupach lokalnie zwartych i dualność Pontriagina
58. Zaawansowana zbieżność szeregów Fouriera: M. Riesz i Carleson–Hunt

Mapa: `catalog/distribution_theory_structure_plan.json`. Przypisano wszystkie 288 dotychczasowe etykiety do planowanych rozdziałów. Utworzono 13 rzeczywistych plików kandydackich obejmujących 117 zachowanych etykiet. Kandydaci są poza aktywnym katalogiem; bez pustych rozdziałów i bez zmiany kanonicznej numeracji. Sprawdzono bilans etykiet, środowiska LaTeX i jawne zwykłe odsyłacze kandydatów (zero odsyłaczy do późniejszego planowanego rozdziału). Nie jest to jeszcze audyt dowodów ani kompilacja. Rozdziały 7 i 16 wymagają w szczególności uzupełnienia. Następnie przygotować pozostałe kopie, sprawdzić odsyłacze po podziale i pełny master, przenieść testy i aliasy atomowo. CI poprzedniego aktywnego skryptu: 46139581019 PASS.

## Kompletna redystrybucja — kandydat do kompilacji

Wszystkie 288 etykiet istniejącego DT rozmieszczono w 30 rozdziałach kandydackich; 28 planowanych rozdziałów nie ma jeszcze źródeł. Master `shared/pl/distribution_theory/restructure/master.tex` zachowuje numery docelowe i nie tworzy pustych jednostek. Uruchomienie z `books/pl` po kompilacji AF:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=distribution_theory_restructured ../../shared/pl/distribution_theory/restructure/master.tex
```

Dodano test `python3 tools/tests/test_distribution_theory_restructure.py`, sprawdzający rzeczywiste pliki, zgodność etykiet i właścicieli, kolejność zwykłych odsyłaczy oraz master. Test i kompilacja wymagają uruchomienia. Następnie należy skorygować pozostałe opisowe odwołania do historycznej numeracji, sprawdzić zależności niewyrażone przez ref i przygotować atomowe przełączenie aliasów DT/FA. Nie zmieniano aktywnego katalogu ani istniejących workflow.
