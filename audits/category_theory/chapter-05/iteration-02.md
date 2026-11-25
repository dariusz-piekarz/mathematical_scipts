# CAT-05 — audyt II (stabilizacyjny)

Stan badany: e0ccf152b0bc7627c53828f51330bb52afc77a0a.
Źródło: 34cf412b2a5190ecf4bb7f99e81c43c5298d4d4e.
Test: 37e2e8bef7ec4ab7676dd3c77fbe3ffb97a2ab2c.

## Kontrola semantyczna
- Definicje: początkowy ma dokładnie jedną strzałkę do każdego obiektu, końcowy dokładnie jedną z każdego obiektu. Dla pustej dziedziny funkcja do singletonu istnieje i jest jedyna; w Top ciągłość obu odpowiednich funkcji wynika z definicji.
- Jednoznaczność: złożenia dwóch kanonicznych strzałek są identycznościami przez jednoznaczność endomorfizmów, w obu kierunkach. Dla konstrukcji wyposażonych w dodatkowe dane jedyność dotyczy izomorfizmów zgodnych z danymi.
- Pierścienie: n↦n1_R jest wymuszone addytywnością i zachowaniem jedynki, działa również dla pierścienia zerowego. Ten ostatni jest końcowy. Po jego wykluczeniu hipotetyczne mapy z F2 i F3 wymuszają 2·1=3·1=0, więc 1=0. Nie utożsamiono pierścienia początkowego Z z zerowym. Konwencja zgodna z AA-09.
- Moduły i grupy: obiekt trywialny jest zarazem początkowy i końcowy; moduł wolny na pustym zbiorze jest zerowy. Top_*: jedyna strzałka ze singletonu wybiera wyróżniony punkt. Rel: oba iloczyny z pustym zbiorem są puste, co wymusza jedyną relację. Oznaczenia Rel i Top_* zgodne z CAT-01; odsyłacz sec:kategorie istnieje.
- Kategoria iniekcji: końcowość wymusza dokładnie jedną iniekcję z singletonu, a więc singleton jako przeciwdziedzinę; brak iniekcji z dwuelementowego zbioru daje sprzeczność. Jednoobiektowa kategoria nietrywialnej grupy nie ma obiektu początkowego ani końcowego.
- Rozszczepienia: dla f:T→A i końcowego T jedyna r:A→T daje r f=id_T; dla g:A→I i początkowego I jedyna s:I→A daje g s=id_I. Nie odwrócono tych twierdzeń. W Set strzałka pusty→singleton jest kontrprzykładem dla epiczności map do obiektu końcowego. Ścisła początkowość pustego obiektu Set i Top wynika z nieistnienia funkcji z niepustego zbioru do pustego. Grupa trywialna nie jest ściśle początkowa.
- Morfizmy zerowe: dla porównania obiektów zerowych h:O→O' zachodzi p'_A=h p_A oraz j'_B h=j_B, więc faktoryzacja jest niezależna od wyboru. Pochłanianie wynika z jedyności strzałek do i z O; wszystkie typy zgodne. Jeśli id_A=0_A,A, każda strzałka z A i do A jest odpowiednią strzałką zerową, która istnieje. To daje obie własności uniwersalne. Przykłady zer w Grp, modułach, Top_* i Rel są zgodne z definicją.
- Funktor zachowujący obiekt zerowy zachowuje zera przez funktorialność faktoryzacji i niezależność wyboru. Nie przypisano tej własności dowolnemu funktorowi.
- Zgodność kanonicznych porównań trzech początkowych lub trzech końcowych wynika z jedyności właściwej strzałki. Odsyłacze sec:morfizmy i sec:produkty istnieją w CAT-02/06.
- Brak nowych istotnych usterek; bez zmian źródła i bez rozszerzania zakresu.

## CI
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45586223164, commit 8a5961f5101942fd7970f9613f2582de142a279f. Job validate completed/success; wszystkie osiem kroków success, w tym testy, kompilacja całej książki, kontrola odsyłaczy i PDF oraz upload. Zestawy obejmują 4+5+5+6+6+5=31 metod testowych. Porównano 27 blobów (19 rozdziałów, książka, 6 plików testowych, workflow): bez różnic.
Nie odczytano pełnych logów ani nie wykonano kontroli wizualnej PDF. Testy skończone nie zastępują dowodów. Nie wykonano formalizacji Lean.

## Decyzja
Audyt II zaliczony bez zmian. Wymagany niezależny audyt III i kontrola PDF przed CAT-06.
