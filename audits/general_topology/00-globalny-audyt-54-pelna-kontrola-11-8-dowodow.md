# Topologia ogólna — globalny audyt 54: pełna kontrola wszystkich 8 dowodów rozdziału 11

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Badany plik:** `chapters/pl/general_topology/11-zupelnosc-i-twierdzenie-bairea.tex`; blob `8f13420add065dca19d2653c86b0e5781aef2fe7` (351 wierszy).

## Metoda i konkretne ryzyka

Ponownie odczytano wszystkie **8 aktualnych środowisk `proof`** z hipotezami, definicjami i kontekstem, sprawdzając zwłaszcza brak niejawnej zwartości kul metrycznych w konstrukcji Baire'a, orientację implikacji między pierwszą kategorią i gęstością, dziedziczenie przez otwarte podprzestrzenie oraz niepustość przestrzeni w twierdzeniach o sumach domkniętych. Sprawdzono też przykłady podprzestrzeni niezupełnych i zupełności metryki przeniesionej przez homeomorfizm. Nie zmieniono LaTeX.

## Indywidualna macierz 8/8 dowodów

| ID | Etykieta i wiersze proof | Weryfikacja argumentu |
|---|---|---|
| 11-01 | `prop:topog-baire-zbiezny-cauchy`, 32–39 | Z x_n→x dla ε>0 wybiera się N z d(x_n,x)<ε/2, więc d(x_m,x_n)<ε. Jeśli x_n→x i x_n→y, to d(x,y)≤d(x,x_n)+d(x_n,y)→0, co wymusza x=y. Nie potrzeba zupełności ani niepustości całej przestrzeni. |
| 11-02 | `thm:topog-baire-podprzestrzen-zupelna`, 47–60 | Domknięte A w zupełnym X pochłania granice wszystkich ciągów Cauchy'ego w A. Dla zupełnego A i x∈cl_X A ciąg a_n∈A z d(a_n,x)<1/n jest Cauchy'ego i zbiega do a∈A; jednoznaczność granicy w X daje a=x. Puste A i X także są poprawne. |
| 11-03 | `prop:topog-baire-rownowaznosci`, 152–172 | Dla nigdziegęstych A_n dopełnienia cl_X A_n są otwarte gęste. Ich przecięcie jest gęste dokładnie wtedy, gdy suma domknięć ma puste wnętrze. Zbiór pierwszej kategorii jest zawarty w takiej sumie, więc też ma puste wnętrze. Gdy niepusty otwarty U byłby zawarty w sumie dopełnień gęstych otwartych G_n, byłby pierwszej kategorii, co daje odwrotny kierunek. Nie używa się topologii metrycznej. |
| 11-04 | `thm:topog-baire-metryczne`, 186–217 | Indukcyjnie konstruowane niepuste kule domknięte K_n⊂G_n z K_1⊂U, r_n<2^{-n}, spełniają K_{n+1}⊂B(x_n,r_n)⊂K_n. Środki x_m dla m≥n należą do K_n, więc d(x_m,x_n)≤r_n<2^{-n}; ciąg środków jest Cauchy'ego. Zupełność daje x, a domkniętość K_n zapewnia x∈∩K_n⊂U∩∩G_n. Dowód nie zakłada zwartości kul domkniętych (fałszywej w ogólnej przestrzeni metrycznej) i działa przy X=∅ (brak niepustego U). |
| 11-05 | `cor:topog-baire-zupelnie-metryzowalne`, 243–247 | Istnienie zgodnej metryki zupełnej pozwala zastosować metryczne twierdzenie Baire'a; gęstość i otwartość zależą wyłącznie od topologii. Wniosek dotyczy zupełnej metryzowalności, a nie zupełności dowolnej metryki zgodnej. |
| 11-06 | `thm:topog-baire-wymierne-nie-gdelta`, 267–280 | Gdyby Q=∩U_n dla otwartych U_n, wszystkie U_n byłyby gęste w R. Dla numeracji Q={q_n} otwarte gęste V_n=R\{q_n} miałyby razem z U_n gęste, więc niepuste przecięcie na mocy Baire'a. Tymczasem ∩(U_n∩V_n)=Q∩(R\Q)=∅. Zastosowano zupełność R, a nie mylono kategorii z miarą. |
| 11-07 | `prop:topog-baire-otwarte-podprzestrzenie`, 301–315 | Dla otwartego U⊂X i gęstych otwartych H_n⊂U, zbiory G_n=H_n∪(X\cl_X U) są otwarte w X. Ponieważ cl_X H_n⊇cl_X U, suma G_n jest gęsta w X: domknięcie zawiera cl U oraz X\cl U. Dla otwartego niepustego V⊂U własność Baire'a X daje x∈V∩∩G_n, a G_n∩U=H_n. Nie wyciąga się nieprawdziwego wniosku o dziedziczeniu zupełności konkretnej metryki przez otwarte U. |
| 11-08 | `cor:topog-baire-domkniete`, 335–342 | Gdyby każde F_n domknięte w niepustej X miało puste wnętrze, wszystkie byłyby nigdziegęste. Wobec X=∪F_n cała niepusta otwarta X byłaby pierwszej kategorii w sobie, wbrew charakterystyce przestrzeni Baire'a. Hipoteza X≠∅ jest konieczna dla tak sformułowanego wniosku. |

## Przykłady i zależności

**`ex:topog-baire-podstawowe-przyklady`: PASS.** Zupełność R wynika z Bolzana–Weierstrassa i własności Cauchy'ego, domknięty [0,1] dziedziczy zupełność R, a ciągi 1/(n+1) w (0,1) oraz wymierne aproksymacje √2 w Q nie mają granicy we wskazanych podprzestrzeniach.

**`ex:topog-baire-metryka-przedzial`: PASS.** Homeomorfizm h:(0,1)→R dany tan(π(t−1/2)) przenosi kompletną metrykę z R do zgodnej metryki zupełnej d_h. Zwykła metryka |s−t| na (0,1) jest niezupełna, chociaż obie indukują tę samą topologię. Rozróżniono zatem poprawnie niezmiennik topologiczny „zupełna metryzowalność” od własności wybranej metryki.

**Rachunek zależności:** rozdział 10 zapewnia język zgodnych metryk; twierdzenie o podprzestrzeniach zamkniętych jest niezależne od twierdzenia Baire'a; metryczne twierdzenie Baire'a poprzedza wersję topologiczną. Dowód nie powołuje się kołowo na twierdzenia o przestrzeniach polskich z rozdziału 19.

## Wynik i zakres globalny

**8/8 PASS** — każde aktualne środowisko `proof` ma dokładną etykietę z macierzy 34 i indywidualną ocenę. Nie wykryto nowej luki wymagającej edycji źródła. Nie wykonano formalizacji Lean ani ponownego renderingu PDF; źródło jest niezmienione.

Z raportem 53 stan pełnej indywidualnej dokumentacji wzrósł do **250/325**; niniejszy raport podnosi go do **258/325**. Pozostają **67** dowodów: rozdział 12 (14), rozdział 13 (9), rozdziały 24–26 (44). Historycznych raportów i stanów nie nadpisujemy. CI nowego commitu wymaga odrębnej walidacji; kolejny etap dotyczy rozdziału 12.
