# Audyt CXX (120) — rozdział 29: wariacja i zupełność BV
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: HEAD 79cf6648f882f53bda9f7146b2529f8f71e7c0cd, raport CXIX (rozdział 29 otwarty, 28 zamknięty według raportu). Odczytano AGENTS.md, standardy terminologiczne, oba pliki główne oraz źródło rozdziału.
## Kontrola ograniczonego fragmentu
Wiersze 240–366 wersji wejściowej: wariacja gładka, reprezentacja miarowa, zupełność BV. Poprzednia aproksymacja wyłącznie na K nie kontrolowała wkładu poza K. Zastąpiono ją globalnym polem z nieujemną funkcją odcinającą, splotem zachowującym ograniczenie normy i przejściem do granicy na wspólnym zwartym nośniku. Doprecyzowano otwartość Omega i rzeczywiste wartości funkcji w dwóch twierdzeniach, przypadek zerowego testu oraz wykazano skończoność wariacji granicy przed zastosowaniem twierdzenia reprezentacyjnego w dowodzie zupełności.
## Weryfikacja
Commit źródła 791e421f45d86b0be02cfaea6e09d4c5249de462; ponowny odczyt blobu 21c448e1eaf774969a4dc6fb69f76d002ed73e8d; 1775 -> 1786 wierszy, 37 etykiet zachowanych w tej samej kolejności, błędy stosu środowisk: 0. Commit dotyczy tylko rozdziału 29. Nie uruchomiono kompilacji ani testów, nie oglądano PDF.
## Otwarte
Rozdział 29 pozostaje niestabilny. Reprezentacja wariacji przez gęstość wymaga rozpisania utożsamienia z wariacją z definicji podziałowej oraz aproksymacji pola polarnego; lokalne sklejanie miar wymaga uzasadnienia. Następnie kontrola pozostałych sekcji, rysunków, odsyłaczy, regresje i kompilacja, niezależny czysty audyt. Nie przechodzimy do 30. W pliku głównym integration_theory istnieje starsze oznaczenie ind; poza zakresem bieżącego audytu, bez zmian.
