# RRC 21 — iteracja 333

Commit źródła 31afde1262581be2a0c57cff125f23cdcbd9feb5, blob 6eb6732d846e8c1452e15b9a4001b931fbf3bd4a. Pierwszy audyt szczegółowy sekcji 21.7–21.8.

- Określono porządek form kwadratowych, precyzyjne hipotezy mierzalności i regularności symetryzatora oraz współczynników. Wykazano podobieństwo symbolu do macierzy symetrycznej przez S^{1/2}, wraz z ograniczeniem uwarunkowania i uwagą o pochodnych zmiennej macierzy zmiany niewiadomej.
- W ważonej energii zastąpiono nieokreślony zanik w nieskończoności założeniami Sobolewa; uzasadniono absolutną ciągłość energii, różniczkowanie S przez ilorazy różnicowe i Fubiniego, znikanie dywergencji przez funkcje odcinające. Wyprowadzono jawne C=||D_S||/(2 sigma) oraz oszacowanie zwykłej normy L².
- Rozpisano kontrprzykład Jordana: wymiar jądra, brak dodatniego symetryzatora, jawne rozwiązanie, granica z lematu Riemanna–Lebesgue'a i brak ograniczonego operatora ewolucji przedłużającego rozwiązania gładkie.
- Dodano redukcję zmiennowspółczynnikowego równania falowego do układu dla (u_t, grad u), macierze główne, człon niższego rzędu, symetryzator diag(1,G), wartości własne symbolu i rekonstrukcję u przy zgodnych danych początkowych.
- Oddzielono globalną tożsamość energii w konkretnych przestrzeniach Sobolewa od lokalnej propagacji dla u klasy C² i G lipschitzowskiej. Uzasadniono całkowanie przez części, lokalny bilans prawie wszędzie, wzór transportu dla ciągłej gęstości, Gaussa dla pola lipschitzowskiego, oszacowanie strumienia przez sqrt(Lambda) e, zerowanie na całym stożku przez całkowanie w czasie oraz przypadek zerowego promienia końcowego.

Kontrola źródła: 1415 wierszy (1169 wcześniej), 23 zachowane unikatowe etykiety, 53 wystąpienia odsyłaczy, trzy różne cele zewnętrzne (rozdziały 5 i 20). Wszystkie cele jednoznaczne, brak błędów zagnieżdżenia środowisk i delimiterów. Brak potwierdzonej kompilacji rozdziału 21; run 45994503573 rozdziału 20 nadal queued. Postęp pierwszej lektury 8/10 sekcji.

Następny etap: sekcje 21.9–21.10, warunki brzegowe i podsumowanie, następnie pełne audyty stabilizacyjne i dedykowany workflow rozdziału 21.
