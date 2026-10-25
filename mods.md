# Uzasadnienia zmian w repozytorium `mathematical_scipts`

## 2026-10-25 — pełny audyt rozdziału 34

### Problem

Rozdział o formach przecięcia zawierał poprawny pełny rachunek $E_8$,
macierz obramowanego splotu i wyjaśnienie przeszkody dla triku Whitneya,
ale zaplanowany przypadek $2E_8$ był jedynie wymieniony. Nie było jawnego
rachunku jego rzędu, wyznacznika i sygnatury ani wyraźnego rozróżnienia
sumy ortogonalnej $E_8\oplus E_8$ od skalarnej macierzy $2\cdot E_8$.
Opis macierzy splotu nie objaśniał także, dlaczego pomocniczy wybór
orientacji komponentów nie zmienia klasy izometrii formy.

### Rozwiązanie i wpływ

- W `tex/rozdzialy/31-freedman-formy-przeciecia.tex` dodano przykład
  $2E_8=E_8\oplus E_8$. Z blokowej postaci wyprowadzono wyznacznik $1$,
  sygnaturę $16$, parzystość, unimodularność i dodatnią określoność.
- Parzystość odróżnia $2E_8$ od dodatnio określonej formy diagonalnej
  $I_{16}$, mimo zgodności rzędu i sygnatury.
- Dwie rozłączne kopie splotu realizują blokową macierz $2E_8$, ale tekst
  wyraźnie nie utożsamia tego gładkiego korpusu z brzegiem z zamkniętą
  rozmaitością. Topologiczne istnienie nadal jest jawnym wejściem
  Freedmana, a przeszkoda gładka pozostaje w rozdziale o Donaldsonie.
- Dopisano wpływ odwrócenia orientacji komponentu splotu. Zmiana znaków
  odpowiedniego wiersza i kolumny jest kongruencją przez diagonalną
  macierz z jednym wpisem $-1$, więc nie zmienia klasy izometrii.
- `PLAN_DZIALANIA.md` oznacza wyłącznie rozdział 34 jako ukończony i
  pozostawia rozdział 35 jako następny etap. `PRZEGLAD.md` zapisuje zakres
  audytu i wyniki kontroli; rozdziałów 35--38 w tej iteracji nie audytowano.
- Zaktualizowano trzy PDF-y tomów, ponieważ pełny skrypt stabilizuje
  odsyłacze między nimi. Tom III wydłużył się ze 171 do 172 stron.

Kompromisem jest pozostawienie głębokiego topologicznego wypełnienia
brzegu i klasyfikacji Freedmana jako wyników zewnętrznych. Jest to zgodne
z rzeczywistym zakresem rozdziału 34 i nie sugeruje dowodu, którego tekst
nie zawiera.

### Weryfikacja

Niezależna kontrola wyłącznie rozdziału 34 potwierdziła rachunki $E_8$,
$2E_8$, macierzy splotu, homologii brzegu i wymiarów w argumencie Whitneya.
Pełny `buduj_tomy.ps1` zakończył dwa przebiegi: tomy mają 216, 182 i 172
strony, a indeksy przyjęły 113, 96 i 119 haseł bez odrzuceń i ostrzeżeń.
Logi nie zawierają błędów, niezdefiniowanych odsyłaczy, `Overfull` ani
brakujących znaków. Obejrzano wszystkie strony rozdziału 34 w finalnym
PDF-ie tomu III; nowy przykład, akapit o orientacjach, wzory i rysunki są
czytelne. Kontrola XML potwierdziła poprawne cele odsyłaczy, w tym do
wyników używanych później, bez audytowania treści późniejszych rozdziałów.

## 2026-10-25 — audyt dodatków A i B

### Problem

Dodatek A nie odzwierciedlał w pełni wyników zewnętrznych faktycznie
używanych w rozdziałach. Najistotniejsza niezgodność podawała zakres
twierdzenia Walla jako wymiar co najmniej sześć, chociaż wersja
nieparzysta obejmuje również wymiar pięć. Katalog pomijał także między
innymi dekorację `h`, ciąg Rothenberga, część teorii torsji Whiteheada,
globalną geometrię rozdziału 14, normalizację Cherna--Weila oraz główne
wejścia do klasyfikacji Bardena i sfer wymiaru siedem.

