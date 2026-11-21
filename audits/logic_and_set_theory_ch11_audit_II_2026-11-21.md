# Logika matematyczna i teoria mnogości — rozdział 11, audyt II

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Plik:** `chapters/pl/logic_and_set_theory/11-dowody-formalne-i-dedukcja-naturalna.tex`.  
**Punkt wyjścia:** SHA `065fa9c5387ba37410dbfd3d0e1f123d69acda4b` po audycie I.  
**Zakres:** powtórny niezależny przegląd **5 twierdzeń, 5 dowodów, 7 definicji, 16 przykładów i 8 uwag**. Nie dodano żadnego twierdzenia, definicji, lematu ani przykładu.

## Wynik: usterka w przykładzie o symetrii równości

W przykładzie „Symetria równości” podano formułę pomocniczą `θ(x):=x=t` i wywnioskowano, że `θ[x:=t]` równa się `t=t`, a `θ[x:=u]` równa się `u=t`. To rozumowanie jest poprawne **tylko jeśli `x` nie występuje w `t`**. Teza przykładu dotyczy jednak **dowolnych termów `t,u`**.

**Jawny kontrprzykład dla pierwotnego kroku:** niech `t=f(x)`, `u=c`. Przy `θ(x):=x=f(x)` otrzymujemy
- `θ[x:=t]` = `f(x)=f(f(x))`, a nie `f(x)=f(x)`;
- `θ[x:=u]` = `c=f(c)`, a nie `c=f(x)`.

W poprawionym przykładzie wybieramy **świeżą zmienną `z` niewystępującą ani w `t`, ani w `u`** i przyjmujemy `θ(z):=z=t`. Wtedy podstawienia są dopuszczalne i faktycznie zachodzą `θ[z:=t]=(t=t)` oraz `θ[z:=u]=(u=t)`. Użycie `=E` z przesłankami `t=u` i `t=t` daje poprawnie `u=t`. Teza pozostała bez zmian, przykład nie został zastąpiony nowym.

## Pozostałe wyniki drugiego audytu

1. **Reguły zdaniowe** `∧I/E`, `∨I/E`, `→I/E`, `↔I/E`, `¬I/E`, `⊥E`, klasyczna `RAA`: sformułowania odpowiadają poprawnym schematom z rozładowaniem oznaczonych założeń.
2. **Twierdzenie o dedukcji**: poprawne oba kierunki, również gdy `φ` jest już w `Γ` lub nie jest użyta w poddedukcji. Konstrukcja dopuszcza rozładowanie pustego zbioru wystąpień.
3. **Prawo wyłączonego środka**: dowód przez `RAA` zachowuje dokładnie jedno otwarte założenie do ostatniego kroku, następnie je rozładowuje.
4. **Reguły kwantyfikatorów**: poprawka z audytu I uzależnia warunek świeżości w `∃E` od faktycznie użytych otwartych założeń, nie od nieskończonego zbioru `Γ`. Zmienna nie występuje w `φ` i `θ`, więc podstawienie za `x` jest dopuszczalne; zewnętrzna przesłanka główna również spełnia warunek świeżości.
5. **Łańcuch uniwersalny**: podstawienie `x:=x` jest zawsze dopuszczalne i nie przechwytuje zmiennych pod wewnętrznymi kwantyfikatorami. Końcowe `∀I` nie narusza warunku o otwartych założeniach.
6. **Projekcja egzystencjalna**: wybór `y` nieobecnej w dwóch formułach i pozostałych założeniach umożliwia bezpieczne `∃E`; wniosek nie zależy od wartości zmiennej lokalnego świadka.
7. **Kontrmodele świeżości**: oba przykłady po audycie I są prawidłowe, w tym `∃x ¬(x=y)` z niedozwolonym świadkiem `y`.
8. **Skończone użycie założeń**: dowód przez skończone drzewo i zebranie otwartych liści nadal jest poprawny; nie zakłada, że `Γ` jest skończony.
9. **Schematy równości**: `=I` i `=E` same są poprawne; błąd dotyczył wyłącznie sposobu podstawiania w jednym przykładzie. Pozostały przykład o `t=t` i sprzeczności jest poprawny.

## Niezależne testy drugiej iteracji

W drugim audycie zbadano dodatkowo:
- **4** wartościowania pary atomów i **12** sprawdzeń trzech reprezentatywnych tautologii (w tym LEM i przemienności koniunkcji).
- **904** struktury w wybranych uniwersach 1-, 2- i 3-elementowych z predykatami zawierającymi wewnętrzne kwantyfikatory. Zweryfikowano semantyczną poprawność twierdzenia o łańcuchu uniwersalnym.
- **340** konfiguracji par predykatów do sprawdzenia `∃x(P(x)∧Q(x))⇒∃xP(x)`.
- **4740** kontroli zastępowania równych wartości przez równość w wybranych interpretacjach predykatów.
- **576** przypadków rozbieżności spowodowanej błędnym podstawieniem, które przechwytuje zmienną.
- **9** kontrmodeli wykazujących nieskuteczność pominięcia świeżości względem przesłanki głównej.
- **26** termów testowych (zmienne, stała, zagnieżdżone funkcje), co dało **676 par `(t,u)`**, dla których zweryfikowano krok `θ(z)` ze świeżą zmienną i dodatkowo bezpośredni kontrprzykład obalający poprzedni zapis. Trwałą regresję zapisano w `tools/tests/test_logic_and_set_theory_ch11.py`.

**Zero kontrprzykładów** dla poprawionych kroków; kontrprzykłady dla wadliwej wersji ujawniono i utrwalono. Są to ograniczone testy falsyfikacyjne, a nie dowody poprawności całego rachunku pierwszego rzędu.

## Integralność i CI

Zachowano **5 twierdzeń i 5 dowodów, 7 definicji, 16 przykładów, 8 uwag, 21 etykiet oraz 7 odsyłaczy** rozdziału 11. Rozdziały 01–11 nadal powinny zawierać **309 unikatowych etykiet, 119 odsyłaczy**, z dokładnie jednym udokumentowanym celem przyszłym `ch:zf-axioms`.

Poprzedni przebieg CI na audycie I był zielony: [44928682010](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44928682010) (103 strony, 18 testów, bez nieoczekiwanych brakujących odsyłaczy i przepełnień); globalna walidacja aplikacji [44928681964](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44928681964) również przeszła. Nowy commit z audytem II musi przejść obie walidacje ponownie; ich wyniku nie zakładamy przed sprawdzeniem.

## Status

**Audyt II: wykryto i poprawiono błędny krok podstawienia w przykładzie dowodzącym symetrii równości.** Rozdział 11 pozostaje **otwarty do audytu III**, zgodnie z zasadą kontroli każdego zmienionego źródła przed uznaniem go za stabilne. Bez rozszerzania materiału.
