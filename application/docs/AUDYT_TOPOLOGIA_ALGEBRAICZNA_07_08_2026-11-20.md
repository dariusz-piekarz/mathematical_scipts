# Topologia algebraiczna — audyt AT-07 i AT-08

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** wyłącznie rozdziały 07 (fibracje) i 08 (kohomologia); wcześniejsze AT-01–06 występują w kompilacji jedynie jako zależności. Zgodnie z zasadą szczegółowości DG-01 sprawdzono definicje, założenia twierdzeń, rozumowania, rachunki, polską terminologię, odsyłacze, zależności i rysunki.

## AT-07 — fibracje i długi ciąg homotopii

1. **Precyzja podnoszenia:** poprawiono zdanie o jednoznaczności podnoszenia dróg w nakryciach — zależy ona od wyboru początkowego punktu podniesienia. Oddzielono także dokładność niskich stopni dla zbiorów z wyróżnionym elementem od dokładności grup; przy `n=2` opisano obraz przemienny homomorfizmu łączącego w niekoniecznie przemiennej grupie `π₁(F)`.
2. **Monodromia butelki Kleina:** rozszerzono model `K=(S¹×I)/((z,1)~(conj(z),0))`, wyjaśniono lokalną trywialność i konstrukcję przekroju nad pętlą podstawy, otrzymano działanie na `π₁(S¹)=Z` przez `m↦-m`. Pokazano relację `aba^{-1}=b^{-1}`, produkt półprosty i zgodność abelianizacji z wcześniejszym przykładem Hurewicza. Nowe etykiety: `prz:fib-klein-monodromia`, `fig:fib-klein-monodromia`.
3. **Fibracja Hopfa:** dla `h(z,w)=(2z conj(w),|z|²-|w|²)` jawnie porównano przekroje lokalne `s₀(u)=(1,u)/sqrt(1+|u|²)` i `s₁(v)=(v,1)/sqrt(1+|v|²)`. Na przecięciu `s₁(1/u)=(conj(u)/|u|)s₀(u)`, a funkcja przejścia na równiku ma stopień `-1` w przyjętym kierunku. Z długiego ciągu wyprowadzono izomorfizm `∂:π₂(S²)→π₁(S¹)` i `π₃(S³)→π₃(S²)`.
4. **Nietrywialność i brak globalnego przekroju:** osobny przykład dowodzi, że `S³` nie jest produktem wiązkowym `S²×S¹`, a hipotetyczny przekrój dawałby sprzeczność `π₂(S²)≅Z` oraz `π₂(S³)=0`. Nowe etykiety: `prz:fib-hopf-nietrywialna`, `fig:fib-hopf`.
5. **Terminologia:** zastąpiono niewłaściwą formę „sekwencji” przez „ciągu” w odniesieniu do ciągu spektralnego Serre'a.

## AT-08 — kohomologia singularna i iloczyn kubkowy

1. **Rzeczywista korekta dowodu reguły Leibniza:** wcześniejsze rozumowanie błędnie przypisywało kasowanie wyrazom z dwóch środkowych ścian w samej lewej sumie. Rozpisano osobno wyrazy `δ(α∪β)` i oba składniki prawej strony. Redukują się dopiero *dwa dodatkowe składniki* z `δα∪β` i `(-1)^p α∪δβ`, o znakach `(-1)^{p+1}` i `(-1)^p`. Wzór kontrolny w stopniu `p=q=0` zapisano jawnie.
2. **Przykład iloczynu kubkowego na torusie:** kwadrat `[0,1]²` rozcięto przekątną na charakterystyczne trójkąty `[A,B,C]`, `[A,C,D]`; wartości kołańcuchów poziomego i pionowego sprawdzono na wszystkich pięciu krawędziach, w tym na przekątnej. Wzór Alexandra–Whitneya daje wartości `1` i `0`, a więc ocenę `⟨a∪b,[T²]⟩=1`. Wyjaśniono także `a∪a=b∪b=0`, `b∪a=-a∪b`. Nowe etykiety: `prz:kohomologia-kubek-torus`, `fig:kubek-torus`.
3. **Torsja produktu:** dla `X=RP²×RP²` obliczono `H₂(X;Z)≅Z/2Z` ze składnika tensorowego oraz `H₃(X;Z)≅Z/2Z` wyłącznie z `Tor₁(Z/2,Z/2)`. Twierdzenie o współczynnikach uniwersalnych daje `H³(X;Z)≅H⁴(X;Z)≅Z/2Z`. Nowy przykład `prz:kunneth-rp2-razy-rp2` pokazuje, dlaczego nie można pominąć prawego wyrazu ciągu Künnetha.
4. **Konkretny wzór de Rhama:** dla `ω=(x dy-y dx)/(2π)` na `S¹` wyliczono `∫_{S¹}ω=1` i wykluczono dokładność `ω` za pomocą Stokesa. Nowa etykieta: `prz:de-rham-okrag-explicit`.
5. **Terminologia:** „ciąg” zamiast „sekwencja” w opisach homologicznych; nie wprowadzono słowa zakazanego dla operacji iloczynu tensorowego.

