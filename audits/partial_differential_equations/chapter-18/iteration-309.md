# RRC 18 — iteracja 309: druga lektura stabilizacyjna

Commit źródła: 4c9d4958cf8e23592094b41cb4a115fd7a7b9616.

Ponownie odczytano wszystkie 10 sekcji. Uzupełnienia:
- Dokładna charakteryzacja dziedziny operatora Dirichleta przez dystrybucyjne wyrażenie eliptyczne należące do L^2; oba kierunki dowodu przez testy i gęstość.
- Jawne oszacowanie operatora rozwiązującego T i uzasadnienie liniowości; uzupełnienie argumentu ośrodkowości L^2 i rozróżnienie jej od nieskończonego wymiaru.
- W drugiej części min–max jawny argument wymiarowy z bazą F.
- Dwustronny rząd wzrostu wartości własnych dla A,V bez założenia o mierze brzegu: porównanie z wewnętrznym i zewnętrznym sześcianem oraz porównanie form.
- Poprawiono interpretację Li–Yau (koszt całkowity, nie średni); z warunku równości w lemacie i ciągłości transformat Fouriera wykazano ścisłość nierówności dla każdego skończonego k.
- Uściślono Fubiniego w harmonicznym podniesieniu, usunięto powtórzenie dowodu Poincarégo; jawnie zdefiniowano dwuliniową formę i dziedzinę operatora Neumanna.
- Doprecyzowano ograniczenia wynikające z prawa Weyla dla reszty śladu cieplnego.

Kontrola źródła w zapisanym commicie: 1232 wiersze (poprzednio 1180), 42 zachowane unikatowe etykiety, 57 wystąpień odsyłaczy, 13 różnych celów zewnętrznych. Wszystkie cele istnieją jednoznacznie w rozdziale i rozdziałach 7, 9, 10, 12, 14, 20. Brak niezgodności begin/end.

Dedykowany run aktualnego commitu: 45985450719, queued. Dwa wcześniejsze runy rozdziału 18 (45984455701, 45984997926) przy sprawdzeniu na początku iteracji również queued. Kompilacja, wizualny odbiór i globalne CI niepotwierdzone. Nadal stabilizacja: kolejna lektura po zmianach, sprawdzenie CI, odbiór wizualny i audyt kontrolny.
