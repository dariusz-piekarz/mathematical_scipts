# Teoria miary / Miara i całka — rozdział 04, audyt IX (iteracja XXV)

**Data:** 2026-11-23. **Wyłączna gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Audytowany wyłącznie:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.  
**Blob źródła R04:** `ce0105f63aa4da494cf5f2f5e9e2b26fc6389fd4`; źródło **nie zostało zmienione**.

## 1. Rzeczywisty punkt wznowienia i zgodność standardów

Przed rozpoczęciem odczytano aktualny stan gałęzi względem commitu ostatniego raportu `5ba55672f13017ece7c2cefece26daebc570265e`. Najnowszym istniejącym raportem był audyt XXIV, `audits/measure_theory/24-rozdzial-04-audyt-VIII-2026-11-23.md` (blob `bbea792db4fee4d77b1e5a83cd9529ce887d8d97`). Nie było raportu XXV ani późniejszej modyfikacji źródła R04; nowsze commity dotyczyły innych skryptów.

Ponownie odczytano: `AGENTS.md` (blob `32de9b61a368cfdce4923c8f81f9f7014da533fc`), `docs/pl/standardy_terminologiczne.md` (blob `bdbfc9923e1d7224b2c19a2ba8d459eaf72cdbdf`), preambułę `books/pl/measure_theory.tex` oraz `books/pl/integration_theory.tex` wyłącznie dla kontekstu organizacyjnego. Rozdziały 01–03 odczytano wyłącznie do weryfikacji celów odsyłaczy R04. Żadnego innego rozdziału nie audytowano ani nie edytowano.

## 2. Niezależna weryfikacja źródła i kluczowych argumentów

Ponownie odczytano całe źródło R04 (982 wiersze), skupiając się na czterech krytycznych ścieżkach dowodowych:
- geometryczna nierówność objętości przy przeliczalnym pokryciu: przejście od zwartego rdzenia do skończonej siatki, oddzielenie prostopadłościanów zdegenerowanych oraz kolejność granic;
- konstrukcja miary Lebesgue'a: zgodność z premiarą na ograniczonym prostopadłościanie, mierzalność Carathéodory'ego i jednoznaczność przy $\sigma$-skończoności;
- regularność i uzupełnienie: aproksymacja otwarta, zwarta i borelowska, osobno dla miary skończonej i nieskończonej;
- konstrukcje Cantora i Vitaliego: brak punktów izolowanych, długości przedziałów, funkcja Cantora i sprzeczność dla rozłącznych przesunięć reprezentantów.

**Nowej wykazanej niepoprawności matematycznej nie stwierdzono.** Po ostatniej poprawce wykresu Lipschitzowskiego przypadek $a=b$ pozostaje uwzględniony. Weryfikacja źródła dała **28 etykiet, 31 odsyłaczy, 0 nierozwiązanych celów, 0 powielonych etykiet w R01–R04, 0 niesparowanych środowisk**. Brak niedozwolonych notacji `\mathbf{1}`, `\mathbb{1}`, `\mathds{1}` i niezgodnej terminologii „zbieżność zdominowana”, „unia zbiorów”. Zachowano `\chi_A` jako jedyną konwencję funkcji charakterystycznej.

## 3. Wykryta luka w technicznej kontroli składu PDF

Poprzednia wersja workflow `.github/workflows/measure-theory-ch04.yml` sprawdzała, czy **słowa mieszczą się na stronach**, i generowała PNG wszystkich stron. **Nie potrafiła jednak automatycznie odróżnić poprawnego podpisu rysunku Cantora od podpisu nałożonego pionowo na etykiety osi**, czyli od typu usterki faktycznie wykrytej w audycie XX.

Stworzono `tools/test_measure_theory_ch04_pdf_layout.py`, który czyta wygenerowany przez `pdftotext -bbox` plik XHTML, weryfikuje ramki każdego słowa na każdej stronie, identyfikuje jedyny podpis „Pierwsze cztery etapy konstrukcji”, wyszukuje dwie etykiety osi „0” i „1” na tej samej stronie i wymaga co najmniej 5 punktów odstępu pionowego między etykietami a początkiem podpisu.

