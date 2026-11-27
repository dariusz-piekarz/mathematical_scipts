# Atlas matematyczny — kanoniczny plan rozwoju aplikacji

**Zatwierdzono:** 22 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; **gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Właściciel planu:** użytkownik. **Tryb:** jeden wspólny, sekwencyjny strumień automatyzacji.  
**Dziennik postępów:** [ATLAS_DEVELOPMENT_PROGRESS.md](ATLAS_DEVELOPMENT_PROGRESS.md).  
**Inne źródła prawdy:** `application/ROADMAP_I_DZIENNIK.md`, `application/docs/LEAN_FORMALIZATION_PLAN.md`, `README.md`, aktualny HEAD i GitHub Actions.

## Cel

Przekształcić Atlas z przeglądarki matematycznych źródeł LaTeX, grafów i generatora ZIP w zintegrowane lokalne środowisko eksploracji, weryfikacji, przygotowywania publikacji i audytu matematyki. Zachować kanoniczność źródeł `chapters/pl/` i prawdziwe pochodzenie obiektów.

## Obowiązujące zasady realizacji

1. Przed KAŻDĄ iteracją ponownie odczytaj ten plan, dziennik postępów, `application/ROADMAP_I_DZIENNIK.md`, `application/docs/LEAN_FORMALIZATION_PLAN.md`, aktualny HEAD i wyniki odpowiednich CI. **Nigdy nie opieraj następnego kroku na historycznym, niesprawdzonym statusie.**
2. **Cykl naprzemienny A/B (decyzja użytkownika 24.11.2026).** A: dodaj jeden spójny fragment funkcjonalności/materiału, od razu przeprowadź audyt stabilizacyjny, popraw defekty, uruchom właściwe testy i CI; zapisz kandydata i stan. B: osobna iteracja poświęcona wyłącznie dodatkowemu sceptycznemu audytowi, przypadkom brzegowym, regresjom i stabilizacji poprzedniego fragmentu; poprawki są dozwolone, nowe funkcjonalności nie. Po czystym odbiorze technicznym B następna iteracja A dodaje kolejny fragment zgodnie z kolejką. Cykl A/B/A/B powtarzaj. Jeśli CI nadal trwa lub wykryto defekt, pozostań w B aż do rzeczywistych wyników i napraw; nie uruchamiaj bez potrzeby drugiej identycznej serii CI, nie twórz pustych commitów z samą informacją o oczekiwaniu. Runda CI nie jest osobną iteracją rozwojową. Zachowaj techniczny wymóg 2+1 na jednym SHA. Niezależny odbiór formalny pozostaje osobnym warunkiem statusu stable i nie wolno go symulować; gdy jedynym brakiem jest niezależna recenzja po czystej stabilizacji technicznej, odnotuj review pending i nie nadawaj stable/certificate. Nowy cykl nie znosi blokad bezpieczeństwa ani wymogu usunięcia defektów.
3. Dla każdego fragmentu: (a) zdefiniuj kryteria akceptacji i ryzyka; (b) implementacja; (c) testy jednostkowe, integracyjne, bezpieczeństwa i przeglądarkowe zależnie od zakresu; (d) rzeczywisty CI i odpowiedni Lean/Mathlib lub LaTeX, jeśli potrzebny; (e) usuń wszystkie defekty i powtarzaj testy; (f) **stabilność 2+1** — dwa niezależne czyste przebiegi pełnego właściwego CI na tym samym niezmienionym SHA oraz dodatkowy sceptyczny audyt kontrolny i przebieg weryfikacyjny (łącznie 3 czyste kontrole), bez otwartych krytycznych uwag. Test powtórzony po zmianie kodu liczy się od nowa. Gdy powtarzanie pełnego CI jest niemożliwe, jawnie oznacz `blocked`, a nie `stable`.
4. **Nie przeskakuj zadań na podstawie samego commitu, lokalnego testu, zielonego workflow dla innego SHA ani symulowanego uruchomienia.** Przy braku uprawnień/środowiska raportuj blokadę, nie wymyślaj wyników. Skipped tests jawnie odnotuj; nie zaliczaj testów wymaganych, które zostały pominięte.
5. Jeden istniejący branch; bez force-push, bez nowych gałęzi roboczych, bez przepisywania zmian innych audytów. Bezpośrednio przed zapisem sprawdź HEAD i zawartość zmienianych plików; konflikt => odczyt, ponowna integracja albo bezpieczny stop. Nie modyfikuj cudzych plików źródłowych `.tex` bez odrębnego matematyczno-redakcyjnego audytu i uzgodnionego zakresu.
6. Co iterację uaktualniaj dziennik `ATLAS_DEVELOPMENT_PROGRESS.md` z konkretnymi plikami, SHA, linkami CI, wynikami, defektami, stanem `planned | implementing | testing | stabilizing | blocked | stable` i następnym jednoznacznym krokiem. Nie zastępuj historii pustymi raportami ani fikcyjnymi commitami. Jeśli nic nie zmieniono, podaj jawny wynik i blokadę.
7. Formalny status `compiled` nie oznacza `verified` ani zgodności matematycznej. W Lean oddzielaj zgodność źródła, stan formalizacji, rzeczywistą kompilację i certyfikację. Bez podpisanej polityki recenzji pozostaw `certificate=false`. AI, graf i wyszukiwanie semantyczne nie mogą udawać dowodów.
8. Zachowaj ochronę runnera Lean: biała lista plików, brak dowolnych poleceń z przeglądarki, limity wyjścia, czasu, pamięci i procesów potomnych, stabilne skróty źródła i zależności, kontrole przed/po uruchomieniu, odmowa symlinków i nieufnych ścieżek. Nie rozluźniaj zabezpieczeń dla wydajności.
9. Nie usuwać unikalnych definicji, wariantów dowodów, przykładów, kontrprzykładów, zadań, ilustracji ani kodu. Deduplikacja musi być bezstratna i mieć rejestr pochodzenia i odsyłaczy.
10. Zasady terminologii, dokładność matematyczna, przykłady i kompilowalność podlegają ogólnemu standardowi audytu Biblioteki (wzorzec DG-01).

