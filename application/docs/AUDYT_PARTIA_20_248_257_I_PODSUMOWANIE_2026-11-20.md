# Audyt integralności odsyłaczy — partia XX (248–257), zamknięcie migawki 355 rozdziałów

**Data:** 20 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`.  
**Podstawa enumeracji:** `reference_provenance_audit_355.json`: 355 rozdziałów, 257 nierozstrzygniętych wystąpień w indeksie wejściowym.

## Wynik końcowej partii

Wszystkie **10/10** wystąpień mają w indeksie status `ambiguous`. Dla każdego zweryfikowano źródłowy akapit, oryginalny cel w skrypcie topologii algebraicznej i równoległą deklarację w skrypcie geometrii różniczkowej. Semantycznie właściwy właściciel należy w każdym przypadku do `TOP`. Wystąpienia nie są nowymi brakami materiału; indeks nadal wymaga wdrożenia rozstrzygnięć.

| Nr | Lokalizacja cytowania | Oryginalna etykieta | Właściwy właściciel | Równoległy właściciel (bez zmiany) |
|---:|---|---|---|---|
| 248 | `TOP-09:2044` | `prz:pi1-torus-rp2` | `TOP-04:1493` | `DG-07:2269` |
| 249 | `TOP-09:2067` | `prz:rp2-pi2` | `TOP-06:1901` | `DG-09:2344` |
| 250 | `TOP-09:2068` | `prz:homologia-rp2` | `TOP-05:1476` | `DG-08:2060` |
| 251 | `TOP-11:28` | `ch:algebra-homologiczna` | `TOP-03:2` | `DG-06:2` |
| 252 | `TOP-11:29` | `ch:homologia-przestrzeni` | `TOP-05:2` | `DG-08:2` |
| 253 | `TOP-11:59` | `ch:algebra-homologiczna` | `TOP-03:2` | `DG-06:2` |
| 254 | `TOP-11:192` | `ch:formy-de-rham` | `TOP-09:2` | `DG-10:2` |
| 255 | `TOP-11:223` | `prop:lokalna-homologia` | `TOP-05:1597` | `DG-08:2255` |
| 256 | `TOP-11:319` | `ch:homologia-przestrzeni` | `TOP-05:2` | `DG-08:2` |
| 257 | `TOP-21:8` | `sec:poincare-hopf-16` | `TOP-11:2155` | `DG-17:2197` |

## Uzasadnienie poszczególnych grup

**248–250: TOP-09, porównanie homologii, homotopii i de Rhama.**
- `TOP-09:2044`: `TOP-04:1493` oblicza grupę podstawową torusa i podaje model CW z komórką dołączoną słowem komutatora; jest dokładnie modelem używanym przy wycięciu dysku i retrakcji do bukietu okręgów.
- `TOP-09:2067`: `TOP-06:1901` oblicza \(\pi_2(\mathbb{RP}^2)\cong\mathbb Z\) przez nakrycie \(S^2\to\mathbb{RP}^2\).
- `TOP-09:2068`: `TOP-05:1476` oblicza \(H_2(\mathbb{RP}^2;\mathbb Z)=0\) i torsję w \(H_1\). Kontrast z poprzednim wynikiem jest zamierzony: brak jednospójności sprawia, że \(h_2\) nie jest izomorfizmem. Ponadto \(\mathbb{RP}^2\) ma zerowe kohomologie de Rhama w dodatnich stopniach.

**251–256: TOP-11, iloczyny kubkowe, lokalna homologia i orientacja.**
- `TOP-11:28` i `:59`: właściciel `TOP-03:2` — kompleksy łańcuchowe, kołańcuchy i składnik \(\operatorname{Ext}\) przy całkowitych współczynnikach.
- `TOP-11:29` i `:319`: właściciel `TOP-05:2` — homologia przestrzeni, w tym zgodność homologii symplicjalnej i singularnej, użyta przy klasie fundamentalnej.
- `TOP-11:192`: `TOP-09:2` wprowadza iloczyn zewnętrzny form, który porównano z kubkowym.
- `TOP-11:223`: `TOP-05:1597` podaje lokalną homologię \(\mathbb Z\) w stopniu wymiaru **dla rozmaitości bez brzegu**. W tekście `TOP-11` klasa fundamentalna dla rozmaitości zamkniętych jest odpowiednim zastosowaniem. W wersji dla rozmaitości z brzegiem wymagana jest osobna kontrola punktów brzegowych i grup względnych — nie należy przenosić bezpośrednio tego stwierdzenia na brzeg.

**257: TOP-21, twierdzenie Poincarégo–Hopfa.**
- `TOP-21:8` wprost wskazuje wcześniejszy dowód dla zamkniętych zorientowanych rozmaitości; dokładnie ten materiał jest w `TOP-11:2155`, a nie w równoległej sekcji `DG-17:2197`. Rozdział TOP-21 rozszerza teorię na przypadek z brzegiem i nie powinien powielać definicji i dowodu z TOP-11. Równoległy materiał w geometrii różniczkowej zachować do planowanego późniejszego scalania.

## Zamknięcie pierwotnej listy

Wszystkie **257/257** wystąpień z zamrożonej migawki zostały przejrzane w 20 partiach. Surowy stan źródła:
- **166** wystąpień `ambiguous`;
- **91** wystąpień `missing`;
- ponadto **4228** wystąpień `resolved` bez konieczności indywidualnego audytu na tej liście;
- **305** nazw etykiet występujących u wielu właścicieli w całej migawce (globalny problem deduplikacji).

**To jest zakończenie audytu pochodzenia w statycznej migawce, nie usunięcie 257 problemów z działającej aplikacji.** W trakcie audytu rozróżniono m.in. prawidłowe odsyłacze importowane przez `xr-hyper`, kolizje możliwe do rozstrzygnięcia przez właściciela skryptu i cele faktycznie nieobecne w obecnym podzbiorze źródeł. Nie należy automatycznie nazywać wszystkiego „naprawione”. Wcześniejsze raporty zawierają też odrębne uwagi i luki matematyczne.

## Zakres i ograniczenia

- Obecny indeks obejmuje 355 rozdziałów; pełny skrypt „Geometria różniczkowa” zawiera **36 rozdziałów**, ale tylko **20** zaimportowano na gałąź, ponieważ pozostałe są jeszcze audytowane. Nie można z braku etykiety w obecnej migawce wywnioskować nieistnienia tematu w pełnym skrypcie.
- Należy zbudować **nowy indeks po przyszłych importach**, aby wykryć nowe bądź zdezaktualizowane cele, a nie traktować starej liczby 257 jako wiecznie aktualnej.
- Nie wykonywano pełnej kompilacji czterech tomów z rzeczywistymi plikami `.aux` w tej partii.

## Zalecana kolejność kolejnych prac

1. W parserze rozwiązywać etykiety **w obrębie skryptu źródłowego**, a dopiero potem w udokumentowanych zależnościach; zachować wszystkie konkurencyjne deklaracje i wskaźnik pochodzenia.
2. Rozpoznać `I-`, `II-`, `III-`, `IV-` jako przestrzenie prefiksów `xr-hyper` tylko dla odpowiedniego tomu. Używać statusu `external_resolved` dla rzeczywiście potwierdzonych zewnętrznych celów; niezależnie walidować brakujące `.aux`.
3. Oddzielnie śledzić prawdziwe braki celów i pozorne braki wynikające z **niepełnego importu 36-rozdziałowej geometrii różniczkowej**.
4. Wykonać test regresyjny parsera i aplikacji na wszystkich 257 wystąpieniach ze statycznej migawki, porównując wyniki z 20 raportami.
5. Wykonać kompilację międzytomową i testy rzeczywistych odsyłaczy w PDF; weryfikacja kompilacji nie wynika z samego sukcesu testów aplikacji.
6. Zachować dodatkowe zadania matematyczne odnotowane w raportach (m.in. ciągłość retrakcji, poprawność założeń i granicę wersji skończonych twierdzeń o CW).
7. Dopiero po skompletowaniu i zrewidowaniu planowanych działów przejść do deduplikacji i scalania treści, z zachowaniem sumy całej unikatowej treści i wszystkich oryginalnych etykiet oraz wariantów dowodów.

**Bez zmian:** `chapters/pl/`, oryginalne `\label`, `\ref`, `\eqref`, gałąź `main`; nie scalono skryptów.

**Następny etap:** wdrożenie rozstrzygnięć w indeksie aplikacji i testy regresyjne, nie kolejna partia starej migawki.