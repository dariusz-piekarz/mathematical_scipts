# Moduł 15B — audyt 10 (poprawkowy)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: raport 09 (5cf95f3dc9de32fe8786abd2b42b68060bd53900), HEAD 5084af1fdb1b8eaba0e3d65ba332119ebe0a517e, źródło 451e23a40f3c6e3f6596d173547866f3bf31f025. Odczytano całe źródło, poprzedni raport i testy.

## Kontrola
- Konstrukcja Bochnera: sprawdzono argument Cauchy'ego, niezależność od aproksymacji, przycięcie i oszacowanie. Dopisano uzasadnienie liniowości całki funkcji prostych oraz silnej mierzalności Tf.
- Pettis o mierzalności, DCT Bochnera, Fubini, zgodność z całką Riemanna: argumenty poprzednich audytów zachowane.
- Dunford: domknięty wykres. W istniejącym przykładzie c0 uzasadniono zdanie o niewystarczalności reprezentacji całki po całym S przez symetryczne powielenie atomów. Całka Dunforda po całym zbiorze jest zerem, po dodatniej połowie jest stałym ciągiem 1/2, nienależącym do kanonicznego obrazu c0. To uzupełnienie uzasadnienia istniejącego twierdzenia, nie nowy zakres.
- Pettis: sprawdzono przykład nieośrodkowej przestrzeni Hilberta, refleksywność, liniowość i zbieżność zmajoryzowaną. Gelfand: poprawiono gramatykę definicji; dowód i przykład zachowane.
- Wariacja: sprawdzono przeliczalną addytywność, oszacowanie różnic wariacji i przejście do granicy.
- RNP: rozróżniono m i jego rozszerzenie, dopisano niezależność od przedstawicieli, rozłącznienie przeliczalnej rodziny, addytywność w normie, zachowanie całkowitej wariacji i bezwzględnej ciągłości. Doprecyzowano definicję całkowalności przy niezupełnej mierze, konstrukcję przedstawiciela silnie mierzalnego i aproksymację w L1 względem pierwotnej miary. Wskazano obie implikacje równoważności definicji RNP.
- Kontrprzykład C([0,1]) i uwagi o przestrzeniach lokalnie wypukłych zachowano. Brak zmian poza modułem i testami.

## Regresje i technika
Commit źródła 6663aa74b37bdadb0ea495686d06cc3e99bfc036, blob 3e92f702d7e024b2f7da636afa46d20a23dba764, 793 wiersze, 23 etykiety zachowane w kolejności, 11 dowodów, poprawne zagnieżdżenie środowisk. Osiem celowanych zamian.
Commit testów 3583ba2a0216016dddbb8a933dd83faa427283d8, blob 8e8cd36ed36a1327411f9a51f07a01b788b9c4a9: dostosowano jeden poprzedni kontrakt i dodano jedenasty test. Ponownie odczytano oba pliki. Wykonano odtworzenie 11 kontroli w JavaScript (kontrakty tekstowe, budżet błędów, dokładna arytmetyka skończonej całki produktowej i wariacja na wszystkich 16 podzbiorach atomów), 11/11 przeszło. Nie jest to wykonanie oryginalnego unittest ani formalna weryfikacja dowodów. Lokalny git ls-remote nie powiódł się z powodu braku rozwiązywania DNS github.com, więc nie pobrano projektu i nie wykonano kompilacji ani oględzin PDF. CI niepotwierdzone.

## Decyzja
15B/10: poprawkowy, 0/2. Następny niezależny audyt 11, w szczególności kontrola nowych fragmentów, rzeczywiste uruchomienie unittest, kompilacji, odsyłaczy i oględzin PDF, jeśli dostępne. Nie przechodzić do rozdziału 16.