## Sekwencyjna kolejka — siedem etapów

Wewnątrz każdego etapu są fragmenty wykonywane po kolei w cyklu A/B. Po czystym technicznym odbiorze B można przejść do kolejnego podetapu rozwojowego; osobna niezależna recenzja nadal warunkuje formalne `stable`. Nie przechodź do kolejnego głównego etapu przy otwartych istotnych defektach ani niespełnionych wymaganiach odbioru.

### 1. Lean 4 — stabilizacja i rozwój formalizacji

- **L1.1** Domknij otwartą kontrolę faktycznego odczytu `.olean` podczas współbieżnego wzrostu pliku; potwierdź nowe regresje, natywne Windows/Linux, pełny CI oraz przypięty Lean/Mathlib. Utrzymaj pełne bezpieczeństwo fingerprintów. **Pierwszy fragment do wykonania po północy.**
- **L1.2** Przeanalizuj i ustabilizuj ścieżkę Czytnik → fragment Lean → runner → historia i migawka inspekcji; testy wyjątków, starych SHA, konfliktów etykiet, anulowania i procesów potomnych.
- **L1.3** Ukończ pilotaż 20–30 rzeczywistych formalizacji począwszy od LST-01, LST-02, LA-01, w małych pakietach, wraz z rzeczywistą kompilacją i recenzją semantyczną. Odrębnie podawaj liczbę zarejestrowanych, skompilowanych i recenzowanych twierdzeń.
- **L1.4** Udoskonal wersjonowanie, cache zależności i raporty rozdziałowe, nie tracąc integralności ani punktów kontrolnych; pomiar na rzeczywistym Mathlib przed uznaniem optymalizacji.
- **L1.5** Rozwijaj hybrydową transkrypcję LaTeX → Lean: lokalny parser i reguły, gotowy lokalny model, Lean 4/Mathlib i ograniczona pętla napraw. **Warunek użytkownika z 27.11.2026: bez opłat za inferencję zewnętrzną i bez wymaganego abonamentu; brak płatnego fallbacku.** Pierwszy warunkowy pilot gotowego procesu: LeanFlow + Lemex + lokalny serwer modelu; AutoformBot jako alternatywa dopiero po potwierdzeniu bezpłatnego lokalnego runtime. Bez treningu własnego modelu. Sama licencja open source nie spełnia kryterium kosztu. Kandydaci `draft`/`needs_review`, osobna kontrola semantyki, bez automatycznej zmiany kanonicznych plików. Kolejność i kryteria: [plan autoformalizacji](LEAN_LOCAL_AUTOFORMALIZATION_PLAN.md).

### 2. Inteligentny graf zależności i pojęć

