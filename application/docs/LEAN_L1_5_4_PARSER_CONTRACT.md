# L1.5.4 — kontrakt pierwszego parsera LaTeX (projekt v1)

Dokument projektowy podczas stabilizacji L1.5.3; nie jest implementacją parsera. Zgodność z [AST v1](LEAN_L1_5_3_AST_CONTRACT.md) i [planem lokalnej autoformalizacji](LEAN_LOCAL_AUTOFORMALIZATION_PLAN.md). Nie zmienia kandydata L1.5.3.

## Dwa poziomy wejścia

1. Pierwszy, samodzielny parser czystych formuł matematycznych: kontrolowany podjęzyk LaTeX/Unicode, deterministyczny, bez makr użytkownika. Można dostarczyć wyłącznie jawnie typowane deklaracje i formuły w osobnym, jednoznacznym formacie pilota.
2. Adapter pełnego twierdzenia z indeksu: rozpoznawanie struktury konkretnego środowiska, deklaracji, założeń i konkluzji, bez swobodnego tłumaczenia prozy. Dopóki adapter nie potrafi pokryć wszystkich składników, cały obiekt ma status unsupported. Sukces pojedynczej formuły nie jest sukcesem transkrypcji twierdzenia.

Nie wolno wybrać jedynie rozpoznanych wzorów z dłuższego fragmentu i zgłosić kompletnej tezy. Nie wolno zakładać typu zmiennej na podstawie jej nazwy. Kontekst indeksu i słownik pojęć w L1.5.5, generacja Lean w L1.5.6.

## Lekser

- Zachować źródło dokładnie w postaci Unicode otrzymanej z pakietu, SHA-256 UTF-8. Każdy token ma półotwarty zakres indeksów znaków w oryginale. Brak normalizacji Unicode i końców linii.
- Jawna lista terminali, najdłuższe pasujące symbole i pełne nazwy poleceń TeX: np. \land i \landscape to różne polecenia. Nie rozwijać makr, \input, \def, \csname, poleceń programistycznych, komentarzy ani dowolnych środowisk. W v1 odrzucać nieznany znak/polecenie, nawet jeśli reszta jest poprawna. Pomijać tylko jawnie dopuszczony biały znak (spacja, tab, CR, LF), nie całe fragmenty.
- Identyfikatory pilota: pojedyncze ASCII a-z/A-Z lub pojedyncze jawnie obsługiwane symbole greckie; komendy greckie tylko z zamkniętej listy, bez automatycznego ujednolicania odmiennych symboli. Zakaz niejawnego mnożenia i indeksów do czasu osobnej reguły. Nazwy wewnętrzne przydzielane deterministycznie według kolejności wiązań, bez używania tekstu jako kodu.
- Jawne tokeny typu: Prop, Nat, Int, Real oraz \mathbb{N}, \mathbb{Z}, \mathbb{R}, ℕ, ℤ, ℝ. Makra \mathbb tylko w tych trzech dokładnych postaciach. Literały ASCII 0 lub niezerowa cyfra z kolejnymi cyframi, najwyżej 64 cyfry. Wymagać jawnej adnotacji typu literału (np. (2 : \mathbb{R})); żadnego domyślnego Nat i inferencji przez domyślanie się zamiaru autora.

## Gramatyka i priorytety

W zapisie poniżej nazwy nieterminali nie są poleceniami LaTeX; nawiasy w cudzysłowach są terminalami. Kwantyfikator w v1 musi rozpoczynać osobną formułę lub grupę w nawiasach. Jego ciało ma pełny zakres aż do końca tej formuły/grupy.

    formula    ::= quantifier | iff
    quantifier ::= ("∀" | "∃") identifier ":" type "," formula
    iff        ::= implies [ IFF implies ]
    implies    ::= disjunction [ IMPLIES implies ]
    disjunction::= conjunction { OR conjunction }
    conjunction::= relation { AND relation }
    relation   ::= additive [ REL additive ]
    additive   ::= product { ("+" | "-") product }
    product    ::= unary { MUL unary }
    unary      ::= NEG unary | "-" unary | atom
    atom       ::= identifier | TRUE | FALSE
                 | "(" digits ":" type ")"
                 | "(" formula ")"

