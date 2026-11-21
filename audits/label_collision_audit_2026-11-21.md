# Audyt kolizji etykiet — iteracja I (ryzyko i pochodzenie)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło liczb:** kanoniczny indeks GitHub Actions, przebieg [44920732533](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44920732533), artefakt `reference-provenance-audit`.  
**Stan bazowy:** 379 zaindeksowanych rozdziałów, 6713 różnych nazw etykiet.

## 1. Wynik globalnej klasyfikacji

| Miara | Wartość |
|---|---:|
| Powtarzające się nazwy etykiet | **306** |
| Kolizje w obrębie jednego skryptu (wg identyfikatora rodziny) | **0** |
| Kolizje wyłącznie między skryptami | **306** |
| Nazwy kolizyjne mające przynajmniej jedno odwołanie | **164** |
| Nazwy kolizyjne niecytowane w obecnym indeksie | **142** |
| Wystąpienia odwołań do nazw kolizyjnych | **603** |
| Spośród nich odwołania rozstrzygnięte | **603** |
| Wystąpienia odwołań niejednoznacznych do nazw kolizyjnych | **0** |
| Nierozwiązane odsyłacze z innych przyczyn | **22** |

W indeksie wszystkie kolizje są **między skryptami**. Mechanizm własności etykiet rozróżnia dokument i skrypt źródłowy, z pierwszeństwem etykiety lokalnej, następnie jedynego właściciela we własnym skrypcie, a dopiero potem właściciela globalnego (z dodatkowymi regułami aliasów i prefiksów `xr-hyper`). Z tego powodu nie należy interpretować 306 współdzielonych nazw jako 306 błędów odsyłaczy. Ta statystyka sama w sobie nie gwarantuje natomiast poprawności matematycznej każdego rozstrzygniętego odsyłacza, szczególnie w przypadku planowanego scalania treści.

### Rozkład po skryptach

| Skrypty | Nazwy |
|---|---:|
| Geometria różniczkowa (`DG`) i topologia algebraiczna (`TOP`) | 303 |
| Tom I i II prawdopodobieństwa (`P1`, `P2`) | 1 |
| Teoria kategorii (`KAT`) i logika/mnogości (`LST`) | 1 |
| Geometria algebraiczna (`ALG`), różniczkowa (`DG`) i topologia (`TOP`) | 1 |

Wśród 303 etykiet współdzielonych przez DG/TOP cytowanych jest 163; pozostałe 140 nie mają odwołań w indeksie. Pozostałe trzy kolizje dotyczą `ch:filtracje`, `def:equivalence` i `sec:moduly`, z których cytowana jest tylko ostatnia.

## 2. Priorytety według użycia etykiety

W pierwszej kolejności należy sprawdzać etykiety o największej liczbie odwołań oraz przy największej liczbie właścicieli. Dziesięć najczęściej cytowanych nazw:

| Etykieta | Cytowania | Właściciele |
|---|---:|---|
| `thm:homologia-sfer` | 16 | DG-08, TOP-05 |
| `ch:homologia-przestrzeni` | 15 | DG-08, TOP-05 |
| `lem:zwartosc-cw-pi` | 15 | DG-09, TOP-06 |
| `thm:podzial-jednosci-formy` | 13 | DG-10, TOP-09 |
| `ch:algebra-homologiczna` | 12 | DG-06, TOP-03 |
| `thm:les-homologia` | 12 | DG-06, TOP-03 |
| `thm:whitehead` | 12 | DG-09, TOP-06 |
| `thm:homotopia-singularna` | 10 | DG-08, TOP-05 |
| `thm:stokes-formy` | 9 | DG-10, TOP-09 |
| `eq:integracja-lancuchowa` | 8 | DG-10, TOP-09 |

Pełne **306 pozycji**, w tym oryginalne pliki, numery wierszy, SHA256 dokumentów, liczby odwołań i ustalone kolejki priorytetowe, znajduje się w artefaktach przebiegu GitHub Actions 44920732533: `reference_provenance_audit.json` i `reference_provenance_audit.md`. Nie ograniczamy audytu do powyższych dziesięciu pozycji.

## 3. Ręczna kontrola znaczenia wybranych kolizji

### `thm:homologia-sfer` — ten sam podstawowy wynik, różna szczegółowość dowodu

- `DG-08`, `08-homologia-przestrzeni.tex`, wiersz ok. 1138: `\widetilde H_k(S^n;\mathbb Z)\cong\mathbb Z` dla `k=n` i grupa zerowa w pozostałych stopniach; także `H_k(D^n,S^{n-1};\mathbb Z)`. Dowód explicite wybiera otwarte półkule `U={z>-ε}`, `V={z<ε}`, objaśnia pas przecięcia i deformację na równik.
- `TOP-05`, `05-homologia-przestrzeni.tex`, wiersz ok. 851: ta sama główna teza o sferach i parze dyskowej, sformułowana jawnie dla `n≥0` i `k∈\mathbb Z`. Dowód Mayera–Vietorisa jest krótszy.

