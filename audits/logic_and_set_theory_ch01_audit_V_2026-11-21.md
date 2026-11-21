# Audyt V — rozdział 01 „Zdania i spójniki logiczne”

Data: 21 listopada 2026. Zakres: dodatkowa niezależna iteracja dotycząca **wyłącznie poprawności, precyzji i redakcji istniejącego materiału**, bez poszerzania pokrycia zagadnień. Porównanie z wersją audytu IV z gałęzi `biblioteka-matematyczna-iteracja-6`.

## Stwierdzone usterki i naprawy

1. **Niepoprawny przykład formalnej składni**: zapis `(p\Rightarrow((\neg q)\lor r))`, określony jako „pełny”, nie był formułą generowaną przez definicję indukcyjną, gdyż gramatyka nie zawiera osobnej reguły dopisania nawiasów do `\neg q`. Zastąpiono go poprawnym `(p\Rightarrow(\neg q\lor r))` i odpowiednio zmieniono nazwę podformuły.
2. **Warunek konieczny i wystarczający**: definicja wyjaśniała osobno konieczność i wystarczalność, ale nie objaśniała ich połączenia zapowiedzianego w tytule. Dopowiedziano, że oba kierunki implikacji muszą być prawdziwe przy każdym dopuszczalnym wartościowaniu.
3. **Błąd językowy** w dowodzie negacji implikacji: „Jest to żądaną równoważnością” zamieniono na poprawne „Otrzymaliśmy zatem żądaną równoważność”.
4. **Zbyt mocne zdanie w dowodzie rozdzielności**: zastąpiono twierdzenie o „wyliczeniu wszystkich wartościowań” poprawnym stwierdzeniem, że rozbicie na przypadki `p=0` i `p=1` wyczerpuje wartościowania, bez ograniczania wartości pozostałych zmiennych.
5. **Nieprecyzyjny przykład pustej listy przesłanek**: zamiast uzależniać prawdziwość stwierdzeń metamatematycznych od wartości `p`, jawnie rozdzielono wartość formuł `\psi` i `\top\Rightarrow\psi` przy obu wartościowaniach od globalnego wniosku `\models\psi`.

## Kontrole powtórne

- Dokładnie **10 twierdzeń** bez zmian liczby ani nowych twierdzeń i lematów.
- Dokładnie **31 etykiet**, bez zmian nazw i bez powieleń w rozdziale.
- Zgodność nawiasowania z indukcyjną gramatyką zweryfikowana parserem testowym; poprawiony przykład jest rozpoznawany jako poprawna formuła, dawny zapis nie jest.
- Enumeracyjne testy tablic prawdy, podstawowych równoważności, obliczeń przykładów, reguł wnioskowania, zasad rozdzielności i przypadku pustej listy przesłanek — **zaliczone**.
- Pełna kompilacja LaTeX: kod wyjścia **0**, **376 stron**, **44 rozdziały**; **1075 unikatowych etykiet**, **brak duplikatów i nierozwiązanych odsyłaczy**. Nieblokujące ostrzeżenia typograficzne/hyperref występują poza analizowanym rozdziałem.
- Oględziny wszystkich **9 stron** rozdziału w wyniku pełnego składu: brak zauważonych przecięć tekstu, rycin, tabel i marginesów.
- Rozdział nie zależy od zewnętrznego pliku graficznego, kodu lub bibliografii. Odsyłacz `ch:syntax-fol` do rozdziału 09 jest poprawnie rozwiązywany w pełnym skrypcie; będzie nierozwiązany w samodzielnym składzie rozdziału 01 bez rozdziału 09 lub konfiguracji `xr`.

## Decyzja

Po piątym, niezależnym audycie oraz kontroli wprowadzonej korekty **nie wykryto kolejnych usterek wymagających zmian**. Rozdział 01 można uznać za zamknięty na potrzeby bieżącego harmonogramu audytów i przejść do rozdziału 02. Nie oznacza to matematycznej gwarancji niewystępowania błędów, ale nie ma obecnie znanych problemów blokujących przejście dalej.
