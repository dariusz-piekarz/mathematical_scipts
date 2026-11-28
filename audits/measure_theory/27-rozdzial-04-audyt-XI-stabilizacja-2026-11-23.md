# Teoria miary / Miara i całka — rozdział 04, audyt XI (iteracja XXVII): czysta kontrola i zatwierdzenie stabilności

**Data:** 2026-11-23. **Istniejąca gałąź:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex.  
**Aktualny blob R04:** ce0105f63aa4da494cf5f2f5e9e2b26fc6389fd4 (bez zmian od audytu XXVI).

## 1. Punkt wznowienia i izolacja prac

Na początku odczytano aktualne źródło rozdziału, raport audytu XXVI (plik 26-rozdzial-04-audyt-X-2026-11-23.md, blob 7a6bb55358afd02e121da948090c9001fa89717a), najnowszą gałąź w porównaniu z commitem f81305c14d4daa099ebea6a49b5f7b2d44a0f898, obowiązujące AGENTS.md i docs/pl/standardy_terminologiczne.md oraz główny plik books/pl/measure_theory.tex. Nie istniał jeszcze raport XXVII; żaden późniejszy commit nie zmienił R04. Zależności z rozdziałami 01–03 czytano tylko w celu sprawdzenia odsyłaczy R04, a books/pl/integration_theory.tex pozostawiono w niezmienionym stanie. Nie audytowano innych rozdziałów, nie scalano i nie usuwano żadnej treści.

Rozdział 04 ma **982 wiersze, 11 sekcji, 3 definicje, 3 lematy, 8 twierdzeń, 3 wnioski, 14 środowisk dowodu, 5 przykładów, 5 uwag i 1 rysunek TikZ**. Przegląd wykonano od początku do końca, niezależnie od ocen poprzednich audytów. W niniejszej iteracji **nie wykonywano poprawki źródła ani kodu testowego**: audyt jest czystym audytem potwierdzającym po ostatniej zmianie technicznej z XXVI.

## 2. Samodzielny przegląd matematyczny — wynik PASS

1. **Siatki i nierówność objętościowa.** Ponownie sprawdzono rozkłady na rozłączne półotwarte komórki, dobrze określoną objętość na pierścieniu, przejście do zwartego rdzenia, podpokrycie skończone, oddzielny przypadek zdegenerowanego zwartego prostopadłościanu i rozdzielenie granic. W tym łańcuchu nie potrzeba zakładać z góry istnienia miary Lebesgue'a.
2. **Premiara i miara zewnętrzna.** Dwie nierówności dla przeliczalnej addytywności na algebrze ograniczonego prostopadłościanu wynikają odpowiednio ze skończonej addytywności i lematu pokryciowego. Pokrycia prostopadłościanami półotwartymi dają miarę zewnętrzną; przecięcie i różnica z ustalonym prostopadłościanem wystarczają do kryterium Carathéodory'ego. Jednoznaczność miary borelowskiej stosuje właściwy układ pi i rosnące pokrycie zbiorami skończonej miary.
3. **Translacje, skalowanie i hiperpłaszczyzny.** Oddzielnie zweryfikowano ujemne skale, obraz przedziału półotwartego typu (a,b] oraz dowolnie małe powiększenia pokryć; dla przekształcenia afinicznego bijektywność zachowuje części przekroju i różnicy. Hiperpłaszczyzny i przeliczalne zbiory punktów są mierzalne o mierze zero.
4. **Regularność, aproksymacje borelowskie i uzupełnienie.** Sprawdzono rozróżnienie miar skończonych od nieskończonych, powiększenia otwarte z błędem sumowalnym, aproksymację przez zbiory zwarte i konstrukcję G-delta / F-sigma za pomocą pokrycia przeliczalnymi zbiorami skończonej miary. Implikacje w geometrycznej charakterystyce mierzalności wykorzystują miarę zewnętrzną i zupełność we właściwym kierunku.
5. **Przykłady i ograniczenia mierzalności.** Zbadano gęste zbiory miary zero, wykres Lipschitzowski (jawne założenia i osobny przypadek a=b), oszacowanie objętości kul, zbiór Cantora (zwartość, doskonałość, homeomorfizm z przestrzenią ciągów, nieprzeliczalność i miara zero), zbiór Smitha–Volterry–Cantora (miara 1/2), funkcję Cantora (ciągłość, monotoniczność, pochodna równa zero prawie wszędzie i brak absolutnej ciągłości), konstrukcję Vitaliego oraz niemożliwość niezmienniczej znormalizowanej miary na całej rodzinie podzbiorów prostej.

**Wynik matematyczny: PASS, bez nowej wykazanej luki wymagającej zmiany.** Zachowano wszystkie jawne kwantyfikatory i zależności logiczne. Dodatkowych niezatwierdzonych twierdzeń, przykładów ani rysunków nie dopisywano.

## 3. Niezależna kontrola źródła i terminologii — PASS

