# Topologia ogólna — rozdział 22, audyt 02 (pierwszy czysty)

**Data:** 2026-11-22.
**Badany blob:** 33765c2bb1b3065f4ad32596795c3d1981b48dda.
**Wynik matematyczny i statyczny:** CZYSTY, **1/2** kolejnych czystych audytów po ostatniej edycji rozdziału.
**Kontrola wydawnicza:** oczekuje na zakończenie CI dla nowego bloba oraz przegląd jego PDF. Nie przypisujemy im sukcesu przed zakończeniem.

## Niezależna rewizja dowodów

1. **Granice Kuratowskiego.** Wykazano równoważność warunków trafienia kul ze zbieżnością d(x,F_n)→0 oraz liminf d(x,F_n)=0. Dla domkniętości Li i Ls nie jest potrzebna domkniętość F_n: jeśli y jest blisko x i ma odpowiednią własność trafienia, trójkąt daje tę własność dla x. Rozróżnienie „ostatecznie” i „nieskończenie często” jest zachowane.
2. **Wijsman.** Dla niepustych domkniętych A,B funkcje d(.,A), d(.,B) są 1-lipschitzowskie, a ich zbiory zerowe identyfikują A i B. Na ośrodkowej X przeliczalny gęsty D wyznacza wszystkie ewaluacje, więc szereg 2^-j min(1,|d(q_j,A)-d(q_j,B)|) jest metryką zgodną z Wijsmanem. Argument działa dla otoczeń i sieci, nie tylko ciągów.
3. **Wijsman ⇒ Kuratowski.** Dla x∈F punktowa zbieżność do odległości zero daje x∈Li. Dla x∉F dodatniość d(x,F) daje x∉Ls. To zapewnia Li=Ls=F.
4. **Wijsman ⇒ Fell (nowy dowód).** Trafienie otwartego U jest stabilne dzięki małej wartości d(x,G) dla x∈F∩U. Ominięcie zwartego C disjoint F jest stabilne, ponieważ min_C d(.,F)>0 i dla finitely many centrów w C narzucono odchylenie ewaluacji < r/4. Oszacowanie d(y,G)>r/2 zachodzi na całym C. Wynika z tego otwartość podbazy Fella bez zakładania właściwości metryki.
5. **Attouch–Wets.** Na ograniczonych kulach funkcje odległości są ograniczone dla każdego niepustego F; definicja Δ_m jest skończona. Suma 2^-m min(1,Δ_m) jest metryką, a jej zbieżność jest równoważna zbieżności jednostajnej odległości na niepustych ograniczonych B⊆X. Wybór środka kul nie zmienia topologii.
6. **Attouch–Wets ⇒ Wijsman.** Każdy singleton jest ograniczony; ewaluacje są ciągłe względem topologii AW. Na nieskończonym ograniczonym dyskretnym X, F_n=X\{n} i F=X, Wijsman zachodzi, lecz dla AW supremum różnicy odległości po X jest zawsze 1.
7. **Właściwość przestrzeni.** Zwarta kula ma dla każdego ε skończoną sieć punktów. Funkcje d(.,F_λ) są 1-lipschitzowskie, toteż zbieżność punktowa jest na każdej zwartej kuli jednostajna; dotyczy to też sieci. Stąd równość topologii Wijsman i AW przy zwartości domkniętych kul.
8. **Fell ⇔ Kuratowski dla ciągów, gdy X lokalnie zwarta metryczna.** Dodatniość zwarto-domkniętego otoczenia x poza F zapewnia implikację Fella ⇒ upper Ls⊆F. Odwrotnie, jeśli nieskończenie wiele F_n trafia zwarty C disjoint F, to sekwencyjna zwartość metryczna C daje punkt w Ls∩C, co jest niemożliwe. Dolny warunek F⊆Li jest dokładnie warunkiem trafienia.
9. **Kuratowski ⇒ Wijsman przy właściwości i niepustym limicie.** Dla każdego x z F⊆Li wynika limsup d(x,F_n)≤d(x,F). Jeżeli liminf byłaby mniejsza, punkty z F_{n_k} bliskie x leżałyby w jednej zwartej kuli i miały podciąg do punktu Ls=F bliższego x niż d(x,F), sprzeczność.
10. **Kontrprzykłady.** W przestrzeni X={p,q}∪{y_n} z d(p,q)=2 i pozostałymi różnymi odległościami równymi 1, X jest lokalnie zwarta, lecz nie właściwa; Fell/Kuratowski do {p} nie implikuje Wijsmana dla F_n={p,y_n}. W R, {0,n}→{0} dla AW i Wijsmana, ale d_H({0,n},{0})=n, co rozróżnia topologię Vietorisa.

## Kontrola źródła LaTeX i zależności

- 716 wierszy, 28 unikatowych etykiet, 20 odsyłaczy.
- Wszystkie cele odsyłaczy są obecne w rozdziałach 14, 21 lub 22.
- Brak niezrównoważonych środowisk twierdzeń, definicji, dowodów i rysunku.
- Brak zakazanych terminów „unia” i „zwartościowanie” oraz angielskiego rzeczownika „dual”.
- Odsyłacze z rozdziału 22 nie wykorzystują rozdziału późniejszego w książce.
- Katalog zawiera 22 rozdziały, a osobny punkt wejścia rozdziału 22 importuje istniejące pliki aux rozdziałów 14 i 21.

## Status

**CZYSTY matematycznie (1/2)** na konkretnym blobie.
Następny audyt 03 musi być samodzielną kontrolą tego samego źródła
z uwzględnieniem końcowego CI i rzeczywistego wyrenderowanego PDF.
Bez tego nie wolno oznaczyć rozdziału jako stabilnego.
