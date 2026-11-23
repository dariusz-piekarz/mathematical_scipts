# Miara i całka — rozdział 04, audyt VIII (iteracja globalna XXIV)

**Data:** 2026-11-23. **Gałąź istniejąca:** `biblioteka-matematyczna-iteracja-6`.  
**Jedyny audytowany rozdział:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.  
**Blob R04 przed i po iteracji:** `ce0105f63aa4da494cf5f2f5e9e2b26fc6389fd4` — tekst matematyczny R04 niezmieniony.

## 1. Odczyt najnowszego stanu, zakres i standardy

Na początku odczytano stan gałęzi względem commitu `c9f6a3d635ab0c3e96384db09da1d11fd6120d54`, najnowszy istniejący raport `23-rozdzial-04-audyt-VII-2026-11-23.md` (blob `d6f7faeb8a50ab268006567cdd705889755d2e62`), rozdział R04, jego workflow oraz skrypty testowe. Wśród nowszych commitów nie stwierdzono modyfikacji R04; raport audytu XXIV nie istniał. Ponownie pobrano `AGENTS.md` (blob `32de9b61a368cfdce4923c8f81f9f7014da533fc`) i `docs/pl/standardy_terminologiczne.md` (blob `bdbfc9923e1d7224b2c19a2ba8d459eaf72cdbdf`). Pobrano także `books/pl/integration_theory.tex` (blob `6ec24a3d62bae4baef945fca0ff1c433510de141`) wyłącznie jako kontekst składniowy i organizacyjny, bez edycji, deduplikacji i audytu osobnego skryptu.

Rozdziały R01–R03 służyły jedynie do rozwiązania odsyłaczy z R04; wcześniej zatwierdzone statusy stabilności R01–R03 pozostają bez zmian. Nie przeprowadzono audytu ani edycji R05–R31.

## 2. Niezależna kontrola merytoryczna R04

Ponownie przeanalizowano łańcuch dowodów konstrukcji miary Lebesgue'a, w szczególności:

- **Nierówność pokryciowa:** zwarty rdzeń $K_\delta$, skończone podpokrycie, siatka i przypisanie komórek otwartym prostopadłościanom. Rozdzielony wcześniej przypadek zdegenerowanego $K$ jest poprawnie obsłużony; przejścia do granic nie wymagają użycia nieistniejącej jeszcze miary.
- **Premiara i przedłużenie:** rozróżniono pierścień ograniczonych sum od algebry na ograniczonym $H$; skończona addytywność oraz oszacowanie przez przeliczalne pokrycie dają odpowiednio obie nierówności. Jednoznaczność wykorzystuje skończoną miarę na $H$.
- **Carathéodory i $\sigma$-skończoność:** rozcięcie pokrycia wzdłuż ścian $Q$ daje właściwy kierunek nierówności; wyczerpanie $[-n,n)^d$ pozwala zastosować twierdzenie o jednoznaczności na układzie $\pi$.
- **Niezmienniczość i regularność:** ujemny współczynnik skalowania wymaga powiększenia obrazów $(tb,ta]$ do półotwartych prostopadłościanów; argument z błędami sumowalnymi pozostaje poprawny. W regularności oddzielono miary skończone i nieskończone; dowód aproksymacji przez zbiory $G_\delta$ i $F_\sigma$ prawidłowo korzysta z podziału na części skończonej miary.
- **Przykłady i kontrprzykłady:** po wcześniejszej poprawce wykresu Lipschitzowskiego przypadek $a=b$ jest uzasadniony. Dla Cantora, zbioru Smitha–Volterry–Cantora i funkcji Cantora porównano liczby przedziałów, ich długości i sumy; dowód Vitaliego poprawnie korzysta z przeliczalnej addytywności i przedziału oszacowań $[1,3]$.

**W tym przeglądzie nie wykazano nowej usterki matematycznej wymagającej zmiany rozdziału.** Nie należy jednak wywodzić z tego pełnej stabilności technicznej i graficznej. Nie proponowano niezatwierdzonych rozszerzeń merytorycznych.

## 3. Wykazana słabość testu rysunku — poprawiona

Dotychczasowe testy regresyjne `tools/test_measure_theory_ch04_source.py` weryfikowały liczbę i długość przedziałów $C_1,C_2,C_3$, ale **nie weryfikowały rzeczywistego położenia każdego przedziału**; rysunek z przesuniętymi przedziałami mógł przejść test.

