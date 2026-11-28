# Logika matematyczna i teoria mnogości — rozdział 31, audyt III

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex`.

## Wybór bez AC w lemacie o odbiciu

W Lemacie `lem:l-finite-reflection` dawny zapis „wybieramy `α_0` i kolejno `α_{n+1}`” nie wyjaśniał, że wybory można wykonać jednoznacznie w ZF. Uzupełniono konstrukcję:

- dla ustalonej skończonej rodziny podformuł egzystencjalnych `Φ` i zbioru parametrów `L_α` istnieje zbiór kodów i krotek `E_α` z prawdziwymi w `L` formułami egzystencjalnymi (separacja);
- dla każdej pary wybiera się nie świadka, lecz **najmniejszy ordynał** `β_{e,p}`, na którego poziomie pojawia się świadek; ich rodzina jest zbiorem przez zastępowanie;
- ustalono jednoznaczne przejście `F(α)=sup({α+1}∪{β_{e,p}+1:(e,p)∈E_α})` i rekursję `α_0=η+1`, `α_{n+1}=F(α_n)`;
- graniczny `θ=sup_n α_n` odbija ustaloną rodzinę formuł; żaden krok nie wymaga wyboru niezależnych świadków ani DC.

Sprawdzono niezależnie, że późniejsze użycia refleksji w dowodach aksjomatów ZF i elementarności poziomów nie potrzebują globalnego predykatu prawdy dla `L`, lecz korzystają z **relatywizacji ustalonej, skończonej rodziny formuł**. Utrzymano wszystkie ograniczenia formalnego kodowania relacji spełniania dla zbiorowych struktur.

**Stan:** bez nowych lematów i twierdzeń, 68 etykiet, 87 odsyłaczy. Wersja przechodzi testy regresyjne; wymaga ostatecznej kompilacji i niezależnego audytu kondensacji/GCH.
