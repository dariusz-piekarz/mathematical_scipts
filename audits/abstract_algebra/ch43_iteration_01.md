# AA-43 — iteracja 1: ciała różniczkowe, derywacje i rozszerzenia

**Data:** 23 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; **gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Geneza i zakres

**AA-43 nie istniał w kanonicznym tomie AA-01–AA-42**. Podstawą redakcji jest niewłączona część rozdziału „Ciała różniczkowe i twierdzenie Liouville'a” ze starszego skryptu `sources/pl/galois(2).tex` (początek od wiersza 802); jej materiał uporządkowano, rozwinięto i oddzielono od pełnego twierdzenia Liouville'a, które jest przeznaczone do osobnego AA-44. Zachowano rozdział tematyczny: AA-43 obejmuje pojęcia i narzędzia, AA-44 ma dotyczyć całkowania elementarnego.

Nowy plik: `chapters/pl/abstract_algebra/43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex`, blob `bf6dd89fe03aa1729b0c3e93cbda434ca09f77be`, **523 wiersze**, **20 unikatowych etykiet**, **4 odsyłacze**, **6 pełnych dowodów**, **9 przykładów**, dodatkowo definicje, uwagi i wnioski.

## Kontrola matematyczna pierwszej iteracji

### A. Definicje i aksjomaty

Derywacja jest zdefiniowana na ciele charakterystyki zero. Reguły odwrotności i ilorazu wyprowadzono ze zwykłej reguły Leibniza, a ciało stałych jawnie zdefiniowano jako jądro derywacji. Przykład \(\mathbb C(x)\) obejmuje dowód, że jedyne elementy o zerowej pochodnej to funkcje stałe; wykonano go bez zakładania algebraicznej domkniętości ciała współczynników.

Dodano kontrprzykłady z charakterystyki dodatniej: \(D(x^p)=0\) oraz niemożność przedłużenia \(D(x)=1\) na rozszerzenie wyznaczone przez \(\alpha^p=x\). Kontrprzykłady pokazują, dlaczego w późniejszych twierdzeniach konieczna jest charakterystyka zero.

### B. Jednoznaczne przedłużenie na rozszerzenie algebraiczne

