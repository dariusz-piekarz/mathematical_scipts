# Topologia ogólna — globalny audyt 19: wszystkie dziesięć dowodów rozdziału 17

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zamrożony punkt odniesienia:** commit `3cd34225ef8a597974899801f97b4dac768c3b25`.
**Aktualny przy audycie blob źródła:** `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4`.
**Ścieżka:** `chapters/pl/general_topology/17-uzwarcenia-aleksandrowa-i-cecha-stonea.tex`.
**Zakres:** odrębna kontrola **10/10** środowisk `proof`, a także przykładów, aksjomatów, przypadków granicznych i zależności. Przeczytano aktualny pełny tekst TeX i raporty 17/02–03, lecz sam wynik poniżej wynika z ponownego przejścia argumentów, a nie z przejęcia starszego werdyktu. W tej iteracji źródła matematycznego nie zmieniono.

## I. Sprawdzenie każdego dowodu

1. **`lem:topog-uzwarcenia-aleksandrow-topologia` — topologia, zwartość i gęstość.** Dla niezwartej przestrzeni Hausdorffa \(X\) skończone przecięcia otoczeń nowego punktu są dopełnieniami skończonych sum zwartych podzbiorów \(X\). Dowolna *niepusta* suma takich otoczeń ma dopełnienie będące przecięciem zwartych \(C_i\); w przestrzeni Hausdorffa \(C_i\) są domknięte, więc przecięcie jest domkniętym podzbiorem jednego \(C_{i_0}\), a zatem zwartym. Pusta rodzina daje zbiór pusty, jawnie należący do topologii. Przypadki mieszane dają \(U\setminus C\) i dopełnienie \(C\setminus U\); w pierwszym użyto domkniętości \(C\), w drugim domkniętości \(C\setminus U\) w zwartym \(C\). Otwarte podzbiory \(X\) pozostają otwarte i wyznaczają topologię podprzestrzeni. Z pokrycia \(X^*\) bierzemy otoczenie \(\infty\), którego dopełnienie jest zwarte i ma skończone podpokrycie. Niezwartość \(X\) wyklucza izolowany punkt \(\infty\), co daje gęstość. **PASS.**

2. **`thm:topog-uzwarcenia-aleksandrow-kryterium` — dokładne kryterium Hausdorffowości.** Niezwartość i Hausdorffowość \(X\) są jawne. Jeśli \(X\) jest lokalnie zwarta, wzięcie otwartego \(U\ni x\) o zwartym domknięciu \(C\) umożliwia oddzielenie \(x\) od \(\infty\) przez \(U\) i \(X^*\setminus C\). Dwa punkty \(X\) oddziela pierwotna Hausdorffowość. Jeśli \(X^*\) jest Hausdorffa, jego zwartość z lematu 1 oraz otwartość \(X\subseteq X^*\) pozwalają skorzystać z wcześniejszego twierdzenia o dziedziczeniu zwartości lokalnej przez otwarte podprzestrzenie. Samo bycie Hausdorffa bez lokalnej zwartości nie zostało pomylone z warunkiem wystarczającym. **PASS.**

3. **`thm:topog-uzwarcenia-aleksandrow-proper` — właściwość i przedłużenie.** Dla niezwartych, lokalnie zwartych Hausdorffa \(X,Y\) wartości na \(X\) i \(\infty_X\) wyznaczają jedyną mapę zbiorów. Przeciwobrazy otwartych \(V\subseteq Y\) to \(f^{-1}(V)\), otwarte także w \(X^*\); przeciwobrazy \(Y^*\setminus C\), gdzie \(C\subseteq Y\) zwarty, to \(X^*\setminus f^{-1}(C)\), otwarte dokładnie przy właściwości \(f\). W odwrotną stronę \(C\) jest domknięty w Hausdorffowym \(Y^*\), więc \((f^*)^{-1}(C)\) jest zwartym, domkniętym podzbiorem \(X^*\) i nie zawiera \(\infty_X\). W topologii podprzestrzeni jest zwarty także jako podzbiór \(X\). Zachowano warunek \(f^*(\infty_X)=\infty_Y\), bez którego równoważność byłaby nieprawdziwa. **PASS.**

