# Topologia ogólna — rozdział 15: audyt iteracja 03 (twierdzenie Stone'a)

Data: 2026-11-22; gałąź: `biblioteka-matematyczna-iteracja-6`.

## Rozbudowa źródła

Zamiast końcowej uwagi o nieudowodnionym twierdzeniu Stone'a dodano pełne twierdzenie i konstrukcyjny dowód parazwartości dowolnej przestrzeni metrycznej, bez założeń ośrodkowości, zupełności i zwartości lokalnej.

Rozdział: `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex`.
Etykieta: `thm:topog-parazwartosc-stone`.
Metoda: konstrukcja Mary Ellen Rudin (1969), porządkowanie elementów pokrycia i rekurencja po skalach metrycznych.

## Niezależna kontrola łańcucha rozumowania

1. Uporządkowanie `U_α` i najmniejszy indeks `α(x)` istnieją z twierdzenia o dobrym uporządkowaniu. Zapisana konwencja `r_n=2^{-n}`, `n≥1`, a dla poziomu pierwszego zbiór wcześniej utworzonych poziomów jest pusty.
2. Dopuszczalne środki `E_{α,n}` muszą: należeć do pierwszego zbioru pokrycia obejmującego punkt, pozostawać poza wcześniejszymi poziomami, spełniać `B(z,3r_n)⊂U_α`. Wtedy `V_{α,n}=∪_{z∈E_{α,n}} B(z,r_n)` jest otwarty i zawiera się w `U_α`.
3. Pokrywanie: dla punktu `x`, który wcześniej nie został pokryty, wybór dostatecznie dużego `n` z `B(x,3r_n)⊂U_{α(x)}` czyni `x` dopuszczalnym środkiem; wtedy `x∈V_{α(x),n}`.
4. Rozdzielenie w warstwie `i`: środki `y∈E_{β,i}`, `z∈E_{γ,i}`, `β<γ`, spełniają `z∉U_β` i `B(y,3r_i)⊂U_β`, więc `d(y,z)≥3r_i`. Dla punktów odpowiednich kul `p,q` zachodzi `d(p,q)>r_i`. Kula o średnicy nie większej od `r_i` może zatem przeciąć najwyżej jeden zbiór z poziomu `i`.
5. Dla `x∈V_{α,n}` wybór `B(x,ρ)⊂V_{α,n}` i `M>n` z `2r_M<ρ` zapewnia, że środki wszystkich poziomów `i≥M` leżą w odległości co najmniej `ρ` od `x`. Ich kule promienia `r_i≤r_M` nie przecinają `B(x,r_M)`.
6. Dla skończenie wielu poziomów `i<M` kula `B(x,r_M)` ma średnicę co najwyżej `2r_M≤r_i`, więc z każdego poziomu przecina co najwyżej jeden zbiór. Otrzymujemy co najwyżej `M-1` zbiorów ogółem, co kończy dowód lokalnej skończoności.
7. Przypadek `X=∅` rozstrzygnięty osobno; pokrycie dowolne, bez niejawnych założeń przeliczalności lub zwartości.
8. Poprzednie konstrukcje podziałów jedności i ich dowody pozostają bez zmian.

## Testy i integracja

Do `tools/tests/test_general_topology_ch15.py` dodano kontrolę etykiety i składników dowodu, a także enumerację wszystkich pokryć otwartych małych (do 4 punktów) dyskretnych przestrzeni metrycznych. Test sprawdza pokrywanie i rozdzielenie poziomów w konstrukcji Rudin. Test skończony jest weryfikacją pomocniczą, nie substytutem dowodu ogólnego.

Zmiany źródła: commit `2ca75736f10488a401b87516a0997ebe9a093389`.
Zmiany testu: commit `a564129a3f95f6353a5cb439a1d1e6dd23aeb4df`.
Workflow dla wersji z nowym testem:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010139633

## Wynik audytu 03

| Warstwa | Wynik |
| --- | --- |
| Dowód twierdzenia Stone'a — konstrukcja i kwantyfikatory | PASS — kontrola matematyczna |
| Lokalna skończoność (oba oszacowania) | PASS — kontrola matematyczna |
| Wcześniejsza konstrukcja podziału jedności | Bez zmian |
| Testy automatyczne i pełna kompilacja | Weryfikacja workflow |
| Kontrola PDF i logów | Do potwierdzenia artefaktem nowego workflow |
| Stabilizacja rozdziału | OTWARTA: nowy dowód wymaga niezależnego ponownego audytu po walidacji CI |

Źródło metody: M. E. Rudin, *A New Proof that Metric Spaces are Paracompact*, Proceedings of the AMS 20 (1969), 603; niezależnie porównano główne oszacowania z omówieniem https://matthewhr.wordpress.com/2014/06/18/metric-spaces-are-paracompact-m-e-rudins-elementary-proof/ .

## Weryfikacja po wpisaniu dowodu

Workflow `45010139633` dla kompletnego dowodu i rozszerzonego testu zakończył się `completed/success`. Pobrano artefakt `14749202693`, zawierający samodzielny PDF rozdziału 15 (4 strony A4) i log. Kontrola logu nie wykazała `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` ani `Fatal error`. Wykonano oględziny stron 3–4: wzory i dowód są czytelne.

Dostrzeżono drobną usterkę redakcyjną: na granicy stron 3–4 sformułowanie tezy twierdzenia zostało rozdzielone. Skrócono nagłówek sekcji do „Twierdzenie Stone'a”, a tezę do równoważnego „Niech $(X,d)$ będzie przestrzenią metryczną. Wówczas $X$ jest parazwarta.” Dowód szczegółowy pozostaje bez zmian. Korekta w commicie `bcd83a8e9fdae6d46e5befe07bfa9acfafb4d15f` wymaga finalnej kontroli składu na tym commicie.
