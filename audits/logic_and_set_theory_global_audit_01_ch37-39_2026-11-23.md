# Logika matematyczna i teoria mnogości — audyt przekrojowy 01 (rozdziały 37–39)

**Data:** 23 listopada 2026 r. (Europe/Warsaw).  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** zatwierdzone rozdziały 37–39, bez nowych definicji, twierdzeń i przykładów.  
**Werdykt:** pięć usterek językowych poprawionych, brak nowo wykrytej usterki matematycznej w skontrolowanych dowodach; lokalne kontrole statyczne czyste. Pełne CI po korektach wymaga odrębnego potwierdzenia.

## 1. Źródła i poprawki

- Rozdział 37, `37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex`: blob przed korektą `bdd452bdeecbf424b10ff14f53eccd6c51aa97e2`, po korekcie `6c495beddc92e39b6885171e6415f0efe21d5b59`, commit `80ae0cc1494688b48ce41e4d08247380c7537546`. Poprawiono „liczba kardynalna λ taki” na „... taka” oraz dwa wystąpienia błędnej formy „nieprzeliczalnym regularną” na „nieprzeliczalną regularną”.
- Rozdział 38, `38-kardynaly-mahla-i-slaba-zwartosc.tex`: blob przed korektą `12bef7a26441d8c5c152af48835201ec67814768`, po korekcie `28d73acfcc3a6db9519822df210aa66391c51628`, commit `a44363dce5669206c76e5cc342748e6fc7a70efb`. Poprawiono „w nieprzeliczalną regularną liczbą kardynalną” na „w nieprzeliczalnej regularnej liczbie kardynalnej” i „liczba kardynalna λ taki” na „... taka”.
- Rozdział 39, `39-slaba-zwartosc-charakterystyki-i-logika-infinitarna.tex`: blob `9d06016d71a4c42434b8f0a58c13f666160a4034`, bez zmian.

W żadnym z trzech rozdziałów nie zmodyfikowano etykiet, odsyłaczy, przesłanek twierdzeń ani treści matematycznych.

## 2. Niezależna kontrola matematyczna

1. **Mierzalność i silna nieosiągalność (37):** gdy κ jest singularna, rozbicie na `cf(κ)<κ` małych przedziałów jest niezgodne z κ-zupełnością niegłównego ultrafiltru; dowód silnej graniczności wykorzystuje iniekcję κ→P(λ) i jedno wspólne włókno wszystkich współrzędnych, które musi mieć co najwyżej jeden element. Obydwa argumenty wymagają prawidłowo wskazanego założenia `λ<κ`.
2. **Model `V_κ` (37):** regularność κ ogranicza supremum rang rodzin obrazów mocy mniejszej od κ, a silna graniczność zapewnia `|V_α|<κ` dla wszystkich `α<κ`. Zastępowanie jest sprawdzane dla relacji spełniania w *zbiorowej* strukturze `V_κ`, bez odwołania do nieistniejącego globalnego predykatu prawdy.
3. **Ultraprodukt uniwersum (37):** wybranie zbiorowych reprezentantów Scotta usuwa problem proper-class klas równoważności, licznik zupełności wyklucza malejące ciągi długości ω, a zbiorolokalność umożliwia kolaps Mostowskiego. Należy nadal rozróżniać dowód matematyczny od rzeczywistej formalizacji w Lean.
4. **Normalizacja ultrafiltru (37→38):** filtr `W={X⊆κ:κ∈j(X)}` jest niegłówny i κ-zupełny. Dla funkcji regresywnej `j(f)(κ)<κ` daje stałe włókno miary jeden. W rozdziale 38 normalność jest poprawnie użyta do wykazania, że każdy klub należy do `W`.
5. **Liczby kardynalne Mahla (38):** elementarność `j` i absolutność silnej nieosiągalności w kierunku `V→M` dają `κ∈j(I_κ)`; skoro klub także należy do normalnej miary, `I_κ` przecina każdy klub. Dowód nie zastępuje stacjonarności samą nieograniczonością.
6. **Własność drzewa (38→39):** zanurzenie z miary daje węzeł poziomu κ w `j(T)`; małość oryginalnych poziomów zapewnia, że wszyscy poprzednicy na poziomach `α<κ` są postaci `j(s_α)`. W rozdziale 39 drzewo profili ma małe poziomy dzięki silnej graniczności, a z gałęzi otrzymuje się jednorodny zbiór o mocy κ, bez zakładania monotoniczności funkcji wyboru `a(δ)`.
7. **Relacja podziałowa → własność drzewa (39):** przy regularnej κ mniej niż κ niskich poziomów zawiera mniej niż κ węzłów. Wyróżniony zbiór `A` zawiera węzeł na każdym poziomie; rozdzielenie stożków porządku leksykograficznego wyklucza nieporównywalne węzły w `A`.
8. **Zwartość zdaniowa (39):** nośnik każdej formuły ma moc mniejszą od κ, a regularność czyni go ograniczonym. Kodowanie gałęzi za pomocą `P_α` i `Q_{s,t}` używa co najwyżej κ formuł o nośnikach mocy mniejszej niż κ. Twierdzenie dotyczy logiki **zdaniowej**, nie automatycznie pełnej logiki pierwszego rzędu `L_{κ,κ}`.

