# RRC 23 — iteracja 351

Pierwszy pełny audyt stabilizacyjny, odczyt 1327 wierszy we wszystkich ośmiu sekcjach. Commit 046a705f95b091024af477a4b0d0cf9947603d04, blob 0ad4d96ac73863b5d9231b6b4b408f5259cd9e25.

- Uzasadniono lokalną jednoznaczność rekonstrukcji charakterystyk w klasie C² aż do chwili 0; sprawdzono równanie gradientu i całkę działania. Uzupełniono własności metryki torusa i zwartość.
- W lemacie Legendre'a zastąpiono powołanie na ciągłość skończonych funkcji wypukłych bezpośrednim oszacowaniem przez jednostajną ograniczoność maksymalizatorów na kulach. Rozpisano nierówność stycznej H. Poprawiono wybór v=0 w oszacowaniu Hopfa–Laxa oraz kolejność uzasadnienia kontaktu testowego.
- Rozszerzono porównanie na całej R^d na nieograniczone globalnie lipschitzowskie pod- i nadrozwiązania: porządek początkowy oraz stałe Lipschitza w czasie i przestrzeni kontrolują u(t,x)-v(s,y) przez C_u t+C_v s+K_v|x-y|. Nierówność Younga pozostawia połowę kary przestrzennej, zapewniając lokalizację i zbieżność odległości. Tym samym jednoznaczność wzoru Hopfa–Laxa obejmuje także nieograniczone dane globalnie lipschitzowskie. Usunięto zbędną ograniczoność danych we wniosku o obszarze zależności.
- W dowodzie entropii poprawiono rzeczywistą nieścisłość: człon eta''(w_epsilon) ∂_x w_epsilon R_epsilon nie musi znikać. Jedynie jego ograniczenie z góry dąży do zera, co wystarcza do nierówności. Zapisano oszacowanie parowania z nieujemną funkcją testową.
- Dowiedziono ciągłości w całym [0,T] z wartościami w L¹_loc dla w=∂_x u: w dodatniej chwili zbieżność minimalizatorów wynika ze zwartości, ciągłości funkcji minimalizowanej i jednoznaczności minimalizatora w punkcie różniczkowalności; następnie zbieżność zmajoryzowana na przedziałach. Nie twierdzono globalnej całkowalności.
- Ponownie sprawdzono argument półwklęsłości, przykład cosinusa, lokalną entropię Krużkowa i początkowy ślad, regularność mieszaną równania lepkiego.

Kontrola zapisanego źródła: 1429 wierszy, 25 zachowanych unikatowych etykiet, 38 odsyłaczy (wszystkie jednoznaczne, cele zewnętrzne w rozdz. 2 i 24), brak błędów zagnieżdżenia i delimiterów. Pierwsze dedykowane CI 46031210962 SUCCESS. Nowe CI 46032675905 queued; aktualna kompilacja, kontrola wizualna i globalne CI niepotwierdzone.

Następny etap: drugi pełny audyt stabilizacyjny. W szczególności sprawdzić nowe porównanie nieograniczonych danych, oszacowanie dyssypacji i ciągłość czasową pochodnej. Rozważyć uzupełnienie rysunków charakterystyk i profilu w okolicy t=1.