Kwantyfikatory mają również aliasy \forall i \exists. Dla notacji \forall x\in\mathbb{R} dopuszczenie reguły wymaga ścisłego rozpoznania, że x jest wiązany z całym obsługiwanym typem, nie podzbiorem; inne wystąpienia \in w v1 są unsupported. Operator negacji logicznej NEG w tej wersji wymaga nawiasów dla negowanego porównania: \neg(x < y), nie \neg x < y. Nie dopuszczać domyślnej zmiany priorytetu na podstawie błędu typowania.

| Terminal | Dopuszczone postacie |
|---|---|
| IFF | \iff, \Leftrightarrow, ↔ |
| IMPLIES | \implies, \Rightarrow, \to, \rightarrow, → |
| OR | \lor, \vee, ∨ |
| AND | \land, \wedge, ∧ |
| NEG | \neg, \lnot, ¬ |
| REL | =, <, >, \le, \leq, ≤, \ge, \geq, ≥ |
| MUL | \cdot, \times, ×, · |
| TRUE/FALSE | \top, ⊤, \bot, ⊥ |

Implikacja prawostronnie łączna; +, -, mnożenie, AND, OR lewostronnie łączne. IFF i REL niełączone: a=b=c, P↔Q↔R odrzucić bez nawiasów. > i ≥ mapować odpowiednio do lt i le z zamianą argumentów, zachowując zakresy dzieci i zapisując regułę w śladzie translacji. Porównania nie oznaczają równoważności: Eq Prop pozostaje Eq, Iff pozostaje Iff. Wszelkie operatory sprawdzane według tabeli AST v1.

## Dokument pilota i pokrycie źródła

Przed integracją pełnego twierdzenia używać pojedynczego źródła z rozłącznymi, uporządkowanymi segmentami deklaracji/założeń/konkluzji. Jeśli zakresy wskazuje wywołujący, muszą być niepuste, uporządkowane, bez nakładania; niepokryte znaki mogą być wyłącznie dozwolonym białym znakiem. Format segmentów jawnie wersjonowany; nie przyjmować dowolnych metadanych jako dowodu poprawności automatycznego wydzielenia z twierdzenia. Deklaracja w pilocie: identifier ":" type. Założenia i konkluzja to formuły typu Prop. Każdy segment wymaga pełnego zużycia tokenów do EOF, bez pomijania ogona. Powtarzające się deklaracje parametrów o tej samej nazwie odrzucać; cieniowanie przez kwantyfikator tylko leksykalne. Przy wyjściu z ciała przywrócić środowisko zewnętrzne. Założenia nie wprowadzają globalnych wiązań.

Wynik AST przekazać do istniejącego validate_ast; jakikolwiek błąd oznacza brak kompletnego AST. Tokeny, reguły i zużyte zakresy mają dać odtwarzalny ślad. Osobne statusy: parsed_formula / parsed_pilot_statement, unsupported, invalid_input; nie nazywać ich pełną transkrypcją źródła indeksowanego. Niezależna kontrola semantyczna nadal pending, candidate_status=not_generated, proof_status=not_run, certificate=false.

## Limity i odbiór

Przed rekurencją i alokacją ograniczyć źródło do 32 KiB UTF-8; maks. 8192 tokenów, 64 poziomy zagnieżdżenia składni, maks. 2048 węzłów, 128 wiązań, 128 KiB serializacji AST. Kontrolować również prawostronne łańcuchy implikacji, zagnieżdżenia nawiasów, negacji i kwantyfikatorów, nie tylko finalny AST. Nie dopuścić do nieobsłużonego RecursionError, nieograniczonej ekspansji makr ani wykonywania kodu. Bez endpointu, sieci i zmian źródłowych.

Testy pozytywne: P→Q→R, (P→Q)→R, \neg(P\land Q), kwantyfikatory z cieniowaniem nazw, typowane działania i nierówności, zamiana argumentów ≥, dwa identyczne założenia zachowane oddzielnie, dokładne zakresy znaków Unicode. Testy negatywne: nieznane polecenie, \landscape, komentarz, niejawne mnożenie, niejawny typ literału, niespójne typy, wolna zmienna, łańcuch relacji, niewłaściwa negacja, brak delimitera, dodatkowy nieprzetworzony ogon, luka w segmentach z prozą lub założeniem, złośliwie głęboka składnia i każde przekroczenie limitu. Testy porównują konkretne oczekiwane AST, a nie sam status sukcesu. Rozdzielić testy samodzielnego parsera od późniejszego adaptera środowisk twierdzeń. Nie uznawać powyższych testów za wykonane przed implementacją.
