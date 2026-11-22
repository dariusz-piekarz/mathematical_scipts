# Logika matematyczna i teoria mnogości — audyt IV rozdziału 37 (dodatkowy audyt potwierdzający)

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex.  
**Blob rozdziału:** 3e0ae67b1b6a9abb5a4ff93691a2947d207647c4, bez zmian po poprawkach audytu I.  
**Werdykt matematyczno-redakcyjny:** czysty; audyt potwierdzający nie ujawnił kolejnej koniecznej poprawki. Pełne domknięcie stabilności zależy od wyniku przebiegów CI dla audytów II–IV.

## 1. Kontrola przypadków granicznych i kwantyfikatorów

1. **Kardynały małe.** ω jest regularny i silnie graniczny, lecz nie jest objęty definicją dużego kardynału, gdyż jawnie zakładamy nieprzeliczalność. Wniosek silnie nieosiągalny ⇒ graniczny kardynał wymaga nierówności λ^+≤2^λ; nie wystarczy stwierdzenie 2^λ>λ.
2. **Poziomy hierarchii.** Dla α=0 nie występuje żadna trudność w indukcji; przy następniku wystarcza silna graniczność, przy limicie potrzebna jest regularność. W dowodzie ZFC w V_κ wszystkie parametry i świadkowie formuł są elementami zbiorowej struktury, więc nie używa się niedefiniowalnej globalnej prawdy uniwersum. Zbiór wszystkich wartości funkcji z dziedziny a jest mały, bo |a|<κ; tylko to pozwala umieścić go w jednym poziomie V_β dla β<κ.
3. **Filtr właściwy a ultrafiltr.** Przecięcie mniej niż κ elementów miary należy do miary, a dopełnienia singletonów są duże. Sama zwykła skończona zupełność na ω nie dowodzi mierzalności. Kontrprzykład z ogonami A_n⊆ω ma wszystkie A_n w niegłównym ultrafiltrze i puste przecięcie.
4. **Niekanoniczni reprezentanci ultraproduktu.** Definicja równoważności modulo U pozwala zmieniać funkcję na zbiorze indeksów o dopełnieniu dużym. Zbiór wartości funkcji f może być pusty, dlatego w ograniczeniu zakresów g uwzględniono także zbiór pusty. Kodowanie reprezentantami Scotta obejmuje klasowy charakter ultraproduktu i nie zakłada istnienia klasy wszystkich funkcji jako zbioru.
5. **Zupełność w krytycznych miejscach.** Do przejścia od rozbicia indeksów na <κ włókien do jednego dużego włókna trzeba *ultrafiltrowości* oraz κ-zupełności; nie wystarcza sam filtr. Podobnie przy przecinaniu A_n dla n<ω potrzeba κ>ω. Wszystkie te założenia są jawne.
6. **Funkcja identycznościowa.** W ogólności nienormalny ultrafiltr nie daje równości obrazu [id] z porządkowym κ po kolapsie. Tekst wykorzystuje tylko nierówności α<[id]<j(κ), co wystarcza do wyznaczenia punktu krytycznego.
7. **Normalność.** Funkcje regresywne w punkcie 0 nie mają wymogu f(0)<0; punkt ten usuwa się z dziedziny bez zmiany członkostwa w niegłównym ultrafiltrze. W przecięciu diagonalnym kwantyfikator ma zakres ξ<α, nie ξ≤α. Dzięki temu obydwa kierunki charakterystyki są poprawne.
8. **Wniosek o niesprzeczności.** ZFC dowodzi implikacji z istnienia nieosiągalnego do Con(ZFC), ale nie dowodzi samej niesprzeczności bez warunku. Drugi Gödel jest użyty wyłącznie do wykluczenia dowodliwości istnienia nieosiągalnego przez niesprzeczną ZFC. Nie wprowadzono nieuprawnionego wniosku Con(ZFC) ⇒ Con(ZFC + istnieje nieosiągalny).

## 2. Niezależna ponowna ocena kompozycji

Rozdział prowadzi od pojęć dostępnych w rozdziałach 25–28 do konstrukcji opartej na ZFC, a następnie do ultraproduktów, zanurzeń i miar normalnych. Nie powiela pełnej konstrukcji modeli wymuszania z rozdziałów 32–36. Terminologia „suma zbiorów”, „zbiór pusty”, „przecięcie diagonalne” i polskie formy nazw są zgodne ze standardem. W tekście nie ma nieuprawnionego postulatu istnienia mierzalnego kardynału.

Inwentarz źródła bez zmian: **775 wierszy; 26 etykiet; 18 odsyłaczy; 7 definicji; 4 lematy; 7 twierdzeń; 1 wniosek; 5 uwag; 1 przykład; 12 dowodów.** Zachowano nazwy etykiet i odpowiedni odczyt \ref w książce. Rzeczywisty PDF z przebiegu 45066748548: **326 stron A4**, rozdział 37 na stronach **321–326**. Wszystkie sześć stron obejrzano w montażu; brak zaobserwowanych błędów składu; log 0 overfull, 0 unresolved reference, 1 underfull.

## 3. Warunek stabilności

**Audyt I — nieczysty, poprawki wykonane. Audyt II — czysty merytorycznie. Audyt III — czysty merytorycznie. Audyt IV — czysty merytorycznie (potwierdzający).** Wszystkie audyty II–IV dotyczą identycznego bloba źródła. Przed wystawieniem końcowego statusu **STABILNY (2/2+1)** należy potwierdzić ukończenie pełnych testów GitHub Actions dla poprawionych testów rozdziału 37 i audytu IV. Następne rozszerzenia (kardynały Mahla, słabo zwarte i superzwarte) pozostają osobną propozycją, nie są dopisywane podczas audytów stabilnego rozdziału. Kompilacja LaTeX i Python nie oznacza weryfikacji w Lean.
