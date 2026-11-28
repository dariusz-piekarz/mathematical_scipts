# Topologia ogólna — rozdział 13, czysty audyt 2/2 po korekcie

**Data:** 2026-11-22.
**Niezmieniony badany blob:** `c9078636452731e42a56196e84b5ed9831120e6b`.
**Metoda:** ponowna kontrola niezależnymi ścieżkami: przypadki brzegowe, kierunki relacji niesymetrycznych, argumenty bez metryzowalności, współzależność lematu o minimalizacji z własnością uniwersalną. Nie zmieniano źródła.

## 1. Bez ukrytej symetrii i bez ukrytej metryki

W aksjomatach struktury jednostajnej dowolne E nie musi spełniać E=E⁻¹. W konstrukcji uzupełnienia:

- Użycie E-hat do stwierdzenia (N_x,N_y)∈E-hat ⇒ (x,y)∈E jest poprawne, bo elementy filtrów N_x i N_y zawierają x i y.
- Dla (x,y)∈D symetrycznego o D³⊆E, dowolne u∈D[x], v∈D[y] spełniają u D x D y D v, zatem D[x]×D[y]⊆E. Jest to właściwy kierunek wykazania jednostajności odwrotności zanurzenia.
- W dowodzie gęstości F wybór x∈A przy A×A⊆D daje (F,N_x)∈E-hat; relacja ta nie musi być symetryczna.
- W niepustości B(H,E) aktualna poprawka **nie odwraca E**, ale wybiera symetryczne D⊆E i stosuje symetrię D-hat. Jest to niezbędna, rzeczywiście dodana przesłanka.
- Gdy H×H⊆D-hat, argument (N_x,F)∈D-hat, (F,G)∈D-hat oraz (N_y,G)∈D-hat można po odwróceniu *symetrycznego* D-hat złożyć do (N_x,N_y)∈(D³)-hat. Z poprzedniej implikacji wynika (x,y)∈D³.
- W dowodzie zbieżności H→F₀ wyrażenie (N_x,F₀)∈(D²)-hat wymaga świadka T[x]∈N_x oraz C∈F₀, gdzie T jest symetryczne i T⊆D. Symetria D² daje (F₀,N_x)∈(D²)-hat; po dołączeniu (N_x,K)∈(D²)-hat otrzymujemy (F₀,K)∈(D⁴)-hat⊆E-hat.

**Wynik:** żaden z pozostałych wskazanych kroków nie dokonuje niedozwolonego odwrócenia relacji niesymetrycznej.

## 2. Przypadki brzegowe i kwantyfikatory

- Pusty X: nie istnieją właściwe filtry na ∅; zbiór minimalnych filtrów Cauchy'ego jest pusty; uzupełnienie puste jest zupełne, rozdzielające, a jedyne odwzorowanie ∅→∅ jest jednostajnym izomorfizmem na gęsty obraz.
- X nie-Hausdorffa: relacja R=∩U jest równoważnością, a iloraz X/R jest rozdzielający. W dowodzie złożenia obrazów D_q wykorzystano R⊆D i potrójne złożenie, nie nieudowodnioną zgodność klas przedstawicieli.
- Produkt z pustym czynnikiem jest pusty. Dla wszystkich niepustych czynników wybór granic filtrów obrazów opiera się na zwykłej zasadzie wyboru i definicji topologii produktowej przez skończone cylindry.
- Własność „każdy filtr Cauchy'ego zbiega” nie wymaga jednoznaczności granicy. Jednoznaczność w konstrukcji przedłużenia i w kryterium domkniętej podprzestrzeni wymaga rozdzielania celu i jest jawnie założona.
- Dla przestrzeni metrycznej warunek Cauchy'ego dla filtrów nie został utożsamiony z warunkiem dla ciągów bez dowodu: konstrukcja malejących A_n jest poprawna i wykorzystuje co najwyżej przeliczalny wybór.
- W przykładzie e(x,y)=|arctan x−arctan y| izometria do (−π/2,π/2) daje uzupełnienie domkniętym przedziałem. Prawidłowo oddzielono „zupełność ustalonej struktury jednostajnej” od „zupełnej metryzowalności topologii”.

## 3. Zależności między dowodami

Filtr ogonów i obraz jednostajnie ciągły sieci/filtra wykorzystują rozdział 12; twierdzenie o domknięciach zwartych nie jest użyte do skonstruowania uzupełnienia. Lemat F° stanowi podstawę rozdzielenia `widehat X` i nie wymaga uzupełnienia. Dopiero po nim skonstruowano bazę E-hat i wykazano zupełność. Lemat o rozszerzeniu przez gęstość korzysta z zupełności **przeciwdziedziny**, a nie z istnienia uzupełnienia **dziedziny**; własność uniwersalna jest więc niekołowa.

Uwaga „każda zwarta przestrzeń jednostajna jest zupełna” wynika z istnienia punktu skupienia filtra, z którego wraz z warunkiem Cauchy'ego otrzymuje się zbieżność; nie wymaga Hausdorffowości.

## 4. Testy i PDF

Rzeczywisty workflow na commicie z testem regresyjnym: [45070070493](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070070493), completed/success. Log kroku `python tools/tests/test_general_topology_ch13.py` potwierdza `PASS chapter 13 finite uniformities=24, principal Cauchy filters=127, entourage models=113, asymmetric=92, labels=810, refs=262`.

Z artefaktu **14773205627** tego przebiegu odczytano:
- `general_topology_ch13.pdf`: 6 stron A4;
- `general_topology.pdf`: 188 stron;
- `general_topology_ch13.log` i `general_topology.log`: brak dopasowań do `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence`, `Fatal error`.
W nowym PDF poprawiony akapit o B(H,E) występuje w sekcji 13.4.

## Wynik

**Czysty audyt 2/2:** nie wykryto dalszego błędu ani luki. Oba czyste audyty 07–08 przeprowadzono na tym samym blobie `c9078636452731e42a56196e84b5ed9831120e6b`. Pozostaje ostatnia niezależna kontrola potwierdzająca (+1); przed nią nie deklaruje się jeszcze ponownego zamknięcia stabilizacji.
