# Topologia ogólna — rozdział 19, audyt iteracja 02

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Plik źródłowy: `chapters/pl/general_topology/19-przestrzenie-polskie-i-zbiory-borelowskie.tex`.

## Niezależna ponowna kontrola

Sprawdzono ponownie całą aktualną treść matematyczną rozdziału 19: definicje przestrzeni polskich, przykłady, iloczyny, charakteryzację podprzestrzeni typu `G_\delta`, σ-algebra borelowska, generatory i odwzorowania borelowskie, hierarchię skończoną oraz pozaskończoną. W tej iteracji nie dodano nowych twierdzeń ani definicji; skupiono się na istniejących dowodach, kontrprzykładach, kwantyfikatorach i LaTeX.

1. **Polskość, ośrodkowość, drugi aksjomat przeliczalności.** Istnienie zgodnej zupełnej metryki nie oznacza zupełności każdej metryki zgodnej. Baza kul o środkach w przeliczalnym gęstym zbiorze i dodatnich promieniach wymiernych jest rzeczywiście bazą, ponieważ środek można wybrać bliżej niż ε/2. Metryka logitowa na (0,1) pochodzi z homeomorfizmu na R, więc jest zupełna i zgodna.
2. **Przestrzenie Cantora i Baire'a.** Ultrametryka 2^{-k} przy pierwszej różnej współrzędnej wyznacza topologię produktową; nierówność ultrametryczna wynika z nierówności dla pierwszych indeksów różnic. Dla ciągu Cauchy'ego pierwszych n współrzędnych dostatecznie późnych wyrazów są ostatecznie równe, więc istnieje jednoznaczna granica współrzędna, a odległość do niej jest najwyżej 2^{-(n+1)}. W audycie 02 doprecyzowano ten krok. Zbiór ciągów o ostatecznie ustalonym ogonie jest przeliczalny i gęsty. Przestrzeń Cantora jest zwarta; przestrzeń Baire'a nie jest zwarta, co potwierdza rzutowanie na nieskończoną dyskretną N.
3. **Przeliczalny iloczyn przestrzeni polskich.** Ważona suma obciętych metryk daje metrykę zgodną z topologią produktową; kontrola finitarnych współrzędnych i ogona szeregu wyprowadza zgodność topologii i zupełność. Ośrodkowość wynika ze zbioru funkcji o skończenie wielu współrzędnych różnych od ustalonego punktu bazowego. Przypadek pustego czynnika jest wyodrębniony.
4. **Zbiory F_sigma i G_delta.** Lemat o zapisie otwartego U jako przeliczalnej sumy domkniętych poziomic funkcji d(x,X\U) prawidłowo rozpatruje także przypadek U=X. Dualna własność domkniętych G_delta wynika z dopełniania.
5. **Kierunek G_delta ⇒ przestrzeń polska.** Dla A=∩U_n i zupełnej metryki d na X zdefiniowano h_n(x)=1/d(x,X\U_n), przy U_n=X ustalając h_n=0. Sumaryczna metryka ρ=d+Σ2^{-n}min(1,|h_n(x)−h_n(y)|) wyznacza topologię A i jest zupełna. W audycie 02 jawnie oznaczono ciąg x_j→x w d, kontrolowano skończenie wiele składników oraz ogon szeregu i wykazano, że każdy h_n(x_j) jest ciągiem Cauchy'ego przez wspólny próg j_0 i nierówność ρ(x_j,x_k)<2^{-n}ε. Jeśli x leżałby poza U_n, odpowiednie h_n(x_j) dążyłoby do ∞, co jest sprzeczne z Cauchy'owskością. Po stwierdzeniu x∈A rozpisano oszacowanie ρ(x_j,x)<ε w trzech częściach (składnik d, skończony początek szeregu, ogon). Ośrodkowość A wynika z dziedziczenia drugiego aksjomatu przeliczalności przez podprzestrzeń i wyboru punktów z niepustych elementów przeliczalnej bazy.
6. **Kierunek przestrzeń polska ⇒ G_delta.** Istnieją promienie r_n(a)<2^{-n} kontrolujące średnicę w zgodnej zupełnej metryce σ na A zbiorów B_d(a,2r_n(a))∩A. Jeśli x∈∩V_n, wybieramy a_n∈A blisko x. Wybór δ_n=r_n(a_n)−d(x,a_n)>0 pozwala wykazać, że wszystkie dostatecznie późne a_m leżą w jednym B_d(a_n,2r_n(a_n))∩A. W audycie 02 jawnie ustalono ε>0, n z 2^{-n}<ε i m_0, a następnie oszacowano σ(a_m,a_l)<2^{-n}<ε dla **dowolnych** m,l≥m_0. Stąd a_m jest ciągiem Cauchy'ego w σ, a jedyność granic w X kończy dowód równości A=∩V_n.
7. **Wymierne i niewymierne.** Q jest F_sigma (przeliczalne singletony domknięte), ale nie jest G_delta przez niezgodność z twierdzeniem Baire'a dla polskich przestrzeni. Dopełnienie Q jest G_delta i polskie, lecz nie F_sigma.
8. **Sigma-algebra borelowska, ślad, generatory.** W obie strony sprawdzono równość B(A)={A∩B:B∈B(X)} bez dodatkowych wymagań oddzielania. Przy przeliczalnej bazie B(X)=σ(baza), ponieważ każdy otwarty jest przeliczalną sumą jej elementów. W R wystarczą przedziały o wymiernych końcach. Odwzorowanie jest borelowskie dokładnie wtedy, gdy przeciwobrazy otwartych są borelowskie; działa to dla ciągłości i składania.
9. **Hierarchia skończona.** Dualność Σ^0_n i Π^0_n jest konsekwencją praw de Morgana. Domknięcie odpowiednich klas na przeliczalne sumy/przecięcia wynika z indeksowania N². Założenie metryzowalności w tezie zapewnia otwarte F_sigma oraz domknięte G_delta i rosnący charakter poziomów, pozwalający uzgodnić definicje skończone i pozaskończone.
10. **Hierarchia indeksowana ordinalnie.** Dla α>1 klasy Σ^0_α tworzą sumy przeliczalne zbiorów Π^0_{β_n}, β_n<α. Ich dopełnienia są klasami Π^0_α. Każdy poziom leży w B(X) przez indukcję pozaskończoną. Rodzina C=⋃_{α<ω1}Σ^0_α zawiera otwarte i jest zamknięta na dopełnienia, gdyż Π^0_α⊂Σ^0_{α+1}; jeśli A_n∈Σ^0_{α_n}, to A_n∈Π^0_{α_n+1}, a suma A_n∈Σ^0_γ dla przeliczalnego γ=sup_n(α_n+2) większego od wszystkich α_n+1. W konsekwencji C jest σ-algebrą i równa B(X). Równość z sumą poziomów Π zachodzi przez dopełnienia.
11. **Zakres twierdzeń.** Dla podprzestrzeni polskich twierdzenie G_delta wymaga X polskiej, a przy funkcjach h_n używa dowolnej *wybranej* zupełnej zgodnej metryki d. Twierdzenie o hierarchii ograniczono do X metryzowalnej, aby bez dodatkowych warunków zgodne były definicje poziomów skończonych i ordinalnych. Nie utożsamiono wszystkich zbiorów borelowskich jedynie z poziomami skończonymi.
12. **Przykłady i terminologia.** Nie wykryto nowych błędów treści; nie ma nieprawidłowych terminów „zwartościowanie”, „zbieżność zwarta”, „pierwszoprzeliczalny”. Słowa „ciąg” i „sieć” zachowują rozróżnienie, a twierdzenia mają jawne założenia.

