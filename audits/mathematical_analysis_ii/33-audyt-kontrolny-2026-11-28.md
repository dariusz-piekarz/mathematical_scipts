# AM II 33 — audyt kontrolny

Data: 2026-11-28. Sprawdzone źródło: commit e67a41d501666662ee8f13a9e3468979edae5b97, blob db556632a675583ac31a0c8725cf4bfc5ffc0d77 (849 wierszy treści). Uzupełnienie w commit 515438b0e86ef5d910f1543cebf56d046677bb43.

## Kontrola merytoryczna
- Wzór na pole: lokalne dwustronne porównanie Lipschitzowskie, dodatni jakobian, borelowskość obrazów, rozłączność podziału, przypadek nieskończonej całki. Wzór ważony przez zbieżność monotoniczną i rozkład na części.
- Miara na podrozmaitości: zgodność z AM2-23 (Gram i orientacja) oraz AM2-30 (zamiana zmiennych); przypadek k=1 zgodny z AM2-31. Całka skalarna nie zależy od orientacji.
- Brzeg: lokalne przedłużenia C^1, zerowość miary H^k brzegu, borelowskość części wewnętrznej i brzegowej; dodany wniosek o lokalnej skończoności obejmuje punkty brzegu. Wybór zwartej półkuli parametrów, ograniczenie jakobianu, skończone pokrycie zbioru zwartego i przeliczalne pokrycie M są poprawne.
- Przykłady: paraboloida, płaszczyzna w R^4, sfera, czasza, środek masy półsfery, torus, Pappus–Guldin; prawidłowe jakobiany, wymiary i wartości.
- Immersja: krotność jest sumą funkcji charakterystycznych borelowskich obrazów rozłącznego podziału dziedziny; wyjątek walca ma miarę zero.
- Współrzędne radialne: regularność sfery, ortogonalność kolumn, czynnik r^(n-1), Tonelli i zbieżność monotoniczna, osobno funkcje ze znakiem. Rekurencja objętości i momenty hipersfery poprawne.

## Kontrole statyczne
24 różne etykiety, 40 odsyłaczy wewnętrznych i 5 zewnętrznych. W poprzednim przebiegu dla identycznego blobu wszystkie cele sprawdzono w odpowiednich rozdziałach AM II i ME 26, 28. Nie wykryto duplikatów w kontrolowanych plikach. Stos środowisk LaTeX poprawny. Obie wizualizacje Plotly mają implementację w am2-figures.js; nie przeprowadzono testu renderowania.

## Odbiór techniczny
Terminologia dla 515438b: success (46172115258). Walidacja AM II (46172115173) nadal in_progress w chwili kontroli. Testy aplikacji (46172115175) cancelled. Nie potwierdzono aktualnej kompilacji PDF.

Wynik: zero nowych uwag merytorycznych i statycznych, bez zmian źródła. Zamknięcie merytoryczne AM2-33; odbiór techniczny PDF pozostaje otwarty. Kolejny etap: AM2-34 — formy różniczkowe, orientacja i całkowanie form, przed ogólnym twierdzeniem Stokesa (AM2-35). 
