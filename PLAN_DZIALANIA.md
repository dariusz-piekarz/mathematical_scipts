# Aktualny plan i pokrycie przeglądem

Stan: 6 października 2026. Gałąź: `review/rozdzialy-matematyka`.
Książka ma 27 rozdziałów i dwa dodatki. Zmiany autora do `19fa283`
porównano z `66b220f`. Pobrano także cztery nowe commity autora
`59fd235`–`46fd90c`; ich dodatkowy zakres kontroli wskazano poniżej.
Uzasadnienia i wyniki kontroli:
[PRZEGLAD.md](PRZEGLAD.md).
Obsługa projektu: [README.md](README.md).

**To jedyna aktualna lista zadań.** Dawne „zakończono” w dzienniku dotyczy
wskazanej tam wersji. Dodanie treści przez autora nie oznacza zakończenia
jej niezależnego przeglądu. W bieżącym audycie zachowujemy uzgodnioną
zasadę: jedna iteracja matematyczna obejmuje jeden rozdział.

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
- Nie dodawać zadań do książki. Istniejący rozdział o siedmiowymiarowych
  sferach Milnora pozostaje w skrypcie; teorię Freedmana i egzotyczne
  $\mathbb R^4$ planować w osobnych rozdziałach tego samego PDF.

Nie dublować tematów już dodanych. Zgodnie z nową prośbą z 6 października
2026 podstawy teorii Freedmana i egzotyczne $\mathbb R^4$ planujemy w tym
samym dokumencie PDF, w osobnych plikach rozdziałów. Istniejący rozdział
o sferach Milnora zachowujemy. Nowe propozycje należy odróżniać od
koniecznych napraw dowodów. Bieżące uzasadnienia zmian: `PRZEGLAD.md`.

## Etap rozbudowy autora — 6 października 2026

Poniższa lista zachowuje plan i deklaracje wykonania przekazane w commitach
autora. Oznaczenia `[x]` dotyczą dodania materiału, nie jego niezależnego
audytu. Bieżąca praca obejmuje najpierw audyt istniejących treści; dalsze
ścieżki rozbudowy pozostają planem. Tabela audytu niżej jest jedyną listą
statusów weryfikacji.

- [x] **0. Dalsza lektura.** Ujednolicić postać sekcji
  `\section*{Dalsza lektura}` we wszystkich rozdziałach według wzorca
  z rozdziału 18; sprawdzić zapisy bibliograficzne i odnośniki.
- [x] **1. Rysunki chirurgii.** Dodać rysunki, które wyjaśniają operację
  chirurgiczną, obramowanie, przecięcia i ruch uchwytów; sprawdzić ich
  geometrię, oznaczenia i widoczność w złożonym PDF.
- [x] **2. Pogłębienie części chirurgicznej i jej zastosowań.** Rozwinąć
  w istniejących plikach rozdziałów 19–26 trik Whitneya, ruchy uchwytów,
  twierdzenie Walla, klasyfikację powierzchni, przypadek wymiaru 5 oraz
  rachunek sygnatury i sfer Milnora. Najpierw ustalić, co już jest
  dowiedzione, a następnie dopisać brakujące lematy i rachunki. Przy
  każdym głębokim wyniku oddzielić własny dowód od jasno nazwanego
  twierdzenia wejściowego; celem jest zmniejszenie liczby takich wejść.
- [x] **3. Dodatek: homologia singularna i cecha Eulera.** Rozwinąć
  przykłady i związki z charakterystyką Eulera, odsyłając do istniejących
  definicji w rozdziale 8 i dualności z rozdziału 17. Nowy tekst umieścić
  w osobnym pliku `tex/dodatki/`, bez powtarzania podstaw teorii.
- [ ] **4. Dodatek: twierdzenia Brouwera.** Dodać dowody twierdzenia
  o punkcie stałym i niezmienniczości obszaru tylko wtedy, gdy audyt
  wcześniejszych rozdziałów potwierdzi wszystkie potrzebne narzędzia.
  Dla pierwszego wyniku sprawdzić retrakcję kuli na sferę i homologię
  sfer; dla drugiego sprawdzić homologię lokalną, dualność i każdy krok
  przejścia od lokalnej homotopii do otwartości obrazu. Jeśli tych
  narzędzi brak, odłożyć oba dowody zamiast podawać ukryte założenia.
