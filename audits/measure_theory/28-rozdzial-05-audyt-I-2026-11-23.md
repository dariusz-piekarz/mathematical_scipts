# Miara i całka — rozdział 05, audyt I (iteracja globalna XXVIII)

**Data:** 2026-11-23. **Wyłączna gałąź:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/05-struktura-przestrzeni-mierzalnych.tex.  
**Stan wejściowy źródła:** blob 4fb3edb84f1e773faf435d26c1e59f7d831d0901.  
**Stan po poprawkach:** blob ad8382d2b331d26c16612430dcd4b7d8f132a2d2.

## 1. Rzeczywisty punkt wznowienia i izolacja zakresu

Na początku sprawdzono istniejącą gałąź względem commitu f4fbcc1395edf72edb6cb3e585c9ac95b22b1a8c. Potwierdzono raport stabilizacyjny poprzedniego rozdziału 04, audits/measure_theory/27-rozdzial-04-audyt-XI-stabilizacja-2026-11-23.md (blob 88b207d3e200cb1d9d8d72d9d39c8b33cadfc28a); nowsze commity go nie zmieniły. Nie istniał raport audytu 05. Na tej podstawie rozpoczęto **pierwszą iterację wyłącznie R05**. Nie audytowano i nie edytowano innych rozdziałów, nie scalano ani nie usuwano treści. Pliki R01–R04 służyły wyłącznie do rozwiązania odsyłaczy R05.

Sprawdzono aktualne AGENTS.md (blob 32de9b61a368cfdce4923c8f81f9f7014da533fc), docs/pl/standardy_terminologiczne.md (blob bdbfc9923e1d7224b2c19a2ba8d459eaf72cdbdf), books/pl/measure_theory.tex (blob c80ec1f02cc8548f64fe44d202d89d961496d92b) i jako kontekst organizacyjny books/pl/integration_theory.tex (blob 6ec24a3d62bae4baef945fca0ff1c433510de141). Ostatni plik jest osobną książką z własnymi rozdziałami o rodzajach całek; nie wykonywano wobec niego audytu merytorycznego ani zmian.

## 2. Zakres szczegółowego audytu matematycznego

R05 liczy obecnie **406 wierszy i 8 sekcji**, zawiera **3 definicje, 1 lemat, 7 twierdzeń, 2 wnioski, 10 środowisk dowodu, 5 przykładów i 2 uwagi**; nie zawiera rysunków.

Sprawdzono łańcuchy argumentacyjne i wymagane założenia:

1. **Ślad i generowanie:** rodzina D utworzona z warunku mierzalności przecięcia z A jest $\sigma$-algebrą na X; przez minimalność otrzymujemy oba zawierania. Podprzestrzeń topologiczna generuje dokładnie ślad borelowskiej $\sigma$-algebry; A nie musi być borelowskie w X.
2. **Testy mierzalności:** przeciwobrazy zachowują dopełnienia i przeliczalne sumy; prawe półproste z wymiernym początkiem generują $\mathcal B(\mathbb R)$; ograniczenie mierzalnego odwzorowania jest mierzalne względem śladu.
3. **Struktura początkowa:** $\sigma(f)$ jest $\sigma$-algebrą wszystkich przeciwobrazów mierzalnych, minimalną dla mierzalności f. Dla rodziny odwzorowań bierze się $\sigma$-algebrę generowaną wspólnie przez przeciwobrazy.
4. **Produkt i współrzędne:** prostokąty są przecięciami przeciwobrazów zbiorów przez rzutowania; kryterium mierzalności odwzorowania do produktu jest równoważne mierzalności obu współrzędnych. Dla dwóch topologii z przeliczalnymi bazami produkt baz jest przeliczalny, więc borelowska $\sigma$-algebra produktu zgadza się z produktem borelowskich $\sigma$-algebr. Dla wektora o d współrzędnych użyto skończonej indukcji.
5. **Kontrprzykład dla przestrzeni bez przeliczalnych baz:** dla dyskretnego D o mocy większej niż continuum zamknięta przekątna nie należy do produktowej $\sigma$-algebry. Każdy zbiór ze $\sigma$-algebry generowanej przez dowolną rodzinę zależy tylko od przeliczalnie wielu generatorów; rozróżnianie $(x,x)$ i $(x,y)$ prowadzi do iniekcji D w $\{0,1\}^{\mathbb N}$ i sprzeczności z mocą D. Użyto wyłącznie $\chi_A$.
6. **Przestrzenie standardowe borelowskie:** pełna definicja z mierzalną bijekcją i mierzalną odwrotnością; przeliczalna baza przestrzeni polskiej daje przeliczalną rodzinę generującą i rozdzielającą punkty. $\mathcal L_1$ nie jest przeliczalnie generowana, ponieważ zawiera wszystkie podzbiory zbioru Cantora.
7. **Miary obrazowe:** zgodność składania z przeciwobrazami prowadzi do funktorialności. Dla odwzorowania stałego obrazy mierzalnych zbiorów przyjmują właściwe wartości, z osobnym uwzględnieniem masy nieskończonej i niezdefiniowanego wyrażenia $\infty\cdot0$.

Nie stwierdzono fałszywego sformułowania twierdzenia ani błędnej implikacji wymagającej zmiany zakresu rozdziału. Wykryto jednak niżej opisane usterki językowo-formalne i niejawne hipotezy przykładów.

## 3. Cztery rzeczywiste poprawki źródła

Wprowadzono w pojedynczym commicie **79a834ace94b62cd1294004f3ed269eaf0f811b3**:

