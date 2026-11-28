# Teoria miary / Miara i całka — rozdział 07, audyt I (iteracja globalna XXXII)

**Data:** 2026-11-23. **Wyłączna gałąź:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/07-konstrukcja-calki-lebesguea.tex.  
**Źródło przed audytem:** blob 55a0e8dda182f8368f74aeb531c2821df15f441a.  
**Źródło po poprawkach:** blob **783976ccc4d0c1ff02056e171233e2e70022f4f1**.

## 1. Punkt wznowienia, izolacja zakresu, standardy

Przed pracą odczytano najnowszą gałąź względem poprzedniego commitu ee7425ab0a22e0f78221c6fbc0c2e59635fc58b7. **Istniał już** raport audits/measure_theory/31-rozdzial-06-audyt-II-stabilizacja-2026-11-23.md (blob 331050f9c73290ae6a4e1935542ee889c795219f), utworzony przez inną iterację projektu po audycie XXX. Ten raport potwierdza, że **R06 jest STABILNY**, a rzeczywisty przebieg CI [45148448457](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148448457) zakończył się sukcesem 2/2 jobów. Dlatego nie powielano audytu R06: zgodnie z zasadą kolejności rozpoczęto **wyłącznie audyt R07**.

Pobrano AGENTS.md, docs/pl/standardy_terminologiczne.md, books/pl/measure_theory.tex i books/pl/integration_theory.tex (ostatni plik wyłącznie do ustalenia odrębności skryptu całkowego). Odczytano R01–R06 **tylko jako źródła wcześniejszych definicji i etykiet**; z R08 odczytano wyłącznie etykiety do sprawdzenia legalnego przyszłego odsyłacza. Nie audytowano ani nie edytowano R08–R31, nie dokonano scalania ani deduplikacji.

## 2. Szczegółowy audyt matematyczny

R07 po korektach ma **509 wierszy, 5 sekcji, 5 definicji, 2 lematy, 5 twierdzeń, 7 środowisk dowodu, 6 przykładów i 5 uwag**. Nie zawiera rysunku TikZ.

Przeanalizowano kolejno **wszystkie siedem dowodów**, ze szczególnym uwzględnieniem:
1. **Niezależność całki funkcji prostej od podziału:** wspólne rozdrobnienie, skończona addytywność i prawidłowa konwencja 0·∞=0. Pusta przestrzeń wymaga jawnej konwencji sumy pustej — dopisano.
2. **Monotoniczność, addytywność i jednorodność całki prostej:** wspólny podział na A_i∩B_j; kontrola przypadku miary nieskończonej bez odejmowania nieskończoności.
3. **Definicja całki nieujemnej przez supremum minorant:** niepustość rodziny, monotoniczność, skalowanie także przez zero, zgodność obu definicji dla funkcji prostej i zerowanie całki przy nośniku na zbiorze zerowym.
4. **Ograniczenie miary i całka po zbiorze:** równość supremów przez przedłużanie minorant zerem poza A i ograniczanie minorant do A.
5. **Nierówność Markowa:** minoranta a·χ_{f≥a}; wnioski o skończoności prawie wszędzie i całce zerowej.
6. **Niezmienniczość całki przy zmianie na zbiorze zerowym:** wycinanie nośnika z prostych minorant i odrębne porównanie części dodatnich i ujemnych.
7. **Absolutna całkowalność:** pełny argument obu implikacji bez użycia nieudowodnionej jeszcze ogólnej addytywności całki nieujemnej; rozcięcie na P={f≥0} oraz M={f<0} i niezależne supremum części prostych.

Wynik: **brak nowych wykazanych błędów** w tych twierdzeniach. Dwa istotne błędy wykryto natomiast w **przykładach** — opisane w kolejnej sekcji.

## 3. Wykazane błędy i poprawki źródła

