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

