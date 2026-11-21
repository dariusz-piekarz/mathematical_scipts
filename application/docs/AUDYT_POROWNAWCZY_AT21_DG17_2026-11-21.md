# Etap VIII — audyt porównawczy AT-21 / DG-17: indeks, brzeg i względna klasa Eulera

**Data:** 21 listopada 2026 r.  
**Repozytorium:** dariusz-piekarz/mathematical_scipts  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (bez zmian w main).  
**Zakres:** szczegółowy audyt dwóch pełnych rozdziałów, tj.
AT-21 (*Indeks pól wektorowych i twierdzenie Poincarégo–Hopfa z brzegiem*)
i DG-17 (*Przecięcia, dualność i klasy charakterystyczne*).

**Automatyzacje:** na wyraźne polecenie użytkownika wyłączono wszystkie trzy zadania cykliczne:
logika i teoria mnogości, algebra abstrakcyjna, topologia algebraiczna.
Nie uruchamiano ani nie tworzono nowego zadania okresowego.

## 1. Mapa pojęć i zachowanie treści

AT-21 w oryginalnej wersji zawierał porównanie lokalnego indeksu zera pola z indeksem punktu stałego przy użyciu mapy wykładniczej, alternatywny dowód twierdzenia Poincarégo–Hopfa przez liczbę Lefschetza, pełną wersję dla pola skierowanego na zewnątrz brzegu oraz wzór (-1)^n χ(M) dla pola skierowanego do wnętrza, z przykładami dysku i pierścienia.

DG-17 obejmuje znacznie szersze tło: kohomologię i iloczyny kubkowe, dualność Poincarégo, systemy lokalne, liczby przecięcia, wiązki, klasy Stiefela–Whitneya, klasę Thoma, bezwzględną klasę Eulera, lokalne indeksy pola i ich interpretację przez Poincarégo–Hopfa, samoprzecięcia i przygotowanie do chirurgii. Nie należy usuwać pełnego rozdziału DG-17 z powodu częściowego pokrycia AT-21.

Po poprawkach jest **12 etykiet w AT-21** i **57 w DG-17**; **brak nazw wspólnych** w tej parze, ale dużo związków matematycznych.
Pełny dokładny wykaz etykiet i decyzji:
application/config/KANDYDACI_SCALEN_AT_DG_ETAP_08.json.
Historyczne etykiety i wszystkie istniejące różne dowody zachowano.

## 2. AT-21 — nowy dowód ogólnej formuły stopnia brzegowego

### Twierdzenie thm:PH-stopien-brzegowy-21

Niech n≥2 i U⊂R^n będzie ograniczonym obszarem o gładkim, zwartym brzegu. Niech X∈C¹(\bar U,R^n) nie znika na ∂U i ma skończenie wiele izolowanych zer p_j we wnętrzu.

Suma indeksów jest równa stopniowi mapy brzegowej:
  Σ_j ind_{p_j}(X) = deg((X/|X|)|_{∂U}).
Konieczne jest zorientowanie ∂U konwencją „zewnętrzna normalna, potem styczna”.

**Pełny rachunek:** usuwamy rozłączne kulki B_j wokół zer i bierzemy V=\bar U\setminus∪int B_j. Na V mapa u=X/|X| jest ciągła do S^{n−1}. Z długiego ciągu pary (V,∂V) obraz [∂V] w H_{n−1}(V;Z) znika. Pod mapą u_* dostajemy u_*[∂V]=0 w H_{n−1}(S^{n−1};Z)=Z. Orientacja względnego brzegu daje
  [∂V]=[∂U]−Σ_j[∂B_j].
Porównanie współczynników na generatorze [S^{n−1}] daje stopień brzegowy równy sumie lokalnych stopni. Działa to również przy braku zer, kiedy suma jest pusta.

**Rozróżnienie:** twierdzenie nie utożsamia tej sumy z χ(U) dla dowolnego nieznikającego pola na brzegu. Taki wniosek wymaga dodatkowego warunku zewnętrzności lub innej hipotezy.

### Przykłady prz:PH-stopien-dysk-trzy-pola-21 i prz:PH-stopien-pierscien-21

Na D^n (n≥2) pola: stałe e_1, radialne x oraz dośrodkowe −x.
Stopnie normalizacji brzegowej wynoszą odpowiednio 0, +1 i (−1)^n.
Pole stałe nie spełnia założenia „zewnętrzne na całym brzegu”, więc nie stanowi kontrprzykładu dla Poincarégo–Hopfa z brzegiem.

