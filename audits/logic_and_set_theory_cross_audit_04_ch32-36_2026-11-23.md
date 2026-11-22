# Logika matematyczna i teoria mnogości — audyt przekrojowy 04: rozdziały 32–36

**Data:** 23 listopada 2026 r. (Europe/Warsaw).  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Zakres:** dowody o wymuszaniu, hipotezie continuum, modelach boolowskich i modelach symetrycznych, integralność odniesień, język i testy regresyjne. Nie dodano nowych zagadnień matematycznych.

## 1. Faktyczne źródła i wcześniejsza stabilność

Pobrano aktualne pięć plików rozdziałów, a także wcześniejsze końcowe audyty V/IV/V/XII/IV, które oznaczały rozdziały jako stabilne. Wykonano ponownie niezależne kontrole dowodów, zamiast traktować poprzednie werdykty jako wystarczające.

| Rozdział | Blob SHA | Wiersze | Etykiety | Odsyłacze |
|---|---|---:|---:|---:|
| 32 | 2ccb38c7877fed86607173dc316692039eeac295 | 766 | 33 | 11 |
| 33 | 515ad48d535730aa92c5ce640420e7f1eea7aebe | 1091 | 25 | 26 |
| 34 | a49d162f573d0d93054666eec646472e5cd8cd6c | 970 | 23 | 24 |
| 35 | 385d1e7b5763ec17b9cdd1e0c4a3cb9ffd29efa9 | 2406 | 28 | 34 |
| 36 | 6891b26609ccf77a0aaddc28653bb872f05a1701 | 938 | 21 | 27 |
| **Razem** | — | **6171** | **130** | **122** |

## 2. Audyt A: pojęcie wymuszania i lemat prawdy (32–33)

1. **Kierunek porządku:** q≤p oznacza silniejszy warunek. Zbadano definicję filtru, gęstości, zgodności i konsekwencje dla pojęć bez antysymetrii. Przy konstrukcji Rasiowej–Sikorskiego (32, wiersze 209–244) dobry porządek P wybiera następne warunki z danego zbioru gęstego; filtry M-generyczne nad przeliczalnym tranzytywnym M wybiera się zewnętrznie, bez wniosku G∈M.
2. **Nazwy:** przy interpretowaniu nazwy ranga każdej pierwszej współrzędnej maleje. Największy warunek pojawia się jawnie dopiero przy nazwach kanonicznych i nazwie filtru. Wstępne twierdzenie z rozdziału 32 mówi o tranzytywności i zawieraniu M oraz G, nie o ZFC w rozszerzeniu.
3. **Atomowe wymuszanie:** klauzule przynależności i równości z rozdziału 33 odwołują się do nazw o mniejszych rangach, kontrolowanych naturalną sumą rang. Przejście przez gęsty zbiór warunków w obu kierunkach atomowego lematu prawdy nie wymaga jeszcze ZFC w M[G].
4. **Negacja i egzystencja:** zbiór rozstrzygnięć D_φ należy do M przez lemat definiowalności. Dla egzystencji używa się tylko nazwy świadka z M, a nie zbioru wszystkich nazw. Lemat prawdy jest schematem dla każdej ustalonej formuły.
5. **ZFC w M[G] (33, wiersze 670–1014):** nazwy podzbiorów ograniczono do P(A_τ×P)^M. W zastępowaniu najpierw ogranicza się rangi minimalnych świadków przez zastępowanie na zbiorze J, potem stosuje AC do jednego zbioru kandydatów. W dowodzie wyboru wystarczy, że obraz mapy indeksowanej liczbą porządkową *zawiera* a=τ^G, nawet jeśli przyjmuje również inne wartości.

**Wynik A:** nie znaleziono w tych kontrolowanych zależnościach nowej nieuzasadnionej hipotezy ani błędnego koła.

## 3. Audyt B: dwie metody rozstrzygnięcia CH w rozszerzeniach (34)

