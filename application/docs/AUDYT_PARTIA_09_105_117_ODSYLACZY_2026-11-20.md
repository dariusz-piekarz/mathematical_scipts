# Audyt matematyczny odsyłaczy — partia IX (wystąpienia 105–117)

Data: 20.11.2026. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Metoda i zakres

Pozycje 105–117 (indeksowanie od 1) pochodzą z niezmiennej kolejności `unresolved_references` w `reference_provenance_audit_355.json`, zbudowanym na 355 rozdziałach. Odczytano fragmenty kanonicznych źródeł cytujących i deklaracje kandydatów, z uwzględnieniem lokalnych hipotez twierdzeń. Żaden plik `chapters/pl/` nie został zmieniony; zachowano oryginalne `\label`, `\ref`, `\eqref`. To audyt semantyczny, NIE naprawa etykiet ani scalanie książek.

## Zestawienie wszystkich 13 wystąpień

| Lp. | Cytujące miejsce | Etykieta | Status indeksu | Rekomendacja |
|---:|---|---|---|---|
| 105 | `DG-17:74` | `ch:algebra-homologiczna` | wielu właścicieli | `DG-06` |
| 106 | `DG-17:230` | `ch:formy-de-rham` | wielu właścicieli | `DG-10` |
| 107 | `DG-17:325` | `prop:lokalna-homologia` | wielu właścicieli | `DG-08` |
| 108 | `DG-17:421` | `ch:homologia-przestrzeni` | wielu właścicieli | `DG-08` |
| 109 | `DG-17:733` | `prz:hodge-dwie-sfery-18` | brak | `BRAK` |
| 110 | `DG-17:1840` | `ch:chern-weil` | brak | `BRAK` |
| 111 | `DG-17:1888` | `thm:CGB-boundary-26` | brak | `BRAK` |
| 112 | `DG-17:2182` | `thm:CGB-boundary-26` | brak | `BRAK` |
| 113 | `DG-18:726` | `ch:homologia-przestrzeni` | wielu właścicieli | `DG-08` |
| 114 | `DG-18:892` | `ch:homologia-przestrzeni` | wielu właścicieli | `DG-08` |
| 115 | `DG-18:2392` | `def:chirurgia-zarys-16` | wielu właścicieli | `DG-17` |
| 116 | `DG-19:270` | `def:chirurgia-zarys-16` | wielu właścicieli | `DG-17` |
| 117 | `DG-20:1202` | `cor:whitehead-homologiczny` | wielu właścicieli | `DG-09` |

## Ustalenia szczegółowe

### 105. DG-17:74 — `ch:algebra-homologiczna`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: DG-06:2, TOP-03:2.
- Wynik: Rozdział DG-17 używa ciągu Ext i zmian współczynników; DG-06 jest wcześniejszym rozdziałem tego samego skryptu. Oznaczyć jako lokalną propozycję właściciela, bez zmiany etykiety.

### 106. DG-17:230 — `ch:formy-de-rham`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: DG-10:2, TOP-09:2.
- Wynik: Iloczyn zewnętrzny form porównywany z iloczynem kubkowym; DG-10 zawiera teorię form w tym samym skrypcie.

### 107. DG-17:325 — `prop:lokalna-homologia`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: DG-08:2255, TOP-05:1597.
- Wynik: Definicja lokalnej klasy orientacji korzysta z H_n(M,M\setminus\{p\}; Z)=Z dla rozmaitości bez brzegu; DG-08:2255 stwierdza dokładnie tę tezę. Zachować ograniczenie bez brzegu w miejscu użycia.

### 108. DG-17:421 — `ch:homologia-przestrzeni`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: DG-08:2, TOP-05:2.
- Wynik: Zgodność homologii symplicjalnej i singularnej w triangulacji DG-08; poza skończonymi triangulacjami wymaga kontroli przejścia do lokalnie skończonych.

### 109. DG-17:733 — `prz:hodge-dwie-sfery-18`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: nie ma.
- Wynik: W DG-17:733 zapowiedziano obliczenie okresów form na S²×S² w przykładzie hodge-dwie-sfery-18. Brak etykiety; skontrolować czy istnieje w innym pliku Biblioteki i wtedy przenieść pełny fragment z jego etykietą lub przygotować dowód, nie zastępować inną etykietą.

### 110. DG-17:1840 — `ch:chern-weil`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: nie ma.
- Wynik: DG-17:1840 stwierdza, że pełny rachunek klas Chern/Pontriagin omówiono w rozdziale ch:chern-weil. Ten cel nie figuruje w aktualnym indeksie; nie wolno traktować zapowiedzi jako dostępnego dowodu.

### 111. DG-17:1888 — `thm:CGB-boundary-26`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: nie ma.
- Wynik: DG-17:1888: TS² i liczba Eulera 2. Cytowany brakujący wynik CGB-boundary-26 dotyczy brzegu; sfera jest bez brzegu. Istniejący wynik DG-14:4603 thm:chern-gauss-bonnet ma właściwe hipotezy; wymaga świadomej korekty – nie nadpisywać źródłowej etykiety.

### 112. DG-17:2182 — `thm:CGB-boundary-26`

- Dowód źródłowy: `pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`; SHA-256: `cae7e6bff59a8b23052b9ccf9b3defcd7fd3837615a516ad721cf4f29a30992d`.
- Kandydaci z indeksu: nie ma.
- Wynik: DG-17:2182: samoprzecięcie przekątnej w S²×S² i e(TS²)=2. Analogicznie, ścisła podstawa to thm:chern-gauss-bonnet (DG-14), nie niedostępny wynik z poprawką brzegową; niezależny rachunek homologiczny A+B jest w DG-17:2185–2189.

