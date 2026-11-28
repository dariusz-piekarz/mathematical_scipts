# AA-60 — audyt II: hipotezy, dowody i integracja regresji

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Źródło przed korektą 48353594ba3f4f2f685d7fd36bcad18e49b4dbb9, po korekcie 6a494ed2249d6f8d3bc58ff3fadf001e3dbfbe01 (commit b53246ae7b0865764c2b0c270c2c537bf7939520).

## Kontrola matematyczna
Sprawdzono klasyfikację nieprzywiedlnych, relacje komutacyjne i Casimira. W dowodzie pełnej redukowalności sprawdzono maksymalny podmoduł, rozkład uogólnionych przestrzeni własnych Casimira, wyodrębnienie składników L(m) w jądrze, wybór przeciwobrazu najwyższej wagi, przesuwanie uogólnionych wag, EF^(m+1)v=0 oraz iniektywność F^m na przestrzeni najwyższej wagi w jądrze; obejmuje to m=0. Rozszczepienie wynika z izomorfizmu rzutu na skonstruowanym podmodule. Uzupełniono jawne hipotezy, oznaczenia i kwantyfikatory, zakres wzoru z F^(j-1), rozkład podmodułu M i parzystość najwyższych wag. Sprawdzono argument rangi E na wadze zero, wykluczenie wielokrotności ułamkowych, istnienie przeciwnych korzeni, ciągi korzeniowe i znak p-q. Dodatkowo rozpisano dodatnią określoność odwrotności macierzy B w modelu rzeczywistym. Nie znaleziono fałszywej tezy, lecz wprowadzono korekty, więc audyt nie jest czysty. Zakres bez zmian.

## Regresje i CI
Zapisano tools/tests/test_abstract_algebra_ch60.py (314a1ec8cf3c730fb36ac33accc3e0d98860cfed), obejmujący relacje operatorów L(m) dla m=0,...,12, Casimira, potęgi F i tożsamości komutacyjne, odtwarzanie krotności z wag, całkowitość liczb Cartana i odbicia w modelach typu A. Zaktualizowano 12 starszych kontroli liczby rozdziałów z 59 na 60 oraz globalną bramkę integralności (1e2888c5ce850849dfabc20d71836ba02606a7e8), bez usuwania poprzednich asercji. Workflow rozszerzono w 600d410cd9c5d06af10b47b1f203cb7fe033622e. Wyniki nowych regresji w CI jeszcze niepotwierdzone; drugi niezależny zestaw pozostaje do przygotowania. Nie oglądano PDF.

AA-60 W AUDYCIE, czyste audyty 0/2, AA-61 nieotwarty.