Dodatek B miał poprawne rachunki, lecz trzy miejsca wymagały domknięcia:
użyty homeomorfizm nie był nazwany, skończony model CW kobordyzmu nie
wynikał jawnie z tekstu, a planowany związek cechy Eulera z dualnością
Poincarégo nie został podany.

### Rozwiązanie i wpływ

- W `tex/dodatki/a-zaleznosci-zewnetrzne.tex` poprawiono zakres Walla
  do `n >= 5`, rozdzielono kryterium przeszkody od twierdzeń
  realizacyjnych i opisano wersję z brzegiem, dekorację `h`, ciąg
  Rothenberga oraz ciąg dokładny chirurgii.
- Poprawiono niedziałający DOI pracy Whiteheada o triangulacji gładkiej,
  zapisano współczynniki grup `L` w ciągu chirurgii, doprecyzowano
  kofinalność dobrych pokryć i jednoznaczność rozkładu de Rhama oraz
  uzupełniono odsyłacz do stabilnego wygładzania u Freedmana--Quinna.
- Ten sam katalog uzupełniono o miarę Hausdorffa, dokładniejsze hipotezy
  triku Whitneya, torsję Whiteheada, Ambrose'a--Singera, globalny
  rozkład de Rhama, miarę Haara, zgodność Cherna--Weila z klasami
  topologicznymi, pełniejsze wejścia Bardena, Eellsa--Kuipera,
  Kervaire'a--Milnora i Quinna. Doprecyzowano też zależności w wymiarach
  trzy i cztery.
- W `tex/dodatki/b-homologia-singularna-euler.tex` nazwano homeomorfizm
  `h`, wyprowadzono skończony typ CW przestrzeni `W` z względnego
  rozkładu uchwytowego oraz dodano konsekwencję dualności Poincarégo:
  zamknięta zorientowana rozmaitość nieparzystego wymiaru ma cechę
  Eulera równą zero.
- `PLAN_DZIALANIA.md` zaktualizowano po zakończeniu obu audytów;
  pozostaje on jedynym miejscem bieżącego zakresu i kolejki.
- `PRZEGLAD.md` rejestruje ustalenia matematyczne, źródła, zakres
  poprawek i wyniki weryfikacji. `README.md` wskazuje niniejszy plik
  i `manual.md` jako dokumentację ogólnorepozytoryjną.
- `manual.md` rozdziela wykonane polecenia od instrukcji dla czystego
  stanowiska i podaje instalację Git, MiKTeX, pakietów TeX oraz `ripgrep`,
  katalog roboczy, wersje sprawdzone i używane polecenia kontroli PDF.
- Trzy pliki `geometria_tom1.pdf`, `geometria_tom2.pdf` i
  `geometria_tom3.pdf` wygenerowano ponownie, aby utrwalić zgodne
  odsyłacze między tomami; wydłużył się tylko tom III, z 168 do
  171 stron.

Zmiana nie próbuje zastępować głębokich twierdzeń własnymi szkicami.
Kompromisem jest dłuższy dodatek A, ale w zamian granica
samowystarczalności skryptu i dokładne hipotezy są jawne w jednym
miejscu.

### Weryfikacja

Uruchomiono pełny `buduj_tomy.ps1`. Dwa przebiegi ustabilizowały pliki
pomocnicze. Tomy mają 216, 182 i 171 stron, a indeksy przyjęły 113, 96
i 119 haseł bez odrzuceń. Nie ma niezdefiniowanych odsyłaczy,
`Overfull`, brakujących znaków ani błędów TeX-a. Obejrzano wszystkie
zmienione strony dodatków A i B. Na finalnym PDF-ie ponownie wyodrębniono
tekst i XML, po czym sprawdzono odsyłacze do tomów I i II. Znane
ostrzeżenia `Underfull`, zduplikowany cel `page.1` oraz dwa ostrzeżenia
tomu I o zmianie specyfikatora rysunku z `h` na `ht` były obecne przed
tym etapem i nie dotyczą zmienionych stron.
