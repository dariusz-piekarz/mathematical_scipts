# Przegląd matematyczny skryptu

Gałąź: `review/rozdzialy-matematyka`. Jedna iteracja obejmuje jeden rozdział.
Źródło: `geometria_i_topologia_rozniczkowa.tex`; wynik: plik PDF o tej samej nazwie.
Rejestr zawiera także uzasadnienia, aby można było niezależnie sprawdzić poprawki.
Aktualny zakres, kolejka i propozycje są wyłącznie w [planie](PLAN_DZIALANIA.md).
Poniższe wpisy są chronologiczne: numery rozdziałów, strony i statusy dotyczą
wersji wskazanej w danym wpisie. Audyt 18 rozdziałów nie obejmuje późniejszych
dodatków autora. Od 5 października źródła są w `tex/rozdzialy/`;
plik główny tylko ustala ich kolejność.

## Iteracja 1 — Rozmaitości różniczkowe

Status: sprawdzono i poprawiono wszystkie 11 sekcji oraz 15 ilustracji.
Data: 2026-09-30. Źródło bazowe: pierwotny `origin/main` pobrany w tej iteracji.

### 1.1. Rozmaitości topologiczne

1. **Niezmienniczość wymiaru a niezmienniczość obszaru.** Tekst utożsamiał
   nazwy dwóch twierdzeń. Podano właściwą treść twierdzenia Brouwera i wyprowadzono
   z niej niezmienniczość wymiaru przez dołączenie zer. Obraz w podprzestrzeni
   niższego wymiaru nie może być otwarty w przestrzeni wyższego wymiaru.
   Doprecyzowano wyjątek pustej rozmaitości.
2. **Metryzowalność i parazwartość.** Rozpisano ciąg przesłanek:
   lokalna zwartość + Hausdorff → regularność; przeliczalna baza + regularność
   → metryzacja Urysohna; metryzowalność → parazwartość. Są to jawnie
   przyjęte twierdzenia topologii ogólnej. Usunięto błędną sugestię, że lokalna
   funkcja odcinająca wymaga rozkładu jedności, który dopiero z takich funkcji się buduje.

### 1.2. Atlasy i rozmaitości gładkie

3. Sprawdzono zgodność map, równoważność atlasów, maksymalizację atlasu
   i przykład struktury określonej przez x³. Dowody zasadniczo poprawne;
   różność struktur na ustalonym zbiorze nie oznacza braku dyfeomorfizmu.

### 1.3. Rozmaitości zespolone

4. **Holomorficzność implikuje gładkość.** Zastąpiono niepełne odwołanie
   do równań Cauchy’ego–Riemanna argumentem z lokalnej analityczności,
   wynikającej ze wzoru całkowego Cauchy’ego na polidysku.
5. **Sfera Riemanna.** Rzeczywiste rzuty z dalszego przykładu mają przejście
   z/|z|² = 1/conj(z), a nie 1/z. Odwrócono drugą współrzędną w mapie
   południowej; wtedy przejście jest holomorficzne. Dodano jawny wzór
   CP¹ → S², sprawdzenie niezależności od reprezentanta, obrazu na sferze,
   bijektywności i gładkości obu kierunków. Rysunek otrzymał zgodne oznaczenia
   ζ_N, ζ_S i objaśnienie dziedziny przejścia.

### 1.4. Odwzorowania gładkie

6. **Gładkość w punkcie.** Doprecyzowano, że chodzi o gładkość na otwartym
   otoczeniu współrzędnych punktu. Rozpisano wynikającą z definicji ciągłość
   i możliwość zmniejszenia dziedzin przy zmianie map.

### 1.5. Przykłady rozmaitości

7. **Przestrzenie rzutowe.** Uzupełniono dowód ciągłości map ilorazowych:
   współrzędne schodzą z ciągłych ilorazów, a odwrotność wstawia 1
   i przechodzi do klasy. Oddzielono budowę map od późniejszego sprawdzenia
   aksjomatów Hausdorffa i przeliczalności. Poprawiono „nadającym struktury”.
8. **Torus jako iloraz.** Brakowało sprawdzenia Hausdorffa i drugiej
   przeliczalności. Rozłączne otoczenia skonstruowano z dodatniej odległości
   różnicy reprezentantów od kraty; bazę uzyskano przez otwarte rzutowanie
   przeliczalnej bazy Rⁿ.

### 1.6–1.7. Przestrzeń styczna i kostyczna

9. **Przedłużanie funkcji odcinającej przez zero.** Wymagamy zawierania
   całej domkniętej kuli w obrazie mapy. Zwarty nośnik leży wewnątrz mapy
   i jest domknięty w M; pokrycie U oraz M poza nośnikiem uzasadnia gładkość
   przedłużenia, której samo uzgodnienie wartości nie wystarczało dowieść.
10. **Błąd dziedziny we współrzędnych.** W dowodzie izomorfizmu przestrzeni
    stycznych zastąpiono niedozwolone złożenie xⁱ∘φ przez xⁱ = φⁱ.
    Funkcje xⁱ zostały wcześniej zdefiniowane na M, nie na Rⁿ.
    Jawnie dobrano funkcję odcinającą w bieżącej mapie.
11. Sprawdzono trzy definicje przestrzeni stycznej, lemat Hadamarda,
    lokalność derywacji, bazę współrzędnościową i dualną oraz wzór na df.

### 1.8–1.9. Wiązki i funkcje przejścia

12. **Terminologia.** Obraz całej wiązki nie jest jej „przekrojem”;
    zmieniono podpis rysunku. Dodano równoważne terminy „sekcja” i „przekrój”,
    definicję izomorfizmu wiązek oraz uzasadnienie gładkości przekroju zerowego.
13. **Trywializacja Möbiusa przy sklejeniu.** Dotychczas opisano wyłącznie
    łuki omijające sklejenie. Dodano trywializację z ujemnym kątem i zmianą
    znaku we włóknie oraz sprawdzenie przejść i aksjomatów topologicznych.
14. **Przekroje ciągłe i gładkie.** Warunek f(2π) = −f(0) zapewnia jedynie
    ciągły przekrój. Dla gładkości trzeba zgodności wszystkich pochodnych
    z tym samym znakiem. Dodano też odwrotny kierunek korespondencji,
    niezbędny w dowodzie nietrywialności.
15. **Brzeg wstęgi Möbiusa — błąd rzeczowy.** Cała wiązka z włóknem R
    nie ma brzegu. Zwarty pas |t| ≤ c ma brzeg, ale jego włókna są odcinkami,
    więc nie jest wiązką wektorową. Doprecyzowano też ograniczenie parametru
    w modelu narysowanym w R³ i jedną składową brzegu zwartego pasa.
16. **Topologia TM i sklejanej wiązki.** Zbiór z bijekcjami współrzędnych
    nie jest jeszcze rozmaitością. Dodano definicję topologii i uzasadnienie,
    że dziedziny są otwarte, mapy są homeomorfizmami, a rzutowanie ciągłe.
    Poprawiono kolejność złożenia definiującego trywializację TM.
17. **Warunek kocyklu.** Poprawiono „kokykl” oraz objaśnienie:
    porównujemy bezpośrednią zmianę współrzędnych z jej złożeniem przez trzecią mapę.

### 1.10. Różniczka i rząd

18. **Niewymierne nawinięcie torusa.** Sama wzmianka o gęstości nie była
    uzasadnieniem nieciągłości odwrotności. Dodano dowód injektywności,
    immersyjności, ciąg powracających punktów z zasady szufladkowej i dowód
    gęstości przez małe niezerowe wielokrotności α modulo 1.
19. **Twierdzenie o rzędzie stałym.** Oddzielnie obsłużono rząd zero.
    Znikanie pochodnych w kierunkach włókna przekłada się na niezależność
    od tych zmiennych po ograniczeniu do produktu kul; dodano całkę
    wzdłuż odcinka, która uzasadnia ten krok.

### 1.11. Podrozmaitości

20. **Obraz zanurzenia.** Postać lokalna u ↦ (u,0) nie daje automatycznie
    równości obrazu z całym plasterkiem w dowolnie dobranej mapie celu.
    Dodano dobór produktu kul i odpowiednie zmniejszenie obu map przed
    zastosowaniem homeomorficzności na obraz.
21. Sprawdzono dowód struktury podrozmaitości, przeciwobrazu wartości
    regularnej, identyfikacji przestrzeni stycznej z jądrem oraz rachunki
    dla sfery, O(n) i torusa obrotowego.

### Dalsze doprecyzowania z tej samej iteracji

22. **Rzut stereograficzny — nowy rysunek.** Zastąpiono rzut na płaszczyznę
    styczną w biegunie południowym dokładnym przekrojem rzutu na płaszczyznę
    równikową, czyli tę z definicji. Usuwa to konieczność pamiętania o czynniku 2.
    Współrzędne rysunkowe N=(0,1), x=(3/5,4/5), P=(3,0) spełniają
    równanie okręgu, współliniowość i wzór P=x₁/(1−x₂).
23. **Kolejność wprowadzania pojęć.** Przeniesiono przykład wiązki normalnej
    za definicję podrozmaitości i dowód jej struktury. Poprzednio używał
    niezdefiniowanej mapy plasterkowej. Jawnie wskazano identyfikację TS
    przez różniczkę inkluzji.
24. **Druga przeliczalność.** Dodano prosty kontrprzykład: nieprzeliczalną
    sumę rozłączną prostych. Długa prosta pozostaje przykładem spójnym;
    nie jest już potrzebna do uzasadnienia niezależności aksjomatów.
25. **RP¹ i wiązka tautologiczna.** Dodano dowód identyfikacji RP¹ z S¹
    przez z ↦ z² oraz jawny izomorfizm wiązki Möbiusa z tautologiczną,
    używający wektora (cos(θ/2), sin(θ/2)). Sprawdzono sklejenie
    i gładką odwrotność w lokalnych trywializacjach.
26. **Metryka na przestrzeni rzutowej.** Dodano ciągłość rzutowania
    z przestrzeni bez zera przez normalizację. Wcześniejsze przejście
    od ciągłości na sferze do zgodności z pierwotną topologią ilorazową
    pomijało właśnie ten krok.
27. **Drobne doprecyzowania.** Ustalono konwencję rozmaitości bez brzegu,
    dodano brakujące dim M=n w twierdzeniu o poziomicy, ujednolicono
    „surjektywność”, poprawiono zapis mapy jako pary (U,φ) z osobno
    podanymi współrzędnymi i gramatykę zdania o bazie dualnej.
28. **Rysunek przestrzeni stycznej.** Kontrola PDF wykazała sztuczny
    trójkąt wypełnienia poza obrysem powierzchni. Zbudowano jeden ciągły
    obrys z tej samej parametryzacji co siatka: S(u,v)=(u,v,0.12u²+0.08v²).
    Rzut (x,y,z) ↦ (x+0.45y,0.65y+z) i mniejsza krzywizna dają czytelny
    obraz bez nakładania się siatki. Płaszczyzna styczna w zerze to z=0,
    krzywa γ(t)=(t,0,0.12t²) leży na powierzchni i ma styczną (1,0,0).
29. **Pliki pomocnicze.** Dodano `.gitignore` dla katalogu `build/`
    i produktów pośrednich LaTeX. PDF pozostaje śledzony i zostanie
    zaktualizowany razem ze źródłem. Skrypty robocze i podglądy nie trafiają do repozytorium.
    Dodano też `.gitattributes` z `*.pdf binary`, aby Git nie traktował
    zawartości PDF jako tekstu przy kontroli białych znaków i zmian końców linii.
30. **Domknięcie argumentów lokalnych.** Rozpisano blokową różniczkę
    przejść map plasterkowych: dolny lewy blok jest zerowy, a odwracalny
    dolny prawy blok wyznacza przejścia wiązki normalnej i spełnia warunek
    kocyklu. Dopisano otwartość rzutowania przestrzeni rzutowej przez sumę
    dylatacji. Przy dxⁱ doprecyzowano przedłużanie funkcji zgodnej jedynie
    blisko punktu, zamiast sugerować możliwość przedłużenia dowolnej
    funkcji z całej dziedziny mapy.

### Kontrola i materiały pomocnicze

- Kontrola rachunków i logicznych zależności: bezpośrednio ze źródła LaTeX.
- Sprawdzenia symboliczne (SymPy): wzór CP¹ → S² i obie mapy zespolone,
  Jacobian przejścia w RP² oraz dokładna geometria nowego rzutu stereograficznego — poprawne.
