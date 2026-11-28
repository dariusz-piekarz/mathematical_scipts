# Miara i całka — audyt XLII: rozdział 12, audyt I (2026-11-23)

**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Rozdział:** chapters/pl/measure_theory/12-miary-produktowe-twierdzenia-tonellego-i-fubiniego.tex.  
**Status: W STABILIZACJI — NIEZATWIERDZONY.** Nie przechodzić do R13 przed niezależnym, pełnym, czystym audytem po ostatniej poprawce.

## Stan wznowienia

Odczytano aktualny rozdział R12 (blob 59a5357c80b68b6cd6a147548f4ce56073e03f96), ostatni zatwierdzony raport R11 XLI (blob 0ea798ff5ae15402c52bdb4e3089358b4e25ab8c), książkę books/pl/measure_theory.tex, sąsiedni books/pl/integration_theory.tex, AGENTS.md i docs/pl/standardy_terminologiczne.md. Raport R12 XLII nie istniał w chwili wznowienia. R11 ma w zapisanym raporcie status STABILNY; R12 jest następnym rozdziałem. Nie zmieniano innych rozdziałów.

## Audyt matematyczny

Rozdział ma 12 środowisk dowodowych, 23 etykiety, 841 wierszy w wersji wejściowej. Przeanalizowano argumenty: mierzalność przekrojów; klasę monotoniczną na prostokątach skończonej miary; wyczerpanie sigma-skończone; istnienie i jednoznaczność miary produktowej; przejście od funkcji charakterystycznych do prostych i nieujemnych; całkowalność przekrojów Fubiniego; przypadek niebezwzględnej zbieżności; przykład przekątnej przy braku sigma-skończoności; porównanie z miarą Lebesgue'a; uzupełnienie produktu; przekroje zbiorów zerowych; łączność produktów.

Kontrola przypadków brzegowych: konwencja 0·∞=0 w miarach prostokątów, zerowe miary czynników, nieskończone całki nieujemne, nieistnienie całki funkcji o nieskończonych częściach dodatniej i ujemnej, przekroje wyjątkowe dla uzupełnienia produktu. W przedstawionych krokach nie wykryto jawnego błędu rachunkowego, lecz pełna niezależna stabilizacja matematyczna po poprawce pozostaje otwarta.

**Wykryta usterka M12-01 (potwierdzona):** wniosek cor:practical-fubini-12 formułował kryterium Fubiniego bez własnego określenia przestrzeni, sigma-algebr, miar i hipotezy sigma-skończoności; odniesienie do poprzedniego twierdzenia w dowodzie nie zastępowało jawnych założeń w tezie. Ponadto nie precyzował, że przekrojowe całki dla funkcji zespolonej istnieją prawie wszędzie, a na zbiorach wyjątkowych należy zadać wartość zero.

**Poprawka:** zachowano etykietę cor:practical-fubini-12; dopisano obie przestrzenie z miarami sigma-skończonymi, mierzalność f względem F⊗G, jawne określenie całkowalności względem μ⊗ν i konwencję zerowania na wyjątkowych mierzalnych zbiorach. Dowód nie wymagał zmian, gdyż powołuje się na Tonellego i Fubiniego z odpowiednimi hipotezami.

**GitHub commit źródła:** [4020efbcacc6b0cb4b491e44f46d0f8bac833ad7](https://github.com/dariusz-piekarz/mathematical_scipts/commit/4020efbcacc6b0cb4b491e44f46d0f8bac833ad7). Potwierdzono odczytem po zapisie: nowy blob **5534eed7aed056956f8d7d21a373393c26a3ba40** oraz dokładną zgodność treści z wysłaną wersją. Rozdział zachował 12 dowodów i 23 etykiety.

## Kontrola językowa i techniczna

Weryfikowano zgodność z AGENTS.md i docs/pl/standardy_terminologiczne.md, w szczególności zapis \chi_A oraz termin „twierdzenie o zbieżności zmajoryzowanej”. W źródle nie występują \mathbf{1}, \mathbb{1}, „indykator” ani „zbieżność dominowana”. Zachowano wszystkie istniejące etykiety, wzory i zaakceptowane przykłady. books/pl/integration_theory.tex został odczytany wyłącznie jako kontekst; nie wykonano scalania ani usuwania treści.

**Nie uruchomiono w tej iteracji pdflatex ani GitHub Actions; nie ma podstaw do deklarowania ich sukcesu.** Nie wykonano też nowego oglądu PDF. Są to otwarte zadania obowiązkowe przed stabilizacją.

## Następny krok

**Audyt XLIII / R12 II**, niezależny od bieżącego: ponownie przeczytać wszystkie 12 dowodów, hipotezy i kwantyfikatory, przykłady, etykiety i odsyłacze; uruchomić kompilację izolowanego rozdziału i pełnej książki, testy/CI, sprawdzić wizualnie wszystkie strony PDF. Jeśli pojawi się nowa poprawka, wymagany będzie jeszcze jeden czysty audyt tego samego rozdziału. R13 pozostaje nietknięty.