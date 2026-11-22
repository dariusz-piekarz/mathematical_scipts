# Topologia ogólna — mapa nakładek i zatwierdzony dalszy zakres

**Stan:** 22 listopada 2026.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Cel:** planować rozdziały 23–25 i zagadnienia wariacyjne
bez powielania materiału znajdującego się już w Bibliotece.

## 23. Wymiar topologiczny

Kanoniczne źródło: `chapters/pl/general_topology/23-wymiar-topologiczny.tex`.
Obejmuje wymiar pokryciowy Lebesgue'a,
mały i duży wymiar indukcyjny,
charakterystykę wymiaru zero,
przykłady Cantora i odcinka,
nerwy skończonych pokryć,
triangulacje i wymiar sześcianu.

**Istotne źródła powiązane, bez powielania:**
- `chapters/pl/algebraic_topology/19-stopien-indeks-punktu-stalego-i-twierdzenie-lefschetza.tex`
  — zawiera już dowód twierdzenia Brouwera o punkcie stałym.
  W rozdziale 23 używamy tego wyniku do udowodnienia
  własności Poincarégo–Mirandy, a następnie dolnego
  oszacowania wymiaru sześcianu, zamiast ponownie
  dowodzić całego twierdzenia Brouwera.
- `chapters/pl/algebraic_topology/10-homologia-i-kohomologia-c-echa-od-pokryc-do-granic-przestrzeni.tex`
  — nerwy pokryć w kontekście (ko)homologii.
  W 23 badamy tylko konstrukcję odwzorowania
  barycentrycznego i rząd pokrycia.
- `chapters/pl/measure_theory/26-miara-hausdorffa-i-wymiar-hausdorffa.tex`
  — wymiar Hausdorffa; różni się od wymiaru
  pokryciowego i zależy od metryki.
  Nie przenosić do rozdziału 23 dowodów miarowych.

**Otwarta uwaga do audytu:** pełne twierdzenia porównawcze
\(\dim X=\operatorname{ind}X=\operatorname{Ind}X\)
dla ogólnych klas przestrzeni metrycznych
wymagają odrębnego dowodu; na razie
rozdział 23 wykazuje zgodność w wymiarze 0.

## 24. Grupy topologiczne — kolejny zatwierdzony etap

- `chapters/pl/abstract_algebra/01-grupy-podgrupy-i-grupy-cykliczne.tex`,
  `02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex`,
  `03-dzialania-grup-orbity-i-rownanie-klas.tex`
  — grupy, homomorfizmy, ilorazy i działania **algebraiczne**.
- `chapters/pl/measure_theory/23-miara-haara-na-grupach-lokalnie-zwartych.tex`
  — już definiuje grupę topologiczną, translacje,
  grupy lokalnie zwarte i konstruuje miarę Haara.
  Nie wolno kopiować dowodów miarowych do nowego rozdziału.
- **Nowy zakres:** relacja topologii do działań grupowych,
  topologia otoczeń jedynki, jednorodność i translacje,
  podgrupy otwarte/domknięte, ilorazy topologiczne,
  przykłady, a następnie metryzowalność
  przez lewostronnie niezmiennicze metryki
  (w odpowiednich hipotezach).
  Dokładny zakres twierdzeń i warunków
  zostanie ustalony po stabilizacji rozdziału 23.

## 25. Continua — kolejny zatwierdzony etap

- `chapters/pl/general_topology/08-spojnosc.tex`
  zawiera definicje spójności, składowe,
  spójność drogą i lokalną oraz krzywą sinusową topologa.
- **Nowy zakres bez powtórzeń:** continua jako niepuste
  zwarte spójne przestrzenie Hausdorffa,
  continuum nierozkładalne, strukturę podcontinuów,
  niektóre twierdzenia o obrazach i funkcjach Peana,
  granice odwrotne z zachowaniem ścisłych hipotez.
  Nie powtarzać podstaw rozdziału 08.

## Analiza wariacyjna: Mosco i zbieżność epigraficzna

- `chapters/pl/functional_analysis/16-funkcjonaly-wypukle-i-podstawy-rachunku-wariacyjnego.tex`
  omawia funkcjonały wypukłe, półciągłość z dołu,
  koercywność i metodę bezpośrednią.
  Nie zawiera pełnego rozdziału o zbieżności Mosco
  ani o zbieżności epigraficznej.
- `chapters/pl/general_topology/22-zbieznosc-kuratowskiego-wijsman-attouch-wets.tex`
  obejmuje topologiczną zbieżność zbiorów
  i funkcji odległości, nie zaś zbieżność
  wypukłych funkcjonałów w topologii słabej i silnej.
- **Właściwy docelowy skrypt:** analiza funkcjonalna /
  analiza wariacyjna, nie topologia ogólna.
  Planowany zakres: epigrafy, zbieżność epigraficzna,
  zbieżność Mosco w przestrzeni Hilberta
  lub refleksywnej przestrzeni Banacha przy
  wyraźnych hipotezach, związki z minimalizatorami,
  podgradientami i zbieżnością zbiorów.
  Rozdział powinien odsyłać do FA-16 i TO-22
  bez kopiowania definicji z obu źródeł.

## Zasady wykonania

Zachowujemy regułę: jeden nowy rozdział, iteracyjny
audyt do dwóch kolejnych czystych kontroli
na tym samym blobie oraz jeden audyt dodatkowy,
rzeczywista kompilacja samodzielna i globalna
oraz wizualna kontrola PDF.
Nowe materiały 24–25 i materiały o Mosco
nie są jeszcze napisane ani oznaczone jako stabilne.
