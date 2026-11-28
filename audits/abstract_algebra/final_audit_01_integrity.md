# AA-01–72 — końcowy audyt przekrojowy I: integralność i przygotowanie mapy zależności

Stan wejściowy f941965d971ce54d66ac683198122c6233dd13c4. Nie otwierano AA-73.

## Potwierdzona integralność

Bezpośrednio porównano uporządkowaną listę 72 plików z katalogu chapters/pl/abstract_algebra z 72 importami książki i 72 wpisami catalog/books.json. Dokładnie jeden wpis książki abstract_algebra/pl, właściwy entrypoint i identyczna kolejność: PASS. Odczytano rzeczywisty log job 138836379787, run 45504587648, w którym istniejąca bramka globalna dla AA-01–72 zaliczyła 1288 etykiet (1288 unikatowych), 932 odsyłacze (501 różnych celów), zero duplikatów, brakujących celów i błędów kolejności rozdziałów. 598 środowisk proof, 312 twierdzeń, 182 lematy, 70 wniosków i 363 przykłady; liczności nie oznaczają dowodu poprawności. Porównanie wcześniejszego zielonego commitu z wejściowym stanem wykazało brak modyfikacji źródeł algebry, preambuły i testów do końca audytu VI.

## Usterka i naprawa

Strona tytułowa pozostawała przy nieaktualnym opisie „Rozdziały 01–71 stabilne; rozdział 72 w audycie”. Commit 1e163c6dbc26f94b340f3931f729289a90b9494a aktualizuje status: stabilizacja rozdziałowa 01–72 zakończona, audyt końcowy tomu w toku. Nie zmieniono matematyki ani etykiet. Nową kompilację i inspekcję tytułu należy jeszcze potwierdzić.

## Jawne odsyłacze w AA-01–20

Odczytano źródła 01–10 i 11–20 z tego samego commitu; odpowiednio 270 i 251 unikatowych etykiet, 58 i 89 odsyłaczy. W obu blokach zero lokalnych duplikatów. W 01–10 wykryto dwa odsyłacze w przód w AA-06: do rozdziału 08 i twierdzenia o iloczynie tensorowym grup cyklicznych; dodatkowo odsyłacz do AA-18 spoza bloku. Wszystkie trzy są jawnym wskazaniem dalszego rozwinięcia, a nie użyciem wyniku w dowodzie wcześniejszego twierdzenia. W 11–20 trzy odsyłacze w przód: AA-17:114 do lematu Smitha–Bézouta, AA-18:115 do stwierdzenia o bazie iloczynu tensorowego przestrzeni wektorowych i AA-18:119 do przykładu cyklicznego. Pierwszy jest zapowiedzią techniki, drugi stanowi jawne uzasadnienie przykładu przez później udowodniony wynik, trzeci wskazuje dalszy przykład. Nie stwierdzono koła dowodowego w tych miejscach; globalna ocena zależności nadal otwarta. Próba jednorazowego odczytu 21 źródeł przekroczyła limit wywołań; dalsze źródła wymagają kontroli partiami lub wyniku bramki CI.

## Trwała bramka

Commit 24dcff5618b9cdcd7c153467cdb3877236ce17c7 rozszerza istniejący test tools/tests/test_abstract_algebra_global_integrity.py o zgodność katalogu z uporządkowanymi źródłami, pozycje etykiet, listę jawnych odsyłaczy w przód i grupy silnie spójne grafu odsyłaczy między rozdziałami. Odsyłacze w przód i grupy cykliczne są diagnostyką do ręcznej klasyfikacji, a nie samoczynnym werdyktem o błędzie matematycznym. Workflow już śledzi i uruchamia ten plik. Nowej wersji bramki nie wykonano lokalnie na pełnym drzewie; potrzebny wynik aktualnego CI. Nie uruchamiano Lean.

## Następna iteracja

Odczytać wynik rozszerzonej bramki, zweryfikować nowe wydanie PDF (w tym stronę tytułową), sklasyfikować jawne odsyłacze w przód i grupy cykliczne, następnie przejść do semantycznej kontroli zależności na granicach bloków AA-01–42 / AA-43–55 / AA-56–72. Nie zamykać tomu na podstawie samych statystyk.
