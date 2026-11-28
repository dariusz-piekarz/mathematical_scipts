# Globalna konwencja terminologiczna: „presnop” — 22 listopada 2026

## Polecenie i zakres

Po zakończeniu niezależnego audytu IV ALG-04 i uzyskaniu statusu
**STABILNY / ZAMKNIĘTY** zastosowano globalną polską regułę:
obiekt *presheaf* nazywamy **presnopem**, w liczbie mnogiej
**presnopy**. Obowiązują wszystkie poprawne odmiany
(presnopu, presnopem, presnopie, presnopów, presnopami).
Termin **snop** zachowuje swoje odrębne znaczenie,
tj. presnop spełniający aksjomaty snopa.

## Rzeczywiste zmiany

Jednorazowa migracja na gałęzi
`biblioteka-matematyczna-iteracja-6`:
[commit 37cda4dd](https://github.com/dariusz-piekarz/mathematical_scipts/commit/37cda4dda1065c95eac543c3cdeda1546e175701).

Przejrzano aktywne pliki źródłowe `.tex`, `.md`, `.txt`,
`.html` w repozytorium; historyczne raporty
z katalogu `audits/` świadomie pozostawiono jako
zapis ich pierwotnego stanu.

**4 zmienione pliki, 32 poprawione wystąpienia:**

| Plik | Wystąpienia |
| --- | ---: |
| `chapters/pl/algebraic_geometry/04-algebra-przemienna-snopy-i-krzywe-algebraiczne.tex` | 11 |
| `chapters/pl/algebraic_topology/23-kohomologia-snopow-z-nosnikami-i-podstawy-dualnosci-verdiera.tex` | 5 |
| `sources/pl/geometria_algebraiczna(1).tex` | 11 |
| `sources/pl/topologia_algebraiczna(2).tex` | 5 |
| **Łącznie** | **32** |

Powyższy wynik potwierdza
[workflow 45022322170](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022322170):
w logu zgłoszono `Files: 4; obsolete terminology occurrences: 32`,
a bezpośrednio po poprawkach:
`Files: 0; obsolete terminology occurrences: 0`.
Przebieg **completed/success**.

W zweryfikowanym diffie zmieniają się wyłącznie słowa w
prozie, tytułach i opisach przykładów. **Nie zmieniono
wzorów, etykiet `\label`, odsyłaczy `\ref` ani nazw plików.**
Teksty źródłowe scalonych wersji zachowano.

## Reguła trwała i egzekwowanie

- Narzędzie `tools/normalize_polish_terminology.py`:
  `--fix` stosuje normalizację do całego aktywnego
  korpusu; `--check` odrzuca niedozwolony wariant.
  Commit [86d8bacd](https://github.com/dariusz-piekarz/mathematical_scipts/commit/86d8bacd9049ab81ddc54862170a53c4368b2feb).
- Istniejący `tools/check_terminology.py` obejmuje
  nową regułę przy kontrolach nowych i zmienianych
  plików LaTeX; commit
  [df3f4fd2](https://github.com/dariusz-piekarz/mathematical_scipts/commit/df3f4fd26dfce5c4a24b32021c3cd188a1801b7b).
- Uzupełniono oba dokumenty normatywne:
  `docs/pl/konwencje_terminologiczne.md` oraz
  `docs/pl/standardy_terminologiczne.md`.
- Rozszerzono `.github/workflows/mathematical-terminology.yml`:
  globalny `--check` jest wykonywany w każdym
  przebiegu, a obserwowane ścieżki obejmują
  polskie źródła rozdziałowe, zbiory źródłowe,
  dokumenty konwencji i kontrolery. Commity
  [e4cc69ca](https://github.com/dariusz-piekarz/mathematical_scipts/commit/e4cc69cae01bb3563a0f9719d04d38669629fa09)
  oraz [6495f6c6](https://github.com/dariusz-piekarz/mathematical_scipts/commit/6495f6c6b2679cfee171edf034ed701f347c02e5).
  Potwierdzono **SUCCESS** w przebiegach
  [45022532910](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022532910)
  i [45022671254](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022671254).

## Odbiór ALG-04 po migracji słownictwa

W dedykowanym workflow ALG-04 dodano pełny skan
terminologii przed uruchomieniem testów i kompilacji.
[GitHub Actions 45022536496](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022536496)
**completed / SUCCESS** na commicie
`db45c6c8277ad26209608b2af8c2593ca1e98e64`:
- globalny skan terminu PASS;
- **14/14 regresji PASS**;
- kompilacja ALG-00–04 i odsyłacze PASS;
- rzeczywisty artefakt GitHub Actions
  `14753929570` zawiera PDF i log.

Pobrany PDF ma 108 stron całego ALG-00–04;
sam rozdział ALG-04 liczy 43 strony (PDF strony 66–108).
Nie wykryto błędów lub ostrzeżeń LaTeX,
bloków tekstu poza stronami ani brakujących odsyłaczy.
Zlokalizowano wszystkie dziesięć rysunków ALG-04.
Wersję 43-stronicową wyodrębniono i zapisano do pobrania.

## Wpływ na stan rozdziałów

**ALG-04 pozostaje STABILNY / ZAMKNIĘTY po audycie IV.**
Późniejsza migracja ma wyłącznie charakter terminologiczny;
potwierdzono ją nowymi testami i rzeczywistą kompilacją.
ALG-00–03 nie zmieniono merytorycznie.
Kolejny audyt rozdziałowy: **ALG-05, audyt I**.
