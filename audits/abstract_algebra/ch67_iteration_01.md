# AA-67 — etap D, pierwszy audyt stabilizacyjny

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Źródło a79a86a0b97e7482f1f392bdeeb3f0633d87658f (commit b2f73d1e7852a35efb00cf6ecdfbc88354628e72).

Zakres: uniwersalna własność modułu Verma skonstruowanego w AA-62, największy właściwy podmoduł, lokalna nilpotentność w ilorazie przez relacje potęg generatorów ujemnych, symetria wag i skończoność wymiaru przez uśrednianie po grupie Weyla, klasyfikacja reprezentacji i prostota ilorazu przez twierdzenie Weyla, przykład sl2.

Audyt sześciu dowodów:
1. Jednorodność ideału Serre'a zapewnia rozkład na wagi, różne wielostopnie dają różne wagi, a każdy wielostopień zawiera skończenie wiele słów. Odwzorowanie T do modułu cyklicznego zeruje dwustronny ideał relacji i komutuje z generatorami przez rekurencję z AA-62. Nie wymaga skończoności wymiaru modułu docelowego.
2. Projekcje interpolacyjne działają na skończonym nośniku wag każdego wektora, więc każdy podmoduł rozkłada się wagowo; suma właściwych podmodułów nadal nie zawiera jednowymiarowej składowej najwyższej.
3. Wektory f_i^(m_i+1)v są zerowane przez e_j również dla j=i. Ich podmoduły nie zawierają wagi najwyższej, co gwarantuje niezerowość ilorazu. Lokalna nilpotentność e_i wynika z dolnego ograniczenia współczynnika wielostopnia; dla f_i wykorzystano relacje Serre'a, uogólnioną regułę Leibniza dla ad f_i na słowach i wzór dwumianowy. Dla p>=b+m_i każdy składnik znika.
4. Moduł sl2 generowany przez wektor wagowy mieści się w skończonej rozpiętości f^a e^b u; stabilność względem e wynika z operatorowej tożsamości komutacyjnej, bez założenia najwyższej wagi u. Własność wagowa względem ker(alpha_i) pozostaje zachowana.
5. Średnia po skończonej grupie Weyla jest niezmiennicza i zerowa, ponieważ h_i tworzą bazę. Współczynniki |W| lambda w bazie korzeni prostych są sumami nieujemnych całkowitych współczynników lambda-w mu. Daje to skończony prostokąt wielostopni, również dla układów redukowalnych; nie użyto porządku na K ani wzoru wymiarowego Weyla. Każda składowa wagowa ma skończony wymiar. Jednoznaczność i konieczność pochodzą z AA-65.
6. Po wykazaniu skończoności wymiaru Q twierdzenie Weyla pozwala rozłożyć go na moduły proste. Rzut generatora na każdy składnik jest niezerowy, więc każdy składnik wnosi niezerowy wektor do jednowymiarowej najwyższej przestrzeni wagowej. Dokładnie jeden składnik; N=R(lambda). Nie ma zależności kołowej.

Regresje rzeczywiście wykonane w JavaScript:
- 5424602171eb61a2ad35a3828febe67fdb481a7d: 21 modeli rzędu jeden, 231 kontroli relacji i jąder operatorów podwyższających; 15 cyklicznych modeli A2 w iloczynach tensorowych, suma wymiarów 182, 155 przestrzeni wagowych, 310 symetrii wag, 30 kontroli relacji potęg generatorów. Dokładna eliminacja BigInt. PASS.
- 5ff3708fc37124565246563f1befd347fc8e5a8a: 7 układów korzeni (A1,A2,B2/G2 z niesymetrycznymi macierzami, A1+A1,A3,C3), 104 elementy grup łącznie, 196 wag dominujących, 5096 elementów orbit z krotnościami, 16087 zaakceptowanych i 30981 odrzuconych kandydatów w skończonej siatce wielostopni, 138012 kontroli współczynników średniej. Arytmetyka małych całkowitych macierzy i wyznaczników, sprawdzenie całkowitości wyników. PASS. Nie jest to formalizacja Lean.

Integracja książki, katalogu, planu i 12 testów przekrojowych na 67 rozdziałów. Atomowa integracja przez GraphQL nie powiodła się; zastosowano aktualizacje pojedynczych plików z kontrolą SHA. Pełny CI i oględziny PDF pozostają do potwierdzenia. P i AA-68 nieotwarte.
