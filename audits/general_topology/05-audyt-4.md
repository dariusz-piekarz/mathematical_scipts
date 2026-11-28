# Topologia ogólna — rozdział 05 „Aksjomaty oddzielania” — audyt 4

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.3.  
**Status:** audyt wykonany z jedną korektą logiczną w podpisie rysunku; **0/2** kolejnych czystych audytów.  
**SHA-256 źródła:** `fc94e4513ea664c691617f0d1be99078375229bd86be5e5e1f2cb576e87e3cfd`.  
**SHA-256 wersji 0.2:** `aac79536f99ddc242d775fba472a4d2f3fcbf24129dec7ca0ad597313bda242c`.

## Błąd wykryty i poprawka

Podpis rysunku porównującego aksjomaty $T_1$ i $T_2$ głosił, że „każde otoczenie nie zawiera drugiego punktu”. Jest to fałsz: aksjomat $T_1$ żąda *istnienia* dwóch odpowiednich zbiorów otwartych; np. całe $X$ jest otoczeniem obu różnych punktów nawet w przestrzeni dyskretnej. Zmieniono podpis tak, aby jawnie mówił o **wybranych** otoczeniach $U$ i $V$. Geometria rysunku nie wymagała zmian.

## Niezależna kontrola merytoryczna

Ponownie przeanalizowano założenia $T_0$–$T_4$, charakterystykę $T_1$ przez singletony, domkniętość przekątnej, regularność, całkowitą regularność oraz normalność. Zweryfikowano konstrukcję w lemacie Urysohna, w szczególności oba wzory na przeciwobrazy przedziałów i przypadki wartości brzegowych $0$, $1$.

W dowodzie twierdzenia Tietzego sprawdzono: domkniętość poziomic w przestrzeni $X$, oszacowanie $2M/3$, indukcyjne ograniczenie błędu, zbieżność jednostajną, zachowanie przedziału $[a,b]$, przejście do funkcji nieograniczonych przez homeomorfizm $\mathbb{R}	o(-1,1)$ i zastosowanie lematu Urysohna bez dodatkowego założenia $T_1$. Zweryfikowano także argument kardynalny z płaszczyzną Sorgenfreya, własności metryczne i dziedziczenie aksjomatów przez podprzestrzenie.

## Kontrola techniczna

- `bash tools/validate_general_topology_ch05.sh`: **PASS**.
- Testy wszystkich 390 topologii skończonych na 0–4 punktach: **PASS**.
- Dziedziczenie: 5931 testów; normalność: 4133 pary zbiorów domkniętych: **PASS**.
- Regresja twierdzenia Tietzego: 7688 funkcji na domkniętych podprzestrzeniach: **PASS**.
- Niepowtarzalne etykiety i rozwiązane odsyłacze: 40 etykiet, 9 odsyłaczy: **PASS**.
- Samodzielna kompilacja rozdziału: **9 stron**, bez ostrzeżeń LaTeX.
- Kompilacja całej książki 01–05: **45 stron**, bez ostrzeżeń LaTeX.
- Wszystkie strony PDF wyrenderowane; wizualnie sprawdzono nowy podpis i układ rysunków: **PASS**.
- Dodano test regresyjny dla dokładnej treści poprawionego podpisu.

## Decyzja

Audyt nie jest czysty, ponieważ poprawiono merytorycznie mylący podpis. Wersja 0.3 pozostaje poza GitHubem. Kolejny krok: audyt 5 bez rozszerzania zakresu materiału, z docelowym licznikiem 1/2, jeśli nie pojawią się nowe uwagi.
