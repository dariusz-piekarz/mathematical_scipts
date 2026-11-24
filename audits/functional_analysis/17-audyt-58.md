# Rozdział 17 — audyt 58 (4/4, czysty, 2/2)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6. Źródło niezmienione od audytu 56: blob f4dd20e99ca5b89973577e545facd2f20e489c15.

## Kontrola merytoryczna
Ponowny przegląd wszystkich czterech podsekcji. Sprawdzono w szczególności: współkońcowość wyczerpania i puste zbiory, zupełność przez granice pochodnych oraz metrykę niezmienniczą względem przesunięć; konstrukcję funkcji odcięcia, odległości od dopełnień, skalowanie funkcjonału także dla zerowej seminormy; równoważność seminorm Schwartza w tym N=0, zupełność, mnożenie przez jednomiany, całkowalność wag, gęstość, brak normowalności nad R i C; znaki transformaty Fouriera, majoranty, odwracanie, normalizację jądra Gaussa i splot. Nie wykryto istotnych usterek wymagających zmian. Nie rozszerzano zakresu.

## Weryfikacja
738 wierszy, 22/22 unikatowe etykiety, 13/13 odsyłaczy, poprawnie zagnieżdżone środowiska. CI audytu 57, bieg 45383557335, zakończony sukcesem: wszystkie siedem metod testowych ze skryptu regresji, kompilacja kontekstu 01–17, automatyczna kontrola PDF i odsyłaczy oraz upload. Dodatkowa kontrola numeryczna wzoru Fouriera dla Gaussa: 20 par (a,xi), a=0.5,1,2,4, xi=-3,-1,0,1,3; całkowanie sumą prostokątów na [-12,12] z krokiem 0.005; największy błąd bezwzględny ok. 2.22e-15. To kontrola przykładu, nie dowód twierdzenia. Kontrola wizualna wszystkich ośmiu stron rozdziału została wykonana w audycie 57 dla tego samego blobu; nie powtarzano oględzin w tej iteracji.

## Decyzja
Dwa kolejne czyste audyty 57–58, 2/2. Rozdział 17 stabilny i zamknięty. Następny audyt 59: pierwsze dwa bloki rozdziału 18 (Funkcje testowe i ścisłe granice induktywne).
