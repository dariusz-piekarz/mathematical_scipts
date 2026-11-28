# AA-50 — audyt VI: włączenie regresji do CI

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Usterka konfiguracji i poprawka
Workflow .github/workflows/abstract-algebra-chapter.yml uruchamiał jawnie dwa wcześniejsze moduły AA-50, ale nie test_abstract_algebra_ch50_nonmonic.py. Brakowało także tego pliku w push.paths. Dodano oba wpisy bez modyfikowania pozostałych kroków. Commit 37ff2350053622c307a92d02c4776d7181b68750; blob workflow 32647d9d57116c800466d1c47a47ceeb5364d48c. Ponowny odczyt potwierdził oba wpisy.

## Rzeczywiste wykonanie lokalne
Skopiowano treść testu z GitHub do lokalnego środowiska; git hash-object potwierdził identyczność z blobem 7ff8ae1933a11768a6dc015db08466bfbce7a4d1. Python z SymPy 1.14.0: python /tmp/test_aa50_nonmonic.py -v, 2/2 testy OK (0,302 s). test_mixed_factors obejmuje dziewięć kombinacji; test_riccati_roots oba pierwiastki. To nie jest wykonanie całej regresji AA ani kompilacja książki.

## CI
Uruchomienie https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45292640958 ma head_sha 37ff2350053622c307a92d02c4776d7181b68750. Job 138105028679: in_progress; w odczycie kroki obu dotychczasowych testów, nowej regresji, kompilacji, weryfikacji i archiwizacji były pending. Nie przypisujemy im sukcesu przed zakończeniem.

## Werdykt
AA-50 W AUDYCIE: potwierdzona lokalnie nowa regresja, konfiguracja CI poprawiona, wykonanie CI trwa. Następny krok: odczyt końcowych wyników i artefaktu PDF tego uruchomienia, oględziny wszystkich stron AA-50. AA-51 nieotwarty. Nie zmieniono treści rozdziału ani poprzednich raportów.