Przy elementarnym generatorze algebraicznym \(\alpha\) wzór
\(D\alpha=-m_\alpha^D(\alpha)/m_\alpha'(\alpha)\)
ma niezerowy mianownik ze względu na rozdzielczość w charakterystyce zero. Sprawdzono potrzebne osobno przejścia:
1. wyprowadzenie wzoru z równania minimalnego;
2. niezależność obliczenia \(D(f(\alpha))\) od przedstawiciela modulo wielomian minimalny;
3. zachowanie reguł derywacji na \(K[\alpha]\) i ich przejście na \(K(\alpha)\);
4. indukcja po skończonej liczbie generatorów i zgodność przedłużeń na podrozszerzeniach skończonych dowolnego rozszerzenia algebraicznego.

### C. Ciało stałych i zakres hipotez

Jeśli \(C_K\) jest algebraicznie domknięte, algebraiczne rozszerzenie \(L/K\) nie dodaje nowych stałych: dla stałej algebraicznej \(\alpha\) wielomian współczynników pochodnych ma stopień mniejszy niż wielomian minimalny. Zatem musi być zerowy, a \(\alpha\) jest algebraiczna nad \(C_K\). Bez domkniętości hipoteza jest niezbędna: przykład \(\mathbb Q(x)\subset\mathbb Q(i)(x)\) dodaje nową stałą \(i\).

### D. Derywacja śladu i normy

Dla skończonego \(L/K\) twierdzenie o pochodnej śladu i normy nie zakłada normalności, ale wymaga rozdzielczości, zagwarantowanej w charakterystyce zero. Dowód używa wszystkich zanurzeń do domknięcia algebraicznego i faktu, że zanurzenia komutują z jedynym przedłużeniem derywacji. Porównano tezy z `aa:tw:trace-norm-embeddings` w AA-23 i przykład z \(\alpha^2=x^2+1\).

### E. Przestępne kroki i nowe stałe

Dla przestępnego \(t\) z \(Dt=a\in K\) dowiedziono, że
\(C_{K(t)}=C_K\) wtedy i tylko wtedy, gdy w \(K\)
**nie istnieje** \(b\) z \(Db=a\).
Dowód korzysta z formalnego rozwinięcia Laurenta w nieskończoności; osobno traktuje wyraz najwyższego stopnia \(m=0\), którego odjęcie pozostawia niezerową sumę z najwyższym wykładnikiem \(m<0\). Ujemne wykładniki są niezbędne: pominięcie ich tworzyłoby lukę.

Dla \(Dt=ht\) analogicznie udowodniono dokładne kryterium:
nie może istnieć \(m\in\mathbb Z\setminus\{0\}\)
i \(u\in K^\times\) z \(Du/u=-mh\).
Wykorzystano porównanie najwyższego współczynnika szeregu. Dla \(K=\mathbb C(x)\) osobno wykazano, że logarytmiczna pochodna niezerowej funkcji wymiernej ma zerową część wielomianową, więc nie może być niezerową stałą.

Przykłady \(D\ell=1/x\), \(Dt=t\) i \(Dt=1\) rozdzielają rozszerzenia bez nowych stałych od takich, w których istnieje nowa stała \(t-x\). W przykładzie \(e^x\) podano dodatkowo **algebraiczny dowód przestępności**, wykorzystując normę i ślad, zamiast przyjmować ją bez dowodu.

### F. Poprawna definicja elementarności

Definicja kroków elementarnych wyraźnie oddziela:
- dołączanie elementów algebraicznych;
- kroki logarytmiczne \(D\theta=Du/u\);
- kroki wykładnicze \(D\theta/\theta=Dv\).

**Nie** zastąpiono dołączania logarytmu dowolnym krokiem \(D\theta=a\): ten drugi obejmowałby arbitralne całki i prowadził do pojęcia rozszerzenia liouvillowskiego. Końcowy warunek braku nowych stałych jest zapisany wprost. Przykład automorfizmów wykładniczych i logarytmicznych kontroluje ich zgodność z derywacją i działaniem na generatorach.

## Testy niezależne

Nowe pliki testowe:
- `tools/tests/test_abstract_algebra_ch43.py`: niezależna symboliczna kontrola reguły pochodnej, rozszerzeń kwadratowych, normy/śladu, pochodnych logarytmicznych, derywacji na \(K(t)\) i automorfizmów różniczkowych;
- `tools/tests/test_abstract_algebra_ch43_independent.py`: **bez SymPy**, czysta arytmetyka dokładna `fractions.Fraction`, model \(\mathbb Q(x)[\alpha]/(\alpha^2+b(x)\alpha+c(x))\), sprawdzający wymuszoną pochodną elementu algebraicznego, Leibniza, normę i ślad oraz rozkłady pochodnych logarytmicznych.

Werdykt testowy należy opierać na rzeczywistym wyniku CI; samo dodanie testów nie uzasadnia oznaczenia rozdziału jako stabilnego.

## Struktura i integracja

Kontrola tekstu źródłowego: **20/20 unikatowych etykiet**, **4** odsyłacze, poprawne sparowanie wszystkich środowisk `\begin`/`\end`. Cele zewnętrzne to `aa:wn:charzero-separable` (AA-20) i `aa:tw:trace-norm-embeddings` (AA-23), obecne w kanonicznym tomie.

Wprowadzając AA-43 do książki, należy:
1. dopisać `\input` w `books/pl/abstract_algebra.tex` po AA-42;
2. dodać pozycję w `catalog/books.json`;
3. włączyć dwa testy do `.github/workflows/abstract-algebra-chapter.yml`;
4. zmienić globalną bramkę strukturalną na **43** rozdziały i zachować odrębny historyczny raport globalnego audytu AA-01–AA-42;
5. dopiero po zielonym CI oraz oględzinach kompletnego, nowego PDF i osobnym niezależnym przeglądzie dowodów ustabilizować AA-43.

## Stan

**Pierwsza iteracja: rozdział napisany, pierwszy audyt merytoryczny wykonany; stabilność przed uruchomieniem CI niepotwierdzona.** Następna iteracja, po wykryciu i skorygowaniu wszystkich problemów, powinna dokończyć stabilizację AA-43. Dopiero potem rozbudowujemy książkę o AA-44 (twierdzenie Liouville'a).
