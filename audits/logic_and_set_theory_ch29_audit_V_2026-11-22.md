# Logika matematyczna i teoria mnogości — rozdział 29, audyt V (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/29-slabsze-zasady-wyboru-i-ich-ograniczenia.tex`  
**Zakres:** tylko rozdział 29; bez nowych twierdzeń, przykładów i bez zmian tekstu źródłowego w iteracji V.

## Ponowna kontrola matematyczna

1. **Wybór przeliczalny i zależny.** Zweryfikowano kwantyfikatory definicji ACω i DC, warunek seryjności relacji, wskazanie punktu początkowego i argument AC ⇒ DC poprzez funkcję wyboru na włóknach relacji. Dla DC ⇒ ACω sprawdzono zbiór skończonych funkcji wyboru, jego istnienie przez separację, niepustość, seryjność relacji przedłużania i union ciągu częściowych funkcji.
2. **Przeliczalna suma zbiorów przeliczalnych.** Istnienie każdej rodziny `E_n` iniekcji `A_n→ω` jest uzasadnione zbiorem ograniczającym `P(A_n×ω)`; przed zastosowaniem ACω cała rodzina `(E_n)` istnieje przez zastępowanie. Iniekcja sumy do `ω×ω` wybiera najmniejszy indeks zbioru zawierającego rozważany element, co nie wymaga dodatkowego wyboru.
3. **Twierdzenie Baire'a z DC.** Cały dowód został zweryfikowany na poziomie relacji przedłużania skończonych ciągów kul. Każde przybliżenie ma przedłużenie; z DC uzyskujemy jedną gałąź. Krytyczną poprawkę starszego PDF potwierdzono: **domknięta kula** na następnym etapie leży w poprzedniej **otwartej** kuli i w danym otwartym zbiorze gęstym. Zbieżność środków w przestrzeni zupełnej daje wtedy przynależność granicy do wszystkich zadanych zbiorów. Rozróżniono kulę domkniętą od domknięcia topologicznego kuli otwartej, które w ogólnej przestrzeni metrycznej mogą być różne. Zweryfikowano przykład niezupełnego `Q`.
4. **Filtry i ideały w algebrach Boole'a.** Sprawdzono kompletność aksjomatów algebry Boole'a, definicję właściwego filtru i właściwego ideału pierwszego, jawnie skonstruowany filtr generowany przez `U∪{b}`, obie strony kryterium ultrafiltru oraz dowód zgodności standardowej definicji pierwszości ideału z dopełnieniem ultrafiltru.
5. **BPI ⇔ UF.** Dla pustego zbioru indeksowego lub nośnika filtracyjnego rozważono przypadki brzegowe. W kierunku UF ⇒ BPI konstrukcja skończenie generowanej podalgebry, minimalnego atomu i wartości boolowskiej `h_D` jawnie sprawdza dopełnienie i iloczyn. Warunki na współrzędne kostki `2^B` są domknięte i spełnialne skończenie; kompaktowość zapewnia ich jednoczesne spełnienie. Nie użyto AC poza odpowiednio zadeklarowanymi założeniami.
6. **Tychonoff dla zwartych Hausdorffa.** Zweryfikowano istnienie i jedyność granic obrazów ultrafiltru na współrzędnych, ich zbiór przez zastępowanie i uzyskanie granicy w produkcie. Pusty produkt jest zwarty. Argument odwrotny używa zwartości kostki `2^B` z poprzedniego twierdzenia, bez dodatkowego wyboru.
7. **Pełny Tychonoff ⇔ AC.** W kierunku AC ⇒ Tychonoff użyto ultrafiltrów tylko z `właściwych` filtrów i wyboru punktów granicznych w czynnikach. W kierunku odwrotnym zweryfikowano kanoniczne tagowanie `A_i×{0}` i `∞_i=(i,1)`, czteroelementową topologię czynnika, jego zwartość, domkniętość cylindra, istnienie skończonych przecięć przez wcześniejsze twierdzenie o wyborze skończonym oraz rozkodowanie funkcji wyboru z punktu wspólnego.
8. **Lemat Teichmüllera–Tukeya ⇔ AC.** Udowodniony skończony charakter rodziny grafów funkcji częściowych jest poprawny: każda przeszkoda do bycia funkcją jest świadczona przez dwie pary z tą samą pierwszą współrzędną. Suma łańcucha rodziny skończonego charakteru należy do niej, także dla łańcucha pustego, zaś maksymalność grafu wymusza pełną dziedzinę.
9. **Zasady terminologiczne.** Zachowano polskie nazewnictwo, jawne warunki ZF/AC/DC/ACω/BPI/UF, dowody wymaganych wzorów i odsyłacze do wcześniejszych wyników. Sformułowania o niezależności teorii są oznaczone jako wyniki modelowe, a nie wyprowadzone bez dowodu w ramach ZF.

**Wynik:** audyt V nie wykazał nowych luk matematycznych ani językowych wymagających modyfikacji; źródła rozdziału nie zmieniano podczas tej iteracji.

## Testy, inwentarz i skład

- Inwentarz: **6 definicji, 7 twierdzeń, 1 lemat, 5 przykładów, 7 uwag, 8 dowodów**. Zachowane **24 etykiety i 11 odsyłaczy**.
- Testy rozdziału 29, obejmujące modele skończonych algebr Boole'a, ultrafiltry i ideały, grafy funkcji częściowych, poprawną konstrukcję kul w Baire'ze i kanoniczne czynniki Tychonoffa: **PASS**.
- GitHub Actions [45008880491](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45008880491): **SUCCESS**, w tym pełna kompilacja i kontrola PDF. Porównanie SHA bloba rozdziału na aktualnej gałęzi ze źródłem tego przebiegu daje identyczność, mimo późniejszych commitów dotyczących wyłącznie testów i raportów.
- Pełna książka: **227 stron**, sam rozdział 29: **8 stron** (strony PDF 220–227). Wszystkie osiem stron wyrenderowano i sprawdzono wizualnie; nie stwierdzono nakładania tekstów, uciętych formuł ani naruszeń marginesów.
- Log: **0** przepełnień `Overfull \\hbox`, **0** niezdefiniowanych referencji, **0** nierozwiązanych cytowań i **0** błędów TeX. W całej książce pozostaje **1** niewielkie ostrzeżenie `Underfull \\hbox`, które nie wpływa na czytelność rozdziału 29.

## Werdykt końcowy

**ROZDZIAŁ 29 — STABILNY po audycie V.** Audyty I–IV naprawiły rzeczywistą lukę w dowodzie twierdzenia Baire'a i uzupełniły formalną poprawność konstrukcji; piąta iteracja była niezależnym audytem bez zmian treści przy zielonym CI i pełnej kontroli wizualnej PDF. Nie rozpoczynano rozdziału 30.
