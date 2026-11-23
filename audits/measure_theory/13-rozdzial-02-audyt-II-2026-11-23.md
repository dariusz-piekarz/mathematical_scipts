# Teoria miary / Miara i całka — rozdział 02, niezależny audyt II (iteracja globalna XIII)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Zakres:** wyłącznie `chapters/pl/measure_theory/02-miary-i-ich-podstawowe-wlasnosci.tex` (796 linii; blob `b48e368acfa0b8fffaeed59f7d33ad5ab75a3d20`). Inne pliki wyłącznie dla kontekstu odsyłaczy i kompilacji.

## Stan faktyczny przed audytem

Odczytano HEAD `5c441354a822f8bc079ee5616918c66f41fece85`, katalog raportów 01–12, najnowszy raport `12-rozdzial-02-audyt-I-2026-11-23.md`, bieżący R02, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/measure_theory.tex`, `books/pl/integration_theory.tex` i workflow R02. Rozdział 01 pozostaje stabilny, R02 po audycie I jeszcze nie był certyfikowany. Nie zmieniano źródeł R01, R03 ani pozostałych rozdziałów.

## Niezależny przegląd matematyczny

Powtórnie, bez przyjmowania poprzedniego raportu za dowód, sprawdzono dziewięć sekcji, 10 twierdzeń, 2 wnioski, 8 definicji, 14 przykładów, 8 uwag i 14 dowodów. Poniższe kontrole dotyczą osobnych potencjalnych miejsc awarii:

1. **Definicja miary i przykłady.** Dla miary Diraca nie trzeba mierzalności singletonu, ponieważ sprawdzana jest przynależność punktu do mierzalnych zbiorów. Miara przeliczalno-koprzeliczalna jest jednoznacznie określona dla nieprzeliczalnego X. Miara licząca na nieskończonym X jest dopuszczalna, a w sumie miar dyskretnych z wagami nieujemnymi można zamienić szeregi bez założenia ich zbieżności.
2. **Podaddytywność i różnica.** Rozłącznienie `B_n=A_n\\setminus\\bigcup_{k<n}A_k` daje sumę dokładnie równą sumie `A_n`. Odejmowanie `\\mu(B)-\\mu(A)` występuje wyłącznie przy `\\mu(A)<\\infty`.
3. **Ciągłość miary.** Ciągłość z dołu nie wymaga skończoności; ciągłość z góry wymaga skończoności co najmniej jednego wyrazu. Kontrprzykład ogonów N z miarą liczącą jest poprawny. Dowody nierówności dla liminf/limsup jawnie używają odpowiedniej monotoniczności i w drugiej nierówności skończoności całej miary.
4. **Borel–Cantelli.** Pierwsza część nie zakłada miary probabilistycznej ani niezależności; wniosek wynika z oszacowania przez ogony zbieżnego szeregu.
5. **Klasy miar.** Implikacja `skończona ⇒ σ-skończona ⇒ półskończona` jest uzasadniona, podobnie kontrprzykłady. Użycie własności Lindelöfa przy lokalnej skończoności wymaga przeliczalnej bazy i jest poprawne.
6. **Uzupełnienie.** Dla dwóch par świadków `A_i⊆E⊆B_i` nierówności obu kierunków pokazują niezależność wartości miary również przy nieskończoności. Dla dopełnień zamieniają się świadkowie, dla sum wystarcza przeliczalna podaddytywność zbiorów miary zero. W dowodzie zupełności `μ(B)=0` wynika z `μ(A)=0` i `μ(B\\setminus A)=0`. Minimalność jest wykazana bez odwoływania się do nieudowodnionego faktu.
7. **Operacje i jednoznaczność.** Wspólne wyczerpanie `E_n∈P` z `μ(E_n)=ν(E_n)<∞` umożliwia zastosowanie skończonego twierdzenia π–λ do miar ograniczonych. Przykład `μ=\\#`, `ν=2\\#` rzeczywiście przeczy jednoznaczności bez tego warunku, nawet gdy generator składa się z przedziałów o końcach wymiernych.
8. **Atomy.** Definicja dopuszcza atom o nieskończonej mierze przy niespełnionej σ-skończoności; dowód skończoności masy atomów σ-skończonych poprawnie używa `A∩E_n`. Dowód przeliczalności rozłącznych atomów sprowadza rodzinę do przeliczalnej sumy skończonych klas `I_{n,k}` i wykorzystuje `m/k≤μ(E_n)`, bez ukrytej hipotezy skończoności całej przestrzeni.