- Porównanie źródeł z bazowym commitem: treść rozdziałów 2–18 niezmieniona.
- Kontrola zbilansowania środowisk LaTeX w rozdziale 1 oraz `git diff --check` — poprawne.
- Rozróżnienie twierdzeń Brouwera porównano z pierwotnym artykułem
  [Takayukiego Kihary](https://www.math.mi.i.nagoya-u.ac.jp/~kihara/pdf/paper/invariance.pdf), twierdzenie 1.1.
- Punkt odniesienia dla konwencji rozmaitości:
  [John M. Lee, Introduction to Smooth Manifolds, strona autora i errata](https://sites.math.washington.edu/~lee/Books/ISM/).
- Kontrola wizualna: obejrzano strony 4–35 PDF, w tym wszystkie 15 ilustracji
  rozdziału 1. Ponownie sprawdzono strony po zmianach wypełnienia powierzchni
  stycznej i końcowych uzupełnieniach tekstu.
- Kompilacja: pełny dokument, pdfLaTeX z lokalnego MiKTeX Portable;
  ponawiana do ustabilizowania odsyłaczy. Nie ma błędów LaTeX, niezdefiniowanych
  odsyłaczy ani przepełnionych wierszy (`Overfull`). Pozostają cztery ostrzeżenia
  `Underfull` w dalszych, jeszcze nieprzejrzanych rozdziałach i automatyczne
  dopuszczenie położenia `ht` dla dwóch rysunków zadanych jako `h`.
  MiKTeX emituje dodatkowo komunikat administracyjny o niesprawdzonych
  aktualizacjach; nie przerywa on poprawnej kompilacji.

Polecenie odtworzenia PDF (utworzyć wcześniej katalog `build` i uruchamiać,
aż zniknie komunikat o konieczności ponownego przeliczenia odsyłaczy):

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build geometria_i_topologia_rozniczkowa.tex
```

Źródło i wynikowy PDF należą do tego samego commita przeglądu rozdziału 1.

## Iteracja 2 — Pola wektorowe, przepływy i pochodna Liego

Status: sprawdzono i poprawiono wszystkie 7 sekcji oraz 4 ilustracje.
Data: 2026-10-01. Baza rozpoczęcia pracy: `e144985` (ukończony rozdział 1).
Przed publikacją pobrano i zachowano zdalne commity `5043a70` i `dc53c6b`,
rozwijające przykład 1.1.6. Poprawki rozdziału 2 nałożono na `dc53c6b`;
konflikt binarnego PDF rozwiązano przez ponowną kompilację wspólnego źródła.

1. **Konwencje i terminologia.** Ujednolicono „infinitezymalny” oraz
   „zupełny/zupełność” w odniesieniu do pól. Określono konwencję rozmaitości
   bez brzegu i znaczenie gładkości w półprzestrzeniach, potrzebne na końcu
   rozdziału. Przedział krzywej całkowej jest otwarty.
2. **Derywacje globalne.** W konstrukcji współczynników pola wybiera się
   kulę we współrzędnych o zwartym domknięciu w dziedzinie mapy. Dzięki temu
   funkcja odcinająca wynika bezpośrednio z konstrukcji w rozdziale 1.
3. **Pola wzdłuż odwzorowania.** Zdefiniowano wiązkę cofniętą F*TN i jej
   lokalne trywializacje. Wyjaśniono, dlaczego dla ogólnego F nie powstaje
   automatycznie pole na N; odróżniono je od przenoszenia przez dyfeomorfizm.
   Przy nietrywialności TS² dodano odsyłacz do późniejszego uzasadnienia.
4. **Nawias Liego.** Dodano wyprowadzenie współczynników przez działanie
   na współrzędne lokalne i wyjaśnienie sumowania powtarzających się indeksów.
5. **Frobenius.** Uściślono definicję rozkładu, treść twierdzenia w mapach
   i konieczność inwolutywności; sprawdzono kontrprzykład w R³. Dodano dowód
   wystarczalności przez indukcję po rzędzie: prostowanie jednego pola,
   macierzowe równanie Q′=−AQ usuwające zależność bazy od tego czasu
   i zastosowanie indukcji na przekroju. Umieszczono go dopiero po twierdzeniu
   o prostowaniu, na którym się opiera.
6. **Gładka zależność rozwiązań.** Rozpisano oszacowanie różnic rozwiązań
   równania wariacyjnego i ciągłość pierwszej pochodnej. Przy kolejnych
   pochodnych wskazano równanie liniowe dla nieznanej pochodnej, kontrolę
   reszty Taylora i krok indukcyjny; samo formalne różniczkowanie nie dowodzi
   wcześniej istnienia tych pochodnych. Pochodne mieszane wynikają z równania.
7. **Zmiana parametryzacji.** Podano całkę definiującą nowy czas dla Y=fX,
   f>0, i argument zgodności maksymalnych orbit w obu kierunkach. Przykład
   ∂x oraz (1+x²)∂x pokazuje, że zupełność nie jest zachowywana.
8. **Prostowanie pola.** Skonstruowano przekrój poprzeczny w mapie, wybrano
   produktową dziedzinę i wyprowadzono postać przepływu z prawa grupowego.
9. **Niezmienniczość i komutowanie.** Uzupełniono dowód równoważności trzech
   warunków, w tym zgodność maksymalnych przedziałów pola Y po działaniu
   zupełnego przepływu X. Dodano osobny dowód wzoru
   d/dt Φt*Y = Φt*[X,Y], z jawnym odsyłaczem w miejscu użycia.
10. **Pierwsza całka obrotu.** Poziomice dodatnie są okręgami, zerowa jest
    punktem stałym, ujemne są puste; pierwotne zdanie pomijało te wyjątki.
11. **Komutator przepływów.** Przeniesiono rysunek i rachunek za definicję
    przepływu oraz pochodnej Liego. Rozpisano wszystkie cztery rozwinięcia
    Taylora do rzędu drugiego, aby uzasadnić znak nawiasu dla dowolnych pól.
    Podpis nie nazywa już składnika t² pierwszym niezerowym przy zerowym nawiasie.
12. **Rysunek przesuwania przekroju.** Końce obu odcinków poprzecznych mają
    teraz identyczny zakres niezmiennika y−A sin(κx). Wcześniej były dobierane
    przybliżeniowo i nie stanowiły dokładnego obrazu przez ten przepływ.
    Podano rzeczywiste stałe rysunku i dokładny wzór przepływu.
13. **Pola zależne od czasu.** Wymagana jest łączna gładkość w (t,p).
    Podniesienie do ∂t+Xt uzasadnia gładką zależność od obu czasów i punktu.
    Wskazano dziedziny praw ewolucji i dowód istnienia na całym [0,1]
    przy wspólnym zwartym nośniku, także przy końcach przedziału czasu.
14. **Generator izotopii.** Dodano dowód łącznej gładkości odwrotności ht⁻¹
    przez odwzorowanie (t,p)↦(t,ht(p)). Doprecyzowano „osadzenie”
    i zdefiniowano nośnik całej izotopii.
15. **Ślad izotopii.** To podrozmaitość z brzegiem, nie bez brzegu.
    Skonstruowano mapy zachowujące czas, które prostują ślad również
    w chwilach 0 i 1; nie stosuje się bez wyjaśnienia twierdzenia bez brzegu.
16. **Przedłużenie prędkości izotopii.** Uściślono lokalne nośniki i zbiór U,
    na którym suma funkcji odcinających jest dodatnia. Końcowa funkcja
    odcinająca musi mieć nośnik wewnątrz U, a nie jedynie w dużym otoczeniu O:
    inaczej wcześniejszy wzór dzieliłby przez zero. Podano konstrukcję funkcji
    odcinającej i wspólnego zwartego nośnika przez rzut na M.
17. **Kołnierz brzegu.** Uzasadniono konstrukcję pola skierowanego do wnętrza
    i lokalną odwracalność w półotoczeniach. Dodano argument ciągowy ze
    zwartości, który zamienia lokalną injektywność w globalną dla wspólnego
    małego czasu. Samo twierdzenie o funkcji odwrotnej tego nie zapewnia.
18. **Doprecyzowania po kontroli.** Uzasadniono konieczność i lokalną
    wystarczalność styczności do brzegu dla przepływu dwustronnego.
    Odróżniono lokalne prawo grupowe od globalnej grupy przy polu zupełnym.
    W zmianie parametryzacji dopisano argument zachowania maksymalności.
    Podpis pola obrotowego ujawnia wspólną skalę strzałek (0,22), a wektor
    t²[X,Y] na schemacie komutatora ma teraz dokładnie długość pionowej
    różnicy między początkiem i końcem. Użyto terminu „przekrój poprzeczny”.

### Kontrola iteracji 2

- Przeczytano cały rozdział, sprawdzając definicje, rachunki, dowody
  i kolejność zależności. Nowe dowody korzystają z wcześniej wykazanych
  faktów; późniejsze użycia są oznaczone odsyłaczami.
- Weryfikacja symboliczna w SymPy: znak komutatora dla pary nieliniowych
  pól na płaszczyźnie, rozwiązania obrotu, x′=x², x′=1+x² oraz niezmiennik
  i pochodna przepływu z rysunku przekrojów — poprawne.
- Porównanie ze źródłem w `dc53c6b` po integracji zdalnych zmian:
  rozdział 1 i rozdziały 3–18 pozostały niezmienione przez tę iterację.
  Środowiska LaTeX są zbilansowane, wszystkie
  odsyłacze rozdziału mają cele, brak powtórzonych etykiet.
- Jako zewnętrzny punkt odniesienia dla lokalnej postaci twierdzenia
  Frobeniusa wykorzystano twierdzenie 14.5 w
  [J. M. Lee, Introduction to Smooth Manifolds, wersja robocza 3.0](https://www.math.colostate.edu/~renzo/teaching/DiffGeo2011/Introduction%20to%20Smooth%20Manifolds%20-%20J.%20Lee.pdf),
  s. 359 (strona 371 pliku PDF). Numeracja dotyczy tej wersji,
  nie drugiego wydania wymienionego w bibliografii skryptu.
- Kontrola wizualna całego rozdziału: strony 36–51 PDF; wszystkie cztery
  ilustracje obejrzano również w większej rozdzielczości (strony 42, 44,
  47, 49). Opisy, kierunki strzałek i wzajemne położenia są czytelne.
- Pełna kompilacja pdfLaTeX: 275 stron, bez błędów, niezdefiniowanych
  odsyłaczy i przepełnionych wierszy. Pozostały wcześniejsze cztery
  ostrzeżenia `Underfull` poza rozdziałem 2 oraz trzy automatyczne zmiany
  położenia rysunków `h` na `ht` po integracji zmian przykładu 1.1.6.
  Polecenie odtworzenia PDF podano wyżej.
- `git diff --check` poprawny. Źródło i zaktualizowany PDF publikowane razem.

## Iteracja 3 — Algebra tensorowa i zewnętrzna

Status: sprawdzono i poprawiono wszystkie 9 sekcji oraz sprawdzono 2 ilustracje.
Data: 2026-10-01. Baza: `9bfa3af`.

1. **Konstrukcja iloczynu tensorowego.** Poprawiono klasę x+R dla x∈F
   (wcześniejsze [x]+R niepotrzebnie wprowadzało drugi symbol klasy).
   Wskazano kombinacje liniowe klas generatorów i poprawiono gramatykę.
   Zaznaczono, że pomocnicza przestrzeń wolna jest na ogół nieskończenie
   wymiarowa mimo skończonych wymiarów V i W.
2. **Terminologia baz.** Eij nazwano jednostkami macierzowymi i podano ich
   elementy. „Macierz jednostkowa” oznacza zwykle macierz identycznościową,
   więc poprzednia nazwa była myląca. „Tuple” zastąpiono układami lub ciągami.
3. **Wiele czynników.** Dopisano uzasadnienie niezależności izomorfizmów
   od sposobu zmiany nawiasowania dla więcej niż trzech przestrzeni.
4. **Dualność i stopień zero.** Wyraźnie określono liniowość nad C bez
   sprzężenia, puste iloczyny, funkcje bez argumentów oraz T⁰₀(V)=K.
   Wyprowadzono zmianę bazy dualnej i macierzy operatora A⁻¹[S]A.
5. **Iloczyn mieszany.** Ustalono kanoniczne przestawienie bloków, które
   identyfikuje iloczyn tensorów typów (r,s), (r′,s′) z typem (r+r′,s+s′).
   Przestawienie nie wprowadza znaku. Podano porządek par dla macierzy Kroneckera.
6. **Kontrakcja.** Określono zakres indeksów, kolejność pozostałych czynników
   i wzór sumowania współczynników. Wcześniejszy opis pomijał te konwencje.
7. **Algebra tensorowa.** Zdefiniowano homomorfizm algebr z jedynką
   i element jednorodny. Uzasadniono dobre określenie mnożenia przez własność
   uniwersalną, przypadek skalarów i skończoność wyniku w sumie prostej.
8. **Symetryzacja.** Dopisano działanie permutacji z prawej strony
   symetryzatora i antysymetryzatora; jest ono używane w dowodzie zanikania
   ideału. Wyjaśniono, że rozkład Sym+Alt=id zachodzi w stopniu 2,
   i podano kontrprzykład dla stopnia 3.
9. **Algebra symetryczna.** Uzasadniono jednorodność ideału J i stopniowanie
   ilorazu. Doprecyzowano odwrotność izomorfizmu z obrazem symetryzatora,
   stopień zero i przestrzeń V=0, do której nie stosuje się podanego wzoru
   wymiaru dla n≥1. Ujednolicono termin „jednomian”.
10. **Alternowanie i znaki.** Wyprowadzono równoważność zerowania przy
    powtórzeniu argumentów ze zmianą znaku przy transpozycji (nad R lub C).
    Wyjaśniono, że ideał zewnętrzny nie ma w stopniach 0 i 1 elementów
    niezerowych. Poprawiono odmianę „odwzorowanie ilorazowe”.
11. **Potęgi odwzorowania i dualność zewnętrzna.** Osobno ustalono Λ⁰A=id,
    E₀=id oraz wyznacznik pustej macierzy. Zdefiniowano używaną przestrzeń
    Altᵏ(V;K) i wskazano zerowanie przy k>dim V.
12. **Normalizacje.** Poprawiono jₖ na j₂ przy iloczynie dwóch kowektorów.
    Dopisano ogólną relację Eₖ=k!jₖ po odczytaniu tensorów jako funkcji.
    Wyprowadzono czynnik (k+ℓ)!/(k!ℓ!) przed antysymetryzatorem dla form.
13. **Zmiana współrzędnych pola tensorowego.** Zamiast samej wzmianki
    dodano pełne prawo transformacji, wyprowadzone z reguły łańcucha
    osobno dla wektorów i kowektorów. Przykład y=x² pokazuje czynnik 1/(4y)
    dla dx⊗dx. Wyjaśniono, że wyznacznik różniczki między różnymi włóknami
    wymaga wyborów, choć sama najwyższa potęga zewnętrzna jest kanoniczna.
14. **Cofnięcie i pochodna Liego.** Dodano cofnięcie funkcji i regułę
    F*(fT)=(f∘F)F*T, uzasadniono gładkość cofnięcia i pochodnej Liego.
    Wyjaśniono, że wystarcza rozkład lokalny, bez założenia globalnej bazy.
    Poprawiono gramatykę dowodu kontrakcji; „koneksja (połączenie)”
    uzgadnia terminologię z dalszymi rozdziałami.
15. **Cauchy–Binet i lektura.** Doprecyzowano zakresy indeksów i nawiasy
    wokół podmacierzy AB. Wyjaśniono pustą sumę przy k>n i przypadek k=0.
    Dodano krótką bibliografię na końcu rozdziału, analogicznie do sąsiednich.
    W dowodzie własności wyznacznika poprawiono zgodę gramatyczną:
    „jedna z kolumn”, zamiast „jeden z nich”.

### Kontrola iteracji 3

- Przeczytano cały rozdział: konstrukcje ilorazowe i własności uniwersalne,
  bazy, operacje tensorowe, znaki, wyznacznik, wiązki i pochodną Liego.
- SymPy: sprawdzono relację między wyznacznikiem i antysymetryzacją
  w stopniach 1–4, współczynniki iloczynu form w stopniach (1,2), (2,1)
  i (2,2), wszystkie minory stopnia 2 w przykładzie Cauchy’ego–Bineta
  dla macierzy 3×4 i 4×3 oraz pole równoległoboku równe 5.
- Sprawdzono zgodność kontrakcji ze zmianą współrzędnych tensora (2,1).
  Niezależne różniczkowanie dokładnego cofnięcia przez przepływ ścinania
  Φt(x,y)=(x+ty,y) zgadza się ze wzorem współrzędnym pochodnej Liego
  we wszystkich ośmiu składowych zmiennego tensora (2,1).
- Zakres zmian porównany z `9bfa3af`: źródła rozdziałów 1–2 i 4–18
  są niezmienione. Środowiska LaTeX zbilansowane, brak powtórzonych etykiet
  i odsyłaczy bez celu. `git diff --check` poprawny.
- Zewnętrzny punkt odniesienia dla konstrukcji tensorowych i dualności:
  [B. Conrad, Tensor algebras, tensor pairings, and duality](https://math.stanford.edu/~conrad/diffgeomPage/handouts/tensor.pdf).
- Kontrola wizualna wszystkich 19 stron rozdziału (52–70 PDF).
  Diagram własności uniwersalnej (s. 52) oraz równoległobok (s. 64)
  obejrzano w większej rozdzielczości. Oba są poprawne i czytelne;
  ich geometria nie wymagała zmian.
- Pełny dokument kompiluje się do 277 stron. Brak błędów LaTeX,
  niezdefiniowanych odsyłaczy i ostrzeżeń `Overfull`. Pozostają wcześniejsze
  cztery ostrzeżenia `Underfull` w dalszych rozdziałach i trzy zmiany
  położenia rysunków `h` na `ht`. PDF aktualizowany razem ze źródłem.

## Iteracja 4 — Grassmanniany, algebra Clifforda i spinory

Punkt odniesienia: `02ea77d`. Przeczytano cały rozdział.

### Zmiany i uzasadnienia

1. **Atlas Grassmannianu.** Doprecyzowano zależność map od dopełnienia,
   wybór baz przy wyznacznikach i topologię określoną przez atlas.
   Uzupełniono model rzutów ortogonalnych: otwartość dziedzin map,
   identyfikację z idempotentami samosprzężonymi i dowód zwartości.
2. **Przestrzeń styczna i wiązki.** Dodano argument z lokalną ramką
   dla niezależności identyfikacji od reprezentującej krzywej,
   sprawdzenie różnowartościowości i gładkości izomorfizmu wiązek.
   Poprawiono zapis izomorfizmu wiązki ilorazowej z dopełnieniem
   ortogonalnym oraz odsyłacz do wcześniejszej definicji wiązki normalnej.
3. **Modele jednorodne i Plücker.** Podano lokalne sekcje z procedury
   Grama–Schmidta i lokalną strukturę iloczynową ilorazu grupowego.
   W dowodzie zanurzenia Plückera ilorazy współrzędnych przedłużono
   na otwarte podzbiory przestrzeni otaczającej, co rzeczywiście daje
   lewą odwrotność różniczki. Uzasadniono gładkość modelu z normalnymi.
4. **Algebra Clifforda.** Poprawiono porównanie z algebrą zewnętrzną:
   teraz oba kwadraty dotyczą tego samego wektora. Zdefiniowano
   automorfizm parzystości i rewersję, dowodząc, że przechodzą na iloraz.
   Rewersja jest niezbędna w późniejszym dowodzie jądra nakrycia Spin.
5. **Grupa Spin.** Uzupełniono przejście od lokalnych podniesień obrotów
   do gładkiej struktury grupy i gładkości jej działań. W wymiarze 3
   wyjaśniono, dlaczego każdy jednostkowy biwektor jest iloczynem
   dwóch ortogonalnych wektorów jednostkowych.
6. **Moduły i chiralność.** Doprecyzowano dwuliniowość działania,
   niezerowość modułu nieredukowalnego oraz zależność operatora
   chiralności od orientacji. Dodano projektory na jego podprzestrzenie
   własne i dowód nieredukowalności ograniczeń modułów w wymiarze nieparzystym.
   W uwadze o tych ograniczeniach sprecyzowano n≥3, zgodnie z zakresem
   wcześniej zdefiniowanej grupy Spin. Zredagowano początek dowodu
   kwadratu operatora chiralności, usuwając nierówne odstępy w składzie.
7. **Sfera Blocha.** Dodano jawne współrzędne mapy i jej odwrotności
   oraz rachunek ekwiwariantności z wykorzystaniem projektora rzędu 1.
8. **Struktury spinowe.** Poprawiono indeks ilorazu definiującego
   wiązkę stowarzyszoną (grupa Spin zamiast modułu), podano kierunek
   zmian współrzędnych spinora i rozszerzono definicję na wiązki
   euklidesowe. W konstrukcji na S² ustalono właściwą podgrupę
   stabilizującą e₃ i jej działanie z prawej strony; poprzedni opis
   odwoływał się do stabilizatora zmiennego punktu. Sprawdzono lokalną
   trywialność i zgodność z nakryciem wiązki ramek.
9. **Rachunki algebraiczne.** Uzasadniono alternowanie wzoru na kontrakcję
   w dowodzie bazy algebry Clifforda. W indukcyjnej klasyfikacji algebr
   zespolonych zdefiniowano mnożenie tensorów algebr i podano izomorfizm
   macierzowy przez jednostki macierzowe, zamiast pomijać ten krok.
10. **Podnoszenie i przeszkoda spinowa.** Dodano uzasadnienie podnoszenia
    map z obszarów ściągalnych przez podnoszenie dróg i homotopii.
    Wyjaśniono, dlaczego hipotetyczna struktura spinowa wiązki
    tautologicznej nad S² wymuszałaby zamknięte podniesienie jej przejścia
    na równiku. Poprawiono zdanie, które myliło podnoszenie pętli
    z podnoszeniem samego odwzorowania nakrywającego.
11. **Kryterium znaków.** Podano jawną relację sklejania wiązki głównej
    i wzór na mapę do wiązki ramek. W implikacji odwrotnej podnosimy
    dokładnie ustalone wcześniej ramki. Sprawdzono też niezależność
    przeszkody od zmiany ramek, poza wcześniej opisaną zmianą znaków.
    Wyjaśniono założenie dobrego pokrycia i wskazano, że utożsamienie
    z klasą w H² korzysta z teorii kohomologii Čech, nieudowodnionej tutaj.
12. **Terminologia i redakcja.** Poprawiono „kokykl” na „kocykl”,
    „realna” na „rzeczywista”, „lift” na „podniesienie”, literówki
    i niejasną „wiązkę podstawową” przy zapomnieniu struktury zespolonej.
    Dopisano pozycję dalszej lektury do spisu treści.
13. **Rysunki.** Mapa wykresowa jest teraz rzutem konkretnych płaszczyzn
    liniowych przechodzących przez zero; punkty u i u+Au rzeczywiście
    należą do odpowiednich płaszczyzn, a ich różnica jest pionowym Au.
    W ilustracji iloczynu Clifforda oba wektory jednostkowe mają tę samą
    długość, a rzut i kąt pochodzą z tych samych współrzędnych.
    Na ilustracji nakrycia Spin łuki mają dokładnie 180° i 360°,
    ze strzałkami wewnątrz ścieżek. Normalne n i −n na rysunku orientacji
    mają teraz równe długości.
    Po obejrzeniu PDF odsunięto opisy punktów od krawędzi płaszczyzn
    i poszerzono ramkę na rysunku Blocha, aby mieściła warunek normy 1.

### Kontrola iteracji 4

- Przeczytano wszystkie siedem sekcji rozdziału, w tym dowody bazy
  algebry Clifforda, nakrycia Spin i klasyfikacji modułów.
- Rachunki dokładne w SymPy sprawdzają rzeczywisty i zespolony model
  rzutów Grassmannianu (samosprzężoność, idempotentność, ślad i odwrotną
  mapę wykresową) oraz relację Plückera dla dwupłaszczyzn w wymiarze 4.
- Niezależna implementacja mnożenia uporządkowanych słów Clifforda
  sprawdza znaki w wymiarach 2–6, kwadrat i antykomutację chiralności,
  rewersję i działanie jawnego rotora na parze wektorów jednostkowych.
  Sprawdzono też rekurencję macierzy Pauliego w wymiarach 2, 4 i 6,
  normę mapy Blocha, wzór projektora i znak działania obrotu.
- Zweryfikowano dokładne współrzędne poprawionej ilustracji wykresu.
  Obejrzano wszystkie 17 stron rozdziału (71–87 PDF) oraz osobno
  pięć ilustracji w większej rozdzielczości; po poprawkach etykiet
  ponowiono kontrolę odpowiednich stron.
- Zakres porównany z `02ea77d`: rozdziały 1–3 i 5–18 są niezmienione.
  Środowiska LaTeX zbilansowane, etykiety niepowtórzone, wszystkie
  odsyłacze rozdziału mają cel. `git diff --check` poprawny.
- Punkty odniesienia: [B. Conrad, Clifford algebras and spin groups](https://math.stanford.edu/~conrad/210CPage/handouts/clifford.pdf)
  oraz [K. Wernli, Lecture Notes on Spin Geometry, §2.3](https://arxiv.org/pdf/1911.09766).
  Sprawdzono zgodność kryterium znaków z opisem przeszkody w₂;
  własny dowód sklejania podano jawnie w tekście.
- Pełny dokument ma 280 stron. Brak błędów LaTeX, niezdefiniowanych
  odsyłaczy i ostrzeżeń `Overfull`. W rozdziale 4 brak `Underfull`;
  pozostają trzy takie ostrzeżenia w dalszych rozdziałach oraz trzy
  wcześniejsze zmiany położenia rysunków `h` na `ht`.
  PDF jest aktualizowany razem ze źródłem.

## Iteracja 5 — Algebra homologiczna: moduły, kompleksy i (ko)homologie

Punkt odniesienia: `831cbcc`. Przeczytano wszystkie dziesięć sekcji.

### Zmiany i uzasadnienia

1. **Moduły wolne.** Naprawiono dowód niewolności Z/mZ: poprzedni
   zakładał, że [1] należy do hipotetycznej bazy. Teraz rozwijamy [1]
   w dowolnej bazie i wykorzystujemy jednoznaczność współczynników.
   Dodano niezbędne założenie m≥2.
2. **Podstawowe konstrukcje.** Wyjaśniono rolę przemienności pierścienia
   w strukturze modułu Hom i zdefiniowano sumę prostą z jej włączeniami
   i rzutami. W dowodzie rozszczepienia zapisano retrakcję jako konkretne
   złożenie, usuwając niejasny kierunek izomorfizmu.
3. **Długi ciąg homologii.** Naprawiono końcowy argument: H₋₁(A)=0
   wynika z A₋₁=0, a nie z C₋₁=0. Założenie twierdzenia pozostaje to samo.
   „Niezależność od [c]” zastąpiono niezależnością od reprezentanta [c];
   wynik oczywiście zależy od klasy.
   W uwadze o naturalności określono wszystkie trzy odwzorowania
   między krótkimi ciągami i wymagane równości przemienności.
4. **Kohomologia i naturalność.** Uzupełniono zgodność homomorfizmu
   łączącego z mnożeniem przez skalary i jego naturalność. W twierdzeniu
   o dualności nad ciałem dodano rachunek naturalności ewaluacji.
5. **Homotopie.** Wymagamy jawnie, aby hₙ były homomorfizmami modułów,
   a f i g odwzorowaniami łańcuchowymi. Bez pierwszego warunku późniejszy
   przykład kompleksu acyklicznego, lecz nieściągalnego nie działałby.
   W dowodzie kasowania pary przedłużono homotopię na cały kompleks
   i podano id−jp=∂h+h∂ oraz pj=id, uzasadniając zastosowanie twierdzenia.
6. **Ilorazy i suma kompleksów.** Rozróżniono klasę c modulo podkompleks
   od jej klasy homologii. Doprecyzowano, że używana filtracja jest
   skończona i rosnąca. W dowodzie Mayera–Vietorisa uzasadniono
   Hₙ(A⊕B)≅Hₙ(A)⊕Hₙ(B) przez cykle, brzegi i ich ilorazy.
7. **Redukcja modulo m.** Dodano jawny wzór na ostatnią strzałkę:
   ∂c=ma prowadzi do [a]. Wyjaśniono jednoznaczność a, warunek bycia
   cyklem, m-torsję oraz naturalność. Wstęp do sekcji ograniczono
   do kompleksów wolnych grup, zgodnie z założeniem twierdzenia.
8. **Tensorowanie modułów.** Uzupełniono brakującą konstrukcję nad
   pierścieniem: iloraz modułu wolnego przez relacje dwuliniowości,
   własność uniwersalną, rozszerzenie skalarów i bazę modułu po tej
   operacji. Uzasadniono zachowanie sum prostych i izomorfizmów.
   To wyjaśnia operacje potrzebne w istniejącym dowodzie zmiany
   współczynników; wcześniejszy rozdział dotyczył tensorowania nad ciałem.
9. **Charakterystyka zero.** Zdefiniowano zapis Hₙ(C;Z), poprawność
   różniczki po tensorowaniu, pełną mapę [c]⊗q↦[c⊗q] i reprezentowanie
   dowolnego tensora przez wspólny mianownik. Zapisano oba kierunki
   izomorfizmu rozszerzenia skalarów Z→Q→F i wyjaśniono kanoniczność
   wyniku mimo wyboru dopełnień. Usunięto niepasujący zapis Hₙ(D;Q)
   dla kompleksu D, który już jest racjonalny.
10. **Terminologia i skład.** W całym rozdziale zastąpiono „kokykl”
    przez „kocykl” oraz „lift” przez „podniesienie”, z poprawną odmianą.
    Zamiast „n-ta homologia” piszemy „homologia stopnia n”. Poprawiono
    zgodę gramatyczną kilku zdań i dodano dalszą lekturę do spisu treści.
    W diagramie podnoszenia krótki podpis „wybór b” mieści się nad strzałką.

### Kontrola iteracji 5

- Cały rozdział przeczytano i sprawdzono matematycznie: definicje modułów,
  dokładność, oba długie ciągi, dualność, kasowanie pary, filtracje,
  Mayer–Vietoris, zmiana współczynników, Euler i lemat pięciu.
- Dla kompleksów Z —k→ Z sprawdzono 64 pary k,m∈{2,…,9}:
  wzór homomorfizmu łączącego, jego addytywność, obraz równy m-torsji
  i rozmiary jąder/ilorazów. Obejmuje to złożone m, a nie tylko ciała.
- Na kompleksie Z→Z³→Z² z macierzami ∂₂=(−6,3,0)ᵀ,
  ∂₁=((1,2,3),(2,4,8)) sprawdzono dokładnie całkowite zmiany baz,
  oddzielenie pary, zgodność rzutów z różniczkami i tożsamość homotopii.
  Po przejściu do Q sprawdzono homologię, kohomologię dualną i Eulera.
- Przykład Mayera–Vietorisa zweryfikowano nad F₂, F₃, F₅ i F₇:
  obraz klasy u+v jest x−y i daje wymagane jądro następnej mapy.
- Obejrzano wszystkie 17 stron rozdziału (88–104 PDF) i osobno diagram
  odwzorowania łączącego na stronie 93. Geometria diagramu była poprawna;
  zmieniono tylko podpis na polski. Pozostały układ jest czytelny.
- Porównanie z `831cbcc` potwierdza, że rozdziały 1–4 i 6–18 nie zostały
  zmienione. Środowiska LaTeX są zbilansowane, etykiety niepowtórzone,
  odsyłacze mają cele. `git diff --check` poprawny.
- Punkty odniesienia: [The Stacks Project, Complexes](https://stacks.math.columbia.edu/tag/010V)
  oraz [Tensor products](https://stacks.math.columbia.edu/tag/00CV).
  Sprawdzono wymaganie liniowości homotopii i zakres konstrukcji tensorowej.
- Pełny dokument kompiluje się do 281 stron, bez błędów, niezdefiniowanych
  odsyłaczy i `Overfull`. Brak ostrzeżeń `Underfull` w rozdziale 5;
  pozostają trzy wcześniejsze w dalszych rozdziałach i trzy zmiany `h` na `ht`.
  PDF aktualizowany wraz ze źródłem.

## Iteracja 6 — Homotopia, nakrycia i komórkowe modele przestrzeni

Status: sprawdzono i poprawiono wszystkie 5 sekcji oraz 6 ilustracji.
Data zakończenia: 2026-10-01.

Przegląd rozpoczęto od `4f017f4`. W jego trakcie, na prośbę użytkownika,
wykonano pull trzech commitów Darka, do `5b259e6`; ten commit jest
końcowym punktem odniesienia iteracji. Niezacommitowane zmiany rozdziału 6
zabezpieczono w stashu i przywrócono bez konfliktów. Przeczytano cały
rozdział i źródła sześciu rysunków.

**Drobna naprawa po pullu poza rozdziałem 6.** W przykładzie „Prosta
z podwojonym początkiem” w rozdziale 1 przywrócono widoczne klamry zbiorów
(`\{…\}` zamiast grupujących `{…}`) i zapis `{[x]: x∈I, x≠0}`.
Pobrany zapis błędnie umieszczał klasę [x] w przedziale liczb rzeczywistych.
Zachowano nowe nawiasy w definicji relacji równoważności i wszystkie
pozostałe zmiany merytoryczne oraz redakcyjne Darka.

### Zmiany i uzasadnienia

1. **Homotopie i retrakty.** Dodano jawne wymagania ciągłości f,g,H
   w definicjach. Zbiór wypukły uznano za ściągalny przy niezbędnym
   założeniu niepustości. Wyjaśniono, że homotopia dróg jest relacją
   równoważności. Poprawiono zdanie o parametrze czasu.
2. **Punkt bazowy.** Wyjaśniono, dlaczego obraz brzegu kwadratu jest
   homotopijny do stałej z ustalonym narożnikiem. W dowodzie niezmienniczości
   π₁ rozróżniono drogę fu od drogi otrzymanej z homotopii fg≃id:
   mają te same końce, ale nie muszą być równe; podano potrzebne złożenie
   izomorfizmów zmiany punktu bazowego.
3. **Podnoszenie.** Doprecyzowano homeomorfizmy na arkuszach i podano
   dowód lematu o liczbie Lebesgue’a, używanego przy podziale odcinka
   i kwadratu. W kryterium podnoszenia uzasadniono równość końców
   przez odwrócenie drugiej części podniesionej pętli i jednoznaczność.
4. **Warunek półlokalny.** Poprawiono tytuł definicji i określono ją
   dla pętli opartych w rozważanym punkcie. Wyjaśniono zmianę punktu
   bazowego w łukowo spójnym otoczeniu, potrzebną w konstrukcji nakrycia.
5. **Nakrycie uniwersalne.** Sprawdzono aksjomat bazy topologii dla
   przecięcia arkuszy nad różnymi U,U′ oraz ciągłość i otwartość mapy
   na każdym arkuszu, zamiast tylko postulować homeomorfizm.
6. **Klasyfikacja nakryć.** Udowodniono wolność działania, rozłączność
   przesunięć arkusza i otwartość projekcji na orbity. Sama wolność
   działania nie gwarantuje nakrycia. Wykazano, że iloraz realizuje
   dokładnie zadaną podgrupę. Przy porównaniu z dowolnym nakryciem
   uzasadniono surjektywność oraz równoważność włókien i orbit.
   Opisano sprzężenie podgrupy przy zmianie punktu nad bazą i jego odwrotność.
7. **Van Kampen.** Rozwinięto opis iloczynu wolnego i jego własności
   uniwersalnej. Naprawiono punkt bazowy pętli porównującej drogi
   pomocnicze: używamy λ′ⱼ*λ̄ⱼ, z początkiem w x₀. Dowód jądra
   zapisano przez drogi do wszystkich wierzchołków siatki, elementy
   przypisane krawędziom i relacje wokół prostokątów. Sprawdzono zgodność
   na wspólnych krawędziach oraz odtworzenie początkowego słowa.
8. **Sympleksy.** Rozróżniono ściany kowymiaru jeden od ogólnych ścian,
   osobno określono pusty brzeg Δ⁰. Usunięto literówkę „afininicznej”.
   W homeomorfizmie z dyskiem dodano jawne przedłużenie radialne
   i kontrolę ciągłości w środku. Definicja triangulacji zaznacza
   używany zakres skończony, więc nie sugeruje objęcia przestrzeni niezwartych.
9. **Δ-kompleksy i CW.** Doprecyzowano warunek Hausdorffa i ciągłość map
   charakterystycznych, zgodność kolejności wierzchołków ścian oraz
   topologię ilorazową także dla nieskończonej sumy sympleksów.
   Dla torusa podano oba porządki wierzchołków. W definicji CW poprawiono
   równoważność definiującą topologię słabą, gramatykę i nazwę warunku
   skończoności domknięć. Wyjaśniono argument o zwartej sumie sympleksów
   i topologii ilorazowej skończonej realizacji.
10. **Dołączanie komórek.** Sprawdzono osadzenie Y jako podzbioru
    domkniętego i otwarte osadzenie wnętrza komórki. W dowodzie zmiany π₁
    podano wzór homotopii pasa przy brzegu, uzasadniono ciągłość przy Y
    przez otoczenia zawierające całe odcinki radialne i sprawdzono
    otwartość obu zbiorów użytych w twierdzeniu van Kampena.
11. **Płaszczyzna rzutowa.** Uzasadniono homeomorfizm [z]↦z² na
    okręgu z utożsamionymi antypodami i wynikającą z niego relację a²=1.
    Zamiast niewprowadzonego jeszcze stopnia mapy użyto liczby owinięć.
    Niejasne porównanie z podgrupą indeksu 2 zastąpiono opisem roli brzegu komórki.
12. **Rysunki i redakcja.** Dodano kierunek przekątnej torusa i usunięto
    niezwiązane z matematyką zdanie o kratkowanym tle. Na rysunku szkieletów
    strzałka wskazuje właściwą 1-komórkę. W rysunku D²/∂D² strzałka
    ma oznaczenie mapy ilorazowej q: wcześniejsze φ było zdefiniowane
    tylko na brzegu, a strzałka dotyczyła całego dysku. Doprecyzowano podpis.
    Nakrycie okręgu przedstawiono jako linię śrubową (zamiast „spirali”).
    Dalszą lekturę dodano do spisu treści.

### Kontrola iteracji 6

- Przeczytano cały rozdział, w tym definicje, dowody i przykłady.
  Sprawdzono kolejność wprowadzania pojęć oraz zależności między dowodami.
- Niezależnie sprawdzono rachunek słów przy zmianie dróg pomocniczych
  i identyfikacji orbit w nakryciu. Dla siatek 1×1, 2×3 i 5×4 sprawdzono,
  że przesuwanie drogi przez prostokąty przechodzi przez każdą komórkę
  dokładnie raz i zachowuje końce drogi.
- Symbolicznie sprawdzono warunki końcowe homotopii radialnej,
  normę odwzorowania dysku na sferę i granicę w środku dysku.
  Dla sympleksów wymiarów 1–4 sprawdzono przecięcia promieni z brzegiem
  w zestawie kierunków o współrzędnych całkowitych. Zweryfikowano
  orientacje ścian obu trójkątów torusa i zgodność liczby komórek.
  Są to kontrole pomocnicze; ogólne uzasadnienia pozostają w tekście.
- Obejrzano wszystkie 14 stron rozdziału (105–118 PDF), a sześć rysunków
  dodatkowo w większej rozdzielczości (strony 106, 108, 113, 115 i 116).
  Sprawdzono czytelność podpisów, kierunki strzałek i wskazania komórek.
  Obejrzano także poprawiony zapis przykładu z rozdziału 1 na stronie 6.
- Porównanie z `5b259e6` potwierdza brak zmian w rozdziałach 2–5 i 7–18.
  Jedyny wyjątek poza rozdziałem 6 to opisana wyżej naprawa notacji
  w pobranym przykładzie z rozdziału 1. Środowiska LaTeX są zbilansowane,
  etykiety niepowtórzone, a odsyłacze mają cele.
- Punkty odniesienia: [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
  rozdział 1 (van Kampen, podnoszenie, konstrukcja i klasyfikacja nakryć),
  oraz [materiały UW o CW-kompleksach](https://www.mimuw.edu.pl/~sjack/ta/5_cw_grupy_homotopii_jhcw.pdf)
  (definicje i terminologia).
- Pełny dokument kompiluje się do 283 stron. Końcowy przebieg nie zgłasza
  błędów, niezdefiniowanych odsyłaczy, potrzeby ponownej kompilacji ani
  `Overfull`. Pozostają trzy wcześniejsze ostrzeżenia `Underfull`
  w dalszych rozdziałach i trzy zmiany położenia ilustracji z `h` na `ht`.
  PDF zaktualizowano wraz ze źródłem; `git diff --check` poprawny.

Następna iteracja: rozdział 7 — „Homologia przestrzeni”.

## Iteracja 7 — Homologia przestrzeni

Status: sprawdzono i poprawiono wszystkie 8 sekcji oraz 3 ilustracje.
Data zakończenia: 2026-10-01.

Punkt odniesienia: `21a3ecb`. Przed rozpoczęciem wykonano pull;
gałąź była aktualna. Przeczytano cały rozdział: osiem sekcji i trzy ilustracje.

### Zmiany i uzasadnienia

1. **Orientacja i składowe.** W dowodzie opisu H₀ symplicjalnego
   podano argument z otwartymi i domkniętymi realizacjami składowych
   grafu krawędzi. Samo stwierdzenie, że sympleksy są spójne, nie wyjaśniało
   wystarczająco przejścia od drogi ciągłej do drogi po krawędziach.
   Ujednolicono „składowe łukowe” z poprzednim rozdziałem.
2. **Operator pryzmatyczny.** Rozpisano osobno znaki ścian bocznych
   dla j<i i j>i oraz kasowanie ściany między dwiema sąsiednimi częściami.
   Określono P₋₁=0. Poprawiono błędną odmianę „afininiczną posyłającą”.
3. **Homologia zredukowana.** Zdefiniowano ją jednolicie przez kompleks
   augmentowany, także dla przestrzeni pustej. Wzór Z^(c−1) ograniczono
   do skończonej liczby składowych; dla dowolnej liczby podano bazę
   różnic klas i sumę prostą. Uzasadniono zredukowany ciąg pary,
   używany następnie do obliczenia homologii dysku względem brzegu.
4. **Podział barycentryczny.** Ustalono kolejność barycentrów według
   wymiarów ścian i podano sumę po permutacjach ze znakiem permutacji.
   W łańcuchach singularnych zmiana parametryzacji nie jest formalnie
   mnożeniem przez −1; wspólne ściany muszą mieć identyczną parametryzację.
   Rozpisano kasowanie ścian wewnętrznych i znaki ścian zewnętrznych.
5. **Homotopia podziału i małe łańcuchy.** Zastąpiono nieokreślony zapis
   tₙ₋₁(∂uₙ) sumą obrazów przez włączenia ścian. Dodano wzór stożka
   singularnego i sprawdzenie ciągłości w jego wierzchołku. Wyjaśniono
   stopień zero. Oszacowanie zmniejszenia średnicy wyprowadzono ze wzoru
   na barycentra dwóch zagnieżdżonych ścian.
6. **Porównanie z modelem symplicjalnym.** Podkreślono, że mapa porównawcza
   używa wybranych uporządkowanych generatorów i rozszerzenia liniowego,
   a nie dowolnego odwracania parametryzacji. W dowodzie indukcyjnym
   wykazano, że mapa par przenosi generator na generator przez
   homeomorfizm ilorazów; sam fakt, że obie grupy są Z, nie wystarcza.
7. **Iloraz pary komórkowej.** Dodano niezbędne założenie A≠∅ oraz
   uzasadnienie ciągłości homotopii na ilorazie z parametrem czasu.
   Użyto domkniętości projekcji i zwartości jej włókien. Rozszerzono
   konstrukcję otoczenia na dołączenie jednej komórki, potrzebne w dowodzie
   porównania. Wyjaśniono ciągłość radialnej retrakcji przy sklejanym A.
   Poprawiono zdanie utożsamiające pełne kompleksy z modelami małych
   łańcuchów: lemat zapewnia tu izomorfizm homologii.
8. **Generator sympleksu i bukiet sfer.** Skonstruowano konkretne otwarte
   pokrycia oraz retrakcje części i przecięć do użycia w Mayerze–Vietorisie.
   Używanie bezpośrednio domkniętych części nie wynikało z wcześniejszej
   wersji tego twierdzenia. W warstwie komórek obsłużono pusty szkielet.
9. **Homologia komórkowa i stopień.** Oddzielono przypadek n=1 w dowodzie
   ∂²=0, unikając niezdefiniowanych map w stopniach ujemnych. Uzasadniono
   deg(z↦zʳ)=r przez konkretny singularny trójkąt realizujący dodawanie
   klas pętli, odwrotność pętli i generator z Mayera–Vietorisa.
   We wzorze brzegu komórkowego określono orientacje sfer dziedziny
   i obrazu zgodnie z orientacjami komórek; to ustala znaki stopni.
10. **Współczynniki.** Zdefiniowano łańcuchy z wartościami w R i wyjaśniono,
    dlaczego konstrukcje pryzmatu, podziału, ciągów par i szkieletów działają
    także nad pierścieniem. Wykorzystano rozszczepienie odpowiednich ciągów
    w każdym stopniu, bez zakładania dokładności dowolnego tensorowania.
    Uzasadnia to w szczególności podany w skrypcie rachunek RP² modulo 2.
    Wyjaśnienie wydzielono do osobnej uwagi przed przykładem.
11. **Lokalna homologia.** Rozróżniono otoczenie U w rozmaitości od kuli
    Bᵐ będącej obrazem mapy. Retrakcję otwartej kuli bez środka skierowano
    na sferę o promieniu 1/2: jednostkowa sfera nie należy do otwartej kuli.
12. **Rysunki i język.** Na ilustracji singularnego sympleksu zaznaczono
    trzy obrazy wierzchołków i trzy skierowane części brzegu; wypełnienie
    ma teraz dokładnie ten sam brzeg co strzałki. W diagramie torusa
    „wnętrze torusa” zastąpiono „jedna 2-komórka”. Poprawiono m.in.
    „dowolna ciągłe”, „homologa punktu”, „fundament dysku”, „nie koniecznie”,
    odmianę słowa „odwzorowanie” i odsyłacze nazywające sekcje rozdziałami.
    Dalszą lekturę dodano do spisu treści.

### Kontrola iteracji 7

- Niezależnie obliczono brzegi uporządkowanych sympleksów afinicznych
  w wymiarach 0–5, traktując różne parametryzacje jako różne generatory.
  Sprawdzono ∂²=0, ∂S=S∂ i tożsamość operatora pryzmatycznego.
  Nie upraszczano sympleksów przez zamianę orientacji ani nie usuwano
  generatorów zdegenerowanych, co mogłoby ukryć błąd znaku.
- W wymiarach 1–4 skonstruowano łańcuchy homotopii stożkowej
  i sprawdzono dokładnie ∂T+T∂=S−id. Sprawdzono też ich obrazy
  przez nieróżnowartościowe odwzorowania afiniczne.
- Z porządków wierzchołków obu trójkątów torusa niezależnie otrzymano
  macierz brzegu i jej postać Smitha: H₁=Z², H₂=Z, zgodnie z modelem CW.
  Dla RP² sprawdzono torsję całkowitą oraz jądra i ilorazy mnożenia
  przez 2 nad Z/m dla m=2,3,4,5,7. Kontrole te uzupełniają ogólne dowody.
- Obejrzano wszystkie 14 stron rozdziału (119–132 PDF), a rysunki
  na stronach 120, 121 i 130 także w większej rozdzielczości.
  Po końcowych poprawkach sprawdzono ponownie zmieniony skład.
- Porównanie z `21a3ecb` potwierdza, że pozostałe rozdziały są bez zmian.
  Środowiska LaTeX są zbilansowane, etykiety unikalne, odsyłacze mają cele;
  `git diff --check` nie wykazał problemów.
- Punktem odniesienia był [Allen Hatcher, Algebraic Topology, rozdział 2](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf):
  podział barycentryczny, homologia ilorazu dobrej pary i model komórkowy.
- Pełny dokument skompilowano lokalnie do 285 stron. Końcowy przebieg
  nie zgłasza błędów, niezdefiniowanych odsyłaczy, potrzeby ponownej
  kompilacji ani `Overfull`. Pozostały trzy wcześniejsze `Underfull`
  poza rozdziałem 7 i trzy zmiany położenia ilustracji z `h` na `ht`.
  Próba wbudowanego kompilatora edytora zwróciła status nieznany;
  potwierdzona kompilacja i dostarczony PDF pochodzą z lokalnego MiKTeX.
  PDF zaktualizowano wraz ze źródłem.

Następna iteracja: rozdział 8 — „Wyższe grupy homotopii i związek z homologią”.

## Iteracja 8 — Wyższe grupy homotopii i związek z homologią

Status: sprawdzono i poprawiono wszystkie 7 sekcji merytorycznych oraz 4 ilustracje.
Data zakończenia: 2026-10-02.

Punkt odniesienia: `3e871f0`. Pull przed rozpoczęciem nie pobrał nowych zmian.
Przeczytano cały rozdział: siedem sekcji merytorycznych, zakończenie i cztery rysunki.

### Zmiany i uzasadnienia

1. **Definicje i punkty bazowe.** Zastąpiono nieokreślone „dobrze wskazane
   topologicznie” wyborem punktu bazowego; w argumentach komórkowych jest
   on wierzchołkiem. Ujednolicono „spójność łukową”. Wyjaśniono zależność
   zmiany punktu bazowego od klasy drogi i zgodność z homotopią, która
   porusza bazę; jest to potrzebne przy przybliżaniu słabej równoważności.
2. **Eckmann–Hilton.** Rozpisano podstawienia elementu neutralnego.
   Oddzielono równość map na czterech ćwiartkach od równości klas po
   usunięciu stałych połówek. Te drugie wymagają zmiany parametryzacji.
3. **Ciąg względny.** W dokładności przy πₙ(X) wykorzystano konkretną
   ścianę homotopii zerującej i dwie drogi w kwadracie parametrów.
   Rozpisano koniec ciągu jako ciąg zbiorów wskazanych i dowód naturalności.
   W definicji spójności par zaznaczono wszystkie punkty bazowe w A.
4. **Nieskończone CW.** Dodano dowód, że zwarty podzbiór leży w skończonym
   podkompleksie. Wyjaśniono ilorazowość iloczynu z przedziałem i wynikające
   z niej kryterium ciągłości homotopii na wszystkich komórkach.
   Uzasadniono komórkową homologię par przez iloraz kompleksów i lemat pięciu,
   a następnie przejście z homologii skończonych CW do dowolnych CW.
   Rozdział 7 dowodził wcześniej twierdzenia jedynie w zakresie skończonym.
5. **Przybliżenie komórkowe.** Wypełniono techniczną lukę: zwarte K,
   wielościenne otoczenie P, interpolacja afiniczna, funkcja odcinająca
   i kontrola błędu zapewniają punkt pominięty przez cały nowy obraz,
   także poza obszarem przybliżania. Opisano kolejność usuwania komórek.
   W równych wymiarach wybór punktu poza obrazami ścian i części niższego
   rzędu daje skończone przeciwobrazy z lokalnymi znakami; ten wariant
   uzasadnia późniejsze liczenie komórek w dowodzie Hurewicza.
6. **Szkielety i homotopie nieskończone.** Przed względnym przybliżaniem
   dysku przybliżono jego brzeg i użyto HEP. Wcześniej brzeg nie musiał być
   komórkowy, więc nie można było zachować go i otrzymać obrazu w Xⁱ.
   Dla kolejnych etapów podano przedziały czasu i sprawdzono ciągłość
   w chwili granicznej na każdej komórce z całym przedziałem.
7. **Nakrycia i H₁.** Podnoszenie homotopii wyprowadzono z kryterium dla
   jednospójnego Sⁿ×I; wyjaśniono stałość bazy w dyskretnym włóknie.
   W dowodzie Hurewicza w stopniu 1 dopisano niezmienniczość względem
   homotopii pętli. Kasowanie dróg pomocniczych odbywa się w łańcuchach
   modulo brzegi, nie w „klasach” pojedynczych niezamkniętych dróg.
8. **Ściskanie i Whitehead.** Podano jawny wzór kołnierza unieruchamiającego
   cały brzeg dysku podczas homotopii. Oddzielono pustą przestrzeń i stopień 1,
   gdzie zamiast argumentu dla grup potrzebny jest rachunek dróg.
   Opisano komórki cylindra odwzorowania i jawną odwrotność homotopijną.
9. **Pierwsze komórki.** Uzasadniono abelowość π₂(W,A) przy jednospójnym A,
   doprowadzanie dysków do bazy, lokalne znaki i rozcinanie wzdłuż drzewa.
   Dla relacji od wyższych komórek wskazano, że drogi doprowadzające leżą
   w W, które też jest jednospójne. Poprawiono Zⁿ⁺¹ na A∪Zⁿ⁺¹ tam,
   gdzie A może mieć komórki wyższych wymiarów. Dodano surjektywność
   przed opisem jądra oraz sens obrazu klas dołączających w grupie względnej.
10. **Model Hurewicza.** Dodano osobny wniosek o zabijaniu wybranych klas
    z dowodem z ciągu pary. W kolejnych etapach bazą jest cały aktualny
    model, a nie punkt: lemat o pierwszych komórkach z bazą punktową
    nie miałby wtedy wymaganych założeń. Sprawdzono stabilizację grup,
    komórkowość map dołączających i przejście do nieskończonego modelu.
11. **Względny Hurewicz i przykłady.** W porównaniu ciągów osobno obsłużono
    π₂ i względny stopień 1. Ustalono zgodne orientacje dla map Hurewicza,
    ograniczono względny homomorfizm do n≥2 i opisano addytywność.
    W przykładzie dysku chodzi o reprezentanta generatora, nie każdej klasy.
    Wyjaśniono oparte i nieoparte mapy sfer. W kompleksie Moore’a zaznaczono
    także C₀. Dla nakrycia S¹∨S² podano bezpośredni model CW i uzasadnienie
    jednospójności, bez nieuzasadnionego zwijania nieskończonej prostej.
12. **Język i ilustracje.** Poprawiono odmianę słowa „odwzorowanie”,
    „antipodalne” na „antypodalne”, niejasne użycie słowa „baza” i wymiar
    sfery jako brzegu dysku. Rysunek względnego dysku pokazuje A jako pas
    zawierający obraz brzegu, a wnętrze obrazu może wyjść poza A.
    W nakryciu bukietu usunięto szczelinę między sferami i prostą.
    Wycentrowano pionowy podpis kierunku sklejania i przeniesiono
    oznaczenie utożsamienia w cylindrze ponad rysunek, poza tekst objaśnienia.
    Zakończenie i dalszą lekturę dodano do spisu treści.

### Kontrola iteracji 8

- Przejrzano kolejność zależności: zwarte obrazy i iloczyn z przedziałem
  poprzedzają HEP oraz przybliżenie komórkowe; Whitehead poprzedza budowę
  modelu; lemat o pierwszych komórkach poprzedza zabijanie klas i Hurewicza.
  Lokalny argument afiniczny nie korzysta z twierdzenia Sarda ani z
  twierdzenia Hurewicza, które dopiero ma być udowodnione.
- Sprawdzono wzory Eckmanna–Hiltona na 441 parach wymiernych parametrów,
  także na liniach sklejania, zachowując współrzędne wewnątrz każdej ćwiartki.
  Rachunek potwierdza równość map używaną przed przejściem do klas.
- Dla retrakcji HEP sprawdzono na tej samej siatce, że obraz leży
  na dole lub boku cylindra, współrzędne pozostają w dozwolonym zakresie,
  a zadany podzbiór jest nieruchomy. Symbolicznie sprawdzono zgodność
  czasów obu wzorów kołnierza i jego promienie końcowe.
- Dla skończonych fragmentów nakrycia z 3,5,…,13 sferami niezależnie
  obliczono macierze brzegów: H₀=Z, H₁=0, a H₂ ma po jednym generatorze
  na sferę. Rzut sumujący współczynniki ma rangę 1. Sprawdzono też
  ilorazy Smitha dla kompleksów Moore’a o m=2,3,5,7.
  Te kontrole są pomocnicze; argumenty ogólne, w tym przejście do
  nieskończonego nakrycia, pozostają w tekście.
- Obejrzano wszystkie 15 stron rozdziału (133–147 PDF). Cztery rysunki
  na stronach 134, 135, 141 i 147 sprawdzono także w większej rozdzielczości,
  a po zmianie położenia podpisów ponownie obejrzano dwa zmienione rysunki.
- Kontrola zakresu względem `3e871f0` potwierdziła brak zmian w pozostałych
  rozdziałach. Środowiska LaTeX są zbilansowane, etykiety niepowtórzone,
  odsyłacze mają cele. `git diff --check` poprawny.
- Punkty odniesienia: [Hatcher, rozdział 4](https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf)
  oraz [dodatek o CW](https://pi.math.cornell.edu/~hatcher/AT/ATapp.pdf)
  (w szczególności skończone podkompleksy zawierające zwarte obrazy).
- Pełny PDF ma 288 stron. Kompilację potwierdzono lokalnym MiKTeX;
  wbudowany kompilator edytora ponownie zwrócił status nieznany.
  Nie ma błędów ani `Overfull`. Pozostały dwa wcześniejsze `Underfull`
  w późniejszych rozdziałach i trzy zmiany położenia ilustracji `h` na `ht`.
  Poprzednie ostrzeżenie `Underfull` w rozdziale 8 zniknęło po redakcji.
  PDF zaktualizowano razem ze źródłem.

Następna iteracja: rozdział 9 — „Formy różniczkowe, orientacja i kohomologia de Rhama”.

## Rozdział 9 — formy, orientacja i kohomologia de Rhama (2026-10-02)

Punkt wyjścia: `f7df0ae`. W trakcie przeglądu pobrano także commit Darka
`0d9857f` („Uzupelnienie dowodow i przykladow do przestrzeni stycznej.”).
Przywrócenie lokalnych zmian po aktualizacji przebiegło bez konfliktów.
Kontrola względem `0d9857f` potwierdza zachowanie jego zmian w całości;
nasze poprawki tej iteracji dotyczą wyłącznie rozdziału 9.
Przegląd i poniższe kontrole rozdziału 9 zakończono.
Nowe uzupełnienia Darka z rozdziału 1 zachowano; ich osobny ponowny
przegląd merytoryczny należy uwzględnić w końcowej kontroli zmian
powstałych po wcześniejszych iteracjach.

### Dowód de Rhama i całkowanie po sympleksach

- Poprawiono definicję gładkiego sympleksu dla rozmaitości z brzegiem.
  Przedłużamy jego składowe we współrzędnych do przestrzeni euklidesowej;
  nie wymagamy przedłużenia o wartościach w samej półprzestrzeni.
  Wcześniejsze sformułowanie wykluczało np. gładki odcinek t ↦ t
  zaczynający się na brzegu półprostej.
- Zastąpiono nieuzasadnione rozcinanie sympleksu na części z gładkim
  brzegiem lokalnym dowodem Stokesa w narożach. Każda współrzędna
  półprzestrzeni daje wkład jednej ściany; przecięcia ścian mają w nich
  miarę zero. Wyjaśniono zgodność orientacji ścian ze znakami (−1)^j.
- Usunięto sugestię, że można niezależnie wygładzać poszczególne
  sympleksy ciągłe przy definiowaniu kołańcucha całkowania. Bez zgodności
  na ścianach taki wybór nie definiuje odwzorowania kompleksów.
- Przepisano dowód porównania trzech kompleksów: form, gładkich
  kołańcuchów singularnych oraz wszystkich kołańcuchów singularnych.
  Izomorfizm ograniczenia z ciągłych do gładkich kołańcuchów otrzymujemy
  równocześnie z izomorfizmem całkowania, zamiast powoływać się na
  niedowiedzione wygładzanie względne przy narożach.
- Uzupełniono algebrę kompleksu podwójnego: znaki różniczki całkowitej,
  usuwanie składników kocyklu w dokładnych kolumnach, kryterium
  izomorfizmu przez stożek odwzorowania oraz rolę skończonych przekątnych.
  Dokładność wierszy jest uzasadniona osobno dla form (podział jedności)
  i kołańcuchów (wybór indeksu zawierającego mały sympleks).
- Wyeliminowano odwołanie do silnie wypukłych kul geodezyjnych i
  nieuzasadnionych „półkul” przy brzegu. Dwukrotne sklejanie wystarcza:
  najpierw prostokąty w dowolnym otwartym podzbiorze przestrzeni lub
  półprzestrzeni, następnie dziedziny map na rozmaitości. Ich przecięcia
  nie muszą być ściągalne. Dowód nie używa pojęć z późniejszych rozdziałów.
- Wyjaśniono dualizację nad R także w nieskończonym wymiarze oraz
  wynikającą stąd możliwość zastąpienia całego cyklu gładkim cyklem.
  Niezależność okresów wynika z istnienia gładkiego łańcucha między
  takimi reprezentantami i ze Stokesa.

### Pozostałe dowody, założenia i terminologia

- W dowodzie jednoznaczności różniczki zewnętrznej najpierw wykazano
  lokalność za pomocą pojedynczej funkcji odcinającej. Dopiero to pozwala
  stosować warunki określające globalny operator do lokalnych współrzędnych.
- Dodano konwencję zerowych form w ujemnych stopniach i przypadek k=0
  operatora homotopii. Wyjaśniono gładkość homotopii przy narożach iloczynu.
- Dla definicji pochodnej Liego przez dwustronny przepływ wymagamy
  styczności pola do brzegu. Dla dowolnego pola wskazano definicję przez
  wzór Cartana i jednoznaczne przedłużenie z wnętrza. Rozróżniono też
  różniczkę form od euklidesowych identyfikacji z rotacją i dywergencją.
- Doprecyzowano lokalną skończoność rodziny nośników w podziale jedności,
  zawieranie domknięcia większej kuli wewnątrz mapy, wersję przy brzegu
  i grupowanie funkcji według pierwotnego pokrycia. To ostatnie uzasadnia
  nośniki dwóch funkcji używanych w dowodzie Mayera–Vietorisa.
- Uzupełniono orientację w wymiarze 0: są dwa znaki, lecz tylko jedna
  baza pusta, więc opis przez dwie klasy baz nie działa w tym wymiarze.
  Całka jest sumą ze znakami, a orientację brzegu przedziału definiuje
  wartość kontrakcji formy z wektorem skierowanym na zewnątrz.
- W dowodzie równoważności opisów orientowalności wydzielono wymiar 0,
  zmniejszono mapy do spójnych dziedzin i dopuszczono obie półprzestrzenie.
  Pozwala to dobierać mapy dodatnie także na obu końcach przedziału.
- W twierdzeniu o orientacji regularnego przeciwobrazu dodano konieczne
  założenie regularności ograniczenia do brzegu, jeśli M ma brzeg.
  Dowiedziono lokalnej postaci półprzestrzeni i równości brzegów.
  Kontrprzykład F(x,s)=x²+s na s≥0 pokazuje, że sama regularność F
  nie wystarcza. Ilorazowy wzór na formę orientującą poziomicę obejmuje
  także wymiar 0 i wyjaśnia niezależność od podniesień i baz.
- We wzorze Stokesa sprawdzono znaki normalnej zewnętrznej i indeksu
  pominiętej współrzędnej. Zaznaczono, że odzyskanie podstawowego
  twierdzenia rachunku całkowego jest identyfikacją przypadku szczególnego;
  dowód Stokesa sam już używa tego faktu analizy.
- Dla okręgu wykazano pełną okresowość funkcji pierwotnej, zamiast
  jedynie równości wartości na końcach przedziału. Dla sfer rozpisano
  surjekcję (a,b) ↦ b−a w stopniu 0; dla torusa oddzielono niezależność
  dwóch klas stopnia 1 od niezerowości klasy stopnia 2.
- W porównaniu trzech teorii dodano spójność drogową przy H₁ oraz k≥2
  przy wyższym twierdzeniu Hurewicza, objaśniono warianty oznaczeń
  homologii i przejście do lokalnie skończonych triangulacji przez
  skończone podkompleksy. Doprecyzowano położenie wycinanego dysku w torusie.
- Jawnie wskazano dodatkową zależność zastosowania Hurewicza:
  twierdzenie o triangulacji gładkich rozmaitości daje strukturę CW.
  Jest to wskazany z nazwy wynik zewnętrzny, z odsyłaczem do
  [notatek Luriego](https://www.math.ias.edu/~lurie/937notes/937Lecture3.pdf),
  a nie twierdzenie udowodnione w tym rozdziale. Dowód de Rhama po
  poprawkach nie korzysta z triangulacji. Ewentualny osobny dowód
  twierdzenia o triangulacji pozostaje propozycją rozbudowy do oceny
  po zakończeniu całego przeglądu.
- Poprawiono „kokcykl” na „kocykl”, nawiasy w definicji jądra operatora
  brzegu, błędne położenie odsyłacza do przykładu dysku i określenie
  „baza otoczenia” w obliczeniu orientacji odwzorowania antypodalnego.

### Ilustracje i skład

- Rysunek 9.1: nawiasy w wartości iloczynu zewnętrznego, łuk o właściwym
  środku i precyzyjny podpis odróżniający wybraną formę od pola
  euklidesowego. Dowolna 2-forma nie jest automatycznie polem powierzchni.
- Rysunek 9.2: oba łuki orientacji leżą dokładnie na obwodzie dysku.
- Rysunek 9.4: usunięto biały dysk i jego przerywany obwód, które
  sugerowały usunięcie całego otworu. Pozostaje jeden zaznaczony punkt;
  podpis wyjaśnia, że niebieski dysk jest fragmentem dziedziny.
- Rysunki 9.3 i 9.5 są merytorycznie poprawne. Do przykładu z dwoma
  trójkątami dopisano argument o składowych otoczenia po usunięciu
  wspólnego wierzchołka. Zwiększono odstępy w tabeli porównawczej.

### Kontrole w trakcie pracy

- Kontrola zakresu względem `f7df0ae`: źródło zmieniono tylko w rozdziale 9.
  Środowiska są zbilansowane, etykiety niepowtórzone, odsyłacze mają cele.
- Symboliczny rachunek form wielomianowych w stopniach 0–3 potwierdził
  d²=0, wzór Cartana porównany z niezależnym wzorem współrzędnych
  pochodnej Liego oraz tożsamość radialnego operatora homotopii.
- Wyznaczniki dla wszystkich 35 ścian standardowych sympleksów
  wymiarów 1–7 potwierdziły znaki (−1)^j z normalną zewnętrzną najpierw.
- Sprawdzono tożsamość hδ+δh=id dla rozszerzonego kompleksu Čecha
  z pięcioma indeksami w stopniach 0–4, w tym indeksy powtórzone.
  Rozpisano też znaki stożka porównania tabel w samym dowodzie.
  Te kontrole są pomocnicze; uzasadnienia ogólne pozostają w tekście.
- Obejrzano wszystkie 21 stron rozdziału (148–168 PDF po drugiej kompilacji,
  przed przesunięciem numeracji przez nowy commit Darka)
  oraz pięć stron z ilustracjami w większej rozdzielczości.
- Sprawdzono materiał porównawczy o formach i kohomologii w
  [notatkach Gualtieriego](https://www.math.toronto.edu/mgualt/courses/17-1300/docs/17-1300-notes-13.pdf)
  oraz wskazane w rozdziale źródła MIT i Luriego. Nowy dowód sklejania
  jest rozpisany bez przyjmowania istnienia dobrego pokrycia rozmaitości.

### Weryfikacja końcowa

- Po pobraniu zmian Darka ponownie sprawdzono zakres: względem `0d9857f`
  źródło przed i po rozdziale 9 pozostaje identyczne. Powtórzono kontrole
  odsyłaczy i rachunków. Niezależne macierze kompleksu podwójnego
  potwierdziły zgodność podanych znaków stożka kolumn ze stożkiem
  odwzorowania kompleksów całkowitych.
- Ponownie obejrzano wszystkie strony rozdziału w aktualnej numeracji
  157–177 oraz tabelę na stronie 175 w większej rozdzielczości.
  Pięć rysunków znajduje się teraz na stronach 158, 163, 165, 170 i 174.
- Końcowa kompilacja lokalnym MiKTeX dała 300 stron, bez błędów,
  nieznanych odsyłaczy, żądań ponownej kompilacji i ostrzeżeń `Overfull`.
  Pozostały dwa wcześniejsze `Underfull` w późniejszych rozdziałach
  oraz trzy automatyczne zmiany położenia ilustracji `h` na `ht`.
  Wbudowany kompilator edytora zwrócił status nieznany; potwierdzeniem
  kompilacji jest wynik lokalnego MiKTeX. PDF zaktualizowano ze źródłem.

Następna iteracja: rozdział 10 — „Tensor metryczny, długość i miara”.

## Rozdział 10 — tensor metryczny, długość i miara (2026-10-02–03)

Punkt wyjścia: `c4efcb0`. Aktualizacja repozytorium na początku iteracji
potwierdziła brak nowych commitów. Przeczytano cały rozdział (osiem sekcji,
dwie ilustracje); przegląd oraz poniższe kontrole zakończono.

### Definicje, modele i odległość

- Oddzielono zapowiedź zachowania geodezyjnych i krzywizny przez izometrie
  od bieżącego wywodu: dowód tych dwóch własności korzysta z definicji
  następnych rozdziałów, co teraz wskazano wprost. Długość, odległość
  i miara są dalej rozwijane niezależnie od tych przyszłych pojęć.
- Dopisano R>0 przy sferze. W przykładzie Schwarzschilda doprecyzowano
  asymptotyczne unormowanie czasu i podano czas własny obserwatora
  statycznego: dτ=√(1−2M/r) dt.
- Dla Kerra obliczono wyznacznik Σ zmiany bazy różniczek t,φ;
  uzasadnia to sygnaturę. Dodatnią określoność przekroju t=const
  potwierdza jawny dodatni współczynnik przy dφ², po przekształceniu
  nawiasu do (r²+a²)Σ+2Mr a² sin²θ. Poprawiono pisownię
  „pseudoriemannowska”.
- W definicji długości podano a<b, ciągłość krzywej i skończony podział
  na kawałki klasy C¹. Rozróżniono wektor prędkości i jego długość.
  Dla punktów w różnych składowych infimum pustej rodziny wynosi +∞;
  zwykłą metrykę otrzymujemy na każdej składowej osobno.
- Uściślono klasę regularności przeparametryzowania do stałej szybkości:
  dla regularnej krzywej C¹ jest ono C¹, dla krzywej odcinkami regularnej
  odpowiednio odcinkami C¹. Dodano niezmienniczość długości przy
  odwróceniu kierunku parametru.
- W dowodzie skończoności odległości użyto otwartych klas osiągalności
  krzywymi odcinkami C¹. Dopisano przypadek wymiaru 0 i pełną wersję
  argumentu lokalnego w półkulach przy brzegu.
- Poprawiono przykład ciągu 1/j w (0,1): indeksowanie zaczyna się od j=2.
- Rozpisano dolne oszacowanie długości drogi w kuli Poincarégo przez
  całkę 2|ρ′|/(1−ρ²), z jawnym użyciem absolutnej ciągłości ρ=|γ|.
  To obejmuje również przejścia przez środek, gdzie norma nie zawsze
  ma klasyczną pochodną. Promień osiąga dolne oszacowanie.

### Całkowanie i dywergencja

- Zwarty nośnik funkcji mierzalnej nie wystarcza do całkowalności.
  Definicję całki sformułowano dla funkcji nieujemnych (możliwa wartość
  +∞) albo całkowalnych bezwzględnie. Dodano miarę liczącą i formę
  objętościową ze znakiem w wymiarze 0.
- Przy całkowaniu po sferze wyjaśniono pominięcie biegunów i południka:
  mają zerową miarę powierzchniową w regularnych mapach, z twierdzenia
  Fubiniego. Nie traktujemy osobliwych współrzędnych jako poprawnej mapy.
- Przy wzorze z iloczynem wektorowym dopisano konieczne założenie
  euklidesowej metryki na R³, a przy całce strumienia jednokrotne
  pokrywanie fragmentu przez parametryzację.
- Uzasadniono gładkość gradientu przez gładką macierz odwrotną oraz
  niezależność lokalnej dywergencji od lokalnie stałych znaków orientacji.
- Skonstruowano zewnętrzną normalną jednostkową jako −∇s/|∇s| przy
  lokalnej funkcji brzegowej s≥0 i wyjaśniono zgodność na przecięciach.
- W dowodzie Gaussa wydzielono n=1: w zerowymiarowej przestrzeni
  stycznej brzegu nie zawsze istnieje „dodatnia baza”, więc użyto
  znaków punktów i kontrakcji formy. Twierdzenie wyraźnie obejmuje
  również przypadek nieorientowalny, już uzasadniony przez podział jedności.

### Miara Hausdorffa

- Doprecyzowano skończone i przeliczalne pokrycia, puste pokrycie,
  pomijanie pustych składników oraz brak dopuszczalnego pokrycia.
  Wykazano, że H⁰ rzeczywiście liczy punkty, także dla zbiorów nieskończonych.
- Dodano dowód, że konstrukcja daje miarę zewnętrzną, addytywną na
  zbiorach o dodatniej wzajemnej odległości. Kryterium Carathéodory’ego
  dla zbiorów domkniętych sprawdzono przez warstwy odległości od zbioru;
  z niego wynika mierzalność borelowska. Jest to potrzebne do późniejszego
  przeliczalnego rozcinania zbiorów w dowodzie równości miar.
- W lemacie Lipschitza użyto dodatnich stałych, unikając nieokreślonych
  iloczynów 0·∞; mapy stałe nadal są objęte twierdzeniem. Wyjaśniono,
  dlaczego pokrycia można ograniczać do samego podzbioru.
- Poprawiono „podrozmaitość zanurzona (bez samoprzecięć)” na precyzyjne
  założenie osadzenia. Sam brak samoprzecięć immersji nie zapewnia
  topologii podprzestrzeni. Rozróżniono składowe dla odległości wewnętrznej.
- W kroku euklidesowym osobno wykazano, że zbiór zerowej miary Lebesgue’a
  ma zerową miarę Hausdorffa: pokrycie drobnymi sześcianami ma koszt
  ograniczony stałą razy sumę ich objętości. Dzięki temu argument
  Vitalego nie zakłada już niejawnie właśnie dowodzonej równości miar.
- Zastąpiono „dostatecznie bliskie punkty” konkretnymi kulami B_r i B_3r.
  Wyjście z większej kuli kosztuje co najmniej 2r√(1−ε), co wystarcza
  do dolnego oszacowania dla każdej pary punktów w mniejszej kuli.
  Argument obejmuje półkule i drogi opuszczające dziedzinę mapy.
- Rozpisano współczynniki ((1−ε)/(1+ε))^(n/2) i odwrotne w porównaniu
  miar, przeliczalny rozkład dla ustalonego ε i dopiero późniejsze
  przejście ε→0, także dla zbiorów nieskończonej miary.
- Na podrozmaitości wykorzystano DF bliskie izometrycznemu włożeniu J.
  Całkowanie po odcinku parametrów daje dolną granicę odległości
  otoczenia, a obraz odcinka daje górną granicę odległości wewnętrznej.
  Razem z wyznacznikiem Grama dowodzi to równości obu miar z μ_h,
  bez twierdzenia, że same odległości są globalnie równe.

### Ilustracje

- Rysunek trzech modeli: czerwone wektory mają teraz dokładnie długość
  hiperboliczną 1, z uwzględnieniem skali narysowanej kuli. Profil
  hiperboloidy pochodzi ze wzoru t=√(1+r²), zamiast krzywych z ostrym
  czubkiem; dodano dwa przekroje i usunięto nieobjaśnioną złotą strzałkę.
- Rysunek pozostaje przed sekcją o metrykach lorentzowskich. Skrócono
  pierwszy nagłówek sekcji, który wcześniej łamał wyraz między wierszami.
- Rysunek parametryzacji powierzchni jest poprawny: odróżnia obszar
  parametrów, jego obraz, wektory styczne i normalną. Pozostawiono go.
  Określenie „Gram ich iloczynów” zastąpiono „macierzą Grama tych wektorów”.

### Weryfikacja rachunkowa i źródła

- Kontrola zakresu względem `c4efcb0` potwierdziła brak zmian poza
  rozdziałem 10. Etykiety są niepowtórzone, odsyłacze mają cele,
  środowiska są zbilansowane, rozdział zawiera dwie ilustracje.
- Symbolicznie sprawdzono cofnięcie i przeniesienie metryki przez
  ścinanie (u,v) ↦ (u,v+u²), metrykę sfery w obu układach współrzędnych,
  metrykę hiperboloidy, jej macierz odwrotną i wyznacznik.
- Oba przekształcenia między modelami hiperbolicznymi sprawdzono przez
  macierze Jacobiego; wzory odwrotne między kulą a półprzestrzenią przez
  złożenie w obu kierunkach. Są to kontrole w wymiarze 2; ogólny argument
  dla n znajduje się w tekście.
- Dla metryki Kerra obliczono niezależnie blok t,φ, wyraz mieszany,
  wyznacznik pełnej macierzy −Σ²sin²θ, dodatni współczynnik przestrzenny
  i granicę a=0 dającą Schwarzschilda.
- Sprawdzono całkę pola paraboloidy, całkę z² po sferze oraz przykład
  regularnej krzywej o zmiennej szybkości i jej przeparametryzowanie
  osiągające minimalną energię.
- Jako kontrolę wzorów na gęstość, normalną i dywergencję obliczono
  obie strony tożsamości Gaussa dla X=(xy,y²) w metryce hiperbolicznej
  na prostokącie [1,2]×[1,3]. Całka objętościowa i suma strumieni
  przez cztery krawędzie wynoszą log(3). Jest to pomocniczy rachunek
  z narożami, nie zastępstwo dowodu ogólnego twierdzenia.
- Wszystkie cztery strzałki na rysunku modeli mają normę hiperboliczną 1;
  pochodna profilu hiperboloidy w najniższym punkcie jest zerowa.
- Punkty odniesienia: wzory tensorów
  [Schwarzschilda](https://sites.science.oregonstate.edu/physics/coursewikis/GGR/_export/xhtml/book/ggr/schwarz.html)
  i [Kerra](https://sites.science.oregonstate.edu/coursewikis/GGR/book/content/kerr)
  w kursie Teviana Draya oraz twierdzenie Carathéodory’ego i dodatek A
  [notatek Gautama Iyera](https://www.math.cmu.edu/~gautam/sj/teaching/2022-23/720-measure/pdfs/measure.pdf).
  Nierówność izodiametryczna i twierdzenie Vitalego pozostają jawnie
  nazwanymi faktami z teorii miary; ich pełne dowody nie są deklarowane
  jako zawartość tego rozdziału. Aneks z podstawami miary jest kandydatem
  do listy możliwych rozszerzeń po przeglądzie całego skryptu.

### Kontrola końcowa

- Obejrzano wszystkie 18 stron rozdziału (178–195 PDF), a po korektach
  nagłówka i położenia ilustracji ponownie sprawdzono układ stron.
  Oba rysunki, na stronach 182 i 188, sprawdzono w większej rozdzielczości.
- Końcowa kompilacja lokalnym MiKTeX dała 303 strony. Brak błędów,
  niezdefiniowanych odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostały dwa wcześniejsze `Underfull` w późniejszych rozdziałach
  oraz trzy automatyczne zmiany położenia ilustracji `h` na `ht`.
- Wbudowany kompilator ponownie zwrócił status nieznany; poprawną
  kompilację potwierdza lokalny MiKTeX. PDF zaktualizowano ze źródłem.
- Kontrole zakresu, odsyłaczy i rachunków zakończyły się poprawnie;
  `git diff --check` nie wykazał błędów. Przed wysłaniem ponownie
  sprawdzono serwer: brak nowych commitów do włączenia.

Następna iteracja: rozdział 11 — „Koneksje i transport równoległy”.

## Rozdział 11 — koneksje i transport równoległy (2026-10-03)

### Zakres i stan początkowy

- Pobrano stan zdalnego brancha `review/rozdzialy-matematyka`:
  brak nowych commitów względem `3735830`. Wcześniejsze zmiany Darka
  pozostają zachowane. Ta iteracja obejmuje wyłącznie rozdział 11,
  ten dziennik oraz wynikowy PDF.
- Przeczytano wszystkie sześć sekcji: aksjomaty i lokalne współczynniki,
  konstrukcję Leviego-Civity, przykłady modelowe, transport i tensory,
  Schwarzschilda i Kerra oraz wariację energii. Sprawdzono oba rysunki.

### Definicje i dowody

1. **Lokalność koneksji.** Dodano lemat i dowód z funkcją odcinającą.
   Aksjomaty początkowo dotyczą pól globalnych; przed użyciem lokalnej
   ramki trzeba uzasadnić ograniczanie koneksji do otwartych podzbiorów.
   Dowód wyjaśnia również zależność pierwszego argumentu tylko od
   wektora w punkcie. „Kierunek” zastąpiono „wektorem”, ponieważ
   długość tego wektora również wpływa na wynik.
2. **Transformacja symboli Christoffela.** Pokazano etap przed zmianą
   bazy, z którego pochodzi druga pochodna zmiany współrzędnych.
   Ułatwia to sprawdzenie kolejności indeksów i członu nietensorowego.
3. **Konstrukcja Koszula.** Poprawiono sformułowanie „współczynniki są
   kowektorem”: to całe `K(X,Y,·)` jest 1-formą. Dodano jawny wzór
   z czynnikiem 1/2 i odwrotną macierzą metryki oraz argument zgodności
   konstrukcji na przecięciach map. Pozostałe sprawdzenia wzoru Koszula
   i rzutowania pochodnej na podrozmaitość są poprawne.
4. **Izometrie a koneksje.** Rozwinięto użycie jednoznaczności:
   zdefiniowano przeniesioną koneksję i wskazano rolę naturalności
   nawiasu Liego oraz cofnięcia metryki. To uzasadnia porównywanie
   koneksji w różnych modelach hiperbolicznych.
5. **Pochodna wzdłuż dowolnej krzywej — istotna luka.** Wcześniejszy
   argument przez przedłużenie pola nie obejmował nawet krzywej stałej
   z polem `V(t)=t v`. Zastąpiono go pełnym sprawdzeniem transformacji
   `A` i `V` za pomocą jakobianu. Nie trzeba zakładać immersyjności,
   braku samoprzecięć ani niezerowej prędkości. Dodano wymaganie
   gładkości pola jako przekroju wiązki cofniętej.
6. **Zmiana parametru i sklejenia.** Udowodniono regułę łańcuchową
   dla pochodnej kowariantnej. Uzasadnia ona niezależność transportu
   od zachowującej orientację zmiany parametru. Dodano definicję
   transportu dla krzywych kawałkami gładkich i niezależność od
   zagęszczania podziału; obejmuje to sklejenia z narożnikiem.
7. **Istnienie transportu na całym odcinku.** Dodano oszacowanie
   normy rozwiązania przez nierówność Grönwalla oraz argument
   przedłużania rozwiązania z granicy na końcu przedziału.
   Regułę różniczkowania `g(V,W)` wyprowadzono we współrzędnych,
   także dla pól niemających przedłużenia poza krzywą.
8. **Założenia metryczne.** Zdanie o izometrii dla zamkniętej drogi
   wymaga koneksji zgodnej z metryką; dodano ten warunek. W sekcji
   o tensorach oddzielono ogólną koneksję afiniczną od szczególnego
   warunku `nabla g=0`. W dywergencji jawnie wskazano koneksję
   Leviego-Civity i ślad endomorfizmu `Y -> nabla_Y X`.
9. **Pochodne tensorów.** Uzasadniono, dlaczego wzór dla 1-formy jest
   liniowy nad funkcjami w argumencie wektorowym. Dodano definicję
   dla typu `(r,s)` przez różniczkowanie ewaluacji, wyjaśnienie
   tensorialności oraz istnienia i jednoznaczności rozszerzenia.
   Wyjaśniono znaki przy górnych i dolnych indeksach.
10. **Wariacja energii.** Doprecyzowano gładkość i założenie, że
    krzywa leży we wnętrzu rozmaitości. Inaczej dowolne małe wariacje
    współrzędnych mogą być niedopuszczalne. Dodano realizację pól
    wariacyjnych o zwartym nośniku, dowód użytej wersji lematu
    podstawowego rachunku wariacyjnego oraz przejście przez wiele map.
    Udowodniono także kierunek odwrotny: równanie geodezyjnej implikuje
    stacjonarność, bo wyrazy brzegowe na wewnętrznych punktach podziału
    się znoszą. Dodano zachowanie kwadratu normy prędkości i wyjaśnienie,
    dlaczego parametr geodezyjnej niestałej można zmieniać afinicznie.

### Przykłady, terminologia i ilustracje

- Doprecyzowano zakres współrzędnej kątowej w mapie biegunowej.
  W przykładzie sferycznym wyjaśniono, że pełny równoleżnik wymaga
  wielu map, lecz ramka ortonormalna skleja się i jest okresowa.
  Ustalono orientację pomiaru kąta transportu.
- Uzupełniono symetryczne symbole w modelu półprzestrzeni i informację
  o zerowaniu pozostałych. Wyjaśniono euklidesowy sens dolnych indeksów
  współrzędnych w modelu kuli i hiperboloidy: nie jest to obniżanie
  indeksu metryką hiperboliczną.
- Poprawiono pisownię „pseudoriemannowska”, użyto „ramka ortonormalna”
  i wyjaśniono „kontrakcję”. Mylące „odjęcie zmiany bazy” zastąpiono
  „uwzględnieniem zmiany bazy”, zgodnie ze znakiem we wzorze.
- Pierwszy rysunek zachowano jako schemat; podpis wyraźnie określa,
  że wygląd strzałek nie koduje metryki ani konkretnego kąta.
- Drugi rysunek zbudowano na nowo jako rzut ortogonalny sfery.
  Równoleżnik ma dokładnie `theta=pi/3`, a dwa wektory są przeciwne,
  zgodnie z obliczonym obrotem `-pi`. Oba wychodzą z oznaczonego punktu
  i mają tę samą skalę. Widoczność łuku wynika z iloczynu z kierunkiem
  obserwacji, a nie z arbitralnego podziału elipsy na połowy.
  Podpis wyjaśnia przesunięcie początku pętli na potrzeby rysunku.

### Kontrole rachunkowe

- Ponownie obliczono wszystkie symbole dla współrzędnych biegunowych,
  sfery, półpłaszczyzny, dysku Poincarégo i dwuwymiarowej hiperboloidy.
  Ogólne wzory wielowymiarowe sprawdzono bezpośrednio w tekście.
- Sprawdzono transformację zerowej koneksji kartezjańskiej do
  współrzędnych biegunowych i transformację pochodnej dowolnego pola
  na krzywej o jednocześnie zmiennym promieniu i kącie.
- Sprawdzono jednostkowe pola równoległe w modelach hiperbolicznych,
  pochodne ramki sferycznej, macierz rozwiązania transportu, jej
  ortogonalność oraz wartość `-I` po obiegu przy `theta=pi/3`.
- Ponownie wyliczono pełny zestaw symboli Schwarzschilda i wszystkie
  wypisane symbole Kerra, w tym znak członu mieszanego. Sprawdzono
  przejście `a=0` do Schwarzschilda. Istniejące wzory są poprawne.
- Sprawdzono zgodność równań Eulera–Lagrange'a z kowariantnym
  przyspieszeniem dla przykładu z niediagonalną macierzą metryki.
- Sprawdzono styczność wektora z rysunku sfery, jego rzut oraz
  punkty przejścia między widoczną i zasłoniętą częścią równoleżnika.
- Kontrole symboliczne wykonano w SymPy. Osobno sprawdzono zakres
  zmian, zgodność środowisk LaTeX, unikatowość etykiet i odsyłacze.
  Źródła porównawcze: rozdział 15
  [notatek Eckharda Meinrenkena](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)
  i wykład 7
  [notatek MIT 8.962](https://web.mit.edu/8.962/www/lecnotes/8_962TA-lec-all.pdf).

### Kontrola końcowa

- Obejrzano wszystkie 11 stron rozdziału (196–206 PDF), a oba rysunki
  na stronach 196 i 203 także w większej rozdzielczości. Po pierwszym
  oglądzie poprawiono kolizję podpisu ze sferycznym równoleżnikiem,
  odstęp opisu drogi i skrócono tytuł sekcji 11.3, aby nie łamał słowa
  „modelowych”. Ponownie sprawdzono wszystkie strony po korektach.
- Końcowa kompilacja lokalnym MiKTeX dała 305 stron. Brak błędów,
  niezdefiniowanych odsyłaczy, żądań kolejnej kompilacji i `Overfull`.
  Pozostał jeden `Underfull` w późniejszym rozdziale oraz trzy
  wcześniejsze automatyczne zmiany położenia ilustracji `h` na `ht`.
- Wbudowany kompilator zwrócił status nieznany; poprawną kompilację
  potwierdza lokalny MiKTeX. PDF zaktualizowano ze źródłem.
- Kontrole rachunkowe i zakresu zmian przeszły ponownie po końcowych
  poprawkach. `git diff --check` nie wykazał błędów. Ponowne pobranie
  stanu serwera potwierdziło brak nowych commitów do włączenia.

Następna iteracja: rozdział 12 — „Geodezyjne, odwzorowanie wykładnicze
i zupełność”.

## Rozdział 12 — geodezyjne, odwzorowanie wykładnicze i zupełność (2026-10-03)

### Zakres

- Pobrano stan serwera: brak nowych zmian względem `4c29411`.
  Przegląd obejmuje wszystkie sześć sekcji rozdziału i dziewięć
  ilustracji. Zmiany poza rozdziałem ograniczają się do tego dziennika
  oraz wygenerowanego PDF.

### Założenia i dowody lokalne

1. **Rozmaitości bez brzegu.** Dodano ogólne założenie i powtórzono
   je przy twierdzeniu Hopfa–Rinowa. Bez niego stwierdzenia są fałszywe:
   domknięty przedział jest zwarty, ale geodezyjnej dochodzącej do jego
   końca nie można przedłużyć. Określono też domyślny riemannowski
   charakter metryki i rozpatrywanie odległości w jednej składowej.
2. **Pierwsza wariacja długości.** Uzasadniono różniczkowanie normy
   przez jednostajną regularność na zwartym przedziale. Zamianę
   pochodnych kowariantnych wyprowadzono we współrzędnych; nie wymaga
   ona immersyjności odwzorowania wariacji. Doprecyzowano regularność
   kawałków i stały podział przy wzorze z wyrazami narożnikowymi.
3. **Dziedzina eksponenty.** Dodano otwartość `D_p`, jej gwiaździstość,
   gładkość eksponenty na całej dziedzinie i zależność od punktu
   bazowego. Podano ogólne prawo skalowania geodezyjnej, również
   potrzebne przy różniczkowaniu eksponenty dla ujemnego parametru.
   Opiera się to na otwartości dziedziny maksymalnego przepływu na `TM`.
4. **Współrzędne normalne w sygnaturze nieokreślonej.** Wyjaśniono,
   że macierz jednostkową zastępuje macierz sygnatury, a kula w
   przestrzeni stycznej korzysta z pomocniczej normy euklidesowej.
   Niezdegenerowana metryka nieokreślona sama nie definiuje normy.
5. **Minimalność radialnej geodezyjnej.** Wybrano większą dziedzinę
   dyfeomorfizmu, zawierającą domknięcie kuli użytej w dowodzie.
   Uzupełniono krok w punkcie centralnym: funkcja promienia wzdłuż
   drogi jest lipschitzowska i absolutnie ciągła, a jej pochodna jest
   zerowa prawie wszędzie na zbiorze zer. Argument działa również dla
   wielokrotnych powrotów do środka, nie tylko skończonego podziału.
6. **Przypadek równości.** Wykazano niemalejący promień i stały
   kierunek na jedynym końcowym przedziale, gdzie promień jest dodatni.
   Wyjaśniono dopuszczalność postojów; nie każda droga minimalna jest
   regularną reparametryzacją przez dyfeomorfizm. Osobno uwzględniono
   identyczne końce i drogę stałą.
7. **Małe kule.** Dodano równość małych kul metrycznych (otwartych
   i domkniętych) z obrazami kul przez eksponentę. Argument pierwszego
   wyjścia wyklucza krótsze drogi spoza otoczenia. Ten krok jest
   później potrzebny do zwartości sfer w dowodzie Hopfa–Rinowa.

### Modele i twierdzenie Hopfa–Rinowa

8. **Sfera.** Dopisano `R>0` i uzasadniono dolne ograniczenie długości
   drogi przechodzącej przez antypodę, przez pierwsze osiągnięcia
   poziomów zbliżających się do `pi R`. Wskazano obsługę niegładkości
   promienia przy przejściu przez punkt początkowy.
9. **Półprzestrzeń hiperboliczna.** Dodano jawne rozwiązanie półokręgu
   przez `tanh` i `cosh`, aby uzasadnić gładkie przejście przez punkt
   maksymalnej wysokości, gdzie wcześniejsze dzielenie przez pochodną
   wysokości nie działa. Oddzielono krzywe stałe i przypadek wymiaru 1.
10. **Hiperboloida.** Rozwinięto argument rzutowania pochodnej dla
    metryki lorentzowskiej otoczenia: wcześniejsze stwierdzenie
    dotyczyło otoczenia euklidesowego. Podano wzór `nabla_X Y =
    D_X Y - g(X,Y)x` i sprawdzono przyspieszenie. Wykazano pozostawanie
    na górnym płacie, istnienie przez cały czas oraz nierówność
    `-<p,q>_L >= 1`, z równością dokładnie dla `p=q`, potrzebną do
    użycia `arcosh`. W modelu dysku uzasadniono położenie środka
    okręgu poza dyskiem.
11. **Wykluczenie narożnika.** Zastąpiono argument wymagający kontroli
    promienia normalnego otoczenia przy zmieniającym się środku
    bezpośrednią wariacją. Wektor wariacyjny jest różnicą stycznych,
    a pierwsza pochodna długości wynosi minus kwadrat normy tej
    różnicy. Daje to ścisłe skrócenie narożnika bez dodatkowego
    twierdzenia o jednolitych otoczeniach normalnych.
12. **Zupełność.** W lemacie o jednej pełnej eksponencie dodano
    spójność i wskazano wcześniejsze uzasadnienie małych kul.
    W implikacji „zupełność metryczna => geodezyjna” wyodrębniono
    ciąg zbieżny do końca parametru, a następnie pełną granicę krzywej.
    Osobno uwzględniono geodezyjne stałe. Dla zwartej rozmaitości
    argument stosuje się składowa po składowej.
13. **Przebita płaszczyzna.** Dopisano rodzinę dróg o długościach
    `2+(pi-2)epsilon`, wykazującą, że infimum rzeczywiście wynosi 2.
    Wyjaśniono także warunek równości wykluczający osiągnięcie infimum.

### Czasoprzestrzenie i przekroje

14. **Lokalna maksymalność czasu własnego.** Uzupełniono brakujący
    krok: dlaczego przyszłościowa krzywa czasopodobna pozostająca
    w dostatecznie małym otoczeniu normalnym nie opuszcza obrazu
    przyszłego stożka. Dla `Q(exp_p v)=g_p(v,v)` lemat Gaussa daje
    `dQ(W)=2g(R,W)`. Na niezerowym świetlnym brzegu pochodna wzdłuż
    krzywej czasopodobnej jest ujemna, co wyklucza pierwsze wyjście.
    Lokalna współrzędna czasu wyklucza powrót do wierzchołka.
    Uzasadniono znak pochodnej radialnego czasu i całkowanie od jego
    zerowej wartości początkowej. Pozostają jawne ograniczenia do
    małego otoczenia i krzywych czasopodobnych; nie jest to twierdzenie
    o globalnej maksymalności w dowolnej czasoprzestrzeni.
15. **Schwarzschild.** Wyjaśniono redukcję do płaszczyzny równikowej
    przez odbicie i jednoznaczność danych początkowych. Dopisano pełne
    równanie radialnego przyspieszenia, z którego wynika warunek
    zerowania pochodnej potencjału dla orbity kołowej. Sama pochodna
    pierwszej całki nie uzasadnia tego w punkcie `dot r=0`.
16. **Kerr.** Powtórzono zakres parametrów i dziedzinę zewnętrzną;
    wskazano analogiczne ograniczenie pierwszej całki radialnej przy
    punktach zwrotnych. Istniejące wzory pędów, energii i dwóch
    kandydatów na prędkość kątową są poprawne.
17. **Przekroje przestrzenne.** Sprecyzowano, że ciąg Cauchy'ego
    zbliżający się do pominiętego horyzontu leży na ustalonym promieniu
    równikowym. Sam warunek zbiegania współrzędnej radialnej nie
    wystarcza przy dowolnie zmieniających się kątach. Poprawiono też
    odsyłacz na „Wniosek” zamiast „Twierdzenie”.

### Język i ilustracje

- „Minimizer” zastąpiono polskimi określeniami krzywej lub geodezyjnej
  minimalnej. Poprawiono „pseudoriemannowska”, rozróżnienie prędkości
  i jej normy oraz zapis kwadratów pochodnych.
- Na sferze zastąpiono arbitralne krzywe Béziera dokładnymi rzutami
  dwóch półokręgów wielkich kół. Równik rzutuje się na odcinek,
  zgodnie z położeniem biegunów w przyjętym kierunku obserwacji.
- Niespójny szkic hiperboloidy i płaszczyzny zastąpiono dokładnym
  przekrojem `z_2=0` z hiperbolą `(cosh u,sinh u,0)`, początkiem
  przestrzeni otaczającej oraz oznaczonymi parametrami punktów.
  Podpis precyzuje, że to przekrój, nie widok całej powierzchni.
- Odsunięto końce kolorowych fragmentów geodezyjnych hiperbolicznych
  od idealnego brzegu, który nie należy do rozmaitości.
- W diagramie czasu własnego poprawiono nachylenie promieni świetlnych
  na 45 stopni w skali użytych współrzędnych. Poprzedni stożek był
  zbyt wąski i umieszczał narysowaną krzywą czasopodobną poza nim.
  Sprawdzono również czasopodobność całej czerwonej krzywej Béziera.

### Sprawdzenia rachunkowe

- Kontrole symboliczne potwierdziły wzory eksponenty sfery i
  hiperboloidy, normy prędkości, przyspieszenia, metryki w radialnych
  współrzędnych riemannowskich i lorentzowskich, półokręgi hiperboliczne
  w obu orientacjach oraz wzory odległości w dysku i półpłaszczyźnie.
- Sprawdzono radialne równanie Schwarzschilda, promień i energię
  orbity fotonowej, pędy Kerra, normalizację prędkości, granicę
  `a=0`, oba pierwiastki równania orbit kołowych i ich normy.
- Kontrola zakresu zmian, etykiet, odsyłaczy i dziewięciu rysunków
  przeszła poprawnie. Testy symboliczne wykonano w SymPy.
- Punkty odniesienia: [dowód Daniela Spiegla](https://math.uchicago.edu/~may/REU2016/REUPapers/Spiegel.pdf),
  [notatki Eckharda Meinrenkena](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)
  oraz [postać metryki Kerra w kursie Teviana Draya](https://sites.science.oregonstate.edu/coursewikis/GGR/book/content/kerr).

### Kontrola końcowa

- Obejrzano wszystkie 15 stron rozdziału (207–221 PDF), w tym wszystkie
  dziewięć ilustracji w większej rozdzielczości. Po oglądzie rozdzielono
  nakładające się strzałki dwóch kierunków orbity Kerra, odsunięto
  podpisy od krzywych na rysunkach orbity fotonowej i przebitej
  płaszczyzny. Ilustracje hiperboliczne umieszczono przed nagłówkiem
  sekcji o twierdzeniu Hopfa–Rinowa. Poprawione strony sprawdzono ponownie.
- Końcowa kompilacja lokalnym MiKTeX: 307 stron, bez błędów,
  niezdefiniowanych odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostał wcześniejszy `Underfull` w późniejszym rozdziale oraz trzy
  wcześniejsze automatyczne zmiany ustawienia ilustracji `h` na `ht`.
- Wbudowany kompilator ponownie zwrócił status nieznany; wynik
  potwierdza kompilacja lokalna. PDF zaktualizowano ze źródłem.
- Ponownie wykonano kontrole zakresu i rachunków; `git diff --check`
  nie wykazał błędów. Ponowne pobranie stanu serwera potwierdziło
  brak nowych commitów do włączenia.

Następna iteracja: rozdział 13 — „Krzywizna: od transportu równoległego
do tensorów”.

## Iteracja 13 — Krzywizna (2026-10-04)

Przeczytano cały rozdział: tensor Riemanna i jego symetrie,
krzywiznę Gaussa, Ricciego i skalarną, modele, Schwarzschilda
i Kerra, płaskość, drugą wariację, pola Jacobiego, twierdzenia
porównawcze oraz Gaussa–Bonneta z uogólnieniami.

### Matematyka i dowody

- Dopisano domyślne założenie braku brzegu. Rozwijanie walca na
  płaszczyznę opisano lokalnie.
- Zdefiniowano rzeczywistą małą pętlę we współrzędnych normalnych
  i wyprowadzono znak oraz resztę wzoru na jej transport. Przy
  interpretacji „na jednostkę pola” uwzględniono pole równoległoboku.
- Naprawiono błędny zapis kwadratów we wzorze Gaussa. Dodano dowód
  symetrii Ricciego potrzebnej przy polaryzacji i doprecyzowano
  użycie symetrii par w dowodzie o stałej krzywiźnie.
- Wyjaśniono jednostajność reszt rozwinięcia małej kuli i związek
  współrzędnych normalnych z rzeczywistą kulą metryczną. Wyprowadzono
  obwód małego okręgu bez niedozwolonego różniczkowania symbolu O.
- Przy skalowaniu metryki rozróżniono niezmieniony tensor Ricciego
  typu (0,2), jego wartości na nowych jednostkowych wektorach oraz
  skalujące się krzywizny sekcyjną i skalarną.
- Dopisano dziedzinę i sygnaturę ramki Schwarzschilda. Usunięto
  niepopartą dalszą treścią obietnicę późniejszego rozkładu Weyla.
- W dowodzie płaskości zapisano homotopię liniową i obsługę dróg
  odcinkami gładkich. Wyprowadzono komutator pochodnych pól wzdłuż
  dowolnej mapy, także bez założenia immersji.
- Uzupełniono regularność krzywej minimalnej: lokalna równość
  długości wymusza promienie, brak narożnika skleja je w geodezyjną.
  Doprecyzowano niezerowość danych pola Jacobiego w przykładach.
- Dodano lemat o czasie cięcia: mierzalność, jedyność promieni,
  lokalną odwrotność, gładkość odległości i zerową miarę zbioru
  cięcia. Dowód miary wykorzystuje wykres czasu cięcia i Fubiniego,
  dzięki czemu nie wymaga jeszcze nieprzedstawionego twierdzenia
  Sarda ani Rademachera. Porównanie hesjanu ma jawne założenie
  zupełności i oddzielony przypadek zerowego wektora.
- Naprawiono końcowy argument Bishopa–Gromowa: wykazano lokalną
  absolutną ciągłość ilorazu, bo sama ciągłość i niedodatnia pochodna
  prawie wszędzie nie dowodzą monotoniczności. Dodano n >= 2.
- Pełne niezależne obliczenie symboliczne z metryki Kerra potwierdziło
  wszystkie składowe Ricciego i pełną kontrakcję Kretschmanna;
  na tej podstawie dodano kompletną tabelę krzywizny w ramce
  pseudoortonormalnej. Tekst zawiera ramkę, odwrotną metrykę,
  dwa pośrednie rachunki, wszystkie niezależne składowe, oba ślady
  i zliczenie składników pełnej kontrakcji, w tym ujemnych wkładów
  mieszanych. Wyjaśniono przedłużenie tożsamości wymiernych poza
  obszar rzeczywistości użytej ramki.
- Dla Kerra wyprowadzono metrykę we współrzędnych wpadających
  i obliczono jej wyznacznik. To uzasadnia usuwalność osobliwości
  współrzędnych na horyzoncie; sama skończoność jednego niezmiennika
  nie wystarczałaby do takiego wniosku. Założenie M > 0 pozwala
  wnioskować o osobliwości pierścieniowej z rozbieżności na równiku.
- W lemacie indeksowym dopisano ciągłość pól odcinkami gładkich
  i poprawiono brakujący znak pochodnej w całkowaniu przez części.
  Opis wersji Raucha odpowiada teraz dokładnie użytemu założeniu,
  bez nieprecyzyjnej obietnicy słabszego porównania.
- W przykładzie sprzężenia na sferze podano n >= 2, R > 0
  i niezerowe pole początkowe. W twierdzeniu Bonneta–Myersa
  uzupełniono jawne n >= 2 i oddzielono identyczne końce drogi.
- W Cartanie–Hadamardzie uzasadniono otwartość obrazów gałęzi
  odwrotnych, potrzebną w definicji nakrycia.
- Krzywiznę Gaussa abstrakcyjnej powierzchni zdefiniowano wewnętrznie;
  utożsamienie jej z iloczynem krzywizn głównych dotyczy zanurzenia
  w przestrzeni euklidesowej. Podano regularność łuków i zakres
  kątów w wersji Gaussa–Bonneta z narożnikami.
- Naprawiono argument o obrocie stycznej: ramka współrzędnych
  nie jest na ogół ortonormalna, więc przejście nie jest samym
  obrotem. Rozkład polarny macierzy i przedłużenie na dysk
  uzasadniają niezmienność liczby obrotów.
- Doprecyzowano gładką triangulację i niezdegenerowane kąty,
  a w przykładzie trójkąta założono, że rzeczywiście ogranicza dysk.
- W wersji stożkowej dodano brak brzegu i argument z nakryciem
  orientacyjnym dla powierzchni nieorientowalnych.
- Wyjaśniono niezmienniczość Pfaffianu przy dodatniej zmianie ramki
  i jego sklejanie w formę globalną. Rozpisano kontrakcję z symbolami
  antysymetrycznymi prowadzącą do współczynników 1, -4, 1 w 4D.
- Pełne twierdzenie Cherna–Gaussa–Bonneta pozostaje jawnie wskazanym
  wynikiem zewnętrznym, wymagającym teorii klas charakterystycznych.
  Jego wersja brzegowa jest oznaczona jako schemat bez definicji
  formy brzegowej i bez dowodu. Nie przedstawiamy testów wzoru jako
  dowodu ogólnego twierdzenia. Ewentualne pełne rozwinięcie tej teorii
  trafia do propozycji po zakończeniu całego przeglądu.
- W brzegowym przykładzie zastąpiono kulę otwartą kulą domkniętą.

### Terminologia i ilustracje

- Poprawiono zdanie o znikaniu pochodnych metryki we współrzędnych
  normalnych i użyto określenia „brak torsji”. Dla kąta od bieguna
  użyto „kąt biegunowy (kolatytuda)”, zamiast mylącej szerokości.
- Zastąpiono szkic siodła rzutem rzeczywistej powierzchni
  z siatką i przekrojami x = 0, y = 0 przez zaznaczony punkt.
  Złoty łuk na sferze jest rzeczywistym rzutem wielkiego okręgu.
- Ilustrację pól Jacobiego oparto na dokładnych rzutach południków,
  z poprawnym równikiem, wspólnymi biegunami i stycznym rzutem pola.
  Podpis wyjaśnia umowną skalę strzałki.
- Poprawiono podpis wykresu Raucha: jednakowa jest początkowa
  pochodna pola, a samo pole początkowo znika. Odsunięto etykiety
  krzywych od linii wykresu.
- Rysunek brzegu Gaussa–Bonneta zastąpiono ćwierćdyskiem, na którym
  T jest dokładnie styczny, JT wewnętrzny, a kąt narożnika jednoznaczny.
  Czapkę pokazano w jawnym rzucie od bieguna, z prawidłowym kierunkiem
  obiegu. Rozdzielono etykiety JT i kąta po kontroli PDF.
- W trójkącie Poincarégo zastąpiono zaokrąglone parametry okręgów
  dokładnymi zależnościami: boki są prostopadłe do brzegu dysku
  i kończą się dokładnie we wspólnych wierzchołkach.

### Weryfikacja

- Do repozytorium dodano `weryfikacja/rozdzial13_krzywizna.py`,
  aby rachunki dało się odtworzyć później. Uruchomienie:
  `uv run --with sympy python weryfikacja/rozdzial13_krzywizna.py`.
  Skrypt nie modyfikuje książki i nie zapisuje plików wynikowych.
- Skrypt wyprowadza Christoffela i Riemanna z metryki Kerra,
  sprawdza Ricciego, wszystkie 36 pozycji tabeli oraz pełną
  kontrakcję. Oddzielnie sprawdza zmianę współrzędnych na horyzoncie
  i wyznacznik metryki. Wszystkie kontrole przeszły poprawnie.
- Tożsamość 4D Pfaffianu sprawdzono dodatkowo na pięciu ogólnych
  algebraicznych tensorach krzywizny z dokładnymi całkowitoliczbowymi
  składowymi mieszanymi, zbudowanych z iloczynów Kulkarni–Nomizu.
  Jest to kontrola rachunku, nie zastępstwo dowodu.
- Kontrola źródła potwierdziła, że zmiany dotyczą tylko rozdziału 13;
  wcześniejsze i późniejsze rozdziały zachowano dokładnie. Sprawdzono
  unikalność etykiet, istnienie odsyłaczy, parowanie środowisk i osiem
  ilustracji. Pobranie stanu serwera nie wykazało nowych zmian.
- Punkty odniesienia: [kurs Davida Tonga](https://davidtong.org/teaching/general-relativity/grhtml/S6)
  oraz wskazane już w rozdziale źródła twierdzeń porównawczych
  i Gaussa–Bonneta. Nową tabelę Kerra i wzór przedłużenia sprawdzono
  bezpośrednio z metryki, niezależnie od tabel z literatury.

### Kontrola końcowa

- Obejrzano wszystkie 33 strony rozdziału (222–254 PDF), a osiem
  ilustracji również w większej rozdzielczości. Po poprawkach ponownie
  obejrzano rysunki siodła, wykres porównawczy i brzeg Gaussa–Bonneta.
  Przy rysowaniu siodła poprawiono nawiasowanie kwadratów ujemnych
  parametrów w TikZ i podniesiono kierunek obserwacji, by uniknąć
  nakładania się fragmentów rzutu.
- Końcowa kompilacja lokalnym MiKTeX: 310 stron, bez błędów,
  niezdefiniowanych odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostał wcześniejszy `Underfull` w późniejszym rozdziale i trzy
  wcześniejsze automatyczne zmiany ustawienia ilustracji `h` na `ht`.
- Wbudowany kompilator zwrócił nieznany status; wynik potwierdza
  ukończona kompilacja lokalna. Zaktualizowano PDF razem ze źródłem.
- Końcowe kontrole zakresu i `git diff --check` przeszły poprawnie.
  Repozytorium zawiera również skrypt do samodzielnego ponowienia
  rachunków Kerra i Pfaffianu.

Następna iteracja: rozdział 14 — „Twierdzenie Sarda i transwersalność”.

## Iteracja 14 — Twierdzenie Sarda i transwersalność (2026-10-04)

Przeczytano cały rozdział: dowód Sarda, transwersalny przeciwobraz,
iloczyn włóknisty, brzeg, transwersalność parametryczną, przybliżanie
względne, zera przekrojów, gęstość funkcji Morse'a i lokalny wymiar
przestrzeni trajektorii. Pobranie zmian potwierdziło aktualność gałęzi.

- Wyjaśniono domyślne założenia: brak brzegu, Hausdorff, drugi
  aksjomat przeliczalności i znaczenie podrozmaitości z topologią
  podprzestrzeni. Domkniętość podrozmaitości nadal jest osobnym
  założeniem tam, gdzie jest potrzebna.
- Doprecyzowano definicję zbioru miary zero w mapie i lokalny
  argument Lipschitza na zwartej kostce. W dowodzie Sarda podano
  otwarte dziedziny przekrojów h_t zamiast całych przestrzeni.
  Sprawdzono indukcję, mierzalność obrazów, Fubiniego i oszacowanie
  Taylora; zasadniczy czterostopniowy dowód jest poprawny.
- Wyjaśniono zastosowanie Sarda osobno do wnętrza i brzegu oraz
  siłę warunku regularności ograniczenia do brzegu.
- Poprawiono lokalny zapis mapy plasterkowej i słowo
  „odzwierciedlenie” na „odwzorowanie”. W twierdzeniach o przecięciu,
  iloczynie włóknistym, brzegu i zerach przekrojów zaznaczono możliwy
  pusty przeciwobraz. Dla skończoności przecięcia wystarcza zwartość
  jednego zbioru i domkniętość drugiego; sama dyskretność nie wystarcza.
- Rozpisano argument przy brzegu: gładkie przedłużenie przez r = 0,
  odwracalny minor po zmiennych stycznych i funkcja odwrotna
  zachowująca współrzędną brzegową. Omówiono przypadki m < c i m = c.
- W transwersalności parametrycznej rozpatrzono również przestrzeń
  parametrów wymiaru zero, do której podana wersja Sarda nie stosuje
  się bezpośrednio. Wersję brzegową wyprowadzono z rzutów wnętrza W
  i jego brzegu, obu będących rozmaitościami bez brzegu.
- Dodano brakującą definicję używanej topologii C^r/C^infinity na
  zwartej dziedzinie. Wyjaśniono różnicę między kontrolą każdego
  skończonego rzędu a jednym wspólnym oszacowaniem wszystkich rzędów.
- Uzasadniono jednostajną zbieżność skonstruowanej rodziny w każdym
  C^r i homotopię w wypukłej kuli parametrów. W dowodzie względnym
  otwartość zastosowano do zwartego podzbioru, bez traktowania jego
  domknięcia jako gładkiej rozmaitości. Cała homotopia jest stała
  na zachowywanym otoczeniu C.
- Wyjaśniono kanoniczną pochodną pionową przekroju w zerze oraz
  brak zer przekroju transwersalnego, gdy r > m. Rozpisano prawo
  transformacji hesjanu i zgodność z hesjanem kowariantnym z rozdziału 13.
- Dopisano zwarte nośniki funkcji odcinających w konstrukcji Morse'a;
  w przykładzie na R² „małość” perturbacji dotyczy zbiorów zwartych.
- W zapowiedzi Smale'a wyjaśniono niezależność indeksu od metryki,
  potrzebę istnienia trajektorii na odpowiedniej półprostej czasu
  i lokalne użycie gałęzi immersji. Prostowanie pola stosuje się
  do pola na przecięciu. Oddzielono izolację od skończoności oraz
  lokalny iloraz od globalnego ilorazu Hausdorffa.
- Poprawiono wykres rodziny t² - a: wcześniej rysowano 0,62 t² - a.
  Obecnie wszystkie trzy panele i zaznaczone zera odpowiadają
  dokładnie parametrom -1/2, 0 i 1/2 oraz wzorowi w podpisie.

### Kontrola końcowa

- Obejrzano wszystkie 11 stron rozdziału (255–265 PDF), a wszystkie
  cztery ilustracje również w większej rozdzielczości. Okręgi
  poziomic, transwersalność prostych, parabole i kierunki przepływu
  siodła są zgodne z tekstem. Poprawiona rodzina parabol ma zera
  w zaznaczonych punktach t = ±sqrt(1/2).
- Zweryfikowano zmianę hesjanu przez regułę łańcucha, rangi
  różniczek w iloczynie włóknistym i transwersalności parametrycznej,
  oraz wymiar przecięcia i lokalnego ilorazu trajektorii. Nie dodawano
  testów odtwarzających sam tekst dowodów.
- Kontrola źródła względem początku iteracji potwierdziła, że
  zmiany dotyczą wyłącznie rozdziału 14. Etykiety są unikalne,
  odsyłacze istnieją, środowiska są sparowane; `git diff --check`
  nie wykazał błędów.
- Końcowa kompilacja lokalnym MiKTeX: 312 stron, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostał wcześniejszy `Underfull` w późniejszym rozdziale oraz
  trzy wcześniejsze automatyczne zmiany położenia ilustracji `h` na `ht`.
  Wbudowany kompilator ponownie nie potwierdził statusu; wynik
  potwierdza kompilacja lokalna. Zaktualizowano PDF.
- Porównano zakres twierdzeń z [wykładem 3 A. Rittera](https://people.maths.ox.ac.uk/ritter/morse-cambridge/lecture03.pdf),
  [wykładem 4](https://people.maths.ox.ac.uk/ritter/morse-cambridge/lecture04.pdf)
  i [notatkami M. Mügera](https://www.math.ru.nl/~mueger/diff_notes.pdf).
- Podczas końcowego pobrania wykryto commity `5915d4a` i `57de31e`,
  dodające i aktualizujące `do_zrobienia.md`. Włączono je przez
  fast-forward, zachowując plik bez zmian. Lista jest materiałem
  do końcowej propozycji rozszerzeń; nie rozszerza bieżącej iteracji.

Następna iteracja: rozdział 15 — „Zanurzenia i otoczenia podrozmaitości”.

## Iteracja 15 — Zanurzenia i otoczenia podrozmaitości

Punkt wyjścia: `bde2d8d`. Przeczytano cały rozdział, łącznie
z dowodami obu twierdzeń Whitneya i czterema ilustracjami.
Pobranie zmian przed rozpoczęciem iteracji nie wykazało nowych commitów.

### Matematyka, terminologia i kompletność

- Ustalono domyślny brak brzegu, z wyraźnymi wyjątkami dla kołnierzy
  i wyczerpań. Ujednolicono „zanurzenie” w części o izotopiach.
  W dowodzie słabego twierdzenia Whitneya wybór skończonych map
  zachowuje pokrycie; nie polega na dowolnym zmniejszeniu ich dziedzin.
- W lemacie o dysku Whitneya dopisano zwartość M. Jest potrzebna
  w podanym dowodzie do skończoności par oraz oddzielenia otoczenia
  ruchu od pozostałego obrazu immersji. Samo założenie immersji
  nie wyklucza gromadzenia się innych płatów.
- Rozpisano względne położenie ogólne dysku: perturbacje wartości
  i różniczki funkcjami odcinającymi, kowymiar warstw macierzy
  niepełnego rzędu, następnie eliminacja samoprzecięć i przecięć
  z M. Sam ujemny oczekiwany wymiar samoprzecięć nie dowodzi immersji.
- Doprecyzowano obramowanie dysku: przedłużamy rozkład na dwie
  podwiązki; na drugim łuku przepisujemy dopełnienie kierunków
  drugiego płata. Dowiedziono potrzebnej własności grupy podstawowej
  grassmannianu przez jego zorientowane nakrycie i wiązania grup SO.
  Wyjaśniono rolę przeciwnych znaków oraz różnicę między przedłużeniem
  rozkładu a przedłużeniem dowolnej pełnej ramki na brzegu.
- Dodano jawny model ruchu dwóch wykresów w dysku Whitneya,
  sposób pogrubienia i powód niezależności użycia późniejszego
  twierdzenia tubularnego. Uściślono zastosowanie tego twierdzenia
  do powierzchni przedłużonej poza brzeg i naroża dysku.
- Uzupełniono graniczny argument dla siecznych, skończoną rodzinę
  perturbacji usuwających trójki, weryfikację rangi immersji W,
  standardowe sklejenie M z przebitą sferą i skończoność składowych.
  W zanurzeniu RP² zaznaczono normalizację współrzędnych jednorodnych.
- Dowód tubularny działa teraz dla dowolnej ustalonej metryki g.
  Poprzednio dowód zmieniał ją w przypadku niezwartym. Zastąpiono
  zmianę metryki jednolitym oszacowaniem zmiany wartości funkcji
  wyczerpującej na krótkich wektorach nad zwartym zbiorem.
  Wyjaśniono też zgodność map wykładniczych po ograniczeniu do
  otwartego otoczenia niedomkniętej podrozmaitości.
- W homologii wskazano abelową grupę współczynników. Rozróżniono
  otwarty dysk wiązki i domknięty dysk używany w danych chirurgii;
  uzasadniono wspólny promień dla nieortonormalnego obramowania.
- Zastąpiono niepełny globalny argument kołnierzowy dowodem
  z jednoznaczności trajektorii: spotkanie dwóch trajektorii
  wymuszałoby powrót jednej z wnętrza na brzeg. Podano konstrukcję
  gładkiej zmiennej szerokości i różniczkę w każdym punkcie kołnierza.
  Usunięto zbędne założenie pomocniczej zupełnej metryki.
- W podwojeniu sprawdzono Hausdorffa i przeliczalną bazę.
  Rodzinę kołnierzy przy zwartym brzegu przedłużono do izotopii
  ustalonej na brzegu, co uzasadnia dyfeomorfizm podwojeń.
  Wyjaśniono zmianę metryki przy przenoszeniu map tubularnych izotopią.
- Dopisano ciągłość w definicji wyczerpania, względną zwartość
  użytego pokrycia i wspólne otoczenie zerowania ogona szeregu.
  Przy konstrukcji Morse'a ustalono porównywalne normy pochodnych
  oraz przesunięto końcową funkcję do wartości nieujemnych: teraz
  wszystkie podpoziomice są zwarte. Sama właściwość funkcji do R
  nie zapewnia tego bez ograniczenia od dołu.
- W dowodzie zupełności uwzględniono brzeg i rozmaitości niespójne.
  W twierdzeniu o pasie dopisano cofanie przepływu do poziomicy a
  i przypadek pustej poziomicy; poprawiono składnię założenia.

### Ilustracje

- Dysk Whitneya: zastąpiono niezależne krzywe Béziera dwiema
  parabolami. Zaznaczone punkty są teraz dokładnie ich przecięciami,
  a wypełnienie ma granicę na obu narysowanych łukach.
- Otoczenie tubularne: użyto jednej analitycznej krzywej i jej
  jednostkowych normalnych. Strzałki są rzeczywiście prostopadłe,
  a brzegi pasa stanowią odsunięcia wzdłuż tych normalnych.
- Kołnierz: wyróżniono trajektorię wskazanego punktu p i przeniesiono
  jej podpis do właściwej strzałki.
- Pas bez punktów krytycznych: poziomice wyprostowano we współrzędnych
  produktowych przepływu i opisano te współrzędne w podpisie.
  Etykieta pola nie zasłania już strzałek.

### Kontrola końcowa

- Zakres argumentu Whitneya porównano z
  [wykładami T. Mrowki 21–22](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/d0598b3b5ced2d2d0a9884ee14abeae3_lecture21_22.pdf).
  Dodatkowe rachunki rang, model ruchu, szczegóły zwartości i dowód
  własności grassmannianu rozpisano bezpośrednio w tekście.
- W ostatnim sprawdzeniu rozwinięto również argument o podnoszeniu
  pętli i dysków w wiązaniach grup SO. Nie pozostawiono samego
  powołania się na długi ciąg homotopii wiązania: wyjaśniono potrzebne
  własności przez lokalne trywializacje oraz znikanie π₁ i π₂ sfer
  wymiaru co najmniej trzy.
- Skontrolowano wszystkie 15 stron rozdziału (266–280 PDF), a cztery
  ilustracje także w większej rozdzielczości. Po kontroli przeniesiono
  jeszcze podpis trajektorii poza linię ograniczającą pas kołnierza.
- Zweryfikowano rachunki różniczek, warstwy macierzy rzędu r,
  rozkład wiązki normalnej, indeksy promieni nad pierścieniami
  wyczerpania oraz odwrotność mapy produktowej z przepływu.
  Dla krzywej ilustracji normalna ma postać (-h',1)/sqrt(1+h'²),
  więc jej iloczyn skalarny ze styczną (1,h') jest równy zeru.
- Kontrola względem początku iteracji potwierdziła, że źródło
  poza rozdziałem 15 nie zmieniło się. Etykiety są unikalne,
  odsyłacze istnieją i środowiska są sparowane; `git diff --check`
  nie wykazał błędów.
- Końcowa kompilacja lokalnym MiKTeX daje 315 stron, bez błędów,
  brakujących odsyłaczy, żądań powtórzenia kompilacji i `Overfull`.
  Zaktualizowano PDF. Wbudowany kompilator
  nie potwierdził statusu; wynik sprawdzono lokalnie. Pozostał
  wcześniejszy `Underfull` w późniejszym rozdziale i trzy wcześniejsze
  automatyczne zmiany położenia ilustracji `h` na `ht`.
  Błąd kolizji nazwy pomocniczej funkcji TikZ z nazwą wbudowaną
  usunięto, nadając funkcjom rysunku odrębne nazwy.
- Końcowe pobranie zmian z repozytorium nie wykazało nowych commitów.

Następna iteracja: rozdział 16 — „Przecięcia, dualność i klasy charakterystyczne”.

## Iteracja 16 — Przecięcia, dualność i klasy charakterystyczne

Punkt wyjścia: `f3d1458`. Pobrano zmiany (repozytorium aktualne)
i przeczytano wszystkie dziesięć sekcji oraz cztery ilustracje.

### Zmiany i ich uzasadnienie (uzupełniane podczas przeglądu)

- Iloczyn kubkowy zdefiniowano także nad Z i wskazano rosnący
  porządek wierzchołków. Poprawiono dowód reguły Leibniza:
  skracają się dwa dodatkowe wyrazy prawej strony, a nie wyrazy
  lewego kobrzegu. Dopisano znak przy zmianie drugiego czynnika.
- Zastąpiono nieuzasadnione utożsamienie końców pryzmatu z dwiema
  przekątnymi konstrukcją homotopii łańcuchowej między mapą
  Alexandera–Whitneya i jej zamianą czynników. Wypełnienia cykli
  istnieją w ściągalnych kompleksach przypisanych sympleksom.
- Dodano brakującą definicję iloczynu kapowego, jego wzór na brzeg
  i zgodność ewaluacji z iloczynem kubkowym. Ustalono jedną
  kolejność czynników dla dalszych rachunków znaków.
- W dualności wyprowadzono jawnie znak (-1)^(k+1) przy brzegu
  komórki dualnej. Usunięto arbitralną zmianę orientacji stopni,
  która bez komentarza zmieniałaby znak deklarowanej mapy kapowej.
  Podano ewentualny czynnik przeskalowania i argument homotopii
  porównującej mapę komórek dualnych z iloczynem kapowym.
- Przy brzegu rozróżniono klasę względną i lokalną homologię:
  ta ostatnia w punkcie brzegu jest zerowa. System orientacji
  określa się tam przez przestrzeń styczną lub kołnierz.
  Uzupełniono jedyność klasy względnej, jej brzeg i przypadek n=0.
- Wyjaśniono, dlaczego dualne komórki do sympleksów niebrzegowych
  tworzą podkompleks obliczający homologię M: wnętrze cofa się
  na niego przez normalizację wag barycentrycznych, a kołnierz
  porównuje wnętrze z całą rozmaitością.
- Uściślono abelowość grup współczynników. W klasyfikacji przez
  równik dopisano normalizację całej homotopii, nie tylko pojedynczej
  mapy, aby uzasadnić użycie opartych grup homotopii, i wymaganie
  zachowania orientacji przez izomorfizmy. Podano jawnie obie
  względne wersje dualności ze skręconymi współczynnikami.
- Równość przecięcia i iloczynu kubkowego uzasadniono całkowitymi
  względnymi klasami Thoma, wycięciem i lokalizacją na punktach
  przecięcia. Rachunek form przy punkcie służy tylko kontroli
  orientacji; nie zastępuje argumentu nad Z.
- Uzupełniono przejście od znaków funkcji przejścia w definicji
  w₁ do kohomologii singularnej przez monodromię pętli i H¹.
  Dopisano gładkość ram i wygładzenie homotopii w sklejaniu wiązek.
- W konstrukcji wᵢ dopisano brakujące uzasadnienie bazy
  1,x,…,x^(r−1) na włóknie projektowym: hiperpłaszczyzny są dualne
  do w₁ tautologicznej linii, a ich transwersalne przecięcia
  wykrywają kolejne potęgi. Uwzględniono rząd zero i zgodność
  nowego współczynnika w₁ z wcześniejszą definicją przez wyznaczniki.
- Rozdzielono niezależną klasę Eulera modulo 2 od nazwy wᵣ.
  Najpierw dowodzi się jej własności z klasy Thoma, potem
  e₂(L)=w₁(L) dla linii, a dopiero przez rozszczepienie e₂(E)=wᵣ(E).
  Dzięki temu argument dla sumy Whitneya nie zakłada swojego wniosku.
- Dopisano uzasadnienie zgodności w₂ z przeszkodą spinową:
  redukcję do 2-szkieletu, rozszczepienie części trywialnej,
  płaszczyznową klasę Eulera i parzystość nawinięcia w SO(2).
- W dowodzie Thoma zbudowano globalny kocykl w kompleksie
  komórkowym pary, zamiast uznawać lokalne generatory za automatycznie
  sklejone. Uściślono jedyność, niezwartą bazę, zapominanie względności
  przed cofnięciem do zera i iloczyn względny dla sumy wiązek.
- W twierdzeniu o zerach ustalono orientację „normalna, styczna”
  i cofnięcie klasy pary (E,E bez przekroju zerowego).
  Przy samoprzecięciu podano konieczne założenie orientacji otoczenia
  oraz konkretną orientację normalnej „styczna, normalna”.
  Macierz blokowa bezpośrednio potwierdza znak lokalnego stopnia.
- W indeksie zera uzasadniono niezależność od mapy i wskazano
  konwencje n=1 oraz n=0. Doprecyzowano użycie funkcji uwikłanej
  z parametrem przy krótkim przepływie, wykluczając dodatkowe
  punkty stałe zarówno blisko zer, jak i na zwartym dopełnieniu.
- Zastąpiono skrótowy rachunek śladu Lefschetza obliczeniem klasy
  przekątnej w dualnych bazach kohomologii. Wyprowadzono wszystkie
  znaki, lokalną macierz grafu i przekątnej oraz przejście do śladu;
  potrzebną formułę Künnetha nad Q uzasadniono na kompleksach.
- Dla formy przecięcia podano termin „unimodularna”, konkretny
  znak izomorfizmu z kratą dualną i niezależność od reprezentantów
  modulo torsja. Symetrię wyprowadzono z iloczynu kubkowego,
  bez założenia, że każda klasa ma reprezentanta podrozmaitościowego.
- W chirurgii rozróżniono wymiar operowanej sfery i indeks uchwytu
  jej śladu. Ustalono sklejenie wyznaczone przez obramowanie,
  rolę kołnierzy i warunek zachowania orientacji. Dwa walce dają
  torus przy odpowiednim sklejeniu; bez tego warunku możliwa jest
  butelka Kleina. Uzupełniono rachunek charakterystyki Eulera.

### Ilustracje i kontrola końcowa

- W komórce dualnej użyto dokładnych barycentrów, a podpis
  przeniesiono do wnętrza dysku, aby nie przecinał krawędzi triangulacji.
- Na sferze zastąpiono dowolne pionowe strzałki rzutami rzeczywistych
  południkowych trajektorii gradientu wysokości. Podano wzór pola.
- Dodano niezależny, niewymagający bibliotek skrypt
  `weryfikacja/rozdzial16_znaki.py`: 8540 par bazowych kołańcuchów
  dla Leibniza, 247 przypadków wzoru kapowego oraz 128 macierzy
  dla porównania klasy przekątnej z det(I−A) w wymiarach 1–4.
  Wszystkie kontrole przechodzą. Zakres skryptu jest rachunkowy;
  nie zastępuje dowodów dualności, triangulacji czy twierdzenia Thoma.
- Obejrzano cały rozdział (17 stron, 281–297 PDF), a wszystkie
  cztery ilustracje również w większej rozdzielczości. Rysunki
  torusa i sklejania wiązki na równiku zachowano po kontroli.
- Sprawdzono dodatkowo porządek orientacji w samoprzecięciu,
  względny charakter przeszkody w₂ na 2-komórce oraz brak
  cyklicznej zależności między klasą Thoma i konstrukcją wᵢ.
- Końcowa kompilacja lokalnym MiKTeX: 319 stron, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji, `Overfull`
  i `Underfull`.
  Wbudowany kompilator nie potwierdził statusu; wynik zweryfikowano
  lokalnie. Pozostały trzy wcześniejsze zmiany położenia ilustracji
  `h` na `ht`. Przeredagowanie początku dowodu Thoma usunęło
  wcześniejszy `Underfull`; skład tego akapitu obejrzano.
  Zaktualizowano PDF.
- Kontrola zakresu względem `f3d1458` potwierdziła, że źródło
  poza rozdziałem 16 jest identyczne. Wszystkie etykiety są unikalne,
  odsyłacze istnieją, środowiska są sparowane i `git diff --check`
  przechodzi. Końcowe pobranie nie wykazało nowych commitów.
- Konwencję kapową i zakres twierdzeń porównano z
  [A. Hatcherem, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
  a zależności w konstrukcji klas z
  [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf)
  oraz [wykładami R. Cohena](https://math.stanford.edu/~ralph/bookR4.pdf).
  Rozwinięcia dowodów i kontrole rachunkowe zapisano w repozytorium.

Następna iteracja: rozdział 17 — „Teoria Morse'a: punkty krytyczne, uchwyty i przepływ”.

## Iteracja 17 — Teoria Morse'a: punkty krytyczne, uchwyty i przepływ

Punkt wyjścia: `f3222f9`; pobranie zmian na początku iteracji
nie wykazało nowych commitów. Przegląd obejmuje cały rozdział 17.

### Matematyka i uzupełnienia dowodów

- W lemacie Morse'a wyjaśniono gładkość pierwiastka macierzy
  przez lokalnie jednostajną zbieżność szeregów pochodnych.
  Osobno uwzględniono indeksy 0 i n, bez odwracania pustych bloków.
- Poprawiono sprzeczne założenie przy uchwycie: regularne są
  końce a,b, natomiast c=f(p) jest wartością krytyczną.
- Zastąpiono nieuzasadnioną globalną deformację za pomocą pola Y
  jawnym uchwytem H={|v|≤r, |u|²≤ε+|v|²}. Podano jego parametryzację
  i dokładne przecięcie z dolną podpoziomicą. Poprzednie twierdzenie,
  że tylko punkty v=0 mogą nie dojść do dolnego poziomu, było błędne:
  w obszarze μ=0 także inne punkty mogą asymptotycznie zbiegać do rdzenia.
- Uzasadniono zaokrąglanie naroży z zachowaniem poprzeczności,
  skończony i gładki czas trafienia oraz produktową postać dopełnienia.
  Przy przejściu od uchwytu do komórki użyto homotopii mapy
  przyczepienia i kołnierzy. Samo kurczenie czynnika poprzecznego
  nie unieruchamia punktowo pierwotnej części przyczepianej.
  Doprecyzowano wycięcie i przypadki skrajnych indeksów.
- Aproksymację komórkową umieszczono w każdym kroku indukcji
  budującej CW, zanim nowa komórka zostanie dołączona.
- Rozszerzono dowód rozmaitości stabilnej na dowolną gładką metrykę,
  zgodnie z zakresem późniejszych twierdzeń. Podano liniowy rozkład
  spektralny, równania całkowe, normę z wagą wykładniczą, oszacowanie
  kontrakcji, gładką zależność i globalne przedłużenie kołnierzem.
  Dla metryki euklidesowej podano jawną parametryzację przez R^m.
- Iloraz trajektorii zidentyfikowano z globalnym przekrojem regularnym,
  uzasadniając jego strukturę rozmaitości i własność Hausdorffa.
  Rozróżniono przecięcie rozmaitości immersowanych od założenia,
  że ich obrazy są globalnie osadzone.
- W dowodzie gęstości metryk Morse'a–Smale'a użyto stałych lokalnych
  sfer oraz map pierwszego trafienia. Warunki z czasami ≤N są otwarte
  i gęste; zwartość parametrów uzasadnia oba stwierdzenia.
  Wyjaśniono przestrzeń Baire'a i zachowanie metryki blisko punktów
  krytycznych. Poprzednie „zwarte fragmenty” zależały od zmienianej metryki.
- Dodano osobny lemat o zwartości z przełamaniami: wybór podciągu
  na skończenie wielu poziomach, ograniczenie czasu w regularnym paśmie,
  wykluczenie skoku między różnymi punktami tej samej wartości
  przez oszacowanie spadku ≥ długość razy dolne ograniczenie gradientu,
  zachowanie końców i topologię przestrzeni trajektorii łamanych.
- Sklejanie trajektorii rozpisano na mapy wykresów i jawne równania
  θ=A(δρω), ω=B(δρθ); ich różniczka przy ρ=0 jest identycznością.
  Dla ogólnej metryki dodano problem z mieszanymi warunkami końcowymi
  oraz oszacowania map przejścia. Nie założono nieuprawnionej gładkiej
  linearyzacji gradientu. Do brzegu przestrzeni jednowymiarowej wystarcza
  kołnierz topologiczny, gładki we wnętrzu; nie twierdzimy, że ewaluacja
  jest gładka na brzegu w dowolnie wybranym parametrze.
- Ustalono orientację przekroju przez kolejność „X, przekrój”
  oraz koorientację rozmaitości stabilnej. W dowodzie ∂²=0
  oddzielono iloczyn znaków trajektorii od wspólnego znaku konwencji
  zależnego wyłącznie od wymiarów, który nie wpływa na zerowanie sumy.
- Porównanie z homologią komórkową przebudowano wokół filtracji
  według indeksów. Jawnie wskazano odwołanie naprzód do geometrycznego
  twierdzenia o przestawianiu w rozdziale 18 i brak zależności kołowej.
  Zmiana funkcji zachowuje pole i trajektorie; podano metrykę realizującą
  to samo pole jako ujemny gradient nowej funkcji.
- Generatory względne reprezentują dyski niestabilne przedłużone
  do wspólnego poziomu; współczynniki odczytują współrdzenie stabilne.
  Wyjaśniono osiąganie poziomu, lokalny stopień i zgodność znaków.
  Usunięto niepoprawny termin „kokorem”; użyto „współrdzeń”.

### Ilustracje i kontrola

- W lokalnych poziomicach tło zmieniono na neutralne, aby niebieski
  oznaczał wyłącznie podpoziomicę.
- Rysunek uchwytów zastąpiono widokiem z góry z dokładnymi szwami
  na brzegach. Poprzednia perspektywa pokazywała końce mostka wewnątrz dysków.
- Na sferze użyto rzeczywistych rzutów południków zamiast dowolnych krzywych.
  Równik pokazano jako odcinek, zgodnie z tym samym rzutem prostopadłym.
- Sprawdzono rachunek czterech punktów krytycznych przechylonej wysokości
  torusa, nierówności Morse'a i dowód twierdzenia Reeba; zachowano wyniki.
- Kontekst i zakres twierdzeń porównano z
  [wykładami R. Cohena](https://math.stanford.edu/~ralph/morsecourse/biglectures.pdf),
  [wykładami A. Rittera](https://people.maths.ox.ac.uk/ritter/morse-cambridge/full.pdf)
  i [pracą J. Webera](https://arxiv.org/abs/math/0411465).
  Dodano odsyłacz do tej ostatniej pracy w dalszej lekturze.
- Kontrola zakresu względem `f3222f9`: poza rozdziałem 17 źródło
  pozostało identyczne. Etykiety są unikalne, odsyłacze istnieją,
  środowiska są sparowane; rozdział zawiera pięć ilustracji.
- Obejrzano wszystkie 15 stron rozdziału (298–312 PDF) i każdą
  z pięciu ilustracji w większej rozdzielczości. Rysunek torusa
  oraz schemat trajektorii łamanej zachowano po kontroli.
- Końcowy skład lokalnym MiKTeX: 322 strony, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji, `Overfull`
  i `Underfull`. Pozostały trzy wcześniejsze ostrzeżenia zmieniające
  położenie ilustracji z `h` na `ht`. Wbudowany kompilator zwrócił
  nieznany status, dlatego wynik zweryfikowano lokalnie.
  Zaktualizowano PDF. `git diff --check` przechodzi.
- Ponowne pobranie zmian przed zapisem nie wykazało nowych commitów.

Następna iteracja: rozdział 18 — „Kobordyzmy i rachunek uchwytów”.
Przy jego przeglądzie trzeba również sprawdzić zgodność twierdzenia
o przestawianiu z używaną tutaj wersją zachowującą pole spadku.

## Iteracja 18 — Kobordyzmy i rachunek uchwytów

Punkt wyjścia: `af689aa`; pobranie zmian na początku iteracji
nie wykazało nowych commitów. Przegląd obejmuje cały rozdział 18.

### Poprawki i ich uzasadnienie

- Ustalono wymiar m≥1 oraz konwencję kobordyzmu zorientowanego
  ∂W=(−N₋)∐N₊. Usunięto sugestię, że całkowity kompleks uchwytów
  wymaga orientowalnego W: wystarczają orientacje rdzeni
  i koorientacje sfer pasa.
- Poprawiono dobór regularnych pasów w rozkładzie uchwytowym,
  uwzględniając brak punktów krytycznych, pusty brzeg wejściowy
  i składowe rozpoczynające się uchwytem indeksu 0.
- Dla dysku zastąpiono F=|x|² przez F=(1+|x|²)/2.
  Poprzedni wzór naruszał F⁻¹(0)=∅. Wskazano także współrzędną
  kołnierza, w której nowa funkcja ma wymaganą postać 1−t.
- Przy śladzie chirurgii odróżniono wnętrze części przyczepianej
  od jej brzegu, który przed wygładzeniem leży na narożu.
- W przykładzie S²→T² dodano konieczny warunek przedłużenia orientacji.
  Drugie sklejenie pierścieni daje butelkę Kleina, więc samo usunięcie
  dwóch dysków i wartość χ=0 nie wystarczają do stwierdzenia, że to torus.
- Dla bloku uchwytów jednego indeksu uzasadniono sprowadzenie ich sfer
  do wspólnego poziomu i rozłączność małych pogrubień przez brak
  trajektorii między równymi indeksami. Jawnie zapisano różniczkę
  filtracji względnej i lokalną konwencję znaku TA→νB.
- Rozwinięto algebraiczne skracanie przy współczynniku ±1:
  zerowanie wiersza i kolumny oraz użycie ∂²=0 wydzielają ściągalny
  podkompleks. To nadal nie dowodzi jednego przecięcia geometrycznego.
- Zdefiniowano używane pole gradientopodobne spadku i wyjaśniono,
  jak realizować je jako gradient metryki. Definicja obejmuje
  dowolną metrykę, a nie tylko szczególny model euklidesowy.
- Przebudowano dowód przestawiania: zwarte, rozłączne ślady stabilny
  i niestabilny w poziomicy pozwalają skonstruować gładką funkcję ρ
  stałą wzdłuż trajektorii, równą 1 przy p i 0 przy q.
  Udowodniono gładkość także tam, gdzie trajektorie nie trafiają
  w tę poziomicę. Dwie rosnące reparametryzacje hₚ,h_q dają
  F̃=ρhₚ(F)+(1−ρ)h_q(F), z XF̃<0 i translacjami przy punktach krytycznych.
  Całe pole pozostaje niezmienione. Jest to dokładnie wersja
  wymagana w dowodzie homologii Morse'a w rozdziale 17.
- W przesunięciu uchwytu użyto równoległej kopii sfery q,
  wyznaczonej przez obramowanie, i wstęgi omijającej pozostałe dane.
  Wskazano dysk Dᵏ×{v₀} w nowym brzegu: izotopia przebiega tam,
  a nie po rdzeniu we wnętrzu kobordyzmu. Dalsze przyklejenia
  także trzeba przenieść przez otrzymany dyfeomorfizm.
  Ustalony pozostaje brzeg wejściowy N₋; nie obiecuje się
  punktowego unieruchomienia całej wcześniej dołączonej części.
- W znoszeniu pary uzupełniono dostosowaną wersję lematu Morse'a
  zachowującą odpowiedni dysk stabilny/niestabilny. Pole można
  zmienić lokalnie przez wypukłe sklejenie pól spadku; nie zakładamy
  gładkiej linearyzacji dowolnego pierwotnego gradientu.
- Dopasowanie przekrojów rozpisano na gładką izotopię przez skalowanie
  i rozkład blokowy z dopełnieniem Schura. Wyjaśniono warunek
  odwracalności bloku poprzecznego, wybór znaków i kontrolę nośnika.
  Izotopię realizuje pole styczne do poziomic, dodane do pola
  znormalizowanego; funkcja nadal ściśle maleje.
- Argument braku powrotów zastosowano po zmianie pola, z dwoma
  otoczeniami V⊂U. Modyfikacja usuwająca zera ma nośnik w V,
  a model obowiązuje w U. Dopisano, dlaczego wyjście z U uniemożliwia
  powrót do V i dlaczego wszystkie trajektorie docierają do brzegów.
  Przy budowie funkcji końcowej uzasadniono gładkość czasu trafienia.
- W warunkowym użyciu triku Whitneya doprecyzowano jednoczesny wybór
  rozłącznych dysków dla sparowanych przecięć. Warunek obramowania
  oznacza przedłużenie obramowania zadanego na brzegu, a nie samą
  trywialność wiązki normalnej dysku. Wskazano zakres wymiarów,
  gdy trzeba faktycznie wykonać ruch.
- Przy torsji Whiteheada odróżniono kompleks nad Z od kompleksu
  nakrycia uniwersalnego nad Z[π₁]. Usunięto zapowiedź nieistniejącego
  jeszcze dalszego rozdziału chirurgii; pozostaje propozycją rozbudowy.

### Ilustracje i weryfikacja

- Poprawiono podpis każdej podstawy 1-uchwytu: pojedyncza podstawa
  to {−1}×D² albo {1}×D², a nie całe S⁰×D². Rdzeń dochodzi teraz
  do obu podstaw, a strzałka sfery pasa trafia w jej rzeczywisty brzeg.
- Wykresy znoszenia są dokładnie funkcjami t³/3−t oraz t³/3+t/2;
  punkty krytyczne zaznaczono w (±1,∓2/3), zgodnie ze wzorem modelu.
- Na ilustracji przesunięcia dodano przerywaną równoległą kopię
  sfery q i doprowadzono wstęgę do tej kopii. Podpis odróżnia
  ją od pozostającej na miejscu sfery przyczepienia drugiego uchwytu.
- Kontekst dowodu znoszenia i zakres wyników porównano z
  [wykładem J. Morgana](https://www.math.columbia.edu/~jmorgan/Lecture_IIIA_hcobordism_Contd.pdf)
  oraz [książką A. Ranickiego](https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf).
- Obejrzano cały rozdział (12 stron, 313–324 PDF) oraz wszystkie
  pięć ilustracji w większej rozdzielczości. Rysunki chirurgii
  i przecięcia na torusie zachowano po kontroli; poprawiony schemat
  przesunięcia obejrzano ponownie. Sprawdzono także odsyłacze do lektur.
- Końcowy skład lokalnym MiKTeX: 324 strony, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji, `Overfull`
  i `Underfull`. Pozostały trzy wcześniejsze ostrzeżenia dotyczące
  zamiany położenia ilustracji `h` na `ht`. Wbudowany kompilator
  nie potwierdził statusu; wynik zweryfikowano lokalnie.
  Zaktualizowano PDF.
- Kontrola zakresu względem `af689aa` potwierdziła identyczność
  źródła poza rozdziałem 18, unikalność etykiet, poprawność odsyłaczy
  i sparowanie środowisk. `git diff --check` przechodzi.
  Ponowne pobranie przed zapisem nie wykazało nowych commitów.

Następna iteracja: ponowna kontrola rozdziału 1 po zmianach autora
pobranych podczas przeglądu późniejszych rozdziałów. Dopiero po niej
pozostaje końcowy audyt całości i lista propozycji rozbudowy do wyboru.

## Ponowny przegląd rozdziału 1 po zmianach autora

Punkt wyjścia: `7222128`. Ponownie sprawdzono fragmenty zmienione
od pierwszego przeglądu (`e144985`), w tym uzupełnienia autora
`0d9857f` i poprawkę relacji równoważności `5b259e6`.

### Matematyka, kolejność i język

- W przykładzie prostej z podwojonym początkiem dopisano dowód
  ciągłości map i ich odwrotności. Sama bijekcja nie wystarcza
  do stwierdzenia, że mapa jest homeomorfizmem.
- Analogicznie uzupełniono konstrukcję map CPⁿ: otwartość dziedzin,
  ilorazowość ograniczenia rzutowania, ciągłość ilorazów współrzędnych
  i odwrotności wstawiającej współrzędną 1. Dodano odsyłacz do
  późniejszego dowodu aksjomatu Hausdorffa i przeliczalności bazy,
  potrzebnych do uznania CPⁿ za rozmaitość.
- W dowodzie niezależności gładkości w punkcie od map ograniczono
  przeciwobraz do otoczenia, na którym wykazano ciągłość. Lokalna
  ciągłość nie uprawnia do uznania pełnego przeciwobrazu za otwarty.
  Przy złożeniu map doprecyzowano kolejność zmniejszania dziedzin.
- Obliczenia macierzy Jacobiego przejścia na RP² zachowano.
  Poprawny rachunek współrzędnych wektora stycznego przeniesiono
  za definicję przestrzeni stycznej i ogólną regułę zmiany współrzędnych.
  Dodano odsyłacze w obu kierunkach i przypomnienie map.
- Identyfikację RPⁿ z ilorazem sfery uzupełniono o zgodność topologii:
  ciągła normalizacja reprezentantów pozwala wykazać ilorazowość
  rzutowania ze sfery, bez zakładania z góry aksjomatu Hausdorffa.
- W RP¹→S¹, [z]↦z², uzasadniono ciągłość mapy indukowanej,
  zwartość dziedziny i zgodność współrzędnych kątowych z atlasem
  afinicznym (pochodne tangensa i cotangensa nie znikają).
- W modelu RP² jako dysku poprawiono zdanie o parach antypodalnych:
  dokładnie jeden punkt w otwartej półsferze mają pary spoza równika.
  Uzasadniono homeomorfizm ilorazu dysku, odwołując się do późniejszego,
  niezależnego dowodu własności Hausdorffa.
- Dla metryk na przestrzeniach rzutowych rozpisano nierówność trójkąta
  z dwiema fazami/znakami i symetrię. Uzupełniono brakujące przejście
  od ciągłości rzutowania ze sfery do ciągłości identyczności między
  pierwotnym ilorazem a przestrzenią metryczną: używa ono normalizacji
  i definicji topologii ilorazowej. Dopiero wtedy stosuje się argument
  zwartej dziedziny i przeciwdziedziny Hausdorffa.
- Poprawiono literówki w przykładzie x↦x³ i usunięto przypadkowy
  znacznik Markdown (trzy grawisy) ze źródła LaTeX.

### Ilustracje i weryfikacja

- Obejrzano wszystkie 42 strony rozdziału (4–45 PDF), a wszystkie
  15 ilustracji także w większej rozdzielczości. Na schemacie RP²
  usunięto pomocnicze średnice, które mogły sugerować sklejanie wnętrza
  dysku, i dodano wyraźny napis, że wnętrze nie podlega utożsamieniom.
  Strzałki w obu modelach doprowadzono bliżej wskazywanych par punktów.
- Symbolicznie sprawdzono wzory CP¹→S² w obu mapach, macierz Jacobiego
  przejścia RP² i jej wyznacznik; potwierdzono również zgodność rysunku
  rzutu stereograficznego ze wzorem i współliniowość zaznaczonych punktów.
- Kontrola zakresu względem `7222128` potwierdziła niezmienność źródła
  poza rozdziałem 1, unikalność etykiet, poprawność odsyłaczy,
  sparowanie środowisk i zachowanie wszystkich 15 ilustracji.
- Końcowy skład lokalnym MiKTeX ma 325 stron. Brak błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji oraz ostrzeżeń
  `Overfull` i `Underfull`; pozostają dwa ostrzeżenia o automatycznej
  zmianie położenia ilustracji z `h` na `ht`. Wbudowany kompilator
  nie potwierdził statusu, więc wynik zweryfikowano lokalnie.
  Poprawioną ilustrację obejrzano ponownie i zaktualizowano PDF.
- Pobranie zmian przed zapisem nie wykazało nowych commitów.
  `git diff --check` przechodzi.

Ponowny przegląd rozdziału 1 zakończony. Pozostaje końcowy audyt
spójności całości oraz lista propozycji rozbudowy do wyboru przez autora.

## Audyt końcowy i propozycje rozbudowy (2026-10-05)

- Pobrano zmiany PortableGit z dysku E; gałąź była aktualna.
- Porównano aktualną treść każdego z 18 rozdziałów z commitem
  kończącym jego przegląd. Wszystkie porównania są zgodne, w tym
  ponownie sprawdzony rozdział 1 po uzupełnieniach autora.
- Zestawiono 140 numerowanych sekcji, 87 numerowanych rysunków
  i końcowy zakres stron każdego rozdziału. Dodatkowe nienumerowane
  diagramy pozostają opisane we wcześniejszych kontrolach wizualnych.
- Sprawdzono znaczenie wszystkich międzyrozdziałowych odsyłaczy naprzód,
  szczególnie zależność dowodu homologii Morse'a od przestawiania
  wartości krytycznych w rozdziale 18. Nie wykryto nowej sprzeczności
  ani zależności kołowej w tych odwołaniach.
- Potwierdzono unikalność 964 etykiet, cele 860 odsyłaczy w źródle,
  sparowanie środowisk oraz cele 1028 wewnętrznych linków PDF.
  Plik PDF w repozytorium jest identyczny z ostatnim zweryfikowanym
  składem (325 stron); treści źródła i PDF w tej iteracji nie zmieniano.
- Dodano `AUDYT_KONCOWY.md` (obecnie scalony z tym dziennikiem): tabelę pokrycia,
  weryfikację zależności, wyniki kontroli i jawne granice zakresu.
- Dodano `PROPOZYCJE_UZUPELNIEN.md` (aktualny stan w [planie](PLAN_DZIALANIA.md)):
  12 ponumerowanych propozycji, informację, co już jest w książce,
  zakres nowych prac i sugerowaną kolejność. Uwzględniono życzenia
  z `do_zrobienia.md`, zachowując sam plik bez zmian.
- Rozdzielono dalszą redakcję i podstawy od pełnych h-/s-kobordyzmów,
  chirurgii, sfer egzotycznych i metod czterowymiarowych. Dla Poincarégo
  wskazano różnicę między kategorią topologiczną i gładką; status
  gładkiego problemu w wymiarze 4 sprawdzono w materiale Clay.
  Proponowanego nowego materiału nie dopisywano do skryptu.

Przegląd istniejących 18 rozdziałów i wymagane przygotowanie listy
dalszych uzupełnień są zakończone. Kolejne rozszerzenia zależą od wyboru autora.

## Kontynuacja po rozbudowie autora — podział źródeł (2026-10-05)

Na nową prośbę użytkownika pobrano zmiany do `19fa283` i porównano je
z `66b220f`. Autor rozbudował książkę do 27 rozdziałów i dodatku;
wersja ma 384 strony. Nowy zakres nie jest objęty historycznym audytem
18 rozdziałów. Dalsza kontrola jest rozpisana w `PLAN_DZIALANIA.md`.

- Potwierdzono obecność sekcji o rozmaitościach z brzegiem w rozdziale 1
  oraz konstrukcji grup wolnych i iloczynu wolnego w rozdziale 5.
  Nie dodawano powtórnych definicji. Zaktualizowano status wszystkich
  wcześniejszych propozycji wobec już dopisanej treści.
- Zgodnie z obecną prośbą użytkownika wydzielono 27 plików rozdziałów,
  preambułę, wstęp, dodatek i indeks — łącznie 31 plików wejściowych
  w `tex/`. Główny plik nadal składa tę samą książkę.
- Użyto `\input`, zachowując kolejność, wszystkie etykiety i istniejące
  polecenia przełamania strony. Pełny tekst po rozwinięciu importów
  jest identyczny z monolitycznym źródłem `19fa283` (po normalizacji
  zakończeń linii). Nie zmieniono w tym kroku treści matematycznej.
- Zmieniono nieaktualną zasadę jednego pliku w `AGENTS.md`; nadrzędna
  jest najnowsza prośba użytkownika o podział. Dodano w README opis
  struktury, kompilacji, zachowania etykiet i współpracy przez Git.
- Uruchomiono pełny `latexmk` z lokalnym MiKTeX przed podziałem i po nim.
  Zadziałał Perl już obecny w PortableGit — bez instalowania programów.
  `makeindex` przyjął 152 wpisy, bez odrzuceń i ostrzeżeń indeksu.
- Porównano wszystkie 384 strony: identyczny tekst, rozmiary,
  linki i obrazy renderowane w 72 dpi. Identyczne są spis treści,
  zakładki, dane indeksu i sam indeks. Wszystkie 31 importów istnieje,
  jest użyte dokładnie raz; nie pozostały osierocone pliki TeX.
- Potwierdzono unikalność 1159 etykiet i cele 1051 odsyłaczy w źródle;
  porównano 1553 linki PDF. Końcowy log nie zgłasza błędów,
  brakujących odsyłaczy ani potrzeby ponownego przebiegu. Zachowuje
  dwa wcześniejsze ostrzeżenia o zmianie `h` na `ht` i jedno `Underfull`;
  nie ma `Overfull`. Te komunikaty nie wynikają z podziału.
- Osobno porównano PDF pobrany od autora ze świeżym składem.
  Strony treści 1–382 są identyczne, lecz na stronach 383–384 stary
  indeks odsyłał o trzy strony za wcześnie (np. rozmaitość z brzegiem
  do s. 11 zamiast 14, grupa wolna do s. 98 zamiast 101).
  Pełny `latexmk` ponownie uruchomił `makeindex` po ustaleniu paginacji.
  Obejrzano obie poprawione strony indeksu i zaktualizowano PDF
  w repozytorium. To naprawa nieaktualnego indeksu, niezależna od podziału.
- Dokument `AUDYT_KONCOWY.md` oznaczono jako historyczny, aby nie
  przypisywać starego przeglądu nowo dopisanym rozdziałom.

Nowe rozdziały będą kontrolowane kolejno. Materiał o Freedmanie
i egzotycznych R⁴ pozostaje poza tym skryptem; istniejącego rozdziału
o sferach Milnora nie usuwano ani nie przenoszono bez potrzeby.

## Rozdział 1 — kontrola nowej sekcji o brzegu i uzupełnień autora

Zakres: zmiany autora od `66b220f`, po podziale źródeł w `9148128`.
Przeczytano nową sekcję o brzegu, dopisany rachunek struktury liniowej
na klasach krzywych oraz pozostałe różnice rozdziału 1.

- Zachowano poprawne definicje, dowód niezależności brzegu od map,
  przykłady dysku i okręgu oraz rozróżnienie naroży.
- Utrwalono domyślną konwencję „bez brzegu, o ile nie zaznaczono inaczej”.
  Wcześniejsze zdanie określało ją tylko do momentu wprowadzenia definicji
  brzegu, co mogło sugerować stosowanie dalszych twierdzeń o zanurzeniach
  i wartościach regularnych do dowolnych rozmaitości z brzegiem.
- W stwierdzeniu o wymiarze brzegu zapisano n≥1, aby teza n−1 nie
  obejmowała przyjętej osobno konwencji dla rozmaitości zerowymiarowych.
- Po konstrukcji przestrzeni stycznej dopisano pełne uzasadnienie modelu
  przy brzegu: zarodki, niezależność pochodnych od przedłużenia,
  reprezentacja każdej derywacji przez n współczynników i odwracalność
  przejść w punkcie brzegu. Wcześniejszą wzmiankę połączono z tym dowodem.
- Uzasadniono identyfikację T_p(∂M) z podprzestrzenią vⁿ=0 oraz fakt,
  że krzywe dwustronne reprezentują właśnie tę podprzestrzeń, nie całe
  T_pM. Przykład minimum ostatniej współrzędnej wyjaśnia brak kierunku
  poprzecznego w modelu krzywych. Podano też związek z derywacjami
  funkcji globalnych przez funkcję odcinającą.
- Dopisane przez autora wzory dodawania klas krzywych i mnożenia
  przez skalar są poprawne; zachowano je wraz z reparametryzacją γ(at).

- Kontrola struktury potwierdziła, że spośród źródeł TeX zmieniono
  wyłącznie rozdział 1. Wszystkie 1160 etykiet jest unikalnych,
  wszystkie 1053 odsyłacze mają cel, środowiska są sparowane,
  zachowano 15 rysunków rozdziału.
- Pełny `latexmk` przebudował dokument i indeks do 385 stron.
  Brak błędów, niezdefiniowanych odsyłaczy, `Overfull` i żądania
  kolejnego przebiegu. Pozostają wcześniejsze dwa `h`→`ht` i jedno
  `Underfull` w rozdziale 23, niezwiązane z tą zmianą.
- Obejrzano sekcję o brzegu (strony 13–15), zmieniony przez autora
  kolorystycznie rzut stereograficzny (21), nowy dowód i jego sąsiedztwo
  (34–36) oraz zaktualizowany indeks (384–385). Układ i odsyłacze są poprawne.
  Zaktualizowano PDF w repozytorium.

Kontrola nowych fragmentów rozdziału 1 zakończona. Następna iteracja:
nowy rozdział 5 z podstawami algebry, w tym grupą wolną i iloczynem wolnym.

## Scalenie dokumentacji projektu (2026-10-05)

Na prośbę użytkownika pozostawiono cztery pliki Markdown w katalogu głównym:
README (obsługa projektu), AGENTS (zasady), PRZEGLAD (historia i dowody kontroli)
oraz PLAN_DZIALANIA (jedyna aktualna kolejka i lista pomysłów).

- Z `AUDYT_KONCOWY.md` przeniesiono poniżej unikalną tabelę pokrycia,
  kontrolę zależności i dane techniczne starej wersji. Nie przenoszono
  powtórzonego opisu ukończenia prac jako statusu obecnej książki.
- Z `PROPOZYCJE_UZUPELNIEN.md` zachowano w planie numerację 1–12,
  stan wdrożenia, niewykonane elementy, granice zakresu i źródła.
- Z `do_zrobienia.md` włączono życzenia dotyczące redakcji rozdziału 1,
  zakończeń rozdziałów, brzegu, grup, h-/s-kobordyzmów, chirurgii,
  Poincarégo i struktur egzotycznych. Pokrywały się z propozycjami;
  nie utworzono kolejnych kopii tych samych zadań.
- Usunięto te trzy scalone pliki; ich pełne historyczne brzmienie zachowuje Git
  (m.in. `aa6c59a`). Poprawiono linki w README i dzienniku.
- Zachowano rozróżnienie torsji Whiteheada i triku Whitneya oraz Smale'a
  i Milnora; literówki w dawnej liście autora nie są nową terminologią.

### Historyczna rozbudowa autora — nie jest bieżącym audytem

Autor w `4233e60` i `b2635d0`, zamkniętych planem `19fa283`, dodał
brzeg, grupy i tensor modułów, nawigację oraz indeks, h-/s-kobordyzmy,
chirurgię (geometrię, przeszkodę Walla, ciąg dokładny), Poincarégo,
sfery Milnora, Cherna–Weila i katalog wyników zewnętrznych.
Algebrę abstrakcyjną wydzielił jako rozdział 5, przesuwając dawny rozdział 5
i kolejne o jeden. Jego plan deklarował zakończony przegląd własnych dodatków,
kontrolę torusów i schematów Walla, chirurgii, Poincarégo oraz Milnora,
skład 384 stron i 152 wpisy indeksu. Wspominał też przejściowe składy
381 stron i brak Perla w MiKTeX. To historia tamtej sesji, nie aktualna
instrukcja kompilacji; działający Perl z PortableGit opisuje README.

W planie autora głębokie wyniki (klasyfikacja powierzchni, geometryczne
lematy Walla, h-kobordyzm, twierdzenie Hirzebrucha) pozostawiono jawnie
zewnętrzne tam, gdzie nie ma pełnego dowodu. Zadań i teorii czterowymiarowej
nie włączono do zakresu. Trzy dodatkowe pomysły geometryczne zachowano
w aktualnym planie. Nasz przegląd nowych dowodów ma własne statusy.

### Archiwalne dane audytu 18 rozdziałów

Poniższe wyniki odnoszą się **wyłącznie do `a36c920`, PDF 325 stron**,
sprawdzonego 5 października 2026 przed rozbudową do 27 rozdziałów.
Numery rozdziałów i stron są historyczne.

### Pokrycie rozdziałów

Poniższa tabela została sprawdzona na aktualnym źródle, spisie treści PDF
i historii Git. Tekst każdego rozdziału jest identyczny z jego treścią
w podanym commicie kończącym odpowiedni przegląd. Późniejsze iteracje
nie nadpisały tych poprawek. Kolumna rysunków liczy numerowane środowiska
`figure`; dodatkowe nienumerowane diagramy również były objęte przeglądem
(np. diagram własności uniwersalnej w rozdziale 3).

| Rozdział | Sekcje | Rysunki | Strony PDF | Commit przeglądu |
|---|---:|---:|---|---|
| 1. Rozmaitości różniczkowe | 11 | 15 | 4–45 | `a36c920` |
| 2. Pola wektorowe, przepływy i pochodna Liego | 7 | 4 | 46–61 | `9bfa3af` |
| 3. Algebra tensorowa i zewnętrzna | 9 | 1 | 62–80 | `02ea77d` |
| 4. Grassmanniany, algebra Clifforda i spinory | 7 | 5 | 81–97 | `831cbcc` |
| 5. Algebra homologiczna: moduły, kompleksy i (ko)homologie | 10 | 1 | 98–114 | `4f017f4` |
| 6. Homotopia, nakrycia i komórkowe modele przestrzeni | 5 | 6 | 115–128 | `21a3ecb` |
| 7. Homologia przestrzeni | 8 | 3 | 129–142 | `3e871f0` |
| 8. Wyższe grupy homotopii i związek z homologią | 7 | 4 | 143–157 | `f7df0ae` |
| 9. Formy różniczkowe, orientacja i kohomologia de Rhama | 10 | 5 | 158–178 | `c4efcb0` |
| 10. Tensor metryczny, długość i miara | 8 | 2 | 179–196 | `3735830` |
| 11. Koneksje i transport równoległy | 6 | 2 | 197–207 | `4c29411` |
| 12. Geodezyjne, odwzorowanie wykładnicze i zupełność | 6 | 9 | 208–222 | `940a346` |
| 13. Krzywizna: od transportu równoległego do tensorów | 9 | 8 | 223–255 | `f03c9d3` |
| 14. Twierdzenie Sarda i transwersalność | 6 | 4 | 256–266 | `bde2d8d` |
| 15. Zanurzenia i otoczenia podrozmaitości | 7 | 4 | 267–281 | `f3d1458` |
| 16. Przecięcia, dualność i klasy charakterystyczne | 10 | 4 | 282–298 | `f3222f9` |
| 17. Teoria Morse'a: punkty krytyczne, uchwyty i przepływ | 7 | 5 | 299–313 | `af689aa` |
| 18. Kobordyzmy i rachunek uchwytów | 7 | 5 | 314–325 | `7222128` |

Razem: **18 rozdziałów, 140 numerowanych sekcji, 87 numerowanych rysunków,
325 stron PDF**. Strony w tabeli odnoszą się do końcowego PDF;
wcześniejsze numery stron w dzienniku opisują stan z dnia danej iteracji.

### Spójność między rozdziałami

- Odsyłacz 2→16 dotyczy przykładu nietrywialności TS² i jest jawnie
  opisany jako użycie klasycznego twierdzenia, nie podstawa konstrukcji
  pól wektorowych w rozdziale 2.
- Odsyłacz 3→5 porównuje już wykonaną faktoryzację przez iloraz
  z ogólnym twierdzeniem o izomorfizmie; konstrukcja tensorów ma własny dowód.
- Własności izometrii 10→11,13 są wyraźnie oddzielone jako zapowiedź
  koneksji i krzywizny. Pozostała część rozdziału 10 nie zależy od tej zapowiedzi.
- Odsyłacze 11→12,13 porównują przykłady z późniejszym wzorem geodezyjnej
  i objaśniają, dlaczego zerowanie symboli Christoffela w punkcie
  nie oznacza płaskości. Wzory koneksji wyprowadzono niezależnie.
- Odsyłacz 12→13 zapowiada drugą wariację i pola Jacobiego po dowodzie
  lokalnej minimalności; nie jest używany w tym dowodzie.
- Zależność 17→18 jest istotna dla identyfikacji homologii Morse'a:
  potrzebne przestawianie wartości krytycznych zachowuje wybrane pole.
  Dowód w 18 używa przepływu i braku połączenia, nie homologii Morse'a.
  Konstrukcja rozkładu i przestawiania uchwytów nie używa wyniku,
  który ma dzięki niej zostać udowodniony.
- Uzupełnienia rozdziału 1 zachowują przyjęte znaczenia mapy,
  struktury różniczkowej i wektora stycznego. Przykład na RP² znajduje
  się obecnie po zdefiniowaniu przestrzeni stycznej. Odwołania w dowodach
  modeli rzutowych prowadzą do niezależnego argumentu metrycznego.

Weryfikacja ta dotyczy sensu odwołań naprzód, a nie tylko istnienia
ich numerów. Szczegółowe konwencje znaków i rachunki są udokumentowane
przy rozdziałach 3–4, 9, 13 i 16–18 w dzienniku.

### Kontrola techniczna końcowego pliku

- 964 etykiety: brak duplikatów. Wszystkie 860 wystąpień odsyłaczy
  `ref`, `eqref`, `pageref` i `autoref` mają istniejący cel.
- Środowiska LaTeX są prawidłowo sparowane w każdym rozdziale.
  W źródle nie ma znaczników TODO/FIXME/TBD ani przypadkowych ogrodzeń Markdown.
- W tekście końcowego PDF nie ma nierozwiązanych odsyłaczy `??`.
  Wszystkie 1028 wewnętrznych linków PDF prowadzi do istniejących stron.
  Sprawdzono także obecność podpisów wszystkich numerowanych rysunków.
- PDF w repozytorium jest identyczny z wynikiem ostatniej kompilacji
  w `build/`. Jej log potwierdza 325 stron, bez błędów, brakujących
  odsyłaczy, żądań ponownego przebiegu oraz `Overfull` i `Underfull`.
  Pozostają dwa ostrzeżenia o automatycznej zmianie położenia rysunku
  z `h` na `ht`. Wbudowany kompilator nie podał potwierdzonego statusu;
  zweryfikowany skład wykonano lokalnym MiKTeX.
- SHA-256 końcowego PDF:
  `12f296ea00243dd915b5ae388288038103f7e60b06c06dbdc1d56f707bbec378`.
- Sprawdzono `git diff --check`. Do obsługi repozytorium używano
  `E:\Programs\Windows\PortableGit\cmd\git.exe`.

Kontrole strukturalne nie zastępują czytania dowodów. Dowody i ilustracje
sprawdzano w poszczególnych iteracjach; końcowa kontrola porównuje ich
zapisane wyniki z aktualnym źródłem i weryfikuje powiązania między nimi.


W tej dawnej wersji pełne h-/s-kobordyzmy, torsja Whiteheada, dalsza
chirurgia i struktury egzotyczne były dopiero propozycjami. Skrypt jawnie
korzystał z twierdzeń Brouwera, o funkcji odwrotnej, triangulacji i pełnego
Cherna–Gaussa–Bonneta. Późniejsza rozbudowa zmienia zakres tekstu, dlatego
nie wolno przenosić tych dawnych deklaracji na obecny stan bez kontroli.

## Rozdział 5 — podstawy algebry po rozbudowie autora (2026-10-05–06)

Zakres: cały nowy rozdział 5 w wersji `aa6c59a`, cztery sekcje i rysunek
grafu słów. Moduły pochodzą częściowo z uprzednio sprawdzonego rozdziału 5;
przeniesienie nie zastępuje kontroli nowych grup, pierścieni i tensorów.

- Uzupełniono brakującą definicję podgrupy i warstwy oraz kryterium równości
  warstw. Sprawdzono aksjomaty ilorazu i krótkie konsekwencje definicji
  homomorfizmu, aby pierwsze użycia nie zakładały niepodanych pojęć.
- W grupie wolnej dopisano, dlaczego stos reprezentuje tę samą klasę słowa;
  dotychczas argument uzasadniał jednoznaczność, pomijając ten krok istnienia.
- W iloczynie wolnym jawnie oznaczono rozłączną sumę alfabetów i odwracalne
  relacje, także dla dwóch kopii tej samej grupy. Odrębność czynników jest
  istotna: identycznie nazwane elementy nie stają się automatycznie równe.
- Naprawiono lukę logiczną: odwracalność dopisywania x nie dowodzi sama
  zgodności z relacją xy. Nowy dowód sprawdza T_y(T_x(u))=T_xy(u), także
  przypadek skasowania końca stosu. Stąd wynik jest stały na klasie,
  postać normalna jednoznaczna, a czynniki osadzają się w iloczynie wolnym.
  Rozpisano też własność uniwersalną używaną w twierdzeniu van Kampena.
- Dodano przykład dwóch grup rzędu dwa: ich iloczyn wolny jest nieskończony
  (różne słowa (ab)^k), podczas gdy iloczyn prosty ma cztery elementy.
- Zastąpiono błędne „zbiliniowa/zbiliniowość” przez „dwuliniowa/dwuliniowość”.
  Doprecyzowano relację modułu spinorów nad nieprzemienną algebrą Clifforda
  do przyjętej w tej części konwencji pierścienia przemiennego.
- Rozpisano izomorfizm tensoru sumy prostej z sumą tensorów i jego odwrotność,
  w tym skończoność nośnika. Uzupełniono rachunek 3R⊕4R=R dla R=Z/6,
  wyjaśniający przykład modułu projektywnego, który nie jest wolny.
- Dla pierścienia nieprzemiennego podano poprawny obiekt wyjściowy:
  wolną grupę abelową na parach oraz relacje addytywności i zbalansowania.
  Sam wybór prawego i lewego modułu nie nadaje tensorowi struktury modułu
  nad tym pierścieniem; zaznaczono tę granicę i odzyskanie wcześniejszej
  konstrukcji w przypadku przemiennym.
- Pozostałe dowody (ilorazy pierścieni i modułów, torsja, własność uniwersalna
  tensoru, (R/I)⊗M, rozszerzenie skalarów i projektywność) sprawdzono,
  zachowując poprawne rachunki. Rysunek przedstawia poprawny fragment grafu
  Cayleya, a nie pełną kulę; podpis już to zaznacza, więc nie zmieniano geometrii.

Dodano dalszą lekturę z dokładnym miejscem: Hatcher, *Algebraic Topology*,
sekcja 1.2, s. 41–42 ([źródło](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf)),
oraz *The Stacks Project*, sekcja 10.12
([tensor nad pierścieniem przemiennym](https://stacks.math.columbia.edu/tag/00CV)).
Pierwsze źródło potwierdza używaną postać normalną i własność uniwersalną;
drugie konstrukcję tensoru. Dowody w skrypcie pozostają rozpisane samodzielnie.

Zinwentaryzowano ponadto różnice `66b220f`→`19fa283` we wcześniej
sprawdzonych rozdziałach. Występują w rozdziałach 2–4 oraz 6–19;
przeniesienie modułów dominuje w rozdziale 6, a w części pozostałych
zmiany ograniczają się do wpisów indeksu. Sama inwentaryzacja nie została
oznaczona jako audyt matematyczny tych rozdziałów.

Kontrole zakończone 6 października 2026:

- Wśród źródeł TeX zmieniono wyłącznie rozdział 5; zachowano cztery
  numerowane sekcje i jeden rysunek, dodano nienumerowaną dalszą lekturę.
  Wszystkie 31 importów istnieje i występuje dokładnie raz; nie ma
  osieroconych źródeł. Środowiska wszystkich części są sparowane.
- Wszystkie 1161 etykiet jest unikalnych; 1053 odsyłacze mają istniejące
  cele. Sprawdzono także wszystkie lokalne linki czterech plików Markdown.
- Pełny `latexmk` wraz z indeksem dał 387 stron i potwierdził aktualność
  wyników. `makeindex` przyjął 152 wpisy bez odrzuceń i ostrzeżeń.
  Nie ma błędów, niezdefiniowanych odsyłaczy, `Overfull` ani żądania
  kolejnego przebiegu. Pozostają wcześniejsze dwa komunikaty `h`→`ht`
  i jedno `Underfull` w rozdziale 23.
- W PDF nie ma `??`; wszystkie 1428 linków wewnętrznych mają cel
  na istniejącej stronie. Kontrola uwzględnia zarówno zwykłe, jak
  i nazwane cele PDF, używane przez hyperref.
- Obejrzano strony 102–110, w tym graf słów, dowód postaci normalnej,
  tensor i dalszą lekturę, oraz obie strony indeksu 386–387.
  Podpisy, wzory i łamanie tekstu są czytelne.
- Zaktualizowano PDF w katalogu głównym; porównano go bajtowo
  z wynikiem kompilacji. `git diff --check` przechodzi.

Kolejna iteracja dotyczy różnic rozdziału 2. Nowe rozdziały 20–27
i dodatek nadal oczekują na nasz audyt; pełny cel pozostaje otwarty.

## Rozdział 2 — kontrola dodatków po rozbudowie (2026-10-06)

Zakres: wszystkie różnice autora `66b220f`→`19fa283` w rozdziale 2
oraz ich powiązanie z nowym modelem brzegu w rozdziale 1.
Przed pracą pobrano aktualizacje; gałąź była aktualna i czysta (`23483ad`).

- Autor zastąpił powtórzoną konwencję półprzestrzeni odsyłaczem, dodał
  dwa wpisy indeksu i rozwinął bibliografię. Pozostałe dowody oraz cztery
  ilustracje zachowują treść wcześniejszego audytu.
- Sprawdzono zgodność nowego odsyłacza z uwagą o dwustronnym przepływie,
  dowodem rozszerzania izotopii przy końcach czasu i konstrukcją kołnierza.
  Styczność do brzegu gwarantuje lokalny przepływ zachowujący rozmaitość;
  skierowanie do wnętrza daje czas jednostronny. Założenie bez brzegu
  w głównych twierdzeniach pozostaje jawne.
- Odsyłacz do przestrzeni stycznej prowadzi teraz bezpośrednio do
  `prop:styczna-brzeg-1`, gdzie znajduje się pełny dowód, zamiast
  do wstępnej wzmianki w sekcji o definicji brzegu.
- Dodano przykład X=∂r na [0,∞): pole jest gładkie, lecz krzywa z zera
  musiałaby być r(t)=t i dla t<0 opuszcza półprostą. Wyjaśnia to różnicę
  między pełnym T₀M a T₀∂M i zapobiega myleniu lokalnej dwustronności
  z globalną zupełnością. Nie zmieniono poprawnego argumentu ODE.
- Zweryfikowano nowe źródła bibliograficzne: stronę wydawcy i
  [spis treści Lee udostępniony przez autora](https://sites.math.washington.edu/~lee/Books/ISM/front-matter.pdf)
  oraz [tekst Milnora](https://people.dm.unipi.it/benedett/MILNOR-TDVPOINT.pdf).
  Rozdziały 8–9 Lee wskazano jako źródło pól, przepływów, zachowania przy
  brzegu i pól zależnych od czasu, a 12 jako rozszerzenie do tensorów.
  Przy Milnorze dopisano strony 20–24 (izotopia i przemieszczanie punktów)
  oraz 32–41 (pola i liczba Eulera). Nie przypisano tym ogólnym odsyłaczom
  dokładnej wersji naszego twierdzenia o rozszerzaniu izotopii.

Kontrola: zmieniono wyłącznie źródło rozdziału 2; jego cztery środowiska
rysunków są identyczne z wersją przed tą iteracją. Wszystkie 31 importów,
1161 unikalnych etykiet i 1054 odsyłacze są poprawne; środowiska sparowane,
a lokalne linki dokumentacji istnieją. Pełny `latexmk` zakończył skład
387 stron bez błędów, brakujących referencji ani żądania ponownego przebiegu.
Pozostały dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23;
nie ma nowych ostrzeżeń ani `Overfull`.

Obejrzano strony 50, 55, 58–59, 61, 63 i 65, obejmujące wszystkie rysunki,
nowy przykład, odsyłacz i bibliografię, oraz indeks na stronach 386–387.
Układ jest czytelny. Wszystkie 1429 linków wewnętrznych PDF mają poprawne
cele; nie ma `??`. Zaktualizowano główny PDF, sprawdzono zgodność bajtową
ze składem i `git diff --check`. Następna iteracja: różnice rozdziału 3.

## Rozdział 3 — kontrola dodatków po rozbudowie (2026-10-06)

Zakres: wszystkie różnice `66b220f`→`19fa283` w algebrze tensorowej.
Pobranie zmian przed przeglądem potwierdziło aktualną, czystą gałąź `2035433`.

- Porównano całe źródło z wcześniejszą sprawdzoną wersją. Po pominięciu
  nowych poleceń indeksu, bibliografii i zmiany nazwy rozdziału w jednym
  odsyłaczu tekst jest identyczny. Nie ma pominiętych nowych dowodów.
- Odsyłacz do twierdzenia o izomorfizmie prawidłowo wskazuje obecny
  rozdział 5, twierdzenie 5.3.5. Przeczytano konstrukcję tensoru oraz uwagę
  o faktoryzacji: dowód używa własnego argumentu R⊆ker L, więc późniejsze
  twierdzenie jest porównaniem, a nie ukrytą przesłanką. Nadal jawnie
  rozróżnione są F/R i F/ker L. Nie znaleziono luki wymagającej dopisania.
- Sprawdzono 11 wpisów indeksu: tensor, własność uniwersalną, kontrakcję,
  algebry tensorową, symetryczną i zewnętrzną, symetryzator/antysymetryzator,
  wyznacznik, pole tensorowe, cofnięcie i pochodną Liego. Umieszczono je
  przy odpowiednich definicjach, a numery stron wynikają ze świeżego składu.
- Zweryfikowano [notatki Conrada](https://math.stanford.edu/~conrad/diffgeomPage/handouts/tensor.pdf):
  tytuł, 13 stron i zakres odpowiadają bibliografii. Zachowano odsyłacz
  do Lee, rozdziały 12 i 14, potwierdzone w
  [spisie treści autora](https://sites.math.washington.edu/~lee/Books/ISM/front-matter.pdf).
- Kod rysunku pola równoległoboku i nienumerowanego diagramu własności
  uniwersalnej jest identyczny z poprzednim audytem. Obejrzano je ponownie
  na stronach 66 i 78, a także poprawiony przez autora odsyłacz na 67
  i bibliografię na 84. Oznaczenia, strzałki i rachunek pola 3·2−1·1=5
  są zgodne z tekstem; ilustracje pozostawiono.
- Kontrola struktury potwierdziła 31 importów, 1161 unikalnych etykiet,
  1054 poprawne odsyłacze i sparowanie środowisk. `latexmk` potwierdził
  aktualność pełnego składu z indeksem (387 stron). Główny PDF jest
  bajtowo identyczny ze sprawdzonym wynikiem kompilacji; nie wymagał
  zmiany. Lokalne linki czterech plików Markdown są poprawne.

Nie zmieniano źródeł TeX ani PDF; ta iteracja zapisuje pozytywny wynik
audytu w dzienniku i planie. Następny jest rozdział 4.

## Rozdział 4 — kontrola dodatków po rozbudowie (2026-10-06)

Zakres: wszystkie różnice autora `66b220f`→`19fa283` w rozdziale
o grassmannianach, algebrze Clifforda i spinorach. Gałąź po pobraniu
aktualizacji pozostała czysta i aktualna (`01cf513`).

- Pełne porównanie źródeł wykazało tylko siedem poleceń indeksu oraz
  zmianę wypełnienia i obrysu dwóch sfer. Po usunięciu tych dokładnie
  wskazanych różnic tekst jest identyczny z wcześniej sprawdzoną wersją.
  Nie ma nowych twierdzeń ani zmienionych dowodów do naprawy.
- Sprawdzono rysunek 4.2 na stronie 88: wybór orientacji płaszczyzny
  odpowiada wyborowi jednostkowej normalnej, a punkty n i −n pozostają
  antypodyczne. Jasnoniebieskie cieniowanie nie zmienia geometrii ani
  nie zasłania punktów, równika czy etykiet.
- Sprawdzono rysunek 4.5 na stronie 98 z opisującym go rachunkiem:
  faza spinora znika po przejściu do prostej zespolonej, a odwzorowanie
  b prowadzi do sfery. Zaznaczony punkt jest czytelny na powierzchni,
  podpis i kolejność strzałek odpowiadają konstrukcji. Rysunek zachowano.
- Obejrzano również pozostałe trzy ilustracje na stronach 86, 92 i 95.
  Ich źródła nie uległy zmianie; diagram wykresu, rozkład iloczynu
  Clifforda i dwukrotne nakrycie Spin(2)→SO(2) zachowują poprawne oznaczenia.
- Siedem wpisów indeksu prowadzi do stron 85, 87, 88, 90, 93, 95 i 98.
  Dwa wystąpienia hasła „Grupa Spin” wskazują początek rozdziału oraz
  właściwą definicję; indeks scala je w jedno hasło z dwiema stronami.
- Potwierdzono strukturę importów, unikalność 1161 etykiet i cele 1054
  odsyłaczy. `latexmk` potwierdził aktualność składu z indeksem, 387 stron.
  Główny PDF jest bajtowo identyczny ze sprawdzonym wynikiem kompilacji.
  Nie zmieniono źródeł matematycznych ani PDF; zapisano wynik w planie
  i dzienniku. `git diff --check` przechodzi.

Następna iteracja: rozdział 6, w szczególności kompletność po przeniesieniu
podstaw modułów i tensoru do osobnego rozdziału 5.

## Rozdział 6 — kompletność po wydzieleniu algebry (2026-10-06)

Zakres: różnice autora `66b220f`→`19fa283` w dawnym rozdziale 5,
obecnie 6. Przed pracą pobrano zmiany; gałąź `d326e06` była aktualna i czysta.

- Sprawdzono przeniesienie sekcji o modułach: wszystkie sześć jej etykiet
  (sekcja, definicje modułu, torsji i homomorfizmów, przykład podstawowy
  oraz twierdzenie o izomorfizmie) zachowano dokładnie raz w rozdziale 5.
  Nie utracono definicji potrzebnych w dowodach homologicznych.
- Porównano całe pozostałe źródło: dziewięć sekcji zachowuje uprzednio
  sprawdzone dowody i przykłady. Różnice poza wstępem dotyczą wpisów
  indeksu i zastąpienia uwagi o tensorze odsyłaczem do rozdziału 5.
- Przy przeniesieniu usunięto z rozdziału 6 jawną konwencję dotyczącą R.
  Przywrócono na początku założenie pierścienia przemiennego z jedynką
  1≠0 oraz R-liniowość odwzorowań, z odsyłaczem do modułów. To potrzebne
  m.in. dla traktowania Hom_R(M,N) jako R-modułu w kompleksie dualnym;
  uwaga o pierścieniach nieprzemiennych na końcu poprzedniego rozdziału
  nie powinna niejawnie zmieniać założeń obecnego.
- Sprawdzono, że usunięty lokalny opis tensoru ma pełny odpowiednik
  w rozdziale 5: konstrukcję, własność uniwersalną, rozszerzenie skalarów,
  tensorowanie odwzorowań oraz zachowanie sum prostych i izomorfizmów.
  Ostatnie dwie własności, uzupełnione podczas audytu rozdziału 5,
  uzasadniają rozkłady w dowodzie zmiany współczynników na Q, R i C.
- Dopisano połączenie dwóch opisów zmiany współczynników:
  C_n⊗Z/m ≅ C_n/mC_n przez c⊗[a]↦ac+mC_n. Odsyłacz prowadzi
  do wcześniej udowodnionego wzoru na tensor ilorazu przez ideał.
  Sprawdzono komutowanie z różniczkami, więc jest to izomorfizm kompleksów.
  Wyjaśniono, że charakterystyka zero jest założeniem późniejszego
  prostszego wzoru na homologię, nie warunkiem istnienia tensoru.
- Przeczytano w powiązaniu dowód redukcji modulo m, przykład nowej klasy
  stopnia 1, konstrukcję kompleksu dualnego i argument zmiany współczynników
  w charakterystyce zero. Ich założenia oraz odsyłacze do przeniesionych
  podstaw są zgodne; nie zmieniano poprawnych rachunków.

Kontrola zakończona: zmieniono wyłącznie źródło rozdziału 6, zachowując
dziewięć sekcji i niezmieniony kod rysunku. Wszystkie 31 importów,
1161 unikalnych etykiet i 1057 odsyłaczy są poprawne; środowiska są
sparowane. Pełny `latexmk` potwierdził aktualny skład 387 stron z indeksem,
bez błędów, brakujących referencji ani żądania kolejnego przebiegu.
Pozostają te same dwa ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23;
nie ma `Overfull`.

Obejrzano strony 111, 114, 116, 122–123 i 125 (wstęp, diagram długiego
ciągu, kompleks dualny, redukcję i tensorowanie współczynników oraz
zakończenie) oraz indeks na stronach 386–387. Układ jest czytelny.
W PDF nie ma `??`, a wszystkie 1432 linki wewnętrzne mają istniejące cele.
Zaktualizowano główny PDF i potwierdzono zgodność bajtową ze składem.
`git diff --check` przechodzi. Następna iteracja: dodatki rozdziału 7.

## Rozdział 7 — połączenie van Kampena z podstawami grup (2026-10-06)

Zakres: wszystkie różnice autora `66b220f`→`19fa283` w dawnym
rozdziale 6, obecnie 7. Pobranie zmian potwierdziło czystą i aktualną
gałąź `83b0896`. Poza dziesięcioma wpisami indeksu jedyna zmiana autora
zastępuje opis iloczynu wolnego odsyłaczem do nowego rozdziału 5.

- Przeczytano cały dowód van Kampena, wybór dróg do punktu bazowego,
  argument siatki dla jądra oraz zastosowania do bukietu okręgów,
  sfer i dołączania komórek. Własność uniwersalna jest potrzebna już
  przy utworzeniu homomorfizmu z iloczynu wolnego; sama definicja
  nie była precyzyjnym wskazaniem przeprowadzonego dowodu tej własności.
- Dodano odsyłacz do `prop:free-product-normal-5` oraz jawne użycie
  własności uniwersalnej w pierwszym zdaniu dowodu. Zdefiniowano symbole
  i_U oraz i_V jako inkluzje przecięcia do składników pokrycia.
  Nie zakłada się iniektywności indukowanych homomorfizmów grup.
- Rozpisano końcowe przejście: relatory leżą w jądrze, więc ich domknięcie
  normalne N także; argument siatki daje inkluzję przeciwną. Odwzorowanie
  gN↦Φ(g) jest dobrze określone, surjektywne i ma trywialne jądro.
  Stąd wynika izomorfizm z tezy bez niejawnego użycia nieudowodnionego
  wcześniej grupowego twierdzenia o izomorfizmie.
- W przykładzie torusa dodano odsyłacz do rachunku prezentacji w rozdziale 5.
  Rozdzielono role obu miejsc: wcześniejszy przykład oblicza grupę z relacji,
  a obecne dołączenie komórki wyjaśnia topologiczne pochodzenie tej relacji.
- Dziesięć wpisów indeksu umieszczono przy właściwych pojęciach. Porównanie
  potwierdziło, że reszta treści autora, w tym kod sześciu rysunków,
  zachowuje wersję wcześniejszego audytu. Poprawki tej iteracji dotyczą
  wyłącznie rozdziału 7.

Kontrola zakończona: 31 importów, 1161 unikalnych etykiet i 1059 odsyłaczy
bez brakujących celów; środowiska i lokalne linki dokumentacji są poprawne.
Pełny `latexmk` złożył 387 stron i indeks (152 wpisy), bez błędów,
niezdefiniowanych referencji, `Overfull` ani żądania kolejnego przebiegu.
Pozostają dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
W PDF nie ma `??`; wszystkie 1434 linki wewnętrzne mają istniejące cele.
Obejrzano strony 126, 127, 129, 132–134, 136–139 oraz indeks 386–387,
w tym w pełnym rozmiarze strony z twierdzeniem i dowodem van Kampena.
Rysunki, tekst dowodu i odsyłacz w przykładzie torusa są czytelne.
Zaktualizowano główny PDF, sprawdzając zgodność ze składem.
Następna iteracja: dodatki rozdziału 8.

## Rozbudowa z 6 października 2026

Na nową prośbę autora plan z `PLAN_DZIALANIA.md` obejmuje w tym samym PDF
przyszłe rozdziały o grupach Liego, teorii Hodge'a--Bochnera oraz wymiarze 4.
Wcześniejszy zapis o osobnym skrypcie dla Freedmana jest historyczny.

- W rozdziałach 2--11 zastąpiono osobne sekcje „Dalsza lektura”
  krótkimi notkami według wzorca rozdziału 18. Zachowano adresy źródeł.
- W rozdziałach 22 i 23 dodano rysunki ruchu Whitneya i pary hiperbolicznej.
  Rozpisano warunki lokalnego ruchu, wpływ przesunięcia uchwytu na formę
  oraz przejście od lagranżjanu do bazy hiperbolicznej nad $\mathbb Z$.
  W rozdziale 19 doprecyzowano, że łuki dysku Whitneya omijają inne
  punkty przecięcia.
- W rozdziale 25 dodano lemat o ściągalności dopełnienia dysku w sferze
  homotopijnej wymiaru 5 i schemat redukcji wielokąta powierzchni.
  Źródło klasyfikacji zmieniono na pełniejszy tekst Putmana, obejmujący
  także powierzchnie nieorientowalne.
- W rozdziale 26 wyprowadzono wzór na $p_1$ wiązek Milnora z dwóch wiązek
  bazowych i rozwinięto wielomian stopnia osiem we wzorze sygnatury.
  Pełna klasyfikacja powierzchni, geometryczny krok Walla, klasyfikacja
  Bardena i twierdzenie Hirzebrucha pozostają jawnie wskazanymi wynikami
  zewnętrznymi.
- Dodatek B zbiera rachunki homologii singularnej i cechy Eulera.
  Dodatku o twierdzeniach Brouwera nie dodano: niezmienniczość obszaru
  nadal jest w skrypcie wynikiem wejściowym, a autor postawił warunek
  posiadania wcześniej wszystkich narzędzi.
- Pełne `latexmk` z Perlem z Git złożyło 391 stron wraz z indeksem
  po połączeniu pięciu nowszych commitów gałęzi zdalnej.
  Końcowy log nie ma niezdefiniowanych odsyłaczy, błędów ani `Overfull`;
  pozostał jeden `Underfull` w rozdziale 23. Obejrzano strony 360 i 364
  z rysunkami, stronę 387 z początkiem dodatku oraz strony 390--391
  indeksu. Zaktualizowano PDF w katalogu głównym.

## Korekta po uwagach autora z 6 października 2026

Poprzednie uznanie całej klasyfikacji powierzchni za wynik zewnętrzny
było zbyt zachowawcze. Krótki dowód Putmana obejmuje tylko przypadek
orientowalny, ale argument przez drzewo rozpinające, graf dualny i cięcie
krzywych daje również przypadek nieorientowalny w niewielkiej objętości.
W rozdziale 25 zastąpiono odsyłacz dowodem: pokazano kryterium
`χ=2`, istnienie krzywej nierozdzielającej, indukcję po charakterystyce
oraz lokalną relację `T²#RP² ≅ #³RP²`, sprawdzoną czterema jawnymi
przekształceniami słowa brzegowego. Jedynym jawnym twierdzeniem
wejściowym o powierzchniach pozostała triangulowalność topologiczna;
skorygowano jej opis w dodatku A i aktualny stan w planie.

W rozdziale 22 dodano przestrzenny przykład chirurgii: od dwóch dysków
na `∂B³`, przez wybór zawęźlonego rdzenia uchwytu, do torusa będącego
brzegiem otoczenia węzła trójlistnego. Rysunek pokazuje etapy, a tekst
oddziela typ abstrakcyjnej powierzchni od jej osadzenia. Dopisano także
powód, dla którego rogata sfera Alexandra wymaga nieskończonej
konstrukcji dzikiego osadzenia i nie jest wynikiem skończonej gładkiej
chirurgii.

W rozdziale 23 wyszczególniono cztery brakujące składniki pełnego
dowodu twierdzenia Walla: chirurgie poniżej środka z normalnym
obramowaniem, geometryczną realizację lagranżjanu nad `Z[π]`,
niezmienniczość wraz z torsją oraz formacje wymiaru nieparzystego.
Nie oznaczono lokalnego rachunku form jako dowodu ogólnego twierdzenia.
Pełny skład `latexmk` utworzył PDF liczący 393 strony. Końcowy log nie ma
niezdefiniowanych odsyłaczy, błędów ani `Overfull`; pozostał jeden
`Underfull` w rozdziale 23. Obejrzano rysunek na stronie 355 oraz dowód
na stronach 375--376. Indeks powstał bez odrzuconych wpisów.

## Rozwinięcie dowodu Walla — 6 października 2026

Na prośbę autora rozbudowano rozdział 23, zachowując jego etykiety.
Nowe stwierdzenie wyprowadza współczynniki przecięć z etykietami
nakrycia uniwersalnego, relację hermitowską i wzory dla
samoprzecięć. Przykład `1−t` pokazuje, dlaczego zerowa zwykła
liczba przecięć nie wystarcza do znalezienia dysku Whitneya.

Dotychczasowy lemat o lagranżjanie nad `Z` zastąpiono rachunkiem
nad `Z[π]`: podano jawne poprawki dualnych wektorów, które zerują
ich parowania i wartości `μ`, oraz warunek prostoty potrzebny dla
`L^s`. Osobno udowodniono, że suma formy z formą przeciwną jest
hiperboliczna. Lemat o pojedynczej chirurgii poniżej środka
rozpisuje ogólne położenie, stabilną normalną ramę i usunięcie
stabilizacji w zakresie `2r<n`. Dwa ciągi dokładne śladu pokazują,
dlaczego chirurgia na prymitywnym wektorze hiperbolicznym usuwa
parę bez wytworzenia niższego jądra.

W przypadku nieparzystym dodano dwa lagranżjany formacji,
elementarny ciąg dokładny, jego związek z dwoma sąsiednimi
jądrami i przykład z cokernelowym `Z/2`. Poprawiono wcześniejsze
nieścisłe zdanie utożsamiające same jądra z formacją.
Źródłami audytu były Wall, *Surgery on Compact Manifolds*,
§§1, 5--6, oraz Ranicki, *An Introduction to Algebraic Surgery*,
§9. Jawne wejścia pozostają w twierdzeniach 1.2, 5.2,
1.4, lemacie 5.7 i w realizacji relacji formacji z §6 Walla.
Dodatek A i plan uaktualniono do tego zakresu.

Po korekcie lewoliniowości odwzorowania przecięcia oraz zapisaniu
hipotez lematu 5.7 pełny skład `latexmk` dał PDF liczący 396 stron.
Log nie wykazuje błędów, niezdefiniowanych odsyłaczy ani `Overfull`;
indeks został utworzony. Obejrzano strony 370--372 z nowym dowodem.

## Scalenie równoległej rozbudowy autora (2026-10-06)

Podczas wysyłania iteracji rozdziału 7 (`b9e863a`) wykryto cztery nowe
commity: `59fd235`, `9d5e5ff`, `dab4c59` i `46fd90c`. Pobrano je
i scalono, zachowując oba ciągi historii. Konflikty dotyczyły planu,
dopisanych wpisów dziennika oraz binarnego PDF. Zachowano oba wpisy
dziennika, uaktualniono status van Kampena i odbudowano PDF z połączonych
źródeł; nie wybrano jednostronnie żadnego z gotowych PDF.

Nowe treści autora w rozdziałach 19, 22, 23, 25, 26 oraz dodatkach
pozostają w kolejce niezależnego audytu. Dodano do niej nowy dodatek B.
Plany dalszej rozbudowy zachowano jako plany autora; znaczniki wykonania
oznaczają obecność materiału, nie pozytywny wynik naszego audytu.
Bieżące iteracje nadal obejmują po jednym rozdziale matematycznym.

Porównanie całych źródeł rozdziałów 2–7 z `b9e863a` potwierdziło,
że nowa rozbudowa zmienia w nich tylko format bibliografii. Zachowano
wszystkie jej słowa, tytuły, zakresy lektur i adresy oraz cały wcześniejszy
tekst matematyczny. Obejrzano nowe zakończenia na stronach 65, 84, 101,
110, 125 i 139, a także dowód van Kampena i przykład torusa (132–133, 138).
Nie wykryto utraty poprawek ani problemów czytelności.

Kontrola integracji: 32 importy, 1187 unikalnych etykiet, 1112 poprawnych
odsyłaczy w źródle, sparowane środowiska i poprawne lokalne linki Markdown.
Względem `46fd90c` jedyną zmienioną treścią TeX jest rozdział 7;
cała pozostała treść autora została zachowana. `latexmk` potwierdza
aktualny skład i kod zakończenia 0: 397 stron, 155 wpisów indeksu,
bez błędów, niezdefiniowanych referencji, `Overfull` ani zaległego przebiegu.
Pozostają dwa ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
Wszystkie 1484 linki wewnętrzne PDF mają cele; brak `??`.
Obejrzano też spis treści i indeks (strony 1–4, 396–397).
Główny PDF zastąpiono sprawdzonym składem i porównano sumy SHA-256.

## Rozdział 8 — indeks i zachowanie treści homologicznej (2026-10-06)

Zakres: wszystkie dodatki autora do `46fd90c` w dawnym rozdziale 7,
obecnie 8. Iterację rozpoczęto na czystym `046a813`, po pobraniu
i scaleniu najnowszych czterech commitów autora.

- Porównano całe źródło z uprzednio sprawdzonym `66b220f`. Po usunięciu
  dokładnie pięciu nowych poleceń indeksu tekst matematyczny jest identyczny.
  Ostatnia zmiana w `59fd235` dotyczy wyłącznie formatu „Dalszej lektury”.
- Zweryfikowano miejsca wpisów: kompleks łańcuchów symplicjalnych,
  homologia singularna, grupy względne i zredukowane, kompleks komórkowy
  oraz stopień odwzorowania sfer. Wszystkie prowadzą do właściwych definicji.
  Przeczytano te definicje z sąsiednimi uzasadnieniami, w tym augmentację
  dla zbioru pustego, zakres skończonych CW, przypadek stopnia zero
  w porównaniu homologii i orientacje we wzorze na brzeg komórkowy.
- Kod wszystkich trzech ilustracji jest niezmieniony. Obejrzano ich skład:
  zorientowany trójkąt (141), singularny sympleks (142) i kompleks torusa
  (151). Kierunki brzegów, oznaczenia obrazu sympleksu i zerowe operatory
  brzegu torusa zgadzają się z tekstem; etykiety są czytelne.
- Bibliografia nadal wskazuje rozdział 2 książki Hatchera. Nowy dodatek B
  stanowi osobny zakres audytu; jego obecność nie zmienia ani nie zastępuje
  definicji rozdziału 8. Nie dodawano ich drugi raz.

Kontrola: 32 importy, 1187 unikalnych etykiet, 1112 rozwiązanych odsyłaczy,
sparowane środowiska i działające lokalne linki dokumentacji. Skład z tej
samej wersji źródeł jest aktualny: 397 stron, 155 wpisów indeksu i 1484
poprawne linki wewnętrzne, bez `??`. Obejrzano strony 140–143, 150–151,
153 oraz indeks 396–397; odsyłacze indeksu wskazują strony definicji.
Zmiany tej iteracji obejmują tylko plan i dziennik; nie ma potrzeby zmieniać
poprawnej treści TeX ani ponownie generować identycznego PDF.
Następna iteracja: dodatki rozdziału 9.

## Rozdział 9 — wpisy indeksu i terminologia odwzorowań (2026-10-06)

Zakres: wszystkie dodatki autora do `46fd90c` w dawnym rozdziale 8,
obecnie 9. Przed pracą pobrano zmiany: `9a783e7` był aktualny i czysty.

- Porównanie całego źródła z `66b220f` przed naszą edycją potwierdziło
  identyczność tekstu matematycznego po pominięciu pięciu nowych poleceń
  indeksu; późniejsza zmiana dotyczy wyłącznie formatu bibliografii.
- Sprawdzono miejsca indeksowania grup homotopii, grup względnych,
  spójności homotopijnej, słabej równoważności i odwzorowania Hurewicza.
  Przeczytano definicje z otoczeniem: rozróżnienie grup i zbiorów
  z wyróżnionym elementem w niskich stopniach, warunek wszystkich punktów
  bazowych, zakres CW i zgodność orientacji w wersji względnej Hurewicza.
- Poprawiono 19 wcześniejszych użyć słowa „mapa” oznaczającego ogólne
  odwzorowanie: m.in. odwzorowania par, charakterystyczne, ilorazowe,
  dołączające i ściskające równik. Dostosowano rodzaj i odmianę przymiotników.
  Zgodnie z konwencją projektu „mapa” pozostaje nazwą lokalnego układu
  współrzędnych; w tych miejscach nie chodziło o takie mapy.
  Zachowano etykietę `def:mapa-hurewicza`, aby nie naruszyć odsyłaczy.
- Cztery ilustracje zachowują swój kod. Sprawdzono dwa kierunki sklejania,
  warunek obrazu brzegu dysku w A, cylinder odwzorowania oraz nakrycie
  bukietu S¹∨S². W ostatnim przykładzie każda podniesiona sfera daje osobny
  generator, a odwzorowanie Hurewicza sumuje współczynniki; rysunek i tekst
  przedstawiają tę samą konstrukcję. Nie wymagały zmiany.

Kontrola: zmieniono wyłącznie źródło rozdziału 9. Wszystkie 32 importy,
1187 unikalnych etykiet i 1112 odsyłaczy są poprawne; środowiska sparowane.
Pełny `latexmk` zakończył się kodem 0: 397 stron, indeks ze 155 wpisami,
bez błędów, niezdefiniowanych referencji, `Overfull` ani zaległego przebiegu.
Pozostają dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
Obejrzano wszystkie strony rozdziału 154–168 i indeks 396–397;
złożenie terminów i etykiet ilustracji jest czytelne. PDF nie zawiera `??`,
a wszystkie 1484 linki wewnętrzne mają istniejące cele.
Zaktualizowano główny PDF i porównano sumy SHA-256 ze składem.
Następna iteracja: dodatki rozdziału 10.

## Rozdział 10 — indeks, ilustracje i zgodność przy brzegu (2026-10-06)

Po pobraniu zmian potwierdzono aktualność i czystość `1481067`.
Porównano cały rozdział z `66b220f`: treść matematyczna i bibliograficzna
jest identyczna po pominięciu siedmiu poleceń indeksu i zmiany formatu
„Dalszej lektury”. Kod wszystkich pięciu ilustracji jest niezmieniony.

Sprawdzono wpisy indeksu przy formach, kontrakcji i pochodnej Liego,
orientacji, orientacji brzegu, całkowaniu oraz kohomologii de Rhama.
Przeczytano definicje i związane uzasadnienia. Konwencje są zgodne
z uzupełnionym rozdziałem 1: gładkość przy brzegu przez lokalne
przedłużenie, pełna przestrzeń styczna i reguła normalnej na zewnątrz.
Uwzględniono także orientację punktów oraz warunek styczności pola do
brzegu przy definicji pochodnej Liego przez dwustronny przepływ.
Wzór Cartana dla pozostałych pól jest osobno opisany przez przedłużenie.

Obejrzano strony 169–171, 173–177, 180, 182, 186, 189 i indeks 396–397.
Rysunki poprawnie pokazują znak formy dwuliniowej, kierunek brzegu dysku,
kasowanie wspólnej krawędzi, okres na przebitej płaszczyźnie i kompleks,
który nie jest rozmaitością. Etykiety są czytelne, a indeks wskazuje
właściwe strony. Zachowano poprawną treść bez dopisywania duplikatów.

Kontrola struktury: 32 importy, 1187 unikalnych etykiet, 1112 poprawnych
odsyłaczy, sparowane środowiska i działające lokalne linki Markdown.
Aktualny sprawdzony PDF ma 397 stron; źródła i PDF tej iteracji pozostają
niezmienione. Zmieniono jedynie plan i dziennik. Następny rozdział: 11.

## Rozdział 11 — metryka i miara, usunięcie powtórzenia indeksu (2026-10-06)

Zakres: dodatki autora do `46fd90c`, na bazie czystego `d39617b`.
Porównanie z `66b220f` potwierdziło niezmieniony tekst matematyczny,
bibliografię i obie ilustracje. Autor dodał dziewięć poleceń indeksu
oraz zmienił format zakończenia. Wpis „Metryka riemannowska” występował
dwukrotnie na tej samej stronie: przy tytule i przy definicji.
Usunięto pierwsze polecenie, pozostawiając odsyłacz przy definicji.

Sprawdzono położenie wszystkich pozostałych wpisów i przeczytano
definicje z uzasadnieniami: dodatniość cofniętej metryki wymaga immersji,
przeniesienie wymaga dyfeomorfizmu, długość riemannowska nie dotyczy
ogólnej metryki lorentzowskiej, a odległość między składowymi może być
nieskończona. Opis gęstości nie wymaga orientacji; miara Hausdorffa ma
jawną normalizację i konwencję dla stopnia zero. Definicja dywergencji
poprawnie skleja się także na rozmaitości nieorientowalnej.

Obejrzano strony 190–191, 194–196, 198–200, 202, 205 i 207. Ilustracje
trzech modeli hiperbolicznych i parametryzowanej powierzchni są czytelne
oraz zgodne z opisem długości wektorów i wyznacznika Grama.
Ponowny skład potwierdził identyczność tekstu wszystkich 397 stron
i zakładek, a także obrazu wszystkich stron rozdziału 11 i indeksu.
Usunięcie podwójnego polecenia nie zmienia drukowanego indeksu, ponieważ
program indeksujący już scalał oba wystąpienia na tej samej stronie.

`latexmk` zakończył się kodem 0: 154 wpisy indeksu przyjęte bez odrzuceń,
brak błędów, niezdefiniowanych referencji i `Overfull`. Pozostają dwa
ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23. Kontrola obejmuje
32 importy, 1187 unikalnych etykiet, 1112 odsyłaczy oraz 1484 działające
linki PDF; brak `??`. Główny PDF zaktualizowano i porównano ze składem.
Następna iteracja: rozdział 12.

## Rozdział 12 — indeks koneksji i transportu (2026-10-06)

Pobranie zmian potwierdziło aktualność czystego `4793c2e`. Całe źródło
porównano z `66b220f`: poza czterema wpisami indeksu treść matematyczna,
bibliografia i oba rysunki są niezmienione. Wpisy wskazują wprowadzenie
do koneksji, jej definicję afiniczną, torsję i zgodność metryczną oraz
pochodną pola wzdłuż krzywej.

Przeczytano indeksowane definicje i powiązane argumenty: lokalność koneksji,
tensorowość torsji, transformację pochodnej wzdłuż krzywej i istnienie
transportu. W szczególności definicja nie zakłada przedłużalności każdego
pola wzdłuż krzywej do pola na rozmaitości; obejmuje postoje i samoprzecięcia.
Istnienie na całym zwartym odcinku jest uzasadnione oszacowaniem liniowego
równania, nie samym lokalnym twierdzeniem ODE.

Obejrzano strony 208–209, 213, 215, 218 i indeks 396–397. Schemat transportu
nie sugeruje metryki na podstawie samego rysunku. Przykład sfery przy
θ=π/3 pokazuje przeciwne wektory po pełnym obiegu, zgodnie z obrotem −π;
oznaczenia i strzałki są czytelne. Wszystkie wpisy indeksu mają właściwe strony.
Kontrola struktury: 32 importy, 1187 etykiet bez powtórzeń, 1112 poprawnych
odsyłaczy, sparowane środowiska i działające lokalne linki dokumentacji.
Źródła i aktualny PDF 397 stron pozostawiono bez zmian; zapisano wynik
w planie i dzienniku. Następna iteracja: rozdział 13.

## Rozdział 13 — geodezyjne, zupełność i indeks (2026-10-06)

Na czystym `5bbd500` porównano cały rozdział z `66b220f`. Jedyne dodatki
to cztery polecenia indeksu; treść, bibliografia i dziewięć ilustracji
są niezmienione. Usunięto podwójny wpis „Geodezyjna” przy tytule:
pozostaje wpis przy definicji na tej samej stronie.

Przeczytano indeksowane definicje geodezyjnej, odwzorowania wykładniczego
i dwóch rodzajów zupełności oraz ich powiązania z konwencjami książki.
Parametr geodezyjnej jest afiniczny; dziedzina exp jest jawnie określona,
a jej otwartość i gwiaździstość uzasadnione. Współrzędne normalne wynikają
z różniczki exp równej identyczności i twierdzenia o funkcji odwrotnej.
Założenie braku brzegu obowiązuje jawnie w całym rozdziale; przykłady
lorentzowskie nie są objęte wnioskami Hopfa–Rinowa.

Obejrzano strony 219, 221–224, 226–227, 229, 231–233 i indeks 396–397.
Wszystkie dziewięć ilustracji jest zgodnych z opisem: lokalne exp,
odcinek euklidesowy, antypody na sferze, modele hiperboliczne, niezupełna
przebita płaszczyzna oraz schematy Schwarzschilda i Kerra. Podpisy ostatnich
rysunków odróżniają rzuty współrzędnych od osadzenia czasoprzestrzeni
i minimalność riemannowską od maksymalności czasu własnego.

Pełny skład zakończył się kodem 0: 397 stron, 153 przyjęte wpisy indeksu,
bez błędów, niezdefiniowanych referencji i `Overfull`. Pozostają dwa
ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23. Tekst wszystkich stron
i zakładki są identyczne z poprzednim PDF; obraz stron rozdziału 13
i indeksu także jest identyczny. Kontrola 32 importów, 1187 etykiet,
1112 odsyłaczy i 1484 linków PDF przeszła; brak `??`.
Główny PDF zaktualizowano i sprawdzono zgodność ze składem.
Następna iteracja: rozdział 14.