4. **`thm:topog-uzwarcenia-aleksandrow-minimalne` — minimalność.** Przy ustalonym \(x\in X\) i otwartym \(U\ni x\) o zwartym domknięciu \(C\), otwarty w \(K\) zbiór \(O\) z \(O\cap e(X)=e(U)\) spełnia \(O\subseteq\overline{e(U)}^{K}\), ponieważ \(e(X)\) jest gęsty *w całym \(K\)*. Ponieważ \(e(C)\) jest zwarty i \(K\) Hausdorffa, jest domknięty, a zatem \(O\subseteq e(C)\subseteq e(X)\). To wystarcza do otwartości \(e(X)\), nie jedynie jego lokalnej zwartości względnej. Reszta \(F=K\setminus e(X)\) jest zwarta i niepusta (w przeciwnym razie \(X\) byłaby zwarta). Mapa \(p(e(x))=x,\ p(F)=\{\infty\}\) jest ciągła, bo \(p^{-1}(V)=e(V)\) dla otwartych \(V\subseteq X\) oraz \(p^{-1}(X^*\setminus C)=K\setminus e(C)\) dla zwartych \(C\subseteq X\). Obraz jest całym \(X^*\). Gęstość i Hausdorffowość dają jednoznaczność. Kierunek porządku to \((X^*,\iota)\preccurlyeq(K,e)\), nie odwrotny. **PASS.**

5. **`cor:topog-uzwarcenia-aleksandrow-jednoznacznosc` — jednopunktowa reszta.** Otrzymana wyżej surjekcja jest iniektywna na \(e(X)\), a jedyny punkt reszty musi iść na \(\infty\). Jest więc bijekcją; ciągła bijekcja zwartej przestrzeni na Hausdorffa jest homeomorfizmem zgodnym z zanurzeniami. Nie ma ukrytego założenia, że *dowolne* dwa uzwarcenia są homeomorficzne. **PASS.**

6. **`lem:topog-uzwarcenia-lokalna-tych` — lokalna zwartość Hausdorffa daje Tychonoffa.** Dla domkniętego \(F\) i \(x\notin F\) silniejszy lemat o zwężaniu z rozdziału 14 daje \(x\in W\subseteq C=\overline W^X\subseteq X\setminus F\), gdzie \(C\) jest zwarty. W \(C\), zwartej Hausdorffa, zbiory \(\{x\}\) i \(C\setminus W\) są domknięte i rozłączne. Urysohn daje \(g(x)=1\), \(g|_{C\setminus W}=0\). Funkcje \(g\) na \(C\) oraz zero na \(X\setminus W\) sklejają się na dwóch domkniętych zbiorach, których sumą jest \(X\), i zgadzają się na przecięciu. Wynik \(1-h\) oddziela \(x\) od \(F\). Hausdorffowość daje osobno \(T_1\). Sprawdzono treść i dowód `lem:topog-baire-zwarte-domkniecie` w aktualnym rozdziale 14. **PASS.**

7. **`thm:topog-uzwarcenia-cech-stone-uniwersalne` — uniwersalność \(\beta X\).** Z rozdziału 07 \(\beta X\) jest domknięciem obrazu \(e_X:X\to[0,1]^{I}\), \(I=C(X,[0,1])\). Dla \(f:X\to L\) do zwartej Hausdorffa \(L\), \(\Phi(z)_g=z_{g\circ f}\) jest dobrze określone, bo \(g\circ f\in I\) dla \(g\in J=C(L,[0,1])\). Wszystkie współrzędne są ciągłe, więc \(\Phi\) jest ciągła do kostki. Dla \(e_X(x)\) wartości to \(e_L(f(x))\). Obraz \(e_L(L)\) jest domknięty jako zwarty podzbiór przestrzeni Hausdorffa, a gęstość \(e_X(X)\) wymusza \(\Phi(\beta X)\subseteq e_L(L)\). Złożenie z ciągłą odwrotnością zanurzenia \(e_L\) daje mapę \(\beta X\to L\), nie tylko do kostki. Dwie takie mapy są zgodne na gęstym obrazie w Hausdorffa \(L\), więc są równe. Dla \(X=\varnothing\) \(\beta X=\varnothing\) i wniosek pozostaje prawdziwy (istniejące \(f\) wymusza dopuszczalny przypadek). **PASS.**