- [ ] **5. Hodge–Bochner.** Przygotować i dodać osobny rozdział według
  ścieżki poniżej.
- [ ] **6. Grupy Liego.** Przygotować i dodać osobny rozdział według
  ścieżki poniżej.
- [ ] **7. Wymiar cztery.** Przygotować osobne rozdziały z podstawami
  teorii Freedmana i z dowodem istnienia nieskończenie wielu parami
  nierównoważnych struktur gładkich na $\mathbb R^4$, z jawnym bilansem
  twierdzeń zewnętrznych.
- [ ] **8. Potok Ricciego.** Przygotować osobny rozdział o ewolucji metryki,
  przykładach i pierwszych równaniach ewolucyjnych według ścieżki poniżej.
- [x] **9. Terminologia kiełków.** Ujednolicić tłumaczenie *germ* funkcji
  jako „kiełek funkcji” w rozdziale 1 i zasadach redakcyjnych `AGENTS.md`.

Stan po tej iteracji: punkty 0--3 i 9 wykonano w źródłach rozdziałów,
w dodatku B oraz w zasadach terminologicznych. Klasyfikację powierzchni
dowiedziono teraz w rozdziale 25
przy jawnym wejściu w postaci twierdzenia o triangulacji powierzchni.
W punkcie 2 nadal zewnętrzne pozostają geometryczne lematy Walla,
klasyfikacja Bardena oraz twierdzenie Hirzebrucha. Rozdział 22
zawiera przestrzenny przykład chirurgii dającej zawęźlony torus.
Na dalszą prośbę autora rozdział 23 rozwinięto o rachunek przecięć
nad `Z[π]`, dowód przejścia od prostego lagranżjanu do bazy
hiperbolicznej, zgodne obramowanie pojedynczej chirurgii poniżej
środka, dokładne ciągi po chirurgii i model formacji nieparzystej.
Rozpisano skończoną indukcję chirurgii poniżej środka dla zamkniętego
przypadku parzystego, używając modelu CW z rozdziału 18 i kontroli
odwróconych uchwytów. Następnie rozwinięto lemat~5.7 Walla: bazowany
ciąg jąder, identyfikację dualną, znoszenie przecięć i samoprzecięć
na brzegu kobordyzmu oraz wynikający z nich prosty lagranżjan.
Nadal osobnego dowodu wymagają realizacja obramowanych immersji,
prosta dualność i bazowość oraz przygotowanie kobordyzmu; dokładne
wejścia Walla wymienia dodatek A.
Pełnego twierdzenia nadal nie oznaczamy jako dowiedzionego:
pozostałe wejścia geometryczne wymienia dodatek A.
Punkt 4 odłożono: skrypt używa
niezmienniczości obszaru jako wyniku wejściowego, więc warunek
samowystarczalności wskazany przez autora nie zachodzi.
Punkty 5--8 mają poniżej plan rozdziałów, ale nowe rozdziały
nie zostały jeszcze napisane.

### Ścieżka: grupy Liego

Zależności: rozmaitości i różniczka (rozdział 1), przepływy i nawias Liego
(rozdział 2), grupy (rozdział 5), nakrycia (rozdział 7). Powinien powstać
**jeden osobny plik w `tex/rozdzialy/`**, włączony przez `\input` po tych
podstawach i przed zastosowaniami w geometrii wiązek i Cherna–Weila.
Do istniejących przykładów $\mathrm O(n)$ i $\mathrm{SO}(n)$ dodać
$\mathrm{GL}(n)$, $\mathrm{SU}(2)$ oraz torus jako grupę Liego.

Kolejność dowodów: gładkość mnożenia i odwrotności w przykładach;
utożsamienie algebry Liego z lewostronnie niezmienniczymi polami i
sprawdzenie, że ich nawias jest zamknięty; jednoznaczność podgrup
jednoparametrowych z twierdzenia o przepływie; konstrukcja odwzorowania
wykładniczego i obliczenia dla grup macierzowych; działanie przez
sprzężenie i różniczka $\operatorname{Ad}$. Dla relacji
$\mathrm{SU}(2)\to\mathrm{SO}(3)$ podać jawne działanie kwaternionowe,
jądro i argument nakryciowy. Pełne twierdzenia Liego o istnieniu grupy
z zadanej algebry lub ogólne BCH dodawać dopiero po przygotowaniu
ich dowodów; nie są potrzebne do tego rdzenia.

