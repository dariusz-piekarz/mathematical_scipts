# Audyt L — rozdział 15: Dualność, wypukłość i słaba zbieżność w przestrzeniach Lp (II)

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Status: W STABILIZACJI (nie STABILNY).**

## Wznowienie od rzeczywistego stanu GitHub

Przed audytem pobrano listę plików audits/measure_theory oraz bieżący plik źródłowy R15. Najnowszy ukończony raport był **49-rozdzial-15-audyt-I-2026-11-23.md**, a raport R14 XLVIII zatwierdzał stabilność R14. Wykryto, że od raportu XLIX wykonano rzeczywiste poprawki R15 i dodano odrębny workflow oraz testy; nie należy powtarzać audytu I ani rozpoczynać R16.

**Źródło R15 obecnie:** chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex, **blob d41de3e4f4e7faad473065b3f472e5f6fa95b352**. Wcześniejszy blob z raportu XLIX: 6cfb80433e293edfdbd713036493bdb78349c113. W międzyczasie commit **624d3d9202bf650e223ba80e0d36a4499f3a635a** wprowadził 9 miejscowych doprecyzowań: jawne przestrzenie z miarą w samodzielnych sformułowaniach, jawne q=p/(p−1), wyjaśnienie gęstości schodkowych funkcji dyadycznych w przykładzie Rademachera. Zachowano etykiety i inne rozdziały. Utworzono też **tools/test_measure_theory_ch15.py** i **.github/workflows/measure-theory-ch15.yml**.

## Druga kontrola matematyczna i językowa — tylko R15

Ponownie przeanalizowano wszystkie 12 dowodów i ich zależności: (1) izometryczne zanurzenie Lq w dualnej Lp i szczególną hipotezę sigma-skończoności dla p=1; (2) obie nierówności punktu środkowego, w tym osobliwość hesjanu dla 1<p<2; (3) jednostajną wypukłość; (4) istnienie minimum energii bez zakładania refleksywności; (5) wariacyjny dowód reprezentacji dualnej dla 1<p<∞ bez twierdzenia Radona–Nikodyma; (6) reprezentację dualnej L1 przez zmianę miary na skończoną i rzut Hilbertowski; (7) ostrość Höldera; (8) refleksywność; (9) kryterium słabej zbieżności; (10) dolną półciągłość normy; (11) diagonalny dowód słabej zbieżności podciągu z jawnym założeniem separowalności Lq; (12) istnienie i jednoznaczność minimizatora wypukłej energii.

Sprawdzono również **2 przykłady i 3 uwagi**, w szczególności próg całkowalności x^(−α), funkcje Rademachera i kontrprzykład dla dualnej L∞. Poprawki wprowadzające samodzielne hipotezy oraz uzasadnienie aproksymacji dyadycznej są matematycznie właściwe; nie wykryto nowej usterki wymagającej edycji źródła. Obowiązują zasady terminologiczne AGENTS.md i docs/pl/standardy_terminologiczne.md: zachowano \chi_A, nazwę „zbieżność zmajoryzowana”, poprawne polskie nazwy i istniejące etykiety. Nie dodano nowych twierdzeń ani przykładów.

**Wynik kontroli merytorycznej R15 II:** 12/12 dowodów, 2/2 przykłady, 3/3 uwagi bez nowej udowodnionej usterki; **0 edycji R15 w tym audycie**. Wynik nie zastępuje kontroli wizualnej PDF.

## Rzeczywiste CI po poprawkach

Zweryfikowano [GitHub Actions run 45195500890](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45195500890), commit **3c56f41fbbd2e116ae4732d74770e1cd2ba1d33e**, i odczytano **oba joby oraz ich logi**: **chapter-15-finite-and-source SUCCESS; chapter-15-pdf-and-references SUCCESS (2/2)**. Aktualny blob R15 odpowiada temu przebiegowi.

Autentyczne logi testów potwierdzają:
- **17 496** ważonych, zespolonych modeli atomowych nierówności punktu środkowego;
- **6 336** prób normowania funkcjonału i minimalizacji wypukłej energii;
- **6 750** testów dualności L1 na skończonych przestrzeniach atomowych;
- **1 012** kontroli znoszenia się funkcji Rademachera na przedziałach dyadycznych;
- **17 odsyłaczy** i **12 środowisk proof** w kontroli źródła.

Łącznie **31 594 / 31 594** testów matematycznych zakończyło się sukcesem. Testy skończenie wymiarowe są regresjami, nie dowodami ogólnych twierdzeń.

