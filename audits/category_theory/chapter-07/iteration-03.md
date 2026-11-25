# CAT-07 — audyt III (kontrolny)

Stan badany 7055eed6cb92eaa67fed967f874ecde3346ee099; źródło 688fc2af259de918dde0bf2861c8a9ca8b09bb79. Ponownie porównano 29 blobów na stanie 86a3a17ca8e2fc6e1df27353deaf27593b195965 z CI 45588820491 (a408e8f0a14df0abf4b35260a97c37a03bbba1ea): bez różnic.

## Kontrola matematyczna
Ponownie przeanalizowano definicje equalizatora i koequalizatora, konstrukcje iloczynów włóknistych i pushoutów przez iloczyn/koprodukt oraz odpowiedni equalizator/koequalizator, normalne domknięcie relacji w Grp i iloraz przez obraz różnicy w modułach. W lemacie o sklejaniu przy prawym kwadracie kartezjańskim zewnętrzna para strzałek wyznacza jednoznacznie strzałkę do środkowego obiektu Q. W kierunku odwrotnym jednoznaczność w prawym kwadracie wymusza zgodność ze środkową strzałką. W dualnym twierdzeniu zakłada się lewy kwadrat kokartezjański. Stabilność mono/epi wynika ze skracania i własności uniwersalnych, a izomorfizm z jawnego przekroju i moniczności. W kontrprzykładzie gładkim obie krzywe mają ten sam punkt początkowy z jednoznaczności dla singletonu, a ich różniczki dają niezależne wektory w R². Twierdzenie o submersji wyklucza obraz zawarty w dwóch przecinających się prostych. Transwersalność jest warunkiem wystarczającym, nie ogólnie koniecznym. Nie wykryto nowych istotnych błędów; bez zmian tekstu i zakresu.

## Niezależne kontrole
Uruchomiono lokalnie Python, kod zapisano w tests/mathematical/category_theory/chapter-07/control.py, commit e4651827feaa1619e6390228b6b43f21dc2d6aaa.
- 1197 przemiennych diagramów na zbiorach mocy 0–2 z kanonicznym prawym pullbackiem i dowolnym lewym kwadratem: porównano bijektywność map do zbiorów zgodnych par dla lewego kwadratu i prostokąta. Obejmuje przypadki niespełniające własności uniwersalnej.
- 978 przypadków zgodności generatora mapy z modułu cyklicznego do jądra różnicy i wszystkich jego wielokrotności nad Z/m, m=2,3,4,5.
- 978 przypadków faktoryzacji homomorfizmu przez klasy ilorazu modułu dla tych samych pierścieni; zgodność równoważna u f=v g.
- 275 przypadków pullbacku bijekcji: przeciwległy rzut bijektywny.
Łącznie 3428 przypadków PASS. Skrypt ręczny, poza discovery CI. Kontrole skończone nie zastępują dowodów ani formalizacji Lean; Lean nie uruchamiano.

## CI i PDF
Wszystkie osiem kroków job validate success, 45 metod testowych. Pobrano artefakt 15009947548, rozpakowano. pdfinfo: 49 stron. pdftotext -layout: CAT-07 obejmuje strony 28–33. Log bez dopasowań Warning, Overfull, ^!. Render pdftoppm 130 dpi, montaż sześciu stron obejrzano: nie zauważono kolizji, obcięć ani usterek diagramów. Kontrola wizualna ograniczona do CAT-07.
Przy zapisie raportu wystąpił konflikt 409 wynikający ze zmiany głowy gałęzi. Ponowiono po odczycie drzewa i potwierdzeniu niezmienności plików CAT, bez nadpisywania cudzych zmian.

## Decyzja
CAT-07 zamknięty po stabilizacji i niezależnej kontroli. Kolejny CAT-08, granice i kogranice, pierwszy audyt i rozszerzenia z uwzględnieniem materiału AT-10 i AT-29.
