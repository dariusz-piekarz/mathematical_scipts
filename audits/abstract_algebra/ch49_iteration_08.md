# AA-49 — audyt VIII: porównanie pełnych wydań PDF

Stan wejściowy 75a65bab585faeb8c8ee7230fee0ca1b6154e775. Bez zmian matematyki, źródeł i testów.

## Rzeczywiste porównanie dwóch artefaktów
Porównano lokalnie wcześniej pobrane PDF: artefakt 14971458539 (SHA-256 PDF c62f08a759337ba4b83fd7f25df8a290c080ca7889521e77f90b0b63c91daf0b) i artefakt 15001446403 (SHA-256 PDF 0545e2a80c0e270b48a9236cb7065e06553387789f744eb42f3d8499bdd94548). Oba mają 444 strony. Dla każdej strony porównano dokładnie próbki rastra PyMuPDF w skali 1:1 (72 dpi, skala szarości, bez alpha), rozmiar rastra i tekst get_text(). 440 stron identycznych pikselowo i tekstowo; jedyne różnice to strony fizyczne 1, 318, 319, 320. Są to strona tytułowa i trzy strony AA-49. Pozostałe rozdziały nie zmieniły się w tym porównaniu. Obydwa wydania mają identyczne początki rozdziałów AA-48–51: 309, 315, 321, 328.

Dla artefaktu 15001446403: 434 zakładki, 72 zakładki poziomu 1 w ściśle rosnącej kolejności stron; 220243 pozycji słów, zero prostokątów słów poza granicami strony, zero pustych warstw tekstowych, 1368 linków, zero odsyłaczy typu LINK_GOTO z numerem strony poza dokumentem, is_repaired=False. Kontrola automatyczna nie stanowi oględzin wszystkich stron ani sprawdzenia semantycznego celu każdego odsyłacza. Wcześniej ręcznie obejrzano sześć stron AA-49 i stronę tytułową (audyt VI).

## Ostatni przebieg
Run 45568873731, head 17d3fdf94bc02fae4800c9bd5755697ecae60510, job 139050319803: dedykowane regresje AA-49 SymPy i Fraction oraz globalna bramka integralności mają status completed/success. Przy ostatnim odczycie 144 kroki success, aktywna kompilacja latexmk, 5 kroków oczekujących. Brak artefaktu ostatniej korekty redakcyjnej przy sprawdzeniu. Wcześniejsze porównanie nie obejmuje tej korekty. Nie wykonano nowej lokalnej kompilacji całej książki (brak kompletnego drzewa źródeł w środowisku lokalnym). Nie uruchomiono Lean.

Następna kontrola: po pojawieniu się artefaktu 45568873731 porównać go z 15001446403 i obejrzeć zmienione strony AA-49; dopiero wtedy formalnie zamknąć rozdział. Brak nowych usterek w wykonanym zakresie. Nie powtarzać niezmienionych kontroli matematycznych, nie otwierać AA-73.
