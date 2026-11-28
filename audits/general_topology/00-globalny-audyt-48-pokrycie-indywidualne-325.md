# Topologia ogólna — audyt globalny 48: kontrolowany stan 325 dowodów i zakres dokumentacji matematycznej

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Definicje statusów — nie utożsamiać różnych kontroli

- **Zindeksowany**: dowód ma w macierzach globalnych 33–35 identyfikator `NN-NN`, aktualną etykietę i wiersz źródła. To kryterium spełnia **325/325**.
- **Stabilizacja rozdziałowa**: istnieją wcześniejsze powtarzane audyty 2+1; po zmianach rysunków rozdziały 06 i 21 dostały osobne nowe 2+1 (39–41). Potwierdza to wykonaną pracę rozdziałową, **nie** nową indywidualną kontrolę każdego argumentu w tym raporcie.
- **Pełna dokumentacja dowód po dowodzie na bieżącym blobie**: jeden raport obejmuje **każde** środowisko `proof` rozdziału z osobną etykietą i konkretną oceną argumentu, a źródło odpowiada podanemu SHA. Równoważnie: dla 06 jawna lista wszystkich 18 w raporcie 40 i potwierdzenie zmienionego bloba w 41. To bardziej wymagający standard niż sama liczba `proof`, skrócony rejestr albo przykład selektywny.
- **Częściowa kontrola dokumentacyjna** oznacza, że są audyty lokalne i/lub globalne selektywne, ale **nie wykazano jeszcze** w jednolitym nowym rejestrze, że wszystkie dowody danego rozdziału otrzymały indywidualny opis merytoryczny. **Nie oznacza to, że dowodów nie sprawdzono w ogóle albo że są niepoprawne**.

## Bilans oparty na aktualnych 26 blobach i macierzach 33–35

| Rozdział | Git blob źródła | Liczba proof | Dowody z indywidualną dokumentacją | Raporty dowodowe / stabilizacyjne |
|---|---|---:|---:|---|
| 01 | `1e8ee853eb9915d96913e5a0a8cdb5e32f2ec5f6` | 9 | 9 | 46 |
| 02 | `53a8dc7e62590a9011bd5858eedb4141c5f38162` | 12 | 12 | 46 |
| 03 | `b571753b5ab9a8777424fc32f6c4a54a4048af77` | 15 | 15 | 47 |
| 04 | `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` | 17 | 17 | 47 |
| 05 | `462acd8f3e1e350478d921429118ec19ac7f4ca8` | 16 | — | 37/44, lokalne 2+1 |
| 06 | `71d7b30abb97286b7c64ddd5e369ec9f69ea1ff5` | 18 | 18 | 40 + 41 |
| 07 | `0c31028e8fd301d805781b676c6713a2572501cf` | 18 | — | 44, lokalne 2+1 |
| 08 | `51b5cd2adf19a0345510bd14d5c0ac318cef3ae1` | 15 | — | 36, lokalne 2+1 |
| 09 | `f483271af93842198c094c95f73a68584e835215` | 10 | — | 44, lokalne 2+1 |
| 10 | `1bc0fb72953cb70bcec7c60d3c2fc222ba1851c6` | 14 | — | 43, lokalne 2+1 |
| 11 | `8f13420add065dca19d2653c86b0e5781aef2fe7` | 8 | — | 43, lokalne 2+1 |
| 12 | `13597073db07742089b82ae3fc9878733dea5e88` | 14 | — | 43, lokalne 2+1 |
| 13 | `c9078636452731e42a56196e84b5ed9831120e6b` | 9 | — | 44, lokalne 2+1 po korekcie |
| 14 | `24ca61f0e19fe6674719fc76e53073aa82cc755c` | 7 | 7 | 15 |
| 15 | `82e0fb5be75489017c8ea1844c698c87ce580901` | 7 | 7 | 16 |
| 16 | `1c2fcb925d62120feaea468400e48842a508a062` | 7 | 7 | 18 |
| 17 | `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4` | 10 | 10 | 19 |
| 18 | `f7340514548ed3dfb5d98793bf7068fd84276c30` | 9 | 9 | 20 |
| 19 | `dd05dd723a4e92756d1e339309079c68a4580485` | 9 | 9 | 21 |
| 20 | `2607376331f94935063107dee49148b45cc1679f` | 11 | 11 | 22 |
| 21 | `eae0bef9c2357189e1bdb7c9398b845fe7347c7b` | 15 | 15 | 23 + 39–41 |
| 22 | `33765c2bb1b3065f4ad32596795c3d1981b48dda` | 11 | 11 | 24 |
| 23 | `9dc1ed4784d929b405d00a3216865418f240a37c` | 20 | 20 | 25 + 45 (zaleznosc) |
| 24 | `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6` | 21 | — | 42, lokalne 2+1 |
| 25 | `7b772123870296af95d3ce951ccddb65685af7aa` | 14 | — | 42, lokalne 2+1 |
| 26 | `161d04d779ae86554f81c11bb24daa842c8dd363` | 9 | — | 42, lokalne 2+1 |

