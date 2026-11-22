# Topologia ogólna — globalny audyt 18: wszystkie siedem dowodów rozdziału 16

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/general_topology/16-funkcje-ciagle-i-uzwarcenia.tex.
**Badany blob:** 1c2fcb925d62120feaea468400e48842a508a062.
**Głowica gałęzi zaobserwowana podczas kontroli:** 8cd2bb3ed85af64e616071d6b81128f75ce7ffba (gałąź jest modyfikowana współbieżnie).
**Zakres:** niezależne sprawdzenie wszystkich **7/7** środowisk proof na aktualnym blobie oraz przykładów, założeń, zależności i bieżących dowodów technicznych. Nie jest to jedynie powtórzenie konkluzji audytu 10 (który badał wybrane twierdzenia). Nie zmieniono rozdziału.

## 1. Kontrola poszczególnych siedmiu dowodów

1. **Definicja topologii początkowej — def:topog-uzwarcenia-topologia-poczatkowa.**
   Zbiory f_i^(-1)(V) generują topologię przez skończone przecięcia i dowolne sumy. Wszystkie f_i są ciągłe, a każda topologia, w której są ciągłe, zawiera tę podbazę, więc również generowaną topologię. Dla pustego I podbaza jest pusta, zaś puste przecięcie to X: otrzymuje się topologię antydyskretną, także dla X pustego. Nie założono niejawnie T1.

2. **Kryterium ciągłości do przestrzeni z topologią początkową — prop:topog-uzwarcenia-poczatkowa-ciaglosc.**
   W kierunku koniecznym ciągłość złożeń; w dostatecznym przeciwobrazy g^(-1)(f_i^(-1)(V))=(f_i∘g)^(-1)(V) są otwarte, a przeciwobraz zachowuje sumy i skończone przecięcia. Dla I pustego dowolne g do antydyskretnego X jest ciągłe, warunek na złożenia jest pusty. Działa też dla pustego Z.

3. **Funkcyjny opis przestrzeni Tychonoffa — thm:topog-uzwarcenia-funkcyjny-opis.**
   (i)⇒(iii): całkowita regularność dla F=X\U dostarcza h z h(x)=0 i h|F=1; f=1−h ma wartości wymagane w (iii). T1 zapewnia domkniętość singletonu {y}, więc dla x≠y dostajemy oddzielanie punktów. (iii)⇒(ii): wszystkie rozważane funkcje są pierwotnie ciągłe, zatem topologia początkowa jest słabsza; dla x∈U funkcja f daje otwarty w topologii początkowej przeciwobraz (1/2,1], zawarty w U, co dowodzi inkluzji odwrotnej. (ii)⇒(i): skończony cylinder W zawiera x i leży w X\F; dla każdej współrzędnej wybieramy ciągłą h_j na [0,1], równą 0 w f_j(x) i 1 na dopełnieniu V_j. Istnieje dzięki normalności/całkowitej regularności metrycznego odcinka, nie wskutek założenia o X. Skończone maksimum h_j∘f_j jest 0 w x i 1 poza W, więc na F. Jeśli F jest puste, wystarcza stała 0. Jeśli F jest niepuste, W≠X, więc ilość warunków m nie jest zerem. Wersja z V_j=[0,1] też jest obsłużona przez h_j=0.

4. **Istnienie uzwarcenia Hausdorffa — thm:topog-uzwarcenia-istnienie.**
   Dla uzwarcenia (K,e) zwarty Hausdorff K jest normalny oraz T1, stąd dzięki lematowi Urysohna jest Tychonoffa; tę własność dziedziczy e(X) i przenosi homeomorfizm na X. Odwrotnie, wcześniejsze twierdzenie rozdziału 07 daje zanurzenie X w kostkę [0,1]^I, która jest zwarta i Hausdorffa, a domknięcie obrazu jest zwartą Hausdorffa przestrzenią z gęstym e(X). Nie używa się lokalnej zwartości. Dla X pustego uzwarczenie puste także spełnia definicję.

5. **Jednoznaczność zgodnego homeomorfizmu — prop:topog-uzwarcenia-homeomorfizm-jednoznaczny.**
   Zbiór równości dwóch map ciągłych H1,H2:K1→K2 jest przeciwobrazem przekątnej K2, domkniętej dzięki Hausdorffowości K2. Ponieważ zawiera gęste e1(X), jest całym K1. To uzasadnia mocniejszą tezę „co najwyżej jedno odwzorowanie ciągłe”, bez zakładania istnienia homeomorfizmu.

6. **Uzwarcenie przestrzeni zwartej — prop:topog-uzwarcenia-zwarta.**
   Ciągły obraz zwartego X jest zwarty, a więc domknięty w Hausdorffowym K. Równoczesna gęstość e(X) wymusza e(X)=K, a zanurzenie staje się homeomorfizmem. Obejmuje przypadek X=∅ (wtedy K=∅).

7. **Porządek na klasach uzwarceń — prop:topog-uzwarcenia-porzadek-klasy.**
   Jednoznaczność zgodnego p wynika z dowodu 5. Obraz p(K1) jest zwarty/domknięty w K2 i zawiera gęste e2(X), stąd surjekcja. Zwrotność to identyczność, przechodniość to składanie zgodnych map. Gdy istnieje p oraz q w przeciwnym kierunku, złożenia są równe identycznościom na gęstych obrazach X, a dowód 5 daje równości na całych K1 i K2. Zatem p i q są odwrotnymi homeomorfizmami. Przejście na klasy równoważności jest poprawne dzięki składaniu z homeomorfizmami zgodnymi z zanurzeniami. Antysymetria odnosi się **tylko do klas**, nie do samych par.

