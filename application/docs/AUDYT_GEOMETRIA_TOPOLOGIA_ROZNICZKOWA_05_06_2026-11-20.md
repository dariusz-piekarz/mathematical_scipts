# Audyt DG-05–06 — Geometria i topologia różniczkowa
Data: 2026-11-20  
Gałąź: \`biblioteka-matematyczna-iteracja-6\` (bez zmian w \`main\`)  
Repozytorium: \`dariusz-piekarz/mathematical_scipts\`

## Zakres

W tej iteracji objęto kontrolą dwie kolejne jednostki kanonicznego tomu:
- \`chapters/pl/differential_geometry_and_topology/05-podstawy-algebry-abstrakcyjnej.tex\`;
- \`chapters/pl/differential_geometry_and_topology/06-algebra-homologiczna-kompleksy-i-kohomologie.tex\`.

Sprawdzano sformułowania pojęć i założenia, ważniejsze dowody, przykłady rachunkowe, użycie torsji, poprawność przejść do ilorazów, homotopie łańcuchowe, naturalność długich ciągów, cofnięcie/zmianę współczynników, etykiety, odsyłacze, ilustracje i zewnętrzne zależności. Porównano zakres z równoległymi rozdziałami topologii algebraicznej. Przyjętym punktem odniesienia jest poziom szczegółowości dowodów i przykładów z rozdziału 01 skryptu geometrii różniczkowej. Starsze etykiety i wszystkie poprzednie dowody zachowano.

## Rozdział 05 — algebra abstrakcyjna

Przegląd objął: normalność i ilorazy grup, algorytm redukcji słów w grupach wolnych i iloczynach wolnych, prezentacje, iloczyny proste i półproste, ideały i pierścienie ilorazowe, moduły i własność uniwersalną ilorazu, iloczyn tensorowy modułów i jego prawostronną dokładność, rozszerzenie skalarów, rzutowość, ciało ułamków i lokalizację oraz addytywność rangi.

**Uzupełnienie matematyczne:** Rozdział używał pojęcia „usuwania torsji” w opisie rangi nad dziedziną całkowitości, lecz torsję zdefiniowano wcześniej tylko dla grup abelowych. Dodano definicję \`def:torsja-r-modulu-5\`:
\[
 \operatorname{Tors}_R(M)=\{m\in M:\exists\,0\ne r\in R,\ rm=0\},
\]
wraz z dowodem zamknięcia na odejmowanie i mnożenie przez skalary, wykorzystującym \`rs\ne0\` w dziedzinie całkowitości. Dodano dwa obliczone przykłady:
- \`prz:torsja-z-dzielnikami-zera-5\`: w \`R=Z/6Z\` elementy \`[2]\` i \`[3]\` są zabijane przez niezerowe skalary, ale \`[2]+[3]=[5]\` jest jednostką; poza dziedzinami analogicznie opisany zbiór nie musi być podmodułem;
- \`prz:torsja-wielomiany-5\`: \`R=K[t]\`, \`M=R/(t)\`; moduł jest torsyjny nad \`R\`, ale jednowymiarowy i bez torsji jako przestrzeń liniowa nad \`K\`.

**Naprawa odsyłacza:** \`app:grupy-algebry-macierzowe\` nie występuje w żadnym z 20 aktualnie dołączonych rozdziałów tomu. W rozdziale 05 usunięto odesłanie do nieistniejącego dodatku i wskazano istniejący rozdział 04 \`ch:grass-spin\`. Odsyłacze do \`thm:van-kampen\` są prawidłowe: cel istnieje w rozdziale 07.

**Redakcja:** Usunięto nieobjaśniony skrót \`Z_*\` na rzecz jawnego \`Z\setminus\{0\}\`.

## Rozdział 06 — algebra homologiczna

Przejrzano: krótkie i długie ciągi dokładne kompleksów, jawny opis łączącej strzałki \`\delta\`, naturalność, kohomologię kompleksu dualnego, homotopię łańcuchową, kasowanie par generatorów przy odwracalnym współczynniku, kompleksy względne, filtracje i homologiczną wersję ciągu Mayera–Vietorisa, zmianę współczynników modulo \`m\`, przejście do ciał charakterystyki 0, charakterystykę Eulera i lemat pięciu.

**Uzupełnienie matematyczne:** Przy twierdzeniu \`thm:mod-m-homologia\` dodano przykład \`prz:mod2-dwa-zrodla\` z kompleksem
\[
 0\to\mathbf Z\,t\xrightarrow{(2,0)^T}
 \mathbf Z\,e\oplus\mathbf Z\,f
 \xrightarrow{(0,2)}\mathbf Z\,v\to0.
\]
Przed redukcją otrzymuje się \`H_1(C)=Z/2Z\` i \`H_0(C)=Z/2Z\`; po redukcji modulo 2 obie różniczki są zerowe, a \`H_1(C/2C)=(Z/2Z)^2\`. Jawnie obliczono obie strzałki
\[
 0\to H_1(C)/2H_1(C)\xrightarrow{\iota}H_1(C/2C)
 \xrightarrow{\delta}H_0(C)[2]\to0
\]
w wybranych bazach: \`\iota([e])=[\bar e]\` i \`\delta([\bar a\bar e+\bar b\bar f])=[bv]\`. Pokazano, że \`\ker\delta=\operatorname{im}\iota\`; pierwsza klasa pochodzi ze starej homologii, druga z torsji w niższym stopniu. Nie utożsamiano istnienia rozszczepienia w przykładzie z kanonicznym rozszczepieniem ogólnego twierdzenia.

**Redakcja:** Usunięto nieobjaśniony skrót \`Z_*\`.

## Relacja z topologią algebraiczną: bez scalania

Porównano równoległe pliki:
- \`chapters/pl/algebraic_topology/02-podstawy-algebry-abstrakcyjnej-grupy-pierscienie-i-moduly.tex\` (ok. 26 tys. znaków);
- \`chapters/pl/algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex\` (ok. 61 tys. znaków).

Istnieje silne pokrycie definicji ilorazów, modułów, iloczynu tensorowego i długich ciągów. Nie są jednak wymienne plik za plik: DG-05 rozwija między innymi iloczyny półproste, konstrukcję ciała ułamków i rangę, zaś AT-02 zawiera osobne wprowadzenie \`Tor_1\` oraz \`Ext^1\` z dowodem niezależności od wolnej prezentacji. Przy planowanym przyszłym scalaniu trzeba zachować sumę unikalnych treści, wszystkie istotne warianty dowodów, przykłady i rysunki. Obecnie nie zmieniano modułów topologii algebraicznej ani historycznych etykiet. Etykiety podobne lub identyczne w dwóch oddzielnych tomach wymagają przed połączeniem osobnej mapy przestrzeni nazw.

## Kontrole strukturalne i testy

Po zapisaniu zmian ponownie pobrano siedem pierwszych rozdziałów tomu i sprawdzono:
- \`453\` różne etykiety w DG-01–07, bez powtórzeń;
- \`0\` nierozwiązanych \`ref/eqref/nameref/autoref/pageref\` w DG-05 i DG-06 względem etykiet DG-01–07;
- DG-05: \`53\` etykiety, \`29\` użyć odsyłaczy, \`4\` rysunki \`figure\`;
- DG-06: \`72\` etykiety, \`60\` użyć odsyłaczy, \`4\` rysunki \`figure\`;
- zbilansowane środowiska LaTeX (pary \`\begin\`/\`\end\`) w audytowanych plikach;
- brak zewnętrznych \`input/include/includegraphics/lstinputlisting/inputminted\` w obu rozdziałach;
- nie znaleziono zakazanych form terminologicznych \`tensorowanie\`, \`sekwencyjny\`, \`seskwiliniowy\`, \`zbieżność zdominowana\` w DG-05–06.

Dodano \`application/tests/test_differential_geometry_ch05_06.py\` z regresją etykiet, odsyłaczy, bilansu otoczeń i samowystarczalnych ilustracji oraz obliczeń nad \`Z/6Z\` i dla łączącego homomorfizmu modulo 2. Niezależna kontrola arytmetyczna obu nowych przykładów została wykonana i zwróciła oczekiwane wyniki.

**Granice kontroli:** Nie wykonano pełnego uruchomienia nowego zestawu testów w środowisku repozytorium, kompilacji LaTeX ani wizualnej kontroli wygenerowanych stron PDF. Powód: dostęp do repozytorium w tej sesji odbywa się przez złącze GitHub, a środowisko kompilacyjne nie ma dostępu sieciowego do jego zawartości. Bilans otoczeń i obecność TikZ to kontrole statyczne, nie potwierdzenie poprawnego renderingu.

## Kolejna para

DG-07–08: homotopia, nakrycia, modele komórkowe i homologia przestrzeni. Szczególna uwaga: warunki poprawności twierdzenia van Kampena, konstrukcja i niezależność modeli łańcuchowych, rozbudowane przykłady przestrzeni i zgodność z już istniejącą topologią algebraiczną.
