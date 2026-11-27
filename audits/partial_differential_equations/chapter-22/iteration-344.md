# RRC 22 — iteracja 344

Pierwszy pełny audyt stabilizacyjny wszystkich 8 sekcji (odczyt 1533 wierszy). Commit 4f94413817028f1576458e17aa111dd813ed5c13, blob 9b61ce86ef2baf52dafec511a8545bc75ce0dc65.

- Uzasadniono zupełność H^s dla dowolnego rzeczywistego s przez izometryczny izomorfizm z L². Sprawdzono operator mnożenia, sprzężenie i generator grupy.
- Wzmocniono zasadę Duhamela do jednoznaczności w całej klasie C_t L² rozwiązań dystrybucyjnych: obcięcie częstotliwości różnicy rozwiązań, przejście z H^{-2} do H² i C¹ L², rachunek normy i granica. Ten wynik zastosowano także do potencjału zależnego od czasu. Dopisano wspólną silną ciągłość ewolucji dwuparametrowej. Sprawdzono znaki przy iloczynie skalarnym liniowym w pierwszym argumencie i lokalnym bilansie.
- Sprawdzono normalizację Gaussa, gałąź potęgi, majorantę, interpolację oraz argument identyczności dla pełnego nośnika.
- W TT* zastąpiono skrót o ciągłości w przestrzeni Schwartza argumentem z H², z dowodem zanurzenia H²→L⁴ w d=2. Uzasadniono mierzalność wyników całek pełnej i opóźnionej przez ciągłość w H² dla danych próbnych. Sprawdzono stałe w dowodzie operatora maksymalnego, rozkład dyadyczny, dualność oraz identyfikację całki Bochnera.
- W przeszkodzie spektralnej uwzględniono także wektor własny nienależący do L⁴. Rozpisano reprezentację nieujemnej domkniętej formy przez operator Riesza R, gęstość obrazu, samosprzężoność R^{-1}-I i równoważność opisu dziedziny; zastosowano do oscylatora i realizacji brzegowych. Dopisano obie implikacje spektralnej charakterystyki dziedziny H_D i ciągłość w normie grafowej.
- Ponownie sprawdzono dolny kraniec widma oscylatora i przykład na przedziale. Bez nowych błędów rachunkowych w zasadniczych argumentach; powyższe uzupełnienia wymagają kolejnej lektury stabilizacyjnej.

Kontrola zapisanego źródła: 1649 wierszy, 17 zachowanych unikatowych etykiet, 26 wystąpień odsyłaczy, siedem różnych zewnętrznych celów (8,18,20,21), wszystkie jednoznaczne. Brak błędów zagnieżdżenia środowisk i delimiterów. Poprzedni dedykowany CI 46014868939 SUCCESS; nowy 46017673118 queued. Brak potwierdzenia aktualnej kompilacji, odbioru wizualnego i globalnego CI.

Następny etap: drugi pełny audyt stabilizacyjny, zwłaszcza nowa jednoznaczność dystrybucyjna, konstrukcja R i mierzalność operatorów TT*.
