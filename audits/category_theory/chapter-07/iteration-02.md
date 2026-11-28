# CAT-07 — audyt II (stabilizacyjny)

Stan badany: 9945b0989ccd8ddf5b9d2644bae534abc300cece.
Źródło: 688fc2af259de918dde0bf2861c8a9ca8b09bb79.
Testy: bc8c8710929b8686fc2f172cb05693fa79a7ff3b.

## Kontrola semantyczna
- Equalizator: zgodność f e=g e oraz jednoznaczność rozkładu implikują moniczność. W Set podzbiór zgodności realizuje własność uniwersalną także przy pustej dziedzinie. Jądro w Vect otrzymujemy dla pary f,0. Przykład 2Z jest poprawny, gdyż 3n=0 modulo 6 dokładnie dla parzystego n.
- Koequalizator: przecięcie relacji równoważności zawierających zadane pary istnieje; relacja równości obrazów przez v jest jedną z nich. Faktoryzacja jest dobrze określona i jednoznaczna przez surjektywność rzutu. Epiczność w dowolnej kategorii wynika z jednoznaczności faktoryzacji, nie z argumentu na elementach. W Grp normalne domknięcie elementów f(a)g(a)^(-1) jest zawarte w jądrze każdej zgodnej mapy, co uzasadnia iloraz. W Vect kojądro jest ilorazem przez obraz.
- Pullback: warunek zgodności jest właściwie typowany. W Set parowanie daje jedyny morfizm; przy ograniczeniu do podprzestrzeni obie mapy porównawcze są ciągłe. W przykładzie liniowym parametry x,t są niezależne i wyznaczają y=2t-x. Przeciwobraz zbioru {0,1,4} pod n↦n² obliczono poprawnie.
- Pushout: rozróżniono zanurzenia do sumy rozłącznej i morfizmy do ilorazu. Zgodność pary u,v umożliwia faktoryzację przez relację generowaną. W Ab jądro mapy (a,b)↦3a+2b jest generowane przez (2,-3), a obraz zawiera 1. W Top sklejenie dwóch przedziałów daje ciągłą bijekcję zwartego ilorazu na przestrzeń Hausdorffa, zatem homeomorfizm.
- Konstrukcja pullbacku przez iloczyn i equalizator: złożenia z rzutami wymuszają parowanie, następnie własność equalizatora wymusza jedyną faktoryzację; dualność daje analogiczną konstrukcję pushoutu. W modułach różnica map jest homomorfizmem również dla lewych modułów nad nieprzemiennym pierścieniem. Iloraz przez im(f,-g) wymusza relację zgodności. W Top topologia podprzestrzeni oraz ilorazowa zapewniają odpowiednio ciągłość faktoryzacji do podprzestrzeni i z ilorazu. Nie założono własności Hausdorffa dla wszystkich ilorazów.
- Lemat o sklejaniu: przy prawym kwadracie kartezjańskim zgodna para do X,R najpierw wyznacza jedyny morfizm do Q, a następnie do P. W implikacji odwrotnej morfizm z własności zewnętrznego prostokąta spełnia oba równania do Q, przez jednoznaczność w prawym kwadracie. Wniosek dualny dla pushoutu ma poprawny kierunek (lewy kwadrat jako założenie).
- Stabilność mono i epi: równość jednej składowej oraz skracanie przez g dają równość drugiej składowej; własność uniwersalna daje równość morfizmów. Przy g odwracalnym para id_A,g^(-1)f daje przekrój p_A, a moniczność p_A zapewnia odwrotność obustronną.
- Rozmaitości: przy transwersalności stosuje się twierdzenie z DG-15 o podrozmaitości iloczynu i wzorze wymiaru dla niepustego włókna. Gładkość faktoryzacji do podrozmaitości wynika z lokalnych map dostosowanych. Dla f=g:t↦t² założony pullback i test singletonem dają jedyny punkt o nad (0,0). Obie zgodne pary krzywych dają gładkie podniesienia przez o. Ich wektory styczne przechodzą na (1,1) i (1,-1), więc różniczka F=(p,q) jest surjektywna. Twierdzenie o submersji wymusza otoczenie (0,0) w obrazie F, sprzeczne z zawieraniem się obrazu w sumie dwóch prostych. Nie wyprowadzono nieistnienia obiektu jedynie z braku struktury podrozmaitości na zbiorze zgodności. Argument dotyczy zwykłych rozmaitości bez brzegu.
- Nie wykryto nowych istotnych usterek. Nie zmieniono tekstu ani zakresu.

## CI
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45588820491, commit a408e8f0a14df0abf4b35260a97c37a03bbba1ea. Job validate completed/success; osiem kroków zakończonych success, w tym discovery testów, kompilacja całego tomu, kontrola odsyłaczy i PDF oraz upload artefaktu. Zestawy zawierają 4+5+5+6+6+5+7+7=45 metod testowych. Porównanie 29 blobów (19 rozdziałów, książka, 8 zestawów testów, workflow) bez różnic. Odczytano kod siedmiu metod CAT-07; testy dotyczą modeli skończonych, a kontrola równania przecięcia nie jest formalizacją argumentu różniczkowego. Nie odczytano pełnych logów i nie sprawdzono wizualnie PDF. Nie uruchomiono Lean.

## Decyzja
Audyt II zaliczony bez zmian. CAT-07 pozostaje do niezależnego audytu III z rzeczywiście wykonanymi kontrolami i oględzinami PDF, przed CAT-08.
