# Topologia ogólna — rozdział 21, audyt 02 (kontrola niezależna)

**Data:** 2026-11-22. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Badany blob:** b63abaad5fea93f2a5d4317c8be1ada73fcbe1a2.
**Wynik matematyczno-redakcyjny:** CZYSTY, pierwsza kontrola bez usterek (1/2).
**Walidacja wydawnicza:** pełny CI i PDF bieżącego bloba w toku w momencie sporządzania; nie przypisujemy im z góry sukcesu. Matematyczny status stabilności pozostaje warunkowy.

## Niezależne sprawdzenie struktur

1. W Vietorisie zarówno trafianie otwartego U, jak i całkowite zawieranie w U są potrzebne. Dowód bazy uwzględnia pustą rodzinę warunków dolnych oraz otwarty V będący przecięciem wszystkich ograniczeń górnych.
2. W ogólnym X zanurzenie j(x)={x} jest homeomorfizmem na obraz, niezależnie od oddzielania X. Dla X Hausdorffa zbiór singletonów jest domknięty, ponieważ dowolny zwarty zbiór o dwóch różnych punktach ma otoczenie U^- ∩ V^- wolne od singletonów.
3. K(f) nie wymaga osobnych warunków o X/Y: obraz niepustego zwartego przez ciągłe f jest niepusty zwarty; sprawdzono przeciwobrazy obu rodzajów podbazy.
4. Dla każdej metrycznej X d_H jest metryką na K(X). W szczególności konieczne jest założenie niepustości obu zbiorów; podzbiór zwarty przestrzeni metrycznej jest domknięty i ograniczony.
5. Dla topologii d_H ⇒ Vietorisa: warunek trafienia jest stabilny pod małym zaburzeniem d_H, a odległość zwartego K od zamkniętego X\U ma dodatnie minimum. Dla Vietorisa ⇒ d_H: skończone pokrycie K kulami promienia r/3 oraz warunek górny r/2 skutkują d_H(K,L)<r.
6. W dowodzie zupełności podciąg A_j jest wybrany tak, że kolejne d_H są mniejsze od 2^{-j}. Funkcje d(.,A_j) są jednostajnie Cauchy'ego, a ich granica ma niepusty, domknięty zbiór zerowy K. Każdy punkt A_j daje łańcuch długości najwyżej 2^{1-j} do K; jednostajny limit funkcji odległości zapewnia drugie jednostajne oszacowanie. K jest całkowicie ograniczony i zupełny, więc zwarty. Tym samym można legalnie użyć d_H(A_j,K).
7. Zwartość K(X) dla metrycznie zwartego X: każde K jest bliskie pewnemu niepustemu podzbiorowi ustalonej skończonej sieci S, a takich podzbiorów jest skończenie wiele. Zupełność dostarcza zwartość. Dla niekoniecznie metrycznego zwartego Hausdorffa X dowód przez ultrafiltr na K(X) jest niezależny.
8. Kryterium podbazowe Aleksandra jest wyprowadzone z twierdzenia o ultrafiltrach rozdziału 07: brak granicy ultrafiltru daje pokrycie podbazowe bez skończonego podpokrycia.
9. W Fellu pusta podprzestrzeń jest uwzględniona w rodzinie wszystkich domkniętych. Dla hipotetycznego pokrycia przez U_i^- oraz C_j^0 bez podpokrycia skończonego wybieramy F=X\setminus\bigcup U_i; zwartość C_j wymusza C_j∩F≠∅, co obala pokrycie. Twierdzenie rzeczywiście nie wymaga Hausdorffa X.
10. Hausdorff \(\mathcal F(X)\) przy lokalnej zwartości Hausdorffa X uzyskujemy ze zwartego otoczenia o domknięciu C wewnątrz X\G i rozłącznych warunków W^- oraz C^0.
11. Dla zwartej Hausdorffa X podbazy Vietorisa i Fella po ograniczeniu do K(X) są identyczne przez branie dopełnień. Dla X=R ciąg {0,n} zbiega w Fellu do {0}, choć d_H({0,n},{0})=n; pokazuje ściśle słabszą topologię ograniczoną Fella.

## Redakcja, LaTeX, integracja

Źródło: 724 wiersze, 31 unikatowych etykiet, 9 odsyłaczy,
wszystkie cele w rozdziałach 07, 14, 18 i 21.
Nie znaleziono niedomkniętych środowisk twierdzeń, dowodów
ani rysunku. Poprawiono poprzednio wykrytą kolizję etykiet;
w przykładzie odległości zbiorów są teraz ułamki 1/5 i 17/10.
W całym źródle nie występuje już makro \mathscr,
niedostępne w preambule książki.

Testy skończonych modeli rozdziału 21 i testy wcześniejszych rozdziałów
zostały wykonane pomyślnie przez CI 45042012708 na poprzednim blobie,
ale tamten przebieg nie zbudował PDF ze względu na \mathscr.
Nowy przebieg [45042232081](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45042232081)
jest przeznaczony do weryfikacji aktualnego bloba; wynik do odczytania
przed wydaniem statusu ostatecznego.

**Wynik audytu 02:** matematyka czysta (1/2), bez edycji źródła.
CI i PDF pozostają obowiązkowym, oddzielnym warunkiem stabilizacji.
