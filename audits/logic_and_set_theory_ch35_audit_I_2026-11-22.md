# Logika matematyczna i teoria mnogości — audyt I rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Temat:** „Modele o wartościach boolowskich i względna niesprzeczność CH”.

## Cel i rzeczywisty zakres audytu

Rozdział 34 dowodził istnienia modeli CH i $\neg$CH przy założeniu **przeliczalnego tranzytywnego modelu zbiorowego ZFC**. Rozdział 35 uzupełnia argument i dowodzi obu implikacji z samej $\operatorname{Con}(\mathrm{ZFC})$, bez założenia istnienia modelu tranzytywnego. Audyt obejmuje pełną konstrukcję wartości logicznych, lemat pełności i mieszania, aksjomaty ZFC o wartości $1$, iloraz przez ultrafiltr oraz końcowe wnioskowanie metamatematyczne. Nie jest to jedynie kontrola formalnej obecności etykiet.

## I. Poprawność konstrukcji

1. **Uzupełnienie boolowskie.** Sprawdzono topologię generowaną przez stożki wzmocnień warunków, formuły na regularnie otwarte zbiory, istnienie dowolnych kresów w $\operatorname{RO}(\mathbb P)$ i gęstość obrazu $p\mapsto i(p)$ również dla preorderów nierozdzielających warunków równoważnych.
2. **Nazwy boolowskie.** Hierarchia funkcji $V_\alpha^{\mathbb B}$ jest definiowana rekurencją pozaskończoną. Wartości atomów są określone przez wzajemną rekurencję po sumie naturalnej rang dwóch nazw. Dla każdej ustalonej formuły wartości pozostają w $\mathbb B$.
3. **Kwantyfikator egzystencjalny.** Kres górny wartości wszystkich nazw nie jest kresem po właściwej klasie jako obiekcie zbiorowym: zbiór *różnych wartości* jest ograniczony przez samą algebrę $\mathbb B$ i powstaje przez wyróżnianie. Rozróżnienie to jest wyjaśnione w tekście.
4. **Lemat mieszania.** Pod rodzinę nazw indeksowaną zbiorem antyłańcucha $A$ tworzy się jeden zbiór dziedzin oraz współczynniki $\bigvee_{a\in A}a\wedge\tau_a(\pi)$. Rozłączność antyłańcucha zapewnia lokalne równości nazw.
5. **Lemat pełności.** Dla każdej standardowej formuły wartość egzystencjalna ma nazwany świadek. Wybór świadków nie jest wyborem z właściwej klasy: najpierw minimalizuje się rangi kandydatów, potem zastępowanie ogranicza je jedną liczbą porządkową i dopiero w zbiorze nazw ograniczonej rangi stosuje się aksjomat wyboru.
6. **Aksjomaty ZFC.** Skontrolowano konstrukcje pustej nazwy, pary, zbioru induktywnego, nazwy sumy, wyróżniania, zbioru potęgowego, zastępowania, ufundowania i wyboru. Szczególną uwagę poświęcono ograniczeniu dziedzin nazw dla potęgi i zastępowania do zbiorów istniejących w modelu wyjściowym. Istnieją również logiczne schematy o wartości $1$.
7. **Iloraz.** Zewnętrzna klasa wszystkich nazw *należących do modelu zbiorowego $M$* jest zewnętrznie zbiorem; nie trzeba zakładać jej istnienia wewnątrz $M$. Relacja równości boolowskiej modulo ultrafiltr jest relacją równoważności, a przynależność nie zależy od wyboru reprezentantów.
8. **Lemat prawdy w ilorazie.** Dla formuł atomowych obowiązuje definicja ilorazu; dla negacji i koniunkcji aksjomaty ultrafiltru; dla egzystencji krytycznie potrzebny jest lemat pełności zapewniający nazwę świadka. **Nie jest wymagane, aby ultrafiltr był generyczny.**
9. **Względna niesprzeczność.** Twierdzenie o pełności logiki daje model zbiorowy pełnej ZFC z założenia niesprzeczności. Nie żąda się tranzytywności ani zewnętrznego dobrego ufundowania. W modelu wyjściowym istnieją algebry $\operatorname{RO}(\operatorname{Add}(\omega,\omega_2))$ i $\operatorname{RO}(\operatorname{Coll}(\omega_1,2^{\aleph_0}))$; formalizowalne w ZFC dowody z rozdziału 34 dają odpowiednio wartości $\llbracket\neg\mathrm{CH}\rrbracket=1$ i $\llbracket\mathrm{CH}\rrbracket=1$. Ilorazy przez dowolne zewnętrzne ultrafiltry spełniają te zdania oraz ZFC, a więc obie rozszerzone teorie są niesprzeczne przy założeniu niesprzeczności ZFC.

