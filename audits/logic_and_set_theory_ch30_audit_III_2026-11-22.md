# Logika matematyczna i teoria mnogości — rozdział 30, audyt III

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`.

## Usunięcie niejawnego wyboru przeliczalnego z argumentu o mierzalnych/kategorialnych konsekwencjach AD

1. **Własność Baire'a w przestrzeni Baire'a.** W dowodzie `thm:ad-baire-property` przeliczalna suma zbiorów `[s]\A` pierwszej kategorii nie była formalnie uzasadniona w ZF. Dodano jawny odsyłacz do przywróconego Lematu `lem:ad-meager-countable-union`, który dowodzi tego kroku przy AD, wykorzystując kodowanie domkniętych zbiorów nigdziegęstych i wcześniejszy wynik o przeliczalnym wyborze dla zbiorów rzeczywistych.
2. **Brak dobrego uporządkowania całej prostej w ZF+AD.** W dowodzie `thm:ad-no-wellorder-reals` nie wystarcza stwierdzenie, że wszystkie wymierne przesunięcia mizernych zbiorów pozostają mizerne: ich przeliczalna suma w ZF może wymagać dodatkowego argumentu. Ustalono jedno świadectwo `V⊆⋃_n F_n`; wszystkie przesunięte świadectwa `F_n+q` mają jawny wspólny wzór i są indeksowane przez **już przeliczalny zbiór** `Q×ω`. Nie występuje nowy akt nieskończonego wyboru.
3. **Przestrzeń R jest drugiej kategorii już w ZF.** Zamiast przywoływać Twierdzenie Baire'a sformułowane wcześniej z DC (nie wolno zakładać DC bez dowodu przy AD), dodano niezależny konstrukcyjny argument. Z ciągu zbiorów nigdziegęstych wybieramy w kolejnych otwartych gęstych dopełnieniach **pierwszy** z ustalonej enumeracji dopuszczalny przedział o wymiernych końcach, którego domknięcie zawiera się w poprzednim; średnice dążą do 0. Zupełność R daje wspólny punkt poza wszystkimi zbiorami nigdziegęstymi. W ZF jest to jednoznaczna rekurencja.
4. **Drugi przypadek argumentu Vitaliego.** Rozpisano, dlaczego przy niepierwszokategorialnym V o własności Baire'a musi istnieć niepusty przedział I, na którym V jest współpierwszej kategorii: wystarczy otwarty zbiór O z `V△O` pierwszej kategorii i niepustość O.

**Wynik:** dowód nie korzysta już z niedeklarowanego DC ani AC. Dodano kontrole regresyjne dla racjonalnych przedziałów i odwołania do lematu o przeliczalnej sumie zbiorów pierwszej kategorii.

**Stan tekstu:** 12 definicji, 7 przykładów, 15 twierdzeń, 9 lematów, 4 wnioski, 15 uwag, 26 dowodów, 1 rysunek, 57 etykiet, 46 odsyłaczy. Do audytu IV i pełnego CI.
