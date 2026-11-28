# Atlas matematyczny — graf zadeklarowanych zależności Lean (22.11.2026)

## Zakres

Strumień A, wyłącznie `application/backend/`, `application/frontend/`, `application/tests/` i dokumentacja. Nie zmieniono kanonicznych plików `.tex`, `application/lean/manifest.json` ani źródeł `application/lean/src/`.

## Funkcjonalność

- `GET /api/lean/dependencies?formalization_id=...` tworzy odczytowy graf tylko dla identyfikatora z rejestru. Nie przyjmuje ścieżki pliku, kodu Lean ani komend procesu z klienta.
- Węzły: wskazane źródło LaTeX, deklaracje z `lean_theorems` w manifeście, fizyczny plik `.lean` oraz moduły wymienione w jawnych poleceniach `import`.
- Typy krawędzi: `manifest_correspondence` (deklarowane przez rejestr mapowanie LaTeX → nazwa Lean), `manifest_file` (deklarowana lokalizacja nazwy w pliku) i `declared_import` (syntaktyczny `import` modułu na poziomie pliku). Żadna z tych krawędzi nie jest dowodem, że konkretny lemat używa konkretnej definicji Mathlib.
- Odczyt statusów `ready/draft/stale` i `approved/needs_review` korzysta z istniejącego `lean_catalog`: indeks SQLite, jego SHA256, etykieta w konkretnym module, przypięty SHA i aktualne źródło na dysku. Graf nie zwraca `proof_status`, zawsze `certificate=false`.
- Parser usuwa zagnieżdżone komentarze Lean `/- ... -/`, komentarze wierszowe `--` i zawartość napisów, a następnie rozpoznaje wyłącznie jawne, pełne polecenia `import`. Limit 80 unikatowych importów i 60 000 bajtów na plik; odrzucenie składni importu spoza obsługiwanego podzbioru.
- Panel pod kodem Lean ma cztery warstwy diagramu: źródło, deklaracje, plik, importy. Kliknięcie jednoznacznego źródła otwiera je w Czytniku. Wszystkie teksty są wstawiane za pomocą `textContent`, a zmiana zaznaczenia unieważnia oczekujące odpowiedzi.

## Testy

- `test_lean_dependencies.py`: pełna struktura grafu, ignorowanie importów wewnątrz zagnieżdżonych komentarzy i napisów, stan `stale`, odmowa nieznanych identyfikatorów, ograniczenia rozmiaru i liczby importów.
- `test_lean_http.py`: rzeczywisty `GET /api/lean/dependencies` dla `lst01-de-morgan`, import `Mathlib`, dwie deklaracje i brak fikcyjnego certyfikatu.
- `test_lean_dependency_browser.py`: wykonywany przez Node test bezpieczeństwa tekstu, nawigacji do źródła, nieaktywnych niejednoznacznych źródeł i asynchronicznych odpowiedzi poprzedniego zaznaczenia.
- `test_lean_formalization.py`: obecność wszystkich elementów panelu i wywołania API.

**Stan CI:** potwierdzać dopiero po rzeczywistym zakończeniu workflow; zapis commitu sam w sobie nie oznacza przejścia testów.

## Granice wiarygodności

Ten graf **nie przedstawia** przechodniego drzewa importów, zależności deklaracji Lean od konkretnych lematów, grafu wyprowadzonego z elaboratora, `#print axioms`, kompletnej semantyki źródłowego LaTeX ani stanu kompilacji. Przypisanie deklaracji do pliku jest danymi manifestu, a nie zweryfikowaną analizą parsera Lean. Następny etap powinien korzystać z eksportu z rzeczywiście uruchomionego Lean / Mathlib i osobnego audytu semantycznego.
