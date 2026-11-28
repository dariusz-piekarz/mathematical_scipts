# PDE — rozdział 09 — iteracja 142, CI i kontrola wizualna

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.

## Wynik rzeczywisty
Run 45611895966, job 139197285264, head c41381c202bacb282cdb09e2fa0693e1caf3e926: success.
Testy wykonywalne, odsyłacze i struktura, kompilacja, diagnostyka, renderowanie oraz publikacja artefaktu: success.
Źródło rozdziału w tym przebiegu: blob 30d48c49e6db0d013e8fff4cfc9960323e25342b.
Artefakt 15020078686: pobrano ZIP i zweryfikowano SHA-256 bf065a7d78b3472af1dcaaf2cd9079d3d80ea68090b2afbe557f31bd399c6a40 zgodnie z metadanymi API.
PDF: 25 stron A4. Log: brak krytycznych diagnostyk wyszukiwanych przez workflow; 25 ostrzeżeń hyperref o pustych celach zewnętrznych w izolowanym rozdziale, jedno Underfull hbox (badness 1142). Te ostrzeżenia nie są dowodem poprawności pełnej książki.

## Inspekcja wizualna
Przejrzano wszystkie 25 renderów w zestawieniach stron oraz strony 9 i 25 indywidualnie. Nie zauważono obciętych formuł, kolizji bloków tekstu ani pustych stron. Na stronie 9 etykieta B_epsilon(x) rysunku była zbyt blisko prawego brzegu zielonego obszaru U. Przesunięto ją z (1.82,-.38) na (1.60,-.65) w commicie 9c038ce99e782076460e1ea49b74f8c3d0cce393 (nowy blob b14ed2a90f238b9b1429b49712f6b933b1075bf4). Zmiana wyłącznie wizualna, bez zmiany treści matematycznej. Nie zweryfikowano jeszcze renderu po tej zmianie.

## Bramka stabilizacji
Dedykowane CI poprzedniego bloba: PASS. Po korekcie rysunku wymagane ponowne CI i kontrola strony z rysunkiem; niezależny audyt kontrolny nadal do wykonania. Nie uznawać rozdziału za ustabilizowany. Nie uruchamiano Lean ani pełnej kompilacji książki w tej iteracji. Kolejna iteracja 143: odczytać CI dla nowego bloba, obejrzeć poprawioną stronę i rozpocząć niezależny audyt kontrolny.
