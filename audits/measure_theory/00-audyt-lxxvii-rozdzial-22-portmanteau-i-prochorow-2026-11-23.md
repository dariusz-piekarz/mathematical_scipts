# Audyt LXXVII (77) — rozdział 22: Portmanteau, Prochorow i zbieżność miar

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts.
Istniejąca gałąź: biblioteka-matematyczna-iteracja-6.

## Bramka wejścia

Rozdział 21 został zamknięty po audytach LXXIV–LXXVI na blobie fd6eedf8e96f645283ba837061cc3e7c0e955aae. Potwierdzony przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45280854102 obejmował 8+4 zaliczonych testów, pełną książkę (260 stron), samodzielny rozdział 21 (7 stron) i oględziny wszystkich stron. Raport zamknięcia rozdziału 21: audits/measure_theory/00-audyt-lxxvi-rozdzial-21-zamkniecie-2026-11-23.md, commit 4772635536069af42398ad853a60bbae4bfce5d6.

## Pierwszy szczegółowy przegląd matematyczny rozdziału 22

Plik: chapters/pl/measure_theory/22-zbieznosc-miar-twierdzenie-portmanteau-i-zwartosc-prochorowa.tex.
Blob po aktualizacji: 563cdab3f5aaa0bad2b9c74645cab9d5abe00e0a.

Przeczytano pełny rozdział, w tym:
1. Oddzielenie zbieżności wąskiej względem C_b, mglistej względem C_c i słabej-* względem C_0. Przykłady ucieczki masy do nieskończoności.
2. Twierdzenie Portmanteau: otwarte i domknięte zbiory, całki funkcji dolnie półciągłych, zbiory ciągłości miary oraz domknięcie implikacji przez podziały zakresu funkcji ciągłej z granicami nieatomowymi dla jej rozkładu obrazowego.
3. Zbieżność w wariacji całkowitej i brak implikacji odwrotnej.
4. Definicję jednostajnej ciasności; aproksymowanie funkcji ciągłych na zwartym K przez funkcje Lipschitzowskie i przedłużanie; dowód zwartości P(Y) dla zwartej przestrzeni metrycznej przez diagonalizację na przeliczalnej gęstej rodzinie C(Y) i twierdzenie Riesza z rozdziału 21.
5. Włożenie separowalnej przestrzeni metrycznej w kostkę Hilberta, w tym argument ciągłości odwrotności na obrazie.
6. Kierunek Prochorowa „ciasność implikuje względną zwartość ciągową” na przestrzeni separowalnej, także bez założenia zupełności, przez przeniesienie miar do zwartego Y, zachowanie masy na przeliczalnej sumie obrazów K_m, zdefiniowanie granicy na X i przedłużenie funkcji testowych ze zbioru zwartego.
7. Odwrotność na przestrzeni polskiej, przez sprzeczność z Portmanteau dla rosnących skończonych pokryć kulami na kolejnych skalach; zwartość wspólnego przekroju w metryce zupełnej.
8. Ciasność z momentów oraz związek pomiędzy zbieżnością mglistą i wąską dla prawdopodobieństw.

Przegląd pierwszego przejścia nie wykrył błędu w głównych tezach wymagającego ich zmiany. Dla wielu pośrednich nierówności nie jest wystarczające samo przejście testów numerycznych; dowody wymagają osobnej drugiej iteracji.

## Uzupełnienie matematyczne i redakcyjne

W commicie c633864a0d8fb9d2da48c45581b8715d1cfa074f dodano szczegółowo obliczony kontrprzykład:
- X=R, μ_n=(1-1/n)δ_0+(1/n)δ_n i μ=δ_0;
- d_TV(μ_n,μ)=1/n→0, co implikuje zbieżność wąską, a rodzina jest jednostajnie ciasna;
- dla każdego n pierwszy moment ∫|x| dμ_n=1, ale moment granicy wynosi 0.
Pokazuje to, że nawet zbieżność w wariacji całkowitej oraz jednostajne ograniczenie pierwszych momentów nie gwarantują ich zbieżności bez dodatkowej jednostajnej całkowalności. Rozróżniono testowanie funkcjami ograniczonymi od nieograniczonej funkcji |x|. Dodano etykietę ex:moment-not-continuous-22.

W tym samym commicie poprawiono składnię zdania o ciągach całek przy konstrukcji gęstej rodziny w C(Y): „każdy ciąg liczb ... jest ograniczony”.

## Trwałe regresje i kompilacja

Utworzono tools/tests/test_measure_theory_ch22.py, commit 078d05e1169c55db8202a3d12eb33e5d10e3a5bd, blob 5ae059402942c0b17fd282e8a62d406bac29bc39.
Osiem metod: atomowy model Portmanteau i wariacji, zbieżność punktowych miar Diraca bez TV, przykład zbieżności mglistej bez C_0, model przedłużenia lipschitzowskiego, włożenie w kostkę Hilberta, skończone modele ciasności, kontrprzykład momentowy i kontrola źródła LaTeX.

Utworzono .github/workflows/measure-theory-ch22.yml, commit 33dc92c2c938304592337f17c133e79ff5750cfa, blob eaf14a6502cc5582911aa6ce4d3459deafe22003. Workflow uruchamia osiem testów rozdziału, cztery testy integralności całej książki, kompilację pełnego 31-rozdziałowego tomu oraz osobnego PDF rozdziału 22 z zachowaniem numeracji i importem odsyłaczy z AUX przez xr-hyper. Publikuje osobne statusy measure-theory/ch22-regressions i measure-theory/ch22-pdf.

Kontrola statyczna: 22 unikalne etykiety, 14 wystąpień ref/eqref, 40 poprawnie zagnieżdżonych par begin/end. Zidentyfikowano cztery różne odsyłacze zewnętrzne do rozdziałów 20 i 21. Nie jest to jeszcze wynik rzeczywistej kompilacji.

## Werdykt

**ROZDZIAŁ 22: PIERWSZY PRZEGLĄD WYKONANY, W STABILIZACJI.**
W chwili sporządzania raportu zapytania o klasyczne statusy dla commitu 33dc92c2c938304592337f17c133e79ff5750cfa zwracały pustą listę. Nie oznacza to ani sukcesu, ani błędu CI. Konieczny jest odczyt faktycznego przebiegu, sprawdzenie 8+4 testów, całej książki i osobnego PDF oraz niezależny drugi audyt matematyczny, zwłaszcza dowodów Portmanteau i Prochorowa. Nie przechodzić do rozdziału 23 przed stabilizacją 22.
