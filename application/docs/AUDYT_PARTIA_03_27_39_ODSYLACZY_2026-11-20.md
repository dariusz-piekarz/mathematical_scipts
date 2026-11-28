# Biblioteka matematyczna — audyt integralności odsyłaczy, partia 03 (27–39)

**Data:** 20 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Podstawa:** raport `reference_provenance_audit_355.json` (355 rozdziałów), źródła `chapters/pl/differential_geometry_and_topology/{06,07,08}-*.tex` i mapa wystąpień oraz kandydatów. Sprawdzono cytowany kontekst i rzeczywistą deklarację każdego proponowanego celu. Nie scalono skryptów; nie zmieniono `\label`, `\ref`, dowodów ani kanonicznych plików TeX.

## Zasada obowiązująca przy kopiowaniu z Biblioteki

Kopiowany fragment zachowuje **wszystkie pierwotne `\label{...}` i odsyłacze z niezmienionymi argumentami**, także ich wielokrotność. Zmiana nazwy podczas kopiowania jest niedopuszczalna. Konflikt wielu właścicieli tej samej etykiety rozstrzygamy osobno, przez jawną mapę pochodzenia i zweryfikowany kontekst; żadne rozstrzygnięcie poniżej nie jest cichą zmianą nazwy w kopii. Reguła jest wpisana do globalnego `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` i sprawdzana skryptem `verify_copied_labels.py`.

## Audyt wystąpień 27–39

| Nr | Źródło | Etykieta | Kandydaci z indeksu | Kontrola znaczenia | Proponowany cel / status |
|---|---|---|---|---|---|
| 27 | `DG-08:1168` | `prz:pi1-sfera` | `DG-07:1247`, `TOP-04:860` | Przykład `DG-07` opisuje dokładnie deformację punktów pasa sferycznego na równik przez zmniejszanie współrzędnej wysokości. W `DG-08` konstrukcja służy do obliczenia homologii sfery przez Mayera–Vietorisa, nie do ponownego dowodu o `π₁`. | Preferować `DG-07`, **propozycja lokalna**. |
| 28 | `DG-08:1256` | `lem:pieciu` | `DG-06:1996`, `TOP-03:1705` | W dowodzie porównuje się długie ciągi par `(X,A)` oraz `(X,N)`. W `DG-06` jest lemat pięciu z warunkami na mapy zewnętrzne i sąsiednie. **Zastrzeżenie matematyczne:** trzeba jawnie zweryfikować naturalność odwzorowań łączących i pozostałe izomorfizmy, zamiast uznawać samo istnienie diagramu za dowód. | Preferować `DG-06`, **propozycja wymagająca kontroli dowodu**. |
| 29 | `DG-08:1313` | `thm:pi1-dolaczenie-komorki` | `DG-07:2178`, `TOP-04:1435` | Cytat dotyczy konstrukcji otwartego pasa, retrakcji promieniowej i ciągłości przy sklejeniu; dokładnie te kroki znajdują się w dowodzie twierdzenia w `DG-07:2191–2216`. Używa się *argumentu z dowodu*, a nie jego tezy o grupie podstawowej; należy to wyraźnie nazwać w przyszłej redakcji. | Preferować **dowód** w `DG-07`, **propozycja lokalna**. |
| 30 | `DG-08:1333` | `prop:brzeg-sympleksu` | `DG-07:1389`, `TOP-04:962` | W `DG-07` jest dokładnie stwierdzenie, że `∂Δⁿ` jest homeomorficzny z `Sⁿ⁻¹` przy `n ≥ 1`; odpowiada zastosowaniu w obliczeniu względnej homologii sympleksu. | Preferować `DG-07`, **propozycja lokalna**. |
| 31 | `DG-08:1462` | `lem:pieciu` | `DG-06:1996`, `TOP-03:1705` | Diagram zestawia długie ciągi dla par symplicjalnych i singularnych. `DG-06` zawiera wymagany lemat. **Zastrzeżenie:** należy skontrolować wszystkie hipotezy indukcyjne i zgodność map łączących, w szczególności mapy skrajne. | Preferować `DG-06`, **propozycja wymagająca kontroli dowodu**. |
| 32 | `DG-08:1491` | `sec:cw-kompleksy` | `DG-07:1853`, `TOP-04:1148` | `DG-07` wprowadza CW-kompleksy i dołączanie komórek, których oszczędność w stosunku do triangulacji jest motywacją dla homologii komórkowej. | Preferować `DG-07`, **propozycja lokalna**. |
| 33 | `DG-08:1995` | `prz:cw-s2` | `DG-07:2072`, `TOP-04:1344` | W `DG-07` jest dokładnie model `S² = D²/∂D²` z jedną `0`-komórką i jedną `2`-komórką, bez `1`-komórek. | Preferować `DG-07`, **propozycja lokalna**. |
| 34 | `DG-08:2020` | `prz:pi1-torus-rp2` | `DG-07:2269`, `TOP-04:1493` | Dla torusa w `DG-07` występuje 1-szkielet `S¹ ∨ S¹` i relacja komutatora `aba⁻¹b⁻¹` po dołączeniu komórki, zgodne z obliczeniem `∂₂ = 0`. | Preferować `DG-07`, **propozycja lokalna**. |
| 35 | `DG-08:2069` | `prz:pi1-torus-rp2` | `DG-07:2269`, `TOP-04:1493` | Dla `RP²` ten sam przykład `DG-07` daje odwzorowanie dołączające stopnia 2, zgodne z komórkowym `∂₂ = ×2` i torsją `H₁(RP²; Z)`. | Preferować `DG-07`, **propozycja lokalna**. |
| 36 | `DG-08:2096` | `sec:wspolczynniki-euler` | `DG-06:1633`, `TOP-03:1362` | Sekcja `DG-06` odróżnia torsję od obliczeń po zmianie współczynników; to właściwy odsyłacz do zjawiska `Z/2` w homologii `RP²`. Dla ścisłości definicja torsji w tym samym skrypcie pojawia się wcześniej (`DG-05`), lecz obecny tekst cytuje **sekcję**, więc nie należy zmieniać celu bez decyzji redakcyjnej. | Preferować `DG-06`, **propozycja lokalna**. |
| 37 | `DG-08:2189` | `eq:homologia-char-zero` | `DG-06:1799`, `TOP-03:1516` | Formuła `Hₙ(C;F) ≅ Hₙ(C;Z) ⊗ F` w `DG-06` obowiązuje dla `F = Q, R, C` (w kontekście kompleksu wolnych grup). Poprzedzający przykład torusa używa tych współczynników, więc cytowanie jest adekwatne. Porównanie z `Z/2` poniżej **nie** wynika z tej formuły — tekst słusznie oblicza je osobno. | Preferować `DG-06`, **propozycja lokalna z ważnym ograniczeniem zakresu**. |
| 38 | `DG-08:2218` | `thm:euler-homologia` | `DG-06:1917`, `TOP-03:1633` | Twierdzenie w `DG-06` zakłada skończoną liczbę niezerowych skończenie wymiarowych przestrzeni nad ciałem. Dla skończonego CW autor przechodzi do kompleksu komórkowego nad `Q`, co spełnia hipotezy i daje równość naprzemiennych sum liczb komórek i liczb Bettiego. | Preferować `DG-06`, **propozycja lokalna**. |
| 39 | `DG-08:2229` | `thm:homologia-char-zero` | `DG-06:1795`, `TOP-03:1512` | Izomorfizm po przejściu do `Q` jest dokładnie tezą `DG-06`. Ranga skończenie generowanej grupy homologii odpowiada wymiarowi nad `Q`; dla skończonego CW grupy łańcuchów są skończenie generowane i wolne, więc ten krok jest uzasadniony. | Preferować `DG-06`, **propozycja lokalna**. |

