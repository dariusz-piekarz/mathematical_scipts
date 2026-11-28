# Topologia ogólna — rozdział 17, audyt iteracja 03

Data: 2026-11-22. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: chapters/pl/general_topology/17-uzwarcenia-aleksandrowa-i-cecha-stonea.tex.
SHA zweryfikowanej, niezmienionej treści: 6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4.

## Niezależna kontrola po audycie 02

Wykonano niezależne sprawdzenie wszystkich definicji, twierdzeń, dowodów, przykładów i odsyłaczy. Nie dopisywano wyników ani nie modyfikowano źródła LaTeX.

1. **Topologia Aleksandrowa.** Dowolne sumy zbiorów zawierających nowy punkt odpowiadają przecięciom zwartych podzbiorów X. Ponieważ X jest Hausdorffa, zbiory te są domknięte, a ich niepuste przecięcie jest domkniętym podzbiorem jednego ustalonego zbioru zwartego, więc jest zwarte. Skończone przecięcia odpowiadają skończonym sumom zbiorów zwartych; mieszany przypadek sprowadza się do C\U. Rozpatrzono także puste rodziny.
2. **Zwartość, gęstość i Hausdorffowość.** Z dowolnego pokrycia wybieramy otoczenie nieskończoności, którego dopełnienie jest zwarte. Niezwartość X gwarantuje nieizolowalność dodanego punktu i gęstość X. W przestrzeni lokalnie zwartej Hausdorffa otwarty U o zwartym domknięciu C pozwala rozdzielić x i nieskończoność przez U oraz dopełnienie C. Odwrotność opiera się na udowodnionym w rozdziale 14 dziedziczeniu zwartości lokalnej przez otwarte podprzestrzenie.
3. **Własność uniwersalna odwzorowań właściwych.** Dla niezwartych lokalnie zwartych Hausdorffa X,Y odwzorowanie f:X→Y przedłuża się ciągle, przy ustalonej wartości nieskończoność w nieskończoność, dokładnie przy zwartości przeciwobrazów wszystkich zwartych C⊂Y. W dowodzie sprawdzono osobno przeciwobrazy zbiorów otwartych w Y i otoczeń dodanego punktu; w przeciwnym kierunku preobrazy C są domknięte w zwartym X* i nie zawierają nowego punktu.
4. **Minimalność i jednoznaczność uzwarcenia jednopunktowego.** Dla dowolnego uzwarcenia (K,e) otwartość e(X) w K wynika z lokalnej zwartości i domkniętości zwartych e(C) zawierających odpowiednie otoczenia. Zwijając niepustą resztę K\e(X) do nowego punktu uzyskujemy ciągłe surjektywne odwzorowanie K→X*. Gęstość i Hausdorffowość celu zapewniają jednoznaczność. Gdy reszta jest jednopunktowa, odwzorowanie staje się homeomorfizmem. Kierunek relacji: (X*,ι)≼(K,e), zgodny z definicją rozdziału 16.
5. **Prosta i okrąg.** W audycie 02 jawnie rozpisano granice odwzorowania exp(i(2 arctan t+π)) przy t→±∞ oraz wybór M, dla którego dopełnienie [-M,M] w X* odwzorowuje się do zadanego otoczenia punktu 1 w S¹. Ponowny audyt potwierdza ciągłość w dodanym punkcie, bijektywność oraz poprawność przejścia od ciągłej bijekcji przestrzeni zwartej na Hausdorffa do homeomorfizmu.
6. **Lokalnie zwarta Hausdorffa ⇒ Tychonoffa.** Lemat z rozdziału 14 pozwala wybrać otwarty W o zwartym domknięciu C rozłącznym z domkniętym F. Lemat Urysohna w C oddziela x od C\W; na domkniętych C oraz X\W funkcje zgadzają się na przecięciu, więc zastosowanie lematu o sklejaniu jest uprawnione. Rozdzielenie punktu od F i aksjomat T1 są wykazane.
7. **Uniwersalna własność βX.** Zanurzenie e_X do kostki funkcji X→[0,1] pochodzi z rozdziału 7. Dla f:X→L, gdzie L jest zwarta Hausdorffa, i g∈C(L,[0,1]) funkcja g∘f indeksuje współrzędną w kostce X. Funkcja Φ(z)_g=z_(g∘f) jest ciągła współrzędnie. Obraz gęstego e_X(X) leży w domkniętym e_L(L), więc cały obraz βX leży w e_L(L). W konsekwencji przedłużenie e_L^{-1}∘Φ ma wartości w L, a nie jedynie w kostce; jest ciągłe i jednoznaczne.
8. **Przedłużenia funkcji ograniczonych i maksymalność.** Ograniczona funkcja rzeczywista przyjmuje wartości w pewnym zwartym przedziale, więc ma przedłużenie; przypadek funkcji stałej jest dopuszczony. Jedyny zgodny czynnik p:βX→K jest surjektywny dzięki zwartości obrazu zawierającego gęste e(X). Jeżeli wszystkie funkcje X→[0,1] przedłużają się do K, to dla każdego f zachodzi F_f∘p=π_f|_{βX}, gdzie π_f zostało już jawnie zdefiniowane. Równość obrazów przez p wymusza równość wszystkich współrzędnych i punktów kostki; p jest więc homeomorfizmem.
9. **Porządek i przykład N.** Z minimalności i maksymalności wynika (X*,ι)≼(K,e)≼(βX,e_X) dla każdej niezwartej lokalnie zwartej przestrzeni Hausdorffa X. W przykładzie N z topologią dyskretną uzwarcenie ciągu zbieżnego jest uzwarceniem jednopunktowym; funkcja naprzemienna nie przedłuża się do tego uzwarcenia, ale przedłuża się do βN. Potwierdza to ich nierównoważność.
10. **Terminologia i zależności.** Sprawdzono nazwy obu uzwarceń, wszystkie kwantyfikatory, wprowadzenie oznaczeń i odsyłacze. Źródłowe wyniki o kostce z rozdziału 7, otoczeniach o zwartym domknięciu z rozdziału 14 i porządku uzwarceń z rozdziału 16 istnieją i mają właściwe założenia. Brak zależności od przyszłych rozdziałów.

