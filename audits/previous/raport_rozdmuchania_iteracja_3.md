# Audyt merytoryczno-techniczny: rozdmuchanie punktu — iteracja III

**Data:** 19 listopada 2026 r.  
**Baza:** `biblioteka-matematyczna-iteracja-2`.

## Przegląd źródeł i rozróżnienie zakresów

Porównano trzy rozdziały:

1. `rozdzialy/geometria_algebraiczna/06-powierzchnie-algebraiczne-przeciecia-rozdmuchania-i-szczegolne.tex` — geometria dywizorów, wiązka konormalna, transformata ścisła, przecięcia, klasa kanoniczna i grupa Picarda.
2. `rozdzialy/geometria_algebraiczna/10-geometria-algebraiczna-a-topologia-od-cykli-do-twierdzen-lefsc.tex` — kohomologia rzeczywista, liczby Bettiego, charakterystyka Eulera, suma spójna i przykłady powierzchni kubicznej.
3. `rozdzialy/topologia_algebraiczna/28-topologia-gladkich-zespolonych-odmian-projektowych-twierdzenia.tex` — kohomologia całkowita, dowód Mayera–Vietorisa, forma przecięć i sygnatura, klasa kanoniczna, rozdmuchania w gładkich centrach.

**Wniosek:** równania topologiczne dotyczące rozdmuchania *punktu* są wspólne; formuły przecięć krzywych, Picarda i rozdmuchania centrum wyższej kodymensji mają niezależną wartość matematyczną, więc **nie** zostały usunięte.

## Zastosowane scalenie

- `wspolne/rozdmuchanie_punktu_normalna.tex`: jeden lemat z etykietami `st:ga6-exceptional-normal` oraz `lem:xvii-exceptional`, z dwiema jawnie porównanymi metodami: podwiązka tautologiczna i dualizacja konormalnej. Wniosek: `N_{E/\widetilde S}=\mathcal O_{\mathbb P^1}(-1)` oraz `E^2=-1`.
- `wspolne/rozdmuchanie_punktu_kohomologia.tex`: jedno twierdzenie z etykietami `tw:ga10-blowup` oraz `thm:xvii-blowup`. Zawiera rozkład całkowity `H^2(\widetilde S;\mathbb Z)=\pi^*H^2(S;\mathbb Z)\oplus\mathbb Z\operatorname{PD}[E]`, ortogonalność i zmianę `b_2`, `\chi_{\rm top}`, `\sigma`; dowód oparty na porównaniu Mayera–Vietorisa w stopniach 2, 3, 4.
- Rozdział 6 geometrii zastępuje swój lemat z dowodem pierwszym modułem.
- Rozdział 10 geometrii zastępuje powtórzony dowód topologiczny drugim modułem. Zachowuje osobno algebraiczny wzór na `K^2` i **alternatywny dowód** charakterystyki Eulera przez addytywność kohomologii o zwartych nośnikach.
- Rozdział 28 topologii zastępuje lemat, topologiczne twierdzenie i wniosek o sygnaturze/charakterystyce przez oba moduły.
- Oba moduły chronią przed podwójnym składem etykiet (`\ifcsname ...\endcsname`) i dopuszczają budowę książki łączonej.

## Matematyczna kontrola założeń i dowodów

- **Wiązka normalna:** wymagana tylko gładka zespolona powierzchnia i rozdmuchanie punktu; zwartość nie jest potrzebna dla lokalnego stopnia normalnej. `E^2=-1` w sytuacji niezwartej jest lokalnym samoprzecięciem, a nie integralną formą przecięć całej powierzchni.
- **Kohomologia integralna:** potrzebna powierzchnia zwarta i spójna. Rozkład jest ważny **także przy obecności torsji** w `H^2(S;\mathbb Z)`. Klasa wyjątkowa ma restrykcję do `E` równą ujemnemu generatorowi, co daje rozszczepienie na grupach abelowych.
- **Stopień trzeci:** wyjaśniono zerowanie mapy ograniczenia `H^3(U)\to H^3(S^3)` przez mapę łączącą do orientacji względnej; nie pominięto tego subtelnego kroku.
- **Ortogonalność:** wyprowadzona dla dowolnych klas z wzoru projekcji, nie wyłącznie dla klas dywizorów algebraicznych. `\sigma` dotyczy rzeczywistej formy przecięć (lub wolnej części całkowitej kohomologii).
- **Kanoniczna klasa:** nie sklejono różnych uzasadnień: rozdział 6 geometrii przeprowadza rachunek dywizorów i różniczek, rozdział 28 topologii zachowuje rachunek jakobianu. W obu przypadkach `K_{\widetilde S}=\pi^*K_S+E`; dla zwartej powierzchni `K_{\widetilde S}^2=K_S^2-1`.
- **Zakres ogólny:** twierdzenie topologiczne o rozdmuchaniu w gładkim centrum kodymensji `r>=2` pozostaje osobne: zawiera dodatkowe składniki `H^{k-2a}(Z)`, których nie wolno zredukować do przypadku punktu na powierzchni.
- **Dowody niezależne:** dowód topologiczny przez MV oraz alternatywny rachunek Eulera przez zbiory konstruktybilne pozostały dostępne. Przykłady, rysunki, podpisy i zadania są nietknięte.

## Integralność techniczna

- `manifest.json`: 12 źródeł, 236 rozdziałów, bez edycji oryginałów.
- `manifest_integracji.json`: niezmieniony rejestr dwóch zmian z iteracji II.
- `manifest_integracji_3.json`: pięć dokładnie zapisanych zamian tekstu w trzech rozdziałach, sumy kontrolne treści usuniętych, wstawionych i całych rozdziałów.
- `narzedzia/sprawdz_integracje_3.py`: rekonstruuje etap I, następnie II, następnie III i sprawdza cały finalny tekst wszystkich 236 rozdziałów.
- Osobne skrypty LaTeX zachowują kompilację; przy nowym pliku wyodrębnionym do `wspolne/` należy uruchamiać skład z `skrypty/`.

## Co pozostaje na następną iterację

W rozdziale o rozdmuchaniu gładkiego centrum (`topologia`, rozdz. 28) istnieje mocniejszy wzór kohomologiczny z homomorfizmami Gysina. Możliwa jest kolejna iteracja audytu lokalnych przejść przy wyprowadzaniu tego wzoru i porównania go z własnością uniwersalną/algebrą Reesa w `geometria`, rozdz. 5. Rozdziały te nie zostały scalone, ponieważ są zasadniczo komplementarne.
