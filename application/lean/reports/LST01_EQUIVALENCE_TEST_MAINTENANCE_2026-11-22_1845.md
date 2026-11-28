# LST-01 — thm:equiv-test — kontrola utrzymaniowa 2026-11-22 18:45 CET

## Zakres i pochodzenie
- Etap: 2, ten sam obiekt `LST-01:thm:equiv-test`; bez przechodzenia do kolejnego twierdzenia.
- HEAD przed zapisem: `a28b076a2e3e11d00279d0faa9fd48a0948f25a2`.
- Odczytano na tej gałęzi: `AGENTS.md`, `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `application/lean/manifest.json`, `application/lean/src/LST01_SyntaxValuations.lean` oraz `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`.
- Etykieta kanoniczna: `thm:equiv-test`. SHA256 dokumentu zapisane w manifeście: `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`. W tej iteracji nie przeliczono niezależnie SHA bajtów źródła: integralność hasha pozostaje niepotwierdzona.

## Kontrola semantyczna
Źródło mówi, że dwie dowolne formuły zdaniowe są logicznie równoważne wtedy i tylko wtedy, gdy ich równoważność spójnikowa jest tautologią. Lean reprezentuje formuły jako `LST01.Formula`, wartościowania jako `Nat → Bool`, `equivalent p q := ∀ ν, eval ν p = eval ν q` oraz `tautology (.iff p q) := ∀ ν, eval ν (.iff p q) = true`. To rozróżnia metajęzykową relację równoważności od składniowego konstruktora `.iff`. Ten sam `ν` jest użyty dla obu formuł, również przy powtórzonych atomach. Nie wykryto zmiany kwantyfikatorów ani dodatkowych założeń.

Przeprowadzono rzeczywisty niezależny test Python wszystkich czterech par wartości logicznych: `(a == b) == ((not a or b) and (not b or a))`; wynik **4/4**. To tylko regresja tabeli prawdy, nie formalna kompilacja ani pełny test integracyjny.

## Stan weryfikacji i stabilizacji
- Lokalnie: `command -v lake` i `command -v lean` nie znalazły programów; `lake env lean` **not_run / toolchain_unavailable**. Wersja lokalna: niedostępna. Log kompilatora: brak.
- Nie pobrano w tej iteracji nowego surowego logu CI; historyczne sukcesy nie są nowym potwierdzeniem kernela.
- Kontrola tekstowa widocznej deklaracji: brak `sorry`/`admit`; `#print axioms lst01_syntax_equivalence_test` znajduje się w pliku, ale jego nowego wyniku nie uzyskano.
- Kontrole od ostatniej poprawki w tej iteracji: **1 ograniczona kontrola semantyczna**; dodatkowy pełny audyt końcowy: **niezaliczony**. Nie stwierdza się stabilności.
- Manifest: **5 etykiet / cel 20–30**, wszystkie z `statement_status=approved`; liczba nowo formalnie zweryfikowanych w tej iteracji: **0**. Nie utożsamiać `approved` z `verified`. Aktualna liczba etykiet z nowo potwierdzoną kompilacją: **0**.
- Nie modyfikowano Lean, manifestu, źródłowego TeX, backendu, frontendu ani pozostałych audytów.

## Blokady i dalsza kontrola
Potrzebne są: niezależne przeliczenie SHA256 kanonicznego pliku, świeże wykonanie `lake env lean` na przypiętym Lean/Mathlib z pełnym logiem i `#print axioms`, testy regresyjne/integracyjne oraz oddzielny pełny sceptyczny audyt po uzyskaniu czystych wyników. Do tego czasu brak PASS, certyfikacji i zakończenia etapu.
