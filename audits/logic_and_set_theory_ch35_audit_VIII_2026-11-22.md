# Logika matematyczna i teoria mnogości — audyt VIII rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Blob wejściowy:** 89cdd6dcb3e77889b0b7ca67f0b8765f3940bdea.  
**Blob po audycie:** 0f39627cfedab7da6e6e8de8fccb035bcf511af7.  
**Werdykt:** audyt VIII **nie jest czysty**, ponieważ poprawiono błędne założenia samodzielnego lematu o algebrze regularnie otwartych zbiorów. Poprawiona wersja przeszła wszystkie testy i kompilację PDF. Licznik czystych audytów: **0**.

## 1. Zakres niezależnej kontroli

Ponownie przeanalizowano definicję niezerowej zupełnej algebry Boole'a, regularnie otwarte podzbiory przestrzeni topologicznej, regularne uzupełnienie pojęcia wymuszania, rekursję nazw i wartości atomowych, podstawianie równych nazw, mieszanie, pełność i boolowską poprawność ZFC. Sprawdzono argumenty dla aksjomatu zbioru potęgowego, zastępowania, ufundowania i wyboru.

Osobno skontrolowano iloraz nazw przez dowolny zewnętrzny ultrafiltr, jego lemat prawdy oraz możliwość interpretowania dowodu wewnątrz dowolnego modelu ZFC, bez założenia jego tranzytywności lub zewnętrznego dobrego ufundowania. Ponownie zweryfikowano kluczowe uzasadnienia z audytu VII: zachowanie omega_1 i omega_2 przez ccc, nazwy ciągów Cohena i ich rozróżnianie, rozstrzyganie podzbiorów omega przez przeliczalnie domknięte wymuszanie, zachowanie omega_1 oraz nazwę surjekcji omega_1 na 2^{aleph_0}.

Nie stwierdzono nowej luki w tych fragmentach, która wymagałaby zmiany dowodów. Audyt nie jest formalizacją w Lean: testy i kompilacja LaTeX nie zastępują sprawdzenia jądrem asystenta dowodzenia.

## 2. Błąd założeń w lemacie o zbiorach regularnie otwartych

W rozdziale niezerową algebrę Boole'a zdefiniowano jawnie przez warunek **0 != 1** (def:boolean35-algebra). Jednocześnie wcześniejsze sformułowanie lematu **lem:boolean35-ro-complete** mówiło, że RO(X) jest taką algebrą **dla każdej** przestrzeni topologicznej X. Było to fałszywe dla pustej przestrzeni: RO(empty) = {empty}, a zatem 0 = 1.

Poprawiono założenie na **„dla każdej niepustej przestrzeni topologicznej”** oraz dopisano w tekście jednozdaniowe wyjaśnienie konieczności tego ograniczenia i odsyłacz do definicji algebry. Późniejsze zastosowania do RO(P) pozostają poprawne, ponieważ pojęcia wymuszania w tym rozdziale są z założenia niepuste.

**Commity:**
- 4176d0ee94f27fe63d5636fcca831cb79db3ef7 — doprecyzowanie niepustości przestrzeni;
- f292c9e4267a25a3d1171edc3ef9eae51f2e7442 — uzasadnienie przypadku brzegowego.

## 3. Regresja i kontrola struktury

Dodano metodę **test_regular_open_algebra_excludes_empty_space**, sprawdzającą zgodność hipotezy lematu z definicją niezerowej algebry i przypadki przestrzeni pustej oraz jednopunktowej.

Rozszerzono **test_ro_completion_for_every_small_preorder** o wszystkie preordery na jednym elemencie. Regresja obejmuje teraz wszystkie preordery na 1, 2, 3 i 4 oznaczonych punktach, odpowiednio **1, 4, 29 i 355**, razem **389** struktur. Kontrolowane są m.in. dopełnienie w RO(P), skończone kresy, gęstość obrazów warunków i zgodność wzmocnień. Wszystkie testy przeszły.

**Liczba metod testowych rozdziału 35: 21.** Test i rozszerzenie preordera zapisano w commicie **3381d8d006d659d6e41e92e15bffc246cb17448b**.

Nowe wyjaśnienie w rozdziale wprowadziło jeden dodatkowy odsyłacz. Zaktualizowano licznik rozdziału z 32 na **33** (commit 2f5c78258bfc22565bce0c2f72916d9a4347938f), a całej książki z 672 na **673** (commit 5715900b786717c63bb3c384b08f792c72a722cf). W aktualnym źródle jest **28 różnych etykiet**, 33 odsyłacze, 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład i 14 dowodów; brak rozbieżności parowania środowisk.

## 4. CI i kontrola rzeczywistego PDF

**GitHub Actions [45054230101](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45054230101): SUCCESS**, commit 5715900b786717c63bb3c384b08f792c72a722cf, obejmujący wszystkie poprawki audytu VIII. Powiodły się testy rozdziałów 01–35, kontrola inwentarza, kompilacja LaTeX oraz kontrola PDF i logu. Pobrano rzeczywisty artefakt przebiegu, nie założono poprawności na podstawie starszego PDF.

PDF książki ma **311 stron**, format A4. Rozdział 35 rozpoczyna się na stronie PDF **296** i kończy na **311**, zajmując **16 stron**. Wyrenderowano wszystkie strony rozdziału i sprawdzono zbiorczy montaż, a stronę PDF 296 z poprawionym lematem obejrzano dodatkowo w pełnej rozdzielczości. Nie zauważono nakładania elementów ani uciętych wzorów. W logu brak błędów LaTeX, wierszy overfull i nierozwiązanych odsyłaczy; występuje jedno ostrzeżenie underfull hbox w książce oraz ostrzeżenia hyperref dotyczące tokenów w PDF strings, bez obserwowanego wpływu na układ nowej poprawki.

## 5. Status i kolejna iteracja

Ponieważ audyt VIII usunął rzeczywisty błąd w sformułowaniu lematu, **licznik niezależnych czystych audytów pozostaje równy 0**. Następny etap to **audyt IX** na niezmienionym blobie źródła **0f39627cfedab7da6e6e8de8fccb035bcf511af7**, z ponowną niezależną kontrolą założeń, granicznych przypadków definicji, całej argumentacji o CH i negacji CH, redakcji, odsyłaczy oraz CI. Dopiero po stabilizacji należy wykonać dodatkowy audyt potwierdzający.
