# Audyt LXXV (75) — rozdział 21: pierwszy PDF i przykład normy atomowej

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts. Gałąź: biblioteka-matematyczna-iteracja-6.

## 1. Stan początkowy po audycie LXXIV

W audycie LXXIV zapisano korektę podziału jedności przy konstrukcji miary z dodatniego funkcjonału oraz 8 przypadków regresyjnych i nowy workflow dla rozdziału 21. Pierwsze pełne wykonanie na commicie 0a6d5f5557cc4f9b784a960f7e316a981b3794fc przeszło poprawnie:
- GitHub Actions https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45280391189; oba konteksty measure-theory/ch21-regressions i measure-theory/ch21-pdf = success;
- job testów 138063002178: Ran 8 tests ... OK + Ran 4 tests ... OK, czyli 12/12;
- job PDF 138063002552: pełna książka 260 stron, 1 901 313 bajtów, osobny rozdział 21: 7 stron, 282 251 bajtów; zaimportowano 8 etykiet zewnętrznych, 20 etykiet lokalnych zachowano, wszystkie odsyłacze rozwiązane;
- job publikacji statusów 138063543382: completed/success.

Pobrano rzeczywisty artefakt CI ID 14869081935 (ZIP 2 667 625 bajtów), wyodrębniono oba PDF-y i końcowe logi. Obejrzano montaż wszystkich siedmiu stron samodzielnego dokumentu. W logach końcowych: pełny skrypt 0 Overfull hbox, 14 nieblokujących Underfull hbox, 0 nierozwiązanych odsyłaczy oraz 56 ostrzeżeń hyperref o zakładkach; samodzielny rozdział 0 Overfull, 0 Underfull, 0 nierozwiązanych odsyłaczy i 3 nieblokujące ostrzeżenia hyperref.

## 2. Problem kompozycji wykryty na rzeczywistym PDF

W pierwszej wersji ostatnia strona 7 zawierała jedynie 493 znaki tekstu, sam krótki akapit podsumowujący. Tekst był poprawny i nieucięty, ale taka kompozycja nie wykorzystuje strony i stanowiła dobrą okazję do rozwinięcia konkretnego zastosowania reprezentacji zespolonej. Zrezygnowano z mechanicznego ściskania układu.

## 3. Dalsze rzeczywiste uzupełnienie matematyczne

W commicie bd98d18a92ccedb5aaab59fce4907b38ab522bfb dopisano przykład skończonej miary atomowej ν=∑ a_j δ_{x_j} dla parami różnych punktów x_j w lokalnie zwartej przestrzeni metrycznej i funkcjonału T(f)=∑ a_j f(x_j). Dowiedziono tożsamości normy ||T||=∑|a_j| bez odwoływania się do ogólnego twierdzenia o normie reprezentacji zespolonej:
- z nierówności trójkąta otrzymano górne ograniczenie;
- wybrano parami rozłączne względnie zwarte otoczenia punktów i funkcje odcinające φ_j, równe 1 w x_j;
- dla faz b_j=conj(a_j)/|a_j| (lub 0 przy a_j=0) funkcja f=∑ b_jφ_j należy do C_c i ma normę supremum co najwyżej 1;
- T(f)=∑|a_j|, a zatem wartość ta jest osiągana.

Obecny blob źródła: fd6eedf8e96f645283ba837061cc3e7c0e955aae.
W commicie be18f56721885eb9c268c50ed81015eb0ffa6f6b poszerzono test źródłowy o etykietę ex:riesz-complex-atoms-21. Obecny blob testu: 64c4d64165410b588c0b795b325725dc63eafa2e. Zachowano osiem metod testowych.

## 4. Werdykt i dalsza bramka

Wersja sprzed dodania przykładu ma potwierdzone zielone 8+4 testy i obie kompilacje. **Aktualna wersja źródła i testu różni się od zatwierdzonej wersji z runu 45280391189**, dlatego nie wolno na jej podstawie ogłosić zamknięcia rozdziału.

**Rozdział 21: W STABILIZACJI.** W kolejnym audycie należy odczytać oba statusy CI dla commitu be18f56721885eb9c268c50ed81015eb0ffa6f6b (lub nowszego, zawierającego tę zmianę), sprawdzić 8+4 testy i prawdziwy PDF, zwłaszcza rozkład ostatnich stron. Dodatkowo wykonać niezależny, szczegółowy przegląd merytoryczny konstrukcji miary zewnętrznej oraz wersji zespolonej. Dopiero po tym można zamknąć rozdział 21 i przejść do 22.