1. **Lemat o systemie Δ i ccc:** ograniczenie do zbiorów o ustalonej skończonej mocy i wybranie podrodziny o wspólnym rdzeniu zapewnia zgodność dwóch warunków Add(ω,κ), gdy ich wartości na rdzeniu się zgadzają.
2. **Zachowanie liczb kardynalnych:** dla każdej współrzędnej hipotetycznej surjekcji β→λ maksymalny antyłańcuch rozstrzyga jej wartość. Ccc sprawia, że zbiór możliwych wartości na każdej współrzędnej jest przeliczalny. Ich suma dla β<λ ma moc mniejszą od nieprzeliczalnej liczby kardynalnej λ. Warunek dotyczący λ jest istotny i jawny.
3. **Dodanie wielu ciągów Cohena:** gęste zbiory D_{α,β} dają różne wiersze, a E_{α,x} daje nowość każdego wiersza wobec starego x. Przechodzi się od funkcji binarnych do podzbiorów ω przez jawne kodowanie, nie przez utożsamienie tych obiektów jako zbiorów.
4. **Przeliczalna domkniętość:** dla każdej nazwy ciągu wartości porządkowych konstruuje się domknięcie *poniżej dowolnego t≤p*, aby uzyskać gęstość warunków rozstrzygających cały ciąg. Rozstrzygające ciągi i wspólne wzmocnienie należą do M. Wniosek dotyczy braku nowych podzbiorów ω i zachowania ω_1, a nie wszystkich liczb kardynalnych.
5. **Kolaps:** Coll(ω_1,λ) składa się z funkcji częściowych o przeliczalnych w M dziedzinach. Ich suma w malejącym ciągu jest dolnym ograniczeniem. Gęste warunki dają surjekcję ω_1→λ i CH bez dodawania podzbiorów ω.
6. **Granica metamatematyczna:** wyniki rozdziału 34 są warunkowane istnieniem *przeliczalnego tranzytywnego modelu zbiorowego ZFC*. Nie wynikają w tej postaci z samej Con(ZFC).

**Wynik B:** nie wykryto zamiany ról ccc i domkniętości ani nieuzasadnionego przejścia od modelu tranzytywnego do dowolnego modelu ZFC.

## 4. Audyt C: pełna niesprzeczność względna za pomocą modeli boolowskich (35)

1. **Zupełna algebra i nazwy:** wartości kwantyfikatorów powstają jako kresy *zbiorów* wartości, a rangi świadków mają wspólne ograniczenia. Nie wprowadza się zbiorowego predykatu prawdy dla właściwej klasy.
2. **Mieszanie i lemat o pełności (wiersze 445–570):** maksymalny antyłańcuch lokalnie wybiera nazwy świadków, a po ograniczeniu rang i zbiorowym AC można je zmieszać. To konieczne: z przynależności supremum do ultrafiltru nie wynika istnienie składnika należącego do ultrafiltru.
3. **Iloraz przez dowolny ultrafiltr (1203–1405):** relacja równości nazw mod U jest równoważnością, a relacja przynależności nie zależy od reprezentantów. Egzystencjalny krok lematu prawdy wykorzystuje pełność. Nie wymaga generyczności U ani zewnętrznego dobrego ufundowania ilorazu.
4. **Przekład wymuszania porządkowego na boolowskie:** z i(t)≤i(p) wyprowadza się zgodność, nie automatycznie t≤p. Zgodność klauzul atomowych sprawdzana jest przez gęstość obrazów warunków i podstawianie równych nazw.
5. **CH i jej zaprzeczenie:** algebra RO(Add(ω,ω_2)) rozstrzyga negację CH, a RO(Coll(ω_1,2^{aleph_0})) rozstrzyga CH. Oba argumenty odnoszą się do wartości boolowskich równych 1 i są twierdzeniami ZFC, nie jedynie wynikami modelowymi przy silnym założeniu tranzytywności.
6. **Wniosek:** Con(ZFC) wraz z twierdzeniem o pełności daje zbiorowy model ZFC, z którego tworzy się dwa boolowskie ilorazy. Otrzymuje się osobno Con(ZFC+CH) i Con(ZFC+¬CH). Nie przypisuje się ZFC dowodu bezwarunkowej niesprzeczności.

**Wynik C:** sprawdzone przejścia od modeli do niesprzeczności względnej pozostają poprawnie rozdzielone.

## 5. Audyt D: symetria, ZF bez AC, rozróżnienie od AD (36)