## Wynik i ograniczenia

- **13 nowych wystąpień** z pełnego raportu (27–39); wszystkie 13 są **niejednoznaczne**, żadne nie jest brakujące w tej partii.
- Dla wszystkich 13 istnieje **matematycznie uzasadniona propozycja lokalnego właściciela**; w 2 przypadkach (`DG-08:1256`, `DG-08:1462`) pozostała osobna kontrola wszystkich hipotez lematu pięciu. Zakres wzoru zmiany współczynników został wyraźnie ograniczony do `Q`, `R`, `C`.
- Przejrzano łącznie **39 z 257** nierozwiązanych wystąpień według migawki; **218** pozostaje do audytu. Te liczby oznaczają *audyt*, a nie liczbę naprawionych etykiet.
- **Nie zmieniono żadnego pliku `chapters/pl/`**, nie scalano skryptów, nie przemianowywano `\label` ani `\ref`, nie usuwano wariantów twierdzeń. Nie przeprowadzano kompilacji LaTeX dla tej partii.
- Kolejny audyt: **wystąpienia 40–52**. Po uzasadnieniu konkretnych celów należy przygotować jawne rozwiązania kolizji kompatybilne z zachowaniem nazw etykiet, np. kontekstowy wybór właściciela w aplikacji i w projekcie kompilacyjnym, nie cichą zmianę identyfikatora w kopiowanym materiale.

## Długoterminowa kolejność

Najpierw kompletujemy niezależne działy od podstaw matematyki ku kolejnym gałęziom. Dopiero po skompletowaniu rozpocznie się scalanie z zachowaniem wszystkich nietożsamych dowodów i pełnej mapy pochodzenia. Obecny audyt dotyczy jedynie poprawności powiązań.