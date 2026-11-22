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

## 24. Grupy topologiczne — etap ukończony i stabilny

Kanoniczny rozdział:
`chapters/pl/general_topology/24-grupy-topologiczne-i-przestrzenie-jednorodne.tex`.
Status: **stabilny 2/2 + 1**, 10-stronicowy PDF
i [zielone CI](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45053429106).

- `chapters/pl/abstract_algebra/01-grupy-podgrupy-i-grupy-cykliczne.tex`,
  `02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex`,
  `03-dzialania-grup-orbity-i-rownanie-klas.tex`
  zawierają już algebraiczne definicje i dowody.
  Rozdział 24 bada topologiczne działanie na G/H,
  kryterium jego Hausdorffowości, podgrupy
  i ich domknięcia oraz topologiczne twierdzenie
  o izomorfizmie, bez powtórzeń algebry grup.
- `chapters/pl/measure_theory/23-miara-haara-na-grupach-lokalnie-zwartych.tex`
  zawiera konstrukcję miary Haara na grupach lokalnie zwartych.
  Rozdział 24 kończy się na własnościach topologicznych
  i jednostajnych grup; nie kopiuje dowodu o mierze.
- Nowe i odrębne wyniki rozdziału 24:
  regularność wszystkich grup Hausdorffa,
  ciągłość homomorfizmu sprawdzana w e,
  działanie G na G/H, domkniętość centrum,
  składowa neutralna i iloraz całkowicie niespójny,
  lewe/prawe struktury jednostajne i pełne
  twierdzenie Birkhoffa–Kakutaniego z dowodem
  konstrukcyjnym.
- Następny etap: **continua — rozdział 25**,
  bez odtwarzania podstaw spójności z rozdziału 08.

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
Rozdział 24 jest już stabilny. Rozdział 25 o continuach i planowany
materiał o zbieżności Mosco nie są jeszcze napisane ani stabilne.