## Integralność i kontrola kompilacji

- Nie zmieniano istniejących deklaracji `\label`, argumentów istniejących `\ref` ani żadnych innych kanonicznych rozdziałów. W zestawie AT-01–08 nie ma dwóch deklaracji tej samej etykiety. Wszystkie standardowe odsyłacze z AT-07 i AT-08 mają cele w AT-01–08.
- Rozdziały nie wymagają zewnętrznych obrazów, kodu ani plików danych. AT-07 zawiera 2 nowe diagramy TikZ, AT-08 jeden. Złożenie PDF i przegląd stron 79–80 oraz 85 nie wykazały nachodzących podpisów ani obciętych elementów.
- Testy statyczne i merytoryczne: `application/tests/test_topology_chapters_07_08.py` — oryginalne etykiety, kompletność modułu w książce, brak zewnętrznych zasobów, rachunek fazy Hopfa, przeliczenie monodromii, walidacja kołańcuchów torusa, torsji w Künneth, poprawa formy polskiej i zgodność środowisk LaTeX.
- Kontrola PDF: `.github/workflows/algebraic-topology-audit-ch07-08.yml`, włączenie AT-01–06 do zapewnienia wcześniejszych definicji i celów, dwa przebiegi `pdflatex`, kontrola niezdefiniowanych odsyłaczy i przepełnionych wierszy.
- [GitHub Actions — aplikacja #44764782403](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44764782403) — **SUCCESS**, 148 testów Python, jeden pominięty; Chromium zakończone sukcesem, indeks 355 rozdziałów.
- [GitHub Actions — LaTeX #44764848131](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44764848131) — **SUCCESS**, 90 stron PDF, brak niezdefiniowanych odsyłaczy i `Overfull \hbox`; artefakt `algebraic-topology-audit-ch07-08-pdf` zawiera źródło wynikowe i logi.

## Zakres pozostałych zależności

Końcowe porównanie de Rhama jest w AT-08 jawnie zapowiedziane jako materiał rozwijany w następnym rozdziale. Audyt AT-08 sprawdził jego sformułowanie, przykład i użyte zależności, ale nie jest jeszcze odrębnym audytem kompletnego dowodu w rozdziale o de Rhamie. Podobnie rozbudowany dowód konstrukcji ciągu spektralnego Serre'a nie należy do AT-07 — jest jedynie zapowiedziany.

**Status:** AT-07 i AT-08 zaakceptowane w zakresie niniejszej pary; wpisy z dowodami i wynikami walidacji zapisano w `application/data/AUDYT_ROZDZIALOW.csv`. **Następna iteracja: AT-09 i AT-10**, po dwa rozdziały na iterację, ze szczegółowym audytem, poprawkami źródeł, wizualnym przeglądem rysunków i retestem.

Prace wykonano wyłącznie na `biblioteka-matematyczna-iteracja-6`. Gałąź `main` pozostawiono bez zmian.
