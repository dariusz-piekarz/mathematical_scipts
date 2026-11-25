# AM II 03 — audyt otwarty

## Źródła i zakres
AM I 10: kryterium Leibniza, przykład i rysunek szeregu naprzemiennego harmonicznego, części dodatnia i ujemna, pełny dowód twierdzenia Riemanna (dowolna suma rzeczywista, obie nieskończoności, oscylacje), przykład przestawienia harmonicznego. Zachowano sześć oryginalnych etykiet importowanych wyników i rysunku; definicja części dodatniej/ujemnej ma nową etykietę, ponieważ definicję zbieżności warunkowej uogólniono osobno. AF 27: rozwinięcie kryterium permutacji i sum skończonych, bez konieczności zakładania ogólnej zupełności sieci. Nowe twierdzenia o ograniczonych mnożnikach, równoważności w skończonym wymiarze, kontrprzykład w l2. Rozróżniono dwa znaczenia zbieżności warunkowej w nieskończonym wymiarze. Ogólne twierdzenie Dvoretzky'ego–Rogersa wymieniono jako wynik poza zakresem dowodu, nie używa się go w żadnym dowodzie.

## Pierwszy audyt szczegółowy
Wersja początkowa bd54a1f321d9d7536bb078db88e6dd317f02094d — 426 wierszy.
Wersja po poprawkach 41ec40cf1b509e4ff228e2c8a50ff686dadacedc — 449 wierszy.
Doprecyzowano znaczenie zbieżności warunkowej, hipotezy przestawienia szeregu bezwzględnie zbieżnego w przestrzeni niezupełnej, oszacowanie reszty bez założenia zupełności, kryterium Cauchy'ego, indeksy sum częściowych podszeregu, pomocniczą notację teleskopową i rozkład mnożników rzeczywistych oraz zespolonych, uzasadnienie skończonego oszacowania współrzędnościowego. Zachowano dotychczasowe etykiety; rozdziały 01 i 02 bez zmian.

Kontrola statyczna: 449 wierszy, 14 etykiet, 15 wystąpień odwołań, 7 dowodów, 3 przykłady, 1 rysunek. Brak duplikatów etykiet w obrębie AM II i brak lokalnych odsyłaczy bez celu, zbilansowane środowiska. Rejestracja rozdziału w entrypoincie i katalogu wykonana.

Status OTWARTY; czyste audyty 0/2. Konieczny dalszy przegląd dowodów, kompilacja i kontrola wizualna PDF. Nie rozpoczynać rozdziału 04 przed stabilizacją.

## Drugi audyt szczegółowy — 2841f196a0251ec117e2bd0e25b01eeee8834248

Doprecyzowano dziedziny definicji i hipotezy, zależność progu k0 od N w dowodzie przestawień, oznaczenia granic w kryterium Leibniza i odsyłacz do rysunku, indeksy sum częściowych w konstrukcji permutacji oraz sformułowanie twierdzenia o częściach dodatniej i ujemnej. Dodano odwołanie do kontrprzykładu c00 z rozdziału 02 dla warunku sum skończonych bez zupełności. Rozpisano oszacowanie dla mnożników z [0,1], rozkład skalarów i oszacowania ze stałymi 2 dla ciała rzeczywistego i 4 dla zespolonego. Udowodniono równoważne kryterium zbieżności wszystkich szeregów ze znakami +/-1 oraz jednostajną zbieżność ogonów względem wszystkich mnożników o module co najwyżej 1. Sprecyzowano treść twierdzenia Dvoretzky'ego–Rogersa jako wynik niewykorzystywany, bez dowodu. Nie modyfikowano rozdziałów 01–02.

Kontrola statyczna: 524 wiersze, 15 etykiet, 20 wystąpień odwołań, 8 dowodów, 3 przykłady i 1 rysunek; 0 duplikatów etykiet w AM II, 0 lokalnych odsyłaczy bez celu, zbilansowane środowiska. Zachowano wszystkie dotychczasowe etykiety. W chwili rozpoczęcia iteracji CI #45668099034 dla 41ec40c było w kolejce. CI nowej wersji i kontrola wizualna PDF jeszcze niepotwierdzone. Status OTWARTY; licznik czystych audytów 0/2. Następnie ponowny przegląd całego rozdziału bez rozszerzania zakresu, o ile nie zostaną wykryte rzeczywiste braki, i końcowa walidacja. Nie przechodzić do rozdziału 04.
