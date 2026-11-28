# PLAN GLOBALNY BIBLIOTEKI MATEMATYCZNEJ

**Wersja 1.0 — 28.11.2026.** Nadrzędny dokument roboczy. Migawka katalogu: [8e104a7](https://github.com/dariusz-piekarz/mathematical_scipts/commit/8e104a732fb4293b1f23f06774f01f8d6e17d96c). Gałąź robocza: biblioteka-matematyczna-iteracja-6. **22 aktywne skrypty, 607 rozdziałów.** Pełny indeks ścieżek, blobów i kandydatów na raporty: [catalog/global_library_inventory.json](../../catalog/global_library_inventory.json).

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
| P2 | Analiza zespolona, teoria liczb i arytmetyka, analiza p-adyczna | po ustaleniu zależności i pokrycia |
| P3 | Geometria analityczna zespolona, ODE, dalsze specjalizacje | decyzja po podstawowych skryptach |

P0 w wątku AM ma ścisłą kolejność AM II → AM I → RTPC. FSG i inne rozpoczęte wątki mogą być prowadzone osobno pod warunkiem bezpiecznej koordynacji i braku utraty zależności. Nie włączać automatyzacji tym planem.

## 3. Właściciele tematyki i plany wszystkich aktywnych skryptów

### AA — Algebra abstrakcyjna (72)

- **Rdzeń:** Grupy, pierścienie, ciała, moduły, Galois, algebra przemienna, reprezentacje i algebry Liego.
- **Plan / granice:** 01–42 podstawy; 43–50 algebra różniczkowa i Galois; 51–72 niezmienniki, korzenie i reprezentacje. Zachować obecne wyniki; wydzielenie teorii Liego/ reprezentacji rozważyć dopiero przy rozbudowie. Kontrola integracji GA/BT i odsyłaczy. Uzupełnić algebry Hopfa oraz reprezentacje grup skończonych, o ile brak po audycie.
- **Audyt:** Raport globalny AA01–42 istnieje; 43–72 i migracja GA/BT: ustalić bramki per rozdział. [Dokument](../../audits/abstract_algebra/00-globalny-audyt-koncowy-AA01-AA42-2026-11-23.md).
- [Aktywny katalog rozdziałów](../../books/pl/abstract_algebra.tex).

### ALG — Geometria algebraiczna (11)

- **Rdzeń:** Schematy/odmiany algebraiczne, geometria lokalna i globalna, przecięcia, geometria biwymierna.
- **Plan / granice:** 00–10 zachować; rozbudować od schematów: morfizmy, włókna, płaskość, gładkość, étale, koherentne snopy, kohomologia, dywizory, Riemann–Roch, moduły, moduli, podstawy arytmetyczne. AA właściciel algebry przemiennej, CAT formalizm snopów. GAGA łącznik z przyszłą GAZ.
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
- **Plan / granice:** DG03–09: formalizm AL/AA/CAT/AT, zachować pomosty i zastosowania. DG10: abstrakcyjne rozmaitości i de Rham, AM II dowód euklidesowy Stokesa. DG17–20 utrzymać w części topologii różniczkowej, uzgodnić z AT i GT. Uzupełnić wiązki, koneksje główne, Lie groups, symplektykę, Hodge'a, geometrię zespoloną, po sprawdzeniu pokrycia. Rozważyć dwa tomy, nie rozcinać automatycznie.
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
- **Plan / granice:** Zaproponować dwa tomy: grafy (00–17, 37–43 w obecnych ID) i węzły/niska topologia (18–34), z mostami Taita/Tutte/plumbing. Seiberg–Witten: GT zastosowania do 4-rozmaitości, RRC/DG podstawy analityczne i geometryczne. Uzupełnić po audycie grafów algorytmy/kolorowanie, matroidy i teorię węzłów (Alexander, Jones, sploty, niezmienniki). Zachować wszystkie stabilne dowody.
- **Audyt:** Istnieją liczne audyty globalne i rozdziałowe; status na aktualnych blobach ustalić przed rozdziałem tomów. [Dokument](../../audits/graph_and_knot_theory/global-structural-batch-control-2026-11-25.md).
- [Aktywny katalog rozdziałów](../../books/pl/graph_and_knot_theory.tex).

### LA — Algebra liniowa (32)

- **Rdzeń:** Przestrzenie wektorowe, formy, tensory, macierze, rozkłady, Grassmanniany, Clifford, spinory.
- **Plan / granice:** 01–21 rdzeń; 22–28 równania macierzowe i sterowanie jako osobna część, docelowo stosowana algebra/sterowanie przy rozroście; 29–32 geometria algebraiczno-liniowa, DG zastosowania. Nie przepisywać stabilnego materiału. Sprawdzić SVD, QR/LU, jednoczesną diagonalizację i twierdzenie Schura przed ewentualnymi uzupełnieniami.
- **Audyt:** Raport 23.11: 32 rozdziały, 382/382 dowodów, 320 stron i CI PASS; globalnie zamknięte na kontrolowanej wersji. [Dokument](../../audits/linear_algebra/global_audit/status.md).
- [Aktywny katalog rozdziałów](../../books/pl/linear_algebra.tex).

### LTM — Logika i teoria mnogości (23)

- **Rdzeń:** Klasyczny rachunek zdań i kwantyfikatorów, relacje, funkcje, ZF/ZFC, wybór, liczby kardynalne i porządkowe, wymuszanie.
- **Plan / granice:** Zachować zaawansowaną teorię mnogości tutaj; teorię modeli i metamatematykę już wydzielono. Logika infinitarna na styku z MOD/NL: w LTM tylko potrzebne zastosowania do kardynałów. Uzupełnić brakujące elementarne wyniki i sprawdzić archiwalne etykiety, integralność zamiast ponownego pełnego audytu bez przyczyny.
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

## 5. Nowe skrypty i ich program

**Zatwierdzony kierunek: RTPC — Rozszerzona teoria pochodnej i całki.**
- I. Uogólnione pochodne: Dini, pochodna aproksymatywna, różniczkowalność prawie wszędzie, związki z BV/AC i Rademacherem (ME).
- II. Całki skalarne: podziały cechowane, Cousin, Kurzweila–Henstocka, McShane'a, Denjoya (wąska i szeroka), Perrona, Riemanna–Stieltjesa, Kurzweila–Stieltjesa; charakterystyki funkcji pierwotnych, Hake, zbieżność i porównania.
- III. Wielowymiarowe: całki cechowane, Mawhina, Pfeffera, odpowiednie wersje twierdzeń całkowych i granice zakresu.
- IV. Wektorowe: Riemanna w przestrzeniach Banacha, całkowanie w przestrzeniach lokalnie wypukłych, Bochnera, Pettisa, Dunforda, Gelfanda i Birkhoffa; mierzalność, relacje klas, Fubini, różniczkowanie, kontrprzykłady. ME pozostaje właścicielem miar wektorowych i własności Radona–Nikodyma.
- V. Rachunek ułamkowy: Riemanna–Liouville'a, Caputo, Grünwalda–Letnikova, Riesz, warunki równoważności, kompozycje i przykłady; DT/PDE odsyłacze do operatorów i zastosowań.
- Dodać tabelę klas całkowalności, inkluzje wraz z hipotezami, kontrprzykłady i indeks metod. Nie tworzyć duplikatu wycofanej Teorii całki.

**FSG — Geometria różniczkowa przestrzeni Banacha:** istniejący kandydat, jeszcze niezarejestrowany w sprawdzonym katalogu. Gâteaux/Fréchet, Bastiani, wyższe pochodne, lokalne twierdzenia, podrozmaitości Banacha, wiązki, koneksje, metryki słabe/silne, przestrzenie odwzorowań, rozkłady jedności przy odpowiednich hipotezach, rachunek wariacyjny. AF zachowuje funkcjonalne podstawy; AM II elementarny pomost.

**AZ — Analiza zespolona:** liczby zespolone z AM I, gotowy materiał [funkcji elementarnych](complex_analysis_materials/README.md), holomorficzność, Cauchy, szeregi Laurenta i residua, funkcje meromorficzne, odwzorowania konforemne, rodziny normalne, funkcje harmoniczne/subharmoniczne, podstawy powierzchni Riemanna. Dalej osobny tom wielu zmiennych: dziedziny holomorficzności, pseudowypukłość, Levi, problem d-bar, jądra Bergmana/Szegő, funkcje wewnętrzne, Nevanlinna–Pick, geodezyjne zespolone i odległości niezmiennicze.

**TL — Teoria liczb i arytmetyka:** elementarna arytmetyka, kongruencje, kwadratowe prawo wzajemności, funkcje arytmetyczne, aproksymacja diofantyczna, algebraiczna teoria liczb, pierścienie liczb całkowitych, ideały, jednostki, klasy, analityczna teoria liczb, zeta i funkcje L. AA daje teorię ciał i Galois; nie kopiować jej.

**PA — Liczby p-adyczne i analiza niearchimedesowa:** ciała lokalne, wartościowania, lemat Hensela, rozszerzenia, analiza p-adyczna, miary, analiza harmoniczna, przestrzenie Banacha p-adyczne, podstawy geometrii niearchimedesowej. Zależności TL/AA/ME/AF.

**GAZ — Geometria analityczna zespolona:** lokalne zbiory i przestrzenie analityczne, snopy koherentne, twierdzenia Cartana A/B, przestrzenie Steina, osobliwości, analityfikacja, GAGA, porównanie z ALG. Po AZ i CAT.

**Propozycje do zatwierdzenia po podstawach:** ODE i układy dynamiczne (istnienie, jednoznaczność, stabilność, układy dynamiczne, bifurkacje; granica z RRC/FSG); teoria Liego i reprezentacji (wydzielenie AA51–72 dopiero gdy uzasadnione); analiza numeryczna i optymalizacja/sterowanie (kwadratury, metody macierzowe, ODE/PDE, optymalizacja); geometria symplektyczna i kontaktowa jako rozszerzenie DG; teoria informacji i uczenie statystyczne po RP4. Zbiór zadań do RP I–IV z podpowiedziami jako osobny skrypt. Nie tworzyć pustych wpisów katalogu dla propozycji.

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
| Algebra przemienna i Galois | AA | ALG, TL, MOD |
| Prawdopodobieństwo/procesy/całki stochastyczne/statystyka | RP1/RP2/RP3/RP4 | RRC, GT, RTPC |
| Operatory i widmo | AF | RRC, DT, FSG |
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
- [ ] Cross-check właścicieli tematów przed każdym nowym rozdziałem. Zmieniać plan po decyzji użytkownika, nie traktować propozycji P2/P3 jako nakazu implementacji.

## 9. Dokumenty lokalne i techniczne

Niniejszy plan ma pierwszeństwo przy sprzecznościach zakresu, plany lokalne pozostają szczegółowymi listami roboczymi. [AM I](plan_analizy_matematycznej_i.md), [AM II](plan_analizy_matematycznej_ii.md), [AA](plan_algebry_abstrakcyjnej_aa43_plus.md), [LA](plan_algebry_liniowej.md), [ALG](plan_geometrii_algebraicznej.md), [TO](plan_topologii_ogolnej.md), [DT](plan_uzupelnien_teorii_dystrybucji_fourier.md), [LTM/MOD](plan_rozdzielenia_logiki_i_teorii_modeli.md), [NL](plan_logiki_niestandardowej.md), [MM](plan_metamatematyki_i_teorii_obliczalnosci.md), [graf odsyłaczy](plan_globalnego_grafu_odsylaczy.md), [Atlas](../../application/docs/ATLAS_DEVELOPMENT_ROADMAP.md), [Lean](../../application/docs/LEAN_FORMALIZATION_PLAN.md).