8. **`cor:topog-uzwarcenia-cech-stone-funkcje` — funkcje rzeczywiste ograniczone.** Z ograniczoności obrazu wynika istnienie \(a\le b\) z \(f(X)\subseteq[a,b]\), także w przypadku stałym \(a=b\). Przedział jest zwarty Hausdorffa, więc uniwersalność daje przedłużenie do \([a,b]\), a włączenie do \(\mathbb R\) daje żądaną funkcję. Jednoznaczność map do Hausdorffa \(\mathbb R\) wynika z gęstości. **PASS.**

9. **`thm:topog-uzwarcenia-cech-stone-maksymalne` — maksymalność i kryterium równoważności.** Uniwersalność dla \(e:X\to K\) daje jedyne zgodne \(p:\beta X\to K\); jego obraz jest zwarty, domknięty w \(K\) i zawiera gęste \(e(X)\), zatem jest surjektywny. Jeśli uzwarcenia są równoważne, przedłużenia współrzędnych przechodzą przez odwrotny homeomorfizm. I odwrotnie: dla \(F_f:K\to[0,1]\) równość \(F_f\circ p=\pi_f|_{\beta X}\) jest uzasadniona przez zgodność na gęstym \(e_X(X)\). Gdy \(p(z)=p(w)\), równe są wszystkie współrzędne punktów \(z,w\in[0,1]^I\), zatem \(z=w\). Surjektywne \(p\) jest więc bijekcją z kompaktu do przestrzeni Hausdorffa i homeomorfizmem. Odwołanie do \(\pi_f\) jest poprawnie poprzedzone jego definicją. **PASS.**

10. **`cor:topog-uzwarcenia-krance` — krańce porządku.** Dla niezwartych lokalnie zwartych Hausdorffa \(X\) lemat 6 daje Tychonoffa, więc obie konstrukcje istnieją jako uzwarcenia. Z dowodów 4 i 9 wynika \((X^*,\iota)\preccurlyeq(K,e)\preccurlyeq(\beta X,e_X)\), zgodnie z kierunkiem relacji z rozdziału 16. **PASS.**

## II. Przykłady, redakcja, oznaczenia i granice

- Przykład \(\mathbb R\to S^1\setminus\{1\}\), \(e(t)=\exp(i(2\arctan t+\pi))\): granice przy \(t\to-\infty\) i \(t\to+\infty\) wynoszą \(1\), więc mapę można przedłużyć o \(\infty\) i sprawdzić ciągłość otoczeniem \(X^*\setminus[-M,M]\). Bijekcja jest homeomorfizmem dzięki zwartości i Hausdorffowości. Bez dopisania zachowania w *obu* krańcach nie byłoby pełnego dowodu ciągłości w dodanym punkcie; w źródle oba są jawne.
- Dla dyskretnej \(\mathbb N\) uzwarcenie \(\{0\}\cup\{1/n\}\) jest jednopunktowe i równoważne Aleksandrowowi; funkcja naprzemienna nie ma do niego przedłużenia, ale ma przedłużenie do \(\beta\mathbb N\). Przykład jest zgodny z kryterium maksymalności.
- Definicja konstrukcji Aleksandrowa dla niezwartej Hausdorffa \(X\) nie obiecuje Hausdorffowości \(X^*\) bez lokalnej zwartości; te dwa poziomy są konsekwentnie rozdzielone.
- Zachowano uzgodnione nazwy „uzwarcenie”, „uzwarcenie Aleksandrowa” i „uzwarcenie Čecha--Stone'a”. Nie dopisano nieuzgodnionych twierdzeń ani nie zmieniono etykiet. W źródle 17 nie ma środowisk `figure`, więc nie ma nowych rysunków do inspekcji.

## III. Weryfikacja źródeł zależnych, testów i CI

