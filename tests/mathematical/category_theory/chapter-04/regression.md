# CAT-04 — audyt I i trwałe kryteria regresyjne

Źródło: chapters/pl/category_theory/04-transformacje-naturalne.tex. Commit cc22e02b0e7efd41cc2708c8963b52373ace45d7, blob cea506e802e9c9eeea411c9681cda97eb137f5f9.

## Zmiany
- Rozróżniono składanie pionowe i poziome, udowodniono naturalność składania poziomego, prawo wymiany, łączność i jednostki; uwzględniono składanie z funktorem po obu stronach.
- Uzupełniono argument lokalnej małości kategorii funktorów przy małym źródle i lokalnie małym celu.
- Uzasadniono iniektywność kanonicznego odwzorowania do przestrzeni podwójnie dualnej, izomorfizm w skończonym wymiarze i kontrprzykład surjektywności na k^{(N)}; jawnie użyto istnienia bazy Hamela.
- Dodano naturalność izomorfizmu tensorowego, odwzorowania łączącego, izomorfizmu de Rhama oraz zapowiedź naturalności GAGA.
- Poprawiono niefortunne tytuły przykładów, zachowano dotychczasowe etykiety. Kontrola stosu środowisk przy zapisie zaliczona.

## Wykorzystanie źródeł
- AA-18, faaa972f8d1a7625d42c856d78c6f58ee7ad3564, aa:tw:tensor-unit: element neutralny tensoru; wykorzystano twierdzenie i dopisano rachunek naturalności.
- AT-03, 03ee5b773493ee95746413aabd760d54b6a640e6, uwaga:les-naturalnosc: naturalność odwzorowania łączącego; przedstawiono rachunek na podniesieniach jako naturalną transformację. Nie kopiowano pełnego dowodu długiego ciągu dokładnego.
- DG-10, 858d30abdfb27335f8194740f2304ee98d5ca15a, thm:de-rham, eq:de-rham-iso: naturalność całkowania, rozróżniono kołańcuchy gładkie i zwykłe oraz naturalny izomorfizm ograniczenia.
- ALG-09, 32ebab6fc0b6a27855615716b63fa9f58c57ba0c, tw:ga9-gaga: właściwe schematy skończonego typu nad C i naturalne izomorfizmy kohomologii koherentnych snopów. Wynik zewnętrzny, nie przedstawiono jako dowiedzionego tutaj.
- AT-05 odczytano jako dodatkowe źródło kontekstu, bez osobnego importu. Nie weryfikowano odrębnego CI źródeł.

## Kryteria regresyjne
| ID | Odsyłacz | Metoda i kryterium |
|---|---|---|
| CAT-04-001 | cat:thm:interchange | Python + semantyczna: zgodność obu stron prawa wymiany |
| CAT-04-002 | cat:prop:horizontal | Python + semantyczna: naturalność składania poziomego |
| CAT-04-003 | cat:ex:tensor-unit-natural | Python + semantyczna: zgodność z działaniem homomorfizmu w modelu cyklicznym |
| CAT-04-004 | przyklad:podwojny-dual | Python + semantyczna: iniektywność ewaluacji w skończonym wymiarze |
| CAT-04-005 | tw:nat-iso-components | Python + semantyczna: naturalność odwrotności |
| CAT-04-006 | sec:naturalne | Python: zachowanie etykiet i środowisk |
| CAT-04-007 | cat:prop:vertical | semantyczna: lokalna małość kategorii funktorów |
| CAT-04-008 | cat:prop:horizontal-assoc | semantyczna: typy, łączność i jednostki poziome |
| CAT-04-009 | przyklad:podwojny-dual | semantyczna: niesurjektywność na k^{(N)} i użycie wyboru |
| CAT-04-010 | cat:ex:connecting-natural | semantyczna: zgodność podniesień i naturalność delta |
| CAT-04-011 | cat:ex:derham-natural | semantyczna: wariancja, całkowanie, ograniczenie kołańcuchów |
| CAT-04-012 | cat:ex:gaga-natural | semantyczna: hipotezy, naturalność w snopie, status wyniku zewnętrznego |

Testy automatyczne: tools/tests/test_category_theory_ch04.py, commit b0543ae54415156a9f99d3141998ac8558037f0d. Istniejący workflow discovery obejmuje plik. W tej iteracji nie potwierdzono jeszcze wykonania testów i kompilacji PDF. Nie wykonano formalizacji Lean.

Status: otwarty audyt stabilizacyjny. Kolejna iteracja bez rozszerzania zakresu.
