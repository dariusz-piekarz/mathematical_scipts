# Analiza funkcjonalna — rozdział 04 — audyt 02 (niezależny po poprawkach)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/functional_analysis/04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex.  
**SHA obiektu Git kontrolowanego źródła:** 589a27c647ffbc9e3de07c482d9e63a73cb7c040.  
**Decyzja matematyczno-redakcyjna i techniczna:** **CZYSTY (1/2)**, potwierdzony przez końcowy CI PASS. Bez zmian w źródłowym LaTeX; rozdział 04 nie jest jeszcze stabilny.

## Procedura

Przeprowadzono niezależny, pełny przegląd dziewięciu dowodów i pięciu przykładów w wersji rozdziału po audycie 04/01. Osobno skontrolowano poprawność definicji, jawność założeń Hausdorffa, ograniczoność von Neumanna i rodzin operatorów, topologie zbieżności punktowej i jednostajnej na zbiorach ograniczonych oraz dowód metryzowalności przez metrykę łańcuchową. Skontrolowano w szczególności rodzinę pustą, przestrzeń zerowymiarową i nieskończone produkty, a także nazwy pojęć, funkcje charakterystyczne, etykiety, odsyłacze i skład PDF.

## Dowody — 9/9 sprawdzonych, wszystkie PASS

1. **Kryterium ograniczoności przez ciągi skalarne:** dla B ograniczonego i ciągów x_n∈B, λ_n→0 użyto wspólnej homotetii zrównoważonego V⊂U. Jeśli B jest nieograniczony, wybór x_n∉nU i λ_n=1/n daje przeciwprzykład. Warunek działa w ogólnych TVS (bez metryzowalności). PASS.
2. **Podstawowe operacje na zbiorach ograniczonych:** suma zbiorów, ich suma algebraiczna, skalowanie, podzbiory i domknięcie. Dla domknięcia użyto otwartego zrównoważonego V z V+V⊂U, co daje cl(V)⊂V+V; skalowanie dodatnim t przenosi domknięcia. PASS.
3. **Kryterium lokalnej ograniczoności:** lokalnie ograniczona TVS ma zrównoważone ograniczone otoczenie U, którego homotetie tworzą bazę otoczeń zera; odwrotna implikacja wynika z zawierania tU⊂V przy dowolnym otoczeniu V. PASS.
4. **Równociągłość i zbiory ograniczone:** wspólne otoczenie U z T(U)⊂V dla całej rodziny operatorów i B⊂tU zapewniają T(B)⊂tV dla wszystkich T. PASS.
5. **Rodziny operatorów między przestrzeniami unormowanymi:** równociągłość jest równoważna ograniczoności wspólnej normy operatorowej. Przy rodzinnie pustej zachodzi uzgodniona konwencja sup pustej rodziny nieujemnych norm =0, więc teza zachowuje sens. PASS.
6. **Topologie τ_s i τ_b:** τ_s jest topologią podprzestrzeni produktu Y^X. W τ_b baza otoczeń jest wyznaczona przez N(B,V); kontrolę dodawania zapewnia W+W⊂V, a ciągłość łączną mnożenia przez skalar — ograniczoność T_0(B). Singletony są ograniczone, więc τ_b zawiera τ_s. Hausdorff wynika z rozdzielania różnych operatorów przez ewaluacje. PASS.
7. **Ograniczoność rodzin operatorów w τ_s i τ_b:** kryterium w τ_s otrzymuje się z ograniczoności wszystkich obrazów T(x). W τ_b jest ono równoważne ograniczoności łącznego obrazu T(B) dla każdego ograniczonego B; dla skończonej liczby warunków wybiera się maksimum skalowań po symetryzacji/zrównoważeniu otoczeń. PASS.
8. **Topologia τ_b i norma operatorowa:** z B_X wynika, że τ_b kontroluje normę; każde ograniczone B jest zawarte w RB_X, co daje przeciwną inkluzję topologii. Dla X skończeniewymiarowej ciągłość odwzorowań współrzędnych w normie wynika z dodatniego minimum normy na zwartej powierzchni max|a_i|=1; uwzględniono dim X=0. PASS.
9. **Kryterium metryzowalności TVS:** rekurencyjny wybór otoczeń U_n z U_{n+1}+U_{n+1}+U_{n+1}⊂U_n i ∩U_n={0}, definicja przez infimum wag łańcuchów, symetria, translacyjna niezmienniczość, nierówność trójkąta i oszacowanie porównujące kulę metryczną z U_n. W indukcji po liczbie odcinków kontroluje się oba podłańcuchy po lewej i prawej stronie odcinka przecinającego połowę wagi; **pusty podłańcuch daje zero**. Otrzymana metryka wyznacza także tę samą strukturę jednostajną, więc jej zupełność jest równoznaczna z zupełnością TVS. PASS.

## Przykłady — 5/5 PASS