**Zweryfikowana rzeczywista próba dodatnia:** na lokalnym, wcześniej rzeczywiście skompilowanym i wyrenderowanym PDF autentycznego rysunku z R04 oraz jego podpisu (A4; `pdflatex`, `pdftotext -bbox`) uzyskano `PASS 1 pages, 29 bounded words; Cantor caption separated on page 1`. Pomiar wynosił: etykiety osi maksymalnie do 165,473 pt od górnej krawędzi, początek podpisu od 179,999 pt, czyli **14,526 pt odstępu**.

**Zweryfikowana próba ujemna (mutacja testowa):** zmieniono lokalnie współrzędne pierwszego wyrazu podpisu w XHTML, symulując jego przesunięcie w obręb etykiet osi. Skrypt poprawnie zgłosił błąd i zakończył się kodem niezerowym. Oryginalnego PDF ani źródła R04 nie zmieniano.

Test jest przeznaczony dla autentycznego PDF R04 generowanego w CI, ale **nie jest** odpowiednikiem oględzin wszystkich stron i graficznych obszarów wypełnianych przez TikZ.

## 4. Zmiany zapisane na istniejącej gałęzi

1. Nowy test `tools/test_measure_theory_ch04_pdf_layout.py`, commit **`40e5368de51322709d916ee8b18397382ff085f2`**, blob po zapisie **`83d1ce6dbcb8d605de0ed0c3f3b69699e050958b`**.
2. Aktualizacja workflow `.github/workflows/measure-theory-ch04.yml`: nowy test dodano do filtrów uruchomienia oraz do kroku po `pdftotext -bbox`; bez usuwania kontroli matematycznych, pełnej książki i rasteryzacji wszystkich stron. Commit **`f70575a208603517fe91ac1f2420d613ff208f37`**, blob **`858a3cb214a85048d20789a6867f4f4e9221289a`**.

**Oba pliki ponownie pobrano przez API GitHub po aktualizacji; treść i SHA potwierdzone.**

## 5. Faktycznie sprawdzone testy i nadal nierozstrzygnięta kompilacja

W tej iteracji rzeczywiście uruchomiono lokalnie istniejące kontrole arytmetyczne: **262 144** par zbiorów siatki, **11** etapów Cantora, **10** etapów Smitha–Volterry–Cantora, **14** etapów kontroli przyrostów funkcji Cantora i **9** dokładnych oszacowań wykresu Lipschitzowskiego — wszystkie **PASS**. Zweryfikowano dodatnią i ujemną próbę nowego testu położenia podpisu na rzeczywistych danych `pdftotext -bbox`.

Nie uruchomiono w tej iteracji kompilacji **pełnego** R04 lub całej książki: w lokalnym środowisku jest `pdflatex`, lecz nie ma zmaterializowanego pełnego źródła GitHub; próba bezpośredniego pobrania przez HTTPS nie powiodła się z powodu braku rozwiązywania nazw DNS. Endpoint GitHub służący do pobierania przebiegów workflow na podstawie commitu obejmuje tylko PR i nie zapewnia listy przebiegów push. **Nie deklaruje się sukcesu CI ani wizualnego audytu pełnego PDF.**

## 6. Status stabilności i kolejny krok

**R04: NIESTABILNY / NIEZATWIERDZONY.** Audyt IX nie stwierdził nowych błędów w badanych argumentach matematycznych. Zamknął konkretną lukę w teście układu PDF, a nowy test wykazał zarówno poprawną akceptację, jak i skuteczne odrzucenie mutacji. Rozdział wymaga nadal potwierdzenia **obu rzeczywistych jobów CI** na obecnym commicie, pobrania kompletnego PDF R04, przeglądu wszystkich jego stron i jeszcze jednego czystego, niezależnego audytu po zakończeniu kontroli technicznej.

**Następna iteracja: wyłącznie R04, audyt X. Nie przechodzić do R05.**
