# Logika matematyczna i teoria mnogości — rozdział 23, audyt I

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/23-dolne-twierdzenie-lowenheima-skolema-i-domkniecia-skolema.tex`.  
**Źródło:** wcześniejsza wersja rozdziału 23 w opracowaniu rozdziałów 01–44 oraz moduł twierdzeń Löwenheima–Skolema.

## Zakres niezależnej kontroli
1. **Moc rodziny formuł:** sprawdzono zależność od liczby symboli języka, przeliczalności zmiennych, skończonej długości napisów, parametrycznych krotek i arytmetyki mocy nieskończonych z aksjomatem wyboru. Otrzymano oszacowanie `max(aleph_0, |L|, |X|)`.
2. **Funkcje Skolema:** ustalony dobry porządek uniwersum umożliwia jednolity wybór najmniejszego świadka i elementu domyślnego. Wyjaśniono, że to wybory w metateorii i nie dodajemy symboli funkcyjnych do języka struktury.
3. **Domknięcie Skolema:** w `X_0` uwzględniono stałe języka oraz element domyślny, co eliminuje problem pustej podstruktury. Zamknięcie względem funkcji wyprowadzono z `y=f(x)`, uwzględniając arność zerową.
4. **Elementarność:** dla każdej formuły egzystencjalnej z parametrami z sumy konstrukcji świadek pojawia się na następnym etapie. Zastosowano istniejące kryterium Tarskiego–Vaughta `thm:model-tarski-vaught` z rozdziału 15.
5. **Dolne twierdzenie:** w indukcji `|X_n|≤κ` liczba nowych świadków jest ograniczona przez liczbę par formuła–parametry; w drugim stwierdzeniu powiększono zbiór parametrów do mocy `λ`. Każdy użyty rachunek mocy ma podane założenie wyboru.
6. **Przykłady:** przeliczalne elementarne podciało `R` różni się od `Q`; rozpisano rolę pierwiastka kwadratowego z 2, elementów przeciwnych i odwrotności. Niewymierność `sqrt(2)` udowodniono argumentem parzystości.
7. **Język i zakres:** zapis „przeliczalnie nieskończona” odróżniono od „co najwyżej przeliczalna”; wyraźnie odróżniono konstrukcję teoriomnogościową od algorytmu.

## Inwentarz
1 twierdzenie, 2 lematy, 1 wniosek, 3 definicje, 2 przykłady, 3 uwagi, 4 dowody. 12 etykiet, 9 odsyłaczy; wszystkie sprawdzane cele są dostępne w skrypcie.

## Walidacja
- Dodano moduł `tools/tests/test_logic_and_set_theory_ch23.py`: **9/9 testów PASS** w przebiegu CI `44962281632`.
- Pełne GitHub Actions tego przebiegu zatrzymało się na osobnym błędnym teście rozdziału 24, nie na rozdziale 23.
- Końcową kompilację PDF i oględziny stron należy potwierdzić w następnej iteracji.

**Werdykt:** przeprowadzono audyt matematyczny I; tekst oczekuje pełnej kontroli składu i czystej iteracji II.
