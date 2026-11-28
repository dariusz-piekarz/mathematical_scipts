# PLAN GLOBALNY BIBLIOTEKI MATEMATYCZNEJ

**Wersja 1.3 — 28.11.2026.** Nadrzędny dokument roboczy. Migawka katalogu: [8e104a7](https://github.com/dariusz-piekarz/mathematical_scipts/commit/8e104a732fb4293b1f23f06774f01f8d6e17d96c). Gałąź robocza: biblioteka-matematyczna-iteracja-6. **22 aktywne skrypty, 607 rozdziałów.** Pełny indeks ścieżek, blobów i kandydatów na raporty: [catalog/global_library_inventory.json](../../catalog/global_library_inventory.json).

To plan żywy, nie certyfikat ukończenia całej biblioteki. Inwentaryzacja obejmuje katalog i nazwy wszystkich aktywnych rozdziałów oraz wybrane raporty i plany. Nie przeczytano ponownie wszystkich dowodów ani wszystkich raportów; propozycje uzupełnień są zadaniami sprawdzenia pokrycia, a nie stwierdzeniem braku. Statusy historyczne dotyczą wersji wskazanych w raportach. Brak raportu w standardowym katalogu nie oznacza braku przeprowadzonego audytu.

## 1. Reguła obowiązująca przed każdą zmianą

1. Odczytać ten plan, katalog, indeks rozdziałów i właściwy plan lokalny.
2. Wyszukać temat po tytule, synonimach, etykietach i pełnych tezach w aktywnych źródłach, materiałach kandydackich i archiwalnych; sprawdzić dowód i założenia, nie tylko tytuł.
3. Wybrać właściciela kanonicznego. Jeżeli wynik istnieje, użyć odsyłacza lub przejąć zweryfikowany materiał z etykietą; dopisać jedynie brakujący zakres. Dydaktyczny dowód szczególnego przypadku jest dopuszczalny z wyraźnym uzasadnieniem.
4. Sprawdzić raport audytu, blob źródła, zależności oraz aktualność CI/PDF. Nie otwierać bez powodu zamkniętych rozdziałów. Zmiana treści uruchamia ponowną kontrolę dotkniętego zakresu.
5. Przy migracji: źródło → cel → mapa etykiet/ID → kontrola semantyczna → aktualizacja odsyłaczy, katalogu, generatora, testów i figur → audyt stabilizacyjny → niezależny kontrolny → CI i PDF → dopiero wycofanie źródła. Nie usuwać jedynej wersji wyniku; bez pustych rozdziałów i duplikacji etykiet. Zachować archiwum i historię.
6. Zaktualizować globalny plan/rejestr: co zmieniono, źródło, cel, status, commit, raport, CI, następny krok. Nie nadpisywać równoległych commitów; nie uruchamiać dodatkowych workflow bez potrzeby.

## 2. Kolejka prac i priorytety

| Priorytet | Zadanie | Bramka |
|---|---|---|
| P0 | AM II: audyt restrukturyzacji, ukończenie i zamknięcie | kolejność książki/Atlasu, Stokes, komplet audytów, PDF |
| P0 | AM I: klasyczna całka jednowymiarowa i przeniesienie rozszerzeń | zachowane BV/AC i wszystkie zależności |
| P0 | RTPC: utworzenie i integracja rozszerzonej teorii pochodnej i całki | zachowane etykiety AM I/II, AF, ME; brak duplikacji |
| P1 | AF → FSG: rejestracja i migracja geometrii przestrzeni Banacha | istniejący kandydat, cross-check AM II, audyt i CI |
| P1 | DT/Fourier, RRC, MOD, NL, MM, LTM, CAT i RP1–4 | domknięcie rozpoczętych tematów i audytów, nie ponawiać zaliczonych bez powodu |
| P1 | Kontrola integracji całej biblioteki: etykiety, graf pojęć, CI, PDF, aplikacja | raporty na zgodnych blobach, nie sam licznik testów |
| P1 | AF: rozbudowa teorii operatorów; ALG: rozbudowa geometrii algebraicznej | audyt pokrycia, niezależne moduły |
| P2 | AZ I–II, geometria klasyczna, RZUD, teoria liczb i arytmetyka | po ustaleniu zależności i pokrycia |
| P2 | Liczby p-adyczne i analiza niearchimedesowa, analiza niestandardowa | AA, TL, ME, AF, MOD i LTM |
| P2 | Rozdzielenie DG na geometrię i topologię różniczkową; następnie osobne specjalizacje wymiaru 4 | mapa etykiet, audyt pokrycia DG/AT/GT/RRC |
| P2 | Algebra przemienna i nieprzemienna; geometria różniczkowa orbifoldów (szczególnie ważna dla użytkownika) | po inwentaryzacji AA/ALG/CAT/DG/GT; ustalić kolejność zależności |
| P3 | GAZ I–II, geometria nieprzemienna i pogłębione tomy czterowymiarowe | po odpowiednich podstawach; dokładna kolejność do ustalenia |

P0 w wątku AM ma ścisłą kolejność AM II → AM I → RTPC. FSG i inne rozpoczęte wątki mogą być prowadzone osobno pod warunkiem bezpiecznej koordynacji i braku utraty zależności. Nie włączać automatyzacji tym planem.

## 3. Właściciele tematyki i plany wszystkich aktywnych skryptów

### AA — Algebra abstrakcyjna (72)

- **Rdzeń:** Grupy, pierścienie, ciała, moduły, Galois, algebra przemienna, reprezentacje i algebry Liego.
- **Plan / granice:** 01–42 podstawy; 43–50 algebra różniczkowa i Galois; 51–72 niezmienniki, korzenie i reprezentacje. Zachować obecne wyniki; wydzielenie teorii Liego/ reprezentacji rozważyć dopiero przy rozbudowie. Kontrola integracji GA/BT i odsyłaczy. Uzupełnić algebry Hopfa oraz reprezentacje grup skończonych, o ile brak po audycie.
- **Audyt:** Raport globalny AA01–42 istnieje; 43–72 i migracja GA/BT: ustalić bramki per rozdział. [Dokument](../../audits/abstract_algebra/00-globalny-audyt-koncowy-AA01-AA42-2026-11-23.md).
- [Aktywny katalog rozdziałów](../../books/pl/abstract_algebra.tex).

### ALG — Geometria algebraiczna (11)

- **Rdzeń:** Schematy/odmiany algebraiczne, geometria lokalna i globalna, przecięcia, geometria biwymierna.
- **Plan / granice:** 00–10 zachować; rozbudować od schematów: morfizmy, włókna, płaskość, gładkość, étale, koherentne snopy, kohomologia, dywizory, Riemann–Roch, moduły, moduli, podstawy arytmetyczne. AP docelowy właściciel zaawansowanej algebry przemiennej, AA podstaw, CAT formalizmu snopów. GAGA łącznik z przyszłą GAZ.
- **Audyt:** Raport 22.11: ALG00–10 zamknięte na ówczesnej wersji; ponownie sprawdzić bloby przed zmianą. [Dokument](../../audits/algebraic_geometry/STATUS.md).
- [Aktywny katalog rozdziałów](../../books/pl/algebraic_geometry.tex).

### AT — Topologia algebraiczna (31)

- **Rdzeń:** Homotopia, homologia i kohomologia przestrzeni, fibracje, ciągi spektralne, klasy charakterystyczne, dualności.
- **Plan / granice:** 01–03 i 30: skrócić powtórzenia TO/AA/CAT/DG do mostów. Rozdziały 23–28 o snopach i Hodge'u ocenić: formalizm CAT, geometria zespolona/ALG, w AT zastosowania topologiczne. Uzupełnić lub potwierdzić Künnetha, Eilenberga–Zilbera, lokalne współczynniki, dualności Aleksandra i Poincarégo–Lefschetza, spektra.
- **Audyt:** Raport historyczny AT/DG/AG istnieje; brak pełnego rejestru indywidualnego w standardowym katalogu audytów. [Dokument](../../application/docs/AUDYT_GLOBALNY_AT_DG_AG_ETAP_01_2026-11-20.md).
- [Aktywny katalog rozdziałów](../../books/pl/algebraic_topology.tex).

### CAT — Teoria kategorii (48)

- **Rdzeń:** Konstrukcje uniwersalne, sprzężenia, monady, algebra homologiczna, kategorie pochodne, snopy i toposy, kategorie wyższe.
- **Plan / granice:** 00–18 podstawy, 19–32 struktury, 33–47 wyższe; przesunąć słownik na koniec lub do dodatku. Właściciel Ext/Tor, kategorii pochodnych i formalizmu sześciu operacji; AT/ALG/DG podają konkretne realizacje. Domknąć CAT40–47 i kontrolę całego tomu; ewentualnie wydzielić wyższe kategorie jako tom II.
- **Audyt:** CAT39 kontrolnie zamknięty w odczytanym raporcie; nie ekstrapolować na CAT40–47. [Dokument](../../audits/category_theory/chapter-39/control.md).
- [Aktywny katalog rozdziałów](../../books/pl/category_theory.tex).

### DG — Geometria i topologia różniczkowa (20)

- **Rdzeń:** Rozmaitości, pola, formy, geometria riemannowska, koneksje, geodezyjne, krzywizna, transwersalność, Morse, kobordyzmy.
- **Plan / granice:** DG03–09: formalizm AL/AA/CAT/AT, zachować pomosty i zastosowania. DG10: abstrakcyjne rozmaitości i de Rham, AM II dowód euklidesowy Stokesa. DG15–20: rozdzielić materiał geometryczny i topologiczny, uzgodnić z AT i GT. Zatwierdzony kierunek: odrębna geometria różniczkowa i topologia różniczkowa, następnie specjalizacje w wymiarze 4; proponowany podział na DG, TD, DG4 i TD4 opisano w sekcji 5. Uzupełnić wiązki, koneksje główne, grupy Liego, symplektykę, teorię Hodge'a i geometrię zespoloną po sprawdzeniu pokrycia. Nie wycofywać obecnej książki przed pełną migracją.
- **Audyt:** Raporty historyczne; pełna macierz audytów aktualnych 20 rozdziałów do odtworzenia. [Dokument](../../application/docs/AUDYT_CIAGLOSCI_DG_I_ODSYLACZY_2026-11-20.md).
- [Aktywny katalog rozdziałów](../../books/pl/differential_geometry_and_topology.tex).

### DT — Teoria dystrybucji i analiza harmoniczna (30)

- **Rdzeń:** Funkcje testowe, dystrybucje, Fourier, Laplace, analiza harmoniczna, całki osobliwe.
- **Plan / granice:** Wykonać istniejący plan 1–57 bez pustych modułów: szeregi Fouriera, DFT/FFT, transformaty Laplace'a i inne, mnożniki, Hilbert/Riesz, Calderón–Zygmund, Hardy/BMO, Littlewood–Paley, analiza na grupach. Z RRC06–08 przejąć tylko brakującą teorię ogólną; RRC zachowa zastosowania do PDE. Uzgodnić AF i ME, nie dublować topologii ogólnej.
- **Audyt:** 30 aktywnych; plan migracji nie jest audytem. Status per rozdział wymaga odtworzenia. [Dokument](../../catalog/distribution_theory_structure_plan.json).
- [Aktywny katalog rozdziałów](../../books/pl/distribution_theory.tex).

### AF — Analiza funkcjonalna (26)

- **Rdzeń:** Przestrzenie liniowo-topologiczne, lokalnie wypukłe, Banacha i Hilberta, geometria norm, dualność, operatory i widmo.
- **Plan / granice:** AF14–15 → FSG; AF15A–15B → RTPC (całki) i ME (miary wektorowe/RNP); AF16: funkcjonały wypukłe zachować, rachunek wariacyjny uzgodnić z FSG/RRC. 26–33 uzupełnić operatory domknięte, domykalne, normalne, samosprzężone, pierwiastek dodatni, rozkład polarny, rachunki funkcyjne, półgrupy po audycie pokrycia. Nie usuwać źródeł przed pełną migracją.
- **Audyt:** AF15B kontrolnie zakończony według raportu; CI modułu i pełnego AF PASS dla wskazanej rewizji, bez nowej kontroli wizualnej. Cały AF niecertyfikowany tutaj. [Dokument](../../audits/functional_analysis/15B-audyt-kontrolny-reorganizacja-2026-11-28.md).
- [Aktywny katalog rozdziałów](../../books/pl/functional_analysis.tex).

### TO — Topologia ogólna (26)

- **Rdzeń:** Aksjomaty, konstrukcje, zwartość, spójność, metryzacja, jednostajność, uzwarcenia, przestrzenie odwzorowań, opisowa teoria zbiorów.
- **Plan / granice:** 01–26 zachować. Nie otwierać zamkniętych dowodów bez konkretnej potrzeby; uzgodnić z AM I/II, AF i ME, ewentualne rozszerzenia opisowej teorii zbiorów po przeglądzie. Grupy topologiczne: TO podstawy, ME Haar, DG grupy Liego.
- **Audyt:** Raport 23.11: CI i regresja 188 stron PASS dla historycznego wydania; sprawdzić tożsamość bieżących blobów. [Dokument](../../audits/general_topology/00-globalny-audyt-65-zamkniecie-ci-i-regresja-artefaktu-188-stron.md).
- [Aktywny katalog rozdziałów](../../books/pl/general_topology.tex).

### GT — Teoria grafów i węzłów (42)

- **Rdzeń:** Grafy kombinatoryczne, algorytmy, grafy topologiczne oraz węzły i 3-/4-rozmaitości.
- **Plan / granice:** Zaproponować dwa tomy: grafy (00–17, 37–43 w obecnych ID) i węzły/niska topologia (18–34), z mostami Taita/Tutte/plumbing. Seiberg–Witten i rozbudowana teoria 4-rozmaitości: docelowo TD4 (niezmienniki, zastosowania topologiczne), DG4 (geometria i równania cechowania), RRC/AF (ogólne podstawy analityczne); GT zachowuje węzły, sploty i potrzebne pomosty. Przed przeniesieniem sprawdzić GT22–34 i zachować pełny materiał. Uzupełnić po audycie grafów algorytmy/kolorowanie, matroidy i teorię węzłów (Alexander, Jones, sploty, niezmienniki). Zachować wszystkie stabilne dowody.
- **Audyt:** Istnieją liczne audyty globalne i rozdziałowe; status na aktualnych blobach ustalić przed rozdziałem tomów. [Dokument](../../audits/graph_and_knot_theory/global-structural-batch-control-2026-11-25.md).
- [Aktywny katalog rozdziałów](../../books/pl/graph_and_knot_theory.tex).

### LA — Algebra liniowa (32)

- **Rdzeń:** Przestrzenie wektorowe, formy, tensory, macierze, rozkłady, Grassmanniany, Clifford, spinory.
- **Plan / granice:** 01–21 rdzeń; 22–28 równania macierzowe i sterowanie jako osobna część, docelowo stosowana algebra/sterowanie przy rozroście; 29–32 geometria algebraiczno-liniowa, DG zastosowania. Nie przepisywać stabilnego materiału. Sprawdzić SVD, QR/LU, jednoczesną diagonalizację i twierdzenie Schura przed ewentualnymi uzupełnieniami.
- **Audyt:** Raport 23.11: 32 rozdziały, 382/382 dowodów, 320 stron i CI PASS; globalnie zamknięte na kontrolowanej wersji. [Dokument](../../audits/linear_algebra/global_audit/status.md).
- [Aktywny katalog rozdziałów](../../books/pl/linear_algebra.tex).

### LTM — Logika i teoria mnogości (23)

- **Rdzeń:** Klasyczny rachunek zdań i kwantyfikatorów, relacje, funkcje, ZF/ZFC, wybór, liczby kardynalne i porządkowe, wymuszanie.
- **Plan / granice:** Zachować zaawansowaną teorię mnogości tutaj; teorię modeli i metamatematykę już wydzielono. Logika infinitarna na styku z MOD/NL: w LTM tylko potrzebne zastosowania do liczb kardynalnych. Uzupełnić brakujące elementarne wyniki i sprawdzić archiwalne etykiety, integralność zamiast ponownego pełnego audytu bez przyczyny.
- **Audyt:** Migracja strukturalna aktywna; audyty LTM historyczne i nowe; sprawdzić deduplikację semantyczną i etykiety. [Dokument](../../catalog/logic_model_migration.json).
- [Aktywny katalog rozdziałów](../../books/pl/logic_and_set_theory.tex).

### MM — Metamatematyka i teoria obliczalności (7)

- **Rdzeń:** Obliczalność, arytmetyka formalna, kodowanie, Gödel, Tarski, Löb.
- **Plan / granice:** Rozbudować maszyny Turinga, funkcje rekurencyjne, hierarchię arytmetyczną, stopnie Turinga, nierozstrzygalność, siłę dowodową i ewentualnie teorię dowodu. MOD pełność, MM niezupełność; NL logiki alternatywne. Odzyskać mapę audytów po migracji.
- **Audyt:** 7 aktywnych rozdziałów; stan audytów na nowych ścieżkach nieustalony. [Dokument](../../docs/pl/plan_metamatematyki_i_teorii_obliczalnosci.md).
- [Aktywny katalog rozdziałów](../../books/pl/metamathematics.tex).

### NL — Logika niestandardowa (3)

- **Rdzeń:** Logiki rozmyte, wielowartościowe, intuicjonistyczne oraz inne alternatywne systemy.
- **Plan / granice:** Uzupełnić modalne i Kripkego, parakonsystentne, liniowe i sub-strukturalne, temporalne, logiki wyższych rzędów w odpowiednim zakresie; porównać semantykę i systemy dowodzenia. CAT semantyka kategorialna, LTM klasyka, MOD model teoria.
- **Audyt:** 3 aktywne rozdziały; brak osobnego zweryfikowanego rejestru audytów w tej inwentaryzacji. [Dokument](../../docs/pl/plan_logiki_niestandardowej.md).
- [Aktywny katalog rozdziałów](../../books/pl/nonclassical_logic.tex).

### ME — Miara i całka (32)

- **Rdzeń:** Abstrakcyjne miary i całka Lebesgue’a, Lp, miary Radona, różniczkowanie, Hausdorff, pole i koobszar, geometryczna teoria miary.
- **Plan / granice:** Zachować abstrakcyjne miary i RNP; ME30 całki Bochnera/Birkhoffa → RTPC, zostawić potrzebne twierdzenia o miarach wektorowych lub most. ME31 dżety: sprawdzić, czy miarowe zastosowania uzasadniają lokalizację; pełna geometria dżetów DG/FSG. ME32 Daniell–Stone: konstrukcja miary tutaj, porównania całek RTPC. Nie powielać AM I/II.
- **Audyt:** Raport globalny 31/31; późniejsze ME30/32 mają nowe raporty, nie przenosić statusu automatycznie na 32 rozdziały. [Dokument](../../audits/measure_theory/00-audyt-clv-zamkniecie-globalne-2026-11-24.md).
- [Aktywny katalog rozdziałów](../../books/pl/measure_theory.tex).

### MOD — Teoria modeli (13)

- **Rdzeń:** Języki, struktury, logika pierwszego rzędu, pełność, zwartość, Löwenheim–Skolem, ultrailoczyny, typy.
- **Plan / granice:** Dokończyć eliminację kwantyfikatorów, pomijanie typów, modelową zupełność, kategoryczność, modele pierwsze, stabilność, o-minimalność i zastosowania do ciał; inwentaryzacja starego archiwum przed importem. LTM teoria zbiorów, MM niezupełność.
- **Audyt:** MOD12 kontrolnie zakończony według raportu; MOD13 i dalsze do audytu; brak wizualnej kontroli PDF MOD12. [Dokument](../../audits/model_theory/MOD-12-audyt-kontrolny-2026-11-28.md).
- [Aktywny katalog rozdziałów](../../books/pl/model_theory.tex).

### RRC — Równania różniczkowe cząstkowe (33)

- **Rdzeń:** PDE klasyczne, Sobolew, metody wariacyjne, regularność, równania ewolucyjne i nieliniowe, zastosowania numeryczne.
- **Plan / granice:** 06–08 ogólny Fourier/dystrybucje → DT lub odsyłacz; 12 ogólna teoria operatorów → AF, RRC zastosowania. Zachować Sobolewa, Lax–Milgram w kontekście PDE, eliptyczne, paraboliczne, hiperboliczne, Navier–Stokes i mikrolokalną. Różniczkować regularność i analizę harmoniczną od twierdzeń PDE. Rozważyć tomy I (liniowe), II (nieliniowe), III (numeryka) dopiero po pokryciu.
- **Audyt:** Liczne audyty; wskazany raport kontrolny istnieje, bieżące zaawansowanie niezweryfikowane dla wszystkich 33. [Dokument](../../audits/partial_differential_equations/chapter-11/control_184-186_2026-11-25.md).
- [Aktywny katalog rozdziałów](../../books/pl/partial_differential_equations.tex).

### RP1 — Prawdopodobieństwo I (16)

- **Rdzeń:** Prawdopodobieństwo, rozkłady, zbieżność, prawa wielkich liczb, CTG, warunkowa wartość oczekiwana, dyskretny Markow i martyngały.
- **Plan / granice:** Dokończyć audyty rozdziałowe, kontrola RP1 10–15; uzupełnić po sprawdzeniu funkcje charakterystyczne, twierdzenia graniczne, koncentrację, sprzężenia. ME abstrakcyjna miara, RP1 zastosowania probabilistyczne.
- **Audyt:** Brak raportów w standardowym audits/probability_volume_i w migawce; nie oznacza braku pracy.
- [Aktywny katalog rozdziałów](../../books/pl/probability_volume_i.tex).

### RP2 — Prawdopodobieństwo II – procesy (15)

- **Rdzeń:** Konstrukcje procesów, trajektorie, Poisson, Markow, Gauss, Wiener, odnowa, rozgałęzienia, martyngały ciągłe i skoki.
- **Plan / granice:** Potwierdzić pokrycie procesów stacjonarnych, ergodyczności, silnej własności Markowa, regularności i kompensatorów. Granica RP2/RP3: własności procesów vs całki stochastyczne. Kontynuować indywidualne audyty.
- **Audyt:** Brak standardowego rejestru w migawce; status do odtworzenia.
- [Aktywny katalog rozdziałów](../../books/pl/probability_volume_ii.tex).

### RP3 — Prawdopodobieństwo III – analiza stochastyczna (17)

- **Rdzeń:** Całki Wienera, Itô i Stratonovicha, SDE, Girsanow, Lévy, półmartyngały, całki po trajektoriach.
- **Plan / granice:** Uzupełnić po audycie lokalizację i ogólny rachunek półmartyngałowy, rozkłady, SDE ze skokami, SPDE jako most do RRC; całki Feynmana odróżnić od probabilistycznej miary Wienera. Zastosowania finansowe opcjonalnie później.
- **Audyt:** Brak standardowego rejestru w migawce; status do odtworzenia.
- [Aktywny katalog rozdziałów](../../books/pl/probability_volume_iii.tex).

### RP4 — Prawdopodobieństwo IV – statystyka (33)

- **Rdzeń:** Estymacja, testowanie, regresja, Bayes, MCMC, bootstrap, modele zależne, ANOVA/ANCOVA i wielowymiarowe.
- **Plan / granice:** Audyt 00–32; systematyczne porównania testów, założeń, mocy, diagnostyki Shapiro–Wilka, efektów i interpretacji; przykłady z rzeczywistymi/syntetycznymi danymi. Wnioskowanie przyczynowe i modele mieszane rozwijać w tym tomie.
- **Audyt:** Brak standardowego rejestru w migawce; status do odtworzenia.
- [Aktywny katalog rozdziałów](../../books/pl/probability_volume_iv.tex).

### AM1 — Analiza matematyczna I (43)

- **Rdzeń:** Systemy liczbowe w ujęciu analitycznym, analiza jednowymiarowa, klasyczne całki.
- **Plan / granice:** Po AM II: 01–35 zachować, dodać jednowymiarową miarę i całkę Lebesgue’a, twierdzenia graniczne, porównanie Riemann/Darboux/Lebesgue, FTC dla AC. 36–43 → RTPC z zachowaniem BV/AC potrzebnego tutaj; sprawdzić odsyłacze AM2-29. Funkcje specjalne rzeczywiste, kwadratury i całki niewłaściwe pozostają.
- **Audyt:** Raport 27.11: integracja 36–43 i etykiety IT sprawdzone, CI PASS dla wskazanego SHA; pełna wizualna kontrola i semantyka niepotwierdzone w tym raporcie. [Dokument](../../audits/mathematical_analysis_i/final_control_11_integral_redistribution.md).
- [Aktywny katalog rozdziałów](../../books/pl/mathematical_analysis_i.tex).

### AM2 — Analiza matematyczna II (34)

- **Rdzeń:** Szeregi funkcyjne, rachunek wielowymiarowy, elementarny Fréchet, podrozmaitości euklidesowe, całkowanie i Stokes.
- **Plan / granice:** Priorytet: audyt restrukturyzacji sześciu części, zgodność kolejności Atlas/CI/PDF; dokończyć AM2-33, formy i strumień AM2-34, Stokes AM2-35, analityczność rzeczywistą, aproksymację, kwadratury. Pełne całki wektorowe AM2-10/25 → RTPC później; pozostawić tylko potrzebny lemat o przyroście i odsyłacze. Bez Fourier, Mawhina/Pfeffera i rachunku ułamkowego.
- **Audyt:** Restrukturyzacja zapisana; CI/PDF i audyt integracji do potwierdzenia. Rozdział 33 wymaga końcowej bramki. [Dokument](../../docs/pl/plan_analizy_matematycznej_ii.md).
- [Aktywny katalog rozdziałów](../../books/pl/mathematical_analysis_ii.tex).

## 4. Rejestr migracji i zależności (nie wykonywać na podstawie samego planu)

| ID | Źródło | Cel | Zakres i warunek |
|---|---|---|---|
| M01 | AM II 36,25,30,32,33 | AM II | zmiana kolejności już zapisana; audyt numeracji i odsyłaczy, nie zmieniać stabilnych ID bez mapy |
| M02 | AM I 36–43, archiwalne IT | RTPC | KH, McShane, Denjoy, Perron, Stieltjes, całki cechowane; BV/AC klasyczne zostają w AM I, przenieść odsyłacze AM2-29 |
| M03 | AF 15A–15B, AM II 10/25, ME30 | RTPC | teoria całek wektorowych i uogólnionych; elementarny lemat przyrostu w AM II, RNP/miary wektorowe w ME; inwentaryzacja materiałów AM2 w docs/pl/am2_materials |
| M04 | AF14–15, część AF16 | FSG | istniejący [kandydat](../../catalog/function_space_geometry_migration.json); zachować etykiety i zależności AM II, nie rejestrować bez kompilacji |
| M05 | AF/AM II/RRC | DT | [plan struktury](../../catalog/distribution_theory_structure_plan.json), [migracja](../../catalog/distribution_theory_migration.json); Fourier, Laplace i całki osobliwe, RRC zachowuje zastosowania |
| M06 | LTM i dawna MOD | MOD/MM/NL/LTM | [mapa](../../catalog/logic_model_migration.json); archiwum, deduplikacja, etykiety historyczne; teoria mnogości zaawansowana pozostaje LTM |
| M07 | DG03–09, AT01–03/30 | LA/AA/CAT/TO/AT | wskazać kanoniczny dowód, nie usuwać pomostów zastosowań; najpierw audyt semantyczny |
| M08 | AT23–28, ALG04/09/10, CAT29–30/39+ | CAT/ALG/GAZ/AT | formalizm snopowy w CAT; geometria algebraiczna w ALG, zespolona w GAZ, topologiczne zastosowania w AT |
| M09 | GT18–34 vs DG17–20 i AT | GT tom II / DG / AT | propozycja rozdzielenia grafów i węzłów; Seiberg–Witten i plumbing: zachować zastosowania, podstawy analityczne RRC/DG |
| M10 | GA/BT wycofane skrypty | AA | sprawdzić wszystkie etykiety, semantykę i regresje; nie tworzyć ponownie bez uzasadnienia |
| M11 | LA22–28, AA51–72 | LA/AA | potencjalne wydzielenie sterowania i teorii Liego/reprezentacji tylko po analizie rozmiaru i pokrycia; obecnie nie migrować |
| M12 | DG, ME31, AM II | DG/FSG/ME | dżety i geometria: właściciel geometryczny, ME zachowuje zastosowania miarowe |
| M13 | DG01–20, AT09/11/17–21/30 | DG/TD | zatwierdzone rozdzielenie; DG01–04/10–16 jako kandydaci geometryczni, DG15–20 jako kandydaci topologiczni; rozdzielić na poziomie sekcji, unikać podwójnych etykiet |
| M14 | GT22–34, DG/AT, RRC | DG4/TD4 | odrębne opracowania geometrii i topologii czterowymiarowej; zachować GT jako źródło teorii węzłów i splotów |
| M15 | LA/AA/DG/ALG/AM I | GK/AZ I–II | geometrie modelowe i rzutowe, grupy przekształceń, gotowe zespolone funkcje elementarne; dowody algebraiczne pozostają u właścicieli |
| M16 | AF/LA/RRC/AA/FSG | RZUD | ODE, przepływy, układy dynamiczne, stabilność, sterowanie tylko w zakresie potrzebnym dla ODE; istniejące dowody i zastosowania zachować |
| M17 | MOD/LTM/AM I/AA/ME | AN/PA | ultrailoczyny i transfer, liczby hiperrzeczywiste, liczby p-adyczne i wartościowania; odróżniać analizę niestandardową od niearchimedesowskiej |
| M18 | AA09–18, 37–40; ALG00/04 | AP | algebra przemienna: porównać pełne tezy i dowody, wydzielić materiał zaawansowany; AA zachowuje kurs podstawowy, ALG zastosowania geometryczne |
| M19 | AA15–18/41–42/53–72, CAT22–25/44 | ANP | algebra nieprzemienna: moduły, pierścienie, reprezentacje, Morita; nie przenosić automatycznie całej teorii Liego ani kategorii pochodnych |
| M20 | AF31–33, CAT44, DG/AT, ANP | GNP | geometria nieprzemienna: AF właściciel ogólnej teorii operatorów, CAT formalizmu kategorialnego, GNP właściwych konstrukcji geometrycznych |
| M21 | GT24, DG, CAT38, ALG (plan stosów), AT | ORB | geometria orbifoldów; zachować zastosowania Seiferta w GT, formalizm stosów w CAT i algebraiczne stosy w ALG; audyt pełnych tez przed migracją |

## 5. Nowe skrypty i ich program

**Zatwierdzony kierunek: RTPC — Rozszerzona teoria pochodnej i całki.**
- I. Uogólnione pochodne: Dini, pochodna aproksymatywna, różniczkowalność prawie wszędzie, związki z BV/AC i Rademacherem (ME).
- II. Całki skalarne: podziały cechowane, Cousin, Kurzweila–Henstocka, McShane'a, Denjoya (wąska i szeroka), Perrona, Riemanna–Stieltjesa, Kurzweila–Stieltjesa; charakterystyki funkcji pierwotnych, Hake, zbieżność i porównania.
- III. Wielowymiarowe: całki cechowane, Mawhina, Pfeffera, odpowiednie wersje twierdzeń całkowych i granice zakresu.
- IV. Wektorowe: Riemanna w przestrzeniach Banacha, całkowanie w przestrzeniach lokalnie wypukłych, Bochnera, Pettisa, Dunforda, Gelfanda i Birkhoffa; mierzalność, relacje klas, Fubini, różniczkowanie, kontrprzykłady. ME pozostaje właścicielem miar wektorowych i własności Radona–Nikodyma.
- V. Rachunek ułamkowy: Riemanna–Liouville'a, Caputo, Grünwalda–Letnikova, Riesz, warunki równoważności, kompozycje i przykłady; DT/PDE odsyłacze do operatorów i zastosowań.
- Dodać tabelę klas całkowalności, inkluzje wraz z hipotezami, kontrprzykłady i indeks metod. Nie tworzyć duplikatu wycofanej Teorii całki.

**FSG — Geometria różniczkowa przestrzeni Banacha:** istniejący kandydat, jeszcze niezarejestrowany w sprawdzonym katalogu. Gâteaux/Fréchet, Bastiani, wyższe pochodne, lokalne twierdzenia, podrozmaitości Banacha, wiązki, koneksje, metryki słabe/silne, przestrzenie odwzorowań, rozkłady jedności przy odpowiednich hipotezach, rachunek wariacyjny. AF zachowuje funkcjonalne podstawy; AM II elementarny pomost.

### 5.1. Zatwierdzone nowe kierunki (28.11.2026)

Kierunki zatwierdzone przez użytkownika; poniższe szczegółowe programy i robocze identyfikatory są propozycją organizacji, nie poleceniem natychmiastowego tworzenia rozdziałów. GAZ wstępnie dwutomowa. Pierwszeństwo zachowuje kolejność AM II → AM I → RTPC.

#### AZ I — Analiza zespolona jednej zmiennej
1. Liczby zespolone, geometria płaszczyzny i sfery Riemanna (AM I, GK); funkcje elementarne i gałęzie, wykorzystać [materiały zespolone](complex_analysis_materials/README.md).
2. Holomorficzność, równania Cauchy'ego–Riemanna, całki po krzywych, twierdzenie i wzór Cauchy'ego, twierdzenie Morery, rozwinięcia Taylora i Laurenta, osobliwości.
3. Residua, zasada argumentu, Rouché, całki rzeczywiste, funkcje meromorficzne, iloczyny Weierstrassa, Mittag–Leffler.
4. Odwzorowania konforemne, automorfizmy dysku, Schwarz–Pick, rodziny normalne, Montel, twierdzenie Riemanna o odwzorowaniu, twierdzenia Picarda.
5. Funkcje harmoniczne i subharmoniczne, problem Dirichleta, jądro Poissona, teoria potencjału i przestrzenie Hardy'ego/Bergmana w dysku; podstawy powierzchni Riemanna.
6. Zależności: AM I/II, TO, ME; algebraiczna konstrukcja liczb pozostaje AM I/AA; pełny formalizm snopowy GAZ/CAT.

#### AZ II — Analiza zespolona wielu zmiennych
1. Holomorficzność w C^n, szeregi wielowymiarowe, Hartogs, twierdzenia o osobnej holomorficzności, dziedziny zbieżności.
2. Obszary holomorficzności, otoczki holomorficzne, funkcje plurisubharmoniczne, pseudowypukłość, forma Leviego, problem Leviego.
3. Formy typu (p,q), operator d-bar, całkowe reprezentacje i rozwiązywanie d-bar, oszacowania L² i regularność przy odpowiednich hipotezach.
4. Obszary klasyczne, odwzorowania właściwe, biholomorfizmy, automorfizmy, geometria brzegu.
5. Jądra Bergmana i Szegő, metryki i odległości Carathéodory'ego, Kobayashiego i Bergmana, twierdzenie Lemperta, geodezyjne zespolone.
6. Interpolacja Nevanlinny–Picka, zagadnienia ekstremalne, funkcje wewnętrzne, związki z teorią operatorów (AF).
7. Zależności: AZ I, AM II, ME, AF, DG; algebra lokalna i snopy analityczne rozwijane w GAZ, nie powielać ich pełnej teorii.

#### GK — Geometria klasyczna: planimetria, stereometria, geometrie modelowe i rzutowe, program Kleina

Doprecyzowanie użytkownika z 28.11.2026: klasyczna geometria euklidesowa, jej twierdzenia, konstrukcje i obliczenia mają stanowić znaczną, samodzielną część skryptu, a nie krótki wstęp do geometrii abstrakcyjnych. Rozwijać od elementarnych pojęć do zaawansowanych twierdzeń geometrii syntetycznej; prowadzić pełne dowody, liczne zadania i czytelne rysunki z oznaczeniami. Poniższe części są roboczym programem, bez deklaracji istniejącego pokrycia.

**Blok A — klasyczna geometria euklidesowa (główny trzon):**
1. Podstawy aksjomatyczne: punkty, proste, płaszczyzny, odcinki, półproste, kąty, incydencja, porządek, przystawanie, proste równoległe i prostopadłe, postulat Euklidesa.
2. Trójkąty: klasyfikacja, suma kątów, nierówność trójkąta, cechy przystawania i podobieństwa, twierdzenia Talesa i Pitagorasa (z twierdzeniami odwrotnymi), twierdzenia o wysokości i przyprostokątnych, dwusieczne, środkowe i symetralne.
3. Szczególne punkty i proste trójkąta: środek ciężkości, ortocentrum, środki okręgów wpisanego i opisanego, okręgi dopisane, prosta Eulera, okrąg dziewięciu punktów; twierdzenia Cevy, Menelaosa, Stewarta, Simsona, Morleya i Napoleona.
4. Czworokąty i wielokąty: równoległoboki, trapezy, romby, prostokąty, deltoidy, wielokąty foremne, wypukłość, przekątne, kąty i triangulacje.
5. Okręgi i koła: kąty środkowe i wpisane, cięciwy, sieczne, styczne, potęga punktu, oś i środek potęgowy, czworokąty wpisane i opisane, twierdzenia Ptolemeusza, Pitota (z poprawnym zakresem), Miquela, styczność okręgów.
6. Pola figur: pojęcie pola, addytywność i niezmienniczość, rozkłady na figury, pola trójkątów i wielokątów, wzory Herona i Brahmagupty (z hipotezami), pola koła, wycinków i odcinków kołowych, skala podobieństwa, obwody, nierówność izoperymetryczna w odpowiednim zakresie. Rozróżnić pole i obwód; ogólne całkowe uzasadnienia odsyłać do AM II/ME.
7. Trygonometria geometryczna: twierdzenia sinusów i cosinusów, wzory na pola, rozwiązywanie trójkątów, kąty i długości w konstrukcjach. AM I pozostaje właścicielem analitycznej teorii funkcji trygonometrycznych.
8. Przekształcenia: symetrie osiowe i środkowe, obroty, przesunięcia, jednokładności, podobieństwa, inwersja, składanie przekształceń i ich niezmienniki. Klasyczne konstrukcje cyrklem i linijką, kryteria wykonalności z odsyłaczem do AA30.
9. Geometria analityczna płaszczyzny: układy współrzędnych, równania prostych i okręgów, odległości, iloczyn skalarny, metody wektorowe, przekroje stożkowe (elipsa, parabola, hiperbola), ich własności ogniskowe i styczne. LA zapewnia aparat algebraiczny.
10. Stereometria: wzajemne położenie prostych i płaszczyzn, rzuty, kąty i odległości, kąty dwuścienne, wielościany, graniastosłupy, ostrosłupy, czworościany, bryły platońskie, walce, stożki, kule, przekroje, pola powierzchni i objętości, podobieństwo brył, zasada Cavalieriego. Powiązać ze wzorami całkowymi AM II oraz wzorem Eulera z GT/AT.
11. Zadania konstrukcyjne i dowodowe, geometria olimpijska: dodatkowe twierdzenia, dowody syntetyczne, analityczne i wektorowe, nierówności geometryczne, przykłady z pełnym rozwiązaniem oraz osobne zadania z podpowiedziami. Nie ograniczać skryptu do tablic wzorów.

**Blok B — uogólnienia klasycznych geometrii:**
12. Geometria afiniczna: incydencja, równoległość, środki ciężkości, przekształcenia afiniczne, niezmienniki, relacja do geometrii euklidesowej.
13. Geometria rzutowa nad ciałem: współrzędne jednorodne, incydencja, dualność, dwustosunek, twierdzenia Desargues'a i Pappusa, przekroje stożkowe, biegunowość, kolineacje, geometrie rzutowe nad ciałami skończonymi. Rozróżnić geometrię rzutową od geometrii algebraicznej odmian rzutowych.
14. Geometria sferyczna i eliptyczna: wielkie koła, trójkąty, trygonometria sferyczna, pola i nadmiar kątowy, izometrie.
15. Geometria hiperboliczna: modele Poincarégo (dysk i półpłaszczyzna/półprzestrzeń), Kleina i hiperboloidy, metryki, geodezyjne, izometrie, trójkąty, przejścia między modelami; porównanie pól, kątów i podobieństwa z geometrią euklidesową.
16. Program erlangeński Kleina: geometria jako działanie grupy, niezmienniki, przestrzenie jednorodne G/H, hierarchia geometrii; geometria Möbiusa, konforemna, inwersyjna, Cayleya–Kleina, geometria Minkowskiego i Lorentza, geometrie Galileusza.
17. Dodatkowe modele: geometria symplektyczna liniowa, geometria skończona, geometrie modelowe wymiaru 3 (osiem geometrii Thurstona jako pomost do TD, bez powielania dowodu geometryzacji); ewentualna geometria Finslera jako most do DG.

**Granice i audyt pokrycia:** LA zachowuje algebrę liniową, formy i grupy macierzowe; AA teorię działań i grup oraz algebraiczne kryteria konstrukcji; AM I/II analityczne dowody dotyczące całek i funkcji; DG lokalną i globalną geometrię różniczkową; ALG schematy; GT/AT ogólne twierdzenia topologiczne. GK jest właścicielem klasycznych dowodów geometrycznych, konstrukcji, pól i objętości figur, modeli i niezmienników. Sprawdzić istniejące rozdziały przed migracją. Rysunki powinny jasno pokazywać konfigurację, założenia, pomocnicze konstrukcje i elementy dowodu; zadania mają narastać od elementarnych do olimpijskich.


#### GAZ I — Geometria analityczna zespolona: teoria lokalna (proponowany tom I)
1. Pierścienie zbieżnych szeregów, zarodki funkcji i zbiorów, twierdzenia Weierstrassa o przygotowaniu i dzieleniu, noetherowskość, analityczne twierdzenie o zerach.
2. Przestrzenie analityczne zredukowane i niezredukowane, morfizmy, wymiar, składowe, regularność i osobliwości.
3. Snopy analityczne, moduły koherentne, twierdzenia Oki o koherencji, lokalna teoria przecięć, krotności, normalizacja.
4. Rozdmuchania, rozwiązywanie osobliwości, przykłady krzywych i powierzchni, porównanie lokalnych pierścieni z ALG.
5. Zależności: AZ II, AA algebra przemienna, CAT snopy, ALG lokalne metody.

#### GAZ II — Geometria analityczna zespolona: teoria globalna (proponowany tom II)
1. Przestrzenie Steina, holomorficzna wypukłość i oddzielanie, twierdzenia Cartana A/B, kohomologia snopów koherentnych.
2. Wiązki holomorficzne, dywizory, grupy Picarda, twierdzenia Cousina, kohomologia Dolbeaulta, dualność Serre'a.
3. Właściwe odwzorowania analityczne, twierdzenia Remmerta, obrazy proste, rodziny i deformacje; przestrzenie moduli w uzasadnionym zakresie.
4. Rozmaitości zwarte zespolone i rozmaitości Kählera, Hodge, twierdzenia o zanurzeniu, Chow, GAGA i precyzyjne porównanie z geometrią algebraiczną.
5. Zależności: GAZ I, AZ II, DG (metryki i formy), CAT (formalizm kohomologiczny), ALG. Nie utożsamiać AZ II z GAZ I/II.

#### RZUD — Równania różniczkowe zwyczajne i układy dynamiczne (jeden skrypt)
1. Równania pierwszego rzędu, metody elementarne, istnienie i jednoznaczność Peana i Picarda–Lindelöfa, ciągła zależność od danych, przedłużanie rozwiązań, eksplozja.
2. Układy liniowe, macierz fundamentalna, zmienność stałych, równania wyższych rzędów, Floquet, równania specjalne, problemy brzegowe i Sturm–Liouville.
3. Przepływy, portrety fazowe, punkty równowagi, linearyzacja, Hartman–Grobman, stabilność Lapunowa i LaSalle'a, rozmaitości stabilne/niestabilne i centralne.
4. Układy płaskie, Poincaré–Bendixson, cykle graniczne, mapy Poincarégo, bifurkacje (siodło–węzeł, Hopf i inne), układy dyskretne i chaos, podkowy i sprzężenia.
5. Układy Hamiltona, całkowalność, podstawy ergodyczności; numeryczne metody Eulera/Rungego–Kutty, stabilność, błędy i przykłady.
6. LA: ogólna teoria macierzy, AA43–50: różniczkowa teoria Galois i algorytm Kovacica, AF: półgrupy operatorów, DG/FSG: ogólne przepływy na rozmaitościach, RRC: charakterystyki i równania cząstkowe. RZUD jest właścicielem podstaw ODE i dynamiki skończenie wymiarowej.

### 5.2. Rozdzielenie geometrii i topologii różniczkowej

Zatwierdzony kierunek: osobne skrypty geometrii i topologii różniczkowej, z pogłębionymi specjalizacjami dla wymiaru 4. Proponujemy cztery jednostki docelowe; ich nazwy i liczba tomów technicznych mogą zostać doprecyzowane po audycie. Wynik ogólnowymiarowy pozostaje w tomie podstawowym nawet wtedy, gdy obowiązuje także w wymiarze 4. Nie powtarzać go w całości.

**DG — Geometria różniczkowa (ogólnowymiarowa):** rozmaitości, wiązki, pola i przepływy, formy, Stokes, metryki riemannowskie i pseudo-riemannowskie, koneksje, geodezyjne, krzywizna, twierdzenia porównawcze, holonomia, grupy i algebry Liego w ujęciu geometrycznym, wiązki główne, charakterystyczne formy Chern–Weila, geometria symplektyczna i kontaktowa, geometria zespolona i Kählera, operatory Hodge'a i Diraca jako pomost do specjalizacji.

**TD — Topologia różniczkowa (ogólna, ze specjalizacją poza wymiarem 4):** Sard, transwersalność, zanurzenia i immersje, otoczenia tubularne, stopień, indeks, Morse i uchwyty, kobordyzmy, konstrukcja Pontriagina–Thoma, h- i s-kobordyzmy, chirurgia w wysokich wymiarach, klasyfikacja i gładkie struktury, sfery egzotyczne, twierdzenia o wymiarach 1–3 oraz wysokich wymiarach z właściwymi ograniczeniami. AT zachowuje teorię homotopii i homologii; GT zachowuje teorię węzłów i splotów. Wyjątki wymiaru 4 omawiane osobno, nie stosować twierdzeń wysokowymiarowych bez sprawdzenia hipotez.

**DG4 — Geometria różniczkowa czterowymiarowa:** rozkład 2-form na samodualne i antysamodualne, krzywizna Weyla i operator krzywizny, rozmaitości Einsteina, geometria Kählera i hiper-Kählera, spin i spin^c, operator Diraca, teoria twistorów w wymiarze 4, koneksje Yang–Millsa, instantony, równania Seiberga–Wittena, analityczna teoria przestrzeni moduli (eliptyczność, teoria cechowania, zwartość, transwersalność). AF/RRC właściciele ogólnych narzędzi operatorowych i PDE, DG ogólnej geometrii.

**TD4 — Topologia różniczkowa czterowymiarowa:** formy przecięcia, układy uchwytów i diagramy Kirby'ego, plumbing, rozróżnienie kategorii TOP/PL/DIFF, twierdzenia Freedmana i Donaldsona z pełnym zakresem hipotez, niezmienniki Donaldsona i Seiberga–Wittena, rozmaitości symplektyczne i algebraiczne jako źródła przykładów, wymierne kontrakcje, chirurgia wzdłuż węzłów, konstrukcje egzotycznych 4-rozmaitości i egzotycznych R^4, ograniczenia klasyfikacji, otwarte problemy. Dowody centralne opracowywać warstwowo, rozróżniając dowody własne, wyniki przytoczone ze sprawdzonych źródeł i zagadnienia otwarte; nie deklarować kompletnego dowodu głębokiego twierdzenia bez rzeczywistego opracowania.

**Migracja:** DG01–04/10–16 → DG z wydzieleniem sekcji topologicznych; DG15–20 → TD w odpowiednich częściach; AT17–21 i GT18–34 przejrzeć na poziomie twierdzeń, dowodów, rysunków i etykiet. GT22–34 jest istotnym istniejącym źródłem dla TD4/DG4. Uzgodnić pełny zakres z ALG i RRC; żadnych usunięć przed odbiorem docelowych tomów. Zachować obecne identyfikatory i raporty do czasu bezpiecznej migracji.

### 5.3. Liczby i inne rodzaje analizy

**TL — Teoria liczb i arytmetyka:** zachować wcześniejszy plan: kongruencje, kwadratowe prawo wzajemności, funkcje arytmetyczne, aproksymacja diofantyczna, algebraiczna teoria liczb (ideały, jednostki, klasy), analityczna teoria liczb (zeta, funkcje L), po sprawdzeniu pokrycia AA.

**PA — Liczby p-adyczne i analiza niearchimedesowska:** plan wspólnego skryptu z dwiema wyraźnymi częściami, z możliwością wydzielenia tomów po ustaleniu objętości. (I) Liczby p-adyczne, wartościowania, konstrukcja Q_p i Z_p, lemat Hensela, rozszerzenia, ciała lokalne, rozgałęzienie i teoria Galois ciał lokalnych. (II) Ogólne ciała niearchimedesowskie, szeregi i funkcje analityczne, całki i miary z wartościami rzeczywistymi lub niearchimedesowskimi (rozróżnić), transformacja Fouriera na grupach lokalnych, przestrzenie Banacha niearchimedesowskie, operatory i podstawy analizy sztywnej/Berkovicha jako rozszerzenie. Zależności AA, TL, ME, AF, DT.

**AN — Analiza niestandardowa (osobny skrypt, nie utożsamiać z PA):** ultrafiltry i ultrailoczyny z MOD, konstrukcja liczb hiperrzeczywistych, zasada transferu, obiekty wewnętrzne/zewnętrzne, część standardowa, nasycenie i jego założenia, nieskończenie małe i nieskończenie duże, granice i ciągłość, różniczkowanie, całkowanie przez sumy hiperskończone, miara Loeba, zastosowania do prawdopodobieństwa, analizy funkcjonalnej i topologii. Rozróżniać uporządkowane ciało liczb hiperrzeczywistych od ciał z wartościowaniem ultrametrycznym. MOD pozostaje właścicielem ogólnego twierdzenia Łosia i podstaw teorii modeli.

### 5.4. Rozbudowa istniejących skryptów

**AF — teoria operatorów, osobna duża część istniejącego skryptu (zatwierdzone):**
- Operatory ograniczone w przestrzeniach Banacha i Hilberta, sprzężone, zwarte, Fredholma, ideały, ślad i klasy Schattena; aproksymacja i wartości osobliwe.
- Operatory nieograniczone: dziedziny, domknięcie i domykalność, sprzężenie, rdzenie, operatory symetryczne, samosprzężone, rozszerzenia i indeksy defektu, operatory normalne; odróżniać symetrię od samosprzężoności.
- Widmo, rezolwenta i typy widma, rachunek funkcyjny wielomianowy, holomorficzny, ciągły i borelowski, twierdzenia spektralne, miary spektralne, rozkład polarny, pierwiastek dodatni.
- Algebry Banacha, C*-algebry, reprezentacja Gelfanda, konstrukcja GNS, algebry von Neumanna (po ustaleniu zakresu), teoria perturbacji, półgrupy C_0, Hille–Yosida, Stone, Lumer–Phillips; połączenia z RRC, mechaniką kwantową, RZUD i AZ II.
- Przed dopisaniem porównać AF26–33, LA14–28, RRC12/18, ME i DT; istniejących dowodów nie powielać. Rozdzielenie na osobny tom operatorowy rozważyć dopiero przy rozroście, obecnie rozwijać AF.

**ALG — geometria algebraiczna (zatwierdzone pogłębienie):**
- Zachować i audytować most od geometrii afinicznej/rzutowej oraz krzywych i powierzchni (ALG00–10) do schematów: Spec, Proj, snopy strukturalne, morfizmy, włókna, produkty, lokalne własności.
- Algebra przemienna (AA/AP): lokalizacja, moduły, noetherowskość, całkowitość, wymiar, płaskość i uzupełnienia; w ALG zastosowania geometryczne, bez powtórnego pełnego kursu.
- Morfizmy właściwe, skończone, gładkie, nierozgałęzione i étale; dywizory Cartiera i Weila, wiązki, kohomologia koherentna, dualność Serre'a, Riemann–Roch/Hirzebruch–Riemann–Roch w odpowiednim zakresie.
- Geometria przecięć i grupy Chowa, klasy charakterystyczne, osobliwości i rozwiązywanie, geometria biwymierna i program modeli minimalnych, geometria rodzin, deformacje i moduli, podstawy stosów (CAT).
- Geometria arytmetyczna: schematy nad Z, krzywe eliptyczne i odmiany abelowe, redukcja, punkty wymierne, wprowadzenie do kohomologii étale; zaawansowane twierdzenia po TL/PA.
- Porównanie z GAZ (analityfikacja, GAGA), AT (kohomologia, Hodge), DG4/TD4 (powierzchnie zespolone i czterorozmaitości). Uzupełnienia dopiero po inwentaryzacji planu lokalnego i pełnych tez ALG00–10.

**Pozostałe wcześniejsze propozycje (niezatwierdzone automatycznie):** wydzielenie teorii Liego i reprezentacji z AA51–72, analiza numeryczna i optymalizacja/sterowanie, teoria informacji i uczenie statystyczne po RP4, zbiór zadań do RP I–IV z podpowiedziami. Nie tworzyć pustych wpisów katalogu.


### 5.5. Dodatkowe zatwierdzone kierunki: algebra i geometria (28.11.2026)

Użytkownik wskazał algebrę przemienną, algebrę nieprzemienną, geometrię nieprzemienną i geometrię różniczkową orbifoldów; ostatnia jest dla niego szczególnie ważna. Poniżej proponowana organizacja w czterech samodzielnych skryptach (ewentualnie blokach większych tomów, jeśli później tak ustalimy). Kierunki zatwierdzone, szczegółowe programy robocze, realizacja po audycie pokrycia. Nie zmieniać bieżącego priorytetu AM II → AM I → RTPC.

#### AP — Algebra przemienna

- Podstawy: pierścienie przemienne, ideały, moduły, lokalizacje, pierścienie lokalne, spektrum i topologia Zariskiego jako pomost do ALG.
- Pierścienie noetherowskie i artinowskie; rozkłady prymarne, ideały stowarzyszone, lemat Nakayamy, twierdzenie o bazie Hilberta.
- Moduły skończenie generowane, dokładność, iloczyn tensorowy, płaskość i wierna płaskość, moduły rzutowe i injektywne. CAT właściciel ogólnych konstrukcji homologicznych; AP ich realizacji dla pierścieni przemiennych.
- Rozszerzenia całkowite, normalizacja, twierdzenia going-up/going-down, dziedziny Dedekinda i pierścienie wartościowań, wymiar Krulla, twierdzenia o wysokości ideałów.
- Filtracje, algebry graduowane i algebry Reesa, uzupełnienia adyczne, twierdzenia Artina–Reesa i Krulla, funkcja i wielomian Hilberta–Samuela, krotności.
- Ciągi regularne, głębokość, pierścienie regularne, Cohen–Macaulaya i Gorensteina, zupełne przecięcia, formuła Auslandera–Buchsbauma, kohomologia lokalna i dualność lokalna.
- Różniczki Kählera, formalna gładkość, algebraiczne podstawy deformacji, kompleks kotangensowy w uzgodnieniu z CAT/ALG.
- Istniejące źródła: AA09–14,16–18,37–40; ALG00 i ALG04, w którym sprawdzono sekcje o lokalizacji, modułach, płaskości, normalizacji, wymiarze, ideałach prymarnych i różniczkach Kählera. AA zachowuje podstawowy kurs, ALG zastosowania geometryczne; nie wycofywać żadnego wyniku przed sprawdzeniem pełnych hipotez, etykiet i audytów.

#### ANP — Algebra nieprzemienna

- Pierścienie i algebry nieprzemienne, ideały jednostronne, pierścień przeciwny, bimoduły, wolne algebry, algebry grupowe.
- Moduły proste i półproste, radykał Jacobsona, twierdzenie Artina–Wedderburna, pierścienie pierwotne, twierdzenie o gęstości Jacobsona.
- Równoważność Mority, progeneratory, centralne algebry proste, algebry z dzieleniem, grupa Brauera i jej związek z teorią Galois.
- Lokalizacja Orego, teoria Goldiego, pierścienie ilorazowe, pierścienie noetherowskie, dziedziny nieprzemienne, algebry Weyla, rozszerzenia Orego.
- Tożsamości wielomianowe, PI-algebry, algebra homologiczna pierścieni (wymiary globalne i homologie), dualność i kategorie pochodne z CAT.
- Kołczany, algebry ścieżek i reprezentacje; algebry skończenie wymiarowe, typy reprezentacji, podstawy teorii Auslandera–Reiten.
- Algebry Hopfa, bialgebry, moduły i komoduły, grupy kwantowe jako dalsza część. Nie utożsamiać algebraicznych grup kwantowych z analityczną teorią lokalnie zwartych grup kwantowych.
- Źródła: AA15 (sprawdzono sekcje: ideały lewo/prawostronne, macierze, pierścienie przeciwne, grupowe i wolne), AA16–18/41–42/53–72, CAT22–25/44. Zachować teorię Liego w AA do odrębnej decyzji; CAT zachowuje abstrakcyjną teorię Mority i pochodnych lokalizacji.

#### GNP — Geometria nieprzemienna

- Motywacja i dualności: przestrzenie a algebry funkcji, przemienne C*-algebry i dualność Gelfanda (dowód ogólny AF), nieprzemienne przestrzenie.
- Algebry grupoidów, iloczyny skrzyżowane, działania grup, przestrzenie ilorazowe, foliowane rozmaitości i ich grupoidy; orbifoldy jako konkretne źródło przykładów.
- Nieprzemienny rachunek różniczkowy: różniczki uniwersalne, koneksje na modułach rzutowych, krzywizna, ślad i całkowanie, homologia Hochschilda, homologia i kohomologia cykliczna, parowania.
- K-teoria topologiczna i operatorowa, K-homologia, KK-teoria Kasparowa, ciągi dokładne i indeksy; abstrakcyjny formalizm CAT/AT, analityczne podstawy AF.
- Trójki spektralne, operator Diraca, gradacja, rzeczywistość, warunek ograniczonych komutatorów i odpowiednie hipotezy zwartości; wzór na odległość Connes'a, wymiar spektralny, ślad Dixmiera, nieprzemienny torus.
- Nieprzemienne twierdzenia indeksowe, geometria foliacji, kwantowanie deformacyjne i wybrane zastosowania w fizyce matematycznej. Rozróżniać formalne kwantowanie i ścisłe kwantowanie.
- Źródła: AF31–33 (AF31 już obejmuje algebry Banacha, widmo, Gelfanda, holomorficzny rachunek funkcyjny i przemienny model C*-algebr), CAT44 (Morita), AA/ANP, AT, DG/DG4, ORB. Nie powielać kursu algebr operatorowych: AF teoria analityczna, GNP geometria. Algebraiczna geometria nieprzemienna (kategorie modułów i qgr, przestrzenie Artina–Zhanga) jako możliwe późniejsze rozszerzenie w porozumieniu z ALG, nie utożsamiać z podejściem spektralnym.

#### ORB — Geometria różniczkowa orbifoldów (szczególny priorytet)

Proponowany samodzielny skrypt, nie tylko rozdział DG. Teorię budować od podstaw, do narzędzi analitycznych i głębokich zastosowań. Zwykła przestrzeń ilorazowa nie wyznacza całej struktury orbifoldu: istotna jest izotropia i dane lokalnych działań.

1. Motywacja: ilorazy rozmaitości przez działania grup skończonych, przykłady stożków, odbić, orbifoldów dobrych i złych, orbifoldy efektywne i nieefektywne. Rozróżniać orbifold z brzegiem od zjawiska lokalnych odbić oraz ustalić konwencje.
2. Atlasy orbifoldowe, mapy lokalne, zgodność, morfizmy i ich podniesienia, grupy izotropii, warstwy osobliwe, przestrzeń podległa; równoważne opisy przez właściwe étale grupoidy Liego i równoważność Mority. Działania lokalnie swobodne grup Liego przy właściwych hipotezach; orbifoldy a stosy różniczkowe.
3. Różniczkowanie, funkcje gładkie, pola, formy, rozkłady jedności, przestrzenie styczne i wiązki orbifoldowe, orientacja, całkowanie lokalne z właściwą normalizacją izotropii, twierdzenie Stokesa.
4. Metryki riemannowskie, koneksje, geodezyjne, krzywizna, zupełność, twierdzenia porównawcze w zakresie uzasadnionych hipotez; orbifoldy stałej krzywizny i związki z GK.
5. Nakrycia orbifoldowe, orbifoldowa grupa fundamentalna, uniwersalne nakrycie w odpowiednim sensie, charakterystyka Eulera Satakego; rozróżnić charakterystyki Eulera przestrzeni podległej, orbifoldu i sektora bezwładności.
6. Orbifoldy dwuwymiarowe: stożki, punkty lustrzane, kąty, klasyfikacja i uniformizacja, grupy trójkątne, przykłady sferyczne, euklidesowe i hiperboliczne. Powiązać z rozmaitościami Seiferta i geometriami modelowymi wymiaru 3.
7. Kohomologia de Rhama orbifoldów, klasy charakterystyczne, twierdzenie Gaussa–Bonneta, dualności przy odpowiednich założeniach, orbifold bezwładności i kohomologia Chen–Ruana; nie utożsamiać jej ze zwykłą kohomologią przestrzeni podległej.
8. Analiza na orbifoldach: przestrzenie Sobolewa, Laplace, operatory eliptyczne, jądro cieplne, teoria Hodge'a, operatory Diraca i struktury spin/spin^c, twierdzenia indeksowe Kawasaki. RRC i AF dają teorię operatorową i analityczną; w ORB dowody adaptacji i nowe składniki izotropowe.
9. Orbifoldy zespolone, Kählera i symplektyczne; redukcja symplektyczna, ważone przestrzenie rzutowe, osobliwości ilorazowe, rozwiązywanie osobliwości i korespondencja McKaya jako połączenie z AA/ALG/GAZ.
10. Orbifoldy wymiaru 4: geometria samodualna, teoria cechowania, przestrzenie moduli i związki z rozwiązywaniem osobliwości. Specjalistyczne zastosowania topologiczne i geometryczne w DG4/TD4 z odsyłaczami.
11. Orbifoldy w geometrii nieprzemiennej: algebry grupoidów, K-teoria orbifoldowa, trójki spektralne i indeksy; GNP zachowuje ogólne narzędzia nieprzemienne.
12. Liczne rysunki: lokalne ilorazy R² przez grupy cykliczne i dihedralne, stożki, orbifoldy sferyczne i hiperboliczne, ważone przestrzenie rzutowe jako porównanie, modele rozmaitości Seiferta. Wyjaśniać, które rysunki przedstawiają tylko przestrzeń podległą, a które dane izotropii.

Źródła do pierwszego audytu pokrycia: GT24 (sekcja o orbicharakterystyce Eulera i geometrii, etykieta sec:tg-seifert-orbifold), CAT38 (zstępowanie, torsory, stosy ilorazowe), DG01/10–16, AT (nakrycia, kohomologia, klasy charakterystyczne), GK (plan), AA (działania grup), ALG (plan stosów Deligne'a–Mumforda i osobliwości), AF/RRC (analiza eliptyczna). Nie utożsamiać gładkich orbifoldów z dowolnymi stosami Deligne'a–Mumforda; porównać odpowiednie kategorie i hipotezy. ORB powinien otrzymać szczegółowe audyty definicji, niezależności od atlasu, normalizacji całek oraz przypadków osobliwych.

### 5.6. Dodatkowe propozycje do decyzji użytkownika

Poniższe kierunki nie są jeszcze zatwierdzonymi nowymi skryptami. Najpierw ocenić pokrycie obecnych i zaplanowanych książek.

- **Geometria symplektyczna i kontaktowa:** formy symplektyczne, Darboux, Moser, redukcja, odwzorowania momentu, geometria lagranżowska, krzywe pseudoholomorficzne, homologia Floera. Początkowo DG; po rozroście samodzielny tom. Ważny most do TD4, ORB i RZUD.
- **Grupy Liego i teoria reprezentacji:** grupy Liego, algebry Liego, reprezentacje, działania, przestrzenie jednorodne, reprezentacje grup zwartych, Peter–Weyl, reprezentacje unitarne i metody harmoniczne. AA51–72, DG, GK, DT jako źródła; bez automatycznej migracji.
- **K-teoria i teoria indeksu:** wiązki, K-teoria topologiczna, okresowość Botta, K-teoria algebraiczna i operatorowa z rozróżnieniem, operatory Fredholma, indeks Atiyaha–Singera, warianty rodzinne i orbifoldowe. Najpierw wspólna mapa AT/ALG/AF/DG/ORB/GNP; osobny skrypt dopiero jeśli ułatwi uniknięcie duplikacji.
- **Grupoidy Liego, algebroidy i geometria stosów różniczkowych:** grupoidy, algebroidy, integracja, równoważność Mority, foliacje, geometria Poissona, stosy różniczkowe. Początkowo DG/ORB/CAT, osobny tom tylko przy dużej objętości.
- **Geometria metryczna i geometryczna teoria miary:** przestrzenie długości, geodezyjne, Gromov–Hausdorff, przestrzenie CAT(k), krzywizna w sensie Aleksandrowa, przestrzenie metryczno-miarowe, transport optymalny i krzywizna syntetyczna; ME24–29 jako punkt wyjścia.
- **Geometria Poissona i kwantowanie:** nawiasy Poissona, struktury Poissona, algebroidy, kwantowanie geometryczne i deformacyjne, powiązania z symplektyką i GNP. Najpierw rozdziały DG/GNP, wydzielenie później.
- **Topologia geometryczna wymiaru 3:** rozkłady JSJ, geometrie Thurstona, rozmaitości hiperboliczne, teoria węzłów i splotów, geometryzacja. Rozważyć wraz z GT/TD; nie dublować dotychczasowych rozdziałów o Seifercie.
- **Teoria osobliwości:** osobliwości odwzorowań gładkich i analitycznych, stabilność, katastrofy, osobliwości ADE, włókna Milnora, monodromia i cykle zanikające. Początkowo DG/GAZ/ALG/AT, później ewentualna synteza.


## 6. Mapa kanonicznych właścicieli (skrót przed dodawaniem)

| Temat | Właściciel | Skrypty korzystające |
|---|---|---|
| Klasyczna całka skalarna | AM I (1D), AM II (nD), ME (abstrakcyjna) | RP, RRC, DG |
| Całki uogólnione, wektorowe i ułamkowe | RTPC | AF, AM I/II, ME, DT, RRC |
| Różniczkowanie elementarne / Banach | AM I/II / FSG | AF, DG, RRC |
| Funkcje testowe, dystrybucje i Fourier | DT | RRC, AF, RP, ME |
| Miara Hausdorffa i pole/koobszar ogólne | ME | AM II gładkie parametryzacje, DG |
| Formy, Stokes i orientacja | AM II (euklidesowe), DG (abstrakcyjne) | AT, RRC |
| Algebra homologiczna, kategorie pochodne | CAT | AT, ALG, DG, AA |
| Homologia/kohomologia przestrzeni | AT | DG, GT, ALG |
| Macierze, formy i tensory | LA | AA, DG, AF, RRC |
| Algebra podstawowa i Galois | AA | AP, ANP, ALG, TL, MOD |
| Algebra przemienna zaawansowana | AP | ALG, GAZ, TL, PA |
| Algebra nieprzemienna | ANP | GNP, AA, CAT, AF |
| Geometria nieprzemienna | GNP | AF, ORB, DG, DG4 |
| Geometria różniczkowa orbifoldów | ORB | DG, TD, DG4, TD4, GT, GAZ, ALG, GNP |
| Prawdopodobieństwo/procesy/całki stochastyczne/statystyka | RP1/RP2/RP3/RP4 | RRC, GT, RTPC |
| Operatory i widmo | AF | RRC, DT, FSG, DG4 |
| Planimetria, stereometria, klasyczne twierdzenia, geometrie modelowe, rzutowe i program Kleina | GK | AM I/II, LA, DG, ALG, AZ, PA |
| Analiza holomorficzna | AZ I (jedna zmienna), AZ II (wiele zmiennych) | GAZ, ALG, AF |
| Geometria przestrzeni analitycznych | GAZ I–II | AZ, ALG, AT |
| ODE i układy dynamiczne | RZUD | DG, FSG, RRC, RP3 |
| Geometria różniczkowa ogólna i czterowymiarowa | DG, DG4 | TD, TD4, RRC |
| Topologia różniczkowa ogólna i czterowymiarowa | TD, TD4 | AT, GT, DG |
| Analiza niestandardowa | AN | AM, ME, MOD |
| Analiza niearchimedesowska i p-adyczna | PA | TL, AA, GAZ, AF |
| Topologia ogólna i metryzacja | TO | AM, AF, DG, AT |
| Logika klasyczna i mnogości / modele / niezupełność / logiki alternatywne | LTM / MOD / MM / NL | CAT, AA, TL |

## 7. Audyt: dwie niezależne osie

**Merytoryka:** NIEUSTALONY → INWENTARYZACJA → ROBOCZY → STABILIZACJA → CZYSTY → KONTROLNY/ZAMKNIĘTY. Zmiana wpływająca na dowody → PONOWNY AUDYT dotkniętego zakresu.

**Technika:** NIEUSTALONA / OCZEKUJE / FAIL / ANULOWANY / PASS CI / PDF SPRAWDZONY. Niezależnie: formalizacja Lean = brak / szkic / kompilacja / zgodność ze sformułowaniem zweryfikowana; sama kompilacja nie jest dowodem zgodności.

Bramki:
- A0: inwentaryzacja i pełne hipotezy, źródło kanoniczne, brak kołowości.
- A1: każdy dowód, definicja, wzór, przykład i kontrprzykład; każdy nieuzasadniony wzór ma dowód lub dokładny odsyłacz.
- A2: język i notacja (chi_A, d lambda_n(x), d H^k(x), zbieżność zmajoryzowana, mapa, zanurzenie, uzwarcenie, suma zbiorów, pełne nazwy przestrzeni).
- A3: spójność rozdziałów i między skryptami; oryginalne etykiety, unikalność, poprawne cele; nie mylić numeru druku z ID.
- A4: skład, rysunki (pełne powierzchnie tam, gdzie potrzebne), Plotly w Atlasie, kod Python/Julia, regresje.
- A5: stabilizacja do zera usterek; niezależny audyt kontrolny na tym samym blobie.
- A6: CI dla źródła, rzeczywisty PDF (liczba stron, spis treści, render, odsyłacze, log), aplikacja. PASS starego źródła nie jest PASS nowego. Jeżeli CI anulowany, odnotować.
- A7: aktualizacja rejestru. Nie otwierać ponownie zamkniętych audytów bez konkretnej usterki lub zmiany; nie oznaczać całej książki jako stabilnej na podstawie jednego rozdziału.

**Minimalny rekord audytu do uzupełnienia po każdym przebiegu:**

```yaml
book_id: ...
chapter_id: ...
path: ...
source_blob: ...
scope: ...
semantic_status: nieustalony
audit_reports: []
open_issues: []
control_report: null
ci_run: null
ci_status: nieustalony
pdf_artifact: null
pdf_pages: null
visual_review: nieustalony
lean_status: nieustalony
next_action: ...
```

Indeks JSON zawiera wszystkie aktywne pliki z blobami w migawce i ścieżki raportów wykrytych po nazwach. Kandydat na raport nie jest dowodem jego zakresu. Status rozdziału ma być ustawiany dopiero po odczytaniu raportu, zgodności blobu i właściwych bramek. Dla starszych skryptów z inną konwencją raportowania odtworzyć mapę, nie zmyślać danych.

## 8. Najbliższe konkretne zadania

- [ ] AM II: audyt restrukturyzacji (katalog, kolejność Atlasu, tekstowe numery, odsyłacze, testy, PDF), domknąć AM2-33.
- [ ] AM II: formy/strumień, Stokes, pozostałe uzupełnienia, końcowy audyt.
- [ ] AM I: inwentaryzacja 36–43, wydzielenie BV/AC, klasyczna całka Lebesgue'a w R, przeniesienie rozszerzeń dopiero po działającym celu.
- [ ] RTPC: mapa źródło–cel–etykiety, rejestracja i audyty migracji AM I, AF, AM II, ME.
- [ ] FSG: sprawdzić aktualność kandydata i migrację AF14–15 bez zerwania AM II.
- [ ] Uzupełnić rejestr per rozdział dla wszystkich książek, poczynając od aktywnych wątków; wykorzystać już wykonane audyty.
- [ ] Przygotować mapy pokrycia i zależności AZ I–II, GK, RZUD, GAZ I–II, AN i PA; nie tworzyć pustych skryptów.
- [ ] Przygotować szczegółową mapę rozdzielenia DG/TD/DG4/TD4, z inwentaryzacją GT/AT/RRC i audytów źródłowych.
- [ ] AF: teoria operatorów i ALG: pogłębienie geometrii algebraicznej — audyty pokrycia i kolejność rozwoju.
- [ ] AP/ANP: audyt pokrycia AA/ALG/CAT, mapa kanonicznych etykiet i program samodzielnych skryptów.
- [ ] ORB (szczególny priorytet użytkownika): inwentaryzacja GT24, CAT38, DG, AT i źródeł dotyczących działań grup, geometria lokalna i globalna, grupoidy, przykłady, plan dowodów.
- [ ] GNP: audyt pokrycia AF31–33, CAT44, AT i ANP; ustalić zależności operatorowe, homologiczne i geometryczne.
- [ ] Cross-check właścicieli tematów przed każdym nowym rozdziałem. Zmieniać plan po decyzji użytkownika, nie traktować propozycji P2/P3 jako nakazu implementacji.

## 9. Dokumenty lokalne i techniczne

Niniejszy plan ma pierwszeństwo przy sprzecznościach zakresu, plany lokalne pozostają szczegółowymi listami roboczymi. [AM I](plan_analizy_matematycznej_i.md), [AM II](plan_analizy_matematycznej_ii.md), [AA](plan_algebry_abstrakcyjnej_aa43_plus.md), [LA](plan_algebry_liniowej.md), [ALG](plan_geometrii_algebraicznej.md), [TO](plan_topologii_ogolnej.md), [DT](plan_uzupelnien_teorii_dystrybucji_fourier.md), [LTM/MOD](plan_rozdzielenia_logiki_i_teorii_modeli.md), [NL](plan_logiki_niestandardowej.md), [MM](plan_metamatematyki_i_teorii_obliczalnosci.md), [graf odsyłaczy](plan_globalnego_grafu_odsylaczy.md), [Atlas](../../application/docs/ATLAS_DEVELOPMENT_ROADMAP.md), [Lean](../../application/docs/LEAN_FORMALIZATION_PLAN.md).
