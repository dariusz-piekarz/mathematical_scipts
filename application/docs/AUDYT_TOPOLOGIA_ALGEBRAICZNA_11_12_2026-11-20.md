# Topologia algebraiczna — szczegółowy audyt AT-11 i AT-12

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Zakres:** dwa kanoniczne rozdziały `chapters/pl/algebraic_topology/11-przeciecia-dualnosc-i-klasy-charakterystyczne.tex` i `12-ciagi-spektralne-od-filtracji-do-fibracji-serre-a.tex`.  
**Metoda:** standard szczegółowości pierwszego rozdziału geometrii różniczkowej; rzeczywista kontrola założeń i rozumowań, przykładów, kontrprzykładów, języka, rysunków i odsyłaczy; poprawki bezpośrednio w źródłach.

## AT-11 — przecięcia, dualność, klasy charakterystyczne

Przegląd obejmuje iloczyn kubkowy i kapowy, klasę fundamentalną, dualność Poincarégo i Poincarégo–Lefschetza, lokalne współczynniki, dualność Aleksandra, klasyfikację wiązek przez funkcje sklejające, klasy Stiefela–Whitneya i Eulera, klasę Thoma, indeksy zer pól i twierdzenie Poincarégo–Hopfa oraz formy przecięcia i ich zastosowanie do chirurgii.

1. **Rachunkowa klasyfikacja parzystości form przecięcia:** dodano `prz:formy-przeciecia-cp2-s2`. Z filtracji komórkowej `CP⁰⊂CP¹⊂CP²` otrzymano `H₂(CP²;Z)=Z`; dwie różne zespolone linie rzutowe przecinają się transwersalnie w jednym punkcie o znaku `+1`, więc `Q_CP²=(1)`.
2. **Mocny przykład nierozróżnialności przez zwykłą homologię:** skonstruowano spójną sumę `N=CP²#(-CP²)` i przez dokładny ciąg Mayera–Vietorisa wykazano `H₀(N)=H₄(N)=Z`, `H₂(N)=Z²` i zanik pozostałych dodatnich grup — dokładnie tak samo jak dla `S²×S²`. Mimo to `Q_N=diag(1,-1)` jest nieparzysta, podczas gdy `Q_(S²×S²)=((0,1),(1,0))` jest parzysta: `Q(aA+bB,aA+bB)=2ab`. Własność zachowują całkowite zmiany bazy oraz odwrócenie orientacji. Stąd przestrzenie nie są homotopijnie równoważne.
3. **Nowy rysunek `fig:formy-przeciecia-parzystosc`:** obie macierze oraz wartości kwadratowe przedstawione na jednym diagramie z opisem różnicy parzystości.
4. **Terminologia i dowód:** usunięto niedopuszczony wyraz na określenie operacji iloczynu tensorowego z argumentu o homotopii łańcuchowej. Poprawiono „injektywna” na „iniektywna” przy restrykcji klasy `w₂` do `2`-szkieletu; nie zmieniono żadnej starej `\label` ani konstrukcji dowodowych.

## AT-12 — ciągi spektralne i fibracja Serre'a

Przejrzano definicje filtracji, stron `E⁰,E¹,E^r`, cykli i brzegów rzędu `r`, stopnie różniczek, dowody stabilizacji i problemu rozszerzeń, konstrukcję przez dokładną parę, identyfikację strony drugiej Serre'a, fibrację przestrzeni dróg, lokalny rachunek nad komórką, wersję kohomologiczną i transgresję, fibrację Hopfa, butelkę Kleina, klasę Thoma i ciąg Gysina oraz zastosowanie do przestrzeni pętli.

