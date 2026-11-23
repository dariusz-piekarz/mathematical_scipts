# AA-X06 — audyt przekrojowy: ideały, lokalizacja, noetherowskość, pierścienie artinowskie i lemat Nakayamy

**Data:** 23 listopada 2026 r.  
**Repozytorium:** \`dariusz-piekarz/mathematical_scipts\`.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.

## 1. Zakres i identyfikacja niezmienionych źródeł

Główna kontrola obejmuje cztery rozdziały, z zależnościami do AA-10/11:

| Rozdział | Zakres | Git blob |
|---|---|---|
| AA-09 | Pierścienie, ideały, ideały pierwsze i chińskie twierdzenie o resztach | \`c6a5ac5d6f8f067a051c49860eae815915bff7d0\` |
| AA-12 | Pierwiastniki ideałów, lokalizacje i ich własności | \`f64ec91a7fcc58557dba8b13f75b74f6b2ca788d\` |
| AA-13 | Pierścienie noetherowskie i twierdzenie Hilberta o bazie | \`548155ff626fd172691bd241c1240015edae197a\` |
| AA-14 | Pierścienie artinowskie, radykał Jacobsona, Nakayama | \`bd327c84847088000195270dab35e40daa2b73a6\` |

Nie zmieniano matematycznych plików TeX. Celem jest **niezależna kontrola przejść między rozdziałami** z naciskiem na zero-dzielniki, pierwiastniki, lokalizację w zbiorze multiplikatywnym, rozkłady pierścieni artinowskich i warunek skończonego generowania w lemacie Nakayamy.

## 2. Audyt treści i zależności dowodowych

### AA-09 → AA-12: ideały pierwsze, pierwiastnik i lokalizacja

- Sprawdzono logiczne przejście od charakterystyki ideałów pierwszych w AA-09 do wzoru \(\sqrt I=\bigcap_{P\supseteq I,\ P\text{ pierwszy}}P\) w AA-12. Dla pustej rodziny przecięcie jest całym pierścieniem; AA-12 omawia przypadek \(I=R\).
- Dla ideałów \(I,J\) potwierdzono kierunek \(\sqrt{IJ}=\sqrt{I\cap J}=\sqrt I\cap\sqrt J\). W przykładach nad \(\mathbb Z/n\mathbb Z\) pierwsze i maksymalne ideały mają postać \((\overline p)\) dla liczb pierwszych \(p\mid n\).
- Lokalizacja w AA-12 **nie zakłada, że \(R\) jest dziedziną całkowitości**. Relacja na parach \((a,s)\sim(b,t)\) zawiera świadek \(u\in S\) z \(u(at-bs)=0\), co jest istotne przy dzielnikach zera. Zweryfikowano na skończonych pierścieniach, że naiwna równość iloczynów krzyżowych nie wystarcza.
- Sprawdzono nasycenie \(\iota^{-1}(S^{-1}I)=\{a:\exists s\in S,\ sa\in I\}\), zgodność \(\sqrt{S^{-1}I}=S^{-1}\sqrt I\) i odpowiedniość ideałów pierwszych rozłącznych z \(S\). Testy nie odrzucają niesłusznie poprawnych sytuacji, w których nasycenie jest **ściśle większe** niż \(I\).

### AA-12 → AA-13: warunek noetherowski, ilorazy i lokalizacja

- Twierdzenie AA-12 o skończonym generowaniu wszystkich ideałów i stabilizacji wstępujących ciągów stanowi jawny punkt wyjścia AA-13.
- Sprawdzono argument, że ideał lokalizacji jest generowany przez obrazy skończonej rodziny generatorów jego kontrakcji. Istotna subtelność: kontrakcja dowolnego ideału lokalizacji nie musi być identyczna z wyjściowym \(I\), ale na mocy nasycenia nadal jest ideałem i ma skończoną liczbę generatorów.
- W twierdzeniu Hilberta o bazie osobno rozpatruje się współczynniki wiodące wszystkich wielomianów z \(I\) i współczynniki wiodące wielomianów o każdym mniejszym stopniu \(j<D\). Ta druga rodzina jest konieczna: sam wybrany wielomian o współczynniku wiodącym \(1\), np. \(x\in(2,x)\subseteq\mathbb Z[x]\), nie generuje całego ideału \((2,x)\).
- Nie utożsamiono noetherowskości z byciem dziedziną ideałów głównych.

### AA-13 → AA-14: artinowskość, radykał i Nakayama

- Sprawdzono założenia w twierdzeniu „przemienny pierścień artinowski jest noetherowski”: nilpotentność \(J(R)\), iloraz \(R/J(R)\) jako skończony iloczyn ciał, filtrację ideału przez \(I\cap J^k\) i skończone generowanie jej kolejnych ilorazów. Osobno w treści uwzględniono pierścień zerowy.
- Sprawdzono wywód rozkładu \(R\cong\prod_iR/\mathfrak m_i^N\): potrzebne są **parami względnie pierwsze potęgi** ideałów maksymalnych oraz \(J(R)^N=0\). Oba warunki są w AA-14 jawnie uzasadnione.
- Lemat Nakayamy jest sformułowany dla **skończenie generowanego modułu**. Warunek jest niezbędny: źródło zawiera kontrprzykład \(K(x)/K[x]_{(x)}\), dla którego \(\mathfrak mM=M\), ale \(M\ne0\).
- Minimalna liczba generatorów modułu nad pierścieniem lokalnym jest równa \(\dim_{R/\mathfrak m}(M/\mathfrak mM)\), a nie wymiarowi przestrzeni wektorowej \(M\) nad ciałem bazowym. Sprawdzono ten wymóg na modułach z nilpotentnym działaniem \(t\).

## 3. Nowy test I — pierścienie \(\mathbb Z/n\mathbb Z\)

Plik \`tools/tests/test_abstract_algebra_cross_aa09_14.py\`, **wyłącznie biblioteka standardowa Pythona**.

Dla \(2\le n\le72\) wykonano:

| Warunek | Sprawdzenia |
|---|---:|
| Pierwiastniki ideałów \((d)\) | 325 |
| Pierwiastnik jako przecięcie ideałów pierwszych | 325 |
| \(\sqrt{IJ}=\sqrt{I\cap J}=\sqrt I\cap\sqrt J\) | 1 919 |
| Nasycenie ideału względem \(\langle s\rangle\) | 12 026 |
| Zgodność pierwiastnika z lokalizacją | 12 026 |
| Odpowiedniość ideałów pierwszych | 2 422 |
| Równoważność ułamków: pełne porównania par dla \(n\le16\) | 316 125 |
| Radykał Jacobsona | 71 |
| Nilpotentność radykału Jacobsona | 71 |
| Chińskie twierdzenie o resztach | 71 |
| **Razem** | **345 381 / 345 381 PASS** |

Szczególnie kontrolowano lokalizację przez potęgi \(s\): jeśli \(n=\prod p^{e_p}\), to nieodwracalne czynniki \(p\mid s\) znikają po lokalizacji, a pierścień otrzymany jest izomorficzny z \(\mathbb Z/m\mathbb Z\), gdzie \(m=\prod_{p\nmid s}p^{e_p}\), o ile \(\langle s\rangle\) nie zawiera zera. Weryfikacja ułamków korzystała zarówno ze świadków \(u\in\langle s\rangle\) w relacji AA-12, jak i z niezależnej interpretacji w \(\mathbb Z/m\mathbb Z\).

## 4. Niezależny test II — lokalne algebry i lemat Nakayamy

Plik \`tools/tests/test_abstract_algebra_cross_aa09_14_confirming.py\`, wyłącznie biblioteka standardowa Pythona; **inny model i inne algorytmy** niż w teście I.

Dla \(p\in\{2,3\}\) i \(2\le k\le5\) badano algebry \(R=\mathbb F_p[t]/(t^k)\) przez wektory współczynników i bezpośrednie mnożenie:
- jednostki to dokładnie elementy z niezerowym współczynnikiem stałym;
- ideały główne wyznacza wartość najmniejszego niezerowego współczynnika, a łańcuch \((1)\supsetneq(t)\supsetneq\cdots\supsetneq(t^k)=0\) jest kompletny;
- \(J(R)=(t)\), \(J(R)^k=0\), ale \(J(R)^{k-1}\ne0\).

Osobno dla modułów \(M=\bigoplus_i R/(t^{e_i})\) (małe skończone wymiary nad \(\mathbb F_p\)) **wyliczano wszystkie dozwolone układy kandydatów na generatory**. Obraz ich klas w \(M/tM\) miał pełny rząd dokładnie wtedy, gdy ich rzeczywista \(R\)-podmodułowa otoczka generowała \(M\). Rząd otoczki uzyskano z niezależnej eliminacji Gaussa na wektorach \(v,tv,\ldots\).

| Warunek | Sprawdzenia |
|---|---:|
| Jednostki i kryterium Jacobsona | 420 |
| Ideały główne i wartości \(t\)-adyczne | 420 |
| Nilpotentność elementów | 150 |
| Struktura łańcucha ideałów | 8 |
| Nakayama: rzeczywiste generatory i minimalność | 156 067 |
| Dwa generatory dla \((x,y)\subseteq\mathbb F_p[x,y]/(x,y)^2\) | 97 |
| **Razem** | **157 162 / 157 162 PASS** |

Razem: **502 543 / 502 543 sprawdzeń matematycznych PASS**. Liczba ta dotyczy konkretnych przypadków i warunków obliczeniowych, a nie liczby dowiedzionych niezależnych twierdzeń.

## 5. Kontrola strukturalna LaTeX i odsyłaczy

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady |
|---|---:|---:|---:|---:|
| AA-09 | 41 | 1 | 19 | 7 |
| AA-12 | 36 | 7 | 16 | 10 |
| AA-13 | 21 | 6 | 10 | 7 |
| AA-14 | 25 | 11 | 15 | 6 |
| **Suma** | **123** | **25** | **60** | **33** |

Wszystkie **123 etykiety są parami różne**. Wszystkie 25 odsyłaczy mają istniejący cel: 22 we wskazanych rozdziałach, a trzy odsyłacze zewnętrzne — \`aa:ch:wielomiany\` i \`aa:lem:fracfield-well-defined\` (AA-11), \`aa:prz:two-polynomials-not-pid\` (AA-10) — zweryfikowano przez odczyt odpowiednich plików. Żadne środowisko \`\\begin\`/\`\\end\` nie pozostało niedomknięte; wszystkie cztery pliki są dołączone do \`books/pl/abstract_algebra.tex\`.

## 6. Publikacja, odtwarzalność, ograniczenia

Testy wykonano lokalnie z wynikami podanymi wyżej, a następnie opublikowano na istniejącej gałęzi:
- \`tools/tests/test_abstract_algebra_cross_aa09_14.py\`, commit \`8c672b1b5134fc78c07ed0af46a751fb5093423a\`;
- \`tools/tests/test_abstract_algebra_cross_aa09_14_confirming.py\`, commit \`7aeb76a0236f54fb34188abfadd6a17064b9ac3a\`;
- oba kroki z wyzwalaczami w \`.github/workflows/abstract-algebra-chapter.yml\`, commit \`ff06f57c73cd1ebd7a52f6fadaed7d8dafe8a7c3\`.

Odtworzenie:
\`\`\`bash
python tools/tests/test_abstract_algebra_cross_aa09_14.py
python tools/tests/test_abstract_algebra_cross_aa09_14_confirming.py
\`\`\`

**Werdykt matematyczny:** w badanych zależnościach i przykładach nie znaleziono błędów wymagających poprawek, pozostawiono niezmienione źródła AA-09, AA-12, AA-13, AA-14. Nie jest to deklaracja formalnego sprawdzenia wszystkich twierdzeń programu.

**Bramka stabilizacji AA-X06:** zamknąć pełny zdalny workflow z sukcesem dla obu nowych testów, całego tomu AA-01–AA-42, kontroli odsyłaczy i PDF oraz wykonać wizualną kontrolę składów powiązanych rozdziałów. Do czasu uzyskania tych wyników **AA-X06 jest w trakcie stabilizacji**, nie zamknięty.
