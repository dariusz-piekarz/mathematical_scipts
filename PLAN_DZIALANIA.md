# Aktualny plan i pokrycie przeglądem

Stan: 6 października 2026. Gałąź: `review/rozdzialy-matematyka`.
Książka ma 27 rozdziałów i dodatek. Zmiany autora do `19fa283` porównano
z `66b220f`; pobranie aktualizacji przed obecną iteracją nie przyniosło
nowych zmian. Uzasadnienia i wyniki kontroli: [PRZEGLAD.md](PRZEGLAD.md).
Obsługa projektu: [README.md](README.md).

**To jedyna aktualna lista zadań.** Dawne „zakończono” w dzienniku dotyczy
wskazanej tam wersji. Dodanie treści przez autora nie oznacza zakończenia
jej niezależnego przeglądu. Jedna iteracja matematyczna obejmuje jeden rozdział.

## Uzgodniony zakres

- Sprawdzić niezweryfikowane dodatki: matematykę, luki w dowodach,
  polską terminologię, rysunki i powiązania między rozdziałami.
- Uzupełniać potrzebne przejścia i rozwijać materiał tam, gdzie ma to
  uzasadnienie, zwłaszcza w końcowych rozdziałach. Nie dublować już
  wprowadzonych definicji brzegu, grupy wolnej ani iloczynu wolnego.
- Źródła są podzielone na rozdziały; zachować wspólne etykiety i jeden PDF.
  Podział `9148128` sprawdzono przez identyczność rozwiniętego źródła
  oraz tekstu, linków i obrazu wszystkich 384 stron przed/po podziale.
- Prowadzić log uzasadnień, kompilować całość i indeks, obejrzeć zmienione
  strony, następnie commitować i pushować każdą zakończoną iterację.
- Nie dodawać zadań. Teoria Freedmana, egzotyczne R⁴ i dalsze metody
  czterowymiarowe pozostają przeznaczone do osobnego skryptu.
  Istniejący rozdział o siedmiowymiarowych sferach Milnora pozostaje tutaj.

## Kolejka audytu

| Zakres | Stan | Następna kontrola |
|---|---|---|
| Podział źródeł i importy | Zakończono, `9148128` | Kontrola regresji przy dalszych zmianach |
| 1. Rozmaitości | Nowe dodatki sprawdzone, `aa6c59a` | Brzeg i pełna przestrzeń styczna mają uzupełniony dowód |
| 5. Algebra abstrakcyjna | Audyt zakończony 6 października; PDF 387 stron | Uzupełnione dowody, sprawdzony graf słów, indeks i odsyłacze |
| 2. Pola wektorowe | Audyt dodatków zakończony 6 października; PDF 387 stron | Sprawdzone powiązanie z brzegiem, przykład przepływu jednostronnego, bibliografia i rysunki |
| 3. Algebra tensorowa | Audyt dodatków zakończony 6 października; treść bez poprawek | Poprawny odsyłacz do rozdziału 5, indeks, źródła i ilustracje |
| 4 oraz 6–19 | Dawna treść przeszła audyt; różnice po rozbudowie zinwentaryzowano | Przejrzeć różnice rozdziałami, zaczynając od rozdziału 4 |
| 20. h-kobordyzm | Oczekuje | Hipotezy wymiarowe, dyski Whitneya, realizacja ruchów uchwytów |
| 21. Torsja i s-kobordyzm | Oczekuje | Bazy, strona działania pierścienia, konwencje torsji |
| 22. Chirurgia geometryczna | Oczekuje | Obramowania, zmiany homotopii i homologii, rysunki |
| 23. Przeszkoda chirurgiczna | Oczekuje | Formy i dekoracje grup L, zakres twierdzenia Walla |
| 24. Ciąg chirurgii | Oczekuje | Normalne niezmienniki, zbiór struktur, sens dokładności |
| 25. Poincaré | Oczekuje | Wymiar 2, osobno 5 i wyższe; homeomorfizm a dyfeomorfizm |
| 26. Sfery Milnora | Oczekuje | Sklejenie wiązek, klasy charakterystyczne, egzotyczność |
| 27. Chern–Weil | Oczekuje | Normalizacje, transgresja, klasa Eulera i wersja brzegowa |
| Dodatek o wynikach zewnętrznych | Oczekuje | Zgodność katalogu zależności z rzeczywistymi dowodami |
| Końcowa kontrola całości | Oczekuje | Mapa książki, oznaczenia, terminologia, bibliografia, indeks i PDF |

Poprzedni audyt obejmował 18 rozdziałów w `a36c920` (325 stron).
Jego tabela pokrycia i commity są zachowane w dzienniku. Po wydzieleniu
algebry abstrakcyjnej dawne rozdziały 5–18 odpowiadają obecnym 6–19,
przy czym część podstaw o modułach przeniesiono do nowego rozdziału 5.
Porównanie źródeł `66b220f` i `19fa283` wykazuje zmiany we wszystkich
tych rozdziałach. W wielu są to wyłącznie wpisy indeksu, ale statusu
„sprawdzono” nie nadano im automatycznie na podstawie liczby zmienionych linii.

## Stan wcześniejszych propozycji 1–12

Zachowujemy numery, aby wcześniejsze ustalenia nadal były czytelne.
Ta tabela zastępuje `PROPOZYCJE_UZUPELNIEN.md` i listę `do_zrobienia.md`.

