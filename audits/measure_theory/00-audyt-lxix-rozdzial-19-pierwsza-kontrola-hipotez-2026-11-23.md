# Audyt LXIX (69) — rozdział 19 „Zastosowania twierdzenia Radona–Nikodyma”

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Zakres audytu:** wyłącznie rozdział 19.

## Stan wejściowy i kontekst
Odczytano aktualne pliki `books/pl/measure_theory.tex` (blob `c80ec1f02cc8548f64fe44d202d89d961496d92b`), `chapters/pl/measure_theory/19-zastosowania-twierdzenia-radona-nikodyma.tex` (blob wejściowy `7571e99edac729831e83e8061377757874cfb7bc`), `AGENTS.md`, `docs/pl/standardy_terminologiczne.md` i `books/pl/integration_theory.tex` jako kontekst. Odczytano raport LXVIII (blob `f632f3fcd77460fc7711d4ddc557e95758711866`), który potwierdza stabilność rozdziału 18 i dopuszcza rozpoczęcie rozdziału 19. Wyszukiwanie commitów przez API nie zwróciło wyników; nie potwierdzono zatem kompletności listy nowszych raportów i commitów. Nie audytowano innego rozdziału.

## Kontrola matematyczna
Sprawdzono konstrukcję zmiany miary i całkowanie funkcji nieujemnych, obraz miar i warunkową wartość oczekiwaną, wariację całkowitą, nierówność przetwarzania danych, dowód lematu Neymana–Pearsona, kwantylową konstrukcję testu o zadanym poziomie, przykład dwupunktowy, skończony wzór Bayesa, wyciąganie czynnika mierzalnego, warunkową nierówność Jensena, kontrakcję w Lp, entropię względną oraz przykład niejednoznaczności rozkładu warunkowego. Nie stwierdzono w tej kontroli jawnego kontrprzykładu do tez. Sprawdzenie nie zastępuje niezależnego ponownego audytu po poprawce.

## Wykryta usterka i korekta
Wniosek `cor:conditional-lp-19` nie deklarował samodzielnie przestrzeni probabilistycznej, pod-σ-ciała ani mierzalności funkcji Y; posługiwał się obiektami z poprzedniego twierdzenia bez jawnego związania kwantyfikatorów. Dodano pełne hipotezy `(Ω,F,P)`, `G⊆F` oraz `Y:Ω→R` mierzalną. Pozostawiono etykietę i tezę bez zmian. Commit źródła: `b0dcdb8f13b444a01220756e3028c5803d1e808b`. Nowy blob źródła: `f60b1b5073bb36bbd096cc44b110de6994e84d40`. Ponownie odczytano plik i potwierdzono zgodność tekstu po aktualizacji.

## Kontrola techniczna i terminologiczna
Odczytany rozdział liczy 592 wiersze po korekcie. Stosowane funkcje charakterystyczne zapisano jako `\\chi_A` (w odpowiednich zbiorach). Zachowano istniejące etykiety i odsyłacze. Nie uruchamiano w tej iteracji kompilacji LaTeX, testów automatycznych ani GitHub Actions; nie pobrano i nie obejrzano PDF. Te kontrole pozostają otwarte. Nie zmieniano `integration_theory.tex`, nie scalano treści i nie dodawano opcjonalnych twierdzeń.

## Werdykt i następny krok
**Rozdział 19: NIESTABILNY — trwa stabilizacja.** Po poprawce wymagany jest kolejny pełny niezależny audyt tego samego rozdziału, następnie potwierdzenie testów, kompilacji i przegląd wizualny PDF oraz dodatkowy czysty audyt. Nie przechodzić do rozdziału 20.