# Logika matematyczna i teoria mnogości — rozdział 30, audyt IV

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`.

## Kontrola redukowalności Wadge'a

Przegląd ostatniej części rozdziału wykazał, że przykład z `U={x: istnieje n, x(n)=0}` uznawał ten zbiór za zupełny dla otwartych bez uzasadnienia. W poprzednim twierdzeniu wykazano zupełność innego zbioru `U₀={x: istnieje n, x(n)≠0}`. Rozszerzono przykład przez jawną funkcję ciągłą `f`, której każda współrzędna jest `0` dla argumentu niezerowego i `1` dla argumentu zerowego. Otrzymano `U₀=f⁻¹[U]`; dla dowolnego otwartego `V=g⁻¹[U₀]` złożenie `f∘g` zapewnia `V=(f∘g)⁻¹[U]`. Tym samym kompletność alternatywnego zbioru jest rzeczywiście dowiedziona.

Powiązane twierdzenie `thm:wadge-open-nonselfdual` miało sformułowanie odnoszące się wyłącznie do konkretnego zbioru z poprzedniego twierdzenia, podczas gdy przykład zastosowywał je do zbioru alternatywnego. Uogólniono tezę w ramach tego samego dowodu: **każdy zbiór otwarty, który nie jest domknięty, jest niesamodualny względem redukcji Wadge'a**. Przeciwobraz dopełnienia tego zbioru jest domknięty przy każdej funkcji ciągłej; dlatego redukcja `U≤W Uᶜ` byłaby sprzeczna z niezamkniętością `U`. Osobno wykazano, że każdy zbiór zupełny dla otwartych musi sam nie być domknięty, ponieważ z zupełności redukuje się do niego wcześniej skonstruowany niedomknięty zbiór `U₀`.

Dodatkowo pierwszy wniosek o stopniach Wadge'a skorygowano z wersji „W ZFC” na dokładniejsze „Już w ZF” — dowód używa jedynie ustalonych, dwóch świadków z niepustych zbiorów i wyznacza funkcję przez dwie domknięto-otwarte części, więc pełny AC jest zbędny.

## Pozostałe kryteria audytu

- Sprawdzono semantykę determinacji gier Wadge'a i wykazano, że strategia II dająca nieskończenie wiele wyrazów wyznacza funkcję ciągłą; w drugą stronę funkcja ciągła daje strategię II przez wypisywanie wymuszonych kolejnych wyrazów.
- Wyraźnie odróżniono PD i AD, warunki projektowości zbiorów wypłat oraz redukcję do dopełnienia w półliniowym porządku Wadge'a. Bez nowych wyników o rangach lub skalach.
- Zweryfikowano przesłanki zewnętrznych głębokich twierdzeń Martin–Steel i Martin–Steel–Woodin; pozostawiono je jawnie wskazane jako przywołane wyniki, bez przypisywania ich dowodu elementarnym operacjom ZF.
- Zachowano wszystkie 61 elementów strukturalnych pełniejszego PDF oraz nowe domknięcie luki w twierdzeniu o zbiorze doskonałym.
- Inwentarz rozdziału: **12 definicji, 7 przykładów, 15 twierdzeń, 9 lematów, 4 wnioski, 15 uwag, 26 dowodów, 1 rysunek**; **57 etykiet i 49 odsyłaczy**.

## Technika i ciąg dalszy

Regresja wzbogacona o testy konstrukcyjnej redukcji zbiorów otwartych i warunków niesamodualności; wstępne testy regresyjne przechodzą, finalny przebieg CI dla dokładnie tej wersji źródłowej jest w toku. Poprzedni zielony przebieg `45010180808` potwierdził już poprawne złożenie wcześniejszego wariantu z 30 rozdziałami i brak przepełnień PDF.

**Werdykt:** audyt IV usunął brakujące uzasadnienie i nieścisły zakres twierdzenia. Następna iteracja ma być bezpoprawkowym audytem stabilizacyjnym po pełnym CI i obejrzeniu PDF.
