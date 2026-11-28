# Audyt CXII (112) — stabilizacja i regresje
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy bfc126d97265562e8476ba9c7653fac2620b715a. Niezmieniony blob rozdziału 2ab985480236605f769cbc9b09a71ffbeaf906d4.

## Kontrola matematyczna
Nie wprowadzono zmian w tekście rozdziału. Ponownie skontrolowano szczególnie:
- zgodność zastosowania Łuzina z rozdziałem 10: skończona miara zbioru, skończona rodzina rzeczywistych współczynników macierzy, rozdzielona tolerancja i skończone przecięcie zbiorów zwartych;
- konstrukcję maksymalnych kostek diadycznych, granice odległości dla powiększeń, rozłączność wnętrz, odtwarzanie danych afinicznych oraz tożsamości podziału jedności;
- pokrycia zbiorów zerowych: dodatnia średnica także dla singletonów, wybór skali mniejszej od bufora otoczenia Lipschitzowskiego, borelowskie dominanty i zewnętrzna miara wyjątków, przypadek d=0;
- zgodność liniowej tożsamości koobszaru z rachunkiem macierzy Grama oraz przypadkiem n=m.
Nie znaleziono nowej usterki w sprawdzanych argumentach. Nie jest to formalna weryfikacja wszystkich dowodów.

## Regresje
Commit 6cc61b5eb4c62b3c8840c38b7468736db1952815, blob testów 61df8bf05278dc344803e1c3fb66b90e5b87b61a.
Dodano trzy testy z dokładną arytmetyką wymierną: jednowymiarowe maksymalne przedziały diadyczne dla K={0} (dodatnie i ujemne punkty, granice siatki, stałe 19,42,44, rozłączność wnętrz); odtwarzanie danych afinicznych przez wagi i ich pochodne; liniowy koobszar dla nieortogonalnej parametryzacji. Łącznie 10 testów rozdziału, dodatkowo 4 testy integralności tomu.

## CI
Dla commitu CXI c5ca92bdebdf957e1fc683b60ef6b57a0210f4a2 API nie zwróciło przebiegu. Zmiana pliku testowego uruchomiła dedykowany workflow 45352779994, w kolejce w chwili kontroli. Ten przebieg ma sprawdzić dokładnie niezmieniony blob rozdziału CXI. Nie deklaruje się wyniku przed zakończeniem ani nowych oględzin PDF.
## Stan
Pierwszy audyt stabilizacyjny bez zmian źródła rozdziału. Rozdział nadal otwarty do potwierdzenia CI, logów i oględzin aktualnego PDF oraz kolejnej niezależnej kontroli. Stan 27/31. Nie przechodzić do 29.
