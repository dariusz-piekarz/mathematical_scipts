# Audyt II — rozdział 08 „Obrazy, przeciwobrazy i działania na funkcjach”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/08-obrazy-przeciwobrazy-i-dzialania-na-funkcjach.tex`.  
**SHA blobu po audycie I:** `e4374e94314c4e31884b459416396810b2e04615`.  
**Cel:** druga, niezależna kontrola tego samego istniejącego materiału; bez dopisywania twierdzeń, lematów lub rozszerzania zakresu.

## Wynik matematyczny

**Audyt II nie wykrył nowego błędu matematycznego ani luki w dowodzie wymagającej poprawienia źródła.** Tekst `.tex` pozostawiono bez zmian.

Ponownie zweryfikowano komplet: **20 twierdzeń, 20 dowodów, 6 definicji, 16 przykładów, 1 uwagę i 1 diagram TikZ**. Uwzględniono samodzielność założeń, poprawność dowodów w ZF i przypadki graniczne:

1. Obrazy, przeciwobrazy, monotoniczność i prawa sum, przecięć oraz różnic; dokładny warunek zachowania przecięcia przez ustaloną funkcję i ustalone dwa podzbiory, bez założenia iniekcji.
2. Rodziny indeksowane dowolną mocą i **pustą rodzinę przecięć**: dla pustej rodziny równość `f[∩ S_i] = ∩ f[S_i]` zachodzi dokładnie dla surjekcji; przy niepustym indeksowaniu iniekcja wystarcza. W dowodzie dla niepustego indeksowania wybrano jedynie jeden indeks i osobno porównano świadków; nie użyto niejawnie aksjomatu wyboru.
3. Kryteria iniekcji poprzez zachowywanie wszystkich przecięć binarnych albo wszystkich różnic; przypadek pustej dziedziny.
4. Zawierania i równoważności `f[S]⊆T iff S⊆f⁻¹[T]`, dokładne formuły `f[f⁻¹[T]]=T∩f[A]` i `f⁻¹[f[S]]` oraz minimalne nasycenie zbioru przez włókna. Doprecyzowanie redakcyjne z audytu I prawidłowo odróżnia zawierania od ich przypadków równości.
5. Składanie i zestawianie funkcji, zgodność ich dziedzin i przeciwdziedzin, obrazy i przeciwobrazy złożeń, własność uniwersalną funkcji parowanej, również dla pustej dziedziny.
6. Sklejanie dwóch i dowolnej indeksowanej rodziny funkcji: zgodność na przecięciach, istnienie wykresu jako sumy wykresów, jednoznaczność oraz przypadek pustego indeksowania.
7. Iloczyn kartezjański funkcji; konieczność właściwych założeń o niepustości dziedzin do odwracania implikacji o iniekcji, a przeciwdziedzin do analogicznej implikacji o surjekcji.
8. Ograniczenia i przedłużenia funkcji na większą dziedzinę, włącznie z `A=∅`, `D=A`, `B=∅`. Konstruowanie przedłużenia nie wymaga aksjomatu wyboru, bo wystarcza jedna ustalona wartość.
9. Faktoryzację przez relację równoważności i iloraz przez równość wartości `f(a)=f(a')`, także gdy `A=∅`, oraz brak potrzeby globalnego wyboru reprezentantów.

## Nowe, niezależne kontrole modeli skończonych

W drugiej iteracji uruchomiono inne zbiory przypadków niż w audycie I:
- **158 funkcji** `f:n→m`, dla `0≤n≤4, 0≤m≤3`;
- **1928 przypadków ograniczenia** funkcji do podzbioru jej dziedziny, wraz z obrazem, przeciwobrazem i dziedziczeniem iniekcji;
- **256 przypadków przedłużania** dla `0≤|D|≤4`, uwzględniających `A⊆D` i przypadki puste;
- **1688 przypadków faktoryzacji** przez wszystkie podziały zbiorów liczących co najwyżej 4 elementy, weryfikując stałość funkcji na blokach i indukowanie funkcji na ilorazie;
- **1544 przypadki zestawienia** funkcji ze wspólną dziedziną i sprawdzenia rzutów;
- **19 683 trójki funkcji częściowych** na podzbiorach `{0,1,2}`, z wartościami w `{0,1}`, weryfikując równoważność zgodności na przecięciach z istnieniem sklejonej funkcji.

**Wynik: zero kontrprzykładów.** Te skończone kontrole są testami regresyjnymi/próbami falsyfikacji; **nie zastępują dowodów ogólnych**, szczególnie dla rodzin nieskończonych.

## Skład, rysunek i odsyłacze

- Zachowano wszystkie **27 etykiet** rozdziału, strukturę 20 dowodów i bilans środowisk LaTeX. Żadnych zmian w pliku źródłowym.
- Książka rozdziałów 01–08 posiada **250 unikatowych etykiet** i **91 wystąpień odsyłaczy**. Trzy oczekiwane odsyłacze w przyszłość prowadzą do rozdziałów 09, 10 i 25: `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`.
- Diagram `fig:preimage-image-xliv` pozostaje niezmieniony, a poprzedni przegląd wizualny strony 81 pełnego PDF nie wykazał kolizji opisów ani obcięcia; ta iteracja nie wymagała modyfikacji rysunku.
- Ostatnia walidacja przed bieżącym raportem zakończyła się sukcesem na GitHub Actions: kompilacja **77 stron PDF**, testy rozdziałów 07–08, kontrola brakujących referencji i brak przepełnionych wierszy. Bieżący raport automatycznie wyzwala ponowną walidację workflow `.github/workflows/logic-and-set-theory-chapter.yml`; jej wynik potwierdzić przed formalnym zamknięciem.

## Konkluzja

**Rozdział 08 stabilny merytorycznie po audycie II; nie wymaga zmian źródła.** Formalne domknięcie po potwierdzonym zielonym przebiegu CI na commicie zawierającym niniejszy raport.

**Następny rozdział do audytu:** 09 — „Języki formalne, termy i formuły”; kontynuować strategię szczegółowego ponownego przeglądu istniejącego materiału bez dodawania nowych twierdzeń.
