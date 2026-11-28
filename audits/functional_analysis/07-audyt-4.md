# Analiza funkcjonalna — rozdział 07 — audyt 04 (pierwsza kontrola stabilizacyjna)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex.  
**SHA kontrolowanego źródła:** 3802015b41891911fe852e6a2600547d894fab8c — identyczny z końcową wersją po audycie 07/03.  
**Werdykt matematyczny, redakcyjny i techniczny:** **CZYSTY — 1/2** kolejnych czystych audytów. Rozdział źródłowy niezmieniony, pełny CI i kontrola PDF zakończone pomyślnie. Rozdział 07 nie jest jeszcze stabilny.

## Przedmiot niezależnego audytu

Odczytano ponownie aktualną pełną treść rozdziału, bez ograniczania się do wcześniejszych raportów. Skontrolowano wszystkie 11 dowodów, cztery przykłady, jawność założeń, dziedziny funkcjonałów, wariant rzeczywisty i zespolony, separację punktową a separację z luką, topologie produktowe/słabe, warunki brzegowe dla zbioru pustego i przestrzeni nie-Hausdorffa. Dotychczasowe poprawki dotyczące Minkowskiego, domknięcia wyjściowego C i aco(∅) pozostają poprawne. Nie zmieniono żadnego twierdzenia, definicji, etykiety ani rysunku.

## Matematyka — 11/11 dowodów PASS

1. **Ciągły funkcjonał rzeczywiście liniowy na zespolonej TVS:** rekonstrukcja F(x)=ell(x)−i ell(ix) jest zespolono-liniowa, jednoznaczna, ciągła; potrzebne ciągłości mnożenia przez i nie pominięto.
2. **Minkowski otwartego wypukłego otoczenia V:** pochłanianie, skończoność p_V, dodatnia jednorodność i podaddytywność wynikają z wypukłości także bez zrównoważenia. Warunek r>p_V(x) pozwala wybrać x=ru z u∈V; w dowodzie z r,s i przejściem do infimum nie założono symetrii. Równość V={p_V<1} i kontrola x−y w epsilon V∩(−epsilon V) dowodzą ciągłości.
3. **Oddzielanie otwartego C od punktu x0:** D=C−x0, wybór a∈D i V=D−a dają −a∉V. Jednowymiarowe g(t(−a))=t ma dominację przez p_V dla t≥0 i t<0. Hahn–Banach, po oszacowaniu −p_V(−x)≤ell(x)≤p_V(x), daje ciągły, niezerowy separator, z ell(c)<ell(x0) dla każdego c∈C; nie wyciągnięto fałszywego wniosku o jednolitej luce.
4. **Dwa rozłączne zbiory wypukłe, jeden otwarty:** A−B jest otwarty, wypukły, nie zawiera zera. Separator dla A−B daje nierówność dla każdej pary (a,b); ustalenie b0 i a0 zapewnia skończoność sup_A ell oraz inf_B ell, co pozwala wybrać wspólne c.
5. **Jedno otoczenie dla zwartego K i domkniętego F:** dla k∈K otoczenia V_k, W_k z W_k+W_k⊂V_k, skończone podpokrycie i wspólne U gwarantują (K+U)∩F=∅. Dla lokalnej wypukłości można zachować otwartość i wypukłość otoczeń. Nie wymaga to sekwencyjnego charakteru zwartości.
6. **Silne oddzielanie zwartego A i domkniętego B:** A+U jest otwarty, wypukły, nie przecina B. Dla niezerowego ciągłego ell istnieje u0∈U z ell(u0)>0; z nierówności ell(a+u0)<ell(b) wyprowadza się jednolitą delta=ell(u0)>0. Poprawne przejście do sup/inf.
7. **Punkt poza domkniętym wypukłym C:** zastosowanie silnej separacji do A={x0} i B=C w rzeczywistej TVS, bez nieuprawnionego założenia Hausdorffa.
8. **Hiperpłaszczyzna podpierająca:** otwarte G=int(C) jest wypukłe. Przy x∈C, g0∈G i t∈(0,1] kombinacja (1−t)x+tg0 należy do G, ponieważ x_t+tV⊂C, a granica w t↓0 przenosi nierówność na C.
9. **Własności polary:** antymonotoniczność; A°=(aco A)°; A⊂A°°; polara jest zrównoważona i wypukła także nad C, domknięta w σ(X',X), a bipolar domknięty w X jako przecięcie poziomic ciągłych funkcjonałów. Pusty A obsługiwany przez aco(∅)={0}.
10. **Twierdzenie bipolarne:** C=cl(aco A) jest niepuste, domknięte, wypukłe i zrównoważone. Silne oddzielanie x0 spoza C wytwarza ell(x0)>sup_C ell. Nad C funkcjonał F z Re F=ell ma sup_C|F|=sup_C Re F dzięki zrównoważeniu; rozdzielono przypadki m>0 i m=0. Kontrargument dla x0∈A°° jest poprawny również dla A pustego.
11. **Równość słabego i wyjściowego domknięcia zbioru wypukłego:** przy C=∅ oczywista. Dla C niepustego wyraźne zastosowanie separacji do D=cl C (domkniętego, wypukłego), a nie do niekoniecznie domkniętego C. Ciągła ell jest częścią rzeczywistą F∈X', więc półprzestrzeń zawierająca x0 i rozłączna z C jest otwarta w topologii σ(X,X'). Obie inkluzje dowiedzione.

