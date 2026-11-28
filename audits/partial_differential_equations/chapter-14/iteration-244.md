# RRC 14 — iteracja 244: kontrola po stabilizacji

Odczytano pełne źródło (1425 wierszy, blob 52e83d128c67c3d18228f7ffaff226cb6e81b941) i zinwentaryzowano tezy definicji, lematów, twierdzeń, wniosków oraz kontrprzykładu. Kontrola przekrojowa po czwartej czystej lekturze:

- Słaba zasada: rzeczywistość, eliptyczność bez symetrii, ograniczony obszar Lipschitzowski, ślad, c>=0, M>=0 lub c=0; kontrprzykłady przy ujemnym c i M — poprawne.
- Mocna zasada: spójność, d>=2 (d=1 osobno), globalne ekstremum, lokalna wersja w RRC 03; dodatniość i jednoznaczność — poprawne.
- Hopf: niestałość, globalne minimum brzegowe, kula wewnętrzna, dodatnia granica dolna, pochodna tylko przy istnieniu granicy; klin — poprawne.
- Harnack: nieujemność, r<R, stałe niezależne od rozwiązania, usunięcie ciągłego przedłużenia, niepusty zwarty K i spójny U; jednostronne ograniczenie w Liouville'u — poprawne.
- Pochodne: lokalne oszacowanie, możliwość nieskończonego supremum, gładkość z Weyla i iteracja — poprawne.
- Subharmoniczność: rzeczywiste C², nierówności średniej, rozróżnienie dystrybucji i dowolnego reprezentanta, globalne ekstremum — poprawne.
- Caccioppoli: jednorodny operator, lokalne H¹, test zwarto nośny, dowolne k, rzeczywiste eta, stała 4Lambda²/lambda²; brak wniosku o Harnacku z samego oszacowania — poprawne.
- Green: istnienie poprawki jako założenie, d>=2, jednoznaczność poza biegunem, symetria kuli, normalna i reprezentacja istniejącego rozwiązania C¹ na domknięciu — poprawne.

Czwarta lektura 64/64, zero zmian źródła (238–243), kontrola 244 bez nowych usterek. Dedykowane CI 45772524151 ponownie odczytane: oba zadania success. Kontrola strukturalna 74/74 odsyłaczy i przegląd 16 stron PDF w 237 i 243. Nie powtarzano kompilacji. Globalne CI niepotwierdzone, najnowszy przebieg 45778195583 queued, brak zakończonych przebiegów aplikacji w ostatnim odczycie 100 przebiegów.

Odbiór matematyczny i dedykowany techniczny RRC 14 zakończone; globalny gate otwarty. Rozdział 15: blob dc6a563828084666ec50b3ba0c0ee6136cf84019, 584 wiersze, 7 sekcji. Następna iteracja: inwentaryzacja kryteriów i pierwsza szczegółowa lektura RRC 15, bez oznaczania globalnego gate jako PASS.
