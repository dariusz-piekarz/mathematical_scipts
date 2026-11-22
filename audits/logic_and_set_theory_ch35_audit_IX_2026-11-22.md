# Logika matematyczna i teoria mnogości — audyt IX rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Blob wejściowy:** 0f39627cfedab7da6e6e8de8fccb035bcf511af7.  
**Blob wyjściowy:** 1d510628d52469ef8aa00ad021125192c54ec439.  
**Werdykt:** audyt IX **nie jest czysty**, ponieważ ujawnił istotną lukę w szczegółowości dowodu zachowywania przynależności przez nazwy kanoniczne oraz aksjomatu nieskończoności. Poprawiony rozdział przeszedł pełne CI i wzrokową kontrolę PDF. Licznik czystych audytów pozostaje **0**.

## 1. Zakres niezależnego audytu

Ponownie zweryfikowano: RO(X) dla przestrzeni niepustej, uzupełnienie RO(P) niepustego pojęcia wymuszania, rekurencję po rangach nazw, tożsamości równości i podstawiania, lemat mieszania, pełność, wszystkie aksjomaty ZFC, iloraz przez dowolny zewnętrzny ultrafiltr, lemat prawdy oraz translację nazw porządkowych i boolowskich. Osobno sprawdzono poprawione w audycie VII dowody wartości 1 dla CH i jej zaprzeczenia bez zakładania istnienia przeliczalnego modelu tranzytywnego. Nie wykryto w tych częściach nowego błędu wymagającego zmiany źródła.

Przy osobnym rozpatrzeniu aksjomatów pustego zbioru, pary i nieskończoności stwierdzono, że tekst dotąd ograniczał się do deklaracji „nazwa check ω reprezentuje wewnętrznie zbiór induktywny” oraz ogólnego twierdzenia o zachowywaniu przynależności przez check x. Przy przyjętym standardzie szczegółowości dowodów było to niewystarczające.

## 2. Uzupełnienie własności nazw kanonicznych i aksjomatu nieskończoności

W dowodzie **thm:boolean35-zfc** dodano równoczesną indukcję dla dowolnych zbiorów a,b wyjściowego modelu:

- ⟦check a = check b⟧ = 1 wtedy i tylko wtedy, gdy a=b; w przeciwnym razie 0;
- ⟦check a ∈ check b⟧ = 1 wtedy i tylko wtedy, gdy a∈b; w przeciwnym razie 0.

Dowód przynależności rozwija klauzulę do supremum wartości równości z check y, y∈b; dowód równości wykorzystuje zewnętrzną ekstensjonalność a,b i hipotezę indukcyjną na elementach niższej rangi.

Dla nazwy zbioru pustego wykazano, że przynależność każdej nazwy ma wartość 0. Dla nazw σ,τ zdefiniowano jawnie nazwę **P_{σ,τ}** o dziedzinie {σ,τ} i współczynnikach 1 oraz udowodniono ⟦η∈P_{σ,τ}⟧ = ⟦η=σ⟧∨⟦η=τ⟧, także gdy σ i τ są dosłownie tą samą nazwą.

Dla nieskończoności rozpisano ⟦check 0∈check ω⟧=1 i dla dowolnej nazwy η:

  ⟦η∈check ω⟧ = ∨_{n<ω} ⟦η=check n⟧.

Ponieważ każda liczba n spełnia n+1=n∪{n}, nazwy pary i sumy pozwalają utworzyć następnika η, który na fragmencie ⟦η=check n⟧ jest równy check(n+1). Supremum po n daje wartość 1 zdania „dla każdego x∈check ω istnieje y∈check ω, y=x∪{x}”. W konsekwencji \check\omega ma wartość 1 jako zbiór induktywny. Konstrukcja sumy została niezależnie podana w następnym akapicie dowodu.

**Commity rozdziału:**
- 6b13c269bbcdfe70f08b264b2aad1bf3c039a450 — pełny dowód nazw kanonicznych, pary i nieskończoności;
- add5297737bf737122c48e126ee5093d1c746af6 — jawne i jednoznaczne oznaczenie nazwy pary P_{σ,τ}.

## 3. Niezależny test regresyjny i inwentarz

Dodano metodę **test_canonical_names_preserve_atomic_truth_and_successor**. Test niezależnie implementuje skończoną semantykę równości i przynależności w 8-elementowej algebrze Boole'a na nazwach kanonicznych wybranych zbiorów dziedzicznie skończonych. Sprawdza wartość atomowej równości i przynależności, nazwy par, konstrukcję następnika w pierwszych skończonych liczbach porządkowych oraz obecność nowego dowodu w źródle. **22 metody regresyjne** rozdziału 35, wszystkie pomyślnie wykonane w CI.

**Commity:**
- e301e7bb6468dece8e10901af9d19387df7b010f — nowy test i licznik 34 odsyłaczy rozdziału;
- 942db2c77b3ae7b77615668124c94e9000f1eb55 — 674 odsyłacze całej książki w workflow.

Inwentarz rozdziału 35: **8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 różnych etykiet, 34 odsyłacze**. Wszystkie środowiska LaTeX są prawidłowo sparowane. Pozostałe wcześniejsze regresje dla 389 małych preorderów, przekładu nazw, aksjomatów i ilorazu nadal przechodzą.

## 4. Pełne GitHub Actions i inspekcja PDF

**[GitHub Actions 45056534988](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45056534988): SUCCESS**, commit add5297737bf737122c48e126ee5093d1c746af6, tj. dokładnie ostatni commit zmieniający źródło w audycie IX. Wszystkie kroki testów rozdziałów 01–35, inwentarza, kompilacji LaTeX i kontroli PDF przeszły.

Pobrano faktyczny końcowy artefakt **14767691929**. PDF ma **311 stron**, A4; rozdział 35 zajmuje strony PDF **296–311**, łącznie **16 stron**. Wyrenderowano i niezależnie obejrzano zestaw wszystkich 16 stron oraz powiększone strony **300 i 301**, zawierające nowy argument o nazwach kanonicznych i nieskończoności. Nie wykryto kolizji ani uciętych wzorów.

Log kompilacji: **0 błędów LaTeX**, **0 overfull hbox**, **0 nierozwiązanych odsyłaczy**, **0 brakujących znaków**, jedno ostrzeżenie **underfull hbox** w całej książce. Nie stanowi ono błędu merytorycznego.

## 5. Werdykt i dalszy etap

Ponieważ audyt IX wymagał rzeczywistego uzupełnienia argumentacji, **nie może zostać zaliczony jako czysty**. Licznik niezależnych czystych audytów: **0**.

Następna iteracja: **audyt X** na dokładnie niezmienionym blobie źródła **1d510628d52469ef8aa00ad021125192c54ec439**, najpierw matematyczno-redakcyjna kontrola całego rozdziału oraz nowego dowodu \check\omega, następnie ponowna walidacja techniczna. Po uzyskaniu stabilności wykonać jeszcze jeden niezależny audyt potwierdzający. Ani kompilacja LaTeX, ani testy Python nie są weryfikacją w Lean.
