# RRC — iteracja 337

## Rozdział 21
Trzeci pełny audyt stabilizacyjny wszystkich dziesięciu sekcji. Odczytano 1681 wierszy. Commit zmian 611d97037f38f57fa0977c229b8dfaf81cad9224, blob f335249a4d2942aee142b22f4ff4ad92a30f7377.

Nie wykryto nowego błędu w zasadniczych dowodach istnienia, silnej ciągłości, bilansu i propagacji. Wprowadzono doprecyzowania:
- Konwencja unitarna Fouriera przed pierwszym użyciem, norma macierzowa W^{k,∞}, dokładna formuła kwadratu normy H^{-1} przez reprezentanta Riesza.
- Identyfikacja pochodnej Bochnera przez testy iloczynowe i gęstość, jawna kontrakcyjność splotu i zbieżność aproksymacji jedynki, doprecyzowanie wyjątkowych chwil w komutatorze.
- Weryfikacja nowego wniosku o ciągłości w H^s i oszacowaniu bez dodatkowej pochodnej. Określono stałą M w oszacowaniu H^s. Sprawdzono zanurzenie Fouriera dla każdego rzędu pochodnej do l oraz istnienie wspólnie ciągłych reprezentantów współczynników i wymuszenia.
- Uściślono interpretację miary powierzchniowej, nazwę twierdzenia o danych wchodzących na półprostej i oznaczenie iloczynu skalarnego.

Kontrola źródła: 1726 wierszy, 23 zachowane unikatowe etykiety, 64 odsyłacze, trzy różne cele zewnętrzne (5,20); wszystkie jednoznaczne, brak błędów zagnieżdżenia i delimiterów. Dedykowane CI 46001394711 queued. Odbiór techniczny i wizualny nadal otwarty.

## Rozdział 20
Run 45994503573 zakończony failure w kroku samodzielnej kompilacji, po zaliczeniu kontroli i kompilacji zależności oraz przeniesieniu numerów odsyłaczy. Log jobu 140490378733 wskazuje undefined control sequence w wierszu 35, makro Q. Poprawiono jedyne wystąpienie na standardowe mathbb{Q}, bez zmiany dowodów. Commit 3ae49e3f813ea2e1a02a29979c28ebd04a5d9a33, blob bc3284ac89b2df80844d2fddb016b28c3e5668b4. Nowe runy przy odczycie: [{"name":"PDE - chapter 21 audit","id":46001463740,"status":"queued","conclusion":null},{"name":"PDE - chapter 20 audit","id":46001463968,"status":"queued","conclusion":null}]. Nie deklaruje się zaliczenia kompilacji.

Następny etap: kontrola stabilizacyjna ostatnich zmian rozdziału 21; przy braku nowych usterek pełna lektura końcowa. Śledzić dedykowane CI 20–21 i nie deklarować odbioru technicznego przed sukcesem i kontrolą PDF.