- **Bloby zależności:** rozdział 14 `24ca61f0e19fe6674719fc76e53073aa82cc755c` — lemat o otwartych otoczeniach o zwartym domknięciu oraz dziedziczenie zwartości lokalnej przez podprzestrzenie otwarte; rozdział 07 `0c31028e8fd301d805781b676c6713a2572501cf` — zanurzenie w kostkę i jego zwarta otoczka. Rozdział 16 `1c2fcb925d62120feaea468400e48842a508a062` ustala porządek na klasach uzwarceń. Wszystkie wyniki występują *wcześniej* niż 17.
- **Regresja:** odczytano istniejący `tools/tests/test_general_topology_ch17.py`, blob `f9c3cbedce1157a67c360251b1616c4310389023`. Zawiera m.in. 64 skończone modele dopełnień otoczeń, profile charakterystyczne w skończonym modelu \(\beta X\), kontrolę założeń tekstowych, etykiet i odsyłaczy. Testy modeli skończonych nie stanowią dowodu uniwersalności dla dowolnego \(X\).
- **Poprzedni aktualny CI:** [GitHub Actions 45082314478](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45082314478), commit `ef71d9d89f4b482f5de371be1c9241b3fc4a507d`, stan `completed/success`. Zweryfikowano przez GitHub API kroki joba `137392991159`: `Verify Chapter 17 Aleksandrow and Cech-Stone compactifications`, `Build complete book PDF`, `Build standalone Chapter 17 PDF` oraz `Check PDF and LaTeX log` — wszystkie `success`. Odczytany na tym commicie blob rozdziału 17 to **identyczny** `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4`. Audyt 17/02–03 dokumentuje również odrębny udany przebieg [45014196221](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014196221), obejrzenie wszystkich pięciu stron rozdziału i kontrolę logu.
- **Zastrzeżenie:** w tej iteracji nie pobierano i nie oglądano ponownie PDF ani nie uruchamiano ręcznie kompilacji. Po zapisaniu raportu należy zweryfikować nowe CI; samo rozpoczęcie workflow nie jest wynikiem PASS.

## IV. Nowy rejestr liczby dowodów — dokładny zakres 01–23

Wykonano ponowny rzeczywisty odczyt **wszystkich 23** plików rozdziałów na jednym, zamrożonym commicie `3cd34225ef8a597974899801f97b4dac768c3b25`, licząc dosłownie środowiska `\\begin{proof}` i `\\begin{figure}`.

| Rozdziały | Liczba dowodów |
| --- | ---: |
| 01–12 | 166 |
| 13 | 9 |
| 14 | 7 |
| 15 | 7 |
| 16 | 7 |
| 17 | 10 |
| 18 | 9 |
| 19 | 9 |
| 20 | 11 |
| 21 | 15 |
| 22 | 11 |
| 23 | 20 |
| **Razem 01–23** | **281** |

**Ważne:** historyczna liczba 261 z audytu globalnego 01 odnosiła się do ówczesnych 22 rozdziałów, nie do aktualnego zakresu 01–23. W ramach 01–23 są **24 ilustracje** (21 z rozdziałów 01–12 i po jednej w rozdziałach 21–23). Historyczny audyt wydania 188-stronicowego potwierdza **27** ilustracji w pełnym tomie 01–26, a trzy dodatkowe są w rozdziałach 24–26. Nie mieszać tych zakresów. Zmiana liczby dowodów nie oznacza, że wszystkie 281 otrzymały nowy indywidualny audyt.

**Uwaga do kolejnych kontroli:** starszy globalny raport 09 podaje dla rozdziału 13 blob `33200912c034f3f946909f00b9e4068deeca4ed0`, podczas gdy zamrożony aktualny odczyt wykazał `c9078636452731e42a56196e84b5ed9831120e6b`. Audyty 13 należy sprawdzić na tym obecnym blobie przed finalnym zamknięciem; nie przenosić bez sprawdzenia statusu między wersjami.

## V. Werdykt i pozostałe prace

**PASS matematyczny: 10/10 dowodów rozdziału 17 na wskazanym blobie.** Weryfikacja opiera się na samodzielnej kontroli każdego argumentu i aktualnych źródeł zależnych. Źródła pozostawiono bez zmian, zachowując wcześniejsze 2+1 udokumentowanych audytów stabilizacyjnych. Zapisanie tego raportu usuwa brakujący wpis globalnego rejestru pełnych kontroli rozdziału 17, **nie oznacza jednak globalnego PASS 01–23**.

Otwarte: osobno pełne kontrole dowodów kolejnych rozdziałów (w pierwszej kolejności 18, 9 dowodów), uzgodnienie wersji źródła 13, przegląd audytów wszystkich 281 dowodów na aktualnych blobach, końcowa walidacja CI i inspekcja wydania przy niezmienionych źródłach.

**Następny krok:** globalny audyt 20 — niezależna weryfikacja 9/9 dowodów rozdziału 18 (topologia zwarto-otwarta, ewaluacja, prawo wykładnicze, metryzacja i zupełność). Automatyzacja pozostaje aktywna.
