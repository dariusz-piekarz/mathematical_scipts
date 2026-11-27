# RRC 23 — iteracja 347

Pierwszy audyt szczegółowy sekcji 23.1–23.3 (3/8). Commit 0a045d4ad3285eace576c4a7bcc2caecdae4bcbf, blob 4158210ed1aabcbe734639bcc8df567b5e54cd96.

- Sprecyzowano konwencję gradientów i macierzy Jacobiego, dziedzinę czasu oraz różnicę między rozwiązaniem klasycznym a regularnością przy danych początkowych.
- Uzupełniono dowód układu Hamiltona: lokalne istnienie i jednoznaczność, równanie gradientu, argument otwartości i domkniętości dla zachowania tożsamości na całym przedziale istnienia, równanie działania i zachowanie hamiltonianu.
- Dodano lokalny dowód rekonstrukcji rozwiązania z przepływu: regularność przepływu, różniczkowanie całki działania, tożsamość D_y Z=P^T D_y X, twierdzenie o funkcji odwrotnej, identyfikacja obu pierwszych pochodnych, regularność C² i warunek początkowy.
- Wyraźnie oddzielono utratę odwracalności różniczkowej od utraty różnowartościowości. Dla g=cos x sprawdzono globalną odwracalność przy t<1, wyprowadzono wzór na u_xx i jego rozbieżność w t=1, wykazano ścisłą monotoniczność przy t=1 i rzeczywiste przecięcie charakterystyk o różnych pędach dla t>1. Nie utożsamiono tego z automatycznym dowodem nieistnienia wszystkich rozwiązań klasy C¹.
- Uściślono definicję rozwiązania lepkościowego, lokalne funkcje testowe i ich przedłużanie, warunek początkowy oraz współrzędne płaskiego torusa. Sprawdzono zgodność z rozwiązaniem klasycznym.

Kontrola zapisanego źródła: 728 wierszy (567 wcześniej), 25 zachowanych unikatowych etykiet, 23 odsyłacze (wszystkie jednoznaczne, cele zewnętrzne w rozdz. 2 i 24), brak błędów zagnieżdżenia środowisk i delimiterów. Sekcje 23.4–23.8 pozostawiono identyczne. Kompilacja rozdziału 23 niepotwierdzona; kontrola wizualna i dedykowane CI pozostają do wykonania.

Następny etap: sekcja 23.4, zasada porównania na torusie — doprecyzowanie jednostajnego warunku przestrzennego, podwajania zmiennych i wykluczenia punktów brzegowych czasu. Następnie transformata Legendre'a i wzór Hopfa–Laxa.