### Ścieżka: Hodge–Bochner

Zależności: formy i twierdzenie de Rhama (rozdział 10), metryka i
całkowanie przez części (rozdział 11), koneksja Levi-Civity (rozdział 12)
oraz tensor krzywizny i Ricci (rozdział 14). Przygotować **osobny plik
w `tex/rozdzialy/`**, umieszczony po tych rozdziałach. Rozdział ma
dotyczyć najpierw zwartej, zorientowanej rozmaitości bez brzegu;
przypadek z brzegiem wymaga osobnych warunków brzegowych.

Rozpisać gwiazdkę Hodge'a z konwencjami znaków, iloczyn $L^2$,
operator $\delta$ sprzężony do $d$, laplasjan
$\Delta=d\delta+\delta d$ i równoważność harmoniczności z
$d\alpha=\delta\alpha=0$. Następnie: symbol główny i eliptyczność
$\Delta$; wyraźnie wskazane twierdzenie analityczne dające rozkład
Hodge'a, regularność i skończoność jądra; własny dowód jednoznaczności
przedstawiciela harmonicznego i izomorfizmu z kohomologią de Rhama.
Wyprowadzić, przy ustalonej konwencji krzywizny, wzór
Weitzenböcka dla 1-form, zintegrować go i udowodnić wniosek Bochnera:
przy $\operatorname{Ric}>0$ na zwartej rozmaitości znika
$H^1_{\mathrm{dR}}$; przy $\operatorname{Ric}\geq0$ harmoniczne
1-formy są równoległe. Osobno obliczyć przykłady sfery i torusa.
Pełny dowód analitycznej teorii eliptycznej wymagałby kolejnego bloku
o przestrzeniach Sobolewa i operatorach Fredholma; dopóki go nie ma,
twierdzenie analityczne pozostaje jawnie nazwanym wejściem, a nie
„dowiedzioną” częścią twierdzenia Hodge'a.

### Ścieżka: potok Ricciego

Zależności: metryka (rozdział 11), koneksja Levi-Civity (rozdział 12),
krzywizna i tensor Ricciego (rozdział 14) oraz podstawowe rachunki na
formach z rozdziału 10. W pierwszej wersji rozpatrywać gładkie, zwarte
rozmaitości bez brzegu. Zaplanować **osobny plik w `tex/rozdzialy/`**;
docelowy porządek `\input` w pliku głównym:
`14-krzywizna`, nowy rozdział Hodge–Bochner, nowy rozdział o potoku
Ricciego, obecny `15-sard-transwersalnosc`. Nazwy plików i numery
ustalić przy włączeniu, po sprawdzeniu odsyłaczy liczbowych; na etapie
planowania nie zmieniać istniejącej numeracji.

Zdefiniować rodzinę metryk $g(t)$ przez $\partial_tg=-2\mathrm{Ric}(g)$
i wyjaśnić geometryczny sens znaku. Rozpisać obliczenia dla metryki
okrągłej sfery, gdzie promień maleje, i dla płaskiego torusa, który jest
stacjonarny. Wyprowadzić zmianę elementu objętości oraz krzywizny
skalarnej, jawnie uzgadniając dwie konwencje laplasjanu: rozdział 14
używa $\Delta=\operatorname{div}\nabla$, a plan Hodge–Bochner przyjmuje
$\Delta_H=d\delta+\delta d$ na funkcjach. Przy drugiej konwencji
$\partial_t\mathrm{Scal}=-\Delta_H\mathrm{Scal}+2|\mathrm{Ric}|^2$.
W wymiarze dwa skorzystać z udowodnionego już
w rozdziale 14 wzoru $\mathrm{Ric}=Kg$ i wyprowadzić wynikającą stąd
postać równania; zależność całkowitego pola od cechy Eulera wyprowadzić dopiero
po odwołaniu do twierdzenia Gaussa–Bonneta z rozdziału 27. Dla gotowego
rozwiązania podać i uzasadnić prostą wersję zasady maksimum dla krzywizny
skalarnej, z dokładnymi założeniami.

