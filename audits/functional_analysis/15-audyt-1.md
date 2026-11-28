# Analiza funkcjonalna — rozdział 15 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (istniejąca).  
**Źródło:** `chapters/pl/functional_analysis/15-pochodne-wyzszych-rzedow-i-lokalne-twierdzenia-analizy-nieliniowej.tex`  
**Blob źródła przy odczycie:** `39f14f53417fd613006032d5cb5e9b7bbdcc6ebe`.  
**Werdykt:** audyt inicjalny, **0/2 czystych audytów stabilizacyjnych**. Brak potwierdzonego CI dla rozdziału 15.

## Stan zastany

Odczytano przez GitHub API gałąź, katalog `audits/functional_analysis`, źródło rozdziału 15 oraz raport 14/03. Najnowszym raportem analizy funkcjonalnej był `14-audyt-3.md`; raport 15/01 nie istniał. Rozdział 14 zamknięto jako stabilny (12/12 dowodów, 8/8 przykładów, dwa czyste audyty), a dedykowany workflow 14 na commicie `28bcc767f87f212128a12dd8bdd6d7a52093587c`, [#45276750153](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45276750153), miał status `completed/success`. To **nie** jest wynik CI rozdziału 15. Przed iteracją nie było pliku `tools/tests/test_functional_analysis_ch15.py`.

## Przegląd matematyczny: 12/12 dowodów

1. **Kryterium ciągłości odwzorowań wieloliniowych i zupełność:** skalowanie wszystkich niezerowych argumentów do kuli oraz punktowa granica ciągu Cauchy'ego w F; kontrola normy przez przejście do granicy.
2. **Izometria curryingu:** kolejność dwóch supremów i jawna konstrukcja odwrotności.
3. **Symetria drugiej pochodnej:** dwa porządki całkowania przyrostu mieszanego i przejście do granicy dzięki ciągłości normowej D²f.
4. **Symetria wyższych pochodnych:** indukcja i generowanie permutacji przez transpozycje sąsiednie.
5. **Druga pochodna złożenia:** różniczkowanie kompozycji operatorów jako ciągłego odwzorowania dwuliniowego.
6. **Taylor z resztą całkową:** różniczkowanie krzywej Banacha, iterowanie całek i oszacowanie przez ciągłość D^mf.
7. **Warunki ekstremum:** ograniczenie do prostych i jednostajna dodatniość drugiej pochodnej w małej kuli.
8. **Szereg Neumanna:** zbieżność w normie operatorowej i obustronna odwrotność.
9. **Otwartość GL(E) i gładkość odwracania:** faktoryzacja A+H, tożsamość rezolwentowa i reszta drugiego rzędu.
10. **Twierdzenie o funkcji odwrotnej:** kontrakcja na pełnej kuli, lokalna jednoznaczność, otwartość obrazu, Lipschitzowska odwrotność i różniczkowalność.
11. **Wyższa regularność odwrotności:** indukcja ze wzoru Dg=(Df∘g)^{-1}.
12. **Twierdzenie o funkcji uwikłanej:** trójkątny izomorfizm pochodnej (x,y)↦(x,F(x,y)), lokalne prostokąty, jednoznaczność i wzór na Dφ.

Nie znaleziono w tych argumentach jawnie fałszywego twierdzenia wymagającego korekty źródła. Przegląd nie jest formalną weryfikacją w Lean.

## Przykłady: 5/5

- Wielomian z odwzorowania m-liniowego: reszta co najmniej kwadratowa, dla symetrycznego B pochodna m-tego rzędu równa m!B.
- Hesjan kwadratowego funkcjonału Hilberta: występuje część samosprzężona (A+A*)/2.
- Ściśle dodatni, ale nie jednostajnie dodatni Hesjan na ℓ²: dla t=1/n zachodzi f(te_n)=1/(2n³)-1/n³<0; D²||x||³(0)=0.
- Mapa x↦x+||x||²v: pochodna w zerze to I; lokalna, nie globalna, odwracalność.
- Równanie (I−λK)u=g: pochodne u'(0)=Kg i u''(0)=2K²g oraz szereg Neumanna.

## Kontrola redakcyjna i techniczna

Sprawdzono jawne typy przestrzeni w twierdzeniach, założenia otwartości, regularności i odwracalności, kolejność argumentów D², przypadki graniczne i polską terminologię. Odczytane źródło zawiera 12 środowisk `proof`, 5 `przyklad` i odsyłacze do twierdzeń/lematów w rozdziale; nie stwierdzono brakującego celu w odczytanym rozdziale. Nie wykonywano pełnej kompilacji LaTeX ani wizualnego przeglądu PDF dla rozdziału 15.

Dodano nowy plik `tools/tests/test_functional_analysis_ch15.py` z **4 metodami testowymi**: dodatni Hesjan bez minimum, szereg Neumanna i oszacowanie reszty, pochodna mapy rzędu jeden oraz pierwsze dwie pochodne rozwiązania uwikłanego. Commit testu: `d99b36b89907f8f9d3185c78de9769b93dade718`. Są to rzeczywiste testy zapisane w repozytorium, **nie ma potwierdzenia ich uruchomienia**.

## Decyzja i dalsze bramki

**Rozdział 15: niestabilny, 0/2.** Nowe testy wymagają uruchomienia, należy dodać lub potwierdzić dedykowaną bramkę CI dla rozdziału 15, kompilację pełnego dokumentu i inspekcję PDF, a następnie wykonać niezależny audyt 15/02. Rozdział 16 pozostaje zablokowany. Nie przypisuje się statusu PASS przebiegom dotyczącym rozdziału 14.
