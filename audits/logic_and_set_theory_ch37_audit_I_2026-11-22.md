# Logika matematyczna i teoria mnogości — audyt I rozdziału 37

**Data:** 22 listopada 2026 r.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/logic_and_set_theory/37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex.
**Blob po poprawkach:** 3e0ae67b1b6a9abb5a4ff93691a2947d207647c4.
**Werdykt:** **NIECZYSTY** — ujawniono i poprawiono błędny odsyłacz oraz lukę w objaśnieniu zbiorolokalności ultraproduktu; poprawiono też regresję integracyjną w teście rozdziału 36. Licznik kolejnych czystych audytów: **0**.

## 1. Zakres

W rozdziale 37 omówiono definicje regularności, silnej graniczności i nieosiągalności, twierdzenie o modelu V_kappa, jego wniosek o względnej niesprzeczności, ultrafiltry zupełne, mierzalność i silną nieosiągalność, ultraprodukt klasowy, twierdzenie Łosia, jego dobre ufundowanie, zanurzenie elementarne oraz normalne miary i przecięcia diagonalne.

## 2. Poprawki obowiązkowe

1. **Etykieta rozdziału Gödla.** Pierwotny odsyłacz do ch:godel-second nie miał celu; poprawna istniejąca etykieta to ch:second-incompleteness. Poprawiono w commicie ec01a4d2d9de3bcdcaa4488501564a5a104e6d27.
2. **Zbiorolokalność ultraproduktu.** Argument ograniczający reprezentantów elementów poniżej klasy [f] wymaga uwzględnienia wartości domyślnej na indeksach poza zbiorem miary jeden. Zakres reprezentanta można ograniczyć do zbioru (suma wszystkich f(alpha)) wraz ze zbiorem pustym. Doprecyzowano to przed użyciem kolapsu Mostowskiego w tym samym commicie.
3. **Test rozdziału 36 blokował przyszłe rozdziały.** Pierwotna kontrola wymagała dokładnie 36 rozdziałów i umieszczenia ch36 na końcu książki. Po dodaniu ch37 daje to fałszywy błąd. Zmieniono na przynajmniej 36 rozdziałów i stały indeks 35, commit 8ca38137c59c0ecb4ec3dc9c3103a8ad7b7d51e0. Analogicznie zabezpieczono test ch37, commit 1b314a62c6596fd74ba7247b0f783fa37ceb77eb. Przebieg CI 45066664026 wykrył pierwotny błąd.

## 3. Niezależny przegląd matematyczny

**Etapy V_kappa.** Indukcja po randze daje |V_alpha|<kappa dla alpha<kappa. Aksjomaty ZFC w strukturze V_kappa, w tym potęgowanie i wybór, mają jawne uzasadnienia; do ograniczenia rang wartości funkcji z małej dziedziny kluczowa jest regularność kappa.

**Mierzalność.** κ-zupełny ultrafiltr niegłówny nie zawiera zbiorów mocy mniejszej od κ. Rozkład singularnego κ na mniej niż κ małych części przeczy zupełności, więc κ jest regularny. Ewentualna iniekcja κ→P(λ), λ<κ, po wybraniu przez ultrafiltr jednej odpowiedzi dla każdej współrzędnej ξ<λ dawałaby zbiór miary jeden zawierający co najwyżej jeden element. To dowodzi silnej graniczności.

**Twierdzenie Łosia.** Przy egzystencji wybiera się świadków tylko po zbiorze indeksów D⊆κ. Nie jest wymagany globalny wybór z klasy właściwej. Dobre ufundowanie ultraproduktu wynika z przeliczalnej zupełności i aksjomatu ufundowania w metateorii.

**Zanurzenie.** Dla α<κ każda funkcja do α jest na zbiorze miary jeden stała, stąd j(α)=α. Klasa funkcji identycznościowej leży ponad każdym j(α), α<κ, a poniżej j(κ), więc j(κ)>κ.

**Normalność.** Równoważność z diagonalnym przecięciem sprawdzono w obu kierunkach przez funkcję regresywną. Miara pochodna W={X⊆κ : κ∈j(X)} jest κ-zupełna i normalna.

Nie stwierdzono dodatkowego obowiązkowego rozszerzenia treści. Potencjalne tematy kardynałów Mahla i superzwartych zostawiamy jako propozycje, a nie niezatwierdzone uzupełnienia tego rozdziału.

## 4. Inwentarz i testy

Rozdział po poprawkach: **775 wierszy, 26 etykiet, 18 odsyłaczy, 7 definicji, 4 lematy, 7 twierdzeń, 1 wniosek, 5 uwag, 1 przykład, 12 dowodów.** Sparowanie środowisk LaTeX jest poprawne. Rozdział znajduje się w książce i katalogu na pozycji 37. Workflow oczekuje w całej książce 926 etykiet, 719 odsyłaczy i uruchamia osiem metod testowych ch37.

Podczas uruchomienia **[GitHub Actions 45066748548](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45066748548)** inwentarz oraz testy ch37 przeszły; nie deklaruje się sukcesu pełnego CI bez zakończenia kompilacji i kontroli wynikowego PDF.

## 5. Werdykt i następne kroki

Pierwszy audyt pozostaje nieczysty z powodu wyżej wymienionych poprawek. Audyt II ma ocenić z osobna wszystkie dowody na tym samym blobie, bez zbędnego rozszerzania zakresu. Po dwóch czystych audytach i jednym potwierdzającym możliwa jest stabilizacja. Testy skończonych przykładów nie są weryfikacją przez jądro Lean.