Nie wykryto w kontrolowanych zależnościach sprzeczności między definicjami ani przesłankami rozdziałów 37–39. Audyt nie jest maszynową weryfikacją semantyczną wszystkich twierdzeń.

## 3. Kontrole strukturalne i odsyłacze

Po obu poprawkach ponownie odczytano aktualne pliki z GitHuba:

| Rozdział | Wiersze | Etykiety | Odsyłacze | Domknięcie środowisk |
|---|---:|---:|---:|---|
| 37 | 775 | 26 | 18 | PASS |
| 38 | 640 | 26 | 19 | PASS |
| 39 | 949 | 22 | 25 | PASS |
| **Łącznie** | **2364** | **74** | **62** | **PASS** |

- **0** powtórzeń etykiet pomiędzy rozdziałami 37–39.
- Wszystkie wewnętrzne odsyłacze trzech rozdziałów wskazują na istniejące etykiety.
- Pięć zewnętrznych celów z rozdziału 37 znaleziono w rozdziałach: 22 (`ch:second-incompleteness`), 25 (`ch:zf-axioms`), 31 (`ch:constructible`), 35 (`ch:boolean-valued-independence`), 36 (`ch:symmetric-choice`).
- Wszystkie środowiska `\\begin/\\end` tych trzech rozdziałów mają prawidłowo sparowane nazwy.
- Nie znaleziono zakazanego rzeczownika „kardynał” w treści rozdziałów 37–39. Historycznych nazw plików nie zmieniano.

## 4. CI i status stabilności

W chwili sporządzania audytu:
- Test terminologii dla commitu `a44363d`: [workflow 45081007498 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007498).
- Walidacja logiki i teorii mnogości: [workflow 45081007565 — in progress](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007565).
- Testy aplikacji: [workflow 45081007531 — in progress](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007531).

Nie należy ogłaszać sukcesu pełnej kompilacji LaTeX ani oceny PDF po nowych zmianach przed zakończeniem odpowiedniego przebiegu CI. Rozdział 39 zachowuje wcześniejszy status stabilny (niezmieniony blob); poprawione rozdziały 37 i 38 wymagają powtórnej niezależnej kontroli po korektach zgodnie z zasadą 2+1. Najbliższy krok: audyt II na nowych blobach i kontrola wyników CI.

**Nowe treści:** brak; nie dodawano nieuzgodnionych twierdzeń, przykładów ani rozszerzeń zakresu.

## 5. Uzupełnienie — wynik walidacji po korektach

Po opublikowaniu pierwszej wersji raportu zakończył się przebieg
[45081007565 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007565)
dla commitu `a44363dce5669206c76e5cc342748e6fc7a70efb`.
W podglądzie zadań GitHub Actions wszystkie kroki `validate-chapters` uzyskały **SUCCESS**, w tym:

- inwentarz twierdzeń, import CLI i referencje,
- regresje rozdziałów 37, 38 i 39 (oraz 07–36),
- `Compile logic and set theory PDF`,
- `Check compiled PDF and log`,
- archiwizacja PDF i logu.

Wynik potwierdza przejście automatycznej walidacji repozytorium **po pięciu poprawkach**.
Nie jest osobną, wzrokową kontrolą wyrenderowanych stron ani weryfikacją dowodów
w systemie Lean. Zaliczenie CI jest wymaganym potwierdzeniem technicznym,
ale nie zastępuje dalszych niezależnych audytów 2+1 nowych blobów rozdziałów 37–38.
