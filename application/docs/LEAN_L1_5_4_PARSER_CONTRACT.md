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


## Audyt rzeczywistych twierdzeń pilota z rejestru

Przegląd dziewięciu pozycji aktualnego application/lean/manifest.json i ich oryginalnych bloków twierdzeń (nie wykonywano parsera, którego jeszcze nie ma). Pliki źródłowe: chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex, blob 03f0971888288934e47c3453fd8f0de0a2c71469; 02-kwantyfikatory-i-podstawowe-metody-dowodzenia.tex, blob 000ad4c0185eb2296ad7af3523ad30b08dfeebaf. Przewidywany wynik pełnego adaptera v1: 0/9 obsługiwanych w całości; nie jest to pomiar działającego kodu.

| Etykieta | Brakująca semantyka lub konstrukcja, której nie wolno pominąć |
|---|---|
| thm:de-morgan-logic | Formuły jako obiekty składniowe, równoważność pod każdym wartościowaniem (\equiv), dwie klauzule. |
| thm:implication-laws | Dwie równoważności oraz dodatkowa tautologia modus ponens zapisana w prozie. |
| thm:negated-implication-xli | Typ składniowy Formula, nie Prop; równoważność semantyczna. |
| thm:equiv-test | Rozróżnienie metajęzykowej równoważności \equiv, spójnika \Leftrightarrow i predykatu tautologii. |
| thm:logic-distributivity | Trzy klauzule w align*, semantyka formuł; nie redukować do pierwszej. |
| thm:negation-quantifiers | Dowolna, także pusta dziedzina, predykat jednoargumentowy, założenie logiki klasycznej, dwie klauzule. |
| thm:same-quantifier-order | Dwie dowolne dziedziny, predykat dwuargumentowy, dwie klauzule. |
| thm:swap-mixed | Implikacja w jedną stronę oraz osobne stwierdzenie, że odwrotna nie zachodzi ogólnie. |
| thm:unique-expansion-xli | Kwantyfikator jednoznacznego istnienia, dowolna (także pusta) dziedzina, predykat jednoargumentowy. |

Sprawdzono również application/lean/src/LST01_SyntaxValuations.lean: istniejąca formalizacja rozróżnia induktywny typ LST01.Formula, Valuation = Nat → Bool, eval, equivalent i tautology. Nie wolno w adapterze zastąpić tego przez samo Prop i Iff, nawet jeśli otrzymany odpowiednik jest twierdzeniem Lean. Potrzebny będzie wersjonowany słownik i szerszy AST z kontekstem typów, predykatami i wieloma klauzulami. Nie oznacza to zgody na automatyczne rozszerzenie zakresu bieżącego podetapu ani zmianę kanonicznego źródła. Przykłady te stanowią przyszłe negatywne przypadki odbiorcze L1.5.4; właściwą obsługę planować dopiero w odpowiednio rozszerzonym kontrakcie L1.5.5 i kolejnych etapach.


## Wektory odbiorcze gramatyki (oczekiwany wynik, nie wykonane testy)

Poniżej deklaracje są niezależnymi segmentami pilota, a oznaczenia funkcjonalne opisują strukturę oczekiwanego AST (nie jego format JSON). Typy i zakresy źródłowe mają zostać sprawdzone dodatkowo przez testy. Wiersze z kwantyfikatorami używają separatora przecinka; nie wprowadza się niejawnych zmiennych.

| Parametry | Formuła | Oczekiwany AST lub odmowa |
|---|---|---|
| P:Prop, Q:Prop, R:Prop | P\to Q\to R | implies(P,implies(Q,R)) |
| P:Prop, Q:Prop, R:Prop | (P\to Q)\to R | implies(implies(P,Q),R) |
| P:Prop, Q:Prop, R:Prop | P\lor Q\land R | or(P,and(Q,R)) |
| P:Prop, Q:Prop | \neg(P\land Q) | not(and(P,Q)) |
| P:Prop, Q:Prop | P=Q | eq(P,Q), nie iff |
| P:Prop, Q:Prop | P\iff Q | iff(P,Q), nie eq |
| x:Real, y:Real | x\geq y | le(y,x), ślad zamiany argumentów |
| x:Int, y:Int, z:Int | x-y-z=x | eq(sub(sub(x,y),z),x) |
| x:Int, y:Int, z:Int | x+y\cdot z=x | eq(add(x,mul(y,z)),x) |
| x:Real | x+(2:Real)=x | eq(add(x,numeral(Real,2)),x) |
| brak | \forall x:Real,\exists x:Real,x=x | dwa różne ID, oba wystąpienia x w eq odnoszą się do wewnętrznego ID |
| x:Real | (\forall x:Real,x=x)\land x=x | wewnętrzny ID tylko w kwantyfikatorze, dwa końcowe x odnoszą się do parametru |
| x:Nat, y:Nat | x-y=x | unsupported/type_mismatch; bez zastępowania odejmowania działaniem w Int |
| x:Real, n:Nat | x=n | type_mismatch, brak koercji |
| x:Real | x+2=x | unsupported: typ literału niejawny |
| x:Real | x<x<x | unsupported: łańcuch relacji |
| P:Prop, Q:Prop, R:Prop | P\iff Q\iff R | unsupported: łańcuch iff |
| P:Prop, Q:Prop | P\landscape Q | unsupported: nieznane polecenie |
| x:Real, y:Real | \neg x<y | type_mismatch; wymagane \neg(x<y) |
| brak | (\exists x:Real,x=x)\land x=x | unbound_variable, bez wycieku zakresu |
| P:Prop | P%ukryte założenie | unsupported: komentarz |
| P:Prop | P \input{plik} | unsupported: bez odczytu plików |

