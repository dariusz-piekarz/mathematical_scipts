# Topologia algebraiczna — TOP-14, audyty I–V, zamknięcie

**Data:** 2026-11-21  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez nowej gałęzi ani zmian w `main`).  
**Źródło:** `chapters/pl/algebraic_topology/14-wieze-postnikowa-iloczyny-whiteheada-i-operacje-steenroda.tex`; końcowy blob Git `0356bf9136090fa01f3dab72c3bf1a364eec965c`, 1264 wiersze.  
**Zasady:** weryfikacja istniejących definicji, twierdzeń, dowodów, przykładów, rysunków, terminologii, odsyłaczy i CI; nie dodano nowych wyników, lematów ani sekcji tematycznych.

## Audyt I — lemat o potęgach ekwiwariantnych, relacje Adema i zakres dowodu

Przeanalizowano cały tekst: etapy Postnikowa, włókna homotopijne i niezmienniki k, przypadek S², iloczyny Whiteheada i niezmiennik Hopfa, przeszkody podnoszenia, konstrukcję \smile_i, kwadraty Steenroda, wzór Cartana, relacje Adema i wszystkie przykłady. Porównano z wcześniejszym raportem `TOP_13_14_FINAL_REAUDIT_2026-11-21.md`.

Rozdzielono dwa poziomy uzasadnienia w istniejącym dowodzie relacji Adema: (i) nietrywialną tożsamość współczynników uzyskaną ze spójnej konstrukcji potęg ekwiwariantnych dla czterech czynników, będącą częścią jawnie wskazanego lematu zewnętrznego; (ii) wykonywany już w rozdziale algebraiczny rachunek parzystości współczynników dwumianowych z użyciem kryterium Lucasa. Nie twierdzimy już, że pierwszy krok daje się wyprowadzić z samej relacji koróżniczki dla pojedynczych wyższych diagonalnych. W ten sposób dokładnie oznaczono zakres samodzielnego dowodu bez ukrywania jego zewnętrznego składnika.

Uzupełniono przejście od równości na klasach uniwersalnych o stopniu `N=2^r-1+b` do wszystkich stopni, uwzględniając zawieszenia, stopień zero i CW-przybliżenie dowolnej przestrzeni `|Sing X|→X`. Nie zmieniono matematycznej treści relacji Adema.

**Commit:** `3d091347c950852d8ab2fcf090ef09d25474e6cc`.

## Audyt II — język podręcznika i regresje rachunkowe

Usunięto z tekstu robocze uwagi o „poprzedniej próbie” i komentarz iteracyjny z końca pliku, zastępując je matematycznym uzasadnieniem właściwego doboru kołańcucha pierwotnego. Zachowano wyprowadzenie formuły różniczki dla \smile_i i wszystkich 17 etykiet.

Rozszerzono regresje w `application/tests/test_topology_chapters_13_14.py` o **8281 testów** relacji Adema na jednomianach w pierścieniu `H*(RP∞ × RP∞; F₂)=F₂[t,s]`: dla `0≤m,n≤12`, `1≤b≤7` i `1≤a<2b` obie strony obliczano osobno przez wzór Cartana i parzystość symboli Newtona. Jest to test zgodności formuł, nie zastępstwo dowodu uniwersalnego.

**Commity:** `08f0a62ff8687f9710d65bdcfc11c8aee97ab9da`, `bf3f9d064ef4792263dbbf998090dff82ba24f2b`.

## Audyt III — dowód zgodności z zawieszeniem

Jawnie wykorzystano iloraz `q:S¹×Z→S¹∧Z=ΣZ` i wzór `q*(Σz)=u×z` na kohomologii zredukowanej. Z naturalności i zewnętrznego wzoru Cartana otrzymujemy równość po cofnięciu, a z iniektywności homomorfizmu indukowanego przez `q` — równość operatorów przed cofnięciem. Wyjaśniono iniektywność przez summandę produktu zewnętrznego w rozkładzie Künnetha nad ciałem `F₂`. Uzasadnia to przenoszenie relacji z odpowiednio dużego stopnia na niższy.

**Commit:** `39cebf50ef787672afd4c3c7b1469f170e89855c`.

## Audyt IV — samodzielność sformułowania twierdzenia

W twierdzeniu o wzorze Cartana i relacjach Adema jawnie wpisano dowolną przestrzeń topologiczną `X`, nieujemność stopni `p,q,k` i dodatniość liczb całkowitych `a,b` z `0<a<2b`. Dzięki temu twierdzenie nie wymaga domyślania się kwantyfikatorów z kontekstu.

**Commit:** `586dbae7636cdebf2c005fada167b4f7ea462d24`.

## Audyt V — niezależna kontrola i matematyczne sprawdzenie obliczeń

Bezpośrednio odczytano końcowe źródło GitHub, skontrolowano pary i zagnieżdżenia wszystkich środowisk LaTeX, 17 unikalnych etykiet oraz obecność wzorów na k-niezmienniki, kwadrat Whiteheada i relacje Adema. Nie znaleziono kolizji etykiet, niedomkniętych środowisk, starych komentarzy roboczych ani zabronionych terminów (np. „tensorowanie”, „sekwencja” i „injekcja”). Zachowano dwa diagramy TikZ, bez zależności od zewnętrznych obrazów.

Dodatkowo sprawdzono historyczne źródła odniesień do relacji Adema i sekcji 4.L Hatchera, uwzględniając opublikowane erraty; powoływana praca *A cochain level proof of Adem relations in the mod 2 Steenrod algebra* istnieje (Brumfiel–Medina-Mardones–Morgan, 2021). Nie wyprowadzono żadnej nowej tezy na podstawie eksperymentów obliczeniowych.

## Końcowe wyniki GitHub Actions

Wszystkie trzy workflowy dla aktualnego commita źródła `586dbae7636cdebf2c005fada167b4f7ea462d24` mają status **completed / success**:

- [Kompilacja TOP-01–14 LaTeX i kontrola odsyłaczy](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929093838) — sukces.
- [Testy aplikacji, w tym 8281 rachunków testowych relacji Adema](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929093835) — sukces.
- [Audyt zależności AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929093910) — sukces.

**Decyzja:** TOP-14 **stabilny po pięciu audytach**. Zachowano 17 historycznych etykiet i wszystkie istniejące twierdzenia, lematy, przykłady i diagramy; skorygowano jedynie ich uzasadnienia i precyzję. Kolejny rozdział do audytu stabilizacyjnego to **TOP-15**. Automatyzacje pozostały wyłączone.
