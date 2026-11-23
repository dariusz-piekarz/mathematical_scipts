# Topologia ogólna — globalny audyt 56: pełna kontrola 9 dowodów rozdziału 13 i naprawa odsyłacza

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex`.
**Blob pierwotny:** `c9078636452731e42a56196e84b5ed9831120e6b`.
**Blob po jedynej korekcie tekstowej:** `160a4cb67698525f0f5c08f56f3d8bb3cbfa0623`.

## Naprawiona, rzeczywista usterka redakcyjna

W przykładzie `ex:topog-uzupelnienia-arctan` zdanie o zgodności topologii metryk `d(x,y)=|x−y|` i `e(x,y)=|arctan x−arctan y|` błędnie odsyłało do **rozdziału 12**. Bezpośrednie uzasadnienie tej zgodności znajduje się w końcowej uwadze **rozdziału 10**; odsyłacz poprawiono z `(rozdział~12)` na `(rozdział~10)`. Poprawka: commit `175cda1e54c7b165cdd1beeace1e33611b1e0269`.

Dopisano statyczny test regresyjny do `tools/tests/test_general_topology_ch13.py`, który sprawdza referencję w konkretnym przykładzie. Commit testu: `6f5ba48bbe55bf9547cdf704cf389fd3a6840db0`. Należy potwierdzić wynik rzeczywistego CI na tej wersji gałęzi.

**Ścisły zakres diffu:** odczytano osobno stary i nowy blob rozdziału 13. Zamiana **jednego** wskazanego łańcucha znaków daje bitowo całą nową zawartość; wszystkie **9 tekstów środowisk proof** są bitowo identyczne, podobnie jak liczba i zawartość etykiet LaTeX (**24/24**). Korekta nie wymaga przeformułowania matematycznych dowodów, ale zgodnie z rytmem projektu wymaga potwierdzenia stabilności i CI zmienionego źródła.

## Indywidualny, niezależny audyt wszystkich 9 dowodów

| ID | Etykieta; początek dowodu | Zweryfikowany argument |
|---|---|---|
| 13-01 | `thm:topog-uzupelnienia-filtry-sieci`, 39 | Filtr ogonów sieci Cauchy'ego jest Cauchy'ego (rozdział 12), a jego zbieżność dokładnie znaczy eventualną przynależność ogonów do każdego otoczenia. Odwrotnie z filtra 𝔽 buduje się skierowany D={(A,a):A∈𝔽,a∈A}, porządkując przez odwrotną inkluzję pierwszych współrzędnych; późniejsze pary (A,b) dowodzą, że zbieżność sieci wymusza A⊂O, więc O∈𝔽. Brak potrzeby Hausdorffowości. |
| 13-02 | `prop:topog-uzupelnienia-metryczna`, 78 | Jednostajna zupełność gwarantuje zbieżność każdej metrycznej sieci Cauchy'ego, w szczególności ciągu. Odwrotnie z filtra Cauchy'ego wybiera się zstępujące A_n o średnicy <2^{-n} i x_n∈A_n. Metryczna zupełność daje x_n→x; przy 2^{-n}<ε/2 i d(x_n,x)<ε/2 mamy A_n⊂B(x,ε), więc filtr zbiega do x. Pusta przestrzeń jest zupełna w obu sensach. |
| 13-03 | `thm:topog-uzupelnienia-metryczne`, 133 | Relacja dwóch ciągów Cauchy'ego d(x_n,y_n)→0 jest równoważnością. Dla klas odległość \hat d=lim_n d(x_n,y_n) istnieje z odwrotnej nierówności trójkąta, jest niezależna od reprezentantów i rozdziela klasy. Klasy stałych ciągów zanurzają izometrycznie i gęsto X. Dla Cauchy'ego (z_k) w uzupełnieniu wybiera się przybliżenia ι(x_k) odległe <2^{-k}; ciąg (x_k) jest metrycznie Cauchy'ego w X, a jego klasa jest granicą z_k. Pusty X ma puste uzupełnienie. |
| 13-04 | `lem:topog-uzupelnienia-rownowaznosc`, 219 | Zwrotność relacji bliskości filtrów wynika z A×A⊂E dla filtra Cauchy'ego; symetria z odwracania relacji. Przechodniość: dla F~G~H i symetrycznego D o D²⊂E wybiera się B,B'∈G i b∈B∩B'; z A×B⊂D, B'×C⊂D wynika A×C⊂D²⊂E. Prawidłowo wykorzystano właściwość filtra do niepustości przecięcia. |
| 13-05 | `lem:topog-uzupelnienia-minimalizacja`, 258 | Zbiory E[A] tworzą bazę filtra, bo (E∩D)[A∩B]⊂E[A]∩D[B] i są niepuste. Z A⊂E[A] wynika 𝔽°⊂𝔽. Dla D³⊂V i A×A⊂D otrzymujemy D[A]×D[A]⊂V, więc 𝔽° jest Cauchy'ego. D[A]×A⊂D² dowodzi bliskości. Dla dowolnego bliskiego 𝔾, a∈A∩A' implikuje B⊂D[a]⊂E[A] i E[A]∈𝔾: zatem 𝔽° jest zawarty w każdym filtrze bliskim 𝔽, co daje minimalność i jedyność. |
| 13-06 | `thm:topog-uzupelnienia-istnienie`, 329 | Relacje Ê między minimalnymi filtrami mają przekątną, odwrotności, przecięcia i składanie: z A×B⊂D oraz B'×C⊂D, wybór b∈B∩B' daje A×C⊂D². Rozdzielanie wynika z jedyności minimalnych filtrów bliskich. Filtry otoczeń 𝒩_x są minimalne Cauchy'ego dzięki D²[x]⊂A, a ι(x)=𝒩_x jest zanurzeniem jednostajnym dzięki dwóm kierunkom porównania Ê i E. Gęstość: z A×A⊂D dla x∈A uzyskujemy A×D[x]⊂D²⊂E, czyli (𝔽,ι(x))∈Ê. Zupełność: rodzina B(H,E) jest właściwą bazą filtra 𝔾 na X; warunek H×H⊂D̂ i orientacja (ι(x),𝔽)∈D̂ dają B(H,D)×B(H,D)⊂D³. Minimalny filtr 𝔽₀=𝔾° jest granicą 𝓗: dla dowolnego E dobiera się symetryczne D o D⁴⊂E oraz H, co wymusza H⊂Ê[𝔽₀]. Cztery kroki relacji i ich kierunki zweryfikowano niezależnie. |
| 13-07 | `lem:topog-uzupelnienia-rozszerzenie`, 585 | Dla z∈Z gęstość A zapewnia, że zbiory A∩E[z] są niepuste i tworzą Cauchy'ego filtr 𝔽_z; obraz przez jednostajnie ciągłą f jest Cauchy'ego, więc ma w zupełnym Y granicę, jednoznaczną z rozdzielania. Dla bliskich z,z' wybiera się E³⊂D zapewniające, że wszystkie pary (f(a),f(b)) z filtrów przy z,z' leżą w W. Ich granica leży w domknięciu W. Wybór symetrycznego W o W³⊂V daje cl_{Y×Y}W⊂W³⊂V: otwarte otoczenia wewnątrz przekrojów W[y], W[y'] wraz z symetrią zapewniają trzy ogniwa. Jednostajna ciągłość i jedyność rozszerzenia z gęstości są poprawne. |
| 13-08 | `thm:topog-uzupelnienia-uniwersalnosc`, 658 | Utożsamienie X z gęstym obrazem ι(X) w zupełnym X̂ i zastosowanie lematu o rozszerzaniu do f∘ι^{-1} daje jednoznaczną mapę f̂. Dwa uzupełnienia dają T i S zgodne z zanurzeniami; ich złożenia są identycznościami na gęstych obrazach, a przez Hausdorffowość na całych przestrzeniach. T i S są więc jednostajnymi izomorfizmami. |
| 13-09 | `thm:topog-uzupelnienia-podprzestrzenie`, 689 | Filtr Cauchy'ego na domkniętym A podniesiony do X nadal jest Cauchy'ego, więc ma granicę x∈X; jej każde otoczenie przecina A, a domkniętość daje x∈A. Odwrotnie dla x∈cl_X A filtr na A generowany przez A∩E[x] jest Cauchy'ego, ma granicę a∈A, a jako filtr na X zbiega również do x. Rozdzielanie X zapewnia a=x. Pusta A jest zgodna z twierdzeniem. |

## Ryzyka logiczne i matematyczne

- Rozdzielono **zbieżność filtrów** i zbieżność sieci; w kierunku filtr→sieć z konstrukcji D={(A,a)} konieczne jest, że każdy b∈A może wystąpić jako późniejszy indeks. Ujęto to bez uproszczenia do ciągów.
- W konstrukcji uzupełnienia przez minimalne filtry istotna jest **orientacja** relacji `(ι(x),𝔽)` i `(𝔽,ι(x))`. W dowodzie przejścia do filtrów B(H,E) wykonuje się odwrócenie dopiero po wybraniu symetrycznego D; bez tego kroku niepustość bazy nie byłaby uzasadniona.
- Dla pokazania zupełności 𝑋̂ nie wystarcza zwykła gęstość obrazu ι(X). Skontrolowano konstrukcję filtra 𝔾, oszacowanie relacji przez D³, przeniesienie do minimalnego 𝔽₀ oraz ostateczne złożenie D⁴⊂E dla każdego elementu filtra 𝓗.
- W lemacie o rozszerzeniu przejście do granic par należy wykonać w topologii produktu Y×Y, zatem uzyskuje się najpierw **domknięcie** relacji W, nie samą W. Osobno skontrolowano `cl W⊂W³⊂V`, co naprawia potencjalną lukę w uproszczonym rozumowaniu.
- Przestrzeń pusta, niejednoznaczność granic bez rozdzielania, kompletność wybranej metryki versus całkowita metryzowalność i gęstość podprzestrzeni były sprawdzane przy odpowiednich hipotezach.

## Werdykt i bilans

**Matematyka: 9/9 PASS.** Każdy aktualny dowód ma osobny numer i etykietę z globalnej macierzy 34. **Redakcja: 1 poprawiony odsyłacz; 1 dodany test regresyjny.** Nie znaleziono nowych błędów matematycznych w konstrukcji uzupełnienia. Wersja rozdziału 13 ma teraz nowy blob; wcześniejsze lokalne 2+1 dotyczyły starego bloba i wymagają ponownego potwierdzenia bieżącej korekty wydawniczej.

Poprzedni bilans pełnej dokumentacji wynosił 272/325; po tym audycie wynosi **281/325**, a pozostało **44 dowody w rozdziałach 24–26**. Jednak bez zamknięcia stabilizacji obecnego bloba 13 i zielonego CI nie należy uznawać całego tomu za ostatecznie ustabilizowany. Następna praca: 2 czyste niezależne audyty 13, 1 potwierdzający + sprawdzenie CI, dopiero potem pełne indywidualne dokumentowanie 24–26.
