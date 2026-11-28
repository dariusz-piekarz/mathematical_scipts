# AA-53 — audyt III: eliminacja relacji i naprawa bramki regresji

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło rozdziału: blob 5675bf04c336a76e6424eeca337f24b5f211aeb5, bez zmian.

## Kontrola matematyczna
Ponownie sprawdzono dowód niezależności algebraicznej u,v dla grupy dwucyklicznej: w podstawieniu x=X, y=T/X współczynnik najwyższej potęgi X^(2nr) to p_r(T²), niezerowy dla niezerowego p_r; również r=0 jest objęte. Zmiana znaku x zachowuje u,v i zmienia znak w, więc rozdziela część parzystą i nieparzystą każdej relacji zredukowanej modulo moniczną relację kwadratową. Niezerowość w i brak dzielników zera kończą dowód. W przypadku cyklicznym normalne monomy mają różne wykładniki obrazu, także m=1. Nie znaleziono nowej luki.

## Niezależna weryfikacja obliczeniowa
Uruchomiono Python/SymPy w kontenerze. Obliczono bazy Gröbnera nad QQ w porządku leksykograficznym x>y>U>V>W dla ideału (U-u,V-v,W-w). Wyeliminowano x,y; porównano jedyny wielomian eliminacyjny po unormowaniu do współczynnika wiodącego 1 z relacją rozdziału. Dla C_m, m=1,...,8: 8/8. Dla Dic_n, n=2,...,7: 6/6. Niezależnie dla tych sześciu n sprawdzono wyznacznik Jacobiego (u,v) względem (x,y): -4n xy(x^(2n)-y^(2n)) = -4n w, niezerowy wielomian; 6/6. Końcowe wykonanie kod 0. Pierwsze wykonanie miało błędne założenie o normalizacji wielomianu eliminacyjnego nad ZZ; poprawiono porównanie na moniczne nad QQ. Nie jest to błąd rozdziału. Testy skończone nie zastępują dowodu ogólnego.

## CI i naprawa testów
Run 45347673519, job 138286081097, failure w kroku Run repository tool tests. Log: 4599 testów, 12 niepowodzeń; wszystkie dotyczą asercji liczby rozdziałów 53 != 52 w testach przekrojowych. Run 45347855273 dla źródła po II w toku podczas odczytu. Zmieniono dokładnie 12 asercji liczby plików na 53 w modułach cross: aa02_22_28, aa06_07_15_41, aa09_12_43, aa11_28, aa12_17_23, aa13_39, aa25_26, aa26_27_29, aa29_32_35, aa30_36, aa32_34_35, aa37_43. Nie zmieniono innych warunków, dowodów ani testów matematycznych. Nowy pełny CI i oględziny PDF wymagane; nie uznaje się starszych przebiegów za walidację poprawionej bramki.

## Werdykt
Pierwszy czysty przegląd matematyczny źródła po II (1/2); korekta infrastruktury testowej. AA-53 nadal W AUDYCIE. AA-54 nieotwarty.
