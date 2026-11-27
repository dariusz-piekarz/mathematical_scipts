# RRC 15 — iteracja 266: kontrola przed odbiorem technicznym

Źródło: b4952ce41cfeb61edb446c84bd59948940bed4f6, 1457 wierszy, bez zmian. Trzecia lektura 259–265: 64/64, bez nowych usterek na tym samym blobie.

Ponowna kontrola strukturalna i zależności: osiem sekcji, dziewięć środowisk dowodu, 23 etykiety, 76 odsyłaczy do 35 celów, w tym 21 zewnętrznych. Wszystkie cele zewnętrzne znajdują się w RRC 07,09,10,12,13,14. Rozdział jest piętnastym wejściem w książce. Brak własnych środowisk figure, tikzpicture i axis.

Dodano dedykowany workflow .github/workflows/partial-differential-equations-ch15.yml, commit 1ff77ca07429b87cd23dea42e980ba2ebb4712ef, oparty na sprawdzonym mechanizmie rozdziału 14: weryfikacja etykiet, odsyłaczy, środowisk, kolejności wejść i preambuły; kompilacja rozdziałów zależnych z rzeczywistymi licznikami; przeniesienie numerów z aux; kompilacja samodzielnego rozdziału; kontrola logu i renderowanie każdej strony; artefakt pde-ch15-audit. Nie duplikowano odrębnego zadania renderowania figur PDE.

Przebieg 45966233611, zadanie 140395448132, stan queued, potwierdzony przez API check-runs. Nie potwierdzono jeszcze kompilacji, kontroli wizualnej PDF ani pełnego CI. Ponowna kontrola struktury nie jest niezależnym pełnym audytem matematycznym. Następna iteracja: sprawdzić wynik przebiegu, pobrać artefakt po sukcesie, obejrzeć wszystkie strony i domknąć niezależną kontrolę matematyczną przed rozpoczęciem RRC 16.
