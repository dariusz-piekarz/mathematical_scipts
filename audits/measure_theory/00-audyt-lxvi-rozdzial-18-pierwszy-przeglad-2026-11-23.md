# Audyt LXVI (66) — rozdział 18, pierwszy przegląd Radona–Nikodyma i testy

**Data:** 2026-11-23. **Repozytorium:** `dariusz-piekarz/mathematical_scipts`. **Istniejąca gałąź:** `biblioteka-matematyczna-iteracja-6` (bez tworzenia nowej).

**Warunek wejścia:** rozdział 17 zamknięty w audycie LXV (65) na blobie `e8c27586b79374f799533adf99e39b90725ddc25`, po 12/12 testach oraz realnej inspekcji pięciostronicowego PDF. W tej iteracji opracowywany jest wyłącznie rozdział 18; rozdziału 19 nie audytowano.

## 1. Niezależny przegląd matematyczny

Przeczytano cały plik `chapters/pl/measure_theory/18-twierdzenie-radona-nikodyma-i-pochodne-miar.tex`, w tym:
- reprezentację przez `L^2(mu+nu)` dla miar skończonych; sprawdzono ograniczoność funkcjonału `T(u)=∫u dnu`, zastosowanie reprezentacji Hilbertowskiej i uzyskanie `0<=h<=1`;
- wykluczenie `{h=1}` dzięki `nu<<mu` i konstrukcję gęstości `f=h/(1-h)`, bez kołowego powoływania się na twierdzenie Radona–Nikodyma;
- przejście do przypadku sigma-skończonego przez wspólny przeliczalny podział na zbiory o skończonych masach;
- pochodne miar ze znakiem i zespolonych, normę wariacji, rozkład biegunowy;
- regułę łańcuchową i odwrotną, w tym znaczenie `0*∞=0` na `{f=0}`;
- konstrukcję warunkowej wartości oczekiwanej przez Radona–Nikodyma oraz interpretację jako rzutu ortogonalnego w `L^2`.

**Dwie udokumentowane korekty, commit `4b52d2cdab65fb5d4702b36f3f6ea9835120d4cc`:**
1. Dodano drugi, niezależny kontrprzykład do pomijania hipotez sigma-skończoności: na (0,1) miara `mu` Lebesgue'a jest skończona, lecz `nu(E)=0` dla `mu(E)=0` i `nu(E)=∞` dla `mu(E)>0` nie jest sigma-skończona, mimo `nu<<mu`. Gęstość skończona `mu`-prawie wszędzie nie może jej reprezentować: pewien zbiór poziomicowy `{f<=m}` ma dodatnią miarę `mu`, przez co jego całka jest skończona, ale jego wartość `nu` nieskończona. Zachowano rozróżnienie między gęstością z wartościami w [0,∞) a dopuszczeniem +∞ w definicji ogólnej.
2. W przykładzie miary Cantora jawnie ujednolicono przestrzeń mierzalną i miarę porównawczą: `X=[0,1]`, `mu=lambda_1|_X` na `B(X)`; równanie z `kappa` ma teraz identyczną dziedzinę obu miar.

**Zweryfikowany blob po poprawkach:** `6923d52d8e6bf016319465e9f0c18a3470013499`.
Kontrola strukturalna: 28/28 unikalnych etykiet, 32/32 odsyłaczy rozwiązanych w źródłach rozdziałów 16–18, 46 par środowisk prawidłowo zagnieżdżonych, zero użyć `\\mathbf{1}_A` lub `\\mathbb{1}_A`. To kontrola statyczna, nie przebieg PDF.

## 2. Trwałe kontrole i automatyzacja

Dodano `tools/tests/test_measure_theory_ch18.py` (commit `dfb3d29938a1a2c3c1088ce34d02fcbaff8e2077`, poprawka sprawdzanego wzoru `83a6c76e3fd8f2e61b6dd2443783715b1d8a535d`). Test zawiera **8 przypadków**: Hilbertowską konstrukcję gęstości na skończonych przestrzeniach atomowych, składanie po rozłącznych częściach, reguły łańcuchową i odwrotną, zespolone miary i rozkład biegunowy, warunkową wartość oczekiwaną na skończonych podziałach, rzut ortogonalny `L^2`, kontrprzykład niesigma-skończony i źródłowe zależności 16–18.

**Blob testu:** `d0428415793ba9efc70e8a8e13debc1a4a4c0658`.

Zapisano `.github/workflows/measure-theory-ch18.yml`, commit `a880fa7298688e70e1e0a84e723a274cbe7ed301`, blob `0691350af3a6b8f7ea3222992ba5f5c559d8a84e`. Workflow uruchamia osiem testów rozdziału 18 + cztery globalne testy integralności, kompiluje pełny PDF 31-rozdziałowej książki i izolowany PDF rozdziału 18 z zachowaniem numeracji `18`. Izolowany PDF pobiera własne odsyłacze zewnętrzne przez `xr-hyper`, odczytując etykiety z AUX pełnej książki, pomijając 28 własnych etykiet. Publikowane są osobne statusy `measure-theory/ch18-regressions` i `measure-theory/ch18-pdf`.

## 3. Werdykt i kolejny warunek

**Pierwszy przegląd matematyczny:** wykonany, dwie poprawki w repozytorium.
**Testy i konfiguracja CI:** zapisane, wersje i importy sprawdzone.
**Rzeczywiste wykonanie 8+4 testów i PDF:** do potwierdzenia na konkretnym runie (w chwili pierwszego odczytu lista klasycznych statusów commitu była pusta, co nie jest ani sukcesem, ani porażką).
**Rozdział 18: W STABILIZACJI, NIEZAMKNIĘTY.** Następny etap LXVII: odczytać logi i artefakty realnego GitHub Actions, obejrzeć podglądy, osobno ponownie skontrolować główne dowody i dopiero wtedy zamknąć rozdział. Nie rozpoczynać rozdziału 19 wcześniej.
