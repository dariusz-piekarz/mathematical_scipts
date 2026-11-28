# RRC 17 — iteracja 299: pierwszy audyt stabilizacyjny

Ponowna lektura dowodów po audytach 296–298. Commit źródła a794ff8da65469156c164e1e248372147890194f.

- Doprecyzowano rzeczywisty charakter rozwiązań i regułę łańcuchową dla obcięć; dodano odsyłacz do rozdziału 9.
- Uzupełniono oszacowanie Sobolewa w iteracji De Giorgiego (w d=2 użycie p=4/3 i nierówności Höldera), regułę Leibniza i jednolitą kontrolę na kuli B_2; iteracja Mosera korzysta z tego samego oszacowania.
- Rozpisano energię logarytmu z pełnymi miarami i stałymi, skalowanie Poincarégo z odsyłaczem do rozdziału 10 oraz zależność stałej od ilorazu eliptyczności.
- W lemacie Johna–Nirenberga oddzielono M=0, uzasadniono przejście od generacji kostek do ogona wykładniczego i całkowanie ogona przez Tonellego.
- Poprawiono wybór odcięcia w oszacowaniu średniej oscylacji na dużych kulach.

Kontrola źródła: 895 wierszy, 36 etykiet zachowanych, 40 wystąpień odsyłaczy; wszystkie cele istnieją i są jednoznaczne w źródle oraz rozdziałach 9, 10, 14–16; brak niezgodności begin/end.

Dedykowany workflow rozdziału 17 dodano w commicie b31abec2bc6a310fefd90e9de803670d8f7af54a na podstawie działającego workflow rozdziału 16. Kontroluje etykiety, manifest, preambułę, rzeczywistą numerację odsyłaczy zewnętrznych, kompilację i diagnostykę PDF, renderuje strony oraz publikuje artefakt. Pierwszy run 45978707543 ma status queued. Nie potwierdzono jeszcze kompilacji, końcowego logu ani wyglądu stron. Rozdział nie jest ustabilizowany.

Następny etap: drugi audyt stabilizacyjny (w szczególności geometria pokrycia, zbieżność iteracji i reprezentant), odbiór dedykowanego CI, korekta usterek typograficznych, a po stabilizacji niezależny audyt kontrolny.
