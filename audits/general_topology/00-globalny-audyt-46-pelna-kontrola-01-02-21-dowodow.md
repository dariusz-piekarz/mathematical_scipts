# Topologia ogólna — audyt globalny 46: pełny niezależny przegląd 21 dowodów rozdziałów 01–02

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Badane bloby:** 01: `1e8ee853eb9915d96913e5a0a8cdb5e32f2ec5f6`; 02: `53a8dc7e62590a9011bd5858eedb4141c5f38162`. Wersje te są identyczne z obecną gałęzią i wcześniejszym rejestrem 325/325. **Brak zmian źródłowych.**

## Zakres, standard i ograniczenie

Odczytano ponownie **pełny tekst każdego z 9 + 12 = 21 środowisk `proof`**, z hipotezami twierdzeń bezpośrednio nad dowodami, bez korzystania z oceny „PASS” w dotychczasowych krótkich lokalnych raportach 2+1. Każdy wiersz poniżej jest przypisany do jednej etykiety z macierzy globalnej 33. Kontrola obejmuje wszystkie istotne implikacje, przypadku brzegowe i ewentualne potrzeby aksjomatów oddzielania. **Nie jest to ponowna kontrola wszystkich przykładów i ilustracji ani formalizacja 21 dowodów w Lean.**

## Rozdział 01: wszystkie 9 dowodów — PASS

| ID w macierzy | Etykieta | Rzeczywista kontrola matematyczna |
|---|---|---|
| 01-01 | `prop:topog-kule-otwarte-sfery-domkniete` | Funkcja `d(x,·)` jest 1-Lipschitz na skutek odwrotnej nierówności trójkąta. Dla `d(x,y)<r` promień `r-d(x,y)>0` mieści kulę w kuli; dla `d(x,y)>r` promień `d(x,y)-r` mieści otoczenie poza kulą domkniętą; dla `d(x,y)≠r` promień `|d(x,y)-r|` wyklucza sferę. W każdym przypadku nierówność jest ścisła. |
| 01-02 | `prop:topog-topologia-metryczna` | Suma zbiorów otwartych wybiera jeden element pokrycia zawierający x; dla dwóch otwartych zbiorów promień minimum dwóch dodatnich promieni wystarcza. Pusta suma i puste przecięcie są poprawnie opisane, w tym X=∅. |
| 01-03 | `prop:topog-zbiory-domkniete` | Prawa de Morgana zamieniają dowolne przecięcia zbiorów domkniętych na otwarte sumy, a skończone sumy domkniętych na skończone otwarte przecięcia. Odwrotna konstrukcja topologii przez dopełnienia rodziny domkniętych zachowuje aksjomaty, a jednoznaczność jest natychmiastowa. |
| 01-04 | `prop:topog-otoczenia` | Otoczenie nie musi być otwarte, lecz zawiera otwarty zbiór V punktu x. Część (iv) wymaga wyboru M=V, wtedy **każdy** y∈M ma N jako otoczenie. Charakterystyka otwartości przez otoczenia jest poprawna, również dla U=∅. |
| 01-05 | `thm:topog-kryterium-bazy` | B1 wymusza pokrycie X, a B2 daje w każdym punkcie bazowy fragment przecięcia dwóch bazowych U,V. Po zsumowaniu **wszystkich** elementów bazy zawartych w U∩V uzyskuje się przecięcie otwarte, bez arbitralnego wyboru funkcji dla wszystkich punktów. Przy X=∅ warunki są puste i jedyna topologia jest poprawnie wygenerowana. |
| 01-06 | `prop:topog-otwartosc-przez-baze` | W obu kierunkach równoważność wynika z faktu, że każdy U otwarty jest sumą bazowych B⊂U. Dla U=∅ warunek „dla każdego x∈U” zachodzi pusto, a ∅ należy do każdej topologii. |
| 01-07 | `thm:topog-podbaza-konstrukcja` | Włączenie **pustego przecięcia równego X** zapewnia B1 nawet gdy podbaza nie pokrywa X. Rodzina skończonych przecięć jest zamknięta na przecięcia i spełnia B2. Dowolna topologia zawierająca podbazę zawiera wszystkie skończone przecięcia i sumy, co daje minimalność. |
| 01-08 | `prop:topog-porownanie-bazy` | Jeżeli wszystkie elementy bazy τ₁ są otwarte w τ₂, to każda ich suma jest otwarta w τ₂. Ponowna charakteryzacja przez bazę τ₂ sprawdza warunek `∀B∈𝓑₁ ∀x∈B ∃C∈𝓑₂` bez odwrócenia kierunku inkluzji topologii. |
| 01-09 | `thm:topog-przeciecia-topologii` | Przecięcie niepustej rodziny topologii zawiera ∅ i X oraz jest zamknięte na sumy dowolne i przecięcia skończone. Dla pustej rodziny topologii przecięcie **z definicji wynosi 𝒫(X)**, także dla X pustego. Klasa topologii zawierających dowolną podbazę S jest niepusta dzięki 𝒫(X), co domyka dowód istnienia topologii generowanej. |

