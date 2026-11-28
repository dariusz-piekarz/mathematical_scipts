# Algebra liniowa — audyt globalny, iteracja 13 (spektrum, Jordan, Frobenius)

**Data:** 2026-11-22. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Poprzednia iteracja:** [12](iteration_12.md), LA07 i LA09–11.
**Decyzja:** CZYSTY w rzeczywiście skontrolowanym zakresie LA14–20; źródła bez zmian. Audyt globalny wszystkich dowodów książki nadal OTWARTY.

## Źródła i identyfikacja

| Rozdział | SHA Git bloba | Wiersze | Środowiska proof |
|---|---|---:|---:|
| LA14 — spektrum, diagonalizacja | 8216c60505324854e2339928bb9be562724e1db2 | 1691 | 17 |
| LA15 — rozkłady macierzy | 5a17f877bf3639cebc33ca95c202aca4498bd6c9 | 1787 | 13 |
| LA16 — wielomian minimalny | 4f8da3c4b87b87ee8f8e6f7c7504637485c6e09a | 887 | 12 |
| LA17 — postać Jordana | 05b93309d0e444f1c3fcbe3489cfd98a0f02846f | 661 | 7 |
| LA18 — Jordan–Chevalley | ef815633cf3a1f795d912c510fbc8575f21e464d | 790 | 6 |
| LA19 — postać Frobeniusa | dd289d5c86452910a89d60ddfbcc558ef6d5be85 | 720 | 7 |
| LA20 — dzielniki elementarne | 8d585c7f4c208990ad5f82222cc47f586144c138 | 727 | 7 |

Łącznie 7263 wiersze, 69 środowisk dowodu, 197 etykiet i 119 odsyłaczy ref/eqref. Kontrola statyczna: zero niedomkniętych środowisk, zero trafień niedozwolonych określeń w skanowanych formach. Liczba wszystkich dowodów w rozdziałach nie jest deklaracją nowej niezależnej formalnej weryfikacji każdego ich wiersza: poniżej opisano zakres rzeczywiście sprawdzonych kroków i testów.

## Główne zależności i dowody

**LA14.** Skontrolowano indukcję w rozkładzie Schura przez kompresję na dopełnienie ortogonalne, odróżniając tę kompresję od ograniczenia operatora; dla normalnych operatorów sprawdzono niezmienniczość dopełnienia dla T i T*. W rzeczywistym twierdzeniu spektralnym własność zespolonego wektora własnego przekłada się na rzeczywisty wektor, a indukcja odbywa się na rzeczywistym dopełnieniu. Jednoczesna diagonalizacja przemiennych operatorów diagonalizowalnych ma prawidłowy argument przez wielomianowe rzuty, bez domknięcia algebraicznego ciała; jednoczesna triangularizacja nad C opiera się na wspólnej fladze.

**LA15.** Zweryfikowano założenia i indukcję dla LU, PLU, Choleskiego; kryterium dodatniej określoności dopełnienia Schura i sprzężenie zespolone. Zredukowany rozkład QR jest jednoznaczny po normalizacji dodatniej przekątnej tylko przy pełnym rzędzie kolumn. W SVD sprawdzono kolejność baz, w Eckarcie–Youngu dolne granice dla normy operatorowej przez E przecięcie ker B i dla normy Frobeniusa przez rzut na im B oraz nierówność Bessela. Pseudoodwrotność i częściowa izometria biegunowa mają właściwe jądra, obrazy i zakresy jednoznaczności.

**LA16–17.** W Cayleyu–Hamiltonie tożsamość dla macierzy dołączonej w K[t] jest wykorzystana przez porównanie współczynników i mnożenie z lewej, a nie przez nieuprawnione podstawienie macierzy do nieprzemiennego pierścienia. Minimalny wielomian dzieli wszystkie anihilujące i charpoly. Rozkład pierwotny powstaje przez Bézouta na względnie pierwszych czynnikach. Przeanalizowano indukcję nilpotentnych łańcuchów Jordana z W=im N, podnoszenie końców łańcuchów oraz dopełnienie ker N. Różnice wymiarów jąder podają jednoznaczne liczby bloków. Postać Jordana wymaga rozkładu na czynniki liniowe nad wybranym K.

