# AM II 30 — audyt kontrolny

Data: 2026-11-28. Źródło: commit 57ed552d52bcbab1c31b1948526819048ccb8acb, blob 86f4e5e6c7a2f5913f2adf23bc6e6624bb0c9b69, 921 wierszy. Na gałęzi roboczej potwierdzono identyczny blob.

## Kontrola matematyczna
- Tonelli i Fubini: zweryfikowano rozróżnienie nieujemności i całkowalności bezwzględnej, uzupełnienie produktu miar oraz definicję całek przekrojowych z wyjątkami miary zero.
- Przekroje obszarów: granice pionowe i poziome, także przekroje rozłączne, zgodne z nierównościami. Wartości 1/6, 3−e, (e−1)/2, 5/12 poprawne.
- Iterowanie Riemanna: wszystkie przekroje w hipotezie, ograniczoność funkcji całek, nierówności Darboux i argument wspólnego przedziału o dowolnie małej długości. Przykład Dirichleta odróżnia całkowalność przekrojów Riemanna i Lebesgue'a.
- Zbiór Vitaliego na przekroju zerowej miary produktu: brak mierzalności przekroju, nie utożsamiono przypisanej wartości zero z jego miarą.
- Kontrprzykład Fubiniego: pochodne cząstkowe, wyniki ±π/4 oraz rozbieżność obu części funkcji z oszacowania na klinie poprawne.
- Wielokrotne iterowanie: permutacje współrzędnych, iloczyny funkcji mierzalnych, indukcja dla objętości sympleksu i moment 1/24 czworościanu.
- Zamiana zmiennych: dyfeomorfizmy, moduł wyznacznika i całkowalność; wersja Riemanna wykorzystuje obraz brzegu zwartego zbioru Jordana oraz lokalną własność Lipschitza; wersja poza zbiorem wyjątkowym poprawnie wymaga zerowości obu pominiętych zbiorów.
- Przykłady podstawień: (u³,v), (u,uv), układ hiperboliczny — poprawne wyznaczniki i wyniki 2, 1/2, 3 log 3. Afiniczny wzór na objętość elipsoidy poprawny.
- Współrzędne biegunowe, walcowe i sferyczne: różnowartościowość na wskazanych otwartych dziedzinach, zerowość pominiętych zbiorów, jakobiany r i ρ² sin φ. Rachunki Gaussa, objętości pod paraboloidą, między stożkiem i paraboloidą, kuli, momentu radialnego i wycinka sferycznego poprawne. Przykład dwóch obrotów poprawnie wykazuje dwukrotne liczenie pola.

## Statyka i technika
30 etykiet; 33 odsyłacze wewnętrzne, 14 zewnętrznych. Wszystkie cele zweryfikowano w aktualnych źródłach AM II 18,24,26,27,30 i ME 04,12,13. Brak duplikatów etykiet rozdziału w kontrolowanych rozdziałach. Bilans klamer 0, minimalny bilans 0, zagnieżdżenie środowisk poprawne. Katalog i entrypoint: rozdział 30 po 29, przed 36; trzy rysunki bez zmian, kompilacji rysunków w tym przebiegu nie ponawiano.

CI źródła 57ed552: terminologia #46133718789 success; walidacja AM II #46133718722 in_progress, #46133724045 skipped; aplikacja #46133718724 cancelled. Nie uruchomiono dodatkowego workflow. Pełny PDF niepotwierdzony.

Wynik: zero nowych uwag merytorycznych i statycznych. Rozdział zamknięty merytorycznie, odbiór techniczny całego tomu otwarty.

## Przygotowanie rozdziału 31
Sprawdzono rzeczywiste źródła AM II 29 (ma2:thm:curve-ac-length, ma2:thm:curve-arclength, ma2:thm:curve-length-multiplicity, ma2:thm:curve-reparam), ME 28 (thm:lipschitz-area-coarea-28), DG 10 (def:forma-rozniczkowa, prop:formy-wedge-pullback, thm:lemat-poincare-formy, cor:stokes-ftc). Plan: całki pierwszego rodzaju z wagą długości, rozróżnienie całki po obrazie względem H¹ i całki po drodze z krotnością, całki drugiego rodzaju jako całki współrzędnościowe i cofnięcia 1-form, addytywność, zmiana orientacji, niezmienniczość przy odpowiedniej reparametryzacji, twierdzenie o funkcji pierwotnej, niezależność od drogi oraz pole zachowawcze na obszarze gwiaździstym, kontrprzykład na płaszczyźnie bez punktu. Całki ze względu na długość dla ciągłych krzywych prostowalnych definiować za pomocą parametru długości łuku; nie stosować wzoru z prędkością do arbitralnej ciągłej parametryzacji. Przykłady i ilustracje; twierdzenia Greena i Stokesa rozwinąć w późniejszym rozdziale. Bez abstrakcyjnych rozmaitości riemannowskich. Rozdział 31 nie został jeszcze utworzony.
