# Rejestr etykiet i aliasów — implementacja kontekstowa

**Data:** 20.11.2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Zakres:** aplikacja, parser, indeks SQLite, API, podgląd odsyłaczy i testy. Kanoniczne `.tex` są nietknięte.

## Model

Rozróżniamy trzy poziomy:

1. **Oryginalna nazwa etykiety**: np. `thm:homotopia-homologia`, taka jak w źródłowym `\\label`.
2. **Unikalne wystąpienie**: `TOP-03::thm:homotopia-homologia` lub `DG-06::thm:homotopia-homologia`. Rozdziały źródłowe i identyfikatory wystąpień nie są aliasami.
3. **Tożsamość matematyczna**: pole `concept_id` jest zarezerwowane w `label_occurrences`; pozostaje `NULL`, dopóki równoważności nie potwierdzi audyt matematyczny. Identycznych nazw etykiet nie traktuje się automatycznie jako tego samego twierdzenia.

W SQLite tabela `label_occurrences` przechowuje **wszystkie oryginalne wystąpienia**, także przy kolizjach; dotychczasowe `labels` i `label_conflicts` pozostają dla zgodności dotychczasowego API. Schemat parsera ma wersję **3**. Indeks budujemy od nowa ze źródeł, nie modyfikujemy plików kanonicznych.

## Rozwiązywanie odsyłaczy

Resolver `backend/label_registry.py`:

1. Sprawdza jawny, zatwierdzony alias z podanym **rozdziałem cytującym**.
2. Dla `P1`–`P4` rozpoznaje prefiksy `I-`, `II-`, `III-`, `IV-` importów `xr-hyper` i sprawdza dokładnie źródłową etykietę odpowiedniego tomu; wynik: `external_resolved`. Sam parser nie kompiluje `.aux` ani PDF.
3. Preferuje deklarację w **tym samym rozdziale**.
4. Następnie jednoznaczną deklarację **w tym samym skrypcie** (`TOP`, `DG`, `P1` itd.).
5. Dla zachowania starszych zależności dopuszcza tylko **jednoznaczny, globalnie unikatowy** cel, gdy nie ma dopasowania w skrypcie. To nie jest dowód semantycznej zależności między skryptami; przyszły jawny rejestr zależności może zaostrzyć tę regułę.
6. Przy wielu właścicielach nadal zwraca `ambiguous`, bez losowego wyboru. Gdy nie ma celu, zwraca `missing`.

Indeks odróżnia `resolved`, `external_resolved`, `alias_resolved`, `ambiguous`, `missing`. Graf zależności i raport pochodzenia traktują zweryfikowane odsyłacze zewnętrzne i aliasy jako rozstrzygnięte.

## Jawne aliasy

Istniejąca opcja `--aliases` parsera może zawierać dodatkową tablicę `label_aliases`:

```json
{
  "label_aliases": [
    {
      "source_document": "TOP-05",
      "original_label": "thm:stare-oznaczenie",
      "target_document": "TOP-03",
      "target_label": "thm:homotopia-homologia"
    }
  ]
}
```

Alias stosujemy wyłącznie po **ręcznym audycie** i dopiero gdy wskazany cel istnieje. Nie jest to automatyczne scalanie twierdzeń. Oryginalne `\\ref{thm:stare-oznaczenie}` pozostaje w LaTeX-u. Starsze sekcje plików aliasów (`rewritten_xr_prefixes`, `renamed_collisions`, `lost_labels_restored`) zachowują dotychczasowe znaczenie historyczne; nie stają się automatycznie nowymi aliasami kanonicznymi.

## API i UI

`GET /api/labels/{label}?source_document=TOP-05` wykorzystuje rzeczywiście rozstrzygnięte odsyłacze z indeksu. W odpowiedzi pojawia się `occurrence_id`, `canonical_label`, `source_document` i `resolution_status`. Bez kontekstu stare API nadal pokazuje wybór przy kolizji.

Podgląd i kliknięcie `\\ref` w czytniku przekazują bieżący identyfikator rozdziału; kiedy właściciel jest znany, otwierają **właściwe źródłowe wystąpienie**, zamiast pokazywać zbędny wybór dwóch skryptów.

## Testy, ograniczenia, kolejny etap

- `tests/test_label_registry.py`: skryptowa własność etykiet, prefiksy `xr-hyper`, ręczne aliasy, nierozstrzygnięte kolizje, integralność bazy.
- `tests/test_api.py`: API i przejście z kontekstem `TOP` oraz tomów prawdopodobieństwa.
- Testy CI uruchamiają indeksowanie i regresję oraz browser smoke; wynik konkretnego commitu należy zawsze weryfikować osobno.
- Nie wykonano kompilacji czterech tomów z prawdziwymi `.aux` ani pełnego dowodu poprawności matematycznej wszystkich źródeł.
- Nie wdrożono fizycznej deduplikacji treści, globalnej zmiany wszystkich nazw ani automatycznej identyfikacji `concept_id`.
- Pełna geometria różniczkowa ma 36 rozdziałów, ale obecnie zaimportowano tylko 20; po dołożeniu pozostałych trzeba ponownie zbudować i skontrolować indeks.

**Nie zmieniono:** oryginalnych `\\label`, `\\ref`, `\\eqref`, `chapters/pl/`, `main`; brak scalania skryptów.
