# Aktualny plan i pokrycie przeglądem

Stan: 9 października 2026. Gałąź: `review/rozdzialy-matematyka`.
Przed bieżącą pracą pobrano bez konfliktów 12 commitów autora
`b912682`–`386ecb6`, od wcześniejszego wspólnego stanu `34e683b`.
Książka ma **38 rozdziałów, pięć części i trzy dodatki**. Numery w nazwach
plików są historyczne; numer w PDF ustala kolejność importów.

To jedyna bieżąca lista zadań i propozycji. Uzasadnienia zmian oraz wyniki
sprawdzania konkretnych wersji są w [PRZEGLAD.md](PRZEGLAD.md), a budowanie
i organizacja plików w [README.md](README.md). Dawnych planów wykonania
rozdziałów nie powtarzamy obok tabeli ich obecnego stanu. Historia wcześniejszych
propozycji jest w Git oraz w dzienniku.

## Bieżący zakres i kolejność

1. Prośba ze zrzutu z 9 października: rozdział 5 oraz jednolita notacja
   generatorów tensoru i terminologia w pozostałych wskazanych miejscach.
   Ten etap obejmuje też rejestr pojęć użytych bez dostatecznego objaśnienia.
2. Dalej audyt ponad rozdziałem 20, zaczynając od rozpoczętego h-kobordyzmu
   (obecny rozdział 24, plik `20-h-kobordyzm.tex`), następnie torsja
   i s-kobordyzm oraz Poincaré. Kolejne iteracje obejmują po jednym rozdziale.
3. Sprawdzić również niezweryfikowane nowe rozdziały o geometrii globalnej,
   potoku Ricciego, wymiarze 3 i wymiarze 4 oraz dodatki według tabeli.
   Materiał o wiązkach zapowiedziany przez autora trzeba najpierw pobrać
   i porównać; zapowiedź nie jest potwierdzeniem obecności nowego commitu.
4. Przed każdą iteracją i publikacją pobierać zmiany. Prowadzić log,
   kompilować cały dokument i indeks, kontrolować odsyłacze oraz zmienione
   strony, aktualizować wspólny PDF, commitować i pushować ukończony etap.

Nie dodajemy zadań. Rozmaitości z brzegiem, grupy wolne, iloczyny wolne,
geometria Kleina i geometrie Thurstona już są w źródłach; nie tworzymy ich
duplikatów. Freedman, Donaldson i egzotyczne R⁴ pozostają w tym samym PDF,
w osobnych rozdziałach, zgodnie z nowszym ustaleniem z 6 października.

## Pokrycie audytem

Wpisy o sprawdzeniu pochodzą z dziennika wskazanych iteracji. Deklaracje
współautora (w szczególności o chirurgii, sferach Milnora, wymiarze 4
i dodatku C) są zachowane, ale pobranie commitów **nie jest ponownym
niezależnym audytem**. Zmiany po dacie danego przeglądu wymagają kontroli
różnic. Dawne liczby stron dotyczą wyłącznie historycznych składów.
Poprzedni audyt 18-rozdziałowej wersji `a36c920` nie zastępuje tej tabeli.

