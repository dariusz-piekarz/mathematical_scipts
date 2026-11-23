# Teoria miary / Miara i całka — rozdział 08, audyt I (iteracja XXXIV)

**Data:** 2026-11-23. **Wyłączna gałąź:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/08-twierdzenia-graniczne-dla-calki-lebesguea.tex.  
**Blob źródła wejściowego:** e09cc0edca7fd200bcb48e3e5ad24b3b5989aa68.  
**Blob po poprawkach:** ee4660de677bebbe11323f08f18efc5111b91968.

## 1. Kontynuacja od najnowszych rzeczywistych danych

Na początku porównano bieżącą gałąź z commitem a61671143fa3d92b3563ca66b2ec9accbbec1033. Nowy commit dotyczył wyłącznie innego skryptu. Odczytano ostatni istniejący raport audits/measure_theory/33-rozdzial-07-audyt-II-stabilizacja-2026-11-23.md (blob 3304fd8f778d807c2cc5211920b8f0a826e241dd) i potwierdzono jego werdykt: **R07 STABILNY**. Raport audytu XXXIV przed pracami nie istniał, a źródło R08 było niezmienione (blob wejściowy powyżej).

Pobrano AGENTS.md (blob 32de9b61a368cfdce4923c8f81f9f7014da533fc), docs/pl/standardy_terminologiczne.md (blob bdbfc9923e1d7224b2c19a2ba8d459eaf72cdbdf), główną książkę books/pl/measure_theory.tex oraz pełny rozdział R08. Fragmenty R01–R07 odczytano **wyłącznie jako kontekst dla zależności matematycznych i etykiet**. Nie prowadzono audytów R01–R07 ani R09–R31; żadnego innego rozdziału nie zmieniono, nie scalano ani nie usuwano treści.

## 2. Zakres niezależnego audytu matematycznego

Po poprawkach R08 ma **1132 wiersze, 12 sekcji, 17 twierdzeń, 7 wniosków, 2 lematy, 2 definicje, 27 środowisk dowodów, 9 przykładów i 1 uwagę**. Nie ma rysunków. Przeanalizowano kolejno argumenty:

- Fundament konstrukcyjny: ciągłość miary z dołu dla poziomic funkcji prostej i niezależność od skończoności miary; twierdzenie Beppo Leviego z minorantą theta·s i rosnącymi zbiorami E_n, włącznie z nieskończonymi wartościami całek.
- Addytywność całki nieujemnej i liniowość rzeczywista oraz zespolona: przejście od funkcji prostych przez zbieżność monotoniczną i punktowe tożsamości części dodatniej i ujemnej.
- Lemat Fatou, jego wersja odwrócona i ograniczenie od dołu przez funkcję całkowalną; jawna kontrola, że nie odejmujemy nieokreślonego wyrażenia ∞−∞.
- Zbieżność zmajoryzowana i jej konsekwencje w L¹, zbieżność ograniczona na przestrzeniach miary skończonej oraz konieczność dominacji w przykładach masy uciekającej na nieskończoność i koncentrującej się na małych zbiorach.
- Zamiana sumy szeregu i całki dla funkcji nieujemnych oraz szeregu zespolonego z sumowalnymi całkami modułów. Wzór warstwowy i jego wersja z |f|^p dla p>0, z uwzględnieniem wartości funkcji i miar nieskończonych.
- Parametryczne twierdzenia o ciągłości i różniczkowaniu pod całką: wspólny zbiór zerowy, całkowalna funkcja dominująca i rzeczywiste ilorazy różnicowe; przykład transformaty Laplace'a.
- Jednostajna całkowalność: warunek kontroli ogonów, równoważne kryterium ograniczenia norm L¹ i kontroli na małych zbiorach, a następnie zbieżność Vitaliego przy mierze skończonej.
- Zgodność całek Riemanna i Lebesgue'a oraz kryterium Lebesgue'a całkowalności Riemanna przez oscylację punktową i sumy Darboux.

