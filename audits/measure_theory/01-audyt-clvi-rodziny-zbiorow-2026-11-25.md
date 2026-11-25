# Audyt CLVI (156) — rozdział 01: Rodziny zbiorów i przestrzenie mierzalne

25 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6. Punkt wyjścia: 4e09839e81f02d003c7ae7818980963dec74c6d9; historyczne zamknięcie CLV nie zastępuje bieżącej kontroli.

## Ustalenia i poprawki
- Definicja przestrzeni mierzalnej: zbiory mierzalne są elementami sigma-algebry, nie pary.
- Lemat o układzie Dynkina: usunięto przedwczesne określenie mierzalności; wykazano przynależność rozłącznych różnic, rozłączność i równość sum przez najmniejszy indeks.
- Twierdzenie pi–lambda: rozpisano wszystkie trzy aksjomaty dla K_B.
- Funkcja charakterystyczna: rozpisano cztery przeciwobrazy i ich przynależność do sigma-algebry.
- Terminologia: ko-skończony zamiast kofinitywny.
- Bez nowych tematów i bez zmian innych rozdziałów.

## Weryfikacja i trwałe kryteria regresji
Źródło po poprawce: 3a3d0aa1eda9d500d2c9c184144ef421799c0b30; commit 4915217d0a008e47ad2bd5c362ecfef6739a7613. Ponowny odczyt przez API: 19 etykiet, zachowano ich listę i kolejność; 43 otwarć i 43 zamknięć środowisk (kontrola liczności, nie kompilacja). Brak dawnego terminu i przedwczesnej mierzalności. Brak środowisk figure/tikzpicture.
- MT01-R156-01 (semantyczny): w lem:dynkin-intersection sprawdzić n=1, przynależność różnic, rozłączność i pokrycie przez najmniejszy indeks.
- MT01-R156-02 (semantyczny): w thm:pi-lambda sprawdzić X, różnicę zagnieżdżoną i sumę rozłączną dla K_B, bez zakładania zamknięcia L na przekroje.
- MT01-R156-03 (semantyczny): w przykładzie funkcji charakterystycznej sprawdzić wszystkie cztery przeciwobrazy i konieczność.
- MT01-R156-04 (statyczny): zachować 19 etykiet, nie używać kofinitywny ani alternatywnego oznaczenia funkcji charakterystycznej.

## Otwarte
Pełny niezależny audyt po poprawce, rozwiązanie odsyłaczy w kontekście tomu, kompilacja, testy repozytorium i synchronizacja listings nie zostały wykonane. W sąsiednim books/pl/integration_theory.tex makro ind nadal używa pogrubionej jedynki; nie zmieniano go poza zakresem. Status: OTWARTY, bez przejścia do rozdziału 02. Kryteria semantyczne powyżej nie są automatycznymi testami ani formalizacją Lean.
