# Audyt globalny 167 — regresje i terminologia

Kontynuacja audytu 166. Wyłącznie gałąź biblioteka-matematyczna-iteracja-6.

## Wykonane kontrole
- CI pełnej książki 45587929282, job 139114214833: krok "Execute all chapter and book regression files" success. Skrypt uruchamia każdy z 36 plików w osobnym procesie i zwraca niezerowy status przy jakimkolwiek niepowodzeniu. Zatem 36/36 plików zaliczyło ten etap, w tym test integralności (unikatowe etykiety, rozwiązane odsyłacze, stos środowisk, inwentarz i katalog). Dokładnej liczby metod testowych i liczby etykiet/odsyłaczy nie odczytano jeszcze z logu. Kompilacja mastera i kontrola TOC/PDF w toku przy odczycie.
- Pobranie wszystkich 35 jednostek w czterech partiach 9+9+9+8 z ustalonego commitu 33cc75c21da21fdc4419f67ea144590699482dd4. Kontrola leksykalna wybranych niedozwolonych form (zbieżność zdominowana, tensorowanie, unia, rzeczownik dual i jego wybrane formy, d^3x, przymiotnikowe nazwy przestrzeni Hilberta/Banacha). Komentarze i listingi pominięte, a trafienia w identyfikatorach etykiet/odsyłaczy odrzucone, aby zachować identyfikatory. Jedno rzeczywiste trafienie: rozdział 23, zbieżność zdominowaną.
- Poprawka fb0995c310bfcfd3b81bbc5606c820027987a535, blob 5c4ab0ca2d036a5c324e2e191e3de724b49b323a. Ponowny odczyt potwierdził, że źródło różni się od poprzedniej wersji dokładnie zamianą "zbieżność zdominowaną" na "zbieżność zmajoryzowaną"; nie zmieniono twierdzeń ani etykiet.
- Dodano piątą metodę globalnej regresji FA_BOOK_terminology_02 w tools/tests/test_functional_analysis_book_integrity.py (05b52d96968ea7af5bf5ec69e1f8f139e597377f). Kontrola wybranych form nie stanowi pełnego audytu stylistycznego ani ponownego sprawdzenia wszystkich dowodów.
- CI 45588155490 (poprawka źródła) i 45588182885 (nowa regresja) w toku. Nie przypisano nowej metodzie wyniku PASS. Nie wykonywano formalizacji Lean.

## Decyzja
Audyt globalny pozostaje otwarty. Pierwszy zestaw globalnych regresji zaliczony na poprzednim źródle, jedna poprawka językowa wymaga nowej kontroli. Następny audyt 168: odczytać końcowe logi wszystkich trzech przebiegów, zweryfikować liczby metod/etykiet/odsyłaczy, naprawić ewentualne problemy mastera, pobrać aktualny PDF i przeprowadzić kontrolę wizualną wszystkich stron oraz kontrolę spójności między rozdziałami. Nie uznano książki za zamkniętą.