**LA18.** Wielomiany CRT są rzutami na uogólnione przestrzenie własne. W rozkładzie T=S+N semisimple część S i nilpotentna N są wielomianami w T, komutują, a ich jednoznaczność jest oparta na rozkładzie na uogólnione przestrzenie własne. W dodatniej charakterystyce poprawnie stosuje się współczynniki Taylora p^[j](λ), nie ilorazy przez j!. Rachunek holomorficzny odróżniono od algebraicznego i ograniczono do C.

**LA19–20.** W postaci Smitha redukcja elementu wyróżnionego ma ściśle malejący stopień i wymusza podzielność bloku; niezmiennikami operacji są ideały minorów. Prezentacja modułu operatora K[t]^n/(tI−A)K[t]^n umożliwia przejście do bloków towarzyszących, a nie jest mylona z bezpośrednim podobieństwem macierzy wielomianowych. W Frobeniusie m_T jest największym czynnikiem niezmienniczym, a χ_T ich iloczynem. CRT rozdziela potęgi nierozkładalnych wielomianów; odwrotna rekonstrukcja wymaga wyrównania wykładników zerami od lewej. Sprawdzono poprawny czynnik deg p w wymiarze ker p(T)^k, w tym przypadki deg p=2 nad F2 i F3.

## Niezależna bateria matematyczna

Uruchomiono na poprawionym skrypcie /mnt/data/la_global13_spectral_tests.py (219 wierszy, seed 20261122; NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0; SHA256 f454ff4ba6a0453023ac05ce517dbe59b2425c455dcb0946890812ef449ad97b).

| Zakres testu | PASS |
|---|---:|
| Filtracje jąder bloków Jordana nad F2, F3, F5 | 20682 |
| Cayley–Hamilton dla losowo podobnych bloków | 3150 |
| Wielomian minimalny anihiluje operator | 3150 |
| Ostrość wykładników: m/(t−λ) NIE anihiluje operatora | 5044 |
| CRT: idempotentność, rangi i zerowe iloczyny rzutów | 2970 |
| Jordan–Chevalley: nilpotentność, przemienność, S²=S dla λ=0,1 | 2970 |
| Filtracje jąder wielomianów nierozkładalnych stopnia 2 | 3468 |
| Dokładna postać Smitha i Frobeniusa nad Q[t] | 250 |
| SVD: rekonstrukcja, unitarność, normy | 2550 |
| Eckart–Young: błąd dokładny i losowi konkurenci | 3400 |
| Rozkład biegunowy: faktoryzacja i projekcje | 1700 |
| QR przy pełnym rzędzie kolumn | 383 |
| Schur: widmo, triangularność i diagonalizacja normalna | 2800 |
| **Łącznie** | **52517 PASS, 0 FAIL** |

Testy obejmują skończone rodziny przykładów, a nie dowód każdego twierdzenia w pełnej ogólności. Obliczenia nad ciałami skończonymi i Smith nad Q[t] są dokładne, SVD/QR/Schur numeryczne z tolerancją. W trakcie weryfikacji wzmocniono test ostrości wielomianu minimalnego: obecnie rzeczywiście sprawdza, że m_T/(t−λ) przestaje zerować operator, a nie tylko niezerowy rząd operatora T−λI. Całość po tej zmianie przeszła ponownie 52517/52517.

## CI i wersje źródła

[GitHub Actions 45047971276](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047971276) completed/success dla commitu 3078c9ca833f69d908bddbb616086646898e64e6. Osobny odczyt wszystkich siedmiu plików z tego commitu potwierdził identyczne SHA z aktualną gałęzią. Nie zmieniano źródeł i nie wykonywano nowej kontroli wizualnej pełnego PDF w tej iteracji.

## Decyzja i dalszy plan

**ITERACJA 13 CZYSTA** w badanym zakresie LA14–20. Globalna niezależna lektura wszystkich dowodów książki pozostaje OTWARTA. Kolejny blok to LA21–28: komutant, równania Sylvestera/Lapunowa, Riccatiego, sterowalność i obserwowalność, gramiany i minimalne realizacje. W szczególności kontrolować ścisłe hipotezy stabilizowalności/wykrywalności oraz odrębność czasu ciągłego i dyskretnego. Nie resetować zamkniętej stabilizacji LA12–32 ani nie dopisywać opcjonalnego zakresu bez zgody użytkownika.
