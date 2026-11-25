# Audyt 255 — rozdział drukowany 26, przebieg stabilizacyjny

Data 2026-11-25. Stan odczytu 80f29b9f0e5aecd8ce128e89fc483a0f71f59fab, TG19 blob e36191178c6ded835855e80efa3db5fa3144d1f6 identyczny z raportem 254. Odczyt wszystkich trzech sekcji, ośmiu dowodów i czterech przykładów. Ponownie sprawdzono rysunek 1 i wzór (2.1) publikacji Silver–Traldi–Williams (s. 664, DOI 10.18910/76679), zgodność znaków i zakres zewnętrznej prezentacji; nie jest to samodzielny dowód tej prezentacji. Brak nowych istotnych uwag matematycznych; nie zmieniono źródła.

Pobrano dokładne wersje pięciu zapisanych plików JS z przypiętego SHA i wykonano ich kod przez funkcję JS z przechwyceniem console.log. Wszystkie 5/5 PASS:
- test_gkt26_tait_states.js: 452 mapy, 3532 stany, 1786 porównań współczynników.
- test_gkt26_multigraph_minors.js: 238 multigrafów, 16432 wagowania, 58771 kontroli wyznaczników, 3302 minorów.
- test_gkt26_signed_bracket.js: 3532 konfiguracje znaków, 27944 stany, 17580 kontroli dla obu kolorowań, 4 przykłady warkoczy.
- test_gkt26_medial_alternating.js: 9603 spójne mapy, 1766 sferycznych, 13972 konfiguracje.
- test_gkt26_fox_goeritz.js: 111776 porównań wymiarów jąder, 21768 kontroli nad F2 dla diagramów węzłów.

Kontrola siedmiu źródeł: 101/101 unikatowych etykiet, 24 odsyłacze TG19 (15 różnych celów), wszystkie istnieją, 0 błędów środowisk TG19. Nie jest to pełny globalny test --strict.

Bramki techniczne: pdflatex dostępny lokalnie, ale git ls-remote zwrócił Could not resolve host: github.com; brak lokalnej kopii repozytorium. Dla 80f29b9f0e5aecd8ce128e89fc483a0f71f59fab brak statusów kombinowanych; dostępny run 45632899273 dotyczy analizy matematycznej I i nie potwierdza CI grafów. Brak aktualnego PDF do oględzin. Matematyczny przebieg bez istotnych uwag zakończony, techniczna stabilizacja nadal otwarta. Nie zwiększać licznika zamkniętych rozdziałów. Następny krok: uzyskanie i sprawdzenie aktualnego CI pełnego tomu oraz PDF, następnie audyt C i dopiero rozdział 27. Nie powtarzać enumeracji bez nowego celu.
