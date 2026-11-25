# CAT-10 — audyt III, kontrola matematyczna

Źródło 250e1f47ce2df533b2ffc6e63b9869ae3f71de0e, audyt II włączony do gałęzi commitem c0115687f42684a176d148a8b471fa4781cf4ad0. Ponownie odczytano całość rozdziału. Sprawdzono typy morfizmów, formuły i odwrotności bijekcji Yonedy, naturalność w obu zmiennych (w tym równoczesną zmianę), rozróżnienie kategorii lokalnie małej i małej, pełność i wierność obu włożeń, odzwierciedlanie izomorfizmów i klasyfikację operacji na krotkach, zbiorze potęgowym oraz grupach. Nie wykryto istotnej nowej luki matematycznej; bez zmiany zakresu i treści. Przypomnienie: przypadki skończone nie zastępują dowodów.

## Niezależny test

Uruchomiono kod JavaScript i zapisano jako tests/mathematical/category_theory/chapter-10/control.js. Wyniki {"parallel":1820,"actions":12,"candidates":130,"embedding":8}. parallel to liczba par funktor–obiekt reprezentujący w kategorii z dwiema równoległymi strzałkami (odwrócenie tej kategorii jest izomorficzne przez zamianę obiektów). actions to liczba działań monoidu wszystkich funkcji dwuelementowego zbioru w obu orientacjach mnożenia; candidates to liczba sprawdzonych funkcji z reprezentowalnego działania regularnego, embedding to liczba endomorfizmów naturalnych tego działania. Liczniki mają różne jednostki, nie sumujemy. Wszystkie sprawdzenia przeszły. 

## Status

CI I 45593258221: queued/null. CI II po włączeniu c0115687f42684a176d148a8b471fa4781cf4ad0 jeszcze niepotwierdzony. Porównano 32 plików zakresu CI z commitem audytu II. PDF i finalna walidacja otwarte; Lean nie uruchomiono. Nie zamykamy CAT-10 przed zaliczeniem CI i kontrolą wizualną.

## Zamknięcie walidacji technicznej

Po korekcie błędu wcięcia testu CAT-10-010 (commit 0df8d9855124e8a040e97bf6309c31340f5f4d8d, opis w local-validation.md) CI 45596310572 completed/success: 74/74 testy, 8/8 kroków job 139143184315 success. Artefakt 15013768362: category_theory.pdf (59 stron) i końcowy log. Sprawdzono lokalnie brak Warning, Overfull i błędów ^! w logu. Render pdftoppm 110 dpi i oględziny wszystkich stron 44–48, zawierających CAT-10 (sekcja 11): brak widocznych obcięć, kolizji, błędów odsyłaczy. Porównano 32 plików z zakresu CI z aktualną gałęzią przed zapisem. CAT-10 zamknięty. Następny CAT-11. Lean nie uruchamiano.
