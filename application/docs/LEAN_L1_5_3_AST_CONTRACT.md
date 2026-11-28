# L1.5.3 — kontrakt typowanego AST, wersja projektowa 1

Dokument odbiorczy przed implementacją, nie dowód działania parsera. Zgodny z [planem lokalnej autoformalizacji](LEAN_LOCAL_AUTOFORMALIZATION_PLAN.md). Nie zmienia bieżącego kandydata L1.5.2.

## Zakres

Pierwszy silnik reguł ma być czystą funkcją walidującą mały, zamknięty język pośredni. Parser pełnych fragmentów LaTeX i mapowanie do Lean należą do kolejnych podetapów. Nie nazywać walidacji AST transkrypcją kompletnego twierdzenia, dowodem ani certyfikatem.

Typy pilota: Prop, Nat, Int, Real. Jawne deklaracje zmiennych; bez automatycznych koercji, domyślnych typów liczbowych, typów zależnych, ogólnych funkcji, zbiorów i przeciążeń operatorów. Rozszerzenia wymagają wersjonowania gramatyki.

## Zamknięta gramatyka pośrednia

Każdy węzeł posiada dokładnie pola odpowiednie dla swojego rodzaju, typ oraz zakres źródła. Nie dopuszczać dowolnego kodu Lean, importów, nazw taktyk ani metaprogramowania. Wartości typu, rodzaju i operatora to zamknięte enumeracje.

| Konstrukcja | Pola właściwe | Warunek typowania |
|---|---|---|
| var | identyfikator wiązania | typ deklaracji w aktywnym zakresie |
| numeral | nieujemna kanoniczna liczba dziesiętna | jawny Nat, Int lub Real |
| truth / falsehood | brak | Prop |
| not | argument | Prop → Prop |
| and / or / implies / iff | lewy, prawy | Prop × Prop → Prop |
| eq | lewy, prawy | jednakowy typ obu stron → Prop |
| lt / le | lewy, prawy | jednakowy typ liczbowy → Prop |
| add / mul | lewy, prawy | jednakowy typ liczbowy → ten typ |
| neg / sub | argument albo lewy, prawy | wyłącznie Int lub Real, nie Nat |
| forall / exists | wiązanie z jawnym typem, ciało | ciało Prop, wynik Prop |

Nie interpretować eq na Prop jako iff ani odwrotnie. Potęgowanie, dzielenie i odejmowanie w Nat odłożyć do jawnego ustalenia semantyki. W pierwszej wersji nie wprowadzać żadnego węzła unknown zastępującego podwyrażenie: nierozpoznany składnik blokuje całą tezę.

## Wiązania, założenia i pochodzenie

- Każde wiązanie ma niepowtarzalny wewnętrzny ID, typ i zakres deklaracji. Nazwa prezentacyjna LaTeX jest oddzielna od ID. Odwołania sprawdzać leksykalnie; brak wiązania, nieaktywne wiązanie i ponowne wykorzystanie ID są błędami. Cieniowanie nazw prezentacyjnych nie zmienia identyfikatorów.
- Wejście dokumentu pośredniego jawnie rozdziela uporządkowane parametry, założenia typu Prop oraz konkluzję typu Prop. Nie usuwać, nie sortować ani nie deduplikować założeń. Zakres parametrów obejmuje kolejne założenia i konkluzję. Puste założenia są dopuszczalne. Kwantyfikatory tworzą osobne zakresy. Pilot nie obejmuje zależnych typów parametrów.
- Każdy zakres to półotwarty przedział [start,end) indeksów znaków Unicode w niezmienionym źródle Pythona, nie bajtów UTF-8 ani jednostek UTF-16. Wymagać 0 <= start < end <= len(source); zakres dziecka zawarty w zakresie rodzica. Nie normalizować znaków ani końców linii przed sprawdzeniem SHA-256 oryginalnych bajtów UTF-8.
- SHA-256 źródła, wersja schematu i deterministyczna reprezentacja AST stanowią pochodzenie. Zgodność zakresów nie dowodzi zgodności znaczenia. Dane wejściowe mogą być ręcznie opisane w pilocie, dlatego nie deklarować pokrycia całego LaTeX ani pełnej transkrypcji.
- Nie ufać zadeklarowanemu typowi; obliczać go z operatora, wiązań i dzieci, a następnie porównywać z podanym. Brak koercji Nat→Int→Real. Zakresy i identyfikatory sprawdzać bez wykonywania tekstu.

## Limity i kontrakt wyniku

Ustalić jawne, testowane limity: źródło 32 KiB UTF-8, zserializowany AST 128 KiB, maks. 2048 węzłów, głębokość 64, maks. 128 wiązań i 64 cyfry literału. Nie przetwarzać nieograniczonej rekursji, cykli ani nieznanych pól. Odrzucać bool podszywający się pod int oraz wartości poza limitami. Jeśli parser JSON działa przed walidatorem, jego własne limity i obsługa błędów również wymagają kontroli.