1. Tytuł twierdzenia z niedozwolonym sformułowaniem „przestrzeni drugoprzeliczalnych” zastąpiono przez **„przestrzeni spełniających drugi aksjomat przeliczalności”**.
2. Definicję przestrzeni polskiej przeredagowano tak, by jawnie odnieść **przeliczalny zbiór gęsty do zupełnej metryki wyznaczającej topologię**, zamiast nieprecyzyjnego połączenia „metryka zupełna i ośrodek przeliczalny”.
3. W przykładzie $X=\{a,b,c,d\}$ i $\sigma(f)$ jawnie określono mierzalny przeciwdziedzinowy układ $(\mathbb R,\mathcal B(\mathbb R))$.
4. W przykładzie miary obrazowej funkcji stałej dopisano **obie przestrzenie mierzalne, punkt $y_0$, miarę na źródle, funkcję oraz kwantyfikację $B\in\mathcal G$**. Utrzymano oddzielny przypadek $\mu(X)=\infty$.

Nie zmieniono stabilnych etykiet, twierdzeń, zakresu materiału ani innych rozdziałów. Po zapisie ponownie pobrano cały plik R05, potwierdzając nowy blob ad8382d2b331d26c16612430dcd4b7d8f132a2d2.

## 4. Nowe testy i ich rzeczywiste wykonanie

Utworzono tools/test_measure_theory_ch05.py (commit **baf31405a8dbe3f801faef7dbccaf5bfd4e4920e**) i poprawiono przed uruchomieniem CI licznik przypadków złożenia miar obrazowych oraz test funkcji stałej (commit **15347ba24d8b6043692d4584a4281e663458c655**). Ostateczny blob pliku: d948e238760f90e649b1e61cd4047c9c569416bd.

Dodano osobny workflow .github/workflows/measure-theory-ch05.yml (commit **0998b705520c0144fb72fea6165abad34809fea4**, blob a18a81c5c409a53422134e036be68c3778b1fea3). Nie modyfikowano testów innych rozdziałów.

**Autentyczny wynik GitHub Actions:** [run 45145807540](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145807540), oba joby 2/2 **SUCCESS**, w logu testów dokładnie:
- 2048 wyczerpujących modeli skończonych tożsamości śladu i generowania;
- 6912 modeli minimalności $\sigma(f)$;
- 10 par skończonych $\sigma$-algebr w teście konstrukcji produktu przez rzutowania;
- 576 przypadków składania miar obrazowych;
- 15 odsyłaczy R05 rozwiązanych względem R01–R05, brak podwójnych etykiet i błędów parowania środowisk; brak zakazanej terminologii.

**Granica testów:** skończone modele są regresją i nie zastępują dowodów twierdzeń ogólnych, zwłaszcza o przekątnej przestrzeni dyskretnej nieprzeliczalnej.

## 5. Rzeczywista kompilacja i inspekcja PDF

Drugi job tego samego runu zakończył się sukcesem:
- izolowany R05 wygenerowany z oryginalnej preambuły books/pl/measure_theory.tex, **2 rzeczywiste przebiegi pdflatex**;
- **5 stron A4, 2313 słów** zweryfikowanych jako mieszczące się w ramach wszystkich stron, wygenerowane **5/5 podglądów**;
- **3 rzeczywiste przebiegi pdflatex całej książki**, 256 stron; nie wykryto niezdefiniowanych odsyłaczy, powielonych etykiet lub przepełnień blokujących workflow;
- z GitHub pobrano autentyczny artefakt runu **14803168957** (PDF, 5 podglądów, logi, tekst i bbox), rozpakowano go i wyrenderowano wszystkie pięć stron do PNG w rozdzielczości 140 dpi.

Obejrzano komplet pięciu stron zestawiony w podglądzie. Sekcje, twierdzenia, dowody, przykłady i wnioski układają się poprawnie; tytuły zawijają się do następnego wiersza tam, gdzie to konieczne, brak widocznych nachodzących napisów, uciętych symboli czy kolizji. W izolowanym R05 liczba komunikatów Overfull hbox i Underfull hbox wynosi 0. Dwanaście ostrzeżeń LaTeX w izolowanym składzie dotyczy międzyrozdziałowych odsyłaczy nieobecnych w dokumencie zawierającym wyłącznie R05; przy pełnej kompilacji książki są rozwiązane.

## 6. Werdykt: stabilizacja w toku

**R05 — NIESTABILNY / NIEZATWIERDZONY.** Pierwszy audyt R05 wykrył i poprawił cztery nieścisłości językowo-formalne i brak jawnych hipotez. Techniczne testy i pełne CI dla poprawionej wersji zakończyły się sukcesem, a cały autentyczny PDF R05 został sprawdzony wizualnie. Jednak bezwzględna reguła projektu wymaga **co najmniej jednego nowego, pełnego, niezależnego czystego audytu rozdziału 05 po ostatniej poprawce**, również matematycznego i językowego, zanim uzna się go za stabilny.

**R04 pozostaje STABILNY.** W tej iteracji nie otwierano jego audytu ponownie.

**Następny krok:** audyt XXIX / R05 II, wyłącznie rozdział 05, niezależnie przejrzeć ponownie wszystkie 10 dowodów, hipotezy, kontrprzykłady, zgodność ze standardami i gotowy PDF, potwierdzić CI aktualnego SHA, a jeśli znajdą się błędy, poprawić i ponawiać audyt. Nie przechodzić do R06 przed jawnym zatwierdzeniem stabilności R05.
