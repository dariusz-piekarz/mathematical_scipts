# Geometria algebraiczna — audyt globalny III (2026-11-22)

## Podstawa kontroli i sprostowanie terminologiczne

Niezależny reaudyt tekstu po globalnym II, bez zmian źródeł kanonicznych ALG-00–ALG-10. Migawka gałęzi użyta do kontroli: `2987e47918ea51537ec938f909b9430455624f22`. Rozdział ALG-04: blob `ab1344ed93a02bb757e5a78cb3833d6c4a18079c`; ALG-10: blob `5b231c9b40ad7f547ccfb3050e3712b7be7a75b0`; monolit: `6c5ae2c7d971b0c4574e6bd5c6cf3b86b5f28880`.

**Ważne sprostowanie audytu II:** „dywizor” jest prawidłową polską nazwą obiektu *divisor*. W tekście ALG-03/04 nazwy „dywizor Weila”, „dywizor funkcji”, „dywizor główny”, „snop dywizora” i „grupa dywizorów” są poprawne. „Dzielnik” również bywa używany w tym znaczeniu. Różnica tych dwóch dopuszczalnych nazw nie jest usterką matematyczną, a wymuszona migracja ALG-03/04 do „dzielnika” nie jest potrzebna. Nie zmieniano nazw, etykiet, testów ani monolitu. W dalszej redakcji obu form nie należy mechanicznie podmieniać; w szczególności nie dotyczy to „dzielnika zera” w teorii pierścieni.

## Osobny przegląd uzasadnień

1. **ALG-04: dywizory i grupa Picarda.** Reread definicji i dowodów w wierszach ok. 1601–1892. Przyjęcie `k` algebraicznie domkniętego i `C` gładkiej, nierozkładalnej krzywej rzutowej jest jawne na początku części (około 1603), więc definicje poniżej mają określoną dziedzinę. Przejścia `D' = D + div(h)` i `L(D')=h^{-1}L(D)` mają prawidłowy znak; dla snopa `O_C(D)` nad zbiorem pustym przyjęto jedno zero, co pozwala spełnić aksjomat snopa. Konstrukcja `Div(C)/Prin(C) ≅ Pic(C)` wykorzystuje wymierną sekcję i lokalne generatory z właściwym znakiem rzędu.
2. **ALG-07: Riemann–Roch dla powierzchni.** Ponownie rozdzielono krok adjunkcji `2g(C)-2=C²+K_S·C`, ciąg dokładny `0→O(D)→O(D+C)→O_C(D+C)→0`, przyrost charakterystyki `D·C+(C²−K_S·C)/2` i przejście od krzywych gładkich do dowolnego dywizora przez Bertiniego oraz dodanie dostatecznie dużej wielokrotności dzielnika bardzo obszernego. Wynik HRR nie jest tu podmieniany na ukryty element dowodu.
3. **ALG-08 i ALG-10: forma przecięć.** Zbadano odrębnie klasy trzech transformowanych prostych po rozdmuchaniu trzech punktów, rozróżnienie klas nef i obszernych w indeksie Hodge'a, a także warunek równości w nierówności kwadratowej.
4. **ALG-09 i ALG-10: geometria analityczna a algebraiczna.** Zweryfikowano hipotezy projektowości w zastosowaniu twierdzenia Chowa do grafów, wymóg właściwości w GAGA oraz poprawne oddzielenie kohomologii snopów od kohomologii singularnej. W twierdzeniu Lefschetza o klasach (1,1) warunek całkowitości jest jawny; wyższe przypadki hipotezy Hodge'a nie zostały nazwane dowiedzionymi.

## Niezależne rachunki regresyjne (dokładne liczby całkowite)

- **500** stopni hiperpowierzchni `d=1,…,500`: `12(1+p_g)=K_S²+χ_top` i nieujemność `h^{1,1}=χ_top−2−2p_g` dla właściwych wzorów na `p_g`; wszystkie spełnione.
- **14 641** par `(a,b)∈[-60,60]²`: `χ(P¹×P¹,O(a,b))=(a+1)(b+1)` sprawdzone również przez iloczyn różnic `h⁰−h¹`; brak rozbieżności.
- **14 641** par `(a,b)∈[-60,60]²`: dla `A=2H−E` na `Bl_pP²`, `D=aH+bE`, sprawdzono tożsamość `(D·A)²−D²A²=(a+2b)²`; brak rozbieżności.
- **15** par różnych krzywych z sześciokąta Cremony: klasy `E_i` i `H−E_i−E_j` mają samoprzecięcie `−1`; przecięcia różnych par wynoszą `0` albo `1` zgodnie z grafem.

## Integracja i PDF

Ponownie pobrano 11 rozdziałów i monolit; **11/11** bloków są identyczne znakowo. Z trzema współdzielonymi modułami uzyskano **406 unikalnych etykiet, 167/167 rozwiązanych odsyłaczy, zero duplikatów**. Ponowny niezależny odczyt rzeczywistych PDF i logów z ostatniego workflow obejmującego aktualne bloby: **184 strony** w książce modułowej i monolicie; **184/184** stron identyczne tekstowo i obrazowo w renderingu porównawczym, **0** bloków poza granicami stron, **0** ostrzeżeń końcowych logów (brak przepełnień, błędów i niezdefiniowanych referencji). Przejrzano reprezentatywne plansze rysunkowe ALG-04, ALG-06, ALG-08, a wcześniejszy odbiór tego samego źródła obejmował cztery rysunki ALG-10. Nie przypisujemy regresjom mocy dowodzenia twierdzeń zewnętrznych.

Odniesienie: [CI 45069448058](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069448058), zakończony SUCCESS na aktualnych źródłach rozdziałowych.

## Wynik

**GLOBALNY III: PASS — w badanych węzłach matematycznych, terminologii po sprostowaniu, integralności źródeł i PDF nie znaleziono nowej jednoznacznej usterki.** Błąd klasyfikacji „dywizora” w raporcie II cofnięto jako blokadę, zachowując historyczny zapis audytu. Źródła ALG-00–10 i monolit niezmienione. Wymagany jeszcze osobny audyt globalny IV na tym samym stanie dla pewności.