**Rezultat:** w tym drugim przeglądzie nie znaleziono nowego wykazanego błędu matematycznego, brakującego koniecznego założenia ani nieuprawnionej operacji z `∞`. Brak zmian treści R02; nie dodano nowych twierdzeń ani przykładów.

## Kontrola redakcyjna i LaTeX

R02 ma 34 unikatowe etykiety, 17 odsyłaczy, 67 poprawnie sparowanych środowisk i dziewięć sekcji. Trzy różne cele odsyłaczy do R01 istnieją w R01; R02 jest włączony do `books/pl/measure_theory.tex`. Nie znaleziono `\\mathbf{1}`, `\\mathbb{1}`, `\\mathds{1}`; funkcje charakterystyczne mają postać `\\chi_A`. Terminologia nie zawiera niedozwolonej „zbieżności zdominowanej”. R02 nie ma rysunków ani podpisów rysunków. Z poprzedniego audytu istnieje realna wizualna inspekcja wszystkich ośmiu stron PDF i potwierdzenie czterech hiperłączy do R01 w pełnej książce. Nie przedstawia się tych starszych przebiegów jako nowych testów.

## Nowy, mierzalny postęp: niezależne testy wyczerpujące

Dodano plik `tools/test_measure_theory_ch02_finite_models.py` (commit `511232b70dd9b31996add7a4b84c71238ea032bf`) i podłączono go do `.github/workflows/measure-theory-ch02.yml` (commit `130318688447181453f2c2e30d06a2f2899f1af4`).

Nowy test bada wszystkie **256** miary wagowe na czteropunktowej przestrzeni, z wagami w `{0,1,2,∞}`, sprawdzając **65 536 par podzbiorów** pod względem monotoniczności, podaddytywności, skończonej addytywności i poprawnego odejmowania przy skończonej mierze. Sprawdza także **309** par (σ-algebra wyznaczona podziałem czteropunktowego zbioru, miara o wagach bloków w `{0,1,2}`) oraz ich uzupełnienia: domknięcie, addytywność, zupełność i zgodność z miarą początkową.

Przed zapisem wykonano test lokalnie: `PASS: 256 measures, 65536 subset pairs` oraz `PASS: 309 partition-algebra/measure completions`. Ponownie odczytano z GitHub skrypt (blob `92f7d64a03935e49c26c7bef723ae7ad09b7e7a1`) i workflow (blob `331657e8a3373e4a0c136869c996c3b40b5ff9d8`). **Należy niezależnie potwierdzić końcowy wynik nowego przebiegu GitHub Actions [45133163263](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133163263)**, uruchomionego na commicie `130318688447181453f2c2e30d06a2f2899f1af4`.

## Status i dalsze kroki

**R02: DRUGI NIEZALEŻNY AUDYT MATEMATYCZNY CZYSTY; STABILIZACJA WARUNKOWA DO KOŃCOWEGO WYNIKU CI.** Brak zmian w treści rozdziału od audytu I, a więc jest to dodatkowy czysty audyt po ostatniej poprawce źródła. Matematyka, redakcja, odsyłacze i dotychczasowa wizualna kontrola PDF są pozytywne. Przed ostatecznym oznaczeniem rozdziału jako stabilny trzeba odczytać wyniki nowego CI na dokładnym commicie i sprawdzić brak regresji. Jeżeli wszystkie zadania przejdą, można zapisać certyfikat stabilności R02 w następnej iteracji; dopiero po nim wolno przejść do R03.