1. **Dlaczego różniczka może pojawić się dopiero na stronie `3`:** nowy `prz:spectral-d3-cancel` z kompleksem `C₃=Zx`, `C₂=Zy`, `∂x=y` i filtracją `F₀=Zy`, `F₁=F₂=F₀`, `F₃=C`. Jawnie wykazano brak możliwych niezerowych różniczek `d¹,d²`, izomorfizm `d³:E³_(3,0)→E³_(0,2)` i zerową stronę `E⁴`. Wyjaśniono ogólny odpowiednik z pierwszą różniczką `d^r`.
2. **Problem rozszerzeń faktycznie obliczony, a nie tylko wspomniany:** nowy `prz:spectral-extension-z4` zestawia `C₁=Z/4Z`, `F₀=2Z/4Z`, z `C'₁=(Z/2Z)²`, `F'₀=Z/2Z⊕0`. Wszystkie różniczki w obu kompleksach są zerowe, a jedyne wyrazy każdej strony `E^r` to `E^r_(0,1)=E^r_(1,0)=Z/2Z`. Mimo identycznych wszystkich stron końcowe grupy homologii to odpowiednio `Z/4Z` i `(Z/2Z)²`. Różnica wynika z nierozszczepionego albo rozszczepionego krótkiego ciągu dokładnego.
3. **Nowy diagram `fig:spectral-extension-z4`:** przedstawia identyczną stronę stabilną i dwie odmienne grupy docelowe.
4. **Precyzyjne rozgraniczenie udowodnionych twierdzeń:** poprzednia uwaga deklarowała ogólną wersję dla fibracji Serre'a jako nieudowodnioną, podczas gdy wcześniejsze Lematy `lem:serre-mappingpath-v6`, `lem:serre-cell-hurewicz-v6` i Twierdzenie `thm:serre-general-v6` dają jej dowód dla włókien typu CW przy skończeniewymiarowej bazie CW. Uaktualniono uwagi i przykład fibracji przestrzeni pętli, rozdzielając ten wynik od nadal otwartych w skrypcie kwestii nieograniczonych filtracji, pełnej multiplikatywności i transgresji.
5. **Terminologia:** „ciąg” zamiast „sekwencja”, „przeciwobrazy” zamiast „preobrazy” oraz „iniekcja” zamiast „injekcja”, z zachowaniem matematycznego sensu formuł.

## Integralność i kontrola źródeł

- W AT-01–12 brak duplikatów deklaracji etykiet. W AT-11 i AT-12 są łącznie **52** standardowe odsyłacze `\ref/\eqref`, wszystkie mają cele w tym dwunastorozdziałowym zestawie. Wszystkie historyczne etykiety pozostają niezmienione.
- AT-11 ma obecnie **5** figur TikZ, AT-12 **2**; rozdziały nie wprowadzają nowych zależności od zewnętrznych grafik, plików danych ani kodu.
- Testy regresyjne: `application/tests/test_topology_chapters_11_12.py` sprawdzają wszystkie dwanaście kanonicznych rozdziałów w książce, historyczne etykiety, odsyłacze, bilans środowisk TeX, słownictwo, nieparzystą/parzystą formę przecięcia, filtrację z `d³`, problem rozszerzeń i zgodność deklarowanego zakresu dowodu Serre'a.
- Workflow: `.github/workflows/algebraic-topology-audit-ch11-12.yml` dwukrotnie kompiluje książkę ograniczoną do AT-01–12. AT-01–10 służą jako kontekst dla definicji i odsyłaczy, **nie** są ponownie oznaczane jako zaaudytowane w tej iteracji.
- Ostateczny status potwierdzenia kompilacji i oględzin PDF należy zapisać po zakończeniu GitHub Actions i inspekcji wszystkich siedmiu rysunków. Nie wolno deklarować sukcesu przed faktycznym retestem.

## Zakres otwarty

Pełna konstrukcja silnej zbieżności ciągów spektralnych przy nieograniczonych filtracjach i ogólna teoria multiplikatywności z dowolnymi lokalnymi systemami współczynników wymagają odrębnych rozwinięć — nie wynikają ze skończonowymiarowego twierdzenia Serre'a. Nie wykonywano globalnego scalania pozostałych skryptów ani zmian w `main`.

**Następna para:** AT-13 i AT-14, z zachowaniem rytmu dwóch rozdziałów i tego samego standardu audytu.