Istnienie i jednoznaczność rozwiązania dla krótkiego czasu wymagają
teorii równań parabolicznych. Pokazać rachunek wiodącego symbolu po
poprawce DeTurcka oraz odzyskanie potoku Ricciego przez dyfeomorfizmy;
analityczne twierdzenie o istnieniu dla układu parabolicznego podać jako
jawny wynik wejściowy, dopóki jego dowód nie zostanie dopisany.
Zbieżność potoku, analiza osobliwości i twierdzenia Perelmana są odrębnym
dużym etapem i nie należą do dowodów tego rozdziału. Źródła podstawowe:
[Hamilton, *Three-manifolds with positive Ricci curvature* (1982)](https://projecteuclid.org/journals/journal-of-differential-geometry/volume-17/issue-2/Three-manifolds-with-positive-Ricci-curvature/10.4310/jdg/1214436922.full),
[DeTurck, *Deforming metrics in the direction of their Ricci tensors* (1983)](https://projecteuclid.org/journals/journal-of-differential-geometry/volume-18/issue-1/Deforming-metrics-in-the-direction-of-their-Ricci-tensors/10.4310/jdg/1214509286.full).

### Ścieżka: Freedman, Donaldson i egzotyczne $\mathbb R^4$

Ta część powinna następować po teorii uchwytów i chirurgii, nadal w
jednym głównym PDF. Każdy z pięciu punktów poniżej oznacza **osobny
rozdział i osobny plik w `tex/rozdzialy/`**. Sugerowana kolejność:

1. **Algebra i uchwyty w wymiarze cztery.** Przypomnieć formę przecięcia
   z rozdziału 17, obliczyć przykłady form unimodularnych (w tym $E_8$),
   zdefiniować parzystość i sygnaturę, wprowadzić obramowane diagramy
   uchwytowe oraz pokazać na rysunkach, dlaczego gładki trik Whitneya
   zawodzi przy usuwaniu przecięć powierzchni w wymiarze 4. Oddzielić
   kategorię topologiczną, PL i gładką.
2. **Uchwyty Cassona i twierdzenie o osadzaniu dysku.** Zbudować
   pierwsze piętra, znakowane drzewa i intuicję rekurencyjnego usuwania
   przecięć. Sformułować dokładne hipotezy używanej wersji twierdzenia
   Freedmana i zakres grup podstawowych; przeprowadzić wszystkie
   dostępne redukcje geometryczne. Izomorfizmu uchwytu Cassona ze
   standardowym otwartym uchwytem 2 w kategorii topologicznej nie
   ogłaszać udowodnionym bez pełnego argumentu.
3. **Topologiczne zastosowania Freedmana.** Wyprowadzić konsekwencje
   twierdzenia o osadzaniu dysku: odpowiednią klasyfikację zwartych,
   jednospójnych topologicznych rozmaitości 4-wymiarowych przez formę
   przecięcia wraz z niezbędnymi warunkami i niezmiennikiem
   Kirby'ego–Siebenmanna; omówić topologiczną hipotezę Poincarégo w
   wymiarze 4. Każde twierdzenie podać z precyzyjną kategorią i
   hipotezami, bez przenoszenia go na kategorię gładką.
4. **Gładkie przeszkody Donaldsona.** Wykorzystać grupy Liego, koneksje,
   rozkład Hodge'a 2-form i klasy charakterystyczne do zdefiniowania
   krzywizny połączenia oraz równania antysamodualności. Wyjaśnić
   strukturę dowodu twierdzenia o diagonalizacji formy określonej;
   analizę przestrzeni moduli, zwartość i usuwanie osobliwości można
   nazwać dowiedzionymi dopiero po ich rzeczywistym rozwinięciu.
5. **Struktury gładkie na $\mathbb R^4$.** Zbudować drogę od uchwytów
   Cassona i przeszkody gładkiej do otwartych rozmaitości
   homeomorficznych z $\mathbb R^4$, ale nie dyfeomorficznych z
   modelem standardowym. Jako główny cel wybrać rodzinę Gompfa:
   rozpisać konstrukcję zwartych podzbiorów i argument zakazu ich
   gładkiego osadzenia, który rozróżnia nieskończenie wiele elementów.
   Sprawdzić, czy sformułowanie dotyczy dyfeomorfizmów zachowujących
   orientację, czy wszystkich; sama mnogość opisów uchwytowych niczego
   tu nie dowodzi. Wynik DeMichelisa i Freedmana o kontinuum klas może
   być następnym etapem, z jawnym wskazaniem zależności od teorii
   cechowania i twierdzenia Taubesa.

Źródła do weryfikacji hipotez i oznaczenia granicy samowystarczalności:
[Freedman, *The topology of four-dimensional manifolds* (1982)](https://projecteuclid.org/journals/journal-of-differential-geometry/volume-17/issue-3/The-topology-of-four-dimensional-manifolds/10.4310/jdg/1214437136.full),
[Donaldson, *Self-dual connections and the topology of smooth 4-manifolds* (1983)](https://doi.org/10.1090/S0273-0979-1983-15090-5),
[Gompf, *An infinite set of exotic R⁴'s* (1985)](https://doi.org/10.4310/jdg/1214439566),
[DeMichelis–Freedman, *Uncountably many exotic R⁴'s in standard 4-space* (1992)](https://projecteuclid.org/euclid.jdg/1214447810).
Przy pisaniu podać dokładne źródło każdego użytego twierdzenia analitycznego
i topologicznego, w tym twierdzenia Taubesa, jeśli jest potrzebne.

### Włączenie do składu i kontrola

Nowe rozdziały mają własne pliki w `tex/rozdzialy/`, dodatki w
`tex/dodatki/`, a ich kolejność określa wyłącznie `\input` w pliku
głównym. Przed nadaniem ostatecznych numerów sprawdzić wszystkie
liczbowe odsyłacze w prozie, podpisach rysunków i bibliografii;
istniejące `\label` oraz `\ref` zachować. Po każdym etapie zaktualizować
mapę książki we wstępie, katalog wyników zewnętrznych, indeks oraz
złożyć i obejrzeć cały PDF zgodnie z `AGENTS.md`.

## Kolejka audytu

| Zakres | Stan | Następna kontrola |
|---|---|---|
| Podział źródeł i importy | Zakończono, `9148128` | Kontrola regresji przy dalszych zmianach |
| 1. Rozmaitości | Nowe dodatki sprawdzone, `aa6c59a` | Brzeg i pełna przestrzeń styczna mają uzupełniony dowód |
| 5. Algebra abstrakcyjna | Audyt zakończony 6 października; PDF 387 stron | Uzupełnione dowody, sprawdzony graf słów, indeks i odsyłacze |
| 2. Pola wektorowe | Audyt dodatków zakończony 6 października; PDF 387 stron | Sprawdzone powiązanie z brzegiem, przykład przepływu jednostronnego, bibliografia i rysunki |
| 3. Algebra tensorowa | Audyt dodatków zakończony 6 października; treść bez poprawek | Poprawny odsyłacz do rozdziału 5, indeks, źródła i ilustracje |
| 4. Grassmanniany, Clifford i spinory | Audyt dodatków zakończony 6 października; treść bez poprawek | Sprawdzone dwa zmienione rysunki sfer, pozostałe ilustracje i indeks |
| 6. Algebra homologiczna | Audyt dodatków zakończony 6 października; PDF 387 stron | Zachowana kompletność po przeniesieniu, przywrócone założenie o R i związek redukcji modulo m z tensorem |
| 7. Homotopia, nakrycia i CW | Audyt dodatków zakończony 6 października; PDF 387 stron | Precyzyjne odsyłacze do grup, końcowa faktoryzacja i przykład torusa |
| 8. Homologia przestrzeni | Audyt dodatków zakończony 6 października; treść bez poprawek | Sprawdzone pięć wpisów indeksu, definicje, bibliografia i trzy ilustracje; PDF 397 stron |
| 9. Wyższe grupy homotopii | Audyt dodatków zakończony 6 października; PDF 397 stron | Sprawdzone indeks, definicje i cztery rysunki; poprawiono 19 użyć słowa „mapa” na „odwzorowanie” |
| 10. Formy i de Rham | Audyt dodatków zakończony 6 października; bez poprawek treści | Siedem wpisów indeksu, pięć ilustracji i zgodność konwencji przy brzegu; PDF 397 stron |
| 11. Metryka, długość i miara | Audyt dodatków zakończony 6 października; PDF 397 stron | Sprawdzone definicje i dwie ilustracje; usunięty powtórzony wpis indeksu |
| 12. Koneksje i transport | Audyt dodatków zakończony 6 października; bez poprawek treści | Cztery wpisy indeksu, definicje i dwa rysunki sprawdzone; PDF 397 stron |
| 13. Geodezyjne i zupełność | Audyt dodatków zakończony 6 października; PDF 397 stron | Definicje i dziewięć ilustracji sprawdzone; usunięty powtórzony wpis indeksu |
| 14. Krzywizna | Audyt dodatków zakończony 6 października; PDF 397 stron | Indeks i trzy zmiany cieniowania sprawdzone; rozwinięto powiązania dowodu Cherna–Gaussa–Bonneta z rozdziałami 17 i 27 |
| 15–19 | Dawna treść przeszła audyt; różnice po rozbudowie zinwentaryzowano | Przejrzeć różnice rozdziałami, zaczynając od rozdziału 15; uwzględnić nowe commity do `46fd90c` |
| 20. h-kobordyzm | Oczekuje | Hipotezy wymiarowe, dyski Whitneya, realizacja ruchów uchwytów |
| 21. Torsja i s-kobordyzm | Oczekuje | Bazy, strona działania pierścienia, konwencje torsji |
| 22. Chirurgia geometryczna | Oczekuje | Obramowania, zmiany homotopii i homologii, rysunki |
| 23. Przeszkoda chirurgiczna | Rozwinięto redukcję poniżej środka i rachunek lematu 5.7 Walla 6 października; pełny audyt czeka | Dowieść obramowanego osadzania 5.2, przygotowania 1.4, bazowości i dualności 2.4/2.6 oraz formacji §6 Walla |
| 24. Ciąg chirurgii | Oczekuje | Normalne niezmienniki, zbiór struktur, sens dokładności |
| 25. Poincaré | Oczekuje | Wymiar 2, osobno 5 i wyższe; homeomorfizm a dyfeomorfizm |
| 26. Sfery Milnora | Oczekuje | Sklejenie wiązek, klasy charakterystyczne, egzotyczność |
| 27. Chern–Weil | Oczekuje | Normalizacje i transgresja; uzasadnić model względnej kohomologii de Rhama przy identyfikacji klasy Eulera, granicę całek wokół zer i wersję brzegową |
| Dodatek A o wynikach zewnętrznych | Oczekuje | Zgodność katalogu zależności z rzeczywistymi dowodami |
| Dodatek B: homologia singularna i Euler | Dodany w `59fd235`; audyt oczekuje | Wzory Eulera, skończoność, przykłady i zależności od rozdziałów 8 i 17 |
| Ponowne różnice w 2–7 | Sprawdzone przy scaleniu `46fd90c`; PDF 397 stron | Wyłącznie format bibliografii; zachowane słowa i źródła, obejrzane zakończenia oraz poprawki rozdziału 7 |
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
| 2 | Grupy i prezentacje | Są w rozdziale 5: ilorazy, domknięcie normalne, grupa wolna, iloczyn wolny i prezentacja torusa. Postać normalną uzupełniono w `23483ad`; zastosowanie van Kampena sprawdzono w rozdziale 7. |
| 3 | Redakcja i nawigacja | Jest mapa książki, spis oznaczeń, indeks i rozdzielone źródła. Zakończenia rozdziałów ujednolicono w obecnym etapie; dalsza kontrola stylu rozdziału 1 i precyzji lektur pozostaje. Zachować rozbudowane przykłady. |
| 4 | Zadania z rozwiązaniami | Nie realizować w obecnym zakresie. Dawna propozycja rachunków, kontrprzykładów i wspólnych przykładów (sfera, torus, przestrzenie rzutowe, Möbius) pozostaje odłożona. |
| 5 | Wyniki zewnętrzne i samowystarczalność | Jest dodatek. Sprawdzić hipotezy i odsyłacze, w tym Brouwera, funkcję odwrotną, triangulację i przeszkodę spinową. Pełna triangulacja oraz porównanie kohomologii Čech i singularnej są osobnymi możliwymi rozszerzeniami, nie krótkimi poprawkami. |
| 6 | Chern–Weil i Chern–Gauss–Bonnet | Jest rozdział 27. Sprawdzić wielomiany niezmiennicze, niezależność od koneksji, identyfikację formy Eulera z klasą topologiczną i jawne określenie formy brzegowej. |
| 7 | h-kobordyzm Smale'a | Jest rozdział 20. Sprawdzić wymiar W≥6, spójność, obramowania dysków Whitneya, skrajne indeksy i redukcję uchwytów do iloczynu z ustalonym dolnym końcem. |
| 8 | Torsja Whiteheada i s-kobordyzm | Jest rozdział 21. Sprawdzić Z[π₁], bazowane kompleksy nakrycia, prostą równoważność i przeszkodę do iloczynu. Nie utożsamiać torsji Whiteheada z trikiem Whitneya. |
| 9 | Chirurgia i jej przeszkody | Są rozdziały 22–24, szerzej niż pierwotnie proponowano. Audyt obejmie wpływ operacji na π₁, homologię i formę przecięcia, obramowania, zabijanie klas, Walla i ciąg dokładny. |
| 10 | Poincaré | Jest rozdział 25. Dla n=2 sprawdzić użycie klasyfikacji powierzchni; dla n>5 usunięcie dysków, h-kobordyzm i sklejenie; n=5 wymaga osobnego argumentu. Nie zamieniać homeomorfizmu w dyfeomorfizm. Wymiar 4 zaplanowano osobno w tym PDF. |
| 11 | Sfery Milnora | Jest rozdział 26: wiązki S³ nad S⁴, rachunki i niezmiennik egzotyczności. Sprawdzić użycie klas Pontriagina i sygnatury. Dalsze grupy sfer homotopijnych pozostają możliwym rozszerzeniem. |
| 12 | Egzotyczne R⁴ | Zaplanowane w tym PDF: topologia końców, uchwyty Cassona, Freedman i Donaldson. Nie wynika to z samego niepowodzenia triku Whitneya ani z konstrukcji sfer Milnora. |

## Pozostałe pomysły po audycie

1. **Hodge i Bochner–Weitzenböck:** przyjęte do planu osobnego rozdziału
   w ścieżce Hodge–Bochner powyżej.
2. **Holonomia i rozkład de Rhama:** rozwinąć transport równoległy
   i kryteria lokalnego oraz globalnego rozkładu metryki na produkt.
3. **Geometria podrozmaitości:** równania Gaussa–Codazziego, krzywizna średnia
   i pierwsze przykłady powierzchni minimalnych, na bazie drugiej formy podstawowej.
4. **Dłuższe zależności i rozszerzenia:** triangulacja, porównanie Čech–singularna
   oraz grupy sfer homotopijnych — zakres do ustalenia po sprawdzeniu dodatku
   i rozdziału Milnora. Nie oznaczać ich jako już wykonanych.

Po kolejnych audytach aktualizować pozostałe pomysły na podstawie
faktycznych braków. Pierwszeństwo mają naprawy obecnego materiału.

## Źródła zachowane z wcześniejszych propozycji

- [Morgan: znoszenie uchwytów i h-kobordyzm](https://www.math.columbia.edu/~jmorgan/Lecture_IIIA_hcobordism_Contd.pdf).
- [Ranicki: chirurgia algebraiczna i geometryczna](https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf).
- [Milnor: omówienie Poincarégo dla Clay](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf).
- [Milnor: oryginalna konstrukcja egzotycznej sfery](https://sites.math.rutgers.edu/~feehan/teaching/math866/milnor7sphere.pdf).
- [Gompf: egzotyczne R⁴](https://arxiv.org/abs/1705.06644).
- [Clay: program topologii niskich wymiarów](https://www.claymath.org/events/recent-advances-in-low-dimensional-topology/)
  — źródło wcześniejszego sprawdzenia statusu gładkiego problemu Poincarégo
  w wymiarze 4; nie planować dopisywania jego dowodu.
