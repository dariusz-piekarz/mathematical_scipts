# RRC 12 — iteracja 204: odrębny audyt kontrolny i zamknięcie

Kontrolowana wersja źródła: blob c673beaec26ce80dc4af0d4cf1b7bbef9819d43a, commit c7629cded8fc9e179981555b1cd6d31386b96fed; ponownie potwierdzono identyczność na gałęzi biblioteka-matematyczna-iteracja-6. Nie wprowadzono zmian do źródła. Odrębny przebieg kontrolny wykonano na ustabilizowanym tekście, po czwartej lekturze, przez ponowną kontrolę zależności dowodowych i założeń (nie jest to recenzja innego matematyka).

| Kryteria | Kontrola merytoryczna |
|---|---|
| 001–012 | Domknięcie wykresu, zupełność normy grafowej, znak sprzężenia pochodnej, obie inkluzje dziedzin, koercywność rzeczywistej formy, zwartość i samosprzężoność B, odwrócenie A+I, regularność C^{1,1}, narożnik: bez nowych usterek. |
| 013–026 | Dodatnia forma i maksimum Rayleigha, realifikacja, słaba i silna zbieżność, ortogonalne dopełnienia, jądro i krotności, inwolucja na E_mu, separowalność i nieskończony wymiar, ważona baza formy, min–max, przedłużenie przez zero i baza produktowa: bez nowych usterek. |
| 027–040 | Ograniczoność odwrotności, znak rezolwenty, zespolenie, luka spektralna, rezonans i minimalna norma, skończony rząd i indeks, faktoryzacja B, dziedzina mnożnika Fouriera, powłoki i translacje: bez nowych usterek. |
| 041–054 | Normy półgrupy i potęg, generator, obie pochodne, wspólna ciągłość całkowanego wyrażenia, całka grafowa, domkniętość A, kontrprzykład na rozłącznych przedziałach, lokalny bootstrap: bez nowych usterek. |
| 055–068 | Rozszerzenie energetyczne, ogony w V i H, druga pochodna w V*, jednoznaczność modalna, wzmocnione dane, unitarność, generator, niezmienniczość dziedzin, brak wygładzania, znak Stone'a i dolne ograniczenie widma: bez nowych usterek. |

Weryfikacja hipotez: ponownie odczytano twierdzenia RRC 08 (Plancherel i pochodne), 10 (ślad, Rellich–Kondrachov, Poincaré), 11 (Lax–Milgram i słaba zwartość) oraz 15 (regularność brzegowa i wewnętrzna, bootstrap). Sprawdzono wszystkie osiem kotwic z AF w przypiętych źródłach, każda występuje dokładnie raz, a tezy odpowiadają użyciu. W szczególności AF 33 zapisuje Stone'a dla e^{itA}; znak -iA w RRC jest zgodny z e^{-itA}.

## Indeks Atlasu — dowód z rzeczywistego CI

Przebieg 45685021369, artefakt reference-provenance-audit 15054884832, pobrany plik ZIP. Pliki graph_coverage.json i reference_provenance_audit.json pochodzą z odczytu rzeczywistego indeksu SQLite, nie z ręcznie rekonstruowanego grafu. Wiersz PDE-12: cross_outgoing=8, cross_incoming=3, within_domain=29, unresolved=0, isolated=false, cross_isolated=false. Krawędzie wychodzące typu reading: FA-13=1, FA-15B=2, FA-30=1, FA-33=4. Zestawienie wszystkich ośmiu atlasref w źródle z unikatowymi etykietami docelowymi i tymi licznościami potwierdza 8/8 odsyłaczy. Raport jest zagregowany na poziomie par rozdziałów, nie eksportuje osobnego wiersza każdej rozwiązanej referencji; nie twierdzimy, że odczytano osiem osobnych wierszy SQLite. Żaden z 13 historycznych nierozwiązanych odsyłaczy w całym indeksie nie pochodzi z PDE-12. Globalny audyt: 580 dokumentów, 494 kwalifikowane odsyłacze lekturowe, 0 niepoprawnych.

## Walidacja przypiętego źródła

33 zachowanych etykiet, 50 odsyłaczy (30 celów), poprawny stos środowisk. Dedykowane CI 45685098403 SUCCESS, 10 testów regresyjnych; kompilacja i kontrola diagnostyki SUCCESS. Artefakt 15055434127, 22 strony A4 obejrzane w iteracji 203. CI Atlas 45685021369 i terminologia 45685021437 SUCCESS. Źródło nie zmieniło się od tych walidacji. Nie wykonywano ponownej kompilacji tego samego blobu, pełnej kompilacji książki ani formalizacji Lean. Testy skończone nie zastępują dowodów. PDF samodzielnego rozdziału zawiera numery odsyłaczy do nieobecnych rozdziałów, nie pełne hiperłącza książkowe.

**Decyzja:** rozdział 12 zamknięty w zakresie uzgodnionego audytu rozdziałowego (trzy szczegółowe przebiegi, czwarty stabilizacyjny bez nowych usterek merytorycznych, odrębny kontrolny, CI, PDF i indeks). Kolejna iteracja rozpoczyna rozdział 13 — eliptyczne zagadnienia brzegowe: inwentaryzacja zależności i pierwsza lektura, bez powielania zweryfikowanych wyników rozdziałów 09–12.
