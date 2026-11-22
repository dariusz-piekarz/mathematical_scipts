# Topologia ogólna — globalny audyt 01 (rozdziały 01–22)

**Data:** 2026-11-22.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zakres:** 22 rozdziały aktualnie zarejestrowane w `catalog/books.json`.
**Status:** kontrola globalna **otwarta**; wykonano przekrojową kontrolę strukturalną i wybranych kluczowych dowodów. Nie jest to deklaracja indywidualnej weryfikacji każdego z 261 środowisk dowodów.

## Wynik przekrojowy

- 22 pliki rozdziałów, 15 951 wierszy LaTeX.
- 261 środowisk `proof`, 672 definicje etykiet `\label`, 190 odwołań `\ref`, `\eqref` lub `\pageref`.
- Sprawdzono lokalnie w obu grupach 01–11 i 12–22 brak kolizji etykiet oraz zgodność terminologii. Wszystkie trzy odsyłacze z grupy 12–22, których cele leżą poza tą grupą, wskazują istniejące twierdzenia w rozdziale 07 (`thm:topog-zwartosc-fip` i `thm:topog-zwartosc-ultrafiltry`).
- Utworzono niezależny walidator `tools/tests/test_general_topology_global_audit.py`: kontrola katalogu i kolejności importów, pełnej globalnej unikatowości etykiet, odsyłaczy, terminologii, bilansu środowisk, liczby dowodów i rysunków.
- Wpięto ten walidator jako krok do `.github/workflows/general-topology-chapter.yml`.
- CI dla commitu `078021ef4b47f42e4ef426414ef00234d76be866`:
  [workflow 45049973285](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45049973285).
  W chwili sporządzenia tego wpisu: testy, w tym nowy globalny walidator, pomyślne; budowanie pełnej książki w toku. Nie wolno przedstawiać niezakończonego CI jako zielonego.

## Próbkowa, niezależna kontrola argumentacji matematycznej

1. **07 / Tychonoff:** przypadki pustego indeksu i pustego czynnika rozstrzygnięte osobno. Dla dowolnej niepustej rodziny czynników skorzystano jawnie z aksjomatu wyboru. Przeciwobrazy filtrów rzutowanych są ultrafiltrami; ciągłość rzutowa i skończone przecięcia wystarczają do zbieżności w topologii produktowej.
2. **10 / Urysohn:** sprawdzono poprawność kryterium \(\overline B\subseteq C\) dla wybranych par elementów przeliczalnej bazy, jawne użycie regularności do zwężenia otoczeń, oddzielanie funkcjami Urysohna i konstrukcję szeregu definiującego metrykę. Jest to celowana kontrola wskazanych kroków; inne części dowodu wymagają jeszcze odrębnego przeglądu.
3. **21 / Vietoris:** prześledzono definicję limitu ultrafiltru na hiperprzestrzeni zwartych niepustych, dowód domkniętości i niepustości skonstruowanego \(K\), oraz oba rodzaje warunków podbazowych. Zgodność z rozdziałem 07 jest jawna.
4. **22 / Kuratowski, Wijsman i Attouch--Wets:** w twierdzeniu o przestrzeniach właściwych poprawnie odseparowano warunek \(F\neq\varnothing\) i przypadek \(r=d(x,F)=0\); w przypadku \(r>0\) zwartość kuli umożliwia wybór granicy podciągu, co daje dolne ograniczenie odległości. Nie utożsamiono lokalnej zwartości ze zwartością kul.

## Przegląd powtórzeń i zakresów

- Rozdziały 07, 14, 21 i 22 wykorzystują zwartość odpowiednio ogólną, lokalną, hiperprzestrzeni i zbiorów zbieżnych. Nie są mechanicznym powtórzeniem: zależności są wskazane odsyłaczami.
- Rozdział 10 dowodzi metryzowalności Urysohna, 15 bada silniejsze kryterium Nagaty--Smirnowa. Nie scalać tych twierdzeń bez zachowania obu dowodów i odmiennych założeń.
- Rozdział 18 bada przestrzenie odwzorowań; 21 bada przestrzenie podzbiorów, a 22 szczególne rodzaje ich zbieżności.
- Rozdział 20 ogranicza się do topologicznych aspektów zbiorów analitycznych; teoria gier i determinacji należy do skryptu `Logika matematyczna i teoria mnogości`.
- Wymiar topologiczny ma być opracowany w rozdziale 23, a nie przez zmianę rozdziałów 07–10. Zbieżność Mosco i epigraficzna trafi do dalszego planu analizy funkcjonalnej/wariacyjnej po kontroli pokrycia tematów.

## Dalsze obowiązkowe audyty

1. Przejrzeć *wszystkie*, a nie tylko wybrane, dowody w blokach 01–06, 07–11, 12–17 i 18–22. W każdym sprawdzić wystarczalność założeń, przypadki puste, poprawność kwantyfikatorów, odsyłacze i zgodność przykładów.
2. Zweryfikować wygląd obrazów/rysunków w realnie wyrenderowanym pełnym PDF, nie ograniczać się do zielonego statusu kompilacji.
3. Osobno przeprowadzić mapę podobieństw z topologią algebraiczną, logiką i analizą funkcjonalną, zachowując niepowtarzającą się treść.
4. W razie wykrycia rzeczywistego błędu matematycznego poprawić go od razu; opcjonalne rozszerzenia zatwierdzonych rozdziałów tylko proponować.

**Wynik audytu 01:** istotnych usterek w przejrzanych kluczowych dowodach nie znaleziono; globalna kontrola pełnych 261 dowodów i renderingu pozostaje **otwarta**. Samo dodanie walidatora nie zmienia statusu wcześniej ustabilizowanych rozdziałów ani nie poświadcza ich niezależnej matematycznej poprawności.
