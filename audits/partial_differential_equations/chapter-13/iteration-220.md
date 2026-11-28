# RRC 13 — iteracja 220: uzgodnienie stabilizacji z późniejszym źródłem

Raporty 218 i 219 zamknęły audyty na blobie bb67d3cf0b0d28563e1f8960fe3298a76d5ea418. Równoległe uzupełnienie z iteracji 217 (commit daaa0a4928fb8d85229570f5192c6bcc7874f2c7) zmieniło blob na 9ae8fbff0607c075cca22af178258be8c4b983a6, 1518 wierszy. Potwierdzono, że aktualna gałąź nadal zawiera ten blob. Porównanie obu wersji: identyczny tekst przed sekcją transmisji, wszystkie 40 etykiet w tej samej kolejności, oba bloki TikZ identyczne. Ponownie odczytano wszystkie pięć uzupełnień w ostatnich dwóch sekcjach; bez nowych usterek i bez edycji źródła. Kontrola przyrostowa 055–064 uzupełnia wcześniejszy audyt 001–054 niezmienionego tekstu; nie jest nową pełną niezależną lekturą całych 1518 wierszy.

- Ślady końcowe: gęstość w H¹, jednostajna zbieżność z oszacowania jednowymiarowego, ślad w L² dwóch punktów z miarą liczącą; identyfikacja obu granic prawidłowa.
- Maksimum: znak pochodnej, -9/200+9/100+1/5=49/200, porównanie z prawą częścią prawidłowe.
- Transmisja: globalne H¹ pozostaje hipotezą, lokalne H² implikuje absolutną ciągłość u', całkowanie przez części i znaki prawidłowe.
- Strumień: ciągłe reprezentanty równe p.w. są równe punktowo na domknięciach podprzedziałów.
- Niejednorodny Fredholm: parowanie z L^t, konstrukcja w i u oraz zbiór afiniczny rozwiązań poprawne.

## Walidacja aktualnej wersji

Na commicie daaa0a4928fb8d85229570f5192c6bcc7874f2c7: dedykowany run 45710288699, oba zadania SUCCESS (testy matematyczne, przygotowanie, kompilacja, diagnostyka i render stron; rzeczywisty backend renderowania figur). Artefakt 15067860846 pobrany: PDF 16 stron A4 i 16 PNG; obejrzano wszystkie strony na czterech arkuszach kontaktowych, w tym oba rysunki na stronach 14–15. Nie zauważono obcięć, kolizji ani pustych stron. Log bez Overfull, Missing character i ostrzeżeń o niezdefiniowanych odsyłaczach. Artefakt figur 15066693480 istnieje; nie pobierano go ponownie, ponieważ bloki TikZ RRC 13 nie zmieniły się od kontroli wizualnej 217/219.

Run 45710288456 na tym samym commicie: index-and-test oraz reader-ui SUCCESS, rzeczywisty Chromium PASS. Run 45710288395: terminologia SUCCESS. Artefakt 15066723240 reference-provenance-audit pobrany: graph_coverage.json PDE-13 unresolved=0, within_domain=59, cross_outgoing=0, cross_incoming=0, isolated=false. Wagi wychodzące do RRC 06,07,09,10,11,12 odpowiednio 1,3,11,24,10,5 (54 wystąpienia), przychodzące 5. Jest to dowód agregatowy, nie eksport pojedynczych rekordów SQLite. Weryfikacja źródłowa na tym samym commicie w 217: 106/106 odsyłaczy, 51 różnych celów, bez niejednoznaczności, stos środowisk poprawny.

Decyzja: utrzymujemy zamknięcie rozdziału 13 na aktualnym blobie po uzgodnieniu wcześniejszej kontroli i przyrostowej kontroli wszystkich późniejszych zmian. Nie przeprowadzono Lean, pełnej kompilacji książki ani testu lokalnego komputera użytkownika. Następna iteracja: rozdział 14, pierwszy audyt szczegółowy; sprawdzić najpierw raporty równoległe.