# Algebra abstrakcyjna — AA-27, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Rozszerzenia Artina–Schreiera w charakterystyce dodatniej”.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## 1. Ponowny audyt matematyczny

Ponownie przeanalizowano cały 267-wierszowy rozdział, niezależnie od audytu I, w tym definicje, wszystkie dowody, trzy przykłady, odsyłacze i precyzję notacji.

- **Konstrukcja wprost:** `wp_F(x)=x^p-x` ma jądro `F_p`; wielomian `X^p-X-a` jest rozdzielczy, a jego ciało rozkładu jest `F(α)`. Grupa Galois zanurza się w `(F_p,+)` i dla `a∉wp(F)` ma rząd `p`, co gwarantuje nierozkładalność. **PASS**.
- **Twierdzenie odwrotne:** niezerowość śladu wynika z rozdzielczości; dla `Tr(u)=1` element `α=−Σ_{j=0}^{p−1}jσ^j(u)` spełnia `σ(α)−α=1`; `α^p−α∈F\wp(F)` i `E=F(α)`. **PASS**, w tym w charakterystyce `p`, gdzie `Tr(1)=0`.
- **Klasyfikacja:** przy `a,b∉wp(F)` równość ciał odpowiada dokładnie `b=ca+wp_F(d)` z `c∈F_p^×`, `d∈F`; klasyfikacja przez jednowymiarowe podprzestrzenie `F/wp(F)` jest poprawna. **PASS**.
- **Przykłady:** `F_p(t)` i argument z biegunem w nieskończoności; przypadek trywialny; `F_4`. **PASS**.
- **Terminologia, założenia, etykiety i odsyłacze:** **PASS**; 10 unikatowych etykiet, 5 odsyłaczy; oba zewnętrzne cele istnieją w AA-23 i AA-26.

**Korekty źródła w audycie II: 0**. Źródło jest bajtowo identyczne z wersją po audycie I.

## 2. Testy i dokument PDF

- Wcześniejszy zestaw `AA-27-audyt-I-testy.py`: **17/17 PASS** (uruchomiony ponownie).
- Nowy niezależny zestaw `AA-27-audyt-II-testy.py`: **13/13 PASS**; obejmuje m.in. nierozkładalność wielomianów Artina–Schreiera nad ciałami pierwszymi, konstrukcję śladową, przekształcenia parametrów i kontrolę źródła.
- Wersje repozytoryjne `test_abstract_algebra_ch27.py` i `test_abstract_algebra_ch27_independent.py` wykonane łącznie lokalnie: **30/30 PASS**.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error`: **PASS**; pomocniczy PDF ma 5 stron, z czego 1 strona zawiera testowe etykiety wcześniejszych rozdziałów. **Brak ostrzeżeń LaTeX, niezdefiniowanych odsyłaczy i przepełnień**.
- Wyrenderowano i obejrzano wszystkie 5 stron, bez dostrzeżonych kolizji tekstu.

## 3. Publikacja GitHub

Opublikowano i ponownie zweryfikowano:

- `chapters/pl/abstract_algebra/27-teoria-artina-schreiera.tex`;
- `books/pl/abstract_algebra.tex` — dodany wpis `\input`;
- `catalog/books.json` — 27 rozdziałów algebry abstrakcyjnej;
- `tools/tests/test_abstract_algebra_ch27.py` — 17 testów;
- `tools/tests/test_abstract_algebra_ch27_independent.py` — 13 testów;
- `.github/workflows/abstract-algebra-chapter.yml` — poszerzono zakres do AA-27, w tym oba zestawy testów oraz kompilację książki.

Dla źródła rozdziału potwierdzono **zgodność bajtową** GitHub z lokalnym źródłem:

- SHA-256: `382dc54b77e2bd6a32487447dad6fc8da8f293c52558c66a29009bf67d39f842`;
- Git blob SHA: `628da680adc66f257511a260df4283db8cb9a7d7`.

Dla obu plików testowych również potwierdzono zgodność hashy Git blob.

**Ograniczenie:** wykonano kompilację izolowanego rozdziału, nie całości AA-01–AA-27. Nie potwierdzono jeszcze sukcesu zdalnego GitHub Actions; dodanie testów do CI nie jest równoznaczne z przejściem CI.

## 4. Status

**AA-27: STABILNY — po audycie II bez poprawek; OPUBLIKOWANY** na dotychczasowej gałęzi. Następny rozdział: **AA-28 — audyt I**.