## 2. Przykłady i przypadki szczególne

- **Dyskretna R i arctan:** funkcja 1/2+(1/π)arctan x jest ciągłą bijekcją R_euklidesowej na (0,1) o ciągłej odwrotności; jej topologia początkowa na R_dyskretnej jest zwykłą topologią euklidesową, co nie jest sprzeczne z twierdzeniem dla całej rodziny C(X,[0,1]).
- **(0,1) → [0,1] oraz S¹:** t↦exp(2πit) jest zanurzeniem o gęstym obrazie S¹\{1}. Hipotetyczny homeomorfizm zgodny z obydwoma zanurzeniami musiałby przez ciągłość wysłać 0 i 1 na ten sam punkt 1, wbrew różnowartościowości. Jednocześnie mapa [0,1]→S¹ jest zgodnym czynnikiem w prawidłowym kierunku porządku.
- **Dyskretne N → {0}∪{1/n}:** wszystkie 1/n są izolowane, a 0 jest punktem granicznym. Funkcja do [0,1] przedłuża się ciągle dokładnie wtedy, gdy wartości f(n) są zbieżne. W kierunku dostatecznym dla ε wybieramy N, a następnie 0<δ<1/N: każdy punkt 1/n w [0,δ) ma n>N i odpowiednio małą różnicę od granicy. Funkcja naprzemienna 0/1 dostarcza rzeczywistego kontrprzykładu do nieuprawnionej własności przedłużania każdej funkcji ograniczonej.

## 3. Zależności, LaTeX i CI

- Odczytano źródła rozdziałów 05 (blob 462acd8f3e1e350478d921429118ec19ac7f4ca8) i 07 (blob 0c31028e8fd301d805781b676c6713a2572501cf). Rozdział 05 jawnie definiuje całkowitą regularność, dowodzi lematu Urysohna i dziedziczenia aksjomatu Tychonoffa. Rozdział 07 zawiera twierdzenie o zanurzaniu w kostkę i wniosek o zwartym domknięciu obrazu. Nie wykryto kołowego odwołania.
- Odczytano istniejący test tools/tests/test_general_topology_ch16.py (blob fec312dd601d0e914fedd053a03e43caa3e3d97d): obejmuje skończone modele topologii początkowej, etykiety, bilans środowisk i odsyłacze. Test nie stanowi formalnego dowodu ogólnego twierdzenia. Nie dodano nowego testu, ponieważ nie wykryto błędu ani zmiany semantycznej.
- Weryfikowalny przebieg GitHub Actions [45082314478](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45082314478) dla commitu ef71d9d89f4b482f5de371be1c9241b3fc4a507d ma wynik **completed/success**. Potwierdzono przez API status joba 137392991159: PASS dla testu rozdziału 16, globalnego walidatora, budowy całej książki, samodzielnego rozdziału 16 i kontroli PDF/logów. Bezpośrednio ponownie odczytany blob rozdziału 16 na tym commicie jest dokładnie 1c2fcb925d62120feaea468400e48842a508a062, identyczny z badanym.
- Artefakt przebiegu: **14778385035** (general-topology-ch01-ch26; dostępny, nie wygasł). Istniejący globalny audyt 14 dokumentuje wizualny przegląd 27 rysunków w książce; sam rozdział 16 nie zawiera rysunków TikZ. Nie przeprowadzono w tej iteracji nowego wizualnego oglądu PDF ani nowej lokalnej kompilacji. Nie wolno więc przedstawiać dawnej inspekcji jako nowej.
- Samo dodanie tego raportu uruchamia nowy workflow poprzez filtr „audits/general_topology/**”. Wynik nowego przebiegu należy odczytać **po** commicie; nie wolno z góry oznaczać go jako PASS.

## 4. Werdykt i stan otwarty

**PASS matematyczny: 7/7 dowodów rozdziału 16 na podanym, aktualnym blobie**, poprawne trzy przykłady i zależności od wcześniejszych rozdziałów. Bez zmian w zatwierdzonym źródle. Dokumentacja audytów 01–03 rozdziału 16 i sukces CI potwierdzają dotychczasową stabilizację; ten raport zamyka brakującą pozycję globalnego rejestru dowodów dla rozdziału 16, ale nie poświadcza pozostałych rozdziałów ani nie zastępuje nowego CI na przyszłej głowicy.

**Następny krok:** rozdział 17 — niezależny audyt wszystkich 10 środowisk proof i przykładów (uzwarcenia Aleksandrowa oraz Čecha–Stone’a), na jego aktualnym blobie. Następnie 18 itd. W końcowym rejestrze rozdziałów 01–23 należy sprawdzić rzeczywistą liczbę dowodów na bieżących źródłach; historyczne **261** pochodzi z raportu globalnego 01, gdy katalog zawierał jedynie 22 rozdziały. W repozytorium obecnie istnieją także rozdziały 24–26, których nie należy mylić z zakresem wskazanym przez użytkownika.

**Nie zamykamy jeszcze audytu globalnego ani automatyzacji.**
