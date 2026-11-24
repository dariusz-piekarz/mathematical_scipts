# AA-58 — audyt III: forma Killinga, rozkład, derywacje i kolizje etykiet

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Commit 7c719440a33d51216d2fafeb0c20fb9bba11fb47, blob 0c16050097e6e9a1db456b98b1f4d29fd7372236.

## Kontrola matematyczna i korekty
Uściślono przejście od prostoty do zerowego radykału, założenia lematu o ideałach ortogonalnych i stwierdzenia o formie śladu, dowód rozkładu jako izomorfizmu algebr Liego (nie jedynie przestrzeni wektorowych), cykliczność śladu w dowodzie wewnętrzności derywacji. W obliczeniach klasycznych form Killinga jawnie określono dziedzinę operatorów, dobrze określony izomorfizm tensorowy przez własność uniwersalną, jego działanie na bazie, rzuty i obie tożsamości śladowe. Rozróżniono niezdegenerowanie od braku niezerowych wektorów izotropowych i dodatniej określoności nad R. 12 korekt fragmentów, 930 wierszy. Zakres bez zmian.

## Niezależne obliczenia
Kod JavaScript tworzy jawne bazy gl_n, sl_n, so_n dla n=1,...,6 i sp_(2n) dla n=1,...,4 (łącznie 22 modele, w tym zerowe). Dla każdej uporządkowanej pary oblicza komutator przez mnożenie macierzy naturalnych, odzyskuje współrzędne w bazie (w sl_n przez sumy prefiksowe przekątnej), rekonstruuje komutator i porównuje wszystkie wpisy. Następnie wyznacza ślad iloczynu macierzy dołączonych i porównuje ze wzorem z rozdziału. Dokładna arytmetyka całkowita w bezpiecznym zakresie JavaScript Number. gl: 2275, sl: 2099, so: 371, sp: 1846 par, 6591/6591 rekonstrukcji i 6591/6591 zgodności form. Nie zastępuje dowodu ogólnego.

## CI i etykiety
Run 45370329109, job 138362670850, failure na Run repository tool tests. Log: 4675 testów, 8 niepowodzeń; testy przekrojowe wykazały 1161 etykiet wobec 1159 unikalnych. Zlokalizowano dokładnie dwie kolizje w AA-58: aa:lem:solvable-extension z AA-05 i aa:prz:radical-examples z AA-12. Zmieniono wyłącznie nowe etykiety na aa:lem:lie-solvable-extension i aa:prz:lie-radical-examples wraz z lokalnymi odsyłaczami. Starszych plików nie zmieniano. Log wykazał również odrębne 24 problemy walidatora repozytorium (dwa brakujące zagnieżdżone importy grafów i miary oraz 11 niespójnych kopii rozdziałów geometrii różniczkowej i odpowiadających sum kontrolnych). Nie ingerowano w inne skrypty, nie deklarowano naprawy globalnych problemów. Nowy run [{"id":45371914625,"status":"in_progress","conclusion":null}]. Środowiska LaTeX zrównoważone. Nie oglądano PDF.

## Werdykt
AA-58 W AUDYCIE, 0/2 czystych audytów po korektach III. Następnie kontrola radykału, rozszerzeń, przypadków brzegowych i ponowna weryfikacja kryteriów Cartana; pełna kontrola etykiet i CI. AA-59 nieotwarty.
