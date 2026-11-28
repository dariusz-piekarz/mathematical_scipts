# Audyt LXXIV (74) — rozdział 21: reprezentacja Riesza–Markowa–Kakutaniego

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts.
Gałąź: biblioteka-matematyczna-iteracja-6 (bez zakładania nowej).
Rozdział: chapters/pl/measure_theory/21-twierdzenie-riesza-markowa-kakutaniego.tex.
Blob po poprawkach: 4d7b24bdc4f10a7043b9dcf4ef85211eb4dc4439.

## Bramka wejścia

Rozdział 20 został zamknięty po rzeczywistym przebiegu CI 45276811724: 8+4 zaliczone testy, książka 259 stron, rozdział 20 — 8 stron, oba końcowe PDF-y obejrzane, aktualna wersja źródła 8545b0586adb31dd63a8dba53eb8bc2c51489b01. Raport: audits/measure_theory/00-audyt-lxxiii-rozdzial-20-zamkniecie-2026-11-23.md, commit 054c504ca0ee7ca4f8c49038178e7bd04ae8c412. Rozdziały 15–20 pozostają zamknięte.

## Pierwszy pełny przegląd matematyczny rozdziału 21

Przeczytano cały rozdział (563 wiersze przed korektą), w tym:
1. Przyjęty zakres topologiczny: lokalnie zwarte ośrodkowe przestrzenie metryczne, w odróżnieniu od pełnej wersji twierdzenia dla ogólnych przestrzeni lokalnie zwartych Hausdorffa.
2. Borelowską mierzalność dla metrycznych miar zewnętrznych: argument przez rozdzielone poziomice odległości od zbioru domkniętego i dwie sumy po parzystych/nieparzystych pasach; bez nieuprawnionego przyjmowania ciągłości miary zewnętrznej z dołu.
3. Zwarty przypadek reprezentacji: konstrukcję treści na otwartych zbiorach z dodatniego funkcjonału, przeliczalną podaddytywność przez podział jedności, metryczność miary zewnętrznej, regularność i utożsamienie funkcjonału z całką przez sumy poziomicowe.
4. Lokalizację na kompaktowych wyczerpaniach, zgodność miar z funkcji odcinających, sklejanie na rozłącznych warstwach B_n i regularność przez wyniki rozdziału 20.
5. Gęstość C_c w C_0, tożsamość normy dodatniego funkcjonału z masą skończonej miary i wersję zespoloną z normą wariacji całkowitej.
6. Jednoznaczność, porządek dodatnich funkcjonałów i przykład niewyznaczalności miary przez same momenty na prostej.

**Wykonana korekta źródła, commit f64f6f6b13d2b5c3c1159cf8d6283a8d4ecb3f51:**
- Uzupełniono kluczowy dowód przeliczalnej podaddytywności treści na otwartych: skończone pokrycie zwartego nośnika przez V_i o domknięciu w U_{j_i}, funkcje odcinające ψ_i, ich sumę ψ>0 na nośniku, dodatkową χ o zwartym nośniku w {ψ>0} i jawne θ_i=χψ_i/ψ, przedłużone przez zero. Uzasadniono ciągłość, wymagany nośnik i sumę θ_i=1 na supp f. Poprzednia wersja pomijała argument na granicy zbioru {ψ>0}.
- Rozpatrzono przypadki F=∅ i F=Z przed wprowadzeniem funkcji odległości do F w lemacie o metrycznej mierze zewnętrznej.
- Ujednolicono globalną terminologię: przestrzeń spełniająca drugi aksjomat przeliczalności, także w odniesieniu do rozmaitości.

Kontrola statyczna po poprawce: 20 deklaracji etykiet (wszystkie różne), 27 referencji, 34 środowiska begin/end prawidłowo zagnieżdżone; 8 nazw referencji zewnętrznych do innych rozdziałów wymagających importu. Skład i pełna globalna poprawność odsyłaczy będą sprawdzone przez rzeczywiste CI, nie są poświadczone tym skanowaniem.

## Trwałe testy i workflow

Utworzono tools/tests/test_measure_theory_ch21.py, commit 22af9f8d9ddcd5682c787ef0f28b618696c7489b, blob 986381dae08d182f1509f24e41efce4cc6332511. Osiem przypadków obejmuje: dodatnie funkcjonały i normę na skończonych przestrzeniach, metryczną miarę zewnętrzną dla skończonych atomów, sumy poziomicowe, lokalizację i sklejanie, gęstość C_c w C_0 na przestrzeni dyskretnej, wariację zespoloną i normę, porządek miar oraz regresję LaTeX i podziału jedności. Modele skończone nie są dowodami ogólnych twierdzeń.

Dodano osobny workflow .github/workflows/measure-theory-ch21.yml, commit 0a6d5f5557cc4f9b784a960f7e316a981b3794fc, blob 9548d158bc4318b04ce1ad5df7ccb78820523e17. Workflow uruchamia 8 testów rozdziału i 4 globalne testy integralności całej książki, buduje pełny PDF i osobny rozdział 21 (prawidłowy numer), importuje potrzebne odsyłacze z AUX i publikuje statusy measure-theory/ch21-regressions oraz measure-theory/ch21-pdf.

## Werdykt

**ROZDZIAŁ 21: PIERWSZY AUDYT WYKONANY, W STABILIZACJI.** Poprawki matematyczne i testy zapisane na istniejącej gałęzi. Nie zamykać rozdziału na podstawie samej konfiguracji. Przed uznaniem go za stabilny konieczne są: faktyczne 8+4 testy w CI, obie poprawne kompilacje PDF, logi bez brakujących odsyłaczy, kontrola wszystkich stron PDF, drugi niezależny przegląd matematyczny (szczególnie przejścia od treści na otwartych do miary oraz wersji zespolonej). Dopiero po takim zamknięciu można przejść do rozdziału 22.
