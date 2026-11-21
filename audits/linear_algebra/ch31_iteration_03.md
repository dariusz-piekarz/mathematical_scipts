# Algebra liniowa — rozdział 31, audyt III (drugi czysty; stabilizacyjny)

**Data:** 21 listopada 2026  
**Plik:** `chapters/pl/linear_algebra/31-grupy-pin-spin-i-spinory.tex`  
**Źródłowy blob:** `6c1d09b9eaf4083c9ebaa361dbf46fc350eae147`, identyczny jak podczas audytu II.

## Niezależna kontrola argumentów topologicznych i wiązek
1. **Związki grup:** dla każdego jednostkowego \(u\) wyprowadzono odbicie \(r_u(v)=v-2\langle u,v\rangle u\); obliczono dokładnie jądro Spin i Pin, surjektywność przez odbicia i lokalne płaty dwukrotnego nakrycia. Jawny dowód gładkości \(O(n)\) eliminuje zewnętrzny odsyłacz do DG.
2. **Wiązki główne:** lokalna trywialność, prawostronne działanie grupy i dwukrotne odwzorowanie \(\lambda\) są wyjaśnione. Definicja wiązki stowarzyszonej używa konsekwentnie równoważności \((pg,\psi)\sim(p,\varrho(g)\psi)\), a lokalne pola transformują się przez \(\varrho(h)^{-1}\).
3. **Mnożenie Clifforda na wiązce spinorowej:** poprawnie udowodniono niezależność od reprezentanta \([p,\psi]\), używając \(c(g)c(v)c(g)^{-1}=c(\rho(g)v)\). Daje to \(c_x(v)^2=-g_x(v,v)I\) i prawidłowy rozkład chiralny.
4. **Spinor na sferze i torusie:** dla \(S^2\) skonstruowano strukturę przez \(\operatorname{Spin}(3)\to SO(3)\) z włóknem \(\operatorname{Spin}(2)\); dla \(T^2\) otrzymano cztery nieizomorficzne podniesienia indeksowane \(\varepsilon_1,\varepsilon_2\) oraz dokładnie uzasadnione warunki (anty)periodyczne.
5. **Przeszkoda do podniesienia:** w przykładzie tautologicznej zespolonej wiązki prostej nad \(CP^1\) normalizowane przejście na równiku ma liczbę obrotów \(-1\); nie dopuszcza więc zamkniętego podniesienia do \(\operatorname{Spin}(2)\), zgodnie z dwukrotnym nakryciem.
6. **Dobry układ trywializacji i \(w_2\):** potrójne iloczyny podniesień \(h_{ij}h_{jk}h_{ki}\) są centralnymi znakami. Porównanie dwóch nawiasowań na czterokrotnych przecięciach daje warunek dwukocyklu. Zmiana \(h_{ij}\) o znaki powoduje dodanie kobrzegu, a warunek \(w_2=0\) jest równoważny istnieniu koherentnych przejść.
7. **Pola spinorowe:** przekształcenia lokalnych ramek i ekwiwariantne odwzorowania \(F:P_{\operatorname{Spin}}\to\Delta_n\) opisują ten sam gładki przekrój wiązki. Brak odsyłacza do nienależącego do LA tomu II o koneksjach jest zamierzony.

## Niezależne obliczenia i CI
- Dodatkowy wykonany test \(\delta^2=0\) dla symplicjalnego operatora Čech w charakterystyce 2, na losowych kołańcuchach stopni 0,1,2 i zbiorach 4–8 indeksów: **600 PASS**.
- Test na brzegu czworościanu wykazał, że macierz \(C^1\to C^2\) ma rząd 3, podczas gdy \(\dim C^2=4\), co daje \(H^2(S^2;\mathbb Z/2)\cong\mathbb Z/2\) w tym modelu: **PASS**.
- Niezależne testy dokładnych reprezentacji \(\operatorname{Cl}_4^{\mathbb C}\), chiralności oraz porównanie dwóch modułów \(\operatorname{Cl}_3^{\mathbb C}\) były dodatnie w audycie II.
- [Workflow 44956522593](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44956522593) — **SUCCESS**: testy symboliczne, poprawność odsyłaczy, katalogu, języka, kompilacja książki i eksport rozdziału.
- Z artefaktu `14727736243` pobrano i rozpakowano plik PDF. **14 stron**, brak pustych, **0 bloków poza formatem strony**, obejrzano wizualnie cały montaż i powiększone rysunki ze stron 4,9,11,14. Brak nakładających się opisów i obcięć.

## Wynik
**Audyt III czysty**, drugi bezpośrednio po czystym audycie II. Obie iteracje badały identyczne źródło, nie było konieczności wprowadzania poprawek.
**Rozdział 31: STABILNY po trzech iteracjach**. Status LA-01–31: stabilne.
Plik główny książki otrzymał tylko komentarz o statusie; po commicie należy jeszcze sprawdzić uruchomione przez niego końcowe CI.
Następny etap: LA-32 — twistory; materiał przygotować od podstaw, ponieważ nie występuje w DG-04.
