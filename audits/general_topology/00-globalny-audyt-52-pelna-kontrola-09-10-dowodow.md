# Topologia ogólna — globalny audyt 52: pełna niezależna kontrola 10 dowodów rozdziału 09

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Badany plik:** `chapters/pl/general_topology/09-aksjomaty-przeliczalnosci.tex`, niezmieniony blob `f483271af93842198c094c95f73a68584e835215`.

## Metoda

Ponownie odczytano wszystkie **10 środowisk `proof`** wraz z twierdzeniami, definicjami i istotnymi przykładami. Niezależnie weryfikowano wybór przeliczalnych rodzin, hipotezę metryzowalności, przenoszenie własności na podprzestrzenie, puste przestrzenie oraz ścisłość kontrprzykładów. W szczególności rozdzielono pierwszy/drugi aksjomat przeliczalności, ośrodkowość i własność Lindelöfa. Nie zmieniono tekstu źródłowego ani testów.

## Dowód po dowodzie

| ID | Etykieta i początkowy wiersz proof | Kontrola matematyczna |
|---|---|---|
| 09-01 | `thm:topog-druga-pierwsza`, 44 | Dla co najwyżej przeliczalnej bazy globalnej 𝓑 podrodzina 𝓑_x={B∈𝓑:x∈B} jest bazą otoczeń x. Każde otoczenie N, choćby nieotwarte, zawiera otwarty U z x∈U⊂N, a ten zawiera bazowe B. Nie potrzeba założeń oddzielania; dla X=∅ warunek punktowy jest pusty. |
| 09-02 | `thm:topog-przeliczalnosc-dziedziczenie`, 80 | Względne bazy otoczeń to {N∩A} dla a∈A, a baza topologii podprzestrzeni to {B∩A}. W obu przypadkach przeciwobrazy otwartości mają prawidłowe kierunki inkluzji i liczba elementów nie rośnie. Dla A=∅ oba aksjomaty zachodzą. |
| 09-03 | `thm:topog-druga-iloczyn-przeliczalny`, 105 | Cylindry zależne od skończonego F⊂I tworzą bazę topologii iloczynu. Rodzina skończonych F w przeliczalnym I jest przeliczalna, a skończone produkty przeliczalnych baz również. Przeliczalna suma tych zbiorów parametrów jest przeliczalna. Niezależny wybór baz indeksowanych przeliczalnym I jest zgodny z ZFC; pusty czynnik i I=∅ rozpatrzone. |
| 09-04 | `thm:topog-druga-osrodkowa-lindelof`, 177 | Z każdej niepustej bazowej B∈𝓑 wybiera się x_B, co daje przeliczalny gęsty D. Dla pokrycia otwartego 𝓤 każdemu B⊂U z 𝓑' przypisuje się pokrywający U_B∈𝓤; każda x leży w takim B, więc {U_B} jest przeliczalnym podpokryciem. Wybory dotyczą co najwyżej przeliczalnych rodzin i są dopuszczone w przyjętym ZFC. |
| 09-05 | `thm:topog-osrodk-lindelof-zachowanie`, 229 | Ośrodkowość przechodzi na *otwarte* U, bo W=V∩U jest wtedy również otwarty w X; nie wyciąga się błędnego wniosku dla zamkniętych podprzestrzeni. Dla ciągłej surjekcji obrazy gęstych przeliczalnych podzbiorów są gęste, a pokrycie Y ściąga się na X. Domknięte F w Lindelöfowym X: do otwartego pokrycia F dodaje się X\F; przeliczalna suma podprzestrzeni Lindelöfa jest Lindelöfa przez wybór podpokryć poziomami. |
| 09-06 | `thm:topog-metryczne-trzy-warunki`, 304 | Dla metrycznej ośrodkowej X kule o wymiernych dodatnich promieniach i środkach w przeliczalnym gęstym D tworzą bazę, bo z d(x,a)<ε/4 można wybrać d(x,a)<r<ε−d(x,a). Drugi aksjomat daje ośrodkowość i Lindelöfa z poprzedniego twierdzenia. Dla metrycznej Lindelöfa każde pokrycie przez kule B(x,1/n) ma przeliczalną rodzinę środków D_n; D=∪D_n jest gęsty dzięki 1/n<ε. X=∅ nie tworzy wyjątku. |
| 09-07 | `cor:topog-osrodkowa-metryczna-baza`, 351 | Q^n jest przeliczalny i gęsty w R^n, więc przestrzeń euklidesowa spełnia wszystkie trzy metryczne warunki. Dziedziczenie drugiego aksjomatu oraz metryzowalności każdej podprzestrzeni R^n pozwala ponownie użyć równoważności dla dowolnego A⊂R^n. |
| 09-08 | `thm:topog-sorgenfrey-wlasnosci-przeliczalnosc`, 406 | Baza otoczeń x to [x,x+1/n); Q jest gęsty, bo każdy bazowy przedział zawiera przedział euklidesowy (a,b). Drugi aksjomat dawałby iniekcję R→N przez najmniejszy bazowy B_n zawarty w [x,x+1). Lindelöf: dla pokrycia 𝓤 konstruuje się G jako sumę (a,b) dla bazowych [a,b)⊂U∈𝓤; G ma euklidesowe przeliczalne podpokrycie. Dla F=R\G każdemu x przypisuje się pierwszą wymierną q_x>x z [x,q_x)⊂U; x<y∈F ⇒ q_x≤y<q_y, czyli iniekcja F→Q. Wybór po jednym U na każdy z przeliczalnych składników pokrywa całą S. Wartości graniczne a=x i niepustość F są obsłużone. |
| 09-09 | `cor:topog-sorgenfrey-trzy-nie-druga`, 477 | Prosta Sorgenfreya stanowi pojedynczy przykład spełniający pierwszy aksjomat, ośrodkowość i Lindelöfa, ale nie drugi. Dodatkowa hipoteza T2 jest spełniona: przy x<y rozłączne otoczenia [x,y),[y,y+1) rozdzielają parę. |
| 09-10 | `prop:topog-przeliczalnosc-hierarchia`, 617 | Trzy implikacje od drugiego aksjomatu wynikają z pierwszego i czwartego dowodu. Ścisłość: nieprzeliczalna dyskretna jest pierwszoaksjomatowa, ale nie ośrodkowa ani Lindelöfa; nieprzeliczalna koskończona jest ośrodkowa i Lindelöfa, lecz nie ma pierwszego aksjomatu; S ma wszystkie trzy, ale nie drugi. S×S jest ośrodkowa i spełnia pierwszy, ale nie Lindelöfa; uzwarcenie Aleksandrowa nieprzeliczalnej dyskretnej jest Lindelöfa i nieośrodkowe. Przykłady łącznie wykluczają równoważności parami. |

