# Algebra liniowa — audyt globalny, iteracja 16: fundamenty LA01–05 i most LA12–13

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Poprzednio:** [iteracja 15](iteration_15.md).
**Wynik:** **CZYSTY W ZBADANYM ZAKRESIE**, bez zmian w matematycznych źródłach. **GLOBALNY AUDYT WSZYSTKICH 382 DOWODÓW POZOSTAJE OTWARTY**.

## 1. Zakres i niezmienne źródła

| Rozdział | SHA źródła | Wiersze | Środowiska proof | Etykiety / odsyłacze |
| --- | --- | ---: | ---: | ---: |
| LA01 | `374e74dfa46f72597abcb8f5721268fed2245c4a` | 1722 | 24 | 69 / 27 |
| LA02 | `1e59c0d13379ee7851f3a6386172640b02f9fa75` | 1089 | 16 | 39 / 17 |
| LA03 | `7ee828f8438e6030cb7f47685433aa3639220ab7` | 1019 | 17 | 42 / 19 |
| LA04 | `6bc9a3c2de2d09c5f67e9ba032fac387b3bcb36e` | 1221 | 15 | 49 / 24 |
| LA05 | `c238cb3232b69fb19d0dfe1062af05a2a0d8ddb8` | 752 | 10 | 27 / 16 |
| LA12 | `ded0c69dc298d00842d4009073e2444e1037952a` | 1064 | 13 | 36 / 9 |
| LA13 | `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af` | 1305 | 15 | 34 / 18 |
| **Razem** | | **8172** | **110** | **296 / 130** |

Odczytano i skontrolowano wybrane pełne twierdzenia z ich dowodami, w szczególności wskazane poniżej. **110 to liczba istniejących środowisk dowodowych w 7 rozdziałach, nie liczba indywidualnie certyfikowanych dowodów**.

## 2. Krytyczna kontrola hipotez i rozumowań

### LA01: skończony wymiar i aksjomat wyboru

- Lemat Steinitza (`thm:lin-steinitz`): w kroku indukcji współczynnik przy którymś niewymienionym generatorze musi być niezerowy; dzięki temu wolno rzeczywiście rozwiązać równość względem usuwanego generatora. Przypadki `r=0`, `m=0` i `r>m` nie wymuszają dodatkowych hipotez.
- Skończona suma mnogościowa właściwych podprzestrzeni (`thm:lin-skonczona-unia-nieskonczone-cialo`): argument wymaga nieskończoności ciała; minimalne pokrycie daje dwa odpowiednio wybrane wektory, a dla pozostałych składników co najwyżej jedną wartość parametru. **Kontrprzykład do usunięcia hipotezy:** `F₂²` jest sumą mnogościową trzech swoich jednowymiarowych podprzestrzeni. Jest to niezależny test granicy twierdzenia; nie dodawano go do zatwierdzonego rozdziału.
- Łańcuch rodzin niezależnych i dwa zastosowania lematu Zorna (`lem:lin-lancuchy`, `thm:lin-istnienie-bazy-zorn`, `thm:lin-baza-z-generatorow-zorn`): w dowodzie jawnie badany jest łańcuch pusty, a dla niepustego każda skończona kombinacja należy do jednego elementu łańcucha. Maksymalność implikuje rozpinanie, ponieważ dołączenie wektora spoza rozpiętości zachowuje niezależność. Przyjęcie AC jest wyraźne.
- Współrzędne Hamela (`thm:lin-wspolrzedne-hamela`): wyjaśniono skończone nośniki, przypadek pustej bazy i liniowość odwrotnego odwzorowania współrzędnych.

### LA02: nieskończony wymiar i ilorazy

- Równoliczność baz (`lem:lin2-moce-nosnikow`, `thm:lin2-jednakowa-moc-baz`): konstrukcja iniekcji ze sumy skończonych nośników do `I×N₀` prawidłowo używa dobrego uporządkowania, a więc AC. Dwa oszacowania kardynalne kończy Cantor–Bernstein. Przypadek bazy skończonej jest osobno uzasadniony.
- Wzór `dim(U+W)+dim(U∩W)=dim U+dim W` (`thm:lin2-wzor-wymiarowy`): wspólna baza przecięcia i jej dwa rozszerzenia dają niezależny zbiór `C∪A∪D`; dowód unika niedozwolonego odejmowania nieskończonych liczb kardynalnych.
- Iloraz (`thm:lin2-struktura-ilorazu`, `thm:lin2-iloraz-dopelnienie`, `thm:lin2-iloraz-sumy`): działania nie zależą od przedstawicieli, izomorfizmy mają dobrze określone odwzorowania, jądra i surjektywność. Przypadek skończony odróżniono od użycia AC przy wyborze dopełnienia.

### LA03–05: jądro, macierze i eliminacja

- Rozszerzenie wartości z bazy (`thm:lin3-przedluzenie-z-bazy`) i równość wymiarów jądra/obrazu (`thm:lin3-rzad-nullity`): skończoność nośnika oraz rozłączność bazy jądra i dopełniających ją wektorów zapewniają nie tylko rozpinanie obrazu, lecz także niezależność jego obrazów. Nie odejmuje się kardynałów.
- Pierwsze twierdzenie o izomorfizmie (`thm:lin3-pierwsze-izo`): sprawdzono przedstawicieli warstw, liniowość, jądro i surjektywność bez wyboru bazy.
- Zmiana bazy (`thm:lin4-zmiana-wspolrzednych`, `thm:lin4-zmiana-macierzy`): `P_{B←B'}` przekształca współrzędne **z B' do B**, a przy bazach `B,B'` i `C,C'` poprawna transformacja macierzy to `Q⁻¹ A P`; dla endomorfizmu otrzymujemy `P⁻¹ A P`.
- Eliminacja i zredukowana postać schodkowa (`thm:lin5-gauss`, `thm:lin5-jednoznacznosc-rref`): pivoty rosną, operacje są odwracalne; jednoznaczność RREF wynika z niezmienniczości przestrzeni wierszy i współrzędnych w kolumnach bazowych. W `thm:lin5-baza-obrazu` do bazy obrazu bierze się **kolumny pierwotnej macierzy**, nie kolumny RREF.

