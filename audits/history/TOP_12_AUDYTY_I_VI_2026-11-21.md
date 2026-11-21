# Topologia algebraiczna — TOP-12, audyty I–VI

**Data:** 2026-11-21  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/algebraic_topology/12-ciagi-spektralne-od-filtracji-do-fibracji-serre-a.tex`  
**Źródło po audytach:** blob `54f91a147bc678c60df8daf4a94a692ceb67acad` (1145 wierszy).  
**Zakres:** korekta istniejącego rozdziału, bez dodawania twierdzeń, lematów i nowych sekcji.

## Audyt I — poprawność języka i twierdzeń

- Skorygowano gramatykę w tytule sekcji i opisie krótkiego ciągu dokładnego.
- Poprawiono nieprawdziwe uproszczenie, że długi ciąg homotopii „nie wykrywa torsji”: grupy homotopii mogą mieć torsję; sam ciąg nie wyznacza na ogół grup homologii i pierścienia kohomologii przestrzeni całkowitej.
- Dodano regresje arytmetyczne dla modeli pierwszej niezerowej różniczki `d^r` dla `2 ≤ r ≤ 8`, z brzegiem mnożącym przez `±1, ±2, ±3, ±5`, oraz monodromii `-1` butelki Kleina.

**Commity:** `19ed3f51c6404f1719ad2368a925e4795ed227df`, `9fb7395a8b0ada44a7e39835e0b088246ca129ac`.

## Audyt II — dowód zbieżności, indeksacja dokładnej pary

- Doprecyzowano przeciwobraz podgrupy `F_{p-1}H_n(C)` wśród cykli filtrowanych: jeżeli `z=y+∂w` jest cyklem, to `y` także jest cyklem; w ten sposób wykazano równość mianownika stabilnego z jądrem przejścia do ilorazu.
- Jawnie podano bistopnie i indeksy map `i:D^1_{p-1,q+1}→D^1_{p,q}`, `j:D^1_{p,q}→E^1_{p,q}`, `k:E^1_{p,q}→D^1_{p-1,q}`.
- W dowodzie izomorfizmu Thoma usunięto nieuprawnione wnioskowanie, że zgodność dwóch map na jednostce w stopniu zero implikuje ich identyczność we wszystkich stopniach; isomorfizm mapy iloczynu kubkowego jest wykazywany oddzielnie na ilorazach filtracji.

**Commit:** `b5e118beddf87a673376e5ef150bc1034bb944be`.

## Audyt III — pełniejszy dowód kohomologicznego ciągu Serre'a

- Zdefiniowano malejącą filtrację kołańcuchów `F^p C^n(E)=ker(C^n(E)→C^n(E_{p-1}))`.
- Wykazano `F^pC^*/F^{p+1}C^* ≅ C^*(E_p,E_{p-1})`; wyjaśniono przedłużanie kołańcuchów przez zero.
- Zidentyfikowano `E_1^{p,q}=H^{p+q}(E_p,E_{p-1})` i `E_2^{p,q}=H^p(B;𝓗^q(F))`, podkreślając iloczyn grup kołańcuchowych przy nieskończenie wielu komórkach.
- Wyjaśniono przypadek komórki 0-wymiarowej przez konwencję `D^0={*}`, `S^{-1}=∅`.

**Commit:** `c0d84c256002c32675d441f0851cb6ec15787e7d`. Dodano regresje indeksacji i filtracji w `416128e74f204d87074a13fa6fc932fd8ef49f71` i poprawiono zapis surowy komendy TeX w teście w `5125e20886a00847fdd80ed8b38b22188b0d6f80`.

## Audyty IV–V — przykłady i lokalne współczynniki

- Butelkę Kleina określono jako torus odwzorowania odbicia okręgu, a nie samo odwzorowanie (commit `13d9bada0a244daca96e8ceaf3557e70ff388d3d`).
- W definicji transgresji wyraźnie założono `q≥1`; przy `q=0` strona `q+1=1` poprzedzałaby `E_2` i definicja nie miałaby sensu. Commit `15631b77011389af0b83ec7806ceda05cc22c5c1`.
- Dopisano definicję systemu kohomologicznego `𝓗^q(F)`: transport wzdłuż drogi `γ` to pullback przez transport włókien wzdłuż drogi odwrotnej `γ̄`. Jest to konsekwencja kontrawariantności kohomologii. Commit `52d9de3077361591badae9c418d02ce0ae877beb`.
- Dodano regresje transgresji i kierunku transportu, commity `bdeeb868cd7b79ba64eba7da2687b296b2f38ce0`, `73077606b319c211116fce02adaa73e48953cfa2`.

## Audyt VI — niezależny przegląd źródła

Bezpośrednio z GitHub odczytano najnowszy rozdział i testy. Zbadano:
- 15 etykiet: wszystkie unikalne.
- Liczność i zagnieżdżenie środowisk `begin/end`: brak niezgodności.
- Ochrona wzorów `d^3`, `E_1`, `F^p`, trzech strzałek dokładnej pary, konwencji `S^{-1}` i transgresji.
- Brak starych błędów językowych i zabronionych terminów.
- Istnienie pięciu nowych rodzin testów regresyjnych oraz zachowanie wcześniejszych historycznych etykiet.
- Matematycznie porównano argumenty twierdzeń z konstrukcją filtracyjną, obliczeniami Hopfa, butelki Kleina, klasy Thoma i Gysina; nie znaleziono kolejnych błędów wymagających patchowania.

**Decyzja matematyczna:** audyt VI czysty, brak nowych poprawek źródła. **Status końcowy** zależy od zielonych workflowów GitHub Actions dla ostatniego commita źródła i testów. Nie oznaczamy rozdziału stabilnym przed zakończeniem właściwego CI. Automatyzacje pozostają wyłączone.

## Ostateczne zakończenie CI i decyzja

Po zakończeniu audytu VI potwierdzono na GitHubie wyniki najnowszych uruchomień odpowiadających aktualnemu źródłu TOP-12 (commit `52d9de3077361591badae9c418d02ce0ae877beb`) oraz ostatniemu zestawowi testów (commit `73077606b319c211116fce02adaa73e48953cfa2`):

- [Algebraic topology chapters 11–12 TeX audit](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44927665533): **completed / success**. Kompilacja zależności TOP-01–12 i kontrola odsyłaczy/ramek.
- [Mathematical library application checks](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44927665510): **completed / success**. Testy aplikacyjne i regresyjne.
- [AT–DG–AG cross-volume dependency and label audit](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44927649218): **completed / success**. Kontrola odsyłaczy i zgodności między tomami.

Ostatni niezależny audyt VI nie wykazał następnych błędów. **TOP-12 uznano za stabilny po audycie VI.** Plik pozostaje na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6`, bez tworzenia nowej gałęzi i bez merge do `main`. Następnym rozdziałem do audytu stabilizacyjnego jest **TOP-13**.