### 113. DG-18:726 — `ch:homologia-przestrzeni`

- Dowód źródłowy: `pl/differential_geometry_and_topology/18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex`; SHA-256: `47537879270c3a6d5bddb7860f32b00e50d89c98e57d422017d4fbc1c8c03830`.
- Kandydaci z indeksu: DG-08:2, TOP-05:2.
- Wynik: W nierównościach Morse’a DG-18:726 odwołanie do kompleksu komórkowego; DG-08 w tym samym skrypcie.

### 114. DG-18:892 — `ch:homologia-przestrzeni`

- Dowód źródłowy: `pl/differential_geometry_and_topology/18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex`; SHA-256: `47537879270c3a6d5bddb7860f32b00e50d89c98e57d422017d4fbc1c8c03830`.
- Kandydaci z indeksu: DG-08:2, TOP-05:2.
- Wynik: W przykładzie Morse’a DG-18:892 dotyczy torsji homologii; DG-08 szczegółowo omawia np. H_1(RP²;Z)=Z/2.

### 115. DG-18:2392 — `def:chirurgia-zarys-16`

- Dowód źródłowy: `pl/differential_geometry_and_topology/18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex`; SHA-256: `47537879270c3a6d5bddb7860f32b00e50d89c98e57d422017d4fbc1c8c03830`.
- Kandydaci z indeksu: DG-17:2675, TOP-11:2553.
- Wynik: DG-18:2392 operacja chirurgii na poziomicach; DG-17:2675 jawnie określa indeks jako wymiar operowanej sfery k, uchwyt śladu ma indeks k+1; zgodne z lambda-1 i lambda.

### 116. DG-19:270 — `def:chirurgia-zarys-16`

- Dowód źródłowy: `pl/differential_geometry_and_topology/19-kobordyzmy-i-rachunek-uchwytow.tex`; SHA-256: `37862b0742f4600e351dcc19d0f984f07ce025847e53d96b0ebfcd8eb20c1c21`.
- Kandydaci z indeksu: DG-17:2675, TOP-11:2553.
- Wynik: DG-19:270 przejście z uchwytu do chirurgii w brzegu; DG-17:2675 jest właściwą definicją indeksu k.

### 117. DG-20:1202 — `cor:whitehead-homologiczny`

- Dowód źródłowy: `pl/differential_geometry_and_topology/20-twierdzenie-smale-a-o-h-kobordyzmie.tex`; SHA-256: `b097f26abf41691e09a72ecf2298d0cb79c872dd06a160ab1fa21cf707820d0d`.
- Kandydaci z indeksu: DG-09:2191, TOP-06:1760.
- Wynik: DG-20:1202 korzysta z homologicznego kryterium Whiteheada. DG-09:2191 wymaga jednospójnych CW; DG-20:1167–1172 dowodzi pi1(W)=0, a S^(n-1) ma pi1=0 dla n>=6. Zatem przesłanka spełniona; brak luki w samym cytowaniu.

## Blokery i kontrole matematyczne

1. `prz:hodge-dwie-sfery-18` — brak etykiety, a DG-17:733 odwołuje się do szczegółowego rachunku na S²×S². Zweryfikować, czy istnieje pełne opracowanie w innych zasobach Biblioteki. Nie zastępować domniemaniem.
2. `ch:chern-weil` — brakuje zapowiedzianego rozdziału o klasach charakterystycznych; bez niego cytowania stanowią zależności otwarte. Nie wolno deklarować pełnego dowodu Chern–Gauss–Bonneta wyłącznie z obecnych odsyłaczy.
3. `thm:CGB-boundary-26` — dwa wystąpienia (111, 112). Dla TS² poprawną podstawą jest wersja bez brzegu `DG-14:4603` (`thm:chern-gauss-bonnet`) wraz z identyfikacją charakterystyki i liczby Eulera; sam cytat do wersji brzegowej jest nieadekwatny. W `DG-17:2185–2189` jest ponadto drugi, niezależny rachunek przez klasy A+B.
4. `DG-17:325` — przy lokalnej homologii nie pomijać warunku, że punkt rozmaitości leży we wnętrzu (DG-08:2255 zakłada brak brzegu).
5. `DG-20:1202` — kryterium Whiteheada wymaga jednospójności; została ona sprawdzona dla W w DG-20:1167–1172, a dla S^(n-1) wynika z n≥6. Dlatego sam odsyłacz ma prawidłowe hipotezy.

## Bilans i dalsza kolejność

- 13 wystąpień: **9 niejednoznacznych** (9 uzasadnionych właścicieli w tym samym skrypcie) oraz **4 bez etykiety docelowej** (3 różne nazwy: `prz:hodge-dwie-sfery-18`, `ch:chern-weil`, `thm:CGB-boundary-26`).
- Łącznie przejrzano **117/257** wystąpień; **140** pozostało. Liczba fizycznie naprawionych odsyłaczy nie wzrosła.
- Następna partia: 118–130 w tym samym niezmienionym indeksie; osobno audyt brakujących dowodów Hodge/Chern–Weil i kontrola twierdzenia o samoprzecięciu.
- Obowiązuje zasada: kopiować wszystkie oryginalne etykiety i odsyłacze z materiałem, rozstrzygać konflikty jawnie, bez utraty pochodzenia; scalenia całych dziedzin dopiero po ich skompletowaniu.