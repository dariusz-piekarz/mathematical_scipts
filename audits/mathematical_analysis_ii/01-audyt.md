# AM II 01 — audyt otwarty
Audytowana wersja: 5423d766b72c8e2e18e2e74e9c97206a0c4b0a42.

## Źródła i wykonane poprawki
- AF 12: definicja normy, norma operatorowa, przestrzenie ciągowe; zachowano pięć oryginalnych etykiet.
- AM I 07: adaptacja zupełności metrycznej i przestrzeni funkcji ograniczonych.
- AL 12: norma euklidesowa i nierówność Cauchy'ego–Schwarza.
- Rozpisano dowód Minkowskiego, przypadek normy zerowej oraz zupełność przestrzeni ciągowych przez granice sum skończonych, bez wykorzystywania późniejszej teorii szeregów wektorowych.
- Rozpisano ograniczoność operatora, ciągłość granicy operatorów, zupełność przestrzeni funkcji ograniczonych i ciągłych.
- Dodano równoważność norm, zupełność w skończonym wymiarze, podprzestrzenie domknięte, kontrprzykład c00 i rysunek kul jednostkowych.
- Rejestracja w catalog/books.json i osobny entrypoint; plan 34 rozdziałów uwzględnia całki powierzchniowe i po podrozmaitościach.

## Walidacja
Kontrola statyczna: 343 wiersze, 12 etykiet, 3 lokalne odwołania, brak lokalnych duplikatów i brak odwołań bez celu; środowiska begin/end zbilansowane.
CI dla audytowanej wersji: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45661793240 — w kolejce w chwili sprawdzenia.

## Status
OTWARTY. Nie potwierdzono pełnej kompilacji, kontroli wizualnej PDF ani niezależnego audytu kontrolnego całego rozdziału. Nie przechodzić do rozdziału 02 przed ich domknięciem i usunięciem ewentualnych usterek. Rejestracja w katalogu nie dowodzi działania indeksu Atlasu.

## Kolejny audyt szczegółowy — wersja 2b9f9be9873a691f608c12585e3f7563120aa73d
Poprzedni przebieg #45661793240 zakończony SUCCESS dla 5423d766; artefakt mathematical-analysis-ii ID 15044299814 istnieje. Wynik nie przenosi się automatycznie na nową wersję.

Usunięte braki: przeciwdziedzina i kwantyfikacja normy; weryfikacja aksjomatów metryki; dwustronna kontrola warunku Cauchy'ego dla norm równoważnych; uzasadnienie zwartości sfery i dodatniości minimum w dowodzie skończenie wymiarowym; pełny dowód Younga i Höldera (w tym normy zerowe i p=1); domknięcie przestrzeni ciągowych na działania; uzasadnienie liniowości c0 i c00; jednoznaczność granicy w przykładzie niezupełności; odsyłacz do ciągłości normy. Nie dodawano niezwiązanej tematyki.

Kontrola statyczna: 402 wiersze, 12 etykiet, 4 odwołania lokalne, 0 duplikatów i 0 brakujących celów; środowiska zbilansowane. Status nadal OTWARTY: ponowne CI dla aktualnej wersji, kontrola wizualna PDF oraz końcowy audyt kontrolny.

## Następny audyt szczegółowy — wersja 96f6139479f3c83369b06cd3cf43e6293684d689

Ponowny przegląd całego rozdziału wykazał 14 miejsc wymagających doprecyzowania. Uzupełniono metrykę na produktach, inkluzje kul, granicę w skończonym wymiarze, hipotezy twierdzenia o operatorach (oddzielono normowalność od zupełności), aksjomaty normy operatorowej, liniowość granicy i dowód zupełności przestrzeni sprzężonej, aksjomaty norm współrzędnych i normy euklidesowej, zastosowanie Höldera w dowodzie Minkowskiego, kwantyfikację w dowodzie domkniętości c0, kontrprzykład c00, aksjomaty normy B(S,E) i liniowość C(K,E). Zachowano wszystkie etykiety. Nie rozszerzano zakresu tematycznego.

Kontrola statyczna: 470 wierszy, 12 etykiet, 6 wystąpień odwołań lokalnych, 0 duplikatów, 0 brakujących celów, zbilansowane środowiska. CI #45663392153 dla poprzedniej wersji 2b9f9be nadal w toku w chwili kontroli; wynik CI dla nowej wersji niepotwierdzony. Status OTWARTY. Licznik czystych audytów: 0. Konieczne ponowne czytanie po poprawkach, kompilacja i kontrola wizualna aktualnego PDF. Nie rozpoczynać rozdziału 02.