**Prawdziwa kompilacja CI:** izolowany PDF R15 ma **6 stron A4**, **3805 słów** w granicach stron według pdftotext -bbox i **6/6 wyrenderowanych podglądów**. Pełny skrypt ma **258 stron A4**; job zakończył się sukcesem po weryfikacji wymaganych etykiet, braku nierozwiązanych odsyłaczy i Overfull hbox. Artefakt **14827393155**, nazwa **measure-theory-ch15-audit-pdf**, jest dostępny i nieprzeterminowany. Link: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45195500890/artifacts/14827393155.

**Uczciwe ograniczenie:** w tej iteracji zweryfikowano kompilację, automatyczną kontrolę granic tekstu i utworzenie podglądów, ale **nie dokonano niezależnych oględzin graficznych wszystkich 6 stron**. Nie oznacza się tego kroku jako wykonanego. R15 nie zawiera rysunków TikZ.

## Decyzja i dalsza kolejność

**R15: W STABILIZACJI — nie zatwierdzono jeszcze formalnej stabilności.** Wykonano drugi pełny przegląd matematyczny bez nowej usterki, potwierdzono 2/2 zielone joby CI i rzeczywiste PDF, lecz brakuje niezależnej wizualnej kontroli stron. Nie wolno przechodzić do R16 przed jej wykonaniem i formalnym raportem stabilizacyjnym.

**R01–R14:** zachowują wcześniejsze statusy STABILNE; w tej iteracji nie były audytowane. **R16–R31:** nietknięte. Nie scalano books/pl/integration_theory.tex.

**Następna iteracja:** audyt **LI / R15 III** — niezależne oględziny wszystkich stron PDF, ponowna kontrola bloba i formalna decyzja o stabilizacji R15, bez otwierania R16.


---

## Uzupełnienie: niezależna kontrola wizualna autentycznego PDF

Po pierwotnym zapisie raportu wykonano brakującą **niezależną inspekcję graficzną**, o której była mowa w ograniczeniach technicznych powyżej. Pobrano ponownie **rzeczywisty artefakt CI 14827393155** dla commitu **3c56f41fbbd2e116ae4732d74770e1cd2ba1d33e**. Rozpakowano ZIP do /mnt/data/r15_audit50. Do kontroli wykorzystano autentyczny plik /mnt/data/r15_audit50/measure_theory_ch15_ci.pdf, zawierający **6 stron A4**.

Za pomocą renderera PDF utworzono **6/6 obrazów stron przy 140 dpi**, a następnie planszę zbiorczą /mnt/data/r15_audit50/contact.png. Obejrzano wszystkie strony: w szczególności stronę 2 z nierównościami punktu środkowego i rozbudowanym dowodem, strony 3–4 z reprezentacją dualną, stronę 5 z definicją słabej zbieżności i przykładem funkcji Rademachera oraz stronę 6 z domknięciem argumentu o słabo zbieżnym podciągu i minimalizacją energii. **Nie zauważono uciętych formuł, nachodzenia oznaczeń ani innych wad składu; R15 nie zawiera TikZ.**

**Niezależny od workflow odczyt PyMuPDF:** **2910 słów według własnej segmentacji, 0 słów poza prostokątami stron**, 6 stron. W CI Poppler wykrył **3805 słów**, również w obszarze stron; różnica liczników wynika z tokenizacji. Ponownie otwarto autentyczne logi: **izolowany R15 — 0 Overfull hbox i 0 Underfull hbox**; **pełna książka — 258 stron, 0 Overfull hbox, 0 niezdefiniowanych odsyłaczy, 14 wcześniejszych nieblokujących Underfull hbox**.

Po ostatnich poprawkach niezależny skan źródeł R01–R15 wykazał **17 etykiet R15, 17 odsyłaczy, 0 brakujących celów, 0 duplikatów w kontekście R01–R15, 0 niedomkniętych środowisk i 0 naruszeń terminologii**. Blob źródła R15 nadal wynosi **d41de3e4f4e7faad473065b3f472e5f6fa95b352**.

**Aktualizacja wcześniejszego ograniczenia:** niezależna inspekcja graficzna **została już wykonana — PASS**. Nie jest dalszą zaległością techniczną. Nie znaleziono nowej usterki wymagającej zmiany źródła. Dla zachowania rygoru stabilizacji po poprawkach podczas tej iteracji **R15 pozostaje W STABILIZACJI**, a audyt **LI / R15 III** służy ostatniej czystej, niezależnej kontroli matematycznej i formalnemu zatwierdzeniu. Nie rozpoczynano R16.