Ponownie pobrano wszystkie etykiety tylko z R01–R04 jako kontekst odsyłaczy R04. W rozdziale 04 występuje **28 etykiet i 31 odsyłaczy**; **0 nierozwiązanych celów, 0 duplikatów etykiet w R01–R04, 0 błędnie sparowanych lub niedomkniętych środowisk**. Zweryfikowano 11 nagłówków sekcji i poprawną separację podpisu od jedynego rysunku TikZ.

Nie wykryto zabronionych oznaczeń funkcji charakterystycznej innych niż wymagane chi_A ani wyrażeń „unia zbiorów”, „zbieżność zdominowana”, „zwartościowanie” czy „zbieżność zwarta”. Konwencja skryptu wymaga wyłącznie \chi_A i nazwy „zbieżność zmajoryzowana”; w R04 nie ma odstępstwa.

## 4. Niezależne sprawdzenie geometrii rysunku — PASS

Po raz kolejny, niezależnym rachunkiem na pobranym aktualnym źródle, obliczono oczekiwane współrzędne trzech iteracji zbioru Cantora i porównano z wszystkimi liczbami TikZ. **28/28 końców** jest zgodnych; maksymalne odchylenie wynikające z zaokrąglenia do sześciu cyfr wynosi ok. **3,3334 × 10^(-7)**, poniżej progu 10^(-6). Podpis pozostaje w osobnym akapicie pod rysunkiem.

## 5. Ponowne potwierdzenie rzeczywistego CI i pełnego PDF — PASS

Ponownie odczytano bezpośrednio statusy dwóch zadań **GitHub Actions run 45143823731**, commit b7bf59948d48a99f43035a807516af5a8a0bae4b:
- **chapter-04-exact-geometry: completed / success**;
- **chapter-04-pdf-and-references: completed / success**.

Artefakt **14803650991** jest dostępny i nie wygasł. Potwierdzone w autentycznych logach runu: dwie kompilacje izolowanego R04 do **10 stron A4**, 5821 poprawnie rozpoznanych i mieszczących się na stronach słów w formacie Poppler bbox, kontrola podpisu Cantora na stronie 7, dokładnie **10 PNG na 10 stron**; następnie trzy kompilacje kompletnej książki do **256 stron A4** z rozwiązywaniem referencji. Zadania zakończyły się sukcesem. W tej iteracji nie przedstawia się poprzedniego przebiegu jako nowo uruchomionego: został rzeczywiście uruchomiony w audycie XXVI, a teraz jego rezultat i aktualność potwierdzono niezależnie.

**Nowy, niezależny przegląd lokalnego PDF z pobranego artefaktu:** odczyt wszystkich 10 stron narzędziem PyMuPDF; kontrola granic wszystkich 4720 tokenów słownych w tej segmentacji — **0 poza stronami**. Wizualnie ponownie przejrzano osobno strony 1–6 oraz 7–10 na pełnych renderach; brak widocznych kolizji, w szczególności podpisu Cantora na stronie 7. Różnica liczby słów wobec Poppler (4720 vs 5821) wynika z innej tokenizacji i nie jest usterką PDF. Log izolowanego PDF ma **0 Overfull i 0 Underfull hbox**, bez błędów sterowania TeX.

**Jawne rozróżnienie ostrzeżeń:** izolowana kompilacja ma oczekiwane ostrzeżenia o zewnętrznych referencjach do R01–R03, ponieważ nie są one włączone do izolowanego dokumentu. W pełnej książce jest **0 nierozwiązanych referencji i 0 Overfull hbox**. Są natomiast **14 wpisów Underfull hbox** w innych plikach (rozdział 27 i indeks) oraz ostrzeżenia hyperref o zapisach matematycznych w zakładkach innych rozdziałów. Nie przypisujemy ich R04 i nie naruszamy tych rozdziałów w tym audycie.

## 6. Rozstrzygnięcie stabilności

**ROZDZIAŁ 04 — STABILNY / ZATWIERDZONY.**

Kryteria projektu zostały spełnione:
- dotychczasowe poprawki matematyczne i wizualne udokumentowano w audytach XVII–XXVI;
- wykonano niezależną kontrolę matematyki, języka, struktury i rysunku **bez nowych wykazanych usterek**;
- potwierdzono dwuzadaniowe realne zielone CI, pełny PDF izolowanego rozdziału, kompilację kompletnej książki oraz poprawne odsyłacze;
- **audyt XXVII jest dodatkowym czystym audytem wykonanym po ostatniej poprawce technicznej z XXVI**;
- status został **jawnie potwierdzony** niniejszym raportem, nie jedynie wywnioskowany z historii CI.

**Następna iteracja:** dopiero teraz można rozpocząć **wyłącznie rozdział 05** na tej samej gałęzi, od aktualnych źródeł i audytu wstępnego. W tej iteracji **nie rozpoczęto audytu 05**. Dalsze osobne audyty R05–R31 zachowują własny rygor.
