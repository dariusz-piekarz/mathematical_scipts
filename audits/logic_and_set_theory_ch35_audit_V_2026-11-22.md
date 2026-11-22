# Logika matematyczna i teoria mnogości — audyt V rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Blob źródła po audycie:** bb799ab39a13d9a577b07caaba24e3e00b6bca7e.  
**Werdykt:** audyt V **nie jest czysty**, ponieważ naprawił istotny skrót w dowodzie odwrotnego przekładu nazw boolowskich. Pełny CI jest zielony; konieczna kolejna niezależna iteracja.

## Niezależna kontrola matematyczna

Ponownie sprawdzono definicję zupełnej algebry Boole'a, regularnego otwarcia, gęstą mapę i:P→RO(P), rekurencję po rangach nazw, wartości atomowe, tożsamości równości, mieszanie, pełność, wszystkie konstrukcje aksjomatów ZFC, iloraz przez dowolny ultrafiltr i dwie algebry dające wartości 1 odpowiednio CH i ¬CH.

W aksjomacie ufundowania minimalizuje się rangę po klasie *wszystkich* możliwych świadków, nie tylko dziedzinie nazwy. W aksjomacie potęgowym reprezentant f_tau ma dziedzinę dom(sigma), ale jest tylko boolowsko równy tau pod warunkiem tau⊆sigma; nie utożsamia się nazw jako funkcji. Zastępowanie dowodzi obustronnej równości wartości na fragmencie funkcjonalności. Wybór przenosi porządek liczby porządkowej przez nazwaną surjekcję K→sigma i wybór najmniejszych przeciwobrazów. Lemat prawdy dla dowolnego ultrafiltru używa pełności, nie fałszywej zasady, że ultrafiltr zawierający supremum zawiera składnik.

### Poprawka w odwrotnym przekładzie nazw

Audyt IV wprowadził tau^P, ale wniosek
⟦tau=(tau^P)^B⟧=1
był jeszcze uzasadniony tylko jednym zdaniem „indukcja po rangach”.

Rozwinięto dowód. Dla rho∈dom(tau) definiuje się rho_*=(rho^P)^B, a hipoteza indukcyjna zapewnia ⟦rho=rho_*⟧=1. Gęstość i(P) daje współczynnik tau(rho) po połączeniu obrazów wszystkich p z i(p)≤tau(rho). Po ewentualnym połączeniu dosłownie równych argumentów nazwy i dla dowolnej eta otrzymujemy dokładną tożsamość
⟦eta∈(tau^P)^B⟧ = ∨_{rho∈dom(tau)}tau(rho)∧⟦eta=rho_*⟧ = ∨_{rho}tau(rho)∧⟦eta=rho⟧ = ⟦eta∈tau⟧.
Z boolowskiej ekstensjonalności wynika wartość 1 równości nazw. Dodano również kontrolę standardowej nazwy G={(check p,p):p∈P}: dla każdej nazwy kanonicznej warunku p otrzymuje się ⟦check p ∈ G^B⟧ = i(p). W przypadku kwantyfikatora egzystencjalnego można więc poprawnie zamienić świadka boolowskiego z lematu pełności na równoważną nazwę porządkową.

## Niezależne sprawdzenia skończonych struktur

Testy uruchomione lokalnie w Pythonie, niezależnie od wcześniejszych 16 metod:
- w algebrze 8-elementowej, trzy atomy: **96 000 kontroli** semantyki równości i przynależności; **1344** kontroli ufundowania; **1536** kontroli zbioru potęgowego z reprezentantem f_tau; wszystkie PASS;
- wszystkie **388 preorderów** na odpowiednio 2, 3 i 4 elementach (4, 29, 355): poprawność RO, dopełnienia, przecięć i skończonych supremów, gęstość obrazów warunków, zgodność pojęć zgodności i wspólnego wzmocnienia; wszystkie PASS;
- **192** lokalne równoważności dla mieszania nazw z trzech atomów, wszystkie PASS.

W repozytorium zapisano dwie nowe metody regresyjne: test_three_atom_name_semantics_power_set_and_foundation oraz test_ro_completion_for_every_small_preorder. Zestaw rozdziału 35 ma obecnie **18 metod testowych**.

## LaTeX, odsyłacze, PDF

W rozdziale: 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 etykiet, 32 odsyłacze. W całej książce: 672 odsyłacze; poprawiono ich licznik w workflow i teście po dodaniu drugiego odsyłacza w uzupełnieniu dowodu. Żadne środowisko LaTeX nie jest niedomknięte.

**Pełne GitHub Actions [45048284035](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45048284035): SUCCESS.** Przeszły testy 01–35, inwentarz, kompilacja LaTeX, kontrola PDF i logu. Pobrano faktyczny artefakt przebiegu: książka 308 stron, rozdział 35 na stronach PDF 296–308. Wyrenderowano i wzrokowo sprawdzono wszystkie 13 stron rozdziału. Brak kolizji, przepełnionych wierszy, błędów odsyłaczy i nieczytelnych wzorów; jedna uwaga o niedopełnionym wierszu w całej książce poza nową zmianą, bez wpływu na czytelność.

**Commity:** 0537ec5f91e800c06fa5cac16e1c4557d1a79eb0 (test 3 atomów), 1353e0f1d580a196f3106d26c188f49b9b441e7c (wszystkie małe preordery), 601c0e5410f3d91c506722f1d1aaa16ce43e9942 (dowód), 619843ab6f8092c762c2ab99dd2343b178b8512f (inwentarz workflow), a11ee5fdc2495e8fd464af46e1b8e3653c32c156 (inwentarz testu).

## Następny etap

Ponieważ audyt V wymagał poprawki matematycznej, licznik niezależnych czystych audytów: **0**. Wykonać audyt VI na blobie bb799ab39a13d9a577b07caaba24e3e00b6bca7e, następnie niezależny audyt VII oraz końcowy audyt potwierdzający bez zmiany źródła. Testy numeryczne ani CI nie są formalną weryfikacją w Lean.
