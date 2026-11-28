# Topologia algebraiczna — szczegółowy audyt AT-27/AT-28

**Data:** 20 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (bez zmian w main).  
**Zakres:** dokładnie dwie kanoniczne jednostki: rozdział 27 o sześciu operacjach snopowych i dualności Verdiera oraz rozdział 28 o topologii gładkich zespolonych odmian projektowych.  
**Standard:** wzorcowa szczegółowość dowodów, definicji i przykładów z DG-01; nie usuwano starych etykiet, dowodów, przykładów ani rysunków.

## AT-27 — stwierdzenia, dowody i przykład pochodnego obrazu

Przejrzano definicje kategorii pochodnych snopów, stożka, adjunkcji, funktorów z właściwym nośnikiem, wewnętrznego Homu, dwóch trójkątów lokalizacyjnych, czystości przy submersji, dualności Verdiera, zmianę podstawy, wzór projekcji, Leraya oraz pobliskie i zanikające cykle.

**Błąd składni matematycznej:** W źródle znajdowały się cztery podwójne ukośniki przy poleceniach matematycznych: jedno wystąpienie \\to oraz trzy \\mathcal. Zastąpiono je właściwymi poleceniami \to i \mathcal. Zmieniono też polskie „sekwencje” na „ciągi”.

**Dopisany szczegółowy przykład:** prz:xvi-punctured-disc-audit. Dla włożenia otwartego j: U=C\{0} → C obliczono kohomologię przekłutego dysku przez jawną retrakcję na S¹: H⁰=k, H¹=k i wyższe grupy zerowe. Z przejścia do kiełków otrzymano (R⁰j_*k_U)_0=k, (R¹j_*k_U)_0=k, (R^qj_*k_U)_0=0 dla q≥2; dla j_! kiełek w zerze jest zerowy. Niezależnie przez długi ciąg pary (D,D\{0}) obliczono H²(D,D\{0};k)=k i i^!k_C=k[-2]. Wyprowadzono trójkąt lokalizacyjny, który łączy te rachunki. Zachowano objaśnienia granic ważności twierdzeń ogólnych.

**Rysunek:** fig:xvi-punctured-disc-audit pokazuje przekłuty dysk i klasę pierwszej kohomologii; rysunek jest osadzony bezpośrednio w źródle za pomocą TikZ.

**Zastrzeżenia matematyczne:** Głębokie ogólne twierdzenia o istnieniu f^!, dualności Verdiera, zmianie podstawy, czystości i porównaniu pobliskich cykli z włóknami Milnora pozostają jawnie przyjętymi wynikami; rachunki przykładowe nie stanowią ich dowodu.

## AT-28 — dowód rozkładu całkowitej kohomologii rozdmuchania

Przejrzano hipotezy słabego i silnego twierdzenia Lefschetza, argument oparty na relacjach sl₂, prymitywną kohomologię, relacje Hodge'a–Riemanna i indeks Hodge'a, lokalną konstrukcję rozdmuchania w punkcie, klasy Cherna, formy przecięcia oraz wzór dla rozdmuchania w gładkim centrum.

**Luka dowodowa:** Wcześniejszy dowód Twierdzenia thm:xvii-blowup-general przechodził od izomorfizmu grup względnych i iniektywności p^* do krótkiego ciągu dokładnego poprzez skrótowe powołanie się na lemat o wężu. Dla kontroli wszystkich członów ciągu konieczne jest jawne uzasadnienie obrazu i jądra. Zastąpiono skrót czterema szczegółowymi krokami:

1. Iniektywność π^* — π ma stopień topologiczny 1; z dualności Poincarégo i naturalności iloczynu kap wynika π_!π^*=id. Argument działa nad Z również w obecności torsji.
2. Surjektywność klasy [j^*] z H^k(Bl_Z X;Z) do H^k(E;Z)/p^*H^k(Z;Z) — z Leraya–Hirscha i j^*j_*β=-ξβ każdy nowy składnik ξ^a p^*β ma wskazany przeciwobraz.
3. Dokładne jądro — dla j^*γ=p^*b stosujemy naturalność długich ciągów par (X,Z) i (Bl_Z X,E). Izomorfizm na kohomologii względnej pozwala z równości δ_E(p^*b)=0 wydedukować δ_Z b=0. Podnosząc b do klasy α na X i odejmując π^*α, sprowadzamy γ do obrazu względnego; izomorfizm względny dowodzi, że również ten składnik leży w obrazie π^*.
4. Rozszczepienie — jawny przekrój przez klasy -j_*(ξ^{a−1}p^*β) daje bezpośredni rozkład na część pochodzącą z X i nowe klasy z Z.

