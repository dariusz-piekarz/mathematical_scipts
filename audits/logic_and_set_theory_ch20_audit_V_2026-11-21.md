# Logika matematyczna i teoria mnogości — rozdział 20, audyt V

Data: 21 listopada 2026 r.
Źródło: `chapters/pl/logic_and_set_theory/20-prawda-arytmetyczna-i-twierdzenie-tarskiego.tex`, blob `34acf51274c003df9ffb2f6ca280b3ae60528a05`.
Tryb: niezależna kolejna kontrola istniejących twierdzeń i ich dowodów, **bez dodawania materiału**.

## Kontrola matematyczna

- **Wersja semantyczna Tarskiego**: dla `L` uzyskujemy w `Q` równoważność `L ↔ ¬Tr(⌜L⌝)`. Ponieważ standardowe liczby naturalne spełniają `Q`, jej prawdziwość w modelu standardowym jest uzasadniona. Przeciwną równoważność wymusza hipoteza o definiowalności prawdy. Sprzeczność jest poprawna.
- **Wersja syntaktyczna Tarskiego**: oddzielono niesprzeczność `T ⊇ Q` od poprawności semantycznej i efektywnej aksjomatyzowalności; oba kierunki `L ↔ ¬L` prowadzą do dowodów `L` i `¬L`.
- **Skończone predykaty prawdy**: konstrukcja dla ustalonej listy zdań działa również przy powtórzonych kodach.
- **(D1)**: dowód opiera się na konkretnym kodzie istniejącego dowodu i prawdziwej instancji formuły `Δ₀`; nie odwraca implikacji. Wskazano osobno rolę założenia `Σ₁`-poprawności przy metamatematycznym odwróceniu.
- **(D2) i (D3)**: poprawnie sformułowane jako obowiązki dowodowe, z odsyłaczem do następnego rozdziału; nie zostały tu założone bez dowodu.
- Skontrolowano definicje, kwantyfikatory, rozróżnienie prawdy, dowodliwości, definiowalności, wyliczalności i rozstrzygalności.

## Wykryta usterka w walidacji, poprawiona

Dwa testy w `tools/tests/test_logic_and_set_theory_ch20.py` wskazywały nieistniejącą dawną nazwę `21-formalized-proof-operations-and-derivability.tex`. Warunek `if target.is_file():` powodował ciche pomijanie rzeczywistej kontroli rozdziału 21. Testy odwołują się teraz do `21-operacje-na-dowodach-i-warunki-wyprowadzalnosci.tex` i **wymagają** jego istnienia przez `assertTrue`. Zmiana: commit `9e17f4c9b85186a8d785768515feb22101570291`.

## Status

- Matematyka istniejącego tekstu: **bez nowych usterek w tej iteracji**.
- Inwentarz niezmieniony: 3 twierdzenia, 1 lemat, 4 dowody, 3 definicje, 5 przykładów, 7 uwag; 8 etykiet, 14 odsyłaczy.
- Testy z poprawką zostały **uruchomione przez GitHub Actions**, ale przed zakończeniem biegu nie wolno deklarować PASS. Workflow: `logic-and-set-theory-chapter.yml`; sprawdzić końcowy status i PDF.
- Nie wykonano w tej iteracji lokalnej kompilacji ani ręcznych oględzin nowego PDF. Dotychczasowe wyniki PDF pochodzą z audytu IV.
