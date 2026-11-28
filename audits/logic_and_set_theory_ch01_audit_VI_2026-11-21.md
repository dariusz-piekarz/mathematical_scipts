# Audyt VI — rozdział 01 „Zdania i spójniki logiczne”

**Data:** 21 listopada 2026 r.  
**Zakres:** szósty niezależny audyt poprawności matematycznej, ścisłości języka i zgodności z formalną składnią, wyłącznie dla istniejącego materiału rozdziału 01. Nie dodawano twierdzeń, lematów ani nowych sekcji.

## Poprawione nieścisłości

1. **Interpretacja i prawdziwość:** sformułowanie „rzeczywisty stan rzeczy” zastąpiono określeniem wartości logicznej w ustalonej interpretacji, odpowiednim także dla abstrakcyjnych struktur matematycznych.
2. **Paradoks kłamcy:** odróżniono samoodnoszącą się wypowiedź od formalnego zdania z określoną wartością logiczną.
3. **Miejsce definicji składni:** usunięto zdanie zapowiadające, że „formalna składnia” pojawi się dopiero w rozdziale 09, mimo iż rozdział 01 już definiuje gramatykę rachunku zdań. Rozróżniono składnię rachunku zdań i późniejszą składnię logiki pierwszego rzędu.
4. **Zdanie proste i złożone:** skorygowano twierdzenie, że każda formuła po podstawieniu zdań staje się zdaniem złożonym. Formuła będąca jedną literą daje zdanie proste.
5. **Nawiasy przy negacji, przykład:** zastąpiono niezgodny z dosłowną gramatyką zapis `$(\neg p)\land q$` zapisem `$(\neg p\land q)$`.
6. **Warunki konieczne i wystarczające:** wyraźnie wskazano, że przykłady arytmetyczne dopuszczają wyłącznie wartościowania pochodzące od tej samej liczby całkowitej. Uzasadniono rachunkowo implikację `4 | n` ⇒ `2 | n` i pokazano, dlaczego nie jest to tautologia dla niezależnych liter zdaniowych.
7. **Nawiasy przy negacji, umowa:** ujednolicono skrót z formalną składnią i hierarchią spójników.
8. **Przypomnienie końcowe:** zastąpiono bezwarunkowe „implikacja nie jest tym samym co implikacja odwrotna” ścisłym „na ogół nie jest logicznie równoważna”, co obejmuje także przypadki szczególne, gdy są równoważne.

## Niezależna kontrola po zmianach

- **10/10** twierdzeń zachowanych, liczba i rozmieszczenie istniejących środowisk bez zmian; nie wprowadzono nowych lematów ani twierdzeń.
- **31/31** etykiet zachowanych w dotychczasowej kolejności; pozostawiono odsyłacz do `ch:syntax-fol`, należącego do rozdziału 09.
- Niezależne testy wszystkich ośmiu układów wartości `p,q,r` obejmujące prawa de Morgana, implikacji i jej przeciwstawienia, negację implikacji, podwójną negację, rozdzielność, modus ponens, modus tollens, przechodniość, sylogizm rozłączny, zasadę eksplozji i pustą listę przesłanek — **zaliczone**.
- Test arytmetyczny: dla zdań `4 | n` i `2 | n` realizowane są wyłącznie pary wartości `(0,0)`, `(0,1)`, `(1,1)`. Para `(1,0)` występuje jedynie przy swobodnych wartościowaniach dwóch niezależnych liter.
- Test poprawności gramatycznej wybranych pełnych zapisów i odrzucania zapisów z nieuprawnionymi nawiasami wokół negacji — **zaliczony**.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — kod zakończenia **0**; **376 stron** dla **44 rozdziałów**; **1075** etykiet (bez duplikatów) i **866** odsyłaczy (bez brakujących celów).
- Rozdział nie zawiera zależności od zewnętrznych plików graficznych ani fragmentów kodu; rysunek drzewa składniowego wykonany bezpośrednio w TikZ.
- Oględziny dziewięciu stron rozdziału wyrenderowanych z kompilacji całego skryptu: nie zaobserwowano kolizji tekstów, rysunków ani błędnego składu wzorów. Rozbudowany przykład przechodzi przez granicę dwóch stron, ale jest czytelny i nie wymaga interwencji.

## Ocena

Po szóstej iteracji oraz dodatkowym przejściu kontrolnym nie wykryto kolejnych usterek w istniejącym materiale. Rozdział 01 można uznać za gotowy do pracy nad rozdziałem 02, z zastrzeżeniem, że audyt nie jest formalnym dowodem bezbłędności całego skryptu. Wynik GitHub Actions dla nowego commitu należy odnotować oddzielnie, po jego zakończeniu.