1. **HS:** skończony nośnik zapewnia niezmienniczość nazw, ale klauzule egzystencji wymuszania ograniczają świadków do *dziedzicznie symetrycznych* nazw. Zwykła semantyka z M[G] bez tego ograniczenia byłaby niewłaściwa.
2. **Aksjomaty ZF:** wyróżnianie wykorzystuje nazwę ograniczoną do starej dziedziny τ i warunków P. W zbiorze potęgowym wszystkie nazwy rozważa się w P(D×P) i filtruje przez HS; nie stosuje się zbioru wszystkich nazw. Collection ogranicza rangi świadków w metateorii M, a wspólny nośnik parametrów gwarantuje symetrię wynikowej nazwy.
3. **Zbiór Dedekinda skończony:** jeżeli nazwa funkcji ma nośnik E, przypuszczenie, że przyjmuje wartość c_k dla k∉E, pozwala użyć transpozycji k z całkiem świeżym ℓ. Warunki r i πr są zgodne; wspólne wzmocnienie wymusiłoby c_k=c_ℓ, sprzecznie z gęstym rozdzielaniem wierszy. Nie zakłada się błędnie, że πr musi samo należeć do G.
4. **Niesprzeczność z modelu zewnętrznie źle ufundowanego:** dla przeliczalnego M⊨ZFC tworzy się zewnętrzny filtr M-generyczny i iloraz nazw HS. Lemat prawdy jest przenoszony dla standardowych formuł. Nie stosuje się kolapsu Mostowskiego do zewnętrznie nieufundowanej relacji.
5. **AC i AD:** z Con(ZF) i klasy L wynika Con(ZFC), a z konstrukcji symetrycznej Con(ZFC)⇒Con(ZF+¬AC). To uzasadnia warunkową niezależność AC od ZF. Sama negacja AC nie implikuje AD, co jest wyraźnie odnotowane w rozdziale 36.

**Wynik D:** brak nowej koniecznej korekty w analizowanych argumentach.

## 6. Kontrole źródeł, terminologii i odsyłaczy

- 130 różnych etykiet, brak powtórzeń pomiędzy pięcioma rozdziałami.
- 122 odsyłacze; wszystkie wewnętrzne cele istnieją.
- Jedyne zewnętrzne cele: ch:constructible z rozdziału 31 (blob 03dae2a901f115eacdff67058f96717f3323e4f8) i ch:determinacy z rozdziału 30 (blob 2f45abf617fb2f84fa01f1a0acf7db5c1de131fd), znalezione w rzeczywistych źródłach.
- Brak błędnie zagnieżdżonych lub niedomkniętych środowisk LaTeX.
- Brak skróconej nazwy rzeczownikowej „kardynał” w tekście pięciu rozdziałów.

Nie modyfikowano żadnego pliku źródłowego rozdziału 32–36.

## 7. Nowy test przekrojowy i weryfikacja

Dla ochrony krytycznych zależności dodano test tools/tests/test_logic_and_set_theory_cross_ch32_36.py, commit c150664b0c8f10d4ffd507f129764fcb42cda7fd. Zawiera **5 metod**:
1. kolejność importów i zgodność katalogu rozdziałów;
2. obecność 14 krytycznych odsyłaczy i ich docelowych etykiet;
3. brak duplikatów etykiet, poprawność środowisk i terminologię;
4. odrębność hipotezy istnienia przeliczalnego modelu tranzytywnego od Con(ZFC) i Con(ZF);
5. nieutożsamianie ccc z domkniętością ani ¬AC z AD.

W commicie fc11bf4dcf5123e510c376feb31a2df6fb17ac67 nowy plik podłączono do .github/workflows/logic-and-set-theory-chapter.yml; uruchomienie następuje wraz ze wszystkimi testami rozdziałowymi, kompilacją PDF i kontrolą ostrzeżeń zakładek.

[CI 45084816549](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45084816549) — przebieg kontrolny po zmianie workflow; jego wynik wymaga osobnego potwierdzenia po zakończeniu.

**Ograniczenie:** regresje tekstowe i sprawdzanie skończonych konfiguracji nie są matematycznymi dowodami twierdzeń o nieskończonych strukturach ani formalizacją Lean.

## 8. Werdykt

**Audyt merytoryczny i strukturalny czysty w skontrolowanym zakresie.** Źródła 32–36 zachowują status wcześniejszej stabilności. Dodatkowa kontrola zależności zostanie uznana za zakończoną po zielonym CI na commicie integrującym nową regresję. Nie dodano niezatwierdzonego materiału.