## II. Weryfikacja przykładów i ograniczeń

W czteroelementowej algebrze $\mathcal P(\{0,1\})$ są dwa główne ultrafiltry; element $\{0\}$ należy tylko do pierwszego. Pokazuje to, dlaczego wartość logiczna $1$ daje twierdzenie prawdziwe **w każdym** ilorazie, podczas gdy wartość dodatnia może być prawdziwa wyłącznie w niektórych.

W tekście jawnie odróżniono:
- pełne twierdzenie o względnej niesprzeczności od mocniejszej hipotezy istnienia modelu tranzytywnego;
- model zbiorowy od modelu tranzytywnego;
- **wewnętrzną zupełność** algebry w potencjalnie nietranzytywnym modelu od zewnętrznej zupełności;
- schemat wartości boolowskich dla standardowych formuł od niemożliwego uniwersalnego predykatu prawdy;
- dowód matematyczny od skompilowanej formalizacji w Lean.

## III. Korekty techniczne i regresje

- Rozdział został dodany do books/pl/logic_and_set_theory.tex i catalog/books.json, a workflow .github/workflows/logic-and-set-theory-chapter.yml rozszerzono na rozdziały 01–35.
- **Rozdział 35:** 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 etykiet i 30 odsyłaczy.
- **Książka:** 35 rozdziałów, 879 etykiet, 670 odsyłaczy.
- Dodano tools/tests/test_logic_and_set_theory_ch35.py z **11 testami**. Sprawdzają m.in. wszystkie regularnie otwarte zbiory małej topologii wymuszania, boolowskie wartości formuł atomowych na algebrze czteroelementowej, mieszanie nazw, zachowanie prawdziwości przez ultrafiltry i jawne sformułowania względnej niesprzeczności.
- Odkryto starszy test integracji rozdziału 34 uzależniony od dokładnej liczby 34 rozdziałów. Zastąpiono go kontrolą co najmniej 34 rozdziałów i utrzymania rozdziału 34 na właściwej pozycji. Analogicznie zabezpieczono nowy test przed przyszłym rozdziałem 36.
- Pierwszy przebieg CI w nowym układzie zatrzymał się na starym założeniu w teście rozdziału 34. Po jego poprawce przebieg numer 45040796492 potwierdził przejście regresji rozdziałów 34 i 35, ale kompilacja zgłosiła **niezdefiniowany symbol** $\backslash\mathrm{llbracket}$. Poprawiono to przez dodanie pakietu stmaryrd w preambule książki; uruchomiono pełną ponowną walidację CI.

## IV. Walidacja końcowa i werdykt

- [GitHub Actions #45040918451](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45040918451): **SUCCESS** — cały zestaw regresji rozdziałów 01–35, 11 testów rozdziału 35, poprawny inwentarz 879 etykiet i 670 odsyłaczy, kompilacja LaTeX i kontrola logu.
- [GitHub Actions #45041124029](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041124029): przebieg powtórzony po zapisaniu raportu audytu I; matematyczna treść rozdziału nie była w międzyczasie zmieniana.
- **PDF całej książki:** **305 stron**. Rozdział 35 zajmuje strony PDF **296–305**, drukowane **287–296**. Wyrenderowano i obejrzano wszystkie **10 stron** nowego rozdziału: brak uciętych wzorów, kolizji tekstu i nieczytelnych podwójnych nawiasów boolowskich.
- **Log LaTeX:** 0 błędów, 0 nierozwiązanych odsyłaczy, 0 brakujących cytowań i 0 ostrzeżeń o przepełnionych wierszach; w całej książce pozostało 1 ostrzeżenie o niedopełnionym wierszu.

**Werdykt audytu I:** matematyczna konstrukcja względnej niesprzeczności została opracowana i poddana pierwszej kontroli. Weryfikacja integracyjna wykryła dwa problemy techniczne i oba zostały poprawione. **Rozdział 35 nie otrzymuje jeszcze statusu stabilnego:** kolejne niezależne audyty powinny ponownie skontrolować lemat pełności, ufundowanie, zbiór potęgowy i zastępowanie w uniwersum boolowskim oraz zgodność argumentu z logiką pierwszego rzędu dla dowolnych, także nietranzytywnych modeli.