**Wynik:** wykryto pięć rzeczywistych luk w samodzielności hipotez, przypadkach brzegowych lub dokładności argumentów, poprawionych poniżej. Poza nimi nie znaleziono nowego fałszywego wzoru wymagającego korekty zakresu materiału. Przyszły niezależny audyt ma ponownie ocenić wszystkie te dowody, nie tylko poprawione miejsca.

## 3. Pięć poprawek bez naruszania etykiet i zakresu

Jedyny commit zmieniający źródło R08: **7dade90dc0cc568ffeb3451da98fa15daba073b9**.

1. **Niepusta rodzina w równoważnych kryteriach jednostajnej całkowalności:** twierdzenie thm:ui-two-criteria-8 nie podawało warunku niepustości, mimo że definicja def:uniform-integrability wymaga niepustej rodziny. Uzupełniono hipotezę; wyeliminowano rozbieżność dotyczącą rodziny pustej i konwencji supremum po pustej rodzinie.
2. **Zbieżność ograniczona:** w cor:bct zapisano stałą dominującą M∈[0,∞), a nie jedynie M<∞. Dowód używa funkcji nieujemnej g≡M; jawna hipoteza jest ważna również przy pustej przestrzeni X.
3. **Różniczkowanie pod całką:** do thm:differentiating-integrals wpisano konwencję, że na wspólnym *mierzalnym* zbiorze wyjątkowym, gdzie nie założono istnienia pochodnej, ∂_tF(t0,x) przyjmuje wartość zero. Dzięki temu prawa strona wzoru określa mierzalną funkcję na całym X.
4. **Kryterium Riemanna:** w implikacji od zerowego zbioru nieciągłości do całkowalności Riemanna wybiera się otwarte O zawierające D_epsilon i spełniające λ₁(O)<b−a. Gwarantuje to niepustość K=[a,b]\O, konieczną do zastosowanego dalej skończonego pokrycia i dodatniego minimum promieni; dawny dowód tego nie uzasadniał.
5. **Wniosek o obliczaniu całki przez aproksymacje:** w cor:simple-approx-integral wyraźnie wskazano przestrzeń z miarą (X,F,μ), bez zmiany tezy.

**Wszystkie historyczne etykiety zachowano.** Źródło po poprawce ponownie pobrano z GitHub; dokładny blob ee4660de677bebbe11323f08f18efc5111b91968.

## 4. Nowe testy, faktyczne CI i dokładne wyniki

Utworzono tools/test_measure_theory_ch08.py, commit **6086888796ab3700651dd8db55c53d2b8809c065**, nowy blob **e6e5916c3f6bc0e8f2a40348f65ed2f988562dbf**. Test jest osobnym narzędziem regresyjnym dla R08, bez wpływu na inne rozdziały. Dodano workflow .github/workflows/measure-theory-ch08.yml, commit **3bb895bbfeaf05d6136bec52bec71cbe0c013175**, blob **3f3083f0a5a328a941d3793a7f6e7c47ae529f47**. Oba pliki pobrano po zapisie i potwierdzono równość zawartości oraz SHA.

**Rzeczywisty przebieg GitHub Actions:** [45152299851](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152299851), commit 3bb895bbfeaf05d6136bec52bec71cbe0c013175, oba joby **2/2 completed SUCCESS**. Z logów testów:
- **3600 PASS:** skończone modele monotonicznej zbieżności całek z masami zerowymi i nieskończonymi;
- **36 864 PASS:** modele nierówności Fatou dla trójokresowych ciągów na dwóch atomach;
- **1800 PASS:** dokładne modele zbieżności zmajoryzowanej w L¹;
- **256 PASS:** wzór warstwowy z uwzględnieniem atomów o masie nieskończonej;
- **PASS:** 45 odsyłaczy R08, terminologia i struktura środowisk LaTeX.

**Zastrzeżenie matematyczne:** skończone testy nie są dowodem twierdzeń na dowolnych przestrzeniach z miarą, a testy arytmetyczne nie zastępują sprawdzenia wymiany operacji granicznych. Dlatego rozdział został ponownie przeanalizowany także na poziomie dowodów ogólnych.