## Walidacja techniczna

Zweryfikowano w GitHub Actions przebieg 45014196221 (https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014196221): completed/success, w tym osobno kroki testu rozdziału 17, kompilacji pełnej książki, samodzielnego rozdziału i kontroli logów. Ponieważ w iteracji 03 treść LaTeX i testy się nie zmieniły, przebieg dotyczy dokładnie audytowanej wersji źródła.

Ponownie obejrzano zestawienie wszystkich pięciu stron PDF z artefaktu 14751178008, a także zweryfikowano plik /mnt/data/topologia17_audyt02/general_topology_ch17.pdf (pięć stron). Brak kolizji wzorów, ucięć i nieczytelnego tekstu. Log bez ostrzeżeń został sprawdzony w iteracji 02; krok Check PDF and LaTeX log potwierdzono ponownie w iteracji 03.

## Werdykt iteracji 03

| Kryterium | Wynik |
| --- | --- |
| Konstrukcja i kryterium uzwarcenia Aleksandrowa | PASS |
| Przedłużanie odwzorowań właściwych, minimalność | PASS |
| Całkowita regularność i uniwersalna własność βX | PASS |
| Przedłużanie funkcji, maksymalność βX | PASS |
| Przykłady, przypadki brzegowe i porządek | PASS |
| Terminologia, etykiety i odsyłacze | PASS |
| Testy, pełna książka, samodzielny PDF | PASS |
| Poprawki wymagane w audycie 03 | **BRAK** |
| Status | **STABILNY — audyt 03 zamknięty** |

Po trzech iteracjach, w tym niezależnym czystym reaudycie, rozdział 17 spełnia przyjęte kryteria stabilizacji. Następny rozdział to 18: przestrzenie odwzorowań i topologia zbieżności jednostajnej na zbiorach zwartych.
