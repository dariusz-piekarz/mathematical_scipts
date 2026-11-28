# Moduł 15B — audyt 08 (poprawkowy)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: raport 07 (402de5f70d417d5b39e09a8406b943695047e91b), HEAD c9429151e9b26c6cf51f81504741c2569ad11f2a, źródło 3f2b84aac08535106e7508570aa80e3948258dfe. Ponownie odczytano źródło, raport i testy.

## Kontrola
- Samodzielność: uzupełniono hipotezy twierdzeń Pettisa, kryterium Bochnera, zbieżności zmajoryzowanej Bochnera, Fubiniego, zgodności z całką Riemanna, hierarchii, zbieżności Pettisa, wariacji i miary generowanej przez całkę. Dunford i Gelfand miały już jawne hipotezy. W 11/11 twierdzeń i stwierdzeń sprawdzono jawne określenie ciała skalarów.
- Pettis: dopisano oszacowanie funkcjonałów normujących z gęstej sfery i granicę epsilon. Przypadek zerowy oraz argument Borela–Cantellego zachowano.
- Bochner: jawnie określono warunek całkowalności Tf; dowód przez aproksymację pozostaje poprawny. DCT: jawna dziedzina funkcji granicznej i ciąg funkcji.
- Fubini: określono osobno oba rodzaje przekrojów oraz funkcje całek iterowanych; F_n określone na całym S. Konstrukcja mierzalnego przedstawiciela, klasa monotoniczna i sumowalność błędów zachowane.
- Riemann: jawny przedział a<b; kontrprzykład zachowany. Hierarchia: jawna definicja całkowalności skalarnej i równoważność Pettisa. Dunford: domknięty wykres bez zmian.
- Przykład c_0: określono sigma-algebrę. Przykład nieośrodkowej przestrzeni Hilberta: dopisano skończoność zbiorów współrzędnych ponad progiem, reprezentację Riesza i mierzalność dzięki zupełności miary. Zbieżność Pettisa: zachowano potrzebne założenie mierzalności normy różnicy.
- Gelfand: argument domkniętego wykresu i słaba-* addytywność, kontrprzykład normowy bez zmian.
- Wariacja: zdefiniowano najpierw funkcję zamiast zakładać, że jest miarą; jawnie dopuszczono puste składniki podziału. Dowód addytywności, wzór wariacji miary z gęstością Bochnera oraz kontrprzykład RNP zachowane. Nie rozszerzano tematyki.

## Regresja i zapis
Commity źródła 84092a107fbdf2e258fe818691d200c17a520616 i 6e1b840dbe06073c38b790ce0d5e7e3a1faa1d68. Ponowny odczyt: blob 6dc01e9a784f62bc794614ee88c69e33a91bef66, 678 wierszy, 23 unikalne etykiety, 11 dowodów, zagnieżdżenie środowisk poprawne. Zachowano etykiety i kolejność środowisk. Sprawdzono 22 wybrane kontrakty tekstowe ze wcześniejszych regresji: wszystkie obecne. Dodano dziewiąty test kontrolujący jawne określenie ciała skalarów w 11 twierdzeniach i stwierdzeniach (commit 99024259c25f078a87a8dd34021472649183962d, blob ecaa7af14d9c8a3c87872c3c4c17bcf8cabc3ed5); analogiczna kontrola przez odczyt źródła 11/11.
Nie uruchomiono unittest, kompilacji całego skryptu ani inspekcji PDF. Lista przebiegów PR dla raportu 07 była pusta. Nie potwierdzono CI nowych commitów.

## Decyzja
15B/08: poprawkowy, 0/2. Kolejny pełny audyt 09 aktualnej wersji, w tym samodzielność definicji, notacja i techniczne potwierdzenie regresji, kompilacji oraz PDF. Nie przechodzić do 16. Brak rozszerzeń.
