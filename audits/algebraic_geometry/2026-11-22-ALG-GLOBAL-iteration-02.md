# Geometria algebraiczna — audyt globalny II (2026-11-22)

## Stan po globalnym I i lokalnych VII–IX

Audyt przekrojowy na aktualnej gałęzi `biblioteka-matematyczna-iteracja-6`, po synchronizacji historycznego monolitu i zamknięciu ALG-10 przez dwie niezależne bezusterkowe kontrole VIII i IX. Skontrolowano 11 rozdziałów ALG-00–10, trzy moduły współdzielone, zapisy matematyczne wspólnych niezmienników, wykresy i realne dwa 184-stronicowe pliki PDF.

## Integracja techniczna: PASS

- Ponownie pobrano wszystkie kanoniczne rozdziały oraz monolit: **11/11** pełnych bloków od `\\chapter` zgodnych znakowo i uporządkowanych 00–10.
- Ponownie odczytano 3 współdzielone moduły: **406/406** unikalnych etykiet; **167/167** odsyłaczy rozwiązywanych; żadnych powtórzeń ani brakujących celów. Historyczne aliasy w modułach Lefschetza i rozdmuchania pozostawione celowo.
- Najnowszy rozdział ALG-10 ma blob `5b231c9b40ad7f547ccfb3050e3712b7be7a75b0`; są w nim wymagane definicja `Pic(X)` przez klasy izomorfizmu i jednolity termin „obszerny”. 75/75 domkniętych środowisk.
- [Workflow 45069448058](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069448058), head `bd06a71f178885cb5061dabf2729bfa00a600796`: **SUCCESS, 187 testów**; osobno skompilowano modułową książkę i monolit, obie mają po **184 strony**.
- Faktycznie pobrane PDF i końcowe logi: zero błędów, ostrzeżeń, przepełnień i niezdefiniowanych odsyłaczy; zero bloków tekstowych poza granicami stron; 184/184 stron ma identyczny obraz rastrowy w obu książkach. Dodatkowo ręcznie obejrzano cztery wykresy ALG-10 (10.1–10.4, strony PDF 175, 179, 182, 184): bez kolizji etykiet z liniami ani podpisów z rysunkami.

## Zależności matematyczne: kontrola wybranych węzłów

- Warianty `E²=-1`, `K_{\\tilde S}²=K_S²−1`, `b₂(\\tilde S)=b₂(S)+1` i `χ_top(\\tilde S)=χ_top(S)+1` są zgodne w rozdziałach ALG-06, ALG-07, ALG-08, ALG-10 i module wspólnym. Pamiętano o hipotezach właściwości/zwartości tam, gdzie potrzebne.
- `K_S∼(d−4)H`, `c₂(T_S)=(d²−4d+6)h²`, `χ_top=d(d²−4d+6)`, `p_g=binom(d−1,3)` (dla `d≥4`) i wzór Noethera są spójne w ALG-07/09/10. 1000 sprawdzeń dokładnej całkowitej tożsamości Noethera PASS.
- Słabe Lefschetza jest użyte do `π₁(S)=0`, twarde Lefschetza do monotoniczności liczb Bettiego, a Lefschetz `(1,1)` do klas dzielników; role twierdzeń pozostają rozłączne. Hipoteza Hodge'a nie jest przedstawiana jako twierdzenie. Podane testy i kontrola źródła **nie** są samodzielnymi dowodami wielkich twierdzeń zewnętrznych.

## Znalezione rozbieżności redakcyjne wymagające osobnego cyklu

**ALG-GLOBAL-II-01 — dwie odmiany nazewnictwa tego samego obiektu.** Rozdział ALG-03 (2 wiersze treści, wiersze około 664 i 690) i rozdział ALG-04 (61 wierszy treści) nadal systematycznie używają słowa „dywizor” i jego odmian, podczas gdy ALG-05–10 preferują „dzielnik”. Są to poprawne nazwy matematyczne, lecz corpus jest niespójny, a regresja ALG-10 wymaga wersji „dzielnik”. Zidentyfikowano też historyczne wewnętrzne etykiety `*-charts`, których nie wolno bez zmiany aliasów mechanicznie przemianowywać. W ALG-06 występuje pojedyncza informacja o angielskim tłumaczeniu terminu `ample`, która sama w sobie nie jest błędem.

**W tej iteracji nie modyfikowano zatwierdzonych źródeł ALG-03/04**, by nie unieważnić uprzednich reaudytów wyłącznie na podstawie globalnego przeglądu. Następna iteracja redakcyjna może ujednolicić odmianę „dzielnik” w ALG-03/04, wraz ze zmianą testu oczekującego dosłownego nagłówka `Snop dywizora`, synchronizacją monolitu i ponownymi niezależnymi kontrolami obu rozdziałów. Reguła: utrzymać pełną treść, oznaczenia `Div(C)`, etykiety `\\label` i istniejące odsyłacze; nie robić bezrefleksyjnego zastępowania podciągów nazw etykiet.

## Decyzja

**GLOBALNY II: integracja techniczna, główne węzły matematyczne i PDF PASS; znaleziono problem spójności redakcyjnej.** W przeciwieństwie do lokalnego ALG-10/IX globalna stabilizacja pozostaje **OTWARTA**. Do zamknięcia potrzebne rozstrzygnięcie i ewentualna migracja terminologii w ALG-03/04, ich pełne reaudty po zmianach oraz osobny, bezusterkowy audyt globalny III i kontrolny IV. Nie tworzyć ALG-11 automatycznie.


## Sprostowanie terminologiczne po audycie III (2026-11-22)

Wskazanie słowa „dywizor” w ALG-03/04 jako błędu wymagającego migracji do „dzielnika” było nieprawidłową oceną normatywną. **„Dywizor” jest poprawnym polskim terminem matematycznym** (w szczególności: „dywizor Weila”, „dywizor główny”, „snop dywizora”); „dzielnik” jest również używanym odpowiednikiem ang. *divisor*. Konwencje terminologiczne mogą współistnieć bez zmiany treści twierdzeń. Nie wykonuje się automatycznej zamiany ani ponownych audytów ALG-03/04 wyłącznie z tej przyczyny. Historyczny opis odkrycia z audytu II zachowano dla przejrzystości, lecz **jego rekomendacja migracji oraz wskazana blokada są anulowane**. Zob. [niezależny audyt globalny III](2026-11-22-ALG-GLOBAL-iteration-03.md).
