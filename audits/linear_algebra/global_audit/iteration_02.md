# Globalny audyt algebry liniowej — iteracja 02/09

**Data:** 22 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Wejściowy HEAD:** `f17176b04aabab643da7802e9478827b8fa95ec0`.  
**Zakres:** rozdziały 05–08.  
**Standard:** `AGENTS.md` i `docs/pl/standardy_terminologiczne.md`.

## Rzeczywista kontrola matematyczna

Odczytano źródła czterech rozdziałów (odpowiednio 23763, 23371, 32021, 34067 znaków). Wykryto i przejrzano **55** środowisk dowodów (10 + 11 + 20 + 14), ze szczególnym sprawdzeniem następujących miejsc:

- **05:** istnienie i jednoznaczność RREF, charakterystyka pozycji pivotów za pomocą przestrzeni wierszy, rząd i jądro, wybór kolumn **oryginalnej** macierzy do bazy obrazu, kryterium zgodności i przypadki pustych macierzy. Uzasadnienia przy tych wzorach są obecne.
- **06:** multiplikatywność znaku permutacji przez zamiany sąsiednie, naprzemienność wyznacznika również w charakterystyce dwa, argument z jedyności wieloliniowej funkcji naprzemiennej w dowodzie \(\det(AB)=\det A\det B\), wzory Laplace'a i Cramera oraz przypadek \(n=0\). Nie znaleziono błędu w sprawdzonych rozumowaniach.
- **07:** macierz przejścia \([v]_B=P[v]_C\) i reguła \([\varphi]_{C^*}=P^{\mathsf T}[\varphi]_{B^*}\), dwa podwójne anihilatory, funkcjonały na ilorazie, naturalność bidualności i cykliczność śladu. W szczególności wzór z \(P^{-1}\) dla nowej bazy dualnej ma prawidłową orientację indeksów.
- **08:** współrzędne wieloliniowe, przestrzenie form symetrycznych i naprzemiennych w dowolnej charakterystyce, operatory symetryzacji/alternowania oraz polaryzacja. Znaleziono istotną lukę w indeksowaniu par permutacji, opisaną poniżej.

## Rzeczywiście poprawione usterki

1. **08, dowód Twierdzenia \(\ref{thm:lin8-operatory-wlasnosci}\):** dotychczasowe parowanie \(\sigma\mapsto(p\,q)\circ\sigma\) nie zamienia w ogólności *pozycji* \(p,q\) w krotce \((v_{\sigma(1)},\ldots,v_{\sigma(k)})\); zamienia wartości indeksów. Poprawiono na \(\sigma\mapsto\sigma\circ(p\,q)\), a także dopisano wyjaśnienie, dlaczego argumenty są wówczas zamieniane miejscami, znaki przeciwne, a pary rozłączne. To istotne dla dowodu naprzemienności \(\mathcal AF\) także w charakterystyce dwa.
2. **08, wstęp:** stwierdzenie, że iloczyn tensorowy będzie w „następnym rozdziale”, było fałszywe (rozdział 09 dotyczy form dwuliniowych). Zastąpiono je jawnym odsyłaczem do rozdziału 10.

Nie dodano nowych twierdzeń. Historyczne etykiety pozostawiono bez zmian.

## Audyt formalny i dalsze kontrole

Wszystkie 55 przejrzanych środowisk twierdzeń, lematów, stwierdzeń i wniosków mają środowisko dowodu. W sprawdzonych miejscach uwzględniono ciała dowolnej charakterystyki, przypadki zerowego wymiaru, zmienne swobodne i nieodwracalne macierze. Zbadano przykłady wskazane w rozdziałach, lecz **nie wykonano** kompletnej niezależnej weryfikacji każdego rachunku przykładowego ani pełnej inspekcji wizualnej wszystkich stron i rysunków.

Przed zapisem najnowsze widoczne przebiegi workflow `Linear algebra chapter validation`: `[{"id":44964595675,"sha":"7a29c79fe9481104ff391523433aa957d5002a2d","status":"completed","conclusion":"success"}]`. Przebieg dla nowego commitu może dopiero wystartować. Nie oznaczamy CI/PDF jako PASS, dopóki nie ma potwierdzenia dla aktualnego SHA.

## Status

**Iteracja 02 wykonana, blok 05–08 wymaga ponownej kontroli po poprawce i weryfikacji CI/PDF.** Rozdziały 01–04 nadal mają otwartą kontrolę PDF/CI z iteracji 01. Iteracje 03–09 pozostają do wykonania. Raport i tabela statusów są częścią tego samego commitu.
