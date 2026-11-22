# Topologia ogólna — rozdział 22, audyt 03 (drugi czysty)

**Data:** 2026-11-22.
**Źródło:** chapters/pl/general_topology/22-zbieznosc-kuratowskiego-wijsman-attouch-wets.tex.
**Niezmieniony blob:** 33765c2bb1b3065f4ad32596795c3d1981b48dda.
**Wynik:** CZYSTY — **2/2** kolejnych audytów matematyczno-redakcyjnych poprawionego rozdziału.

## Druga niezależna kontrola matematyczna

1. **Kuratowski:** górna granica spełnia warunek „dla każdego otoczenia i każdego indeksu progowego istnieje późniejszy trafiający zbiór”, dolna — „dla każdego otoczenia wszystkie wystarczająco późne zbiory trafiają”. Warunki są równoważne odpowiednio liminf d(x,F_n)=0 i d(x,F_n)→0. Dowód domkniętości obu granic opiera się wyłącznie na nierówności trójkąta, jest poprawny także dla F_n=∅.
2. **Funkcje odległości:** d(.,F) jest 1-lipschitzowska dla niepustego F, a zbiór zerowy tej funkcji jest domknięciem F. Stąd iniektywność odwzorowania F↦d(.,F) na rodzinie niepustych domkniętych; punktowa zbieżność odległości implikuje dokładnie Li=Ls=F.
3. **Wijsman metryzowalny dla ośrodkowej X:** poprawność szeregu, dodatnia określoność i zgodność topologii wynikają z 1-lipschitzowskości oraz gęstego przeliczalnego D. Dowód nie myli zbieżności ciągów z równością topologii; zawiera argument o otoczeniach.
4. **Wijsman silniejsza od Fella:** dla U otwartego i F trafiającego U wystarczy jedna ewaluacja d(x,.) w x∈F∩U; dla C zwartego rozłącznego z F dodatnia odległość r=min_C d(x,F)>0 i skończony podzbiór r/4-gęsty C pozwalają wykluczyć trafianie C przez wszystkie zbiory z małego otoczenia Wijsmana. W szczególności implikacja nie używa własności przestrzeni właściwej.
5. **AW:** każda Δ_m jest skończona, ponieważ dla niepustego F funkcja d(.,F) jest ograniczona na każdej ograniczonej kuli. Rho_AW jest metryką i wyznacza zbieżność jednostajną odległości na wszystkich niepustych zbiorach ograniczonych. Punkt bazowy jest obojętny, gdyż rodziny jego kul są współkońcowe względem wszystkich ograniczonych podzbiorów.
6. **Właściwość przestrzeni:** zbieżność punktowa funkcji 1-lipschitzowskich daje zbieżność jednostajną na zwartych kulach przez skończone aproksymacje; argument obowiązuje dla sieci i dowodzi równości topologii Wijsman/AW.
7. **Fell kontra Kuratowski:** w lokalnie zwartej metrycznej X każdy x poza F ma otoczenie W o zwartym domknięciu rozłącznym z F. Warunek górny Fella zapewnia ostateczne ominięcie W i x∉Ls. Odwrotnie, jeśli zbiory F_n trafiają zwarty C niezgodny z granicą F w nieskończenie wielu indeksach, zwartość metryczna daje punkt z Ls∩C. Dlatego oba kryteria są równoważne bez globalnej właściwości metryki.
8. **Kuratowski⇒Wijsman dla właściwej:** z F⊆Li wynika limsup d(x,F_n)≤d(x,F); przy hipotetycznie mniejszym liminf można wybrać punkty F_{n_k} w jednej zwartej kuli o promieniu <d(x,F), z których podciąg zbiega do punktu Ls=F, sprzeczność. Osobno rozpatrzono r=0, gdzie nieujemność odległości daje wynik.
9. **Granice zakresu:** dla F=∅ konwencja d(x,F)=∞ jest używana tylko w Kuratowskim, a Fell dopuszcza pusty zbiór. Wijsman i AW wyłączają go wprost. W twierdzeniu o równoważności czterech kryteriów zarówno F, jak i wszystkie F_n są niepuste, co nie dopuszcza błędnego stosowania wyrażeń ∞−∞.
10. **Przykłady rozdzielające:** naprzemienne {0},{1} nie mają granicy Kuratowskiego; {0,n} w R zbiega w AW/Wijsman/Fell/Kuratowski, lecz d_H=n; w nieskończonej ograniczonej dyskretnej X, X\{n}→X w Wijsmanie, lecz nie w AW; metryka na {p,q}∪{y_n} z jedynym odcinkiem długości 2 dowodzi, że lokalna zwartość nie zastępuje właściwości.

## Integralność LaTeX i realna walidacja

- Niezmieniony badany blob: 716 wierszy, 28 różnych etykiet, 20 odsyłaczy; wszystkie cele z rozdziałów 14, 21 i 22 istnieją. Nie ma brakujących środowisk, niezgodnych nazw terminologicznych ani osieroconych plików graficznych.
- [CI 45047289481](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047289481) zakończyło się **completed/success** dokładnie dla commitu d162dc918d46baae12d2f56384d8ece28f7bfb31 z tym blobem rozdziału. Przeszły testy modelowe, spójność katalogu, kompilacja całej książki i 21 samodzielnych punktów wejściowych (02–22) oraz kontrola logów.
- Z tego uruchomienia pobrano artefakt ID **14764545206** „general-topology-ch01-ch22” i wypakowano prawdziwy general_topology_ch22.pdf oraz log. Dokument ma **7 stron A4**. Wszystkie strony wyrenderowano i sprawdzono w przeglądzie zbiorczym, a ostatnią obejrzano w powiększeniu. Na stronie 7 po wprowadzeniu nowego dowodu mieści się zakończenie przykładu oraz pełne podsumowanie, a nie osamotniony czterowierszowy akapit. Nie zaobserwowano nachodzenia tekstów na rysunki ani uciętych wzorów.
- W logu samodzielnego PDF brak komunikatów Overfull, Underfull, Missing character, LaTeX Warning, Undefined control sequence i Fatal error. Rysunek ucieczki punktu jest samodzielnym TikZ, bez zewnętrznych grafik.

## Status

**Rozdział 22 — stabilny matematycznie i redakcyjnie po 2/2 czystych audytach**, pod warunkiem utrzymania wersji 33765c2...
Do zamknięcia pełnego procesu konieczne są jeszcze:
(1) dodatkowy audyt potwierdzający bez zmiany źródła,
(2) aktualizacja strony tytułowej książki i testu integracji,
(3) zielone CI integracji po tej aktualizacji.
