# AM II — globalny audyt integralności, etap 1

Data: 2026-11-28. Migawka źródła: eae6d052a1dba222af68ef76a367d641f362474e.

Książka, katalog books.json i plan strukturalny: 38 identycznie uporządkowanych rozdziałów, 6 części, pending puste. Pierwszy przebieg statyczny w trzech partiach (12+13+13 rozdziałów): 33 531 wierszy, 831 wystąpień etykiet, 1158 odsyłaczy ref/eqref/pageref, 176 odsyłaczy atlasref. Brak niezgodności stosu środowisk i powtórzonych etykiet wewnątrz każdej partii. Pełne porównanie etykiet i celów między partiami i tomami pozostaje do następnego etapu.

PDF z przebiegu 46180896039 (commit feaf7834257d9377f5e248a8fe8f8b8d55fe60b3): 369 stron, 3 487 867 bajtów; raport czytnika 80/80 rysunków PASS. To starsza wersja AM2-38 kończąca się alternansem. W logu 11 ostrzeżeń hyperref dotyczących czterech tytułów sekcji AM2-24, 26, 33 oraz 1 overfull hbox (8,73416 pt) w AM2-30. Naprawiono tytuły przez texorpdfstring i przeniesiono wzór definiujący funkcję charakterystyczną w przykładzie AM2-30 do osobnego wiersza matematycznego. Etykiety i cele odsyłaczy pozostawiono bez zmian. Skuteczność zmian w aktualnej kompilacji wymaga potwierdzenia.

Następny etap: pełna walidacja odsyłaczy i duplikatów między partiami, weryfikacja atlasref oraz zależności dydaktycznych, odbiór końcowego PDF.
