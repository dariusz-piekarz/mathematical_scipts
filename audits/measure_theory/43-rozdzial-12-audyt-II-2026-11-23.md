# Miara i całka — audyt XLIII: rozdział 12, audyt II (2026-11-23)

**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Rozdział:** chapters/pl/measure_theory/12-miary-produktowe-twierdzenia-tonellego-i-fubiniego.tex.  
**Status: W STABILIZACJI — NIEZATWIERDZONY.** Nie przechodzić do R13.  
**Blob na początku:** 5534eed7aed056956f8d7d21a373393c26a3ba40.  
**Blob po poprawkach:** 999411d62c4b1d5e06c2fbd6e6122bf9b457b7d0.

## 1. Rzeczywisty punkt wznowienia

Po potwierdzeniu stabilności R11 zauważono, że równoległa automatyzacja zdążyła wykonać audyt XLII/R12 I: audits/measure_theory/42-rozdzial-12-audyt-I-2026-11-23.md (blob 1b151c13d5c9412db7af0cf7dd7e97a68a8822b7). Poprawiono tam samodzielność wniosku cor:practical-fubini-12 (commit 4020efbcacc6b0cb4b491e44f46d0f8bac833ad7), ale nie uruchomiono CI ani nie obejrzano PDF, więc R12 miał status W STABILIZACJI. Nie powielano tamtego audytu: bieżąca iteracja jest **drugą niezależną kontrolą R12**, obejmującą matematyczne dowody, nowe poprawki i rzeczywiste CI/PDF.

Przeczytano cały R12, AGENTS.md, docs/pl/standardy_terminologiczne.md oraz books/pl/measure_theory.tex. Rozdziały R01–R11 odczytano tylko do kontroli wcześniejszych wyników i celów odsyłaczy. Nie zmieniano tych rozdziałów ani R13–R31; nie tworzono nowej gałęzi.

## 2. Szczegółowy audyt 12 dowodów

R12 po poprawkach liczy **865 wierszy, 12 sekcji, 6 twierdzeń, 4 wnioski, 2 lematy, 12 środowisk dowodu, 7 przykładów i 3 uwagi**; nie ma rysunków TikZ. Sprawdzono:

1. Mierzalność pionowych i poziomych przekrojów: rodziny zbiorów o mierzalnym przekroju są sigma-algebrami zawierającymi prostokąty, a dla funkcji wykorzystuje się przeciwobrazy zbiorów borelowskich.
2. Tożsamość przekrojowa na prostokącie skończonej miary: algebra skończonych rozłącznych sum prostokątów, ciągi rosnące przez Beppo Leviego i malejące przez ciągłość z góry wraz z integrabilną dominantą. Uniknięto cyklicznego stosowania jeszcze nieudowodnionego Fubiniego.
3. Przejście do miar sigma-skończonych: wyczerpania przez prostokąty skończonej miary, E_n rosnące do E i dwukrotne użycie zbieżności monotonicznej.
4. Konstrukcja i jednoznaczność miary produktu: przeliczalna addytywność przez przekroje, konwencja 0·∞=0, a następnie twierdzenie pi–lambda na wyczerpaniu.
5. Tonelli: funkcje charakterystyczne, proste i dowolne nieujemne przez ciąg aproksymacji z dołu; mierzalność funkcji przekrojowo całkowanych również przy +∞.
6. Wniosek o całkowalności funkcji nieujemnej: równoważność skończoności trzech równych całek.
7. Fubini: Tonelli dla |f|, mierzalne zerowe zbiory wyjątków, części dodatnie/ujemne i rzeczywiste/urojone, ograniczenie przez całkę modułu i odejmowanie tylko skończonych wartości.
8. Praktyczne kryterium Fubiniego: iterowana całka |f| jest równa całce produktu |f|, co daje dokładnie hipotezę Fubiniego.
9. Produkt miar Lebesgue'a: borelowskie przybliżenia, zgodność miar na prostopadłościanach, jednoznaczność i uzupełnienie sigma-algebry produktu do pełnej miary Lebesgue'a.
10. Tonelli i Fubini dla uzupełnionego produktu: przedstawiciel produktowo mierzalny poza jednym zbiorem zerowym; przekroje tego zbioru są zerowe niemal wszędzie i dzięki zupełności miar czynników dopuszczają mierzalne przekroje pierwotnej funkcji.
11. Przekroje zbioru zerowego: całka nieujemnej funkcji jest zerem wtedy i tylko wtedy, gdy funkcja znika prawie wszędzie; sprawdzono przykład z dodatnią miarą pojedynczego wyjątkowego przekroju.
12. Łączność produktów: równość dwóch miar na układzie generujących prostokątów w produkcie trzech miar sigma-skończonych i dalsze zastosowanie Tonellego/Fubiniego.

