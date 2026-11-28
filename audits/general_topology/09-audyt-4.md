# Topologia ogólna — rozdział 09: audyt 4

**Data:** 2026-11-21  
**Wersja:** 0.3 (źródło bez zmian)  
**Wynik:** pierwszy kolejny czysty audyt — **1/2**.  
**Zakres:** poprawność matematyczna, samodzielność twierdzeń, dowody i przypadki brzegowe, przykłady i kontrprzykłady, terminologia, diagram, skład i kompilacja LaTeX.

## Niezależna kontrola matematyczna

1. Drugi aksjomat przeliczalności => pierwszy: weryfikacja baz lokalnych (w tym niekoniecznie otwartych otoczeń), przypadku pustego.
2. Dziedziczenie obu aksjomatów przeliczalności przez wszystkie podprzestrzenie; przeliczalne iloczyny i przypadek pustych czynników oraz pustej rodziny.
3. Drugi aksjomat przeliczalności => ośrodkowość i własność Lindelöfa, przy jasno zadeklarowanym ZFC; zachowanie przez ciągłe surjekcje, ośrodkowości przez otwarte podprzestrzenie i własności Lindelöfa przez domknięte podprzestrzenie i przeliczalne sumy zbiorów.
4. Przestrzenie metryczne: pełna równoważność ośrodkowości, drugiego aksjomatu przeliczalności i własności Lindelöfa; sprawdzono wybory promieni wymiernych i szacowania metryczne.
5. Prosta Sorgenfreya: lokalna baza [x,x+1/n), gęstość Q, brak przeliczalnej bazy globalnej, własność Lindelöfa. W ostatnim dowodzie skontrolowano otwartą część G, zbiór F=R\G, wybór wymiernego q_x, włożenie (x,q_x)⊂G i iniekcję F→Q. Dowód jest poprawny.
6. Płaszczyzna Sorgenfreya: zweryfikowano domkniętość i dyskretność antydiagonali oraz brak własności Lindelöfa. Sprawdzono także przykłady nieprzeliczalnej przestrzeni dyskretnej, topologii koskończonej i jednopunktowego uzwarcenia przestrzeni dyskretnej, a także końcowe kontrprzykłady dla odwróconych implikacji.
7. Terminologia: wyłącznie „spełnia pierwszy/drugi aksjomat przeliczalności”, bez niedozwolonych nazw przymiotnikowych. Quasi-składowe nie należą do tego rozdziału i nie zostały dodane.

Nie znaleziono nieuzasadnionych przeskoków, fałszywych założeń ani brakujących przypadków wymagających zmiany źródła.

## Walidacja i wygląd

- `bash tools/validate_general_topology_ch09.sh`: **PASS** dla wszystkich rozdziałów 01–09.
- Rozdział 09: 390 modeli topologicznych; 2483 rekonstrukcje otwartych zbiorów; 5931 prób gęstości; 5931 prób dziedziczenia; 864 sprawdzenia iloczynów; 96 testów modeli przedziałów Sorgenfreya.
- Kontrola globalna: **364** unikatowe etykiety; **93** odsyłacze, wszystkie rozwiązane.
- LaTeX: samodzielny PDF rozdziału 09 — **7 stron**, cała książka — **80 stron**, bez `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning` oraz błędów odsyłaczy.
- Render 7 stron; kontakt graficzny `/mnt/data/topologia_ogolna_ch09_audit04/contact.png`, kontrola czytelności rysunków i ciągłości przykładów: **PASS**.
- SHA256 źródła i PDF odnotowano w `SHA256SUMS.txt`; źródło pozostawiono bez zmian.

## Decyzja

**Audyt 4 jest czysty: 1/2**. Rozdział 09 pozostaje poza GitHubem do uzyskania drugiego kolejnego czystego audytu. Następny audyt 5 powinien ponownie zweryfikować wersję 0.3, bez poszerzania zakresu. Brak nowych propozycji rozszerzeń tego rozdziału.
