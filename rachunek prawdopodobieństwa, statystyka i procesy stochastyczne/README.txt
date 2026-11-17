Naprawione odsyłacze tomów I–IV — zgodne z nazwami plików w Twoim projekcie

Źródła:
  rachunek_prawdopodobienstwa_tom_I.tex
  rachunek_prawdopodobienstwa_tom_II.tex
  rachunek_prawdopodobienstwa_tom_III.tex
  rachunek_prawdopodobienstwa_tom_IV.tex

Wszystkie odwołania \externaldocument wskazują dokładnie te nazwy.
Etykiety i prefiksy \ref{I-...}, \ref{II-...}, \ref{III-...}, \ref{IV-...}
pozostały niezmienione. W każdym katalogu muszą znaleźć się pliki
.tex/.aux/.pdf o tym samym rdzeniu nazwy. Dostarczono skompilowane AUX i PDF.

Budowanie na Windows (PowerShell):
  .\buduj_wszystkie.ps1
  .\buduj_wszystkie.ps1 -Zadania
  .\buduj_wszystkie.ps1 -BezLaczenia

Kompilacja wykonywana jest w trzech przebiegach dla każdego tomu.
Jeśli edytujesz pojedynczy tom, przebuduj następnie wszystkie tomy
przed kolejnym korzystaniem z odsyłaczy międzytomowych.

Pojedyncze pliki PDF zawierają międzytomowe akcje GoToR. Nie każdy
czytnik (zwłaszcza przeglądarka WWW) pozwala przechodzić między plikami
przez te akcje. Dlatego dodano wersję zbiorczą
Cztery_tomy_polaczone_aktywne_linki.pdf, w której połączenia
między tomami są zwykłymi odsyłaczami wewnętrznymi.

Opcjonalna generacja wydania zbiorczego wymaga Pythona i PyMuPDF:
  py -3 -m pip install pymupdf
  py -3 polacz_tomy.py
Skrypt PowerShell bez Pythona buduje cztery tomy bez błędu;
jedynie pomija generowanie zbiorczego PDF.

Wynik kontroli po trzech przebiegach: brak nierozwiązanych odsyłaczy
(??) we wszystkich czterech tomach i w zbiorze zadań. Tom IV:
504 odsyłacze wewnętrzne, 39 międzytomowych i 6 odsyłaczy WWW.
Cała seria: 72 odsyłacze międzytomowe. W PDF zbiorczym:
1307 wewnętrznych, 6 WWW i 0 GoToR; wszystkie cele stron istnieją.