1. **Otoczka wypukła w L^p dla 0<p<1:** rozłączne impulsy o p-masie 1, a ich średnia ma p-masę n^(1-p)→∞. Wynika stąd brak lokalnej wypukłości mimo ograniczoności kuli.
2. **Lokalna ograniczoność a normowalność:** produkt K^N nie ma ograniczonego otoczenia; L^p, 0<p<1, jest lokalnie ograniczona, lecz nienormowalna.
3. **Punktowa ograniczoność bez równociągłości:** funkcjonały T_n(x)=n x_n na c_00 są punktowo ograniczone, lecz normy T_n rosną, a wspólne obrazy e_n pozostają nieograniczone.
4. **Dwie topologie zbieżności operatorów:** te same T_n dążą do zera w τ_s, ale nie w τ_b, gdyż zbiór {e_n} jest ograniczony.
5. **Metryzowalny zupełny produkt nienormowalny:** metryka sumy 2^(-n)min(1,|x_n-y_n|) na K^N odtwarza topologię produktu; zupełność współrzędna nie implikuje normowalności.

## Niezależne próby kontrprzykładów i modele regresyjne

- W skończonej grupie addytywnej Z/16Z z malejącymi podgrupami U_n=2^n(Z/16Z) numerycznie skonstruowano najkrótsze łańcuchy dla wag dyadycznych. Sprawdzono zgodność metryki łańcuchowej z wagami pojedynczych różnic, nierówność trójkąta, symetrię, niezmienniczość względem przesunięć i oszacowania kul przez U_n.
- Oddzielnie zbudowano, zamiast jedynie podstawiać do wzoru, skończone kombinacje wypukłe rozłącznych impulsów dla p=1/2 i n=4,9,16,25,36. Każdy impuls ma p-masę 1, natomiast średnie p-masę √n.
- Sprawdzono na skończenie wspartych wektorach wzór na metrykę produktu, symetrię, nierówność trójkąta i niezmienniczość względem przesunięć.
- W pierwszej wersji dodatkowego testu porównanie ostrej nierówności dla skończonego ogona szeregu dyadycznego zawiodło wskutek zaokrąglenia float (dla n=4 wynik został zaokrąglony do 1/16). Zmieniono implementację na dokładne ułamki Fraction; nie jest to błąd twierdzenia ani rozdziału.
- Z zachowaniem ścisłości dokumentacyjnej skorygowano drobną omyłkę w historycznym raporcie 04/01: w przykładzie L^p zmieniono dwa, a nie trzy wystąpienia \mathbf1 na \chi.

## Kontrola struktury i techniczna

- Źródło niezmienione, nadal **9 środowisk proof**, **5 środowisk przyklad**, **15 różnych etykiet**, **2 odsyłacze** do istniejących etykiet (rozdział 01 i lokalna etykieta przykładu).
- Zachowano reguły językowe: „ciągowe kryterium” zamiast „sekwencyjne”, „spełnia pierwszy aksjomat przeliczalności” oraz \chi_A jako notację funkcji charakterystycznej.
- Rozszerzono wyłącznie tools/tests/test_functional_analysis_ch04.py z 12 do **15 testów**. Kontrole numeryczne uzupełniają, ale nie zastępują powyższych dowodów.
- [Poprzedni pełny CI 45158087741](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45158087741) zakończony SUCCESS dla tego samego pliku LaTeX, 12/12 wcześniejszych testów i dokumentu kontekstowego 01–05.
- **Rozszerzone CI: [przebieg 45158968331](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45158968331) — pełny SUCCESS.** Zweryfikowano 15/15 testów (wynik `Ran 15 tests` / `OK`), dwa przebiegi kompilacji LaTeX, kontrolę PDF i odsyłaczy oraz poprawne zapisanie artefaktu. Pobrany z tego przebiegu **PDF ma 33 strony A4, 480542 bajty**. Obejrzano ponownie komplet stron 22–27, w tym wyprowadzenie metryki na stronach 25–26. Dla tych sześciu stron sprawdzono także pozycje wszystkich bloków tekstu — zero elementów poza granicami strony. Końcowy log nie zawiera `Undefined control sequence`, `There were undefined references`, `Overfull \hbox` ani `Missing character`.
- Obejrzano render poprzednio skompilowanego PDF obejmujący strony 22–27 rozdziału, w szczególności wzory dowodu metryzowalności na stronach 25–26; brak zauważalnych kolizji i ucięć. Ponieważ tekst źródłowy nie został zmieniony, przejrzany obraz jest reprezentatywny również dla tej iteracji.

## Decyzja

**Audyt 04/02 CZYSTY matematycznie, redakcyjnie i technicznie — 1/2 kolejnych czystych audytów, pełny CI PASS.** Rozdział 04 pozostaje w stabilizacji, a audyt 04/03 będzie kolejną niezależną kontrolą potwierdzającą przed rozdziałem 05.