- **G2.1** Jeden sprawdzalny model węzłów, tożsamości, etykiet i pochodzenia źródeł; rozdziel jawne `\\ref`, jawne zależności Lean i hipotezy semantyczne.
- **G2.2** Rozszerz realną inspekcję deklaracji Lean o zależności typu, wartości, założenia i aksjomaty; zachowaj rozróżnienie między syntaktycznym importem a rzeczywistym wykorzystaniem deklaracji.
- **G2.3** Zdefiniuj recenzowane typy relacji: „korzysta z”, „uogólnia”, „szczególny przypadek”, „równoważne”, „wymaga definicji”; każda silna relacja wymaga uzasadnienia.
- **G2.4** Interaktywny graf i ścieżki zależności w UI, filtrowanie źródła relacji, rozstrzyganie konfliktów, testy regresji.

### 3. Generator projektów, PDF i lepszy czytnik

- **P3.1** Pełniejsze rozpoznawanie środowisk TeX, wybranych zakresów, brakujących definicji/makr, zagnieżdżeń i kontekstu fragmentów; jednoznaczne identyfikatory.
- **P3.2** Konserwatywne łączenie preambuł, wykrywanie konfliktów pakietów, środowisk i liczników, testy rzeczywistych zestawów wielodziedzinowych.
- **P3.3** Walidacja `xr-hyper` i `.aux` ze źródłem prawdy w rzeczywistej kompilacji, raporty brakujących i niejednoznacznych odsyłaczy.
- **P3.4** Bezpieczny lokalny proces budowy PDF, diagnostyka, eksport z raportem; nie zakładaj kompilowalności arbitralnych wycinków.
- **P3.5** Lepsze wizualne renderowanie matematyki i ergonomia Czytnika/Explorera, dokładne otwieranie definicji, twierdzeń i źródeł, testy Chromium.

### 4. Centrum audytów i bezstratna integracja Biblioteki

- **A4.1** Dashboard audytów z katalogiem rozdziałów, stanem, historią, błędami, konkretnymi dowodami przejścia CI, zależnościami i informacją o stabilności.
- **A4.2** Zintegrowane walidatory terminologii, LaTeX, `\\label`/`\\ref`, grafów i kompilacji; odróżnienie kontroli automatycznej od audytu matematycznego.
- **A4.3** Rejestr kandydatów do deduplikacji i karta porównawcza obiektów z pochodzeniem, bez automatycznego nadpisania.
- **A4.4** Kontrolowane bezstratne scalanie do `shared/pl/` w małych partiach, mapy aliasów i weryfikacja globalna oraz połączeń między skryptami.

### 5. Wyszukiwanie semantyczne

- **S5.1** Indeks pojęć, definicji, twierdzeń i zależności z identyfikacją źródła i wersji; zachowaj bazową wyszukiwarkę FTS.
- **S5.2** Wyszukiwanie według znaczenia, ranking i sprawdzalne odwołania; odróżniaj sugestię od matematycznej implikacji.
- **S5.3** Ewaluacja jakości wyszukiwania na rzeczywistych pytaniach, obsługa fałszywych trafień i nieaktualnego indeksu.

### 6. Asystent matematyczny w Atlasie

- **M6.1** Pytania o wybrany fragment, cytowanie lokalnych definicji, lematów i wersji źródła; brak niepotwierdzonych przypisań.
- **M6.2** Propozycje uzupełnień dowodów, kontrprzykładów i rewizji z osobną recenzją, bez automatycznej modyfikacji kanonicznych źródeł.
- **M6.3** Opcjonalne połączenie z Lean i raportem audytu; wyraźne oznaczenia „propozycja”, „sprawdzone kompilatorem”, „zatwierdzona semantyka”.

### 7. Ścieżki nauki i wygodna aplikacja lokalna

- **N7.1** Ścieżka od wybranego twierdzenia do potrzebnych definicji i lematów, z kontrolą cykli i braków.
- **N7.2** Budowa własnej książki z wybranej ścieżki, połączenie z kreatorem i audytem zależności.
- **N7.3** Uspójniona instalacja Windows/Linux/macOS, uruchomienie desktop/offline, opcjonalnie lokalny TeX i Lean, dokumentacja i testy środowiskowe.

## Infrastruktura walidacji na niezmiennym SHA (23 listopada 2026)