Dodano generowanie oczekiwanych przedziałów z dokładnych `fractions.Fraction` poprzez rekurencję usuwania środkowej trzeciej części, i porównanie **wszystkich 28 narysowanych współrzędnych końców** z konstrukcją matematyczną, z tolerancją $10^{-6}$ dla współrzędnych TikZ podanych do sześciu miejsc dziesiętnych.

**Wynik niezależnej lokalnej weryfikacji Python:** 28/28 współrzędnych zgodnych; największy błąd $1/3000000 \approx 3.3333\cdot10^{-7}$. To jest realne uruchomienie niezależnej kontroli arytmetycznej; nie deklaruje się uruchomienia pełnego skryptu repozytorium na runnerze GitHub.

**Zmiana:** commit `55fc25f3a2a829c83a2c4ac80c1b444deae43990`, nowy blob skryptu `94e47448962169d4dd9755078fc03c115827492c`. Pobrano skrypt po zapisie i potwierdzono jego pełną zawartość.

## 4. Wykazana luka kontroli PDF — poprawiona

W `.github/workflows/measure-theory-ch04.yml` poprzednio rasteryzowano tylko strony 1–15 izolowanego PDF poprzez `pdftoppm -f 1 -l 15`. Dla rozdziału dłuższego niż 15 stron końcowe strony nie pojawiałyby się w artefaktach, mimo pozornego powodzenia kroku.

Zastąpiono to rasteryzacją **wszystkich** stron, odczytem liczby stron przez `pdfinfo` i sprawdzeniem, że liczba plików `ch04_preview-*.png` jest równa liczbie stron. Kod nowego kroku przetestowano **lokalnie** na niezależnie wygenerowanym czterostronicowym PDF: `pdfinfo` zwrócił 4 strony, `pdftoppm` utworzył 4 pliki PNG, kontrola liczby plików zakończyła się PASS.

**Zmiana:** commit `ea59b90a9424113793bdacc15878cbd2ef373070`, nowy blob workflow `a5e8a66e45b46e9084ed78165f97affeaef10ed0`. Pobrano workflow po zapisie i sprawdzono pełną zgodność zawartości.

**Ważne ograniczenie:** czterostronicowy PDF był tylko syntetycznym sprawdzianem mechanizmu i **nie jest** PDF rozdziału 04. W tej iteracji nie pobrano, nie skompilowano i nie obejrzano wszystkich stron aktualnego R04.

## 5. Kontrola źródeł, etykiet i standardów po zmianach

Z aktualnych blobów R01–R04 zebrano wszystkie etykiety; w R04 jest **28 etykiet i 31 odsyłaczy**. Wszystkie odsyłacze z R04 mają cel w R01–R04; nie wykryto duplikatów etykiet ani nieprawidłowo sparowanych środowisk. Kod podpisu rysunku nadal zawiera \`\par\smallskip\`; zachowana jest wcześniejsza poprawka przypadku $a=b$. Nie wystąpiły zabronione oznaczenia \`\mathbf{1}\`, \`\mathbb{1}\`, \`\mathds{1}\` ani „zbieżność zdominowana”, „unia zbiorów”. Nie zmieniono żadnej etykiety ani pliku źródłowego innego rozdziału.

## 6. Stan CI i decyzja

Dla ostatniego commitu technicznego API sprawdzające statusy commitu zwróciło pustą listę, a dostępna funkcja odczytu workflow według commitu (obsługująca tylko przebiegi PR) także zwróciła listę pustą. To **nie dowodzi**, że workflow nie uruchomił się; jednak w tej sesji brak potwierdzonego wyniku obu zadań CI.

**R04 — NIESTABILNY / NIEZATWIERDZONY.** Audyt VIII nie znalazł nowych wykazanych błędów matematycznych. Wdrożono dwie mierzalne poprawy testowania geometrii i kompletności podglądów; ich logiczne działanie i zapis zweryfikowano, lecz wymagane pozostają prawdziwy zakończony CI, kompilacja izolowanego R04 i całej książki, inspekcja wszystkich stron autentycznego PDF (w tym paginacja rysunku Cantora) oraz kolejny czysty, niezależny audyt po ostatniej zmianie.

**Kolejna iteracja:** wyłącznie R04, audyt IX. Nie przechodzić do R05.
