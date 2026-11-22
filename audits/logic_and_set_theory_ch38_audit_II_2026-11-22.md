# Logika matematyczna i teoria mnogości — audyt II rozdziału 38

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/38-kardynaly-mahla-i-slaba-zwartosc.tex.  
**Blob:** d0d176bf1d4cbb8426cedcf02fbbd3a28510a152 — niezmieniony od dodania rozdziału i audytu I.  
**Werdykt merytoryczny:** bez nowych koniecznych poprawek, kandydat na pierwszy czysty audyt (1/2). Ostateczne zaliczenie wymaga zielonego pełnego CI.

## 1. Odrębna kontrola twierdzeń o klubach

Definicja domknięcia stosuje wyłącznie niezerowe graniczne liczby porządkowe. Dla przecięcia μ<κ klubów w kroku rekurencji wartość supremum z μ punktów pozostaje <κ dzięki regularności. Każdy wybrany punkt dξ(β_n) leży między β_n a β_{n+1}, więc dla danego ξ ciąg tych punktów jest współkońcowy w δ=sup_n β_n; z domknięcia δ∈Cξ. Podobnie w przecięciu diagonalnym wybór γ_{n+1} w przecięciu Cξ dla ξ≤γ_n zapewnia, że wszystkie późniejsze wyrazy należą do ustalonego Cξ, ilekroć ξ<sup γ_n. Nie zastąpiono nierówności ξ<α przez ξ≤α.

Dowód Fodora ponownie sprawdzono przez zaprzeczenie tezy, wybór klubów rozłącznych z włóknami i przecięcie diagonalne. Istotny moment jest zapisany: dla α∈S∩D, ξ=f(α)<α, z definicji D wynika α∈Cξ, a z przynależności do włókna α∉Cξ. Nie ma niedozwolonej dedukcji, że każdy nieograniczony podzbiór κ jest stacjonarny.

## 2. Odrębna kontrola drzew i zanurzeń

Własność drzewa wymaga węzłów na wszystkich poziomach drzewa κ-owego, nie tylko niezliczonego łańcucha na wybranych poziomach. Jeżeli w M drzewo j(T) ma wysokość j(κ)>κ, to istnieje węzeł poziomu κ, a jego ścisłe poprzedniki mają unikalne wysokości α<κ. Wartość j(T_α) równa się poziomowi α, ponieważ j(α)=α. Przy |T_α|<κ odpowiedni poziom składa się dokładnie z obrazów s∈T_α, co wynika z surjekcji μ→T_α i elementarności j. Zachowanie porządku daje spójne s_α, a definiowalność j wraz z zastępowaniem pozwala zebrać gałąź do jednego zbioru w V. Przejście od mierzalności do słabej zwartości wymaga także nieosiągalności udowodnionej w rozdziale 37, jawnie przywołanej w tekście.

## 3. Odrębna kontrola stacjonarności nieosiągalnych

Lemat o przynależności klubów do miary normalnej jest niezależny od zanurzenia j: dla dopełnienia C dużego definiuje się f(α)=sup(C∩α) na dużym ogonie. Domkniętość C wymusza f(α)<α. Normalność daje stały obraz na dużym zbiorze B; nieograniczoność C i B prowadzi do sprzeczności.

W drugim kroku sprawdzono wewnętrzną nieosiągalność κ w M. Jeśli M uważałby κ za singularny albo niekardynalny, istniałoby świadectwo w V, sprzeczne z regularnością κ jako kardynału V. Jeśli M naruszałoby silną graniczność przy λ<κ, w M można by skonstruować iniekcję κ→P^M(λ) ⊆ P^V(λ), sprzeczną z mocą zbioru potęgowego λ w V. W M zatem κ jest nieosiągalny i należy do j(Iκ), stąd Iκ ma miarę jeden, a wobec przynależności wszystkich klubów do tej samej miary jest stacjonarny.

## 4. Kolorowania par

Dla każdego α jedno z dwóch rozłącznych B_{α,0}, B_{α,1} jest w ultrafiltrze, ponieważ ich suma zbiorów jest ogonem w ultrafiltrze. Jeden z dwóch kolorów występuje na U-dużym zbiorze indeksów. Przy kroku ξ<κ rekurencji przecina się ξ+1 zbiorów U-dużych; κ-zupełność daje niepustość, uniformność daje nieograniczoność. Zbiór wybranych liczb porządkowych jest ściśle rosnący i ma moc κ. Wszystkie jego pary otrzymują ten sam kolor. Normalność U nie jest do tego dowodu potrzebna.

## 5. Inwentarz i testy

Niezmieniony plik: **641 wierszy, 26 etykiet, 19 odsyłaczy, 8 definicji, 4 lematy, 5 twierdzeń, 1 wniosek, 5 uwag, 2 przykłady, 10 dowodów**. Sprawdzone etykiety są unikalne, środowiska TeX prawidłowo sparowane. W katalogu jest 38 rozdziałów; workflow oczekuje 952 etykiet i 738 odsyłaczy. W nowym przebiegu [CI 45068706353](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068706353) dziewięć testów rozdziału 38 zakończyło się sukcesem; ukończenie pełnego składu i inspekcję PDF trzeba potwierdzić odrębnie.

## 6. Werdykt

**Matematycznie czysty**, bez zmian źródła. Po pozytywnym wyniku pełnego CI może być zaliczony jako **pierwszy czysty audyt (1/2)**. Następnie audyt III na tym samym źródle oraz audyt IV potwierdzający. Opcjonalne rozszerzenia dotyczące logiki infinitarnej i charakterystyki słabej zwartości wymagają osobnej decyzji; nie dopisywać ich podczas audytów. Skończone testy Ramseyowskie i LaTeX nie zastępują dowodów w Lean.
