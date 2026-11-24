# Analiza funkcjonalna — 15B/04 — pierwszy czysty audyt po poprawkach

**Data:** 24 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (ta sama istniejąca gałąź).  
**Źródło:** `chapters/pl/functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex`.  
**SHA źródła:** `9739c713fd978e14623b96e3fea6c981fa81ca97`.  
**SHA testu:** `a1d3dac82e31cf85ea7f5d5ece538a559f3425dc`.  
**Werdykt merytoryczny:** **pierwszy niezależny czysty audyt (1/2)** po poprawkowej iteracji 15B/03. Brak nowych zmian w tekście twierdzeń, przykładach i testach. Końcową walidację CI po zapisie tego raportu należy potwierdzić osobno.

## Kontrola wejściowa: niezmieniona wersja 15B po audycie 15B/03

Pobrano bezpośrednio bieżący plik źródłowy (582 wiersze), pięć testów regresyjnych i raport 15B/03. Zaistniałe w 15B/03 poprawki dotyczą jednoznacznej identyfikacji przekrojów wektorowej funkcji mierzalnej na produkcie z miarą uzupełnioną, kolejności ustalania silnej mierzalności przed zastosowaniem Tonellego oraz błędnego jednokrotnego zużycia generatora `weighted` w teście Fubiniego. Rzeczywisty wynik sumy produktowej po naprawie w obu współrzędnych sprawdzono niezależnie, w arytmetyce dokładnej: `(-53/210,61/50)`. Obecny test wymusza ten wynik niezależnie od zgodności dwóch kolejności całkowania. Nie powtarzano pracy audytu poprawkowego jako „czystego”.

## 11 dowodów: samodzielna kontrola matematyczna