Zmianę matematyczną oraz terminologiczną zapisano w commicie **[e5a53a7bfd6f0c98008da9f6e89d471d14324387](https://github.com/dariusz-piekarz/mathematical_scipts/commit/e5a53a7bfd6f0c98008da9f6e89d471d14324387)**:

1. **Miara dyskretna i wartości +∞ — luka dowodowa.** Dawny dowód utożsamiał częściową sumę ∑_{n≤N} f(n)w_n z całką funkcji prostej. Dla f(n)=+∞ funkcja ta nie jest jednak funkcją prostą w przyjętym znaczeniu, bo musi być skończenie wartościowana. Poprawiono dowód przez **s_{N,M}(n)=min(f(n),M)χ_{\{1,…,N\}}(n)** i przejście M→∞, następnie N→∞. Jawnie dopuszczono wagi w_n∈[0,∞] i zastosowano konwencję 0·∞=0. Argument obejmuje też nieskończone wartości funkcji i mas atomów.
2. **Fałszywe twierdzenie o rozłączności przedziałów.** Dawny podział na [-1,1], [n,n+1) i (−n−1,−n] miał wspólne punkty ±1. Zastąpiono środkowy przedział przez **(−1,1)**; wszystkie przedziały są teraz parami rozłączne i ich suma mnogościowa jest całą prostą, z osobnym określeniem przynależności punktów brzegowych.
3. **Przypadek X=∅:** w definicji całki funkcji prostej jawnie przyjęto listę wartości pustą i całkę równą pustej sumie 0, spójnie z doprecyzowaniem R06.
4. **Terminologia:** „sekwencji” zamieniono na **„ciągu”**.

Nie zmieniono żadnej etykiety, nie dodano niezatwierdzonego twierdzenia ani nie ruszano innych rozdziałów. Treść R07 po zapisie została ponownie pobrana; potwierdzony blob: **783976ccc4d0c1ff02056e171233e2e70022f4f1**.

## 4. Nowe niezależne regresje i historia realnego CI

Utworzono tools/test_measure_theory_ch07.py, commit **16249fd18a1b8e801a041b4e1d98ed0f6992c26d**. Pierwszy CI ujawnił *usterkę testu* odsyłaczy: skrypt zbierał etykiety jedynie z R01–R07, lecz R07 prawidłowo przywołuje etykietę ch:twierdzenia-graniczne z R08. Sprawdzono istnienie tej etykiety w źródle R08, po czym poprawiono skrypt, aby pobierał **wyłącznie etykiety R08 jako kontekst odsyłaczy**, commit **2660042df96ebfb6d51cf27a96a0b941d4953b9e**. To nie był błąd rozdziału R07; treść R08 pozostaje nietknięta. Ostateczny blob testu: **9000b7871a40103f4291cebb1850958f5a2473e0**.

Wdrożono osobny workflow .github/workflows/measure-theory-ch07.yml, commit **a0b4b9dcafb7994fc53bf5f6aeddd3a558ca70e2**, blob **03a0bc4c1fc0508a0059c393625e10c86a22bbbd**.

**Potwierdzony poprawiony przebieg CI:** [GitHub Actions 45150225228](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45150225228) na commicie 2660042df96ebfb6d51cf27a96a0b941d4953b9e. Oba joby **2/2 SUCCESS**, co sprawdzono przez API jobów, ich logi i pobrany artefakt.

Log testów zawiera dokładnie:
- **19683 PASS** skończonych modeli własności całki prostej i addytywności, w tym wagi nieskończone;
- **729 PASS** modeli dyskretnych z f(n)=+∞ i w_n∈[0,∞];
- **161 PASS** przypadków punktów granicznych rozłącznego rozkładu prostej, w tym ±1;
- **34 PASS** wymiernych oszacowań sum n/2 dla minorant funkcji 1/x;
- **PASS** kontroli plików źródłowych, terminologii, sparowania środowisk i **11 odsyłaczy R07**.

Skończone regresje nie zastępują ogólnych dowodów twierdzeń.

## 5. Pełny PDF i kompilacja całej książki

W tym samym CI wykonano **2 rzeczywiste kompilacje pdflatex izolowanego R07** (6 stron A4) oraz **3 kompilacje pełnej książki** (257 stron), bez wykrytych przez workflow nierozwiązanych referencji i przepełnionych wierszy. Poppler potwierdził **3172 wykryte słowa w granicach stron** oraz wygenerował **6/6 podglądów PNG**. Pobrano autentyczny artefakt CI **14805592865** do lokalnego środowiska i ponownie sprawdzono `pdfinfo` oraz komplet sześciu podglądów.

**Inspekcja wizualna:** obejrzano wszystkie 6 stron (strona tytułowa oraz pięć stron zawartości) w zbiorczym podglądzie. Nie widać uciętych wzorów, nakładających się napisów ani przeskakujących podpisów. R07 nie ma osobnego rysunku. Izolowany log nie wykazuje **Overfull hbox** ani **Underfull hbox**. Ostrzeżenia o brakujących w izolowanym rozdziale odsyłaczach są oczekiwane przy nieobecności innych rozdziałów i nie występują w złożonej książce.

Ponownie odczytano R07 oraz R01–R08 **wyłącznie jako kontekst etykiet**: **17 etykiet R07, 11 odsyłaczy, 0 nierozwiązanych celów, 0 powtórzonych etykiet w R01–R08, 0 niesparowanych środowisk**. W źródle R07 brak zakazanych notacji funkcji charakterystycznych i terminów „sekwencji”, „unia zbiorów”, „zbieżność zdominowana”. Stosowana jest wyłącznie notacja χ_A.

## 6. Stan stabilizacji

**R07 — NIESTABILNY / W TOKU STABILIZACJI.** Audyt I wykazał dwie usterki merytoryczne w przykładach, problem pustej przestrzeni i naruszenie terminologii. Wszystkie poprawiono; nowa wersja przeszła kompletne rzeczywiste CI i inspekcję sześciostronicowego PDF. Jednak zgodnie z nadrzędnym rygorem **po ostatniej zmianie musi nastąpić co najmniej jeden kolejny, niezależny, pełny i czysty audyt R07** (matematyczny, językowy i techniczny), zanim wolno nadać status STABILNY.

**R01–R06 — STABILNE**, jak potwierdzają dotychczasowe osobne raporty. **R08–R31 — nieaudytowane w tej iteracji.**

**Następny krok:** wyłącznie R07, audyt II (globalny XXXIII). Nie przechodzić do R08, dopóki stabilizacja R07 nie zostanie jawnie zatwierdzona.
