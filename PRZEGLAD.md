# Przegląd matematyczny skryptu

Gałąź: `review/rozdzialy-matematyka`. Jedna iteracja obejmuje jeden rozdział.
Źródło: `geometria_i_topologia_rozniczkowa.tex`; wynik: plik PDF o tej samej nazwie.
Rejestr zawiera także uzasadnienia, aby można było niezależnie sprawdzić poprawki.
Nowe tematy wykraczające poza naprawę obecnego materiału będą proponowane
po przeglądzie całości, do decyzji autora.

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