## Zmiany iteracji 02

- Doprecyzowano konstrukcję granicy współrzędnej w przestrzeni Cantora/Baire'a.
- Rozpisano zgodność metryki ρ z topologią A w dowodzie G_delta ⇒ polska.
- Uzupełniono oba etapy argumentu o zupełności metryki ρ, w tym kwantyfikatory i kontrolę szeregu.
- W kierunku polska ⇒ G_delta jawnie wykonano przejście od oszacowania średnicy do warunku Cauchy'ego z dwoma niezależnymi indeksami m,l.
- Dodano testy regresyjne ochrony nowych fragmentów dowodów oraz przykład numeryczny x_n=1/n, x_{2n}=1/(2n), który pokazuje, że składnik odwrotności odległości od brzegu wyklucza Cauchy'owskość w metryce ρ przy zbliżaniu się do brzegu (100 przypadków).
- Testy źródłowe wychwyciły brakujący delimiter matematyczny $ w nowym fragmencie; poprawiono zapis w TeX przed zamknięciem audytu. Nie był to błąd twierdzenia, lecz błąd składu.

Commity:
- 3892b34bab6c1bea2e1c8fe0afee14cb91bde709 — rozpisanie dowodów.
- b977812df24cd4aaa2b754d67c5ee2b4ca456412 — jawne określenie ciągu w argumencie topologicznym.
- e46d7c8463b1c5e19e1e4806015a121923158792 — rozszerzenie testów.
- c1faeeef025a37508fce111579b35d9fbd9e4bb8 — poprawka reguł dopasowania testu.
- 40c27a6df3a540c1e5159a195810e93bcdd83914 — naprawa delimitera matematycznego.

## CI i PDF

Wersja sprzed audytu 02 przeszła GitHub Actions 45018362870 i wizualny audyt PDF (6 stron). Dla poprawionego źródła uruchomiono odrębny workflow [45019373792](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45019373792) dla commita 40c27a6df3a540c1e5159a195810e93bcdd83914: **completed/success**, bez nieudanych kroków. Zakończyły się sukcesem test rozdziału 19, kompilacja całej książki, kompilacja samodzielnego rozdziału 19 i kontrola logów.

Pobrano artefakt 14753047959 i rozpakowano do /mnt/data/topologia19_audyt02. Samodzielny general_topology_ch19.pdf ma **6 stron A4**. Wyrenderowano i obejrzano wszystkie strony, szczególnie strony 3–4, na których znajdują się dopracowane dowody o metryce ρ i o polskich podprzestrzeniach G_delta. Nie wykryto kolizji tekstu, uciętych wyrażeń ani usterek czcionek i numeracji. Logi general_topology_ch19.log i general_topology.log nie zawierają \`Overfull\`, \`Underfull\`, \`LaTeX Warning\`, \`Missing character\`, \`Undefined control sequence\` ani \`Fatal error\`.

## Wynik

| Element | Status |
| --- | --- |
| Pełny audyt matematyczny | PASS po doprecyzowaniu dowodów |
| Twierdzenie o G_delta (oba kierunki) | PASS po uzupełnieniach |
| Zbiory borelowskie i hierarchia ordinalna | PASS |
| Przypadki brzegowe, terminologia i odsyłacze | PASS |
| Nowy CI i samodzielny PDF | **PASS — workflow 45019373792; 6 stron A4** |
| Stabilizacja | **W AUDYCIE — iteracja 03 wymagana po poprawkach** |

Nie przenosić pozytywnego statusu technicznego z audytu 01 bez sprawdzenia najnowszego kodu. Następną iterację przeprowadzić jako niezależny przegląd bez dodawania nowego materiału.