- Orkiestrator: `.github/workflows/atlas-stabilization.yml`. Jego kandydat `candidate_sha` jest **pełnym** 40-znakowym identyfikatorem istniejącego commitu w historii gałęzi. `application/scripts/atlas_validation_gate.py verify-sha` sprawdza istnienie obiektu Git i przynależność do gałęzi. Każdy checkout w podworkflow weryfikuje `git rev-parse HEAD` przeciw wskazanemu SHA. Nowe commity z innych audytów nie zmieniają tego kandydata.
- Trzy niezależne przebiegi wykonuje się **po kolei** (kolejny dopiero po zaliczeniu wcześniejszego), a w każdym przechodzą pełne CI aplikacji z Chromium, natywne Linux+Windows oraz rzeczywista kompilacja Lean 4/Mathlib wraz z audytem aksjomatów. Każdy przebieg uruchamia własne joby, nie przenosi pomiędzy nimi cache rezultatów testów; standardowy cache pobranych zależności/buildów nie zastępuje kontroli fingerprintu.
- `application/scripts/atlas_ci_report.py` uruchamia faktyczny `unittest discover` i zapisuje w artefakcie `atlas-unittest-<nr>` identyfikator każdego testu, rzeczywisty powód pominięcia, klasyfikację, liczniki oraz SHA; nieznane pominięcie powoduje FAIL. Znane pominięcia ze względu na Windows, wymagany Lean/Mathlib i ograniczenia hosta są **jawnie** raportowane; odpowiednie testy platformowe/Lean uruchamia osobny obowiązkowy workflow. `unittest -q` nie jest już jedynym źródłem obserwacji.
- Trzeci przebieg poprzedzają testy sceptyczne walidatora: fałszywe SHA, niekompletne lub podmienione raporty, nieznane skipy, brak wymaganej regresji wzrostu pliku oraz nieudany Lean/Windows muszą zostać odrzucone. Końcowy `atlas-validation-status` zawiera `blocked`, `stabilizing` albo `stable` i `certificate=false`.
- **Ważne ograniczenie:** poprawne trzy pełne techniczne przebiegi i testy sceptyczne **nie oznaczają jeszcze recenzji niezależnego człowieka**; bez jawnie zatwierdzonego raportu audytu końcowego status wynosi co najwyżej `stabilizing`. Od 23.11.2026 funkcja `gate --review` zapisuje tylko deklarację recenzji (`documented_unverified`); **niesygnowany JSON, nawet z `independent=true`, nie może ustawić `stable`**. Do ostatecznego awansu wymagane jest odrębnie uwierzytelnione zatwierdzenie niezależnego recenzenta (np. chroniona aprobata GitHub), udokumentowane w dzienniku. Ten gate celowo nie imituje ani nie zastępuje takiego poświadczenia. Nie awansować L1.1 do `stable` na podstawie samego zielonego CI.
- **Uruchamianie bez zmian w `main`:** zaktualizuj `application/config/atlas_validation_request.json` na istniejącej gałęzi, podając pełny `candidate_sha` i `fragment` (np. `L1.1`). Zmiana samego pliku żądania wyzwala workflow na gałęzi, ale **nie zmienia badanego commitu**. Można powtórzyć ten sam kandydat przez nową zmianę `request_note`. Walidator `atlas_validation_select.py` sprawdza schemat i pochodzenie SHA oraz emituje oba pola przez `GITHUB_OUTPUT`. Ręczne `workflow_dispatch` jest opcjonalne i może wymagać obecności workflow na domyślnej gałęzi; nie przenosić samowolnie zmian do `main`. Numer CI i wynik każdej próby należy odczytywać z GitHub Actions, nie ze statusu pojedynczego commitu.

## Protokół zamknięcia fragmentu i etapów

Fragment jest `stable` tylko po rzeczywistym spełnieniu wszystkich adekwatnych kryteriów oraz serii **2+1** na identycznym kodzie. Wymagany sceptyczny audyt nie może być wyłącznie powtórzeniem lokalnego testu; powinien próbować obalić założenia, sprawdzić wyjątkowe przypadki i wskazać ograniczenia. Po wykryciu błędu lub zmianie kodu licznik kontroli wraca do zera. Ostatnia kontrola zapisuje SHA, CI, listę testów, decyzję i zakres faktycznej pewności. `Blocked` nie jest `stable`; pierwsza kolejna iteracja ponawia pracę nad tym fragmentem.

Etap przechodzi w `stable` dopiero, gdy wszystkie fragmenty są stabilne i wykonano dodatkowy audyt integracyjny etapu. Przejście do kolejnego etapu następuje w **następnej** iteracji, nie w tej samej, w której finalizowano poprzedni. Jeśli cały plan został wykonany, nie twórz sztucznych zmian; opublikuj raport końcowy i zgłoś konieczność zakończenia harmonogramu.

## Harmonogram automatyzacji

Jeden strumień: **co godzinę od 23 listopada 2026 r., 00:00 Europe/Warsaw**. Pojedyncze uruchomienie realizuje jeden fragment/podetap; wraca do niego aż do stabilizacji. Wcześniejsze oddzielne automatyzacje Lean są wyłączone. Automatyzacje audytujące inne dziedziny pozostają niezależne i nie są częścią tego planu.
