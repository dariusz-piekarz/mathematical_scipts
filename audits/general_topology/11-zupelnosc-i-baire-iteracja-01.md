# Topologia ogólna — rozdział 11: audyt iteracja 01

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Rozdział: `chapters/pl/general_topology/11-zupelnosc-i-twierdzenie-bairea.tex`.

## Status

| Warstwa | Wynik |
| --- | --- |
| Istnienie rozdziału i integracja z książką | PASS (rozdział, punkt wejścia, katalog) |
| Domknięcie środowisk LaTeX | PASS (10 dowodów; kontrola definicji i rysunku) |
| Unikatowość etykiet i lokalne `\\ref` | PASS w rozdziale (25 etykiet, 5 odsyłaczy) |
| Audyt merytoryczny sformułowań | Przegląd wykonany; nie znaleziono kontrprzykładu ani braku założeń |
| Niezależna kontrola skończonych modeli | PASS (390 topologii na zbiorach o 0–4 elementach) |
| Testy Pythona w CI | Dodane; wynik uruchomienia niepotwierdzony |
| PDF rozdziału i całej książki | Konfiguracja CI dodana; kompilacja i oględziny niepotwierdzone |
| Ostateczna stabilizacja | OTWARTA — wymaga wyniku kompilacji i wizualnego sprawdzenia rysunku |

## Zbadane kroki matematyczne

1. Zupełność domkniętych podprzestrzeni: obie implikacje używają poprawnie ciągów Cauchy'ego i jednoznaczności granicy. W odwrotnej implikacji użyto metryzowalności do konstrukcji ciągu w domknięciu.
2. Przykład $(0,1)$: wyraźnie odróżniono zupełność konkretnej metryki euklidesowej od istnienia zgodnej metryki zupełnej, zbudowanej przez homeomorfizm na $\mathbb R$.
3. Równoważność definicji przestrzeni Baire'a: użyto dokładnie relacji między nigdziegęstością i gęstością otwartych dopełnień domknięć, bez ukrytego założenia $T_1$.
4. Dowód metryczny: istnieją zamknięte kule $K_{n+1}$ zawarte w otwartych kulach z poprzedniego kroku; promienie maleją do zera, centra tworzą ciąg Cauchy'ego; granica należy do każdego $K_n$.
5. Dowód lokalnie zwarty: zastosowano zwartość i normalność zwartego podzbioru przestrzeni Hausdorffa do znalezienia otwartego otoczenia o zwartym domknięciu; potem wykorzystano własność skończonych przecięć w zwartym $K_1$.
6. $\mathbb Q$ nie jest $G_\delta$ w $\mathbb R$: przecięcie dwóch przeliczalnych rodzin zbiorów otwartych gęstych musiałoby być gęste, lecz jest puste.
7. Dziedziczenie własności Baire'a przez otwarte podprzestrzenie: gęstość $H_n$ w $U$ zapewnia, że $H_n\cup(X\setminus\overline U)$ jest otwarty i gęsty w $X$.
8. Wniosek o sumie przeliczalnej domkniętych: założenie niepustości $X$ jest jawne.

## Uwagi

- Test wszystkich skończonych topologii sprawdza skończone modele, nie zastępuje dowodu twierdzenia nieskończonego.
- Sformułowanie lematu o zwartym domknięciu wymaga założenia Hausdorffa i używa go jawnie.
- Nie nadawać jeszcze rozdziałowi statusu „stabilny” bez zielonego wyniku PDF i kontroli wizualnej.
- Reguła terminologiczna dla przyszłych rozdziałów: **uzwarcenie**, a nie **zwartościowanie**.
