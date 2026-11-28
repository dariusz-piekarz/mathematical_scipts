# Topologia ogólna — rozdział 10, audyt 2

- **Rozdział:** Metryzowalność przestrzeni topologicznych.
- **Wersja robocza po audycie:** 0.2.
- **Status:** audyt 2 zakończony z poprawkami; czyste audyty **0/2**.
- **Plik:** `chapters/pl/general_topology/10-metryzowalnosc.tex`.
- **SHA-256 źródła:** `ad5de242b4dd63fdadea8eb5228e910e774147396f06dfe04611b1b150a4f088`.
- **Integracja na GitHubie:** nie; oczekujemy dwóch kolejnych czystych audytów.

## Matematyka — ponowny audyt niezależny

Sprawdzono kolejno całość 765 wierszy wersji 0.1, w tym:

1. Aksjomaty pseudometryki, bazowość kul i pierwszy aksjomat przeliczalności;
   implikację metryzowalność ⇒ $T_3$.
2. Zgodność metryk ograniczonych, metryzowalność podprzestrzeni i przenoszenie
   metryki przez homeomorfizm.
3. Lemat regularność + Lindelöf ⇒ normalność, w tym przypadki pustych zbiorów
   domkniętych, wybrane przeliczalne podpokrycia i argument rozłączności.
4. Konstrukcję metryki w twierdzeniu Urysohna: pary bazowe $(B,C)$,
   normalność, funkcje Urysohna, sumę ważoną, dodatnią określoność, obie
   inkluzje topologii i poprawną otwartość *całej* kuli.
5. Metrykę na przeliczalnej kostce, zanurzenie w kostkę Hilberta,
   przeliczalne iloczyny metryzowalnych przestrzeni i przypadek zwarty Hausdorffa.
6. Kontrprzykłady: prosta Sorgenfreya, kostka nieprzeliczalna, iloraz
   z dwoma początkami oraz rozróżnienie zgodności i zupełności metryki.

Nie wykryto kolejnej luki w zasadniczych dowodach. Ujawniono natomiast
jedno mylące sformułowanie dotyczące jednoznaczności bazy.

## Usterka i korekta

W uwadze 10.1.6 (nieprzeliczalna przestrzeń dyskretna) było
„jego jedyna baza ... musi zawierać wszystkie singletony”. Taka fraza
mogła błędnie sugerować, że przestrzeń dyskretna ma **jedną jedyną** bazę.
To nieprawda: baza dyskretna może zawierać wszystkie singletony oraz
inne zbiory otwarte.

Zmieniono na jawne stwierdzenie: **każda baza** $\mathcal A$ topologii
przestrzeni nieprzeliczalnej $X$ zawiera każdy singleton: dla $x\in X$
otwartość $\{x\}$ daje $A\in\mathcal A$ z $x\in A\subseteq\{x\}$,
a zatem $A=\{x\}$. Dzięki temu każda taka baza jest nieprzeliczalna.
Jawnie oznaczono też zbiór $X$ i metrykę $d$.

Dodano test regresyjny w `tools/tests/test_general_topology_ch10.py`.

## Testy i kompilacja po poprawce

- Pełna walidacja `bash tools/validate_general_topology_ch10.sh`: **PASS**.
- Modele skończone: 390 topologii, siedem metryk rozdzielających,
  1295 trójek dla metryk oraz 551880 trójek dla iloczynów: **PASS**.
- Wszystkie testy regresyjne rozdziałów 01–10: **PASS**.
- Etykiety i odsyłacze: 393 unikatowe etykiety i 104 rozwiązane odsyłacze.
- Globalna terminologia, w tym „spełnia pierwszy/drugi aksjomat przeliczalności”: **PASS**.
- Kompilacja samodzielnego rozdziału: **8 stron**, zero ostrzeżeń.
- Kompilacja całej książki: **88 stron**, zero ostrzeżeń.
- Wyrenderowano osiem stron po zmianie; poprawione zdanie na stronie 2
  oraz oba rysunki są czytelne, bez ucięć, nachodzenia lub sierot.

## Licznik czystych audytów

Ponieważ poprawiono sformułowanie nieścisłe matematycznie,
**audyt 2 nie jest czysty; 0/2**. Kolejnym etapem jest audyt 3
wersji 0.2. Nie dodano żadnych nowych twierdzeń ani przykładów.
