# Audyt CXXXII (132) — aproksymacja ścisła BV
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia 63caff486f704cdd9fe919db4a6f041416f6f016, blob 4404368ad1d1065d06e314a73910fe7ce0d407bb. Commit źródłowy d577e8883b5b804f90deaa8247fe0f433133afb1, blob 86f8d53b7090e2e2a2dfc03d6486575d2e2cd4fc.
## Wyniki
Dwa zasadnicze zastąpienia, 3248 -> 3376 wierszy, zachowane wszystkie 37 etykiet.
- Jawne wyczerpanie dowolnego otwartego zbioru przez względnie zwarte otwarte zbiory oraz lokalnie skończone pokrycie pierścieniowe. Udowodniono pokrywanie i lokalną skończoność, dobrano podział jedności i dodatnie marginesy powiększenia nośników wewnątrz tego pokrycia.
- Dokładne założenia na jądro, dobór promieni przez dwa oszacowania L^1, kontrola nośników i sumowalność norm wygładzeń. Jawna zbieżność w L^1 z błędem 2^(-j).
- Dystrybucyjna reguła iloczynu dla lokalnych funkcji psi_i*u przedłużonych przez zero. Nie zakłada się, że globalne przedłużenie u przez zero jest BV.
- Rozkład polarny i Tonelli dają kontrolę pierwszej sumy gradientów przez wariację; druga suma jest sumowalna dzięki doborowi promieni. Znoszenie składników u*grad psi_i następuje lokalnie, bez założenia globalnej sumowalności ich norm.
- Uzasadniono przynależność do W^{1,1}, dolną półciągłość wariacji i dokładną granicę całek z gradientu.
- Wyjaśniono różnicę między zbieżnością ścisłą a zbieżnością w normie BV na przykładzie funkcji charakterystycznej przedziału (osobliwość pochodnej atomowej względem pochodnych funkcji gładkich).
## Otwarte
Kolejny audyt: obwody zbiorów nadpoziomicowych funkcji gładkiej, pełny koobszar BV, następnie wersja ważona i teoria prądów. Kompilacja, testy i PDF pozostają do wykonania. Stan 28/31.
