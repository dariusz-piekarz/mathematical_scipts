# Topologia algebraiczna — TOP-10, audyty I–II (drugi cykl)

**Data:** 2026-11-21  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmiany `main`)  
**Rozdział:** `chapters/pl/algebraic_topology/10-homologia-i-kohomologia-c-echa-od-pokryc-do-granic-przestrzeni.tex`.

## Audyt I: spójność dowodów i precyzja

Sprawdzono wszystkie istniejące rozdziały tematyczne TOP-10: nerw i rozdrobnienia, kierunki granic w teorii Čecha, porównanie dla wielościanów, ciągłość granic odwrotnych, kolczyk hawajski, krzywą sinusową topologa, solenoid, otoczenia i niedokładność granicy odwrotnej. Nie dodano twierdzeń ani lematów.

- W dowodzie ciągłości granic odwrotnych jawnie określono **odwzorowanie wsteczne** z poziomu $P_m$: $V'_x=f_{j_x,m}^{-1}(V_x)$ oraz tożsamość $\pi_m^{-1}(V'_x)=\pi_{j_x}^{-1}(V_x)$. Z surjektywności $\pi_m$ wynika, że $V'_x$ pokrywają całe $P_m$.
- W dowodzie spójności solenoidu rozwinięto argument o zwartości: z założonego rozkładu na dwa niepuste zbiory domknięto-otwarte wynika rozłączność rzutów na pewnym skończonym poziomie, sprzeczna ze spójnością $S^1$.
- Naprawiono literówkę „rozdrobnienień” na „rozdrobnień”.

**Commity merytoryczne:** `00830820a8ead27451757c754c3b59cc12f39193` i `1233515b97160f0f8f0fec2a3530f6100366037d`.

## Korekta po CI i zabezpieczenie regresyjne

Pierwsze dwa uruchomienia audytu TOP-09–10 na commitach `00830820` i `1233515` zakończyły się błędem: w nowym dowodzie spójności solenoidu zabrakło poleceń LaTeX przy $\Sigma_p$, $\pi_j$ i \texttt{\textbackslash sqcup}. Błędy usunięto w commicie `1b1a9b46fa32d91a05b7eefbe8667335fad66a76`, odczytując ponownie plik na GitHubie i potwierdzając zachowanie dosłownych makr.

W commicie `5554d094c6ada968c3c8a705edda192db90be611` dodano test regresyjny do `application/tests/test_topology_chapters_09_10.py` kontrolujący konstrukcję przeciwobrazów i poprawne makra w dowodzie solenoidu. Po poprawce TeX workflowy dla commita `1b1a9b46` zakończyły się sukcesem:
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922368573 — TOP-09–10 TeX, `success`;
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922368569 — aplikacja i testy, `success`;
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922368643 — AT–DG–AG, `success`.
Po dodaniu testu regresyjnego uruchomienia na `5554d094` zakończyły się sukcesem dla TeX i aplikacji:
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922412651 — TOP-09–10 TeX, `success`;
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922412570 — aplikacja, `success`.

## Audyt II: dzikie zbiory zwarte a otoczenia regularne

W dowodzie opisu kohomologii Čecha przez otwarte otoczenia arbitralnego zwartego $A\subset S^n$ wykryto nadużycie pojęcia „regularne otoczenie $A$”: taki opis w sensie PL wymaga dodatkowych hipotez. W commicie `baef7bd2afaabad74914af847884a6396621e15b` zastąpiono je otwartym otoczeniem będącym **sumą otwartych gwiazd**. Oddzielono przy tym nerw pokrycia otoczenia od nerwu śladów pokrycia na $A$: te nerwy nie muszą być dosłownie identyczne. Wyjaśniono, że w granicy prostej trzeba porównywać odpowiednie rozdrobnienia.

**Wynik:** TOP-10 **nie jest jeszcze uznany za stabilny**. Potrzebny jest audyt III, zwłaszcza precyzyjnego porównania systemów nerwów przy przejściu do granicy prostej i ponownego sprawdzenia CI po najnowszej poprawce. Nie stwierdzono nowych braków w pozostałych obliczeniach grup kolczyka hawajskiego i solenoidu. Automatów nie włączano.