## Przykłady — 4/4 PASS

1. A=(−1,0), B={0}: każdy punkt oddzielony ściśle przez ell(x)=x, brak jednolitej luki ze względu na zbieżność punktów A do 0.
2. Polarność rombu kuli jednostkowej ℓ¹ i kwadratu kuli ℓ∞ w R²: dokładne oszacowanie supremum liniowego przez normę ∞; diagram TikZ zgodny z wzorami.
3. X=K^N z topologią produktową: ograniczone na wektorach bazowych ciągłe funkcjonały o skończonym nośniku, polara z warunkiem |a_n|≤1, bipolar jako kula ℓ¹. Obie inkluzje domknięcia: ciągłość każdej skończonej sumy |x_n| i zbieżność obcięć x^(m) do x w topologii produktowej.
4. X=L^p([0,1]), 0<p<1: X'={0}; dla A={0} bipolar=A°°=X, natomiast cl(aco A)={0}; poprawny kontrprzykład do bipolarności bez lokalnej wypukłości.

## Przypadki brzegowe i regresje

- Konwencja aco(∅)={0} została zachowana: jest to najmniejszy **niepusty** zbiór wypukły i zrównoważony zawierający A. Nie odwołuje się do nieprawdziwej minimalności bez dodatkowego warunku niepustości.
- Zweryfikowano, że funkcjonał Minkowskiego na V=(−∞,1)⊂R ma postać p_V(x)=max(x,0), jest podliniowy i ciągły, ale nie musi być normą ani parzysty.
- Zweryfikowano działanie silnej separacji także w lokalnie wypukłej nie-Hausdorffa TVS R² generowanej przez p(x,y)=|x|: A={(1,0)}, B={3}×R są rozłączne, A zwarty, B domknięty; ell(x,y)=x jest ciągłym separatorem z dodatnią luką.
- Dodano **dwa nowe testy regresyjne** w tools/tests/test_functional_analysis_ch07.py; zestaw wzrósł z 20 do **22 testów**, bez modyfikowania źródła rozdziału.

## Struktura, język i odsyłacze

- 11/11 środowisk proof, 4/4 środowisk przyklad, 17 unikatowych etykiet, 12 wystąpień odsyłaczy i **0 brakujących celów** w rzeczywistych rozdziałach 01–07. Pozostałe środowiska lematów, twierdzeń, stwierdzeń, wniosków, definicji i uwag mają zgodne otwarcia i zamknięcia.
- Zachowano terminologię: „przestrzeń sprzężona” zamiast niedozwolonego rzeczownikowego „dual”; poprawne polskie terminy dotyczące zwartości i topologii.
- Źródło LaTeX identyczne blob SHA z audytem 07/03. Etykiety, sekwencja rozdziałów i schemat polarności niezmienione.
- Dedykowane [GitHub Actions 45186232281](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45186232281) zakończyło się **pełnym SUCCESS** przy niezmienionym blob SHA rozdziału. Wszystkie **22/22 testy PASS**, przygotowanie kontekstu rzeczywistych rozdziałów 01–07, kompilacja LaTeX, kontrola końcowego PDF i odsyłaczy oraz publikacja artefaktu PASS. W logu: `Ran 22 tests`, `OK`, `Pages: 43`.
- Pobrano wynikowy **43-stronicowy PDF A4** (556327 bajtów) z [CI 45185870226](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45185870226), uruchomionego dla dokładnie tego samego źródła i 22 testów. Wyrenderowano i obejrzano strony **39–43**, zawierające cały rozdział 07 i diagram rombu/kwadratu: **0 bloków poza stroną**, bez widocznych kolizji tekstu, ucięć i uszkodzeń znaków. Końcowy log LaTeX zawiera **0** `Undefined control sequence`, `There were undefined references`, `Overfull \\hbox`, `Missing character`. Przejściowe ostrzeżenie po pierwszym przebiegu kompilacji nie występuje po końcowym przebiegu.

## Decyzja

**CZYSTY audyt 07/04, 11/11 dowodów PASS, 4/4 przykłady PASS, 22/22 testy PASS, pełny CI i PDF zweryfikowane. Zalicza się jako 1/2 kolejnych czystych audytów bez zmian źródła.** Kolejny wymagany etap: niezależny audyt 07/05 aktualnej wersji. Nie rozpoczynać rozdziału 08 przed uzyskaniem 2/2.
