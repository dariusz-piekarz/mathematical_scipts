# RRC 16 — iteracja 284: trzecia lektura 013–024

Źródło: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Ponownie odczytano pełne dowody lem:pde16-cz-decomp, thm:pde16-weak11, lem:pde16-interp, thm:pde16-cz oraz rem:pde16-endpoints. Sprawdzono rzeczywiste hipotezy thm:pde7-approx-id, thm:pde8-density i thm:pde8-plancherel.

| Kryterium | Wynik kontroli |
|---|---|
| 013 | Półotwarta siatka dyadyczna: przeliczalność, zagnieżdżenie lub rozłączność, jedyny rodzic. Maksymalne złe kostki istnieją z ograniczenia średniej przez normę L¹ dzieloną przez objętość. Poprawne. |
| 014 | Słaby typ funkcji maksymalnej z rozłączności i sumowania całek; różniczkowanie średnich z gęstości testów i nierówności Czebyszewa, stała 4/tau oraz przeliczalna rodzina progów. Poprawne. |
| 015 | Średnie na złych kostkach między s i 2^d s, ograniczenie f poza ich sumą, g i b_k, zerowa całka b_k oraz oszacowania L¹ i L². Poprawne także dla danych zespolonych. |
| 016 | Zbieżność szeregu w L¹ i L² z rozłączności i Tonellego; topologiczny nośnik wybranego reprezentanta zawarty w domknięciu kostki. Poprawne. |
| 017 | Powiększenie kostek o współczynnik 3sqrt(d), miara E, oszacowanie części dobrej w L² i próg t/2. Poprawne. |
| 018 | Wygładzanie b_k w L¹ i L² o wspólnym zwartym nośniku; podciąg obrazów zbieżny prawie wszędzie; poza Q_k^* granica zwykłych całek dzięki dodatniej odległości od nośnika; odjęcie K(x-c_k) przez zerową średnią. Poprawne. |
| 019 | Geometria odcinka: |y-c_k|<=sqrt(d)ell_k/2 i |x-c_k|>=3sqrt(d)ell_k/2; odległość od zera >=2|x-c_k|/3. Całka radialna int r^{-2} dr pochłania ell_k. Poprawne. |
| 020 | Skończone sumy, zbieżność obrazów w L², podciąg i Fatou; rozkład zbioru poziomicowego na E oraz obie części z progiem t/2. Stała C_d niezależna od danych i progu. Poprawne. |
| 021 | Interpolacja: obie części obciętych danych należą do L¹∩L²; nierówność dla poziomu 2t, wzór warstwowy ważny również przy nieskończonej normie, Tonelli. Poprawne. |
| 022 | Całki t^{p-2} i t^{p-3} dają odpowiednio 1/(p-1) i 1/(2-p), czynnik p2^p; pominięcie f=0 uzasadnione. Jednoznaczność przedłużenia oraz zgodność na L²∩L^p przez wspólne obcięcia i podciąg. Poprawne. |
| 023 | Dualność dla p>2: samosprzężoność z rzeczywistego mnożnika, wcześniejsza przynależność obrazu testu do L^p dzięki zanikowi, funkcja normująca h_0 z poprawnym wykładnikiem i sprzężeniem, gęstość testów, jednoczesne przybliżenie w L² i L^p. Oszacowanie normy Frobeniusa Hessianu przez sumę składowych. Poprawne. |
| 024 | Kontrprzykład L¹: dodatni stożek, błąd O(r^{-d-1}), rozbieżność int dr/r, składowa mieszana bez korekty punktowej. Kontrprzykład L^infty w d=2: stała 1/pi, dodatni podsektor, dolne ograniczenie c r^{-2}, log(1/(4t)), istotna nieograniczoność dzięki ciągłości poza kwadratem i przeniesienie na gładkie dane przez zbieżność L¹. Poprawne. |

Nie wykryto nowych błędów ani luk wymagających zmiany źródła. Piąta kolejna czysta iteracja (280–284). Trzecia lektura 24/64. PDF i CI nadal niepotwierdzone. Następna iteracja 285: 025–032 — lokalizacja i oszacowania W^{2,p}.
