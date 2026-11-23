# Topologia ogólna — globalny audyt 58: rozdział 13, drugi niezależny czysty reaudyt

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex`, blob `160a4cb67698525f0f5c08f56f3d8bb3cbfa0623`.
**Regresja:** `tools/tests/test_general_topology_ch13.py`, blob `ef1996a61c716e4b3380b6b63c56a4a4c3350eb0`.

## Zakres i niezależna metoda

To **drugi czysty reaudyt** po korekcie odsyłacza wykonanej w [audycie 56](00-globalny-audyt-56-pelna-kontrola-13-9-dowodow-korekta-odsylacza.md). W odróżnieniu od [reaudytu 57](00-globalny-audyt-57-reaudyt-13-czysty-1.md), skoncentrowanego na diffie starego i nowego źródła, niniejsza kontrola wykorzystuje nowy odczyt argumentów, kontrolę brzegów założeń oraz **niezależną enumerację modeli skończonych**. Enumeracja nie zastępuje dowodów ogólnych.

## Kontrola matematyczna

1. **Filtry i sieci (13-01): PASS.** W sieci indeksowanej parami `(A,a)` każdy element `b∈A` występuje po indeksie `(A,a)`; jest to krok potrzebny do wywnioskowania `A⊂O`, nie tylko przecięcia `A∩O≠∅`.
2. **Zupełność metryczna i konstrukcja ciągowa (13-02, 13-03): PASS.** Zstępująca rodzina elementów filtra zapewnia nierówność Cauchy'ego; odległość między klasami ciągów jest niezależna od reprezentantów; pusty `X` uwzględniono osobno.
3. **Relacja bliskości i minimalizacja (13-04, 13-05): PASS.** W przechodniości konieczna jest właściwość `B∩B'≠∅`; w minimalizacji do dowodu `F°⊂G` wykorzystuje się wybrany punkt `a∈A∩A'`. Kierunek inkluzji filtrów jest poprawny.
4. **Uzupełnienie przez minimalne filtry (13-06): PASS.** Dla relacji `Ê` skontrolowano przekątną, odwrotności i składanie. W dowodzie zupełności filtra `H` na `X̂` weryfikowano odrębnie niepustość `B(H,E)`, użycie symetrycznego `D` dla zmiany orientacji `(F,ι(x))`, oszacowanie `B(H,D)^2⊂D³` po przeniesieniu przez `ι` oraz końcowy łańcuch `D²∘D²⊂D⁴⊂E`. Argument korzysta z minimalnego przedstawiciela `G°`, nie wymaga arbitralnego wybierania granicy.
5. **Rozszerzenie i własność uniwersalna (13-07, 13-08): PASS.** Dla dwóch filtrów obrazowych otrzymujemy najpierw przynależność pary granic do domknięcia `W` w `Y×Y`. Uzasadnienie `cl W⊂W³⊂V` opiera się na tym, że sekcje relacji jednostajnej zawierają otwarte otoczenia odpowiednich punktów. Jednoznaczność rozszerzenia wymaga Hausdorffowości celu; założenie jest obecne.
6. **Podprzestrzenie (13-09): PASS.** W kierunku odwrotnym filtr na `A` z bazą `A∩E[x]` zbiega do `x` po przeniesieniu do `X`; rozdzielanie `X` wymusza zgodność granic. Przypadek pustej podprzestrzeni nie stanowi wyjątku.
7. **Argumenty poza dziewięcioma środowiskami dowodów: PASS.** Oddzielnie sprawdzono iloraz przez `R=⋂U` dla nierozdzielających przestrzeni (warunek `D³⊂E`, rozdzielanie ilorazu), przykład `arctan`, produkt zupełnych przestrzeni jednostajnych, pusty produkt i zupełność zwartych przestrzeni jednostajnych.

## Niezależny test modeli skończonych

Wykonano enumerację **wszystkich podziałów zbiorów o 0–5 elementach** (struktury jednostajne skończonych zbiorów, których najmniejszą relacją jest relacja równoważności). Dla każdej niepustej podrodziny `A` sprawdzono, czy filtr główny `F_A` jest Cauchy'ego; dla każdej pary filtrów Cauchy'ego porównano warunek bliskości z przynależnością ich generatorów do tej samej klasy. Sprawdzono również, że minimalność względem inkluzji filtrów jest równoważna generatorowi będącemu całą klasą równoważności.

| Liczba punktów | Modele | Generatory filtrów Cauchy'ego | Minimalne filtry |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 5 | 3 |
| 3 | 5 | 22 | 10 |
| 4 | 15 | 99 | 37 |
| 5 | 52 | 471 | 151 |
| **Suma** | **76** | **598** | **202** |

**Wynik: 0 naruszeń** sprawdzonych własności (w tym 70 modeli nierozdzielających). Test wykonano jako dodatkowy skrypt kontrolny w bieżącej iteracji, nie jako nowy plik w repozytorium; nie przypisuje mu się statusu testu uruchomionego w CI. Repozytoryjny test `test_general_topology_ch13.py` zawiera osobną regresję modeli do 4 punktów oraz kontrolę orientacji otoczeń jednostajnych.

## Odsyłacze, język i integracja

- W aktualnym rozdziale są **9 otwarć i 9 zamknięć** `proof`, **24 unikatowe etykiety** i **5 odwołań** do **4 istniejących celów**; brak niezdefiniowanych celów lokalnych.
- Przykład `ex:topog-uzupelnienia-arctan` odsyła do **rozdziału 10**; rozdział 10 zawiera `arctan`. Test statyczny utrwala właśnie ten odsyłacz.
- `catalog/books.json` wskazuje plik jako rozdział nr 13; `books/pl/general_topology.tex` rzeczywiście go dołącza.
- W pliku nie stwierdzono niedozwolonych terminów „zwartościowanie” ani „zbieżność zwarta”. Przykłady odróżniają zgodność topologii od zgodności struktur jednostajnych.

## CI i decyzja

Potwierdzono rzeczywisty status `completed/success` dla workflow [45142384154](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142384154) (poprawka źródła, commit `175cda1e`), [45142452915](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142452915) (test regresyjny, commit `6f5ba48b`) oraz [45142948686](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142948686) (późniejszy sukces walidacji topologii na `abf50f65`). Ostatni z tych przebiegów nie jest deklarowany jako test HEAD po dopisaniu niniejszego raportu.

**Werdykt: drugi czysty reaudyt 13 — PASS.** Matematyka: 9/9 dowodów nadal poprawnych; dodatkowo sprawdzono argumenty pomocnicze. Źródło i test pozostają bez zmian. Pozostał **jeden końcowy audyt potwierdzający (2+1)**: kontrola zgodności blobów i zatwierdzonych wyników CI przed uznaniem poprawionej wersji rozdziału 13 za stabilną. Potem przejść do pełnej indywidualnej dokumentacji dowodów rozdziałów 24–26 (łącznie 44), nie mieszać jej ze starszymi lokalnymi 2+1.
