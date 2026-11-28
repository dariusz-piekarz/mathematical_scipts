# PDE-05 — stabilizacja, iteracja 66

Data: 2026-11-25. Rozdział 05: Równanie falowe.

## Ponowna lektura 5.6–5.8
- PDE-05-023–024: wybór niezerowych wartości A(t*) i X(x*) uzasadnia rozdzielenie zmiennych bez dzielenia w zerach. Całkowanie przez części przy warunkach Dirichleta daje dodatniość lambda. Rozwiązanie ODE wyznacza m≥1, lambda_m=(m pi/L)^2 i omega_m=c sqrt(lambda_m). Skończone sumy z h_m/omega_m spełniają oba dane i warunki brzegowe, bez założenia zbieżności szeregu nieskończonego.
- PDE-05-025–026: całki sin² i cos² wynoszą L/2, energia modu ma współczynnik L/4 i omega_m²(a_m²+b_m²). Różniczkowanie na zwartym prostokącie, przemienność pochodnych i PDE dają strumień c²[u_t u_x]_0^L, zerowy dzięki warunkowi brzegowemu. Zerowa energia różnicy i ciągłość wymuszają znikanie pochodnych, a zerowa wartość brzegowa znikanie różnicy.
- PDE-05-027–028: relacja dyspersji z q=lambda² sin²(theta/2), wielomian z²-2(1-2q)z+1 i wyróżnik 16q(q-1). Dla q>1 pierwiastki ujemne odwrotne, jeden o module >1. Również przy A_0=1,H=0 oba współczynniki wynoszą 1/2, ponieważ A_1 jest średnią pierwiastków. Niestabilność nie jest artefaktem inicjalizacji.
- PDE-05-029–030: q=0 daje A_m=A_0+m dt H; q=1 daje A_m=(-1)^m(A_0-m dt H). Oba znaki poprawne. Eliminacja warstwy -1 daje A_1=(1-2q)A_0+dt H. Dla 0<q<1 suma geometryczna dla sin(m alpha)/sin(alpha) ma m składników modułu 1. Oszacowanie |A_m|≤|A_0|+t_m|H| zachodzi również w obu przypadkach granicznych. Ortogonalność skończonej bazy Fouriera, nierówność trójkąta i mnożnik sqrt(dx) dają właściwe oszacowanie normy l² na skończonym horyzoncie i okresowej siatce.
- PDE-05-031–032: indukcja dla zasięgu stencilu i lokalna inicjalizacja dają maksymalny promień m dx. Warunek geometryczny jest konieczną inkluzją stożków, a nie dowodem stabilności. Podsumowanie zachowuje zakres wyników, w tym dowód Huygensa tylko dla n=1,2,3. Brak dawnych form zdominowan-. Nie wykryto nowych istotnych błędów.

## Identyfikacja wersji i dowody kontroli
Pierwszy audyt 8/8 sekcji: iteracje 55–61. Niezależna pełna lektura 8/8: iteracje 64–66, podzielona na trzy części. Brakujący raport iteracji 65 zapisano w commicie 82638d88ba52d62081710236d3304043080fa73b. Źródło i rejestr pozostają niezmienione po konflikcie równoległych commitów.

Aktualne bloby odczytano w iteracji 66 i porównano z wartościami ustalonymi w iteracji 64 dla commitu CI 55060b71c0f281d5aa343dfea4797423fe28f2f6:
- rozdział 05: 97d5fa77fa7282ceee6fbf924e77b28d788975f8
- rozdział 01: aeea9d0a8c39cb2a2049d0cd982688dd370fc874
- rozdział 04: abd8dc9eca604f7105a6649cfd961547ef7968c5
- rejestr: dd58ee2123ea338f210476584868ede0a501efd6
- test: 233f3d7fcc8d7bdb3080b8e98534b3d06094c45d
- workflow: b1b7b5aa4209088da8c0740142040e4fc894924f
- księga: e765e8341ae75f02a9f4e18c6069208939e009b3
- manifest: 7ce9338ae38894f26a1fe0048dc4bb58913c62dc
- listings: 8a20f4cfae442a5d19ef078a659fad3d70b78f77
- preambuła Atlasu: ecd56e4335ae5b671330ad783964445a010b8786

Sprawdzono 30 unikatowych etykiet, 26 odsyłaczy, oba cele zewnętrzne dokładnie raz we właściwych rozdziałach, poprawne zagnieżdżenie środowisk oraz 34 kolejne ID i kotwice (32 semantyczne, 2 wizualne). CI 45567364891, job 139045324745: wszystkie kroki success, 9 metod unittest, izolowana kompilacja, diagnostyka, render i publikacja artefaktu. Nie uruchamiano testów ponownie lokalnie.

## Kontrola wizualna
Zgodnie z kontrolą artefaktu 15000422877 z iteracji 65 i ponownymi oględzinami w iteracji 66: PDF 16 stron A4, rysunek wraz z podpisem na stronie 3, długość podstawy 2ct0, nierówność regularizowanej energii na stronie 5 mieści się w szerokości składu. Końcowy log nie zawiera przekroczeń szerokości składu ani niezdefiniowanych odsyłaczy; dwa oczekiwane ostrzeżenia hyperref dotyczą pustych celów odsyłaczy zewnętrznych w izolowanej kompilacji. Kryteria 033–034 zweryfikowane.

## Decyzja
Rozdział 05 ustabilizowany w zakresie dwóch pełnych lektur matematycznych, trwałych kryteriów, testów CI, izolowanej kompilacji i kontroli wizualnej. Nie przeprowadzono formalizacji Lean ani pełnej kompilacji tomu; testy rachunkowe nie stanowią dowodów twierdzeń. Przy zmianie źródła lub zależności należy powtórzyć odpowiednie kontrole. Postęp 5/33. Następny etap: rozdział 06 — preflight i pierwszy audyt.
