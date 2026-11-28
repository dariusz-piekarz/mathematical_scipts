# Topologia ogólna — rozdział 24, audyt 03 (drugi czysty)

**Data:** 2026-11-22. **Blob:** `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`.
**Wynik:** CZYSTY 2/2 na niezmienionym źródle,
po czystym audycie 02; bez zmian pliku rozdziału.

## Kontrola wszystkich 21 bloków dowodu

1. **Kryterium \(xy^{-1}\):** ciągłość mnożenia
   i odwracania implikuje ciągłość różnicy;
   odwrotnie różnica przy x=e daje odwracanie,
   a po odwróceniu drugiej zmiennej mnożenie.
2. **Translacje:** jawne wzory na odwrotności
   L_g, R_g, C_g oraz inwolucyjność odwracania.
3. **Jednorodność:** L_{yx^{-1}}(x)=y;
   wszystkie otoczenia x są przesunięciami otoczeń e.
4. **Małe otoczenia:** V=W1∩W2∩W1^{-1}∩W2^{-1}
   jest symetryczne, a V²⊂U;
   iteracja daje V^k⊂U również dla k=1.
5. **Domknięcie otoczenia:** xV∩V≠∅ dla
   x∈cl V, bo xV jest otwarte i zawiera x;
   stąd x∈VV^{-1}=V².
6. **Regularność:** otoczenie x zwęża się
   po lewej translacji na e, a homeomorfizmy
   przenoszą domknięcia.
7. **Homomorfizmy:** ciągłość w e
   daje ciągłość w każdej translacji punktu x.
8. **Domknięcie podgrupy:** \(\overline H\)
   jest podgrupą dzięki ciągłości (x,y)↦xy^{-1};
   sprzężenia zachowują domknięcie,
   jeśli H jest normalna.
9. **Podgrupa otwarta:** wszystkie warstwy
   lewe/prawe otwarte, więc dopełnienie H
   jest otwarte; H jest domknięta.
10. **Centrum i centralizator:** równości
   xa=ax są przeciwobrazami przekątnej
   w G×G, domkniętej dzięki T2.
11. **Otwarta projekcja q:** saturacja
   q^{-1}q(U)=UH, suma otwartych translacji U.
12. **Działanie G×G/H:** dobrze określone
   przez równość warstw, ciągłe przez
   otwartą surjekcję ilorazową id×q,
   przechodnie; stabilizator H to H.
13. **Hausdorffowość G/H:** jeśli H jest zamknięta,
   odrębne warstwy mają rozłączne otoczenia
   q(xV),q(yV); jeśli iloraz T2,
   przeciwobraz singletonu {H} jest zamknięty.
14. **Normalny iloraz:** mnożenie i odwrotność
   ciągłe przez q×q i q, oba odwzorowania
   ilorazowe; N zamknięta dokładnie przy
   hausdorffowym ilorazie.
15. **Izomorfizm topologiczny:** jądro
   zamknięte, wzór na \(\tilde f\)
   niezależny od reprezentanta,
   bijektywny i ciągły; otwartość f
   gwarantuje homeomorfizm.
16. **Zwartość/lokalna zwartość G/H:**
   ciągły obraz kompaktu, lokalnie
   obraz zwartego otoczenia e przez
   otwartą projekcję q i translacje.
17. **Składowa G^0:** ciągły obraz
   spójnego G^0×G^0 przez różnicę,
   sprzężenia i domknięcie;
   otwarta surjekcja o spójnych włóknach
   ma spójny przeciwobraz spójnego C,
   co dowodzi całkowitej niespójności G/G^0.
18. **Lewa/prawa struktura jednostajna:**
   przekątna, przecięcia, symetria
   oraz złożenie kontrolowane małym V;
   topologia jest oryginalna, bo
   otoczenia mają postać xU i U^{-1}x;
   homomorfizmy zachowują je jednostajnie.
19. **Grupy przemienne:** E_U^L=E_{U^{-1}}^R,
   nie założono podobnej równości
   bez przemienności G.
20. **Birkhoff–Kakutani:** potwierdzono
   dyadyczny lemat łańcuchowy przez
   rozbicie przy progu 2^{-(n+1)}
   na najwyżej trzy odcinki
   o sumach <progu i środkowej wadze <=progu.
   Dodatnia określoność metryki
   pochodzi z tego lematu, nie z samej rho;
   równości \((gx)^{-1}gy=x^{-1}y\)
   i \(U_{n+1}⊂B_d(e,2^{-n})⊂U_n\)
   dają niezmienniczość i właściwą topologię.
21. **Prawostronna metryka:** d_R(x,y)
   =d_L(x^{-1},y^{-1}) jest zgodna
   z topologią i prawostronnie niezmiennicza
   dzięki lewostronnej niezmienniczości d_L.

## Przypadki graniczne i rozróżnienia

- G zawsze niepusta i e istnieje z definicji grupy.
- W lemacie Birkhoffa wagę zero ma tylko e,
  a dodatnie wagi tworzą dyskretny zbiór dyadyczny;
  dlatego krok środkowy w indukcji jest poprawny.
- Dla H niedomkniętej iloraz G/H nie jest Hausdorffa;
  nie traktuje się go jako Hausdorffowej grupy
  tylko dlatego, że N jest normalna.
- H domknięta bez normalności wystarczy do
  Hausdorffowości G/H, ale nie daje grupy ilorazowej.
  Przykład S3 wykazuje ten punkt.
- Nieprzeliczalny produkt Z/2 z topologią produktową
  nie spełnia pierwszego aksjomatu przeliczalności;
  nie przeczy to metryzowalności dyskretnej
  nieprzeliczalnej grupy.
- Wprowadzono wyłącznie topologiczne
  konsekwencje lokalnej zwartości;
  miara Haara pozostaje w skrypcie o teorii miary.

## Zakończony CI i rzeczywisty PDF

[CI 45053429106](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45053429106)
zakończyło się **completed/success**.
Źródło rozdziału jest na tym samym blobie,
który zawierało to CI. Artefakt
`general-topology-ch01-ch24`, ID 14766264355,
pobrano i rzeczywiście otwarto.
Samodzielny PDF ma **10 stron A4**, pełna książka **175 stron**.
Wszystkie strony samodzielnego PDF wyrenderowano
i obejrzano na zestawieniu kontaktowym,
a stronę 6 z rysunkiem R/Z→S¹
oraz stronę 10 z końcowym podsumowaniem
sprawdzono także w większej rozdzielczości.
Brak nałożenia napisów na rysunek,
tekst i wzory mieszczą się na stronach,
ostatnia strona zawiera wniosek, przykład i podsumowanie,
a nie osierocony akapit.
W logu samodzielnego rozdziału brak
Overfull, Underfull, Missing character, LaTeX Warning,
Undefined control sequence i Fatal error.

Testy grup skończonych i regresja źródła
przeszły w CI po uzupełnieniu rozdziału.
Nie zmieniono źródła rozdziału w tym audycie.

**Status: CZYSTY 2/2, pozostaje nadmiarowa kontrola 3/2
tego samego bloba oraz finalne CI po oznaczeniu stabilności.**