**Wniosek:** sens matematyczny jest zgodny w sprawdzonym zakresie, ale teksty nie są wymiennymi ciągami znaków. Przy ewentualnym scalaniu trzeba zachować jawne kwantyfikatory z TOP oraz szczegóły konstrukcji homotopii z DG.

### `thm:whitehead` — zgodność tezy, różne rozwinięcia uzasadnienia

- `DG-09`, `09-wyzsze-grupy-homotopii-i-zwiazek-z-homologia.tex`, wiersz ok. 1144.
- `TOP-06`, `06-wyzsze-grupy-homotopii-i-zwiazek-z-homologia.tex`, wiersz ok. 1033.

Oba sformułowania mówią, że słaba równoważność homotopijna między kompleksami CW jest równoważnością homotopijną; obejmują też włączenie podkompleksu indukujące izomorfizmy grup homotopii oraz bijekcję składowych. W DG dowód szerzej omawia punkty bazowe, względne grupy homotopii i stopień 1; TOP przedstawia argument zwięźlej. **Nie usuwać żadnego wariantu dowodu bez pełnego audytu jego kroków.**

### `def:equivalence` — różne obiekty matematyczne, nie scalać

- `KAT-13`, `13-rownowaznosci-kategorii.tex`, ok. wiersz 5: *równoważność kategorii* przez quasi-odwrotność funktora i naturalne izomorfizmy.
- `LST-05`, `05-relacje-rownowaznosci-i-zbiory-ilorazowe.tex`, ok. wiersz 17: *relacja równoważności na zbiorze* jako warunek zwrotności, symetrii i przechodniości.

Identyczny identyfikator `def:equivalence` oznacza tu **dwie różne definicje**. Stanowią bezsporny przykład, dlaczego nie wolno scalać obiektów na podstawie etykiety. Jeśli oba skrypty będą kompilowane we wspólnym zakresie LaTeX, należy przedtem zaplanować niezależne prefiksy etykiet i odsyłaczy, zachowując obie definicje.

### `sec:moduly` — ta sama tematyka, różne role sekcji

- `ALG-04`, ok. wiersz 250: definicja modułu i przykłady w geometrii algebraicznej.
- `DG-05`, ok. wiersz 955: moduły, homomorfizmy i ilorazy w algebraicznych podstawach geometrii różniczkowej, z wyraźnymi konsekwencjami torsji.
- `TOP-03`, ok. wiersz 18: krótkie przypomnienie potrzebne do ciągów dokładnych i homologiach.

Nazwa sekcji jest wspólna, ale materiały pełnią różne funkcje. Kolizja etykiet nie dowodzi pełnej duplikacji treści.

### `ch:filtracje` — różne zastosowania

`P1-13` dotyczy filtracji, adaptacji i czasów zatrzymania; `P2-03` rozwija filtracje i obserwację procesów w czasie ciągłym. To dwa poziomy rozwoju tematu w odrębnych tomach. Obecnie nazwa nie ma cytowań w indeksie; przy kompilacji wielotomowej należy zachować osobne przestrzenie nazw.

## 4. Zmiany w repozytorium

W `application/scripts/audit_reference_provenance.py` dodano — bez zmieniania kanonicznego LaTeX i bez automatycznego przypisywania znaczeń — pola `same_script_collision`, `owner_scripts`, `risk_class`, `all_reference_count`, `resolved_reference_count` i pełną kolejkę `collision_priority_queue`. Raport Markdown pokazuje teraz pierwsze 25 pozycji według ryzyka i zachowuje listę wszystkich konfliktów wraz z pochodzeniem. W `application/tests/test_audit_reference_provenance.py` dodano testy poprawnego rozpoznawania kolizji wewnątrz skryptu i między skryptami, z kontrolą zachowania właścicieli i rozstrzygniętych odwołań.

GitHub Actions [44920732533](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44920732533): **SUCCESS**. Testy aplikacji i Chromium oraz audyt pochodzenia ukończyły się poprawnie. Baza jest nadal audytowana tylko do odczytu; oryginalne etykiety, twierdzenia, dowody i odsyłacze nie zostały zmienione.

## 5. Decyzja

**Iteracja I audytu 306 kolizji: zakończona.** Brak podstaw do masowych zmian etykiet: nie ma obecnie kolizji wewnątrz skryptu ani niejednoznacznych odsyłaczy. Potwierdzono merytorycznie zarówno przykłady pokrywających się twierdzeń (homologia sfer, Whitehead), jak i nieporównywalne definicje (równoważność kategorii i relacja równoważności).

Następny etap: niezależne sprawdzenie kolejnych par z grupy DG/TOP od największej liczby cytowań oraz osobny audyt kompilacji wielotomowych z `xr-hyper` przed ewentualnym scaleniem treści. Zachować oba warianty dowodów, nawet gdy teza wygląda na identyczną.