Na pierścieniu płaskim a≤r≤b, r_0=(a+b)/2, bierzemy
X=(r−r_0)e_r+e_θ=e^{iθ}((r−r_0)+i).
Na obu okręgach parametryzowanych geometrycznie przeciwnie do wskazówek zegara funkcja ma stopień +1.
Jednak indukowana orientacja **wewnętrznej** składowej brzegu jest zgodna z ruchem wskazówek zegara: całkowity stopień wynosi (+1)+(−1)=0, co odpowiada brakowi zer i χ(pierścienia)=0.
Nie wolno sumować nieskorygowanych stopni po wszystkich składowych.

## 3. AT-21 — usunięcie niepotrzebnej hipotezy orientowalności

Twierdzenie thm:PH-boundary-v11 oraz Wniosek cor:PH-inward-boundary teraz nie wymagają orientowalności. Wynika to z charakteru użytego dowodu: lokalny indeks pola jest niezależny od wyboru orientacji mapy, liczba Lefschetza jest określona nad Q bez globalnej orientacji, a argument z podwojeniem rozmaitości i składaniem drugiej kopii nie potrzebuje orientacji.

**Jawny test nieorientowalny:**
Wstęga Möbiusa M=(R×[−1,1])/<g>, g(θ,t)=(θ+2π,−t), ze współrzędną t.
Pole \tilde X=∂_θ+t∂_t przechodzi na iloraz, gdyż Dg(1,t)=(1,−t)=\tilde X(g(θ,t)).
Nie ma zer, ponieważ składowa ∂_θ jest stała i niezerowa.
Dla metryki dθ²+dt² na obu reprezentantach brzegu t=±1 mamy
< X,ν > = t² =1>0.
M ściąga się na S¹, więc χ(M)=0. Twierdzenie daje 0=0, bez orientowalności i bez lokalnych systemów współczynników w samej formule indeksowej.
Jednocześnie zwykłej całkowitej klasy Eulera niezorientowanej wiązki TM nie wolno tu używać bez zmodyfikowanego systemu współczynników.

## 4. DG-17 — względna klasa Eulera, której wcześniej brakowało

### Definicja def:euler-wzgledna-brzeg-17

Dla zwartej zorientowanej gładkiej n-rozmaitości M z brzegiem,
zorientowanej wiązki rzeczywistej E→M rzędu n i zadanego
nigdzie nieznikającego przekroju s_∂ na ∂M,
przedłużenie s daje mapę par
  s:(M,∂M)→(E,E\setminus 0).
W modelu całkowitej klasy Thoma u_E∈H^n(E,E\setminus 0;Z) definiujemy
  e(E,s_∂)=s^*u_E ∈ H^n(M,∂M;Z).

Definicja jest precyzyjnie względna. W odróżnieniu od bezwzględnej
e(E) klasa zależy od **warunku brzegowego** s_∂.

### Twierdzenie thm:euler-wzgledna-liczba-indeksow-17

Konstrukcja przedłużenia odbywa się w kołnierzu brzegu
i przez podział jedności. Homotopia dwóch przedłużeń jest
liniowa we włóknach i nie zmienia brzegowego przekroju.
Stąd ich cofnięcia klasy Thoma są identyczne.

Po odjęciu małych dysków wokół izolowanych zer
cofnięta klasa względna jest wsparta w tych dyskach.
Wycięcie, dodatnie orientacje lokalnych trywializacji
i porównanie z generatorem H^n(R^n,R^n\{0};Z) dają
  <e(E,s_∂),[M,∂M]> = Σ_j ind_{p_j}(s).
Dowód obejmuje również zera osobliwe oraz sytuację, gdy zer nie ma.
Nie dokonujemy nieuzasadnionego podstawienia e(E) w miejsce względnej klasy.

### Przykład prz:euler-wzgledna-dysk-17

Dla E=TD^n, n≥2, trywialnej wiązki nad dyskiem,
przekrój s_∂ na S^{n−1} definiuje unormowaną mapę
g:S^{n−1}→S^{n−1}. Ewaluacja klasy względnej jest równa deg g.
W polach stałym, radialnym i dośrodkowym wynosi odpowiednio 0,1,(−1)^n, mimo że e(TD^n)=0 w H^n(D^n;Z).
To precyzyjnie wypełnia lukę pomiędzy rozdziałami.

## 5. Audyt wcześniejszych twierdzeń i zgodność z nimi