W 7 przykładach sprawdzono: pole trójkąta (1/2), całkę z 1/(x+y) (2 log 2), funkcję e^{-x-y}(x−y) o całce 0, różne kolejności sumowania macierzy niebezwzględnie całkowalnej, przekątną liczenie × Lebesgue przy braku sigma-skończoności, niemierzalny w produkcie podzbiór przekątnej oraz niezależne elementy losowe na arbitralnych przestrzeniach mierzalnych. Kontrolowano również wszystkie 3 uwagi i przypadki zerowych i nieskończonych miar.

**Wynik:** nie znaleziono nowego fałszywego twierdzenia, ale wykazano niekompletne hipotezy kilku wyników, brak jawnej konwencji 0·∞ przy mnożeniu funkcji nieujemnych oraz niepoprawną terminologię w przykładzie o niezależności. Zostały poprawione. Ponieważ w tej iteracji zmieniono źródło, nie jest to czysty audyt stabilizacyjny.

## 3. Rzeczywiste poprawki i commity

- **[6140eb920807876f4813bebb80752330a90b89a8](https://github.com/dariusz-piekarz/mathematical_scipts/commit/6140eb920807876f4813bebb80752330a90b89a8):** jawnie podano (X,F,μ) i (Y,G,ν) w obu lematach o przekrojach, twierdzeniu przekrojowym, Tonellim, Fubinim oraz wnioskach o nieujemnej całkowalności i przekrojach zbioru zerowego. Zmieniono nazwę „zmienne losowe” na „elementy losowe” dla ogólnych przestrzeni mierzalnych.
- **[c9472e6920cfa8b3a82c73686d9e1988609c61bc](https://github.com/dariusz-piekarz/mathematical_scipts/commit/c9472e6920cfa8b3a82c73686d9e1988609c61bc):** określono konwencję 0·∞=∞·0=0 w iloczynie nieujemnych funkcji o wartościach rozszerzonych; poprawiono „całka podpisana” na „całka funkcji ze znakiem”.
- **[1eb9016751c86c78a441af7cefa917ba9fbd228a](https://github.com/dariusz-piekarz/mathematical_scipts/commit/1eb9016751c86c78a441af7cefa917ba9fbd228a):** usunięto rzeczywiste przekroczenie szerokości wiersza o 14.38326 punktu, przenosząc hipotezę o skończonej całce iterowanej do osobnego wzoru we wniosku o praktycznym Fubinim.

Ostateczny blob źródła: **999411d62c4b1d5e06c2fbd6e6122bf9b457b7d0**. Wszystkie historyczne etykiety zachowano.

## 4. Nowe testy i ich wyniki

Dodano tools/test_measure_theory_ch12.py (commit **48a4a9817ac3fcdb0f8ab7ebdb9ec2406983d564**, blob e3b8874879f35f067bb5ae4c28ce0c4ce34e2d40) i .github/workflows/measure-theory-ch12.yml (commit **b4bae709e169b80145c86ec97ffbcec67fcfef0b**, blob 04591bde1353b989143e4cec44a5d992565d5271).

Potwierdzone rzeczywiste wyniki na ostatniej wersji:
- **20736/20736 PASS** — Tonelli na wszystkich badanych produktach dwóch dwupunktowych przestrzeni, z wartościami 0,1,3,+∞ i wagami 0,2,+∞;
- **50625/50625 PASS** — Fubini dla funkcji ze znakiem i skończonych mas atomowych;
- **60/60 PASS** — dokładne skończone obcięcia kontrprzykładu bez bezwzględnej całkowalności;
- **225/225 PASS** — pola prostokątów z wymiernymi końcami;
- **PASS** — zerowa miara produktu z wyjątkowym przekrojem dodatniej miary;
- **PASS** — 21 odsyłaczy R12, środowiska LaTeX i terminologia.

Skończone modele stanowią dodatkową kontrolę, **nie są dowodami ogólnych twierdzeń o miarze produktowej**.

## 5. Pełna weryfikacja CI i autentycznego PDF

Pierwszy [run 45170503751](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45170503751) i drugi [run 45170607845](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45170607845) wykazały poprawne testy, ale **niepowodzenie zadania PDF** z powodu Overfull hbox we wniosku o praktycznym Fubinim. Został on naprawiony. **Końcowy [run 45170775564](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45170775564)** na commicie 1eb9016751c86c78a441af7cefa917ba9fbd228a zakończył się **2/2 completed SUCCESS**. Nie przypisywano nieudanym przebiegom statusu sukcesu.

Przebieg końcowy wykonał dwie kompilacje izolowanego R12 oraz trzy całej książki. PDF rozdziału: **9 stron A4, 4921 słów Popplera w granicach stron, 9/9 podglądów PNG**. Pełna książka: **257 stron, bez nieznanych odsyłaczy i Overfull hbox**.

Pobrano autentyczny artefakt **14817470355** do /mnt/data/measure_theory_ch12_run45170775564.zip, rozpakowano do /mnt/data/r12_audit43 i wyrenderowano wszystkie dziewięć stron w 140 dpi. Obejrzano planszę kontaktową oraz osobno stronę piątą, zawierającą poprawiony wniosek i wzór. Nie ma przyciętych wzorów, nachodzących na siebie napisów lub czarnych kwadratów. Nie występują rysunki TikZ.

Niezależna kontrola PyMuPDF: **4150 słów (inna tokenizacja niż Poppler), 0 poza granicami stron**. Log izolowanego R12: **0 Overfull hbox, 0 Underfull hbox**; pełna książka: 0 Overfull i 0 nierozwiązanych odsyłaczy, **14 wcześniejszych nieblokujących Underfull hbox**. W izolowanym PDF odsyłacze do rozdziałów spoza R12 mogą pokazywać „??”; pełna książka rozwiązuje je prawidłowo.

## 6. Etykiety, terminologia i formalny status

Ostateczny odczyt GitHub API: **865 wierszy, 23 etykiety, 21 odsyłaczy z R12 do istniejących celów R01–R12, 0 duplikatów etykiet, 0 niesparowanych środowisk i 0 zakazanych zamienników notacji \chi_A**. Zachowano wszystkie historyczne etykiety.

**R12 — W STABILIZACJI, NIEZATWIERDZONY.** W audycie XLIII konieczne było ponowne edytowanie źródła, dlatego, mimo zielonych testów, rzeczywistego CI 2/2 i prawidłowego dziewięciostronicowego PDF, **nie wolno zatwierdzić stabilności w tej samej iteracji**. Potrzebny jest kolejny, pełny, niezależny i czysty audyt tego samego bloba, a w razie nowych usterek kolejne poprawki i ponowne kontrole.

**R01–R11 — STABILNE**, bez zmian w tej iteracji. **R13–R31 — nietknięte**.

**Następna osobna iteracja:** audyt globalny **XLIV / R12 III**. Nie zaczynać audytu R13 przed formalną stabilizacją R12.
