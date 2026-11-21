# Topologia algebraiczna — TOP-16, audyty I–V

**Data:** 21 listopada 2026.  
**Źródło:** `chapters/pl/algebraic_topology/16-zawieszenie-twierdzenie-freudenthala-i-homotopia-stabilna.tex`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Zasady:** wielokrotny audyt istniejącego rozdziału; bez dodawania nowych twierdzeń, lematów i rozdziałów.

## Audyt I — kompletna lektura, stabilność i widmo HA

Przeczytano cały TOP-16 wraz z wcześniejszym raportem `TOP_15_16_ITERACJA_18_2026-11-21.md`. Sprawdzono kolejno definicje zawieszenia i par spójnych, twierdzenie Blakersa–Masseya jako jawny zewnętrzny punkt wejścia, dowód Freudenthala, przypadki brzegowe q=1/r=0, przykład butelki Kleina, zakres stabilny, zawieszenie iloczynu, pierwszy stabilny pień Hopfa, stabilizację klas odwzorowań, widma i reprezentację kohomologii przez HA.

W istniejącym dowodzie stabilizacji dla dowolnego CW-kompleksu X rozwinięto przejście od niespójnej X do (j−1)-spójności Σ^jX: pierwsze zawieszenie jest łukowo spójne, a każde następne podwyższa spójność, co wynika z jednospójności zawieszenia przestrzeni spójnej, izomorfizmu zawieszenia w homologii i Hurewicza. Zachowano próg j>k+1.

W dowodzie obliczenia π_0(HA) dopisano konieczny warunek na **strzałki** układu granicznego: sama równość π_n(K(A,n))≅A nie wystarcza do wniosku, że colim=A. Odwzorowania sprzężone K(A,n)→ΩK(A,n+1) są słabymi równoważnościami, zatem indukują izomorfizmy π_n i pochodne strzałki systemu są izomorfizmami.

Dla stabilnych klas odwzorowań wyjaśniono strukturę grupową po zawieszeniu oraz przemienność po dalszym zawieszeniu przez argument Eckmanna–Hiltona.

**Commit:** `ff33cf79ce28650dc0e2d7b916f5f000379f736d`.

## Audyt II — definicje, indeksowanie i terminologia

Doprecyzowano dolną granicę granicy prostej π_k^s(X): j≥max(1,1−k), co gwarantuje dodatnie stopnie π_{k+j}. Dla zasady stabilizacji odwzorowań jawnie zdefiniowano N-spójne odwzorowanie przez izomorfizmy π_i w stopniach i<N i surjekcję w i=N, zamiast pozostawiać termin nieobjaśniony. Zastąpiono „mapa”, „mapą”, „mapę” właściwymi formami „odwzorowanie”. Wszystkie stare etykiety pozostały niezmienione.

**Commit:** `9b79871576c364b821436897a9f352badf82322d`.

## Audyt III — błąd LaTeX wykryty przez CI i naprawa

Pierwsza iteracja w trakcie rozbudowy tekstu przypadkowo usunęła zamykającą klamrę odsyłacza `\ref{thm:freudenthal-v8}`. Ten błąd spowodował niepowodzenie kompilacji LaTeX oraz nieprawidłową interpretację odsyłacza przez kontrolę AT–DG–AG i testy aplikacji. Własny audyt nie uznał wadliwego stanu za stabilny.

Ustalono dokładnie błąd w źródle, przywrócono zamknięcie odsyłacza oraz dodano oddzielny test, który porównuje liczbę wszystkich początków `\ref{`/`\eqref{` itd. z liczbą poprawnie domkniętych jednoliniowych odsyłaczy. W tej postaci uszkodzone wielowierszowe odsyłacze zostają odrzucone przed składaniem całej książki.

Po naprawie kompilacja, aplikacja i audyt zależności przeszły na commicie `8646da10`.

**Commity:** `8646da103ff4901160d833f3943acde71892c035`, `f50871c93cf013f017de4016d84d910ab080299c`.

## Audyt IV — K(A,0), ΩK(A,1) oraz język

Rozwinięto dowód, że poziom zerowy widma Eilenberga–Mac Lane’a jest właściwy: ΩK(A,1) ma składowe klasyfikowane przez π_1(K(A,1))≅A, a każda ze składowych ma zerowe dodatniostopniowe grupy homotopii; w konsekwencji jest słabo równoważna dyskretnej przestrzeni A. To domyka sformułowanie widma HA jako Ω-widma także na poziomie n=0.

Tytuł podsekcji zmieniono z „Łączność przestrzeni i dokładność homotopijna” na „Spójność przestrzeni i ekscyzja homotopijna”, zgodnie z terminologią rozdziału. Usunięto roboczy komentarz „Iteracja IX”.

**Commity:** `7dc20c58b53b7a32f9930be725d581a1b08a484b`, `227064b76071a0f495f105e68b7a13b6326c6d69` (test językowy oraz poziomu zerowego HA).

## Audyt V — niezależna kontrola po wszystkich poprawkach

Najnowsze źródło GitHub, blob `05251dea5f31d79147f17c54ce6c94fef31dc729`, zostało ponownie odczytane bez polegania na zamierzonych podmianach:

- **603 wiersze**, **11 zachowanych, wzajemnie różnych etykiet**, **8 kompletnych odsyłaczy** (wewnętrznych lub do wcześniejszych rozdziałów).
- **Dwa diagramy TikZ** zachowane.
- Stos środowisk `\begin`/`\end` bez naruszeń.
- Reguła domknięcia wszystkich `\ref` / `\eqref` bez naruszeń.
- Brak roboczych komentarzy oraz zabronionej terminologii („sekwencja”, „tensorowanie”, „mapa”, „dual”, „unia”).
- Testy matematyczne obejmują granicę stabilizacji sfer n≥k+2, warunek j≥d+1 dla klas odwzorowań, poprawne indeksowanie granicy prostej, spektalną rolę poziomu K(A,0) oraz historyczne obliczenie π_1(K)_ab=Z⊕Z/2 i π_1^s=Z/2.
- Użycie twierdzenia Blakersa–Masseya i stabilności operacji Steenroda nadal jest jawnie wskazane jako zewnętrzny wynik fundamentalny. Rozdział nie przypisuje im pełnych samodzielnych dowodów.

## Wyniki CI

Po naprawie odsyłacza dla commita `8646da10`:
- [TeX TOP-15/16](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44931001334): **success**.
- [Aplikacja](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44931001424): **success**.
- [AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44931001356): **success**.

Dalsze poprawki obejmują doprecyzowanie przypadku K(A,0), język i osobne regresje. **Końcowy wynik CI dla najnowszej wersji należy uzupełnić przed formalną decyzją o stabilności.**

**Status na tym etapie:** audyt V matematycznie i strukturalnie czysty, oczekiwanie na aktualne CI. Następny rozdział po domknięciu: TOP-17.
