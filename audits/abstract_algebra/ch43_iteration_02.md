# AA-43 — audyt 2: niezależna kontrola dowodów i przypadków brzegowych

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`; **rozdział:** `43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex`.

## Cel

Niezależny od kontroli kompilatora przegląd sześciu dowodów AA-43, precyzji definicji i warunków na charakterystykę oraz ciało stałych; porównanie ze starszym źródłem `sources/pl/galois(2).tex` i uzupełnienie luk.

## Macierz audytu dowodów

| Wynik | Kluczowy punkt i szczególne przypadki |
|---|---|
| `aa:st:differential-field-rules` | $D1=0$ wynika z $D(1\cdot1)=2D1$; reguła odwrotności i ilorazu wymaga niezerowego mianownika; $\mathbb Q\subseteq C_K$ potrzebuje char $0$ |
| `aa:tw:algebraic-derivation-extension` | wzór $D\alpha=-m_\alpha^D(\alpha)/m'_\alpha(\alpha)$ ma niezerowy mianownik **tylko przy rozdzielczości**; reprezentant modulo minimalny wielomian sprawdzono przez Leibniza; dowolne rozszerzenie jest sumą skierowaną skończonych |
| `aa:cor:algebraic-constants` | $m_\alpha$ jest unormowany, więc wielomian pochodnych współczynników ma stopień mniejszy; bez algebraicznej domkniętości stałych kontrprzykładem jest $\mathbb Q(x)\subseteq\mathbb Q(i)(x)$ |
| `aa:tw:differential-trace-norm` | iloczyn/suma po **wszystkich zanurzeniach**, bez hipotezy normalności; przechodzenie derywacji przez zanurzenia wymaga jednoznaczności przedłużenia i rozdzielczości |
| `aa:lem:primitive-extension-constants` | część $m=0$ formalnego szeregu Laurenta musi zostać odjęta; dla $m<0$ człon $t^{m-1}$ jest nadal poprawny, a $m$ nie jest zerem w ciele char 0 |
| `aa:lem:exponential-extension-constants` | warunek $Du/u=-mh$ dopuszcza **ujemne i dodatnie całkowite $m$**, nie tylko dodatnie; nową stałą jest $ut^m$, i odwrotnie pochodzi ona z najwyższego współczynnika niezerowego szeregu |

**Wynik kontroli matematycznej:** nie wykryto fałszywego twierdzenia w powyższych sześciu dowodach. W szczególności odróżniono przypadki przestępne od algebraicznych, a brak nowych stałych sprawdzono przez dokładne warunki konieczne i dostateczne.

## Realnie wprowadzona poprawka

W przykładzie `aa:prz:logarithmic-extension` wersja pierwsza poprawnie konstruowała **formalny** generator przestępny z pochodną $1/x$, lecz zdanie o interpretacji przez zarodek $\log x$ nie zawierało jawnego dowodu, że analityczny zarodek jest przestępny nad $\mathbb C(x)$.

W wersji drugiej dodano argument: jeśli $\ell=\log x$ byłaby algebraiczna i $L=\mathbb C(x,\ell)$ miało stopień $d$, to z tożsamości derywacyjnej śladu otrzymalibyśmy
\[
D\bigl(\operatorname{Tr}_{L/K}(\ell)/d\bigr)=1/x.
\]
Jest to sprzeczne z tym, że pochodna funkcji wymiernej ma w każdym skończonym biegunie resztę zero, podczas gdy $1/x$ ma resztę $1$ w $0$. Dowód nie zakłada więc niejawnie przestępności wybranego analitycznego modelu.

W pliku `tools/tests/test_abstract_algebra_ch43.py` usunięto również tautologiczny test porównujący wyrażenie samo ze sobą; pozostały niezależne sprawdzenia relacji kwadratowej, śladu i normy. **Commity:** źródło `200ff367dd85793ab8e01ccedfc12bc8543a8d91`, test `d02dd2da56bd62b236530d4f98e22e1875e86821`.

## Kontrola niezależności obliczeń

W `tools/tests/test_abstract_algebra_ch43.py` formuły na pochodną w kwadratowym rozszerzeniu są sprawdzane symbolicznie w \(\mathbb Q(x)\), przy wykorzystaniu SymPy tylko do upraszczania i obliczania pochodnych. Drugi test `tools/tests/test_abstract_algebra_ch43_independent.py` realizuje osobny model w bazie $1,\alpha$ z dokładnymi ułamkami `fractions.Fraction`, sprawdzając osobno:
- relację $D(\alpha^2+b\alpha+c)=0$;
- pochodną śladu i pochodną logarytmiczną normy;
- regułę Leibniza dla produktów niezależnych elementów;
- pochodne logarytmiczne wymiernych iloczynów potęg $(x-a)^m$, także dla $m<0$.

Od strony założeń testy obejmują przypadki specjalizowanego wyróżnika $\Delta\ne0$ i wymagają niezależnego dowodu ogólnego; nie interpretujemy testów pojedynczych wartości $x$ jako dowodu tożsamości abstrakcyjnej.

## Zmiany w strukturze książki i katalogu

AA-43 dodano do `books/pl/abstract_algebra.tex` po AA-42 oraz do tablicy `catalog/books.json`. Główną bramkę źródłową `tools/tests/test_abstract_algebra_global_integrity.py` rozszerzono na **43 pliki kanoniczne**, zachowując **11 ukończonych audytów przekrojowych AA-01–AA-42** jako historyczne potwierdzenie tych 42 rozdziałów, oraz wymagając osobno raportu `ch43_iteration_01.md`. Zaktualizowano też `.github/workflows/abstract-algebra-chapter.yml` do kompilacji 43 rozdziałów i niezależnego uruchomienia obu nowych testów.

## Dalsza bramka

**AA-43 nie jest oznaczony jako stabilny przed uzyskaniem zielonego CI na najnowszym źródle i faktycznym przejrzeniem stron nowego PDF.** Po uzyskaniu dowodów z przebiegu GitHub Actions należy dodać raport końcowy lub uzupełnić ten dokument o dokładne wyniki, błędy/ostrzeżenia LaTeX, integralność odsyłaczy, liczbę stron AA-43 i wynik oględzin. Nie rozpoczynać AA-44, dopóki AA-43 nie osiągnie stabilności.
