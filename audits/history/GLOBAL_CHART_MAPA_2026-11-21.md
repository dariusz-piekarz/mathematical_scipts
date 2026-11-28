# Globalna terminologia — chart = mapa, mapping = odwzorowanie

**Data:** 21 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; **gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** wszystkie polskojęzyczne źródła TeX w repozytorium, bez automatycznego zastępowania innych znaczeń wyrazu „karta” oraz bez naruszania etykiet historycznych.

## Zasada obowiązkowa

- Angielskie **chart**, **coordinate chart** → polska **mapa**, „mapa współrzędnych”, „mapa lokalna”, „atlas map”, „zmiana map”; stosujemy poprawną odmianę.
- Angielskie **mapping**, **map** jako funkcja → **odwzorowanie**, nie „mapa” w tym sensie.
- Słowo „karta” pozostaje poprawne w innych znaczeniach, w szczególności dla **kart do gry**.
- Zasada obowiązuje we wszystkich polskich skryptach, nowych rozdziałach, dowodach, przykładach, podpisach i audytach. Nie zmieniamy `\\label`, `\\ref` ani znaczenia konstrukcji matematycznych.

Wpisy w repozytorium:
- [AGENTS.md](../../AGENTS.md).
- [docs/pl/standardy_terminologiczne.md](../../docs/pl/standardy_terminologiczne.md).

## Skan przed i po poprawkach

Automatyczny skan całej repozytoryjnej kolekcji plików `.tex` przed zmianami: **69** wystąpień odmian „karta” w **13** plikach. Przeanalizowano wszystkie konteksty. **31** wystąpień rzeczywiście oznaczało lokalną mapę współrzędnych; poprawiono je kontekstowo, z właściwą odmianą polską, w **10** plikach:

| Źródło | Zmiany |
|---|---:|
| TOP-11: przecięcia, dualność i klasy charakterystyczne | 1 |
| TOP-12: ciągi spektralne | 1 |
| TOP-18: homologia Morse'a | 5 |
| TOP-23: kohomologia snopów i dualność Verdiera | 1 |
| TOP-27: sześć operacji snopowych | 1 |
| TOP-28: zespolone odmiany projektowe | 3 |
| TOP-29: homotopia, granice odwrotne i przeszkody | 2 |
| TOP-30: przypomnienie geometrii różniczkowej | 2 |
| `shared/pl/rozdmuchanie_punktu_normalna.tex` | 4 |
| `sources/pl/topologia_algebraiczna(2).tex` — historyczne pełne źródło | 11 |
| **Razem** | **31** |

**38** wystąpień dotyczyło rzeczywistych kart do gry: `chapters/pl/probability_volume_i/01-...` (17), `04-...` (2) oraz `sources/pl/rachunek_prawdopodobienstwa_tom_I.tex` (19). Zostawiono je bez zmian.

Skan po poprawkach: **38** wystąpień w **3** plikach; wszystkie 38 to zweryfikowane przykłady kart do gry. **Zero niezaakceptowanych użyć**, czyli **zero znanych błędnych wystąpień w znaczeniu „chart”**. Skany uwzględniają kod i komentarze TeX, a przy analizie ignorują zawartość stabilnych identyfikatorów `\\label`/`\\ref`.

## Zabezpieczenia regresyjne i GitHub Actions

- `application/scripts/audit_chart_terminology.py`: skan wszystkich źródeł TeX, raport JSON, tryb `--strict` odrzucający niezaakceptowane wystąpienia.
- `.github/workflows/mathematical-library-app.yml`: **obowiązkowy** test `--strict` przed testami aplikacji; do artefaktu `reference-provenance-audit` dołączono `chart_terminology.json`.
- `application/tests/test_chart_terminology.py`: sprawdzenie wszystkich źródeł, dopuszczenie wyłącznie zweryfikowanych kontekstów kart do gry oraz test sztucznego naruszenia reguły.
- `application/tests/test_topology_chapters_17_18.py`: poprawiono wcześniejszą, zbyt ogólną regresję, która błędnie zabraniała każdego wystąpienia „mapa”; obecnie wymaga poprawnego użycia „w mapie” dla rzeczywistych map współrzędnych i odrzuca stare „w karcie”.

### Zweryfikowane przebiegi

- [TOP-11/12 — LaTeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939523105): **success**.
- [TOP-17/18 — LaTeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939529752): **success**.
- [TOP-23/24 — LaTeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939535484): **success**.
- [TOP-27/28 — LaTeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939574903): **success**.
- [TOP-29/30 — LaTeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939574059): **success**.
- [AT–DG–AG — kontrola międzytomowa](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939574034): **success**.
- [Końcowy CI aplikacji, regresji, skanu terminologii i testów przeglądarkowych](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939838333): **completed / success**.

Wczesne przebiegi kontroli aplikacji po pierwszych poprawkach były czerwone, ponieważ istniał dawny test TOP-18 zakazujący „mapa” także w prawidłowym znaczeniu *chart*. Naprawiono go; końcowy przebieg CI jest zielony.

**Wynik:** zasadę zapisano globalnie w dokumentacji projektu; skorygowano wszystkie wykryte niepoprawne wystąpienia w matematycznych źródłach TeX; dodano strażnika terminologicznego do CI. Nie dodano nowych wyników matematycznych; nie zmieniono stabilnych etykiet i odsyłaczy. W przyszłości obowiązuje `chart=mapa`, `mapping=odwzorowanie`.