# Algebra liniowa — audyt globalny, iteracja 10 (całościowe odsyłacze i zależności)

**Data:** 2026-11-22. **Repozytorium:** `dariusz-piekarz/mathematical_scipts`. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zakres:** wszystkie 32 aktualne pliki rozdziałów, plik książki, krzyżowe odsyłacze, integralność LaTeX, terminologia, porównanie potencjalnych nakładek, kontrola najnowszego dodatku Penrose’a i rzeczywiste wyniki CI.
**Decyzja:** **audyt strukturalno-integracyjny i kontrola wizualna PDF CZYSTE; pełny, niezależny audyt matematyczny wszystkich dowodów nadal OTWARTY**. To nowa iteracja następująca po historycznym audycie 09 (który wprost oznaczono jako częściowy), a nie ponowne uruchomienie zakończonej kolejki LA-12–32.

## Inwentarz pełny, a nie próbka

Odczytano treść wszystkich 32 rozdziałów z GitHub na bieżącej gałęzi. Zapisano dwa reprodukowalne, maszynowo czytelne inwentarze:
- [Rozdziały 01–16](iteration_10_inventory_01_16.json), commit `f3bba12d33672929eaaaa77ac7db4ba717509d00`;
- [Rozdziały 17–32](iteration_10_inventory_17_32.json), commit `e55a778084ed1f679fa9de311266604a952cf263`.

Dla każdego rozdziału zachowano SHA źródła, liczbę wierszy, komplet `\label`, komplet `\ref/\eqref/\pageref/\autoref/\nameref/\cref/\Cref/\vref` z rozwinięciem list argumentów, liczbę `proof` i `figure`, pary `\begin/\end` oraz trafienia niedozwolonej terminologii poza komentarzami, etykietami i indeksami. Następnie scalono inwentarze i porównano SHA 32 plików z aktualnym drzewem repozytorium (brak rozbieżności).

| Kontrola | Zweryfikowany wynik |
|---|---:|
| Pliki źródeł rozdziałów | **32** |
| Wiersze źródeł | **37 466** |
| Pliki dokładnie zgodne z kolejnością `\input` w `books/pl/linear_algebra.tex` | **32/32** |
| Wszystkie `\label` | **1083** |
| Zduplikowane etykiety (w całej książce) | **0** |
| Wszystkie rozpoznane odsyłacze | **659** |
| Odsyłacze bez rozstrzygniętego celu | **0** |
| Różne skierowane zależności między rozdziałami | **85** |
| Odsyłacze w przód książki | **1** |
| Środowiska `proof` | **382** |
| Środowiska `figure` | **21** |
| Niedomknięte lub błędnie zagnieżdżone środowiska | **0** |
| Trafienia skanowanych niedozwolonych określeń w prozie | **0** |

**Uwaga o zakresie narzędzia:** to analiza statyczna bez rozwijania złożonych makr TeX i bez formalnego sprawdzenia wszystkich 382 dowodów. Lista skanowanych komend odsyłaczy jest jawna, więc nie przypisujemy narzędziu obsługi dowolnych przyszłych makr.

## Ocena zależności merytorycznych

**Jedyny odsyłacz w przód:** rozdział 08, wiersz 19, do `ch:lin10-iloczyny-tensorowe`. Jego kontekst brzmi „Nie będziemy jeszcze zakładać istnienia iloczynów tensorowych; ich konstrukcja jest tematem Rozdziału ...”. Jest to **zapowiedź**, a nie użycie twierdzenia bez dowodu. Nie wymaga przeniesienia rozdziału 10.

**Potencjalne nakładki, porównane na źródłach i pozostawione bez zmian:**

1. **LA-09 i LA-12 — Grama–Schmidta:** LA-09 udowadnia ortogonalizację dla rzeczywistej dodatnio określonej formy dwuliniowej `b`; LA-12 rozwija wersję `\mathbb C` dla formy półtoraliniowej z kontrolą kolejności argumentów i sprzężenia. Są to warianty o odmiennym zakresie. LA-12 jawnie odsyła do LA-09; mechaniczna deduplikacja straciłaby istotny rachunek.
2. **LA-22 i LA-23 — Lapunow:** LA-22 dotyczy ciągłego równania i stabilności Hurwitza, LA-23 dyskretnego równania Steina, stabilności Schura i próbkowania. Powiązanie jest jawne, zakres matematyczny różny.
3. **LA-24 i LA-26 — Riccati:** LA-24 konstruuje podstawowe zadanie sterowania liniowo-kwadratowego i równania Riccatiego przy wcześniejszych założeniach, LA-26 rozwija teorię do stabilizowalności, wykrywalności i półokreślonego kosztu. LA-26 jawnie wskazuje rozszerzenie LA-24; to potrzebna progresja, nie sprzeczna definicja.
4. **LA-25 i LA-27 — gramiany:** LA-25 koncentruje się na sterowalności, rozkładzie Kalmana i stabilizowalności, a LA-27 rozwija gramiany obserwowalności, minimalne realizacje i faktoryzację Hankela; LA-27 odsyła do podstaw LA-25. Nie utożsamia się gramianu sterowalności z obserwowalności.

Nie stwierdzono w tych czterech sprawdzonych miejscach koniecznej korekty ani podstaw do usunięcia dowodów. To **przegląd wybranych nakładek**, nie automatyczny dowód, że książka nie ma żadnych powtórzeń.

## Nowy materiał Penrose'a w LA-32

