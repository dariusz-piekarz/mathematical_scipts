# MA1-15 — niezależny audyt 02
Po odczycie HEAD f77cbab stwierdzono, że raport stabilizacji rozdziału 14 i rozdział 15 wraz z audytem 01 już istnieją; nie powielano ich. Rozdział 15 przed zmianami miał blob 12cab51a077644a838ad6bd695b966682143d8dc.
## Przegląd
001–002: poprawne rozróżnienie punktu izolowanego i punktu skupienia, kwantyfikatory i zaprzeczenie kryterium ciągowego.
003–004,014: uzupełniono dowód reprezentacji zbioru względnie otwartego jako przecięcia A z otwartym zbiorem przestrzeni X, przez sumę kul. Wykazano otwartość kuli i dowolnej sumy, obie inkluzje, przypadek pusty, dualne twierdzenie dla zbiorów domkniętych przez dopełnienie. Kryterium przeciwobrazów i kontrprzykłady dla obrazów poprawne.
005–007: złożenie, rachunek ciągłości, niezerowość mianownika, lokalna ograniczoność i zachowanie znaku poprawne.
008–010: zwartość ciągowa, Bolzano–Weierstrass, zachowanie zwartości przez obraz, dowód osiągania kresów i kontrprzykłady poprawne. Ujednolicono kolejność słów w nazwie zwartości ciągowej.
011–012: sprawdzono przypadki końców i zmiany znaku w twierdzeniu o wartości pośredniej; wybór punktu po prawej od supremum poprawny. Rozkład różnicy wielomianu i wniosek o obrazie przedziału poprawne.
013,015: doprecyzowano założenie o przestrzeni X oraz rozpisano nierówność trójkąta na dalszym podciągu, tak aby nie korzystać niejawnie z ciągłości odległości. Jednoznaczność granicy i iniektywność dają sprzeczność. Kontrprzykład dyskretnej metryki poprawny.
## Kontrole
Treść 24ee791 (blob 5a5c2521cb77109af14e9040ab6ed9901525cc45), testy 6f3dba3, rejestr fa09464. Dodano 2 kryteria i 2 metody testowe (15 kryteriów, 13 metod w rozdziale, 134 w tomie), 24 unikalne etykiety. Konflikt 409 przy zapisie rejestru rozwiązano przez ponowny odczyt i zapis. CI 45466560146 i Atlas 45466539534 dla wcześniejszych wersji SUCCESS; terminologia po poprawkach 45466910164 SUCCESS. CI 45466966698 oczekuje, 45466930301 i Atlas 45466910122 w toku. Nie zweryfikowano jeszcze pełnej regresji rozdziału 15 ani PDF po poprawkach. Lean nieuruchomiony. Status: w stabilizacji, nie rozpoczęto rozdziału 16.
