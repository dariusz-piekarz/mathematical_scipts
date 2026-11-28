# Topologia ogólna — audyt globalny 45: rzeczywista weryfikacja zewnętrznej zależności Brouwera

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Cel:** sprawdzić, czy wniosek o wymiarze sześcianu korzysta z faktycznie obecnego, udowodnionego wyniku z Biblioteki matematycznej, a nie tylko z bibliograficznej obietnicy.

## 1. Zweryfikowane połączenie źródeł

| Rola | Źródło i jego aktualny blob | Potwierdzony punkt |
|---|---|---|
| Konsument | `chapters/pl/general_topology/23-wymiar-topologiczny.tex`, blob `9dc1ed4784d929b405d00a3216865418f240a37c` | Uwaga przy wierszach 810–820, lemat Poincarégo–Mirandy, dowód 836–881, i twierdzenie o wymiarze sześcianu, dowód 937–1033 |
| Dostawca | `chapters/pl/algebraic_topology/19-stopien-indeks-punktu-stalego-i-twierdzenie-lefschetza.tex`, blob `5cb2a5022dfe141f07732f5907994c2ec103dad9` | Wniosek „Twierdzenie Brouwera” od wiersza 160 oraz jego dowód, korzystający z `thm:lefschetz-v10` |
| Książka topologii ogólnej | `books/pl/general_topology.tex`, blob `e1a30ad1c4e33c9361d12f52488a8f4d3f3d3da8` | Rzeczywiste `\input` rozdziału 23 (wiersz 79) |
| Książka topologii algebraicznej | `books/pl/algebraic_topology.tex`, blob `ad6be7208779e91c92d3617b0757a54f4fd6480d` | Rzeczywiste `\input` rozdziału 19 (wiersz 103) |

Sprawdzono pełne wskazane źródła na bieżącej gałęzi GitHub. Nie opierano się na samym opisie katalogowym ani na domniemanych nazwach rozdziałów. Rozdział 23 zawiera **tekstowy odsyłacz** do skryptu „Topologia algebraiczna”, a nie działający międzyksiążkowy `\ref`; nie należy tego tekstowego odsyłacza raportować jako sprawdzonego hiperłącza.

## 2. Konkretny ciąg zależności matematycznych

1. W `AT-19` lemat `lem:hopf-trace-v10` dowodzi tożsamości naprzemiennych śladów na ograniczonym kompleksie łańcuchowym i jego homologii.
2. Twierdzenie `thm:lefschetz-v10` pokazuje, że dla ciągłego f na skończonym CW-kompleksie warunek `L(f)≠0` implikuje punkt stały. W przypadku wielościanów dowód używa aproksymacji symplicjalnej i zerowania diagonalnych współczynników przy braku punktu stałego.
3. **Istotne zastrzeżenie:** rozszerzenie tego twierdzenia na wszystkie skończone CW-kompleksy w `AT-19` opiera się dodatkowo na klasycznym twierdzeniu, że skończone CW-kompleksy są metryzowalnymi ANR i mogą być retraktami odpowiednich otoczeń. To twierdzenie ANR jest **przyjęte**, nie udowodnione od podstaw we wskazanym fragmencie. Nie można więc reklamować całego łańcucha jako samodzielnego dowodu od aksjomatów.
4. We wniosku „Twierdzenie Brouwera” w `AT-19` zastosowano `L(f)=1` dla kontraktywnego dysku `D^n`, który jest skończonym wielościanem z dokładnością do homeomorfizmu. Ponieważ dysk jest sam wielościanem, do *tego konkretnego wniosku* wystarcza wcześniejszy **przypadek wielościanowy** argumentu Lefschetza; nie ma potrzeby wykorzystywania zależności ANR dla dowolnego CW-kompleksu.
5. Rozdział 23 „Topologii ogólnej” używa twierdzenia Brouwera w dowodzie lematu `lem:topog23-poincare-miranda`: funkcja `T(x)=P(x-f(x))` przenosi sześcian w siebie. Zweryfikowano poprawność radialnego homeomorfizmu sześcianu na kulę, a warunki znaków na ścianach zapewniają, że punkt stały T leży we wnętrzu i ma `f(x)=0`.
6. W dowodzie `thm:topog23-cube-dimension` lematu Poincarégo–Mirandy używa się do dolnego oszacowania `dim [0,1]^n≥n` przez skonstruowanie funkcji o właściwych znakach, która przy hipotetycznym rozdrobnieniu rzędu n nie może przyjąć wartości 0. Górne oszacowanie pochodzi z rozdrobnienia siatki i triangulacji (wewnętrzne lematy rozdziału 23). **Nie ma kołowego użycia tezy o wymiarze sześcianu** w podanym łańcuchu.

## 3. Weryfikacja istniejącego audytu dostawcy

Odczytano raport `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_19_20_2026-11-20.md`, który omawia wprost `AT-19`, stopień, lemat śladu, twierdzenie Lefschetza i wniosek Brouwera. Raport rozróżnia samodzielny przypadek symplicjalny oraz klasyczną zależność ANR; wpisuje dla `AT-19` status „zaakceptowany z zastrzeżeniem” z powodu dalszej formuły indeksowej dla rozmaitości nieorientowalnych (używa odrębnego twierdzenia ze współczynnikami lokalnymi). **To zastrzeżenie nie dotyczy samego wniosku Brouwera dla dysku** i nie unieważnia go.

W raporcie źródłowym odnotowano historyczny udany workflow `44794340616` dla `AT-19/20` i 217-stronicowy PDF. Jest to informacja z tego raportu; w tej iteracji nie pobierano ani nie oglądano ponownie tego PDF, więc nie należy liczyć go jako nowego przeglądu wizualnego. Sama bieżąca kontrola łańcucha źródłowego nie zmienia ani `.tex`, ani testów.

## 4. Werdykt i następne kroki

**PASS zgodności zależności zewnętrznej:** twierdzenie Brouwera w rozdziale 23 ma rzeczywistą implementację tekstową i dowód w rozdziale 19 „Topologii algebraicznej”, oba pliki są dołączone do swoich książek. Potrzebna zależność Brouwera jest jasno nazwana, a przypadek dysku opiera się na wielościanowej części twierdzenia Lefschetza. Nie ogłaszamy zamknięcia *wszystkich* zewnętrznych zależności obu książek.

**Otwarte dla globalnego PASS:** przegląd zasięgu poprzednich kontroli rozdziałów 01–26 na nowym finalnym HEAD, rygorystyczne rozróżnienie zależności przyjętych od dowiedzionych, i zielony CI finalnego commitu. Nie zmieniono żadnego źródła ani etykiety. Automatyzacja audytów powinna pozostać aktywna.