Po dodaniu i ustabilizowaniu rozdziału 32 sprawdzono poprawność krzyżowych odsyłaczy do LA-29/31/32 i zgodność lokalnej transformaty z udowodnioną wcześniej incydencją `\omega=X\pi`. Nie zmieniono przyjętej normalizacji `\Box_{\mathbb C}=\partial_{11}\partial_{22}-\partial_{12}\partial_{21}`, jednorodności `-2` ani wzoru przykładu `\Phi(X)=-1/\det X`. Rozróżnienie między lokalną całką konturową i pełnym twierdzeniem `H^1(PT_U,\mathcal O(-2))` jest zgodne z przeglądem Atiyaha, Dunajskiego i Masona, *Twistor theory at fifty* (2017), <https://pmc.ncbi.nlm.nih.gov/articles/PMC5666237/>. **Nie wstawiano do tekstu nieudowodnionego globalnego izomorfizmu.**

W ramach bieżącego audytu ponownie uruchomiono istniejące, niezależne regresje matematyczne lokalne (nie są to nowe, czwarte zestawy):
- `/mnt/data/la30_reaudit05.py`: **1370 PASS** (reprezentacja Clifforda, ślad, łączność);
- `/mnt/data/la31_reaudit03.py`: **6840 PASS** (Spin(3), SU(2), chiralia, kocykl `w_2`);
- `/mnt/data/la32_penrose_skeptical04.py`: **751 PASS** (orientacja i odkształcanie konturu, niezależność od przedstawiciela, incydencja).

Łącznie **8961/8961 PASS** w regresji sprawdzającej integrację rozdziałów 30–32. Skrypty są lokalnymi, odrębnymi implementacjami; ich pozytywny wynik nie stanowi formalnego dowodu matematycznego wszystkich twierdzeń.

## CI i wizualny PDF — dokładny zakres poświadczenia

- [GitHub Actions 45041600675](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041600675) zakończyło się **completed/success** po zapisaniu drugiej części inwentarza. Odczytane źródła rozdziałów oraz główny plik książki były identyczne z aktualnym stanem przy porównaniu SHA. Inny zakończony sukcesem run 45041196120 ma kompletną listę kroków: wszystkie testy rozdziałowe, walidacja terminologii, dwukrotna kompilacja PDF, kontrola nierozstrzygniętych odsyłaczy i ostrzeżeń `Overfull/Underfull/Missing character/LaTeX Warning` oraz przesłanie artefaktu zakończyły się `success`.
- Workflow ma jeden krok `Report pre-existing global library validation issues` z `continue-on-error: true`. Zatem zielone CI **nie oznacza**, że ten miękki test całej biblioteki jest bezbłędny; nie należy tego mylić z rygorystycznymi krokami walidacji książki.
- **Wykonano kontrolę rzeczywistego pełnego PDF po dodatku Penrose'a.** Z zielonego [run 45041600675](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041600675) pobrano oryginalne archiwum GitHub Actions `linear-algebra-ch01-ch32`, artefakt ID **14761539115**, i rozpakowano z niego `linear_algebra.pdf` i `linear_algebra.log` (lokalnie `/mnt/data/la_global_audit10_fullpdf/`). Otwarty PDF ma **318 stron A4**, **32 pozycje rozdziałów w zakładkach**, **0 stron pustych**; według kontroli PyMuPDF **7836 bloków tekstowych**, **0 bloków poza stroną**. W logu **0** trafień `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` i ostrzeżeń o niezdefiniowanych odsyłaczach.
- **Bezpośrednie oględziny:** wyrenderowano **14 arkuszy miniatur** obejmujących **wszystkie strony 1–318** i wizualnie obejrzano każdy arkusz. Wyodrębniono **21 stron z ilustracjami** i obejrzano je w powiększonych zestawieniach; osobno sprawdzono powiększenia stron **299 (Spin(2)), 304 (sfera Blocha), 315 (kontur Penrose'a), 317 (fibracja twistorowa)**. Nie wykryto widocznych kolizji napisów, obcięć ani uszkodzonych rysunków. Do tej kontroli służą lokalne pliki `/mnt/data/la_global_audit10_fullpdf/contact_sheets/`, `selected_pages/` i `figure_collages/`.
- **Granice oględzin:** wszystkie 318 stron oceniono wizualnie na arkuszach miniatur i automatycznie zbadano granice 7836 bloków, natomiast nie otwierano każdej z 318 stron osobno w maksymalnym powiększeniu. Automatyczne nakładanie się prostokątów znaków w składzie wzorów matematycznych generuje liczne fałszywe alarmy; zweryfikowano wzrokowo strony i ilustracje podwyższonego ryzyka. Wynik oznacza pozytywny audyt wizualno-techniczny w tym zakresie, nie formalny dowód, że w każdej formule nie ma drobnej usterki składu.

## Decyzja i następny etap

**ITERACJA 10 WYKONANA.** Integralność międzyrozdziałowa `\input/\label/\ref/\begin/\end`, rozpoznana terminologia oraz wybrane potencjalne duplikaty — **bez koniecznych poprawek w źródłach**. Zakończona wcześniej sekwencja stabilizacji 12–32 **pozostaje zamknięta**, nie resetować jej.

**Audyt globalny całej książki nadal NIEZAMKNIĘTY wyłącznie w zakresie pełnej, niezależnej kontroli matematycznej wszystkich 382 dowodów.** Kontrola strukturalna i wizualna całego 318-stronicowego PDF została wykonana z dodatnim wynikiem opisanym powyżej. W kolejnej iteracji należy pogłębić niezależny przegląd matematyczny rozdziałów 06–11, sprawdzić trudniejsze zależności między 14–20 i 22–28 oraz nie powtarzać ukończonej kolejki stabilizacji 12–32 bez nowej, konkretnej usterki.
