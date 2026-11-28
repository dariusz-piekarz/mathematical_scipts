# Audyt 256 — rozdział drukowany 26, bramki techniczne

Data 2026-11-25. Run 45633075462 (SHA 5d4dd3a71c070c125ed28d06fa5499f42056afb9): finite-models 16/16 kroków testowych PASS, cały workflow algorytmiczny ostatecznie success. Run pełnego tomu 45632682647 (SHA 8d9281de3238bd37de3694be6b20412facb0873a): full-book-pdf success, structural-audit failure na --strict wyłącznie przez manual_chapter_numbers 1 (bibliograficzne „rozdział 9” w TG19). Log: 44/44 źródła, 715 etykiet, 368 odsyłaczy, 0 duplikatów etykiet, 0 brakujących odsyłaczy, 0 błędów środowisk, 0 zabronionych zwrotów, 0 kandydatów powtórzeń. 13 odsyłaczy wprzód, nie stanowią błędu strict.

Naprawiono zapis bibliografii Lickorisha (tytuł rozdziału i strony 93–102 zamiast ręcznego numeru); commit e90a5b879f4c602e82b15d7a5498fc5cb01fb173. Nie zmieniono testu ani matematyki. Nowe runy 45633311054 (pełny tom) i 45633311008 (algorytmy) w toku, bez deklaracji success.

Pobrano faktyczny artefakt 15030847662 z runu 45632682647 (ZIP 3033696 B). Log trzech kompilacji pdflatex i plik warnings potwierdzają 363 strony A4, 0 ostrzeżeń. Z rzeczywistego PDF wyrenderowano wszystkie 7 stron rozdziału 26: fizyczne 235–241, drukowane 225–231. Obejrzano układ stron, rysunek grafów Taita, wzory i macierze; nie zauważono kolizji ani obcięć. Oględziny dotyczą wersji sprzed ostatniej czysto bibliograficznej poprawki. Po nowym pełnym CI należy sprawdzić aktualny artefakt PDF, szczególnie stronę z bibliografią, i wykonać audyt C bez istotnych zmian. Nie zamykać 26 przed tymi bramkami.

Nie wykonywano ponownie enumeracji z audytu 255. Nie zmieniano main.
