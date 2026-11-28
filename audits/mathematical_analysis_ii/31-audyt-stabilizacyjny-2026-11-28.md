# AM II 31 — audyt stabilizacyjny bez nowych uwag

Data: 2026-11-28. Źródło: commit b81f9b60761a63653ddb674cd28940c1167391b6, blob 50618adc7743041dd4f31efada5861b0a91707fb (1034 wiersze). Potwierdzono identyczny blob na gałęzi roboczej.

## Matematyka
- Definicje obu całek przez parametr długości łuku: mierzalność, przypadek długości zero, ograniczoność dla ciągłych pól i konwencja iloczynu z nieskończonością — poprawne.
- Ważony wzór pola: jakobian jednowymiarowy, przedłużenie Lipschitzowskie, krotność borelowska, zgodność krotności z dokładnością do zbioru przeliczalnego, rozdzielenie części dodatniej i ujemnej — poprawne.
- Lemat o mierze obrazowej parametru długości: s jest absolutnie ciągła, niemalejąca i surjektywna na [0,ℓ]. Miary skończone mają wspólną masę i zgadzają się na układzie π przedziałów [0,q]; hipotezy ME-02::thm:uniqueness-finite oraz ME-13::thm:pushforward-integral-13 spełnione.
- Wzór dla pola w parametrze absolutnie ciągłym: na zbiorze s'=0 pochodna złożenia jest zerowa dzięki własności Lipschitza; przeciwobraz zbioru wyjątkowego B w części s'>0 jest zerowy dzięki lematowi o mierze obrazowej. Borelowski przedstawiciel pochodnej i reguła łańcuchowa — poprawne.
- Reparametryzacja: monotoniczna surjekcja nie musi być różnowartościowa ani absolutnie ciągła, wzory na parametr długości i znak całki zgodne z AM II 29. Addytywność także przy częściach zerowej długości.
- Sumy z punktami pośrednimi: błędy ograniczone przez ℓ razy moduł ciągłości; zastąpienie długości części długością cięciwy korzysta z twierdzenia o zbieżności długości łamanych AM II 29, które obejmuje dowolne ciągi podziałów o średnicy dążącej do zera. Istnienie poszczególnych całek Riemanna–Stieltjesa wynika z zastosowania do pól jednowspółrzędnych.
- Przykład Cantora: s=C, parametryzacja długością (u,0), obie całki 1/2, natomiast oba nieuprawnione wyrażenia z prędkością dają 0.
- Cofnięcie 1-formy, twierdzenie o funkcji pierwotnej, niezależność od drogi, kryterium zamkniętych łamanych: argument przez odcinek i oszacowanie reszty różniczki poprawny. Potencjał jednoznaczny z dokładnością do stałej na zbiorze spójnym.
- Kryterium gwiaździstości: hipotezy różniczkowania pod całką AM II 28 zweryfikowane, symetria pochodnych i pochodna tF_i(p+t(x-p)) poprawne.
- Rachunki ponownie sprawdzone: okrąg πR³ i 2πR², pole na płaszczyźnie bez punktu 2π, helisa, dwie drogi 2/3 i 1/2, wykres (2√2−1)/3 i 1/3, częściowe powtórzenie 15/2 i 9/2, pole zachowawcze w sześcianie 2, długości √3 i 3. Wzór z jednostkowym wektorem stycznym rozróżnia funkcję parametru od funkcji obrazu.

## Statyka
27 etykiet; 54 wystąpienia odsyłaczy wewnętrznych i 11 między skryptami. Wszystkie cele istnieją w sprawdzonych źródłach AM II 15,28,29,31; AM I 37; ME 02,13,26,28; DG 10. Brak duplikatów etykiet rozdziału w kontrolowanych rozdziałach AM II. Bilans klamer 0, minimalny bilans 0, środowiska poprawnie zagnieżdżone. Trzy rysunki bez zmian; w niniejszym przebiegu nie ponawiano samodzielnej kompilacji.

CI źródła b81f9b6: terminologia #46135630007 success; AM II #46135630088 in_progress, #46135636968 skipped; aplikacja #46135630001 cancelled. Nie uruchomiono dodatkowego workflow. Pełny PDF niepotwierdzony.

Wynik: zero nowych uwag merytorycznych i statycznych. Źródło bez zmian. Następny etap: audyt kontrolny.