| Nr | Temat | Realizacja i pozostały zakres |
|---|---|---|
| 1 | Rozmaitości z brzegiem | Autor dodał definicję, niezależność od map i przykłady w rozdziale 1; nasz audyt uzupełnił przestrzeń styczną. Powiązania z orientacją, transwersalnością, kołnierzem i narożami do kontroli w dalszych rozdziałach. |
| 2 | Grupy i prezentacje | Są w rozdziale 5: ilorazy, domknięcie normalne, grupa wolna, iloczyn wolny i prezentacja torusa. Postać normalną sprawdzono i uzupełniono w `23483ad`; zastosowanie van Kampena będzie sprawdzone w rozdziale 7. |
| 3 | Redakcja i nawigacja | Jest mapa książki, spis oznaczeń, indeks i rozdzielone źródła. Pozostaje ujednolicenie stylu rozdziału 1 i zakończeń rozdziałów oraz precyzji lektur: autor, tytuł, sekcja i link. Zachować rozbudowane przykłady. |
| 4 | Zadania z rozwiązaniami | Nie realizować w obecnym zakresie. Dawna propozycja rachunków, kontrprzykładów i wspólnych przykładów (sfera, torus, przestrzenie rzutowe, Möbius) pozostaje odłożona. |
| 5 | Wyniki zewnętrzne i samowystarczalność | Jest dodatek. Sprawdzić hipotezy i odsyłacze, w tym Brouwera, funkcję odwrotną, triangulację i przeszkodę spinową. Pełna triangulacja oraz porównanie kohomologii Čech i singularnej są osobnymi możliwymi rozszerzeniami, nie krótkimi poprawkami. |
| 6 | Chern–Weil i Chern–Gauss–Bonnet | Jest rozdział 27. Sprawdzić wielomiany niezmiennicze, niezależność od koneksji, identyfikację formy Eulera z klasą topologiczną i jawne określenie formy brzegowej. |
| 7 | h-kobordyzm Smale'a | Jest rozdział 20. Sprawdzić wymiar W≥6, spójność, obramowania dysków Whitneya, skrajne indeksy i redukcję uchwytów do iloczynu z ustalonym dolnym końcem. |
| 8 | Torsja Whiteheada i s-kobordyzm | Jest rozdział 21. Sprawdzić Z[π₁], bazowane kompleksy nakrycia, prostą równoważność i przeszkodę do iloczynu. Nie utożsamiać torsji Whiteheada z trikiem Whitneya. |
| 9 | Chirurgia i jej przeszkody | Są rozdziały 22–24, szerzej niż pierwotnie proponowano. Audyt obejmie wpływ operacji na π₁, homologię i formę przecięcia, obramowania, zabijanie klas, Walla i ciąg dokładny. |
| 10 | Poincaré | Jest rozdział 25. Dla n=2 sprawdzić użycie klasyfikacji powierzchni; dla n>5 usunięcie dysków, h-kobordyzm i sklejenie; n=5 wymaga osobnego argumentu. Nie zamieniać homeomorfizmu w dyfeomorfizm. Wymiar 4 poza tym skryptem. |
| 11 | Sfery Milnora | Jest rozdział 26: wiązki S³ nad S⁴, rachunki i niezmiennik egzotyczności. Sprawdzić użycie klas Pontriagina i sygnatury. Dalsze grupy sfer homotopijnych pozostają możliwym rozszerzeniem. |
| 12 | Egzotyczne R⁴ | Osobny skrypt autora: topologia końców, uchwyty Cassona, Freedman i Donaldson. Nie wynika to z samego niepowodzenia triku Whitneya ani z konstrukcji sfer Milnora. |

## Pomysły pozostawione do wyboru po audycie

1. **Hodge i Bochner–Weitzenböck:** połączyć formy i krzywiznę Ricciego
   z ograniczeniami topologicznymi, z jawnymi założeniami analizy eliptycznej.
2. **Holonomia i rozkład de Rhama:** rozwinąć transport równoległy
   i kryteria lokalnego oraz globalnego rozkładu metryki na produkt.
3. **Geometria podrozmaitości:** równania Gaussa–Codazziego, krzywizna średnia
   i pierwsze przykłady powierzchni minimalnych, na bazie drugiej formy podstawowej.
4. **Dłuższe zależności i rozszerzenia:** triangulacja, porównanie Čech–singularna
   oraz grupy sfer homotopijnych — zakres do ustalenia po sprawdzeniu dodatku
   i rozdziału Milnora. Nie oznaczać ich jako już wykonanych.

Po audycie zaktualizować tę krótką listę na podstawie faktycznych braków
i przedstawić ją użytkownikowi. Pierwszeństwo mają naprawy obecnego materiału.

## Źródła zachowane z wcześniejszych propozycji

- [Morgan: znoszenie uchwytów i h-kobordyzm](https://www.math.columbia.edu/~jmorgan/Lecture_IIIA_hcobordism_Contd.pdf).
- [Ranicki: chirurgia algebraiczna i geometryczna](https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf).
- [Milnor: omówienie Poincarégo dla Clay](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf).
- [Milnor: oryginalna konstrukcja egzotycznej sfery](https://sites.math.rutgers.edu/~feehan/teaching/math866/milnor7sphere.pdf).
- [Gompf: egzotyczne R⁴](https://arxiv.org/abs/1705.06644).
- [Clay: program topologii niskich wymiarów](https://www.claymath.org/events/recent-advances-in-low-dimensional-topology/)
  — źródło wcześniejszego sprawdzenia statusu gładkiego problemu Poincarégo
  w wymiarze 4; nie planować dopisywania jego dowodu.
