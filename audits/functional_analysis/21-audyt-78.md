# Rozdział 21 — audyt 78 (2/5 podsekcji, etap poprawkowy)

24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6.

## Zmiany
Pierwsze dwie podsekcje: uzupełniono dowód niezależności od odcięcia i zgodności przedłużenia z pierwotną dystrybucją, jawne oszacowanie Leibniza, przypadek pustego nośnika, identyfikację z ciągłymi funkcjonałami na C-infinity wraz z jednoznacznością. W lemacie o iterowanych działaniach podano uzasadnienie różniczkowania w seminormach, wspólne oszacowanie C_T C_S p_(m_T+m_S) oraz niezależny od teorii Fouriera dowód gęstości skończonych sum iloczynów funkcji testowych przez iloczynowe jądro wygładzające i sumy Riemanna. Uściślono oszacowanie operatora A_T, zwartość L-K, przenoszenie ograniczonych zbiorów, domkniętość K+F i argument rozłączności nośników. Nie rozszerzono zakresu dalszych podsekcji. Commity ce77b05be0b5f19b41ba0a5069d829670494aebc i d75dba3163237debf8dddbb37414571d40654500, blob 3fd3fbd252b6d593060d349acbae2057edaffc1d.

## Regresje i CI
Dodano trwały plik tools/tests/test_functional_analysis_ch21.py (62407914b177c54979089eba1b55c10507fcc5f9), cztery metody, w tym FA21_compact_extension_01, FA21_iterated_actions_01 i FA21_support_and_transpose_01. Nowy workflow .github/workflows/functional-analysis-ch21.yml (6d5ce371b4cb8ba645d882530a20e43e6d6885f2) kompiluje kontekst 01–21 wraz z 15A/15B oraz sprawdza testy i diagnostykę PDF. W biegu 45423418587 status in_progress przy kontroli; nie potwierdzono jeszcze wykonania całego pliku Python ani kompilacji i oględzin PDF. Niezależnie wykonano kontrolę strukturalną źródła: 19/19 unikatowych etykiet, 16/16 rozwiązanych odsyłaczy w kontekście 17–21, 18/18 warunków tekstowych i poprawnie zagnieżdżone środowiska. Wykonano w JavaScript 32768/32768 dokładnych sprawdzeń równoważności L intersect (K+F) != empty iff (L-K) intersect F != empty, dla wszystkich trójek podzbiorów {-2,-1,0,1,2}. Jest to skończony model regresyjny, nie dowód ogólny ani formalizacja Lean. Nie uruchamiano Lean.

## Decyzja
Audyt poprawkowy 2/5 podsekcji; stabilizacja 0/3. Następny audyt 79: przemienność, łączność, różniczkowanie; skontrolować szczególnie zakres uzasadnienia permutacji trzech czynników i odcięcia w zmiennej niekompaktowej. Następnie wygładzanie i zbieżność silna oraz pełna stabilizacja. Nie zamykać rozdziału na podstawie samego CI.