### LA12–13: rzeczywista i zespolona ortogonalność

- Polaryzacja (`thm:lin12-polaryzacja`): znak `−i(q(u+iv)−q(u−iv))` jest zgodny z konwencją **antyliniowości w pierwszym argumencie**. Dla `h(1,i)=i` wzór oddaje część urojoną poprawnie.
- Riesz (`thm:lin12-riesz`): dla liniowego funkcjonału `F` poprawny reprezentant to `a=Σ conjugate(F(e_j))e_j`; identyfikacja `V→V*` jest w przypadku zespolonym **antyliniowa**. Nie rozszerza się twierdzenia na ogólne niezupelne przestrzenie nieskończonego wymiaru.
- Rzut i Gram (`thm:lin13-rozklad`, `thm:lin13-projection-gram`): w niekoniecznie skończenie wymiarowym `V` rozkład ortogonalny jest wyprowadzony jedynie dla skończenie wymiarowej podprzestrzeni `U`. Dla pełnej rangi kolumn `B`, `B(B*B)⁻¹B*` jest idempotentna i hermitowska; konwencja odpowiada ortogonalności reszty.
- **Negatywny test hipotez:** w przestrzeni skończonych ciągów `c₀₀` ze standardowym iloczynem skalarnym podprzestrzeń `U={x: Σ_{n≥1}n x_n=0}` ma `U^⊥={0}`, mimo że `U≠V`. Dowodzi to, że nie wolno rozszerzyć `V=U⊕U^⊥` na dowolne nieskończenie wymiarowe `U` w ogólnej przestrzeni z iloczynem skalarnym. Uwaga `rem:lin13-nieskonczony` już zawiera potrzebne zastrzeżenie; kontrprzykład jest opcjonalnym uzupełnieniem i **nie został dopisany do tekstu**.

## 3. Nowa niezależna regresja rachunkowa

Wykonano lokalnie skrypt `la_global16_checks.py` (ustalone ziarno `2026112216`), SHA256:
`b4e6bc09f1eafb2ed522c3c9c5da88017649a6c672f5da45e07b86f1c4219b8b`.

| Zakres | Asercje PASS |
| --- | ---: |
| Dokładna RREF i zgodność przestrzeni wierszy nad `F₂,F₃` | 4158 |
| Dokładne jądro, obraz i pivoty nad `F₂,F₃` | 2772 |
| `Q⁻¹ A P` i zgodność współrzędnych nad `F₂,F₃` | 3000 |
| Zespolone projektory Grama, idempotencja, ortogonalność i antyliniowość Riesza | 6000 |
| **Razem** | **15930 / 15930 PASS** |

W rodzinach skończonych enumerowano wszystkie macierze dla rozmiarów `(p,m,n)=(2,2,3),(2,3,3),(3,2,2),(3,2,3)`; testy odwzorowań bazowych i zespolonych używają stałych ziaren losowych. Testy zespolone porównują wyrażenia z tolerancją numeryczną. Testy nie formalizują ani nie dowodzą lematu Zorna czy twierdzeń uniwersalnych.

## 4. Kontrole techniczne i ograniczenia

- Bezpośredni odczyt siedmiu źródeł potwierdził wskazane bloby.
- W siedmiu plikach stwierdzono **0** błędnie zagnieżdżonych/niedomkniętych środowisk `begin/end` i **0** zduplikowanych etykiet w pojedynczych źródłach.
- W rozdziale LA01 słowo `unia` występuje wyłącznie w stabilnych nazwach `\label` i `\ref`; nie jako polskie określenie sumy zbiorów. **Nie zmieniano stabilnych etykiet**.
- Lokalnych odsyłaczy do obcych rozdziałów nie zaliczano fałszywie do braków; pełna globalna kontrola 32 rozdziałów oraz 1083 etykiet / 660 odsyłaczy była udokumentowana w iteracji 15.
- **Brak nowej kompilacji PDF/nowego CI w tej iteracji.** Istniejący [run 45047971276](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047971276) ma `completed/success` i był wcześniej powiązany z identycznymi źródłami; nie poświadcza on nowego pliku raportu ani wszelkich równoległych zmian aplikacji.
- Kontrola analizowanych dowodów jest niezależnym audytem matematycznym, **nie jest ich formalną certyfikacją w Lean** ani pełną, krokową inspekcją wszystkich 110 środowisk.

## 5. Decyzja i dalszy plan

**Iteracja 16: czysta w kontrolowanych argumentach i rachunkach.** Nie znaleziono błędu wymagającego korekty rozdziału. Zamknięta stabilizacja rozdziałowa LA12–32 pozostaje w mocy.

**Następna iteracja 17:** pełniejsze, indywidualne rozpisanie i sceptyczny audyt dowodów LA01–05 nieuwzględnionych krok po kroku w tej kontroli, następnie LA12–13; zwłaszcza interakcje rzędu, ilorazu, przypadków zera i uogólnień bez AC. Weryfikować w rejestrze status każdego sprawdzonego dowodu osobno, nie wyciągać z `PASS`/CI wniosku o pełnej certyfikacji wszystkich **382** dowodów. Po zakończeniu tej pracy przeprowadzić jeden dodatkowy sceptyczny audyt globalny.