1. **Twierdzenie Pettisa o mierzalności.** Dla istotnie ośrodkowego obrazu Y dobór funkcjonałów normujących gęsty ciąg jednostkowy zapewnia `||y||=sup_k|ell_k(y)|`; przy Y={0} wystarczy funkcjonał zerowy. Mierzalność norm odległości `||f-y_j||` pozwala wybrać pierwszy przybliżający punkt. Obcięcie przeliczalnych wartości do funkcji prostych z błędem miary `2^{-n}` i lemat Borela–Cantellego zapewniają zbieżność prawie wszędzie, nie tylko w mierze.
2. **Kryterium całkowalności Bochnera.** Dla funkcji silnie mierzalnej z normą całkowalną, obcięcie przybliżeń `u_n` warunkiem `||u_n||<=2||f||` daje funkcje proste `s_n` z dominacją `||s_n-f||<=3||f||` oraz zbieżnością punktową prawie wszędzie. Skalarne twierdzenie o zbieżności zmajoryzowanej daje zbieżność w `L^1(S;X)`. Niezależność całki od przybliżeń oraz przemienność z operatorem ciągłym wynikają z oszacowania normowego.
3. **Zbieżność zmajoryzowana Bochnera.** Wybór jednego przybliżenia prostego dla `f_n` o wyjątkowym zbiorze miary mniejszej od `2^{-n}` jest możliwy dla miary skończonej. Lemat Borela–Cantellego gwarantuje zbieżność prostych do f poza wspólnym zbiorem miary zero. Norma granicy i różnic są zdominowane odpowiednio przez g i 2g.
4. **Fubini Bochnera.** Poprawiony dowód najpierw zastępuje z dokładnością do zbioru miary produktowej zero przedstawiciela mierzalnego względem uzupełnienia przedstawicielem produktowo mierzalnym. Przekroje zbioru wyjątkowego są zerowe dla prawie wszystkich parametrów. Silna mierzalność przekrojów wynika z punktowej granicy funkcji prostych, po której skalarne Tonelli daje całkowalność norm. Prostokątne `g_n` z błędem `L^1<4^{-n}` mają sumowalne błędy przekrojów; otrzymane `F_n(s)=int_T g_n(s,t)` są proste, a `F_n->F` prawie wszędzie. Dopiero po ustaleniu mierzalności F stosuje się Tonellego do `||F-F_n||`, uzyskuje zbieżność w `L^1` i identyfikuje obie całki iterowane. Wszystkie warunki dotyczą prawie wszystkich przekrojów, nie wszystkich.
5. **Zgodność Riemann–Bochner.** Ciągłość na zwartym odcinku zapewnia jednostajną aproksymację funkcjami prostymi na przedziałach, więc granice sum Riemanna i całek Bochnera są identyczne. `chi_{Q cap [0,1]}x_0` przy `x_0!=0` ma całkę Bochnera równą zeru, lecz nie ma całki Riemanna w sensie wszystkich drobnych podziałów z punktami pośrednimi.
6. **Całka Dunforda.** Dla `Q_f:X'->L^1` wykres jest domknięty: zbieżność normowa `x_n'->x'` daje punktową zbieżność skalaryzacji, zaś zbieżność w `L^1` ma podciąg zbieżny prawie wszędzie. Twierdzenie o wykresie domkniętym daje normowe ograniczenie Q; funkcjonał `D_A` jest więc elementem `X''`.
7. **Hierarchia całek.** Liniowy funkcjonał `x'` przenosi całkę Bochnera na całkę skalarną przez `L^1`-aproksymację, więc Bochner implikuje Pettisa i Dunforda. Reprezentowalność wszystkich `D_A` w `J_X(X)` jest dokładnym warunkiem Pettisa; wymagane są wszystkie A, a nie tylko S.
8. **Zbieżność zmajoryzowana Pettisa.** Refleksywność daje reprezentację całki Dunforda w X, bez przypisywania silnej mierzalności f. Mierzalność `||f_n-f||` jest założona jawnie; oszacowanie normy różnicy całek przez `int_A||f_n-f||` i skalarne DCT kończą dowód.
9. **Całka Gelfanda.** Wykres `Q:Y->L^1` jest domknięty z tego samego powodu co w przypadku Dunforda; otrzymuje się element `Y'`. Dla rozłącznych A_n addytywność skalarna po każdym y daje addytywność w topologii `sigma(Y',Y)`, bez nieuprawnionego wniosku o zbieżności normowej.
10. **Wariacja miary wektorowej.** Dla `|m|(union A_n)>=sum |m|(A_n)` zestawia się przybliżające partycje skończenie wielu A_n i dodaje resztę. Odwrotna nierówność wynika dla każdej skończonej partycji sumy z normowej addytywności m i nierówności trójkąta dla sum szeregu; supremum po partycjach daje równość także przy nieskończonej wariacji.
11. **Miara generowana przez Bochnera.** Oszacowanie ogona normą całki zapewnia przeliczalną addytywność w X. Dla funkcji prostych partycja po zbiorach poziomicowych daje `|m_f|(A)=int_A||f||`; dla ogólnych funkcji nierówność różnicy wariacji `<=int_A||f-f_n||` pozwala przejść do granicy w `L^1`.

**Wynik: wszystkie 11 dowodów skontrolowano ponownie; brak nowej usterki wymagającej zmian w źródle.**

## Cztery przykłady i kontrole graniczne

- **Dunford, nie Pettis, w `c_0`.** Przy masach atomów `2^{-n}` i wartościach `2^ne_n`, skalaryzacje dla każdego `a in ell^1` są całkowalne, lecz `D_S=(1,1,...) in ell^infty\setminus c_0`. Integralność normy zawodzi, zgodnie z hierarchią.
- **Pettis, nie Bochner, w `ell^2([0,1])`.** Każdy element ma co najwyżej przeliczalny nośnik, zatem funkcja `t->e_t` ma wszystkie skalaryzacje równe zero prawie wszędzie. Obraz poza zbiorem zerowym jest nieprzeliczalną rodziną punktów parami odległych o `sqrt2`, więc nie jest istotnie ośrodkowo-wartościowa.
- **Gelfand bez normowej addytywności.** Dla `Y=ell^1`, `Y'=ell^infty` i wskazanych atomów, `g_A=chi_A`; ogony mają normę 1, chociaż dążą słabo-* do 0.
- **Brak RNP dla `C([0,1])`.** Miara `m(A)(t)=mu(A cap [0,t])` ma normę i całkowitą wariację `mu(A)`. Założona pochodna Bochnera prowadzi, po jednoczesnym wyeliminowaniu zbiorów miary zero dla wszystkich wymiernych q, do niemożliwej ciągłej funkcji, której wartości na zbiorze gęstym mają skok w s.

