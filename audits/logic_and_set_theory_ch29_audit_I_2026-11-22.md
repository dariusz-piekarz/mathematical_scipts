# Logika matematyczna i teoria mnogości — rozdział 29, audyt I

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/29-slabsze-zasady-wyboru-i-ich-ograniczenia.tex`.

## Integracja i weryfikacja źródeł

Zintegrowano biblioteczny plik `29-weaker-choice-principles.tex` z pełniejszą wersją książki `logika_teoria_mnogosci_iteracja_79.pdf` (fizyczne strony PDF 233–239). Obecny TeX pomijał istotną sekcję: **twierdzenie Baire'a dla zupełnych przestrzeni metrycznych przy DC**, przykład niespełniania tezy bez zupełności i uwagę o dokładnej roli wyboru zależnego. Sekcję przywrócono z pełnymi dowodami.

Przy analizie wykryto matematyczną lukę oryginalnego dowodu w PDF: jeśli `B(z_{i+1},r_{i+1}) ⊂ B(z_i,r_i)∩D_{i+1}`, to granica ciągu środków musi należeć jedynie do **kuli domkniętej**, która niekoniecznie zawiera się w `D_{i+1}`. Naprawiono konstrukcję, wymagając **domkniętej** kuli `{x:d(x,z_{i+1})≤r_{i+1}}` zawartej w poprzedniej otwartej kuli i `D_{i+1}`. Zapewniono jednocześnie małe wymierne promienie. Dowód przejścia do granicy jest dzięki temu poprawny także w ogólnych przestrzeniach metrycznych, gdzie domknięcie topologiczne kuli otwartej może być mniejsze niż wskazana kula domknięta.

Rozwinięto skrótową definicję algebry Boole'a, jawnie podając działania, ich dziedziny, prawa pochłaniania i oba prawa rozdzielności. W dowodzie UF ⇒ BPI uzupełniono argument o atomie skończonej algebry i sprawdzeniu, że wartość `h_D` zachowuje dopełnienie oraz przecięcie. W BPI ⇒ UF osobno potraktowano zbiór pusty, dla którego `P(∅)` jest trywialną algebrą bez właściwych filtrów.

Pozostawiono oryginalną całość materiału o AC, DC, ACω, BPI, ultrafiltrach, dwóch wersjach Tychonoffa i lemacie Teichmüllera–Tukeya. **Inwentarz rozdziału:** 6 definicji, 7 twierdzeń, 1 lemat, 5 przykładów, 7 uwag, 8 dowodów; 24 etykiety. W pierwszym przebiegu 10 odsyłaczy.

**Werdykt:** integracja wykonana; po rzeczywistej korekcie twierdzenia Baire'a potrzebny dalszy audyt, testy i kontrola PDF.