Zachowano i wyodrębniono potrzebne zależności: dualność Poincarégo, Leray–Hirsch, homomorfizm Gysina i wzór samoprzecięcia. Nie zastąpiono ich niewykazanym stwierdzeniem.

**Dopisany przykład:** prz:xvii-blowup-elliptic-audit. Dla X=P³_C i gładkiej płaskiej krzywej Fermata Z: x³+y³+z³=0 obliczono gładkość (pochodne cząstkowe), g(Z)=1 (adjunkcja i deg K=2g−2) oraz addytywny rozkład H^k(Bl_Z X;Z)=H^k(P³;Z)⊕H^{k−2}(Z;Z). Wszystkie liczby Bettiego wynoszą (1,0,2,2,2,0,1), a charakterystyka Eulera pozostaje 4. Homomorfizm Gysina zwiększa oba indeksy Hodge'a o 1, dlatego nowe klasy H³ mają typy (2,1) i (1,2), po jednej w każdym. To przykład niebanalnego efektu rozdmuchania w centrum dodatniego rodzaju.

**Rysunek:** fig:xvii-elliptic-blowup-audit przedstawia przesunięcie stopni H⁰, H¹, H² krzywej do nowej kohomologii H², H³, H⁴.

**Ważne zależności źródłowe:** AT-28 nadal jawnie włącza trzy istniejące moduły shared/pl: slabe_twierdzenie_lefschetza.tex, rozdmuchanie_punktu_normalna.tex, rozdmuchanie_punktu_kohomologia.tex. Są to wspólne kanoniczne fragmenty, posiadające strażników przeciw ponownemu złożeniu i historyczne aliasy etykiet. Nie kopiowano ich do rozdziału, by nie wytwarzać równoległych definicji i kolizji. Nie są to obrazy ani dane zewnętrzne, lecz faktyczne zależności źródłowe LaTeX i przy scalaniu trzeba je zachować.

**Zastrzeżenia matematyczne:** Bertini, geometryczne słabe twierdzenie Lefschetza, tożsamości Kählerowskie, twierdzenie Hodge'a, punktowa tożsamość Hodge'a dla form prymitywnych, adjunkcja dla krzywych, Leray–Hirsch i Gysin to wyniki zewnętrzne bądź wcześniej przyjęte. Audyt potwierdza wyprowadzone konsekwencje pod tymi jawnymi założeniami, nie deklaruje samodzielnych dowodów całej ich teorii.

## Testy, pełna kompilacja i oględziny PDF

- Dodano application/tests/test_topology_chapters_27_28.py: osiem testów regresyjnych (włączenia 28 rozdziałów; etykiety i referencje; współdzielone moduły; bilans środowisk; polecenia LaTeX i terminologia; rachunek przekłutego dysku; liczby Bettiego/Hodge'a krzywej eliptycznej; kompletność kroków dowodu rozdmuchania).
- Dodano .github/workflows/algebraic-topology-audit-ch27-28.yml, z automatyczną kontrolą testów, dwuprzebiegową kompilacją całego AT-01–28, kontrolą odsyłaczy i przepełnienia wierszy oraz artefaktem PDF.
- **GitHub Actions:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44821606662 — SUCCESS, osiem testów ukończono bez błędów.
- **Kompilacja LaTeX:** SUCCESS — 284 strony A4, dwa przebiegi pdflatex, brak niezdefiniowanych odsyłaczy oraz „Overfull \hbox”.
- **Oględziny prawdziwego PDF:** pobrano artefakt ZIP z GitHub Actions i wyrenderowano strony 269, 270, 282, 283. Przejrzano tekst i układ dwóch nowych przykładów, poprawiony dowód w AT-28 oraz nowe diagramy TikZ na stronach 270 i 283. Nie stwierdzono nakładania napisów, obciętych wzorów ani kolizji strzałek w tych stronach. Oględziny są selektywne, nie obejmują wszystkich 284 stron.
- Oryginalne etykiety i pozostałe historyczne dowody obu rozdziałów zostały zachowane; nie modyfikowano main.

## Status i kolejny etap

AT-27: zaakceptowany_z_zastrzezeniem — sprawdzone rachunki punktowe i podstawowe trójkąty, pozostają jawnie przyjęte twierdzenia ogólnego formalizmu sześciu operacji.

AT-28: zaakceptowany_z_zastrzezeniem — naprawiony kluczowy argument dowodzący całkowitego rozkładu kohomologii rozdmuchania, zweryfikowany nowy przykład i rysunek; podstawowe głębokie twierdzenia Hodge'a/Lefschetza/Leraya–Hirscha pozostają przyjętymi zależnościami.

**Następna iteracja:** AT-29 i AT-30, ze szczególnym przeglądem zależności od kanonicznej geometrii różniczkowej oraz rozróżnieniem materiału powtórzonego od niezbędnych lokalnych przypomnień.
