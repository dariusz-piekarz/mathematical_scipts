# Topologia ogólna — rozdział 05 „Aksjomaty oddzielania” — audyt 3

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.2.  
**Status:** zakończony z poprawkami; licznik kolejnych czystych audytów **0/2**.  
**SHA-256 nowego źródła:** `aac79536f99ddc242d775fba472a4d2f3fcbf24129dec7ca0ad597313bda242c`.  
**SHA-256 poprzedniego źródła:** `f41f5bda8d5af272b3d13c3b94cd2007eabbe77a92452d1dc7e5af5ce107a04b`.

## Zakres i wynik

Na życzenie użytkownika dodano nowe schematy wymagań T1 i T2 (wspólny rysunek porównawczy) i graficzny przykład przedłużenia na domkniętym podzbiorze [0,4]. Dodatkowo wprowadzono pełne twierdzenie Tietzego o przedłużeniu: ciągłe funkcje A→R, gdzie A jest domknięty w normalnym X, przedłużają się ciągle na X. Zachowano wersję przedziałową, a następnie udowodniono wersję dla funkcji nieograniczonych bez T1.

Szczegółowo sprawdzono: domkniętość zbiorów poziomicowych w X, jednoznaczny wybór separatorów na kolejnych poziomach, redukcję błędu do 2/3, jednostajną zbieżność szeregu przybliżeń, zachowanie przedziału oraz konstrukcję przedłużenia funkcji nieograniczonej przez homeomorfizm R→(-1,1) i poprawienie wartości ±1 za pomocą lematu Urysohna.

Audyt rysunków: zintegrowano schematy T1 i T2 w czytelny rysunek porównawczy; umieszczono barierę dla obiektów pływających przed następną sekcją, aby diagram twierdzenia Tietzego nie rozdzielał treści innego twierdzenia między stronami. Kontrolowano wizualnie strony 1, 5, 6, 7 i układ całego rozdziału.

## Testy

- `bash tools/validate_general_topology_ch05.sh` — **PASS**.
- Dotychczasowa regresja rozdziałów 01–05 — **PASS**.
- Aksjomaty oddzielania: wszystkie 390 przestrzeni topologicznych o co najwyżej 4 punktach — **PASS**.
- Dziedziczenie aksjomatów: 5931 przypadków — **PASS**.
- Normalność: 4133 przypadki rozłącznych zbiorów domkniętych — **PASS**.
- Dodatkowy test Tietzego: 7688 funkcji ciągłych o trzech wartościach na domkniętych podprzestrzeniach skończonych przestrzeni normalnych — **PASS**.
- Niepowtarzalne etykiety i odsyłacze — **PASS**.
- Samodzielny PDF rozdziału: 9 stron, bez ostrzeżeń LaTeX — **PASS**.
- Książka rozdziałów 01–05: 45 stron, bez ostrzeżeń LaTeX — **PASS**.

## Decyzja

Źródło zostało rozbudowane zgodnie z prośbą użytkownika. Mimo zakończenia audytu nie zaliczamy go jako czystego, ponieważ wprowadzono istotne zmiany treści i rysunków. W następnej iteracji należy rozpocząć niezależny audyt 4 wersji 0.2. Brak pushu na GitHub do dwóch kolejnych czystych audytów i sprawdzenia CI.