### Pełne pokrycie i ślad

Przykład źródła pilota z segmentami, gdzie znaki LF są zachowane: "P:Prop\nQ:Prop\nP\nP\nP\\to Q". Segmenty półotwarte: parametry [0,6), [7,13), założenia [14,15), [16,17), konkluzja [18,24). Oczekiwanie: obie identyczne przesłanki pozostają oddzielne. (Backslash w cytowanym zapisie jest pojedynczym znakiem źródła, nie dwiema pozycjami.) Każdy segment ma własny EOF; luki wyłącznie z dozwolonych białych znaków.

Warianty negatywne: usunięcie jednego segmentu założenia pozostawia niepokryty znak P; nakładanie segmentów i ich zamiana naruszają strukturę dokumentu; dopisanie nieznanej treści po konkluzji nie jest dopuszczalnym ogonem. Każda taka zmiana musi dać odmowę, nie skrócony AST.

Ślad translacji ma zawierać co najmniej wersję gramatyki, SHA źródła, typy i zakresy segmentów, dokładne zakresy tokenów oraz jawne reguły przekształceń (np. GE_REVERSE). Nie musi powielać pełnego tekstu źródła. Status pokrycia odnosi się wyłącznie do kontrolowanego formatu pilota, nigdy automatycznie do całego środowiska twierdzenia. Test odtwarzalności porównuje cały AST i ślad, nie tylko status i liczbę tokenów.


## Audyt leksera i granica między lekserem a parserem

Implementacja: backend/lean_lexer.py, kandydat f875add0343499753fc2ac53f9e6bf98675eb290. Token jest niemutowalnym rekordem kind/value/start/end. Wartość IDENT może być kanonicznym odpowiednikiem jawnego aliasu greckiego; zakres zawsze dotyczy oryginalnej pisowni. Brak rozszerzania komend TeX. EOF nie jest tokenem treści i nie wlicza się do limitu 8192. Status tokenized dotyczy jedynie warstwy leksykalnej; nawet wejście składające się wyłącznie z białych znaków nie jest poprawnym twierdzeniem.

Wymaganie dla parsera: tokenizować całe źródło raz przed podziałem na segmenty. Nie tokenizować osobno dowolnie wyciętych podciągów, ponieważ podział w środku polecenia, identyfikatora lub typu mógłby ominąć regułę najdłuższej nazwy. Każdy segment zawiera całe tokeny, co najmniej jeden token treści; sąsiednie segmenty rozdziela co najmniej jeden dopuszczony biały znak. Wymagać pokrycia wszystkich tokenów treści dokładnie raz. Sztuczny EOF segmentu wyznacza jego koniec w źródle. Nieprzetworzony ogon, luka w tokenach, granica przecinająca token lub nadmiarowa treść = odmowa. Limity tokenów, węzłów i wiązań obowiązują globalnie dla dokumentu, nie osobno dla segmentów.

Testy integracyjne do wykonania po implementacji: P:PropQ:Prop nie może zostać zaakceptowane przez rozcięcie wewnątrz typu; granica wewnątrz \mathbb{R} albo \land jest błędem; segment samych spacji jest błędem; 8193 tokeny rozproszone po poprawnych segmentach nadal przekraczają limit. Również \in i token DIGITS nie otrzymują znaczenia automatycznie na podstawie sukcesu leksera: wymagane odpowiednio wiązanie z obsługiwanym typem i jawna adnotacja numeryczna. Nie zmieniono kodu produkcyjnego ani bieżącego kandydata. Audyt statyczny własny, nie niezależny odbiór.