| Numer i temat | Plik w `tex/rozdzialy/` | Stan przeglądu | Kontrola / pozostały zakres |
|---|---|---|---|
| 1. Rozmaitości | `01-rozmaitosci.tex` | Dodatki sprawdzone; 7 października dołączono i skontrolowano robocze rozwinięcie identyfikacji przestrzeni stycznych; autor dopisał liniowość $\Phi$ i dwa rysunki funkcji odcinającej | Nowe zmiany autora uwzględniono w składzie; nie stanowią pełnego ponownego audytu rozdziału |
| 2. Pola wektorowe | `02-pola-wektorowe.tex` | Audyt dodatków zakończony 6 października; PDF 387 stron | Sprawdzone powiązanie z brzegiem, przykład przepływu jednostronnego, bibliografia i rysunki |
| 3. Algebra tensorowa | `03-algebra-tensorowa.tex` | Audyt z 6 października; notacja poprawiona 9 października | Formalne generatory par zapisano jako [(v,w)]; zakres tej poprawki nie obejmuje ponownego audytu całego rozdziału. |
| 4. Grassmanniany, Clifford i spinory | `04-grassmanniany-clifford-spinory.tex` | Wcześniejszy audyt z 6 października; 8 października dodano grupę Pin | Sprawdzono nakrycie $\operatorname{Pin}(n)\to O(n)$ i stronę 100 PDF |
| 5. Algebra abstrakcyjna | `05-algebra-abstrakcyjna.tex` | Audyt aktualnej treści i poprawki 9 października | Ujednolicono §5.1; dodano dziedzinę i ciało ułamków, wyjaśniono lokalizację i skalary; sprawdzono ilorazy, tensor i rangę. Opcjonalne definicje są w rejestrze poniżej. |
| 6. Algebra homologiczna | `06-algebra-homologiczna.tex` | Audyt dodatków zakończony 6 października; PDF 387 stron | Zachowana kompletność po przeniesieniu, przywrócone założenie o R i związek redukcji modulo m z tensorem |
| 7. Homotopia, nakrycia i CW | `07-homotopia-nakrycia-cw.tex` | Wcześniejszy audyt z 6 października; 8 października dodano minimalną teorię grafów | Drzewo, las, korzeń, liść i rachunek krawędzi sprawdzone na stronie 151 PDF |
| 8. Homologia przestrzeni | `08-homologia.tex` | Audyt dodatków zakończony 6 października; treść bez poprawek | Sprawdzone pięć wpisów indeksu, definicje, bibliografia i trzy ilustracje; PDF 397 stron |
| 9. Wyższe grupy homotopii | `09-wyzsze-grupy-homotopii.tex` | Audyt dodatków zakończony 6 października; PDF 397 stron | Sprawdzone indeks, definicje i cztery rysunki; poprawiono 19 użyć słowa „mapa” na „odwzorowanie” |
| 10. Formy i de Rham | `10-formy-de-rham.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Siedem wpisów indeksu, pięć ilustracji i zgodność konwencji przy brzegu; PDF 397 stron |
| 11. Metryka, długość i miara | `11-metryka-dlugosc-miara.tex` | Audyt dodatków zakończony 6 października; PDF 397 stron | Sprawdzone definicje i dwie ilustracje; usunięty powtórzony wpis indeksu |
| 12. Koneksje i transport | `12-koneksje.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Cztery wpisy indeksu, definicje i dwa rysunki sprawdzone; PDF 397 stron |
| 13. Geodezyjne i zupełność | `13-geodezyjne.tex` | Audyt dodatków zakończony 6 października; PDF 397 stron | Definicje i dziewięć ilustracji sprawdzone; usunięty powtórzony wpis indeksu |
| 14. Krzywizna | `14-krzywizna.tex` | Audyt dodatków zakończony 6 października; PDF 397 stron | Indeks i trzy zmiany cieniowania sprawdzone; rozwinięto powiązania dowodu Cherna–Gaussa–Bonneta z rozdziałami 17 i 27 |
| 15. Grupy Liego | `29-grupy-liego.tex` | Sprawdzono nakrycie kwaternionowe 7 października; pełny audyt całości czeka | Przykłady, nawias, eksponenta, działanie adjungowane i jawne nakrycie $\mathrm{SU}(2)\to\mathrm{SO}(3)$; później sprawdzić zastosowania w Chernie–Weilu i wymiarze cztery |
| 16. Geometria Kleina (plik 29a) | `29a-geometria-kleina.tex` | Dodano 8 października; niezależny audyt oczekuje | Przestrzenie $G/H$ i modele afiniczny, projektowy, euklidesowy, sferyczny, torusa i dysku Poincarégo |
| 17. Chern–Weil | `27-chern-weil.tex` | Oczekuje | Normalizacje i transgresja; uzasadnić model względnej kohomologii de Rhama przy identyfikacji klasy Eulera, granicę całek wokół zer i wersję brzegową |
| 18. Hodge–Bochner | `28-hodge-bochner.tex` | Sprawdzono kluczowe wzory 7 października; pełny audyt całości czeka | Jawne wejście analityczne; własne dowody wzoru Weitzenböcka, znikania Bochnera i rozkładu sygnatury; sprawdzić zgodność z przyszłą teorią czterowymiarową |
| 19. Sard i transwersalność | `15-sard-transwersalnosc.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Pięć wpisów indeksu, cztery ilustracje i warunki transwersalności przy brzegu sprawdzone; PDF 401 stron |
| 20. Zanurzenia i otoczenia | `16-zanurzenia-otoczenia.tex` | Audyt dodatków zakończony 6 października; PDF 401 stron | Sześć haseł indeksu, cztery ilustracje i kołnierze sprawdzone; poprawiono terminologię odwzorowań oraz zdanie o homotopii do odwzorowania stałego |
| 21. Przecięcia, dualność i klasy | `17-przeciecia-dualnosc-klasy.tex` | Audyt dodatków zakończony 6 października | Sprawdzone indeks, konwencje znaków i cztery ilustracje; ujednolicono terminologię i rozwinięto argument Leraya–Hirscha dla wiązki rzutowej |
| 22. Teoria Morse'a | `18-morse.tex` | Audyt dodatków zakończony 8 października | Sprawdzone definicje i pięć ilustracji; jawne współrzędne krytyczne torusa, dokładne prowadnice podpisów i poprawiona terminologia |
| 23. Kobordyzmy i uchwyty | `19-kobordyzmy-uchwyty.tex` | Audyt dodatków zakończony 8 października; PDF 443 strony | Sprawdzone trzy hasła i pięć ilustracji; przywrócony warunek orientacji w podpisie, jawny opis sklejenia pierścieni i rozwinięty lokalny ruch Whitneya przy zachowanych założeniach o dyskach |
| 24. h-kobordyzm | `20-h-kobordyzm.tex` | Audyt rozpoczęty; niezamknięty | Dokończyć zamianę uchwytów 1 na 3: izotopię okręgu uzasadnić dyskiem i kontrolować obramowanie; wyjaśnić przestawienie uchwytów. Potem lemat o dopełnieniu i dokładne hipotezy ruchu Whitneya. |
| 25. Torsja i s-kobordyzm | `21-torsja-s-kobordyzm.tex` | Oczekuje; nazwa modułu rzutowego poprawiona 9 października | Bazy, strona działania pierścienia i konwencje torsji; sama poprawka nazwy nie zamyka audytu. |
| 26. Chirurgia geometryczna | `22-chirurgia-geometryczna.tex` | Pełny audyt zakończony 8 października; treść bez poprawek | Sprawdzone obramowania, ślad i uchwyt dualny, homologia, $\pi_1$, forma jądra i rysunki |
| 27. Przeszkoda chirurgiczna | `23-przeszkoda-chirurgiczna.tex` | Pełny audyt treści zakończony 7 października; sprawdzono definicje, rachunki znaków i baz, tok dowodu oraz źródła Walla i Milnora | Uściślono dual lewego modułu i wzór dla udoskonalenia kwadratowego; geometryczne lematy Walla i Milnora oraz klasyfikacja grup $L$ pozostają jawnie zewnętrzne Termin „rzutowy” ujednolicono 9 października. |
| 28. Ciąg chirurgii | `24-ciag-chirurgii.tex` | Pełny audyt zakończony 8 października | Uściślono naturę obu strzałek przeszkody i przejście do $s$-kobordyzmu; bijekcja z $[X,G/O]$ i działanie grupy $L$ pozostają jawnymi wynikami Walla |
| 29. Poincaré | `25-poincare.tex` | Oczekuje | Wymiar 2, osobno 5 i wyższe; homeomorfizm a dyfeomorfizm |
| 30. Sfery Milnora | `26-sfery-milnora.tex` | Przegląd konstrukcji, klas charakterystycznych i egzotyczności zakończony 7 października; PDF 442 strony | Rozpisano homologię i niezmiennik; wzór Hirzebrucha pozostaje jawnym wejściem zewnętrznym |
| 31. Potok Ricciego (plik 30) | `30-potok-ricciego.tex` | Sprawdzono równania ewolucyjne i poprawkę DeTurcka 7 października; pełny audyt całości czeka | Ewolucja skalara i pola powierzchni, zasada maksimum, poprawka DeTurcka; istnienie i jednoznaczność PDE pozostają jawnym wejściem analitycznym |
| 32. Poincaré w wymiarze trzy (plik 30a) | `30a-poincare-trzy.tex` | Dodano 8 października; niezależny audyt oczekuje | Dla głębokich twierdzeń Perelmana i Hamiltona zachować jawne hipotezy i źródła; sprawdzić topologiczny wniosek z wygaśnięcia oraz użycie twierdzenia Moise'a |
| 33. Geometrie Thurstona (plik 30b) | `30b-geometrizacja-thurstona.tex` | Dodano 8 października; 9 października kontrola obecności definicji i terminologii | Definicje modelu i rozmaitości geometrycznej istnieją. Pełny audyt ośmiu modeli, rozkładu pierwszego, JSJ i założeń geometryzacji nadal oczekuje. |
| 34. Formy przecięcia i uchwyty w wymiarze cztery (plik 31) | `31-freedman-formy-przeciecia.tex` | Przegląd matematyczny zakończony 7 października w poprzedniej numeracji; PDF 442 strony | Sprawdzono rachunek $E_8$, formę splotu i dwa rysunki; klasyfikacja jest w osobnym rozdziale o etykiecie `ch:freedman-klasyfikacja` |
| 35. Uchwyty Cassona (plik 32) | `32-uchwyty-cassona.tex` | Przegląd i uzupełnienie skutków osadzania dysków zakończone 7 października w poprzedniej numeracji; PDF 442 strony | Geometrycznie dualne sfery w konkluzji mają poprawione źródło Powella--Ray--Teichnera; pełne osadzanie i standardowość uchwytu pozostają zewnętrzne |
| 36. Klasyfikacja Freedmana (plik 33) | `33-freedman-klasyfikacja.tex` | Przegląd i objaśnienie drogi od dysków do klasyfikacji zakończone 7 października w poprzedniej numeracji; PDF 442 strony | Osadzanie sfer, chirurgia i $s$-kobordyzm są wskazane jako dalsze wyniki zewnętrzne; klasyfikacja i niezmiennik Kirby'ego--Siebenmanna pozostają zewnętrzne |
| 37. Donaldson (plik 34) | `34-donaldson.tex` | Dodano jako osobny rozdział; pełny niezależny audyt oczekuje | Sprawdzić konwencję $c_2$ i energii ASD, dokładny zakres diagonalizacji i źródła analityczne; twierdzenie Donaldsona jest jawnie zewnętrzne |
| 38. Egzotyczne $\R^4$ (plik 35) | `35-egzotyczne-r4.tex` | Włączono po Donaldsonie; pełny niezależny audyt oczekuje | Skontrolować trzy wejścia Gompfa, indukcję i różnicę między typami zorientowanymi a niezorientowanymi |
| Podział źródeł i importy | — | Zakończono, `9148128` | Kontrola regresji przy dalszych zmianach |
| Dodatek A o wynikach zewnętrznych | — | Uzupełniany przez autora do 386ecb6; pełny niezależny audyt oczekuje | Zgodność katalogu z rzeczywistymi dowodami, zwłaszcza Walla, geometrii globalnej oraz wymiarów 3 i 4. |
| Dodatek B: homologia singularna i Euler | — | Dodany w `59fd235`; audyt oczekuje | Skończoność, przykłady i wzory Eulera; odsyłacze do homologii oraz przecięć i dualności (obecnie rozdziały 8 i 21). |
| Dodatek C: grupy macierzowe | — | Definicje, algebry i wymiary sprawdzone 8 października; tabela czytelna w PDF | Przy dalszej rozbudowie zachować rozróżnienie wymiaru rzeczywistego i zespolonego oraz $Sp(n)$ od $Sp(2n,\mathbb K)$ |
| Końcowa kontrola całości | — | Oczekuje | Mapa książki, oznaczenia, terminologia, bibliografia, indeks i PDF |

## Rejestr pojęć do decyzji autora

Pierwsza partia z 9 października: lektura rozdziału 5 oraz wskazanych
fragmentów geometrii Kleina i Thurstona, z wyszukaniem wyjaśnień w całym
źródle. To **nie jest jeszcze kompletny audyt słownika wszystkich 38
rozdziałów**. Rejestr uzupełniamy podczas kolejnych przeglądów.
Poniższych opcjonalnych rozszerzeń nie dopisano automatycznie.

| Pojęcie i miejsce | Czego brakuje | Możliwe uzupełnienie |
|---|---|---|
| Monoid — plik 05, między `def:free-groups-5` a `prop:free-reduction-5` | Nazwa występuje raz, bez definicji; przykład słów jest już podany. | Jedno zdanie: łączne działanie z jedynką, bez wymogu odwrotności; odnieść do konkatenacji. |
| Pierścień główny — plik 05, uwaga po `prop:ranga-ilorazu` | Brak definicji i twierdzenia o strukturze. Założenie skończonego generowania poprawiono w bieżącym audycie. | Zdefiniować jako dziedzinę, w której każdy ideał jest główny; podać Z i K[t]. Pełne twierdzenie strukturalne wymaga osobnego dowodu lub jawnego źródła. |
| Indeks podgrupy i „wirtualnie” — plik 30b, przykłady geometrii euklidesowej, hiperbolicznej i Sol | Zdefiniowano warstwy, lecz nie ich liczbę jako indeks ani własność posiadaną przez podgrupę skończonego indeksu. | Definicja indeksu i własności wirtualnej, przykład grupy zawierającej Zⁿ ze skończonym indeksem. |
| Grupa nilpotentna i rozwiązalna — plik 30b, modele Nil i Sol | Nazwy są użyte do porównania grup, bez szeregów centralnego i pochodnego. | Krótki blok algebraiczny z komutatorami; obliczyć te szeregi dla podanych grup zamiast tylko dopisywać nazwy. |
| Uśrednianie po zwartym stabilizatorze — plik 30b, `def:thurston-model` | Podano ideę uzyskania niezmienniczej metryki; nie zdefiniowano miary Haara ani nie wskazano twierdzenia o jej istnieniu. | Podać znormalizowaną miarę Haara jako jawny wynik zewnętrzny i wzór całkowy; sprawdzić dodatnią określoność i niezależność przeniesienia. |
| Ostrzyk hiperboliczny — plik 30b, przykład H³ | Jest informacja o torusowym przekroju, bez modelu metryki końca. | Model ilorazu horokuli i krótki rachunek skończonej objętości; odróżnić torusowy przekrój od całego końca. |
| Wypełnienie Dehna — plik 30b, przykład H³ | Jest odwołanie do twierdzenia, ale bez definicji operacji i nachylenia na torusie. | Opisać doklejenie pełnego torusa i meridian; powiązać z istniejącą chirurgią, a hiperboliczne twierdzenie pozostawić z dokładnym źródłem. |

**Już obecne albo uzupełnione:** grupa wolna i iloczyn wolny mają konstrukcje,
postać normalną i własności uniwersalne w rozdziale 5. Dziedzinę całkowitości,
ciało ułamków i działanie skalarów na lokalizacji uzupełniono 9 października.
Geometria Kleina ma definicję `def:klein-geometria` w pliku 29a oraz przykłady.
Geometria modelowa ma `def:thurston-model` w pliku 30b; zaraz potem zdefiniowano
rozmaitość geometryczną (w przyjętej tam wersji zamkniętej), a dalej podano
osiem modeli i ilorazy. Potrzebny jest audyt ich założeń i wyjaśnień, nie
druga konkurencyjna definicja.

## Dalsze rozszerzenia i granice dowodów

- Holonomia i rozkład de Rhama oraz równania Gaussa–Codazziego pozostają
  propozycjami do decyzji po bieżącym audycie. Hodge–Bochner jest już
  osobnym rozdziałem; nie figuruje ponownie jako temat do napisania.
- Pełne triangulacje, porównanie kohomologii Čecha i singularnej oraz
  dalsze grupy sfer homotopijnych są większymi możliwymi rozszerzeniami,
  nie krótkimi naprawami obecnych dowodów.
- Dawna warunkowa propozycja dowodów Brouwera i niezmienniczości obszaru
  pozostaje odłożona do sprawdzenia homologii lokalnej i potrzebnych
  narzędzi. Nie dopisywać pozornie pełnego dowodu z ukrytym wejściem.
- Głębokie wyniki Walla, Bardena, Hirzebrucha, Perelmana, Freedmana,
  Donaldsona i Gompfa oraz analityczne twierdzenia o PDE pozostają
  jawnymi wejściami z dokładnymi założeniami i źródłami. Kontrola ich
  zastosowania nie jest dowodem tych twierdzeń. W chirurgii sprawdzić
  również realizację obramowanych immersji, prostą dualność i bazowość
  oraz przygotowanie kobordyzmu.
- W egzotycznych R⁴ sprawdzić trzy wejścia Gompfa i przejście od klas
  zorientowanych do niezorientowanych. Wynik DeMichelisa–Freedmana
  o kontinuum klas był dalszą możliwą ścieżką; nie utożsamiać go z już
  dodanym argumentem o nieskończonej rodzinie.

Źródła i szczegółowe deklaracje wykonania zachowuje [PRZEGLAD.md](PRZEGLAD.md)
oraz bibliografia odpowiednich rozdziałów. Po zakończeniu przeglądu przedstawić
użytkownikowi pozostałe propozycje na podstawie rzeczywistych braków.
