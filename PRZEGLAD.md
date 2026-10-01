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

## Następna iteracja

Rozdział 4: „Grassmanniany, algebra Clifforda i spinory”.
Rozdziały 4–18 nie zostały jeszcze objęte przeglądem.
