# GKT36 — drugi audyt kontrolny i domknięcie merytoryczne

Rozdział drukowany 36, źródło `chapters/pl/graph_and_knot_theory/29-analityczne-podstawy-teorii-seiberga-wittena-przestrzenie-modu.tex`, blob `6d8e804a819ba85c2b6b75f3638728115011c894`, commit źródłowy `f980639a0ee2ebca6da2745768556fe6c2adcf56`, 1040 wierszy. Źródło bez zmian od poprzedniego czystego audytu.

Kontrola: przekrój Coulomba, kompleks deformacyjny i jego indeks, oszacowanie Weitzenböcka, regularność Sobolewa i zwartość, rzutowanie Fredholma, orientacje, równanie ściany i lokalny model zmiany komory. Bez nowych istotnych uwag. 14/14 różnych celów odsyłaczy, bez niejednoznaczności w trzech rozdziałach SW; 36/36 zgodnych środowisk. Nie ponawiano weryfikacji publikacji zewnętrznych. Model Kuranishiego i generyczność redukowalnego operatora Diraca nadal przyjęte jako wyniki analityczne, a nie udowodnione tutaj.

Niezależne obliczenia SymPy: 400 prób całkowitych macierzy T i P, 357 spełniających założenie surjektywności [T P]; dla każdej z 357 sprawdzono jądro i cokernel projekcji z ker[T P] na przestrzeń parametrów oraz równość indeksów. 8400 dokładnych rachunków afinicznego równania ściany i niezerowej pochodnej (w jednostkach z wyłączonym czynnikiem 2pi). Wszystkie asercje PASS; testy nie zastępują twierdzeń analitycznych.

CI 45772272907: full-book-pdf i structural-audit success. Artefakt 15094847676 pobrany i rozpakowany, PDF 393 strony, plik ostrzeżeń 0 bajtów. Obejrzano wszystkie 10 stron GKT36 (PDF 335–344, drukowane 325–334), w tym rysunek komór. Bez istotnych usterek składu. CI 45772272854: finite-models success, chapter-pdf w toku w chwili zamknięcia audytu. Terminologia 45772272894 success. CI aplikacji 45772272804: reader-ui success, index-and-test failure na etapie Audit repository-wide chapter and graph coverage; przyczyny w tej iteracji nie ustalano. Pełna stabilizacja techniczna repozytorium pozostaje niepotwierdzona.

Stan GKT36: 2/2 czyste audyty matematyczne, 36/43 rozdziałów domkniętych merytorycznie. Kolejny rozdział: GKT37, z uwzględnieniem ujednolicenia modelu Kuranishiego oraz zakresu założeń z GKT35–36.
