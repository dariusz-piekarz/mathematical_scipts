# Audyt XCVI (96) — rozdział 27: Miary na rozmaitościach
Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt startowy f479f41edab170155e3543e8debba94bb8643672. Porównanie z raportem XCV (7faef055243ac24db30fe2a757e1c16669a54767) wykazało trzy późniejsze commity, wyłącznie w analizie funkcjonalnej. Odczytano pełne źródło 27, raport XCV, AGENTS.md, standardy i oba pliki główne książek.

## Kontrola matematyczna
- Radon: lokalna skończoność wynika z ograniczenia gęstości na zwartej kuli; przeliczalne pokrycie daje sigma-skończoność.
- Kryterium zerowości: poprzedni dowód nie uzasadniał mierzalności obrazów dowolnych zbiorów z uzupełnienia ani obu implikacji. Uzupełniono przez borelowskiego reprezentanta B i borelowski zbiór zerowy Z zawierający różnicę symetryczną; zupełność miary Lebesgue'a daje wynik.
- Immersja: lokalna postać stałej rangi i przeliczalne podpokrycie wystarczają; nie zakłada się globalnego osadzenia.
- Radon–Nikodym i rozkład Lebesgue'a: sigma-skończoność i jednoznaczność prawie wszędzie są właściwe; lokalna całkowalność wynika ze skończoności na zwartych.
- Jakobian: dopisano uzasadnienie niezależności od baz ortonormalnych. W zamianie zmiennych jawnie zapisano iloczyn gęstości i jakobianu, aby usunąć przeskok rachunkowy. Rozłączny podział i odwrotny jakobian są poprawne.
- Produkt: blokowy wyznacznik, przeliczalna baza i Tonelli uzasadniają wynik; w kolejnym audycie warto doprecyzować lokalne utożsamienie miar oraz samodzielność hipotez.
- Przykłady gęstości i zmiany konforemnej zgodne z lokalnym wzorem. Brak rysunków. Nie rozszerzano zakresu.

## Weryfikacja
Trzy celowane zamiany; 333 wiersze (licząc końcowy pusty wiersz), 11 etykiet zachowanych w identycznej kolejności. Wszystkie cztery zewnętrzne cele etykiet potwierdzone w źródłach 17, 18, 20, 28 (wyłącznie kontekst). Konwencja chi_A zachowana; historyczna makrodefinicja w skrypcie całkowym pozostaje poza zakresem. Commit źródła 3b05e481b8e3b302d9899372f4d8478afbcb9f10 odczytany przez API; ponowny odczyt źródła identyczny z zapisem, blob ae1613e6fd0f72bd2d1b682789ff9fe14954aa6c.
Nie uruchomiono kompilacji, testów ani oględzin PDF. Nie potwierdzono pełnej kontroli technicznej.

## Status
NIESTABILNY. Po trzech korektach wymagany następny pełny niezależny audyt wyłącznie rozdziału 27, w tym samodzielność hipotez, uzasadnienie współrzędnościowego wzoru jakobianu, kompilacja, CI i PDF. Nie przechodzić do 28. Brak propozycji rozszerzenia.