## 5. Izolowany PDF, pełna książka i kontrola językowa

Ten sam CI wykonał rzeczywiście **dwie kompilacje pdflatex izolowanego R08** i **trzy kompilacje pełnej książki**. Izolowany R08 ma **12 stron A4, 6777 słów** sprawdzonych jako leżące w granicach stron. Wygenerowano i sprawdzono komplet **12/12 PNG**. Cała książka ma **257 stron** i poprawnie rozwiązuje etykiety: brak błędów kompilacji, niepowiązanych referencji, podwójnych etykiet i Overfull hbox.

Pobrano autentyczny ZIP artefaktu CI **14807430875** i rozpakowano do /mnt/data/r08_audit34. Z samych logów izolowanego R08: **0 Overfull hbox, 0 Underfull hbox**; ostrzeżenia o odsyłaczach międzyrozdziałowych w składzie izolowanym są spodziewane, bo nie kompiluje on R01–R07. Z logu pełnej książki: **0 Overfull hbox, 0 niezdefiniowanych odsyłaczy, 14 Underfull hbox**, ostrzeżenia nieblokujące poza izolowanym rozdziałem R08.

**Wizualizacja:** obejrzano zestawienie wszystkich dwunastu stron pobranego PDF, dodatkowo powiększono stronę 11 z kryterium Riemanna. Nie znaleziono uciętych formuł, nachodzących tytułów ani błędów układu wzorów. Strona 12 zawiera wyłącznie końcowe podsumowanie; jest to nieblokujący problem oszczędności papieru, nie wada matematyczna wymagająca natychmiastowej zmiany paginacji.

Końcowa osobna kontrola statyczna GitHub: **40 etykiet R08, 45 odsyłaczy, 0 brakujących celów w R01–R08, 0 duplikatów etykiet, 0 niesparowanych środowisk**. Brak błędnej terminologii „sekwencji”, „unia zbiorów”, „zbieżność zdominowana” oraz zabronionych zamienników \chi_A.

## 6. Powiązanie z osobnym skryptem całkowania

Dla kontekstu (bez audytu i bez edycji innych rozdziałów) odczytano books/pl/integration_theory.tex, blob **6ec24a3d62bae4baef945fca0ff1c433510de141**, i chapters/pl/integration_theory/11-calka-lebesgue-a.tex, blob **b082083e7f73099263c97f77c959d4e1a627be40**. Tamte materiały zawierają analogiczne twierdzenia graniczne i zbieżność zmajoryzowaną. Istnieje jednak wcześniej zidentyfikowana niezależna rozbieżność oznaczania funkcji charakterystycznych: makro \ind rozwija się do \mathbf 1, zamiast obowiązującej notacji \chi_A. Usterkę należy rozpatrzyć przy odrębnym audycie tamtego skryptu; **nie wolno jej korygować w ramach R08**. Nie wykonano żadnego scalania lub usuwania treści.

## 7. Formalny status stabilizacji i następna iteracja

**R08 — NIESTABILNY / W TOKU STABILIZACJI.** Audyt I doprowadził do pięciu zmian w źródle, osobnych testów i nowego, w pełni zielonego CI. Spełniono techniczną kontrolę PDF i referencji, ale rygor projektu zabrania ogłoszenia stabilności w iteracji z poprawkami. **Konieczny jest następny, niezależny, pełny i czysty audyt całego R08 po ostatniej zmianie**, w szczególności Beppo Leviego, Fatou, zbieżności zmajoryzowanej, różniczkowania pod całką, jednostajnej całkowalności i kryterium Riemanna. Jeśli wykaże nowe usterki, poprawić je i przeprowadzić kolejny audyt R08.

**R01–R07 — STABILNE**, status odziedziczony po wcześniej zatwierdzonych osobnych raportach. **R09–R31 — nieaudytowane w tej iteracji.**

**Następna iteracja:** globalny audyt XXXV / R08 II, wyłącznie rozdział 08. Nie przechodzić do R09 przed jawną stabilizacją R08.