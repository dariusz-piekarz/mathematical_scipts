# GT — pierwszy globalny audyt struktury i zależności

Inwentaryzacja wszystkich 42 źródeł na commicie f6cd4bc82a8746a54be52e13034cd0f39eddf042. Raporty częściowe 307-global-structure-part-1/2/3.json zawierają dokładne etykiety, odsyłacze, statystyki i SHA każdego źródła. Przed agregacją potwierdzono brak zmian wszystkich 42 blobów na 5ed3a2b3367a9b267be1b6bb321edd0e97ac2499. Katalog, kolejność input i rzeczywiste pliki zgodne.

Wyniki: 41 rozdziałów numerowanych i wstęp, 38115 wierszy (suma split na znakach nowej linii), 462 środowiska twierdzeń/lematów/stwierdzeń/wniosków, 440 dowodów, 112 środowisk figure lub tikzpicture (niekoniecznie 112 odrębnych rysunków), 730 etykiet, 550 odsyłaczy, 0 duplikatów etykiet, 0 nierozwiązanych odsyłaczy, 0 błędów zagnieżdżenia, 0 trafień pięciu wzorców zakazanej terminologii. Jedno odwołanie słowne do pierwszego rozdziału jest nagłówkiem uwagi w tym rozdziale, dozwolonym w istniejącym teście.

30 odsyłaczy wyprzedzających: sprawdzono kontekst w źródłach 05, 19, 20, 23, 24, 28, 29, 43. Są to zapowiedzi, odsyłacze do późniejszych uzasadnień lub konwencji; nie stwierdzono podstaw do usuwania ich wyłącznie ze względu na kolejność. Nie dowodzi to braku wszystkich cyklicznych zależności matematycznych.

Korekta literówki kokernu → kokernelu w źródle 19 oraz nieaktualnego opisu liczby źródeł w docstringu testu globalnego. Nie zmieniano etykiet ani dowodów. CI 45976430559 nadal queued przy ostatnim odczycie. W tej iteracji wykonano niezależny skan JS, nie uruchomiono pełnego skryptu Python ani kompilacji PDF (brak bezpośredniej sieci GitHub w kontenerze). Nie zakończono kontroli powtórzonych fragmentów, pełnej terminologii i spójności matematycznej między rozdziałami. Kolejny etap: te kontrole i odbiór CI/PDF.
