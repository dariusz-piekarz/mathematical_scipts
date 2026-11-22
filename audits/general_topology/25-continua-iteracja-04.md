# Topologia ogólna — rozdział 25, audyt 04 (nadmiarowy, czysty)

**Data:** 2026-11-22.
**Blob 02–04:** `7b772123870296af95d3ce951ccddb65685af7aa`.
**Wynik:** CZYSTY 3/2 (dwa wymagane audyty i jeden potwierdzający);
nie zmieniono źródła rozdziału 25.

## Próba obalenia konstrukcji i twierdzeń

1. **Continuum nierozkładalne Knastera.**
   Jeśli C⊊K_T jest podcontinuum o niepustym wnętrzu,
   weźmy cylinder p_k^-1(U) zawarty w C.
   Na każdym poziomie m≥k+2
   p_m(C) jest przedziałem zawierającym
   preobrazy U z pierwszej i ostatniej
   gałęzi T^{m-k}; w konsekwencji zawiera
   [1/4,3/4]. Dla dowolnego j, wybierając
   m≥max(k,j)+2, otrzymujemy
   p_j(C)⊃T^{m-j}([1/4,3/4])=[0,1].
   Jeśli j<k, mamy także pełne projekcje
   przez surjektywność T^{k-j}.
   Każdy cylinder podstawowy spotyka C,
   więc C jest gęsty, a jako kompakt
   w Hausdorffowym K_T jest domknięty.
   Zatem C=K_T, sprzeczność.
   Ten argument dowodzi silniejszej tezy
   o pustym wnętrzu właściwych podcontinuów,
   z której wynika nierozkładalność.
2. **Zwartość i spójność granicy odwrotnej.**
   Surjektywność projekcji jest potrzebna
   do wykazania, że p_n(A)∪p_n(B)=X_n,
   a nie tylko podzbiór X_n.
   Sprawdzenie tej przesłanki w głównym
   twierdzeniu wypada poprawnie.
   Domkniętość warunku f_n(x_{n+1})=x_n
   używa Hausdorffowości X_n.
3. **Solenoid.** Lokalny produkt
   łuku J i Cantora nie przeczy globalnej
   spójności solenoidu: projekcja
   na Cantor rozdziela spójne podzbiory
   otwartego cylindra, nie całą przestrzeń.
   Brak otwartych jednoelementowych
   zbiorów w nieskończonym produkcie
   \{0,1\}^N wyklucza lokalną spójność
   w każdym punkcie solenoidu.
4. **Krzywa Peana.** Przeplatanie cyfr
   w n rozwinięciach binarnych daje
   surjekcję *z Cantora*, ale
   nie z całego przedziału.
   Drugi, niezbędny krok to
   przedłużenia współrzędnych Tietzego
   do [0,1] z zachowaniem wartości
   w [0,1]. Otrzymane odwzorowanie
   na przedziale zawiera obraz C
   równy [0,1]^n. Uniknięto
   nieuzasadnionej tezy, że ciągły
   obraz Cantora jest zawsze
   lokalnie spójny.
5. **Minimalność między punktami.**
   Zorn na rodzinie podcontinuów
   nie wystarcza bez lematu
   o przecięciu łańcucha;
   ten lemat jest obecny i
   udowodniony bez założenia
   metryzowalności X.
6. **Grafy.** Konstrukcja
   spacerów odwiedzających każdą
   krawędź nie zakłada
   eulerowskości ani braku cykli.
   W jednoelementowym grafie
   odwzorowanie stałe
   daje poprawny przypadek skrajny.
7. **Granice twierdzenia Hahna–Mazurkiewicza.**
   Stwierdzenie w uwadze jest
   jawnie oznaczone jako klasyczny
   wynik wymagający dalszego
   szczegółowego opracowania;
   nie jest utożsamiane z
   osobnymi twierdzeniami
   o grafach i sześcianach.
   Dalszy pełny dowód ogólny
   pozostaje tematem dodatkowym,
   a nie niezrealizowanym
   krokiem któregoś z
   14 aktualnych dowodów.

## Redakcja, LaTeX, obrazy i regresje

Najnowszy blob źródła zawiera
35 różnych etykiet i 15 odsyłaczy,
w tym pięć do istniejących twierdzeń
w rozdziałach 05, 08 i 23.
Środowiska twierdzeń, definicji,
przykładów, 14 dowodów i
jednego rysunku mają poprawne
pary begin/end.
Przestrzegano zakazu terminów
„unia”, „zwartościowanie”
i „sekwencyjny”.
Rysunek namiotu ma opis
umieszczony na prawo od
linii wykresu, bez kolizji.

Końcowe źródło powstało przed
[CI 45056802863](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45056802863),
które zakończyło się sukcesem.
Artefakt `general-topology-ch01-ch25`
ID 14767733188 został pobrany i
wypakowany. Zweryfikowano
osobny PDF o 8 stronach A4
i pełną książkę o 183 stronach.
Wyrenderowano wszystkie osiem stron
rozdziału i obejrzano zestawienie,
a strony 6 i 8 również w wysokiej
rozdzielczości; brak nałożeń,
brak osieroconej strony.
W obu logach brak
Overfull/Underfull, Missing character,
LaTeX Warning, Undefined control
sequence oraz Fatal error.

**Wniosek:** 2/2+1 czyste audyty
na tym samym blobie zakończone.
Rozdział 25 może zostać oznaczony
jako stabilny, pod warunkiem
końcowej zielonej walidacji
po zaktualizowaniu tytułu książki,
README, planu i regresji wersji.