**Wynik rozdziału 01: 9/9 PASS.** W definicjach bazy i podbazy nie potrzeba T1, wyboru ani niepustości X. Nie dodano niepotrzebnych hipotez.

## Rozdział 02: wszystkie 12 dowodów — PASS

| ID | Etykieta | Rzeczywista kontrola matematyczna |
|---|---|---|
| 02-01 | `prop:topog-ekstremalne` | Wnętrze jest sumą **wszystkich** otwartych podzbiorów A, a domknięcie przecięciem **wszystkich** domkniętych nadzbiorów A. Własności ekstremalne i charakteryzacje zbiorów stałych wynikają bez założeń oddzielania. |
| 02-02 | `thm:topog-punktowa-charakteryzacja` | `x∉cl A` daje otwarte `X\cl A` rozłączne z A; odwrotnie otoczenie otwarte U rozłączne z A daje domknięty nadzbiór `X\U` niezawierający x. Uogólnienie na otoczenia nieotwarte wynika z istnienia zawartego w nich otwartego otoczenia. |
| 02-03 | `thm:topog-rachunek-wnetrz-domkniec` | Własności monotoniczności, idempotentności, `int(A∩B)=int A∩int B`, `cl(A∪B)=cl A∪cl B` wynikają z ekstremalności otwartych i domkniętych zbiorów. Dla `int(A∪B)` oraz `cl(A∩B)` twierdzenie słusznie podaje **inkluzje**, nie w ogólności równości. |
| 02-04 | `prop:topog-dualnosc-wnetrze-domkniecie` | `X\int A` jest domkniętym nadzbiorem dopełnienia A; każdy inny domknięty F⊃X\A zawiera `X\int A` z własności maksymalności wnętrza. Druga równość otrzymuje się przez podmianę A→X\A. |
| 02-05 | `thm:topog-charakteryzacja-brzegu` | `∂A=cl A∩cl(X\A)` daje symetrię względem dopełnienia i domkniętość brzegu. Przynależność punktowa wymaga spotykania A i dopełnienia przez **każde** otoczenie. Rozkład X na wnętrze, brzeg i zewnętrze jest rozłączny i wyczerpujący. |
| 02-06 | `prop:topog-brzeg-sumy` | Dowód przez kontrapozycję: jeśli x nie leży na żadnym brzegu, jest we wnętrzu albo w zewnętrzu każdego z A,B. Obecność we wnętrzu któregokolwiek daje wnętrze sumy; dwa zewnętrza dają zewnętrze sumy. Nie postuluje się błędnej równości brzegów sumy. |
| 02-07 | `thm:topog-domkniecie-pochodny` | Dla x∈cl A\A każda okolica spotyka A=A\{x}, więc x∈A'. Dla x∈A izolacja jest równoważna istnieniu otoczenia nieprzecinającego A\{x}. Stąd `cl A=A∪A'` i `Iso(A)=A\A'`, **bez hipotezy T1**. |
| 02-08 | `prop:topog-pochodny-monotoniczny` | Z inkluzji A\{x}⊂B\{x} wynika monotoniczność A'⊂B'. Dla równości pochodnego sumy, jeśli x nie należy do A' ani B', przecięcie dwóch odpowiednich otoczeń eliminuje `(A∪B)\{x}`. |
| 02-09 | `thm:topog-pochodny-t1` | Usunięcie singletonu x z otwartego U zachowuje otwartość **właśnie dzięki T1**. Wówczas U jest całe rozłączne z A'. Kontrprzykład z dwupunktową topologią antydyskretną pokazuje istotność hipotezy. |
| 02-10 | `thm:topog-gesty-kryteria` | Gęstość charakteryzuje spotykanie wszystkich niepustych otwartych zbiorów. Przy `int(cl A)=∅` zbiór `V=U\cl A` jest niepusty, otwarty i unika A; odwrotnie każdy otwarty V⊂cl A musi spotykać A. Dopełnienie cl A jest otwarte i gęste dokładnie przy nigdziegęstości A. Sprawdzono przypadek X=∅. |
| 02-11 | `prop:topog-nigdziegesty-sumy` | Monotoniczność domknięcia zabezpiecza podzbiory zbiorów nigdziegęstych. Dla skończonej sumy po wybraniu niepustego U usuwa się kolejno cl A, następnie cl B; każda reszta jest **otwarta i niepusta**, bo poprzedni zbiór jest nigdziegęsty. Indukcja daje dowolną skończoną rodzinę; suma pusta jest ∅. |
| 02-12 | `thm:topog-kuratowski` | Z (K3) wynika monotoniczność c; z (K2) oraz c(X)⊂X mamy c(X)=X. Zbiory stałe c(F)=F są zamknięte na przecięcia dowolne i sumy skończone. Dzięki (K4) c(A) jest najmniejszym stałym nadzbiorem A, zatem dokładnie domknięciem A w nowej topologii. Ostatni krok dowodzi jednoznaczności. |

**Wynik rozdziału 02: 12/12 PASS.** Sprawdzono również rzeczywisty, nie-Hausdorffowy kontrprzykład pokazujący, że zbiór pochodny może nie być domknięty bez T1.

## Wynik łączny i rzeczywisty stan dokumentacji

- **21/21 dowodów 01–02** ma teraz jawny, własny wiersz indywidualnej kontroli matematycznej. To inny zakres niż krótkie lokalne raporty stabilizacyjne 01/11 i 02/05, które weryfikowały wersję SHA i status, lecz nie wyliczały szczegółowo każdego proof.
- Macierz 325/325 z globalnych raportów 33–35 pozostaje zgodna z tym raportem: **identyczne etykiety, numery oraz bloby**; żaden dowód nie został usunięty ani dopisany.
- Niezależnie sprawdzono istniejące pełne audyty globalne **15,16,18–25** dla rozdziałów 14–23: **106/106** etykiet występuje w docelowym raporcie po indywidualnym numerze lub opisie, i dotyczą one tych samych aktualnych blobów (dla rozdziału 21 późniejszy cykl 39–41 potwierdza niezmienione proof po edycji TikZ). Sama obecność etykiety w raporcie nie stanowi formalnego certyfikatu matematycznej poprawności; dowody oceniano we wcześniejszych iteracjach.
- Zwykłe uruchomienie testów CI, statyczne sprawdzenie etykiet ani wizualny przegląd PDF **nie zastępują** powyższej matematycznej kontroli.
- **Nie dokonano edycji źródeł** i nie wykryto nowego błędu wymagającego zmiany tezy, definicji lub dowodu.

**Pozostała praca do finalnego globalnego PASS:** niezależnie rozbudować dokumentację dowód po dowodzie dla rozdziałów **03–13** i **24–26**, których wcześniejsze przeglądy mają także raporty zbiorcze oraz selektywne. Zachować historyczne SHA w starych raportach; ewentualne nowe bloby 06 i 21 są już udokumentowane w globalnym 41. Następnie sprawdzić CI końcowego HEAD na niezmienionych źródłach oraz ostatnią zgodność PDF. Automatyzacja pozostaje aktywna.
