# RRC 17 — iteracja 303: audyt kontrolny źródła

Źródło: blob 6141697a8be95e2e910961824648acd3c16b37eb, commit 1e1d05962bb4ec05d81c0769458ced501d18bd84. 970 wierszy. Sprawdzono ponownie wszystkie osiem sekcji. W stosunku do wersji po 301 różnica ogranicza się do dwóch korekt językowych z iteracji 302.

Kontrola merytoryczna:
- 17.1–17.2: słabe nierówności i znaki, gęstość testów nieujemnych, skalowanie R^(2-d), stała 4(Lambda/lambda)^2.
- 17.3: normalizacja rekurencji i próg małości, zanurzenie w d=2, wykładnik 1-1/chi oraz końcowa granica.
- 17.4: dopuszczalność potęg, znak beta-1, skalowanie na parach kul i absorpcja dla q<2.
- 17.5: test logarytmiczny, dyadyczne pokrycia i miara generacji, ogon wykładniczy, przejście od kostek do kul i most potęgowy.
- 17.6: odwrócenie oszacowania dla v^(-1), granica epsilon, współczynnik redukcji oscylacji, reprezentant i zasada maksimum.
- 17.7–17.8: słabe pochodne w przykładzie skokowym, eliptyczność i całkowalność gradientu przykładu radialnego, oba wyrazy brzegowe oraz zakres twierdzeń.

Wynik: nie wykryto nowych usterek matematycznych, językowych ani strukturalnych wymagających edycji. Nie zmieniano źródła. 36 unikatowych etykiet, 42 wystąpienia odsyłaczy, siedem różnych zewnętrznych celów (jak w 301), prawidłowe zagnieżdżenie środowisk. Kontrola jest ponowną lekturą tego samego audytora, a nie niezależną recenzją innej osoby.

Stan techniczny na końcu iteracji: [{"id":45981760560,"status":"queued","conclusion":null},{"id":45981760573,"status":"queued","conclusion":null}]. Odbiór wizualny 11 stron i PASS poprzedniej wersji udokumentowano w 302. Nie wykonano nowej kontroli wizualnej PDF po korektach językowych. Pełny odbiór zależy od dedykowanego CI aktualnej wersji; globalne CI pozostaje odrębnym warunkiem.

Przygotowanie rozdziału 18: odczytano spis dziesięciu sekcji i początek źródła (699 wierszy, blob 85d2018fc304d7e3499c90e42a57092888d7ff24). Pierwszy audyt obejmie zgodność założeń geometrycznych, konstrukcję operatora z formy i samosprzężoność odwrotności, potem min–max. Nie edytowano rozdziału 18 przed technicznym domknięciem rozdziału 17.
