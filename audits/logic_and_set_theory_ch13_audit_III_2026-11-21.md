# Logika matematyczna i teoria mnogości — rozdział 13, audyt III

Data: 21 listopada 2026 r.  
Źródło audytu: `logika_rozdzial_13_audyt_II.tex` i późniejsze wydanie biblioteczne `logic_and_set_theory_iteration_79.pdf` (strony 118–126).  
Tryb: przegląd istniejących wyników, bez dodawania nowych twierdzeń, lematów lub definicji.

## Odkryte rozbieżności i poprawki

1. **Utrata istniejących fragmentów w starszym źródle `.tex`:** w wydaniu PDF iteracja 79 występują trzy przykłady pominięte w pierwotnym pliku Biblioteki: dwa etapy nadawania świadków, konieczność ilorazowania termów oraz test uniwersalnego kwantyfikatora w lemacie o prawdzie. Wszystkie trzy odtworzono na podstawie tego wydania w zmienionej wersji `logika_rozdzial_13_audyt_III.tex`. Nie są to nowe wyniki; jest to odzyskanie wcześniej istniejącej treści.
2. **Odzyskanie diagramu łańcucha Henkina:** odtworzono z istniejącego wydania PDF schemat `(L_0,T_0) → (L_1,T_1) → (L_2,T_2) → …` wraz z definicjami sum etapów. W pierwszym renderze podpisy strzałek stykały się z ramkami; zwiększono odstęp między węzłami i ponownie wyrenderowano stronę. Ostatecznie brak nachodzących napisów.

## Niezależny przegląd matematyczny

- Lemat o negacji kwantyfikatora: poprawna lokalność świadka `∃E`, odblokowanie `RAA` i dozwolone przemianowanie zmiennej związanej.
- Świeża stała i zachowanie niesprzeczności: zamiana stałej na świeżą zmienną jest wykonana przed końcowym wyprowadzeniem sprzeczności w języku wyjściowym; nie ma niejawnej zmiany języka dowodzenia.
- Jednoczesne dodawanie świadków: dowód przez skończony fragment, nowe symbole parzyście różne, nie pojawiają się wcześniej w aksjomatach.
- Iteracja Henkina: każdy skończony napis pojawia się na pewnym etapie; niesprzeczność sumy przez skończoność dowodu.
- Maksymalna teoria: sprawdzony wariant przeliczalny i Zorn; pusty łańcuch traktowany oddzielnie.
- Model termowy: zwrotność, symetria, przechodniość oraz zgodność równości z funkcjami i relacjami; stała gwarantuje niepustość uniwersum.
- Lemat o prawdzie: atomy, negacja, koniunkcja, alternatywa, implikacja, równoważność, oba kwantyfikatory oraz możliwość nazwania każdej klasy termu.
- Pełność dla zdań i formuł z wolnymi zmiennymi: sprawdzona zmiana parametrów na zmienne, przemianowanie zmiennych własnych `∀I`, `∃E`, eliminacja nieuprawnionego przechwytywania.

## Walidacja

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error` dla lokalnej książki 01–13: **PASS**, 118 stron.
- PDF samego rozdziału: **10 stron**; rysunek sprawdzony wizualnie po korekcie.
- Brak `Overfull \\hbox` w logu; ostrzeżenia lokalnej książki dotyczą wyłącznie dwóch historycznych celów w rozdziałach 01–12 (`ch:zf-axioms`, `thm:ls-second-order-categorical`) i nie pochodzą z rozdziału 13. Bieżąca gałąź GitHuba ma wyłącznie pierwszy z tych odsyłaczy.
- Inwentarz po scaleniu z istniejącym PDF: 5 twierdzeń, 11 lematów, 6 definicji, 6 przykładów, 4 uwagi, 16 dowodów, 1 istniejący diagram.
- Rozdział 13: 32 unikatowe etykiety (31 historycznych + etykieta przywróconego rysunku), 27 wystąpień odsyłaczy, brak nieznanych celów rozdziału.
- Własne regresje `test_logic_and_set_theory_ch13.py`: **4/4 PASS**, w tym skończone modele. Testy falsyfikacyjne nie zastępują dowodów ogólnych.

**Wniosek:** audyt III wykrył i naprawił ubytek zawartości oraz kolizję podpisów w przywróconym diagramie. Przed publikacją konieczny jeszcze jeden niezależny przegląd scalonego pliku (audyt IV).