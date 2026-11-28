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