- DG-17 `thm:euler-thom-16`: zorientowana klasa Thoma w (E,E\setminus 0), naturalność i mnożenie przy sumie wiązek; poprawnie rozróżniamy wersję względną od bezwzględnej.
- DG-17 `thm:euler-zeros-16`: dla zer przekroju zamkniętej zorientowanej rozmaitości n-wymiarowej ocena na klasie fundamentalnej jest sumą znaków pionowej pochodnej. Nowy dowód powtarza niezbędny rachunek w **parze (M,∂M)**, zamiast kopiować bezwzględną tezę bez zmiany warunków.
- DG-17 `thm:poincare-hopf-16`: dla zamkniętych zorientowanych rozmaitości sumę indeksów identyfikuje z e(TM) i χ(M). AT-21 przez Lefschetza daje tę samą liczbę, a rozdział z brzegiem nie musi zakładać globalnej orientacji dla samego indeksu.
- AT-21 `lem:field-fixed-v11`: dla f_t(x)=exp_x(−tX(x)) mamy ind_p(f_t)=ind_p(X); przy zerach nieosobliwych wynika to także z I−Df_t=t DX_p. Nie zmieniono tego dowodu.
- AT-21 `cor:PH-inward-boundary`: antpodalne na S^{n−1} ma stopień (−1)^n. Wzór inward=(−1)^n χ(M) pozostaje poprawny także bez orientowalności.
- Pozostałe unikatowe części DG-17 (dualność Poincarégo, klasy Stiefela–Whitneya, samoprzecięcia, forma przecięcia, rysunki) i AT-21 (pola w pierścieniu i ustalona wersja przez Lefschetza) zostały zachowane bez utraty.

## 6. Korekta infrastruktury: historyczny test etapu V

Podczas dodawania nowych etykiet DG-17 starszy test
application/tests/test_at_dg_pairwise_11_17.py
`test_historical_unique_content_and_labels_preserved` zaczął błędnie wymagać
dokładnego zrównania bieżącego zbioru etykiet z **historycznym**
manifestem etapu V.

Wymaganie było sprzeczne z rozwojem rozdziałów:
prawidłowe dodawanie kolejnych twierdzeń daje nowe, odrębne etykiety.
Poprawka nie usuwa żadnego wymagania o zachowaniu historycznych
etykiet: historyczne, udokumentowane zbiory mają być **podzbiorami**
aktualnych zbiorów. Dodatkowo manifest etapu V zachowuje teraz
**dokładną listę 42 historycznie wspólnych etykiet**, a regresja
sprawdza zachowanie każdej ich nazwy w obu źródłach, nie tylko
ich całkowitej liczby.
Manifest etapu V pozostaje **migawką historyczną**, nie jest
przepisywany po każdej zmianie materiału.

## 7. Rzeczywista weryfikacja

**Testy tematyczne:** 13/13 zaliczone. Plik:
application/tests/test_at_dg_pairwise_21_17.py.

**Pełne testy aplikacji:** 348 testów, wszystkie zaliczone,
1 pominięty. GitHub Actions:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44885235290

**Pełna kompilacja TeX:** obydwa zadania workflow zakończone statusem
**SUCCESS**, trzy przebiegi pdflatex dla każdego tomu:
- AT-01–30: **300 stron**,
- DG-01–20: **492 strony**.

Workflow:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44885098954

Kontrola braku nowych niezdefiniowanych odsyłaczy i przepełnionych
wierszy zaliczona. W DG nadal występuje **12 znanych nazw**
niewyjaśnionych odsyłaczy do niezaimportowanych rozdziałów DG-21–36.
Nie są one skutkiem bieżącej iteracji i są jawnie kontrolowane,
a nie błędnie uznane za usunięte.

**Weryfikacja graficzna:** pobrano rzeczywiste PDF-y z workflow
i wyrenderowano/obejrzano strony **AT 226–227** oraz **DG 438–439**
z nowymi dowodami, notacją, przykładami i podpisami.
Sprawdzono brak obcięcia wzorów, niechcianego nakładania tekstu,
sprzecznych znaków i problemów z akapitami.
W tych miejscach nie stwierdzono problemów ze składem.

## 8. Stan i dalszy zakres

Zakończony jest audyt pary AT-21/DG-17, a nie całości
Biblioteki matematycznej. Nie scalono automatycznie
rozdziałów ani nie zmieniono istniejących \label, \ref.
Przy dalszym scalaniu należy explicite rozróżnić trzy
twierdzenia: Poincarégo–Hopfa na rozmaitości zamkniętej,
wersję z polem ściśle zewnętrznym na brzegu i
względny indeks zależny od ustalonego przekroju brzegowego.
Nie wolno podstawiać χ(M) do ostatniej sytuacji bez warunku zewnętrzności.

Pozostałe prace ogólnobiblioteczne: import DG-21–36,
sprawdzenie pochodzenia 12 nieznalezionych etykiet
oraz międzytomowe ustalenie właścicieli kanonicznych definicji.