**Suma 26 rozdziałów: 325 proof.** Spośród nich **177/325** jest już objętych jednoznacznym **pełnym indywidualnym przeglądem wszystkich dowodów danego rozdziału na aktualnej wersji**: rozdziały 01–04 (**53**, raporty 46–47), rozdział 06 (**18**, raporty 40–41) oraz rozdziały 14–23 (**106**, raporty 15,16,18–25 i potwierdzenie bloba 21 w 41). Dla **pozostałych 148** raporty lokalne 2+1 oraz audyty selektywne nie są odrzucane ani nazywane „brakiem audytu”; wymagają natomiast ujednolicenia do wskazanego silniejszego standardu, zanim ogłosimy kompletny niezależny finalny reaudyt 325/325.

Niezależnie od poziomu dowodowej dokumentacji nadal istnieją **27 podpisane ilustracje / 28 środowisk tikzpicture**; audyt 38 wykrył i usunął dwie kolizje w 06 i 21, a artefakt PDF miał 188 stron. W tej iteracji nie pobierano nowego PDF ani nie wykonywano ponownego pełnorozdzielczego renderingu.

## Harmonogram dalszej kontroli bez zmiany kolejności rozdziałów

1. Rozdziały **05, 07–09**: 16+18+15+10 = **59** dowodów do pełnego jawnego przyporządkowania. Wcześniej sprawdzane trudne dowody (Urysohn, Tietze, Mysior, Tychonoff, Sorgenfrey) mogą stanowić punkt odniesienia, ale trzeba przyporządkować też pozostałe.
2. Rozdziały **10–13**: 14+8+14+9 = **45** dowodów. Istnieją audyty selektywne globalne 43–44 oraz stabilizacja naprawionego 13; należy uzupełnić niewymienione indywidualnie argumenty bez zmiany SHA.
3. Rozdziały **24–26**: 21+14+9 = **44** dowody. Mają zakończone lokalne 2+1 i dodatkowy audyt 17 trudnych dowodów w globalnym 42; do końca pozostają pozostałe 27 i wspólny rejestr wszystkich 44.
**Łącznie 59+45+44 = 148.** Na końcu: audyt zależności zewnętrznych w raportach 45 i 16–23, końcowy przegląd całego PDF i CI ostatniego commitu. Nie wyłączać aktywnej automatyzacji przed faktycznym uzasadnionym globalnym PASS.

## Walidacja i granice tej iteracji

Z repozytorium ponownie pobrano raporty 46–47 i źródła 01–04. Porównanie wszystkich etykiet dowodów w tych czterech aktualnych rozdziałach z etykietami raportów dało **53/53 dokładnych trafień**, bez duplikatów i brakujących pozycji. Osobno zweryfikowano **18/18 etykiet rozdziału 06** w raporcie 40 i zgodność z jego nowym blobem w raporcie 41. Wcześniejsze porównanie indywidualnych etykiet rozdziałów 14–23 z globalnymi raportami 15–25 dało **106/106** trafień. Jest to kontrola **istnienia jawnej dokumentacji**, nie automatyczna weryfikacja prawdziwości twierdzeń.

Ostatnie sprawdzone CI przed tym raportem: raporty 44 i 45 `completed/success`; po nowych raportach 46–47 uruchomiono workflow 45139309804 i 45139515178, które w momencie ostatniego odczytu miały status `in_progress`. Ostateczny wynik tych i przyszłego workflow po raporcie 48 trzeba odczytać osobno. Źródeł `.tex` nie edytowano.
