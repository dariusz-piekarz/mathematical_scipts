# PDE-02 — siódmy przebieg stabilizacyjny (iteracja 26, 2026-11-24)

Źródło: blob cede0206acd0e122be62c5bd6af78df97fcf8eeb, identyczny na aktualnej gałęzi i w commicie e7be79442c3d00c5040dad6ee2c904962a2a92dd. Nie zmieniono źródła.

- Ponowny przegląd dowodów transportu liniowego, równania wariacyjnego, wzoru Jacobiego–Liouville'a, zachowania masy i oszacowań norm L^p: bez nowych usterek. Porównano pełne źródło z wersją z iteracji 24: jedyne zmiany to osiem zamian różniczki całkowania na jawne dλ₁. Nie zmieniono żadnego argumentu dowodowego.
- Sprawdzono 51 różnych etykiet, 62 odsyłacze (jeden zewnętrzny chap:pde-code, sprawdzony przez CI), zagnieżdżenie środowisk, ciągłość ID i kotwice wszystkich 33 kryteriów. Brak pozostałych wystąpień wzorca starej notacji całek. Kontrola kotwic nie jest ponownym dowodem wszystkich twierdzeń.
- Przebiegi 45428529669 oraz 45428593690 success. W drugim potwierdzono wszystkie kroki: 6 testów Python, struktura, kompilacja, diagnostyka, renderowanie, publikacja artefaktu. Nie wykonywano dodatkowego lokalnego uruchomienia testów.
- Pobrano artefakt 14937601427 z przebiegu 45428593690 (5190154 bajtów). Sprawdzono pdfinfo: 16 stron A4 i 16 renderów. Log bez krytycznych komunikatów z zakresu workflow. Obejrzano arkusz kontaktowy wszystkich stron oraz strony 7 i 10 w pełnym rozmiarze: oba rysunki wraz z podpisami na swoich stronach, wzór całkowy rozwiązania słabego mieści się w łamie, brak zauważonych kolizji. Kompilacja izolowana, nie całej książki.
- Lean nie uruchomiono.

Pierwszy czysty przebieg po korekcie notacji z iteracji 25. Rozdział nadal otwarty do drugiego niezależnego przebiegu bez zmian.
