# Audyt odsyłaczy — partia XIX (235–247)

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło numeracji:** statyczny `reference_provenance_audit_355.json`, 355 rozdziałów, 257 zgłoszonych wystąpień.

## Podsumowanie

Ręcznie zweryfikowano **13 wystąpień** z rozdziału `TOP-09` („Formy różniczkowe, orientacja i kohomologia de Rhama”). Każde ma status `ambiguous`: równoległe deklaracje występują w skrypcie topologii algebraicznej (`TOP`) i w zaimportowanej części geometrii różniczkowej (`DG`). Na podstawie źródłowego kontekstu, cytowanego twierdzenia/definicji i oryginalnego ciągu dydaktycznego **we wszystkich 13 przypadkach właścicielem jest rozdział należący do `TOP`**.

## Sprawdzone wystąpienia

| Lp. | Cytowanie | Oryginalna etykieta | Prawidłowy właściciel | Drugi kandydat (nie wybierać) |
|---:|---|---|---|---|
| 235 | `TOP-09:10` | `ch:homologia-przestrzeni` | `TOP-05:2` | `DG-08` |
| 236 | `TOP-09:1275` | `thm:les-kohomologia` | `TOP-03:646` | `DG-06` |
| 237 | `TOP-09:1276` | `ch:algebra-homologiczna` | `TOP-03:2` | `DG-06` |
| 238 | `TOP-09:1379` | `prz:homologia-cw-torus` | `TOP-05:1448` | `DG-08` |
| 239 | `TOP-09:1390` | `ch:homologia-przestrzeni` | `TOP-05:2` | `DG-08` |
| 240 | `TOP-09:1502` | `thm:homotopia-singularna` | `TOP-05:354` | `DG-08` |
| 241 | `TOP-09:1610` | `lem:male-lancuchy` | `TOP-05:507` | `DG-08` |
| 242 | `TOP-09:1860` | `thm:symplicjalna-singularna` | `TOP-05:1033` | `DG-08` |
| 243 | `TOP-09:1968` | `thm:homologia-char-zero` | `TOP-03:1512` | `DG-06` |
| 244 | `TOP-09:1971` | `prz:zmiana-wspolczynnikow-rp2-torus` | `TOP-05:1529` | `DG-08` |
| 245 | `TOP-09:1994` | `ch:wyzsza-homotopia` | `TOP-06:2` | `DG-09` |
| 246 | `TOP-09:1996` | `thm:hurewicz-h1` | `TOP-06:734` | `DG-09` |
| 247 | `TOP-09:2006` | `thm:hurewicz-wyzszy` | `TOP-06:1491` | `DG-09` |

Bilans: {'TOP-05': 7, 'TOP-03': 3, 'TOP-06': 3}.

## Weryfikacja semantyczna i matematyczna

- `TOP-09:10,1390`: rozdział `TOP-05` buduje homologię singularną, wykorzystywaną następnie w porównaniu de Rhama z kohomologią singularną.
- `TOP-09:1275–1276`: `TOP-03:646` daje długi ciąg kohomologii z krótkiego ciągu kompleksów kołańcuchowych; poprzedni argument konstruuje odpowiedni krótki ciąg za pomocą podziału jedności. Warto utrzymać jawne oznaczenie odpowiednich odwzorowań i znaków przy odwzorowaniu łączącym.
- `TOP-09:1379`: model komórkowy torusa w `TOP-05:1448` zgadza się z wymiarami kohomologii de Rhama, wyliczonymi przez formy.
- `TOP-09:1502`: niezmienniczość homotopijna homologii singularnej w `TOP-05:354` jest odpowiednią podstawą do porównania kompleksów na wypukłych zbiorach. **Dalszy audyt matematyczny** powinien osobno doprecyzować, że argument przechodzi również na gładkie sympleksy.
- `TOP-09:1610`: lemat małych łańcuchów `TOP-05:507` służy do lokalnego porównania homologii. Tekst explicite omawia adaptację do gładkich sympleksów i dualizację nad ciałem; to nie jest dowód wynikający automatycznie z samego faktu dla wszystkich ciągłych sympleksów.
- `TOP-09:1860`: twierdzenie `TOP-05:1033` jest sformułowane dla skończonego kompleksu symplicjalnego/Δ-kompleksu. Tekst `TOP-09` proponuje przejście do lokalnie skończonych triangulacji przez skończone podkompleksy i zwartość nośników. Przejście to należy uzasadniać osobno; nie można automatycznie powoływać się wyłącznie na wersję skończoną.
- `TOP-09:1968–1971`: `TOP-03:1512` i przykład `TOP-05:1529` prawidłowo tłumaczą zanik torsji przy przejściu z liczb całkowitych do ciała charakterystyki zero.
- `TOP-09:1994,1996,2006`: `TOP-06` zawiera definicję i oba twierdzenia Hurewicza. W `TOP-09` jawnie zastrzeżono warunki łukowej spójności i `(k−1)`-spójności. Przejście do wersji dla rozmaitości odbywa się przez dodatkowy fakt triangulowalności, który tekst oznacza jako odrębny wynik, niewyprowadzany z twierdzenia de Rhama.

## Ochrona integralności

**Nie zmieniano** oryginalnych `\label`, `\ref`, `\eqref`, zawartości `chapters/pl/` ani gałęzi `main`. Kandydaci z `DG` pozostają w indeksie; aktualna decyzja o właścicielu jest zapisana w audycie, bez fizycznej zmiany indeksu. Dalsze 16 rozdziałów geometrii różniczkowej spośród pełnych 36 nie zostało jeszcze zaimportowanych.

## Dalsze kroki

- Dokończyć statyczny audyt w **ostatniej partii 248–257 (10 wystąpień)**.
- Osobno zaimplementować w aplikacji rozwiązywanie odsyłaczy względem skryptu i klasyfikację międzytomowych `external_resolved`, zachowując oryginalne nazwy.
- Zweryfikować rzeczywistą kompilację `xr-hyper` z plikami `.aux` w oddzielnym zadaniu.

**Postęp: 247/257 wystąpień zweryfikowanych, 10 pozostałych.** Audyt nie oznacza jeszcze naprawy indeksu.