## Kontrole przykładów o wysokim ryzyku

- **Prosta Sorgenfreya:** rozróżniono topologię Sorgenfreya od euklidesowej w dowodzie własności Lindelöfa. Wydzielony G ma zwykłą topologię euklidesową i przeliczalne podpokrycie; dla F iniekcja x↦q_x jest oparta na ścisłym `x<q_x` i na fakcie `(x,q_x)⊂G`, więc nie zakłada dyskretnie żadnego przeliczalnego wyboru punktów nieprzeliczalnego F.
- **Płaszczyzna Sorgenfreya:** domknięty zbiór D={(t,−t):t∈R} jest nieprzeliczalny i dyskretny w S×S; gdyby S×S było Lindelöfa, jego domknięta podprzestrzeń D również byłaby Lindelöfa, sprzeczność. Jednocześnie Q² jest gęsty, co pokazuje, że ośrodkowość nie implikuje własności Lindelöfa poza klasą przestrzeni metrycznych.
- **Uzwarcenie Aleksandrowa nieprzeliczalnej przestrzeni dyskretnej:** E∪{∞} jest zwarte i Hausdorffa, gdy otoczenia ∞ mają skończone dopełnienie w E; E jest otwartą nieprzeliczalną podprzestrzenią dyskretną, dlatego nie jest Lindelöfa. Ponadto każdy gęsty zbiór w E∪{∞} musi zawierać całe E, więc X nie jest ośrodkowa.
- **Topologia koskończona:** na nieprzeliczalnym X każdy przeliczalny nieskończony zbiór jest gęsty, każdy niepusty zbiór otwarty pozostawia skończone dopełnienie, a pierwszy aksjomat przeliczalności zawodzi: dla hipotetycznej przeliczalnej bazy otoczeń punktu x można znaleźć y≠x należący do wszystkich jej członów, choć X\{y} jest otoczeniem x.

## Wynik i status pełnego rejestru

**10/10 dowodów — PASS.** Wszystkie oznaczenia `09-01…09-10` otrzymały osobną ocenę i odpowiadają aktualnym etykietom źródła z macierzy 33. Przypadki brzegowe i kierunki wszystkich implikacji są zgodne z deklarowanymi hipotezami. Brak koniecznej edycji LaTeX.

Po raporcie 51 poziom pełnej indywidualnej dokumentacji wynosił **226/325**. Ten raport daje **236/325**. Pozostają **89** dowodów: rozdziały 10–13 (**45**) i 24–26 (**44**). Rozdziały 01–09 mają teraz kompletne indywidualne wpisy (raporty 46,47,49,40–41,50–52), a 14–23 były udokumentowane wcześniej w raportach globalnych 15–25 z potwierdzeniem zmian 21 w 39–41.

Wersja źródłowa rozdziału 09 pozostaje niezmieniona. CI nowego raportu należy zaobserwować osobno; sukces indeksu czy testów nie jest formalnym matematycznym dowodem. Następny etap: rozdział 10 (14 dowodów) przed 11–13. Automatyzacja audytów pozostaje aktywna.