**Wynik: 4/4 przykłady matematycznie poprawne.** Testy skończenie atomowe są regresjami, nie formalizacjami twierdzeń dla wszystkich przestrzeni.

## Redakcja, odsyłacze i stan techniczny

Bezpośrednio na aktualnym źródle: **582 wiersze, 23 etykiety, 23 unikatowe**, wszystkie 11 środowisk `proof` sparowane, 9 `twierdzenie`, 2 `stwierdzenie`, 6 `definicja`, 4 `przyklad`, 3 `uwaga`. Cztery odwołania lub odsyłacze wskazują na istniejące etykiety 15A, 15B i 16 (część w komentarzach źródła). Notacja `X'` i `X''` jest określona jako przestrzeń sprzężona i podwójnie sprzężona, funkcje charakterystyczne zapisywane są `\chi_A`. W bieżącym module nie ma ilustracji TikZ wymagających oceny graficznej.

Weryfikacja dedykowanej bramki [#45304359300](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45304359300) dla poprzedniego raportu 15B/03 była **w toku** podczas pisania bieżącego audytu: testy i przygotowanie kontekstu 01–17 były już zakończone powodzeniem, lecz kompilacja i końcowa walidacja wymagały potwierdzenia. Nie przedstawiam statusu `in_progress` jako `success`. Skontrolowane w 15B/02 starsze 110 stron PDF pochodziły z innego bloba źródła, więc nie zastępują walidacji nowej wersji 15B/03.

## Decyzja i dalsze kroki

**15B/04 — pierwszy niezależny czysty audyt matematyczny po poprawkowym 15B/03 (1/2).** Źródło `9739c713fd978e14623b96e3fea6c981fa81ca97` i test `a1d3dac82e31cf85ea7f5d5ece538a559f3425dc` pozostały niezmienione w tej iteracji. Do nadania statusu STABILNY wymagany jest jeszcze drugi czysty niezależny audyt 15B/05 oraz zakończony zielony workflow dla niezmienionych blobów z kontrolą rzeczywistego PDF. Dopiero wtedy można przejść do rozdziału 16.

## Walidacja rzeczywistego PDF aktualnych blobów

Pobrano artefakt `functional-analysis-ch15b-pdf` (ID **14880785447**) z zakończonego sukcesem workflow [#45304322170](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45304322170), uruchomionego na commicie `de80bf3f05c4125177128ece01f9b3ab4688b268`. Wprost ponownie pobrano bloby źródła i testu **z tego commitu**, a nie tylko z ruchomej gałęzi: są identyczne z bieżącymi blobami `9739c713fd978e14623b96e3fea6c981fa81ca97` i `a1d3dac82e31cf85ea7f5d5ece538a559f3425dc`. Nie porównywano z poprzednim PDF ze starej wersji 15B/02.

Po rozpakowaniu rzeczywistego archiwum i odczytaniu `pdfinfo`: **110 stron, A4, dokument niezaszyfrowany, pdfTeX**. Wyrenderowano strony **95–100** i oceniono ich zbiorczy podgląd; cały moduł 15B jest czytelny, a zaktualizowany dowód Fubiniego i stwierdzenie o wariacji są obecne. Nie stwierdzono obciętych wzorów, nachodzących fragmentów tekstu ani widocznych uszkodzeń glifów. Sprawdzenie rzeczywistego logu: **0** wystąpień `Overfull \\hbox`, `Undefined control sequence`, `There were undefined references`, `Missing character` oraz `LaTeX Warning:`; **1** wystąpienie `Underfull \\hbox` (wiersze 336–342 rozdziału 16, poza 15B). Wersja CI po raporcie 15B/03, [#45304359300](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45304359300), również ma potwierdzony status **completed/success**.

**Ocena 15B/04 nie zmienia się:** matematycznie/redakcyjnie **czysty (1/2)**; bramka PDF dla tych samych blobów **zielona**. Dedykowany nowy przebieg CI wywołany zapisem 15B/04 pozostaje do osobnego potwierdzenia i nie może być uznany za zakończony przed sprawdzeniem. Do stabilizacji wymagany jest jeszcze 15B/05, drugi czysty przegląd.
