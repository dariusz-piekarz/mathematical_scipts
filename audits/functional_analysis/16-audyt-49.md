# Rozdział 16 — audyt 49 (5/5, poprawkowy, 0/2)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6. Ponowna lektura pełnego źródła po 48.

## Matematyka i język
Poprawiono mylący tytuł przykładu hesjanu (dolne oszacowanie jest warunkiem wystarczającym silnej wypukłości, nie koniecznym warunkiem minimum). Jawnie określono gradient w twierdzeniu subgradientowym oraz poprawiono interpunkcję dowodu proksymalnego. W przykładzie Dirichleta uzupełniono przejście L² do L¹ i niezależność od reprezentanta klasy, ciągłość członu liniowego energii, dokładną tożsamość ścisłej wypukłości, dolne ograniczenie przez dopełnienie kwadratu, odwołanie do lematu słabej półciągłości, przynależność rozwiązania dla f=1 do H oraz całkowanie przez części przez pochodną iloczynu i znikający człon brzegowy. Bez nowych tematów. Pozostałe podsekcje ponownie przeczytano.

## Technika
Źródło 2af4928393f94b84ad12e1f9fea97c7b9210f724, blob d53c9091964254d5293b812b46e797f4a4aeb0a4. Odczyt po zapisie: 666 wierszy według split, 19/19 unikatowych etykiet, zbilansowane środowiska, oba fragmenty kontrolne obecne. Test FA16_DIRICHLET_CONVEXITY_01 w 95ffe58240c6103e3251ec5116d40ad0606ff372; niezależna kontrola całkowitoliczbowa 147 tożsamości wypukłości zaliczona. Nie jest to wykonanie całego pliku testów. CI 48: 45375737671, 45375684315 i 45375634714 zakończone sukcesem. W 45375737671 potwierdzono osobno testy, kompilację kontekstu 01–17, automatyczną kontrolę PDF/odsyłaczy i przesłanie artefaktu functional-analysis-ch16-pdf (14911177055). Nie wykonano oględzin stron PDF. CI 49 po zmianach jeszcze niepotwierdzone.

## Decyzja
Audyt poprawkowy, licznik stabilizacji 0/2; następny 50. Wymagane dwa kolejne czyste audyty; nie dodawać nowych zagadnień.
