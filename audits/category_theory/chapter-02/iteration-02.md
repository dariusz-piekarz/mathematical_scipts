# CAT-02 — audyt II (stabilizacyjny)

Stan badany d43e990d027114f001567887f94b8e1774e42c7e; źródło 189e58009836c8077788f3e5530e71f8c548c6cd; test 961e894cbae4e6a20df5b66341416ce5d58dc07f.

## Ponowna kontrola matematyczna
- Izomorfizmy: oba złożenia z odwrotnością i jedyność wynikają z łączności i obustronnych jednostek.
- Mono i epi: poprawne strony skracania, poprawne typy morfizmów. Reguły składania i wnioski z moniczności/epiczności złożenia mają właściwe kierunki. Odwrotności jednostronne z odpowiednią skracalnością dają odwrotności obustronne.
- Set: świadek z singletonu wykrywa brak iniektywności; dwie funkcje do zbioru dwuelementowego wykrywają brak surjektywności. Pusty zbiór uwzględniony, gdy istnieją stosowne funkcje.
- Grp: u(h) to permutacja z odwrotnością u(h^{-1}); u(ab)=u(a)u(b). Tau jest inwolucją. Dla k w K=f(G), kx w K wtedy i tylko wtedy, gdy x w K (mnożenie przez k^{-1}). Stąd sprzężone działania zgadzają się na K, lecz różnią się na (1,0) dla każdego h spoza K. Nie użyto normalności K.
- Moduły: r↦rx jest homomorfizmem lewych modułów dzięki łączności działania; iloraz przez obraz jest modułem niezerowym dokładnie przy braku surjektywności; projekcja jest różna od zera i zeruje obraz. Liniowość odwrotności bijekcji wynika przez zastosowanie f. R nie musi być przemienny.
- Top: przestrzeń jednopunktowa testuje iniektywność; dowolna funkcja do przestrzeni antydyskretnej jest ciągła, więc świadek braku surjektywności działa. Bimorfizm dyskretna→antydyskretna nie ma ciągłej odwrotności.
- Man: x↦x³ jest gładką bijekcją, odwrotność nie jest różniczkowalna w 0. Nie utożsamiono gładkiej bijekcji z dyfeomorfizmem.
- Ring: jednoznaczność przedłużenia lokalizacji dowodzi epiczności bez założenia iniektywności; inkluzja Z→Q stanowi kontrprzykład dla zachowania epimorfizmów przez funktor zapominania.
- Regularność: definicje odpowiadają equalizatorowi i koequalizatorowi; skracalność wynika z jednoznaczności faktoryzacji. W Set dla iniekcji wykorzystano funkcję charakterystyczną dopełnienia obrazu; dla surjekcji relację par o tym samym obrazie. Faktoryzacja jest zdefiniowana przez jedyność wartości na włóknie, bez globalnego wyboru przekroju.
- Brak nowych istotnych usterek; nie zmieniano źródła i nie rozszerzano materiału.

## CI
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45576579518, commit 9811216fa141e8a0bbf618fc64af1cda35420147. Krok Category theory regression tests: completed/success (4+5+5 metod). Porównano 24 bloby (19 rozdziałów, książka, 3 pliki testowe, workflow): bez różnic. W chwili zapisu ostatniego sprawdzenia kompilacja trwała, kontrola PDF i upload pozostawały pending. Nie odczytano pełnych logów; nie wykonano wizualnej kontroli PDF ani formalizacji Lean.

## Decyzja
Kontrola matematyczna audytu II i testy automatyczne zaliczone. Bramka kompilacji pozostaje otwarta do potwierdzenia. Następnie wymagany niezależny audyt III, przed przejściem do CAT-03.