Wynik: validated_ast albo unsupported/invalid_input z kodem i ścieżką błędu; deterministyczny, bez sieci, zapisu plików, subprocess, modelu AI i kosztów zewnętrznych. Nie zwracać częściowego Lean jako sukcesu. candidate_status=not_generated, proof_status=not_run, statement_status=unreviewed, certificate=false. AST nie jest jeszcze podłączony do publicznego endpointu w L1.5.3.

## Testy odbiorcze

- Poprawne: zagnieżdżona implikacja, kwantyfikatory z cieniowaniem nazw lecz rozłącznymi ID, jawna arytmetyka każdego obsługiwanego typu, uporządkowane założenia, wielobajtowe źródło.
- Negatywne: nieznany operator/pole/typ, zmienna wolna, wyciek wiązania po kwantyfikatorze, powtórzone ID, niezgodne typy i deklarowany typ wyniku, mieszana arytmetyka, neg/sub Nat, liczba z wiodącym zerem lub kodem, nie-Prop jako konkluzja, brak źródła, błędny hash i zakres, przekroczenie każdego limitu. Zmiana kolejności założeń i zakresów musi być wykrywalna w reprezentacji. Powtórzenie wejścia ma dawać identyczny wynik.
- Sceptyczny audyt: nie ma podstaw do twierdzenia, że poprawny AST pokrywa wszystkie założenia oryginalnego tekstu; to odrębny warunek parsera L1.5.4–5 i niezależnej kontroli semantycznej. Testy kontraktu nie mogą udawać kompilacji Lean. Po implementacji rzeczywiste CI 2+1 na niezmiennym SHA.


## Konkretna postać wymiany danych (implementacja d2d4aa1c)

Wejście funkcji `validate_ast(source: str, ast_json: bytes)` to niezmieniony tekst źródłowy i UTF-8 JSON, a nie dowolny obiekt Pythona. Na najwyższym poziomie dokładnie schema_version=1, source_sha256, parameters, assumptions, conclusion. Węzeł ma kind, type, span i pola: var → binding_id, numeral → digits (tekst), truth/falsehood → brak, not/neg → arg, operatory dwuargumentowe → left/right, forall/exists → binding/body. Wiązanie ma id, name, type, span. ID to ASCII zgodne z [A-Za-z][A-Za-z0-9_]{0,63}, name to wyłącznie metadane prezentacyjne, nigdy nazwa bezpośrednio emitowana do Lean. Przy generacji używać bezpiecznego mapowania identyfikatorów na świeże nazwy; nie interpolować nawet poprawnych ID (mogą pokrywać się ze słowami kluczowymi Lean).

### Audyt statyczny pierwszej implementacji

- Sprawdzanie typu każdego dziecka poprzedza rozstrzygnięcie typu operatora. Eq dla zgodnych typów, również Prop, pozostaje odrębny od Iff; nie ma koercji, a neg/sub Nat są blokowane. Literale numeryczne mają jawny typ, nie domyślne Nat. Nie znaleziono niespójności z zamkniętą tabelą operatorów.
- Parametry są dostępne w założeniach i konkluzji; kwantyfikator przekazuje rozszerzoną kopię środowiska tylko do body. Globalny zbiór seen zapobiega powtórzeniu ID również w rozłącznych poddrzewach. Nie jest to analiza zakresów w oryginalnym LaTeX: parser musi niezależnie wykazać poprawność wiązania nazw i pokrycie źródła.
- Przed dekodowaniem JSON działa ograniczenie bajtów i zagnieżdżenia z uwzględnieniem escape w stringach; po dekodowaniu odrzucane są nieznane pola, powtórzone klucze (także po dekodowaniu escape), float/NaN, bool jako wersja/offset. Ograniczenia liczby węzłów i wiązań są globalne dla całego dokumentu. Kanoniczny digest sortuje klucze obiektów, nie listy; zachowuje kolejność założeń i parametrów. Zwracany AST nie jest podpisem ani zamrożonym obiektem: odbiorca musi traktować go jako dane i walidować ponownie przed przyszłą generacją.
- Źródło jest haszowane jako oryginalne UTF-8, span to indeks znaków Pythona. Nie sprawdzamy na tym etapie, czy wskazany zakres rzeczywiście zawiera odpowiednią formułę; np. ręcznie skonstruowany AST truth może przejść dla źródła o innym znaczeniu. Wynik validated_ast oznacza wyłącznie poprawność strukturalno-typową, nie pokrycie i nie dowód. Wymagać od L1.5.4 jawnej kontroli pełnego pokrycia i odmowy przy nieobsługiwanym fragmencie.
- Zakres przyszłego uzupełnienia regresji: dokładne dodatnie granice głębokości/wiązań/węzłów, wszystkie pary typów dla operatorów dwuargumentowych, ID użyte ponownie w rozłącznych kwantyfikatorach, escape kluczy JSON, niepoprawne surrogate i rozróżnienie UTF-16 od Unicode. Nie resetować bieżącej serii 2+1 wyłącznie dla dopisania planu testów. Przypadki te nie są przedstawiane jako wykonane.

Audyt statyczny własnego kodu, nie niezależny odbiór. Nie zmienia implementacji ani konfiguracji walidacji.
