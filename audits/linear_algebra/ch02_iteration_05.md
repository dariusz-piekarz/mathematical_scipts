# Algebra liniowa — rozdział 02, audyt 5

Data: 21 listopada 2026  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Rozdział: `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
Commit zmian merytorycznych: `99212a698a8b2a0d117a14328c814e653e45289e`

## Cel i kryterium

Audyt 5 obejmuje **tylko poprawność i ewentualne luki istniejącego materiału**; jego zakres jest zamknięty i nie należy dodawać kolejnych tematów, lematów ani twierdzeń bez realnej potrzeby. Sprawdzano kwantyfikatory, poprawność operacji na nieskończonych zbiorach indeksów, rolę aksjomatu wyboru, przypadki zerowe, argumenty dowodowe i terminologię.

## Zakres ponownej weryfikacji

Przeczytano wszystkie sekcje rozdziału:
1. Niepowtarzalność nośnika w bazie Hamela; oszacowanie mocy sumy zbiorów skończonych indeksowanej nieskończonym zbiorem; równoliczność baz skończonych i nieskończonych. Wykorzystane \(|I\times\mathbb N_0|=|I|\) i twierdzenie Cantora–Bernsteina są poprawnymi, świadomie importowanymi wynikami arytmetyki kardynalnej w ZFC, a nie nieudowodnionymi konsekwencjami algebry liniowej.
2. Suma algebraiczna podprzestrzeni i jej własność minimalności; wzór wymiarowy dla \(U+W\) z wyborem baz \(C\), \(C\cup A\), \(C\cup D\) i dowodem niezależności \(C\cup A\cup D\). Dodawanie wymiarów kardynalnych jest wykonane bez odejmowania.
3. Równoważne kryteria wewnętrznej sumy prostej, w tym pusty zbiór indeksów i rodziny o skończonym nośniku; konstrukcja zewnętrznej sumy prostej i jej bazy.
4. Równość warstw, dobrze określone działania w ilorazie, uniwersalna własność ilorazu i przykłady, także dla podprzestrzeni zerowej oraz całego \(V\).
5. Dopełnienia algebraiczne, przypadek skończenie wymiarowy bez aksjomatu wyboru, izomorfizm \(W\cong V/U\) i iloraz \(U/(U\cap W)\cong(U+W)/W\).

Nie stwierdzono nowego błędu obalającego tezy rozdziału. Znaleziono jednak niżej wymienione trzy niedokładności dotyczące już istniejących twierdzeń i przykładów.

## Poprawki

### 1. Zakres założenia aksjomatu wyboru we wzorze na wymiar ilorazu

W `thm:lin2-iloraz-dopelnienie` stwierdzenie łączyło rezultat ogólny udowodniony przy AC ze słowami „w przypadku skończenie wymiarowym powyższa równość daje...”. Pomimo osobnego dowodu skończonego, sformułowanie tezy mogło błędnie sugerować, że wzór skończenie wymiarowy nadal wymaga AC.

Zapisano wprost, że jeśli \(V\) jest skończenie wymiarowa, to \(U\) i \(V/U\) są skończenie wymiarowe oraz **bez aksjomatu wyboru** zachodzi
\[
\dim_K(V/U)=\dim_KV-\dim_KU.
\]
Wskazano, że dowód tego przypadku jest niezależny od argumentu ogólnego; sam dowód bez AC, dodany w poprzednim audycie, zachowano.

### 2. Wielomian zerowy w przykładzie podziału na potęgi parzyste i nieparzyste

Przykład `prz:lin2-parzyste-nieparzyste` korzystał z zapisu \(p=\sum_{j=0}^d a_jX^j\) bez określenia \(d\), co w przypadku wielomianu zerowego mogło sugerować nieistniejący stopień \(\deg 0\). Wskazano wyraźnie, że \(d\in\mathbb N_0\) jest po prostu dowolną górną granicą indeksów zapisu, a dla \(p=0\) przyjmujemy \(d=0\), \(a_0=0_K\). Nie przypisano stopnia zerowemu wielomianowi.

### 3. Jawne wskazanie ciała w tożsamościach wymiarowych

W dowodzie `thm:lin2-wzor-wymiarowy` zastąpiono skrócone symbole \(\dim U\), \(\dim W\) itp. pełnymi \(\dim_K U\), \(\dim_K W\), \(\dim_K(U+W)\), \(\dim_K(U\cap W)\). Dzięki temu tożsamości jednoznacznie dotyczą wymiarów nad ustalonym ciałem skalarów \(K\).

## Kontrola techniczna

- W obu rozdziałach pozostaje **108 unikalnych etykiet**: 69 w rozdziale 01 i 39 w rozdziale 02.
- Zweryfikowano 43 wystąpienia `\\ref` i `\\eqref`; **brak nierozwiązanych odsyłaczy**.
- Nie znaleziono niezgodnych lub niedomkniętych środowisk `\\begin` / `\\end`.
- W treści nie występują zakazane „unia” ani „relacja liniowa”; zachowano stabilne historyczne nazwy etykiet.
- Rozdziały nie zależą od zewnętrznych plików ilustracji.
- CI dla zmian: [44897797316](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44897797316) — status końcowy do potwierdzenia.
- Problemy globalnego walidatora innych książek Biblioteki są monitorowane oddzielnie i nie stanowią dowodu poprawności ani niepoprawności rozdziału 02.

## Status

**Audyt 5 zakończony z trzema precyzyjnymi poprawkami istniejącego materiału.** Pokrycia tematów nie rozszerzono. Rozdział 02 zostaje otwarty do kolejnego audytu poprawności, zgodnie z kryterium zamknięcia dopiero po iteracji bez istotnych poprawek.
