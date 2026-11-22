# Logika matematyczna i teoria mnogości — audyt IV rozdziału 38 (potwierdzający)

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/38-kardynaly-mahla-i-slaba-zwartosc.tex.  
**Blob źródła:** d0d176bf1d4cbb8426cedcf02fbbd3a28510a152 — identyczny z audytami I–III.  
**Werdykt końcowy: ROZDZIAŁ 38 STABILNY (2/2+1).** Audyty II, III i IV są czyste, bez żadnej zmiany źródła. Wszystkie trzy pełne przebiegi CI zakończyły się sukcesem, a strony PDF zostały porównane.

## 1. Próby znalezienia kontrprzykładu do twierdzeń

**Zbiór nieograniczony, lecz niestacjonarny.** Rozważono następniki poniżej ω_1. Są nieograniczone, lecz rozłączne z klubem niezerowych ordynałów granicznych. Definicja liczby kardynalnej Mahla nie utożsamia więc nieograniczoności z warunkiem stacjonarności; przykład w rozdziale stanowi odpowiedni test pojęć.

**Przecięcie klubu z samym sobą i z <κ wieloma klubami.** W lemacie o przecięciach nie użyto fałszywego twierdzenia, że przecięcie κ dowolnych klubów pozostaje klubowe. Zamiast tego przy rodzinie rozmiaru μ<κ rekurencja długości ω daje wspólny punkt, zaś dla rodziny rozmiaru κ stosuje się *przecięcie diagonalne* z warunkiem ξ<α. Rozdzielono te dwa rodzaje przecięć, co usuwa częsty błąd kwantyfikacji.

**Drzewo mające gałąź.** Pełne drzewo funkcji binarnych długości <κ ma na każdym poziomie α liczbę 2^{|α|} węzłów, która jest mniejsza od κ wyłącznie z silnej graniczności. Stała gałąź zerowa istnieje, ale nie przesądza własności *wszystkich* drzew κ-owych. W definicji słabej zwartości występuje również nieosiągalność, więc samej własności drzewa przy następnikowym kardynale nie nazwano słabą zwartością.

**Ultrafiltr nienormalny.** Przecięcie mniej niż κ dużych zbiorów i dowód relacji podziałowej używają tylko κ-zupełności i ultrafiltrowości. Z kolei lemat, że każdy klub należy do konkretnej miary, wyraźnie wymaga normalności. Rozdział nie przenosi własności normalnych na arbitralne miary.

**Wewnętrzna kardynalność.** W dowodzie mierzalny ⇒ Mahlo można się obawiać, że P^M(λ) ma mniejszą liczbę elementów niż P^V(λ). To jednak działa w korzystnym kierunku: hipotetyczna iniekcja κ→P^M(λ) byłaby nadal iniekcją do P^V(λ). Weryfikowano również regularność κ w M i brak wewnętrznego świadka niekardynalności. Wszystkie argumenty wykorzystują tranzytywność M i fakt M⊆V.

**Długość rekursji dla jednorodnego zbioru.** W każdym kroku ξ<κ liczba wcześniej wybranych indeksów jest mniejsza niż κ; przecięcie danej liczby dużych zbiorów pozostaje duże. Nie przecina się na raz wszystkich κ wielu zbiorów, co nie wynikałoby z κ-zupełności. Indukcyjny wybór najmniejszego możliwego α_ξ daje rosnący ciąg długości κ.

## 2. Precyzja założeń i redakcja

W każdym twierdzeniu wskazano klasę κ i dodatkowe założenia dotyczące mierzalności. Dla funkcji regresywnej wyłączono α=0, co jest niezbędne. W przykładzie ω_1 każda przeliczalna liczba porządkowa ma ponad sobą większą graniczną liczbę porządkową <ω_1. Lemat Fodora zachowuje niezmienioną treść w rozdziale; nie zakłada bezpodstawnie przecięcia wszystkich zbiorów stacjonarnych.

Inwentarz źródła: 641 wierszy, 26 unikalnych etykiet, 19 odsyłaczy, 8 definicji, 4 lematy, 5 twierdzeń, 1 wniosek, 5 uwag, 2 przykłady i 10 środowisk dowodu. Nazwy etykiet są stabilne i brak nowych koniecznych poprawek językowych. Rozdział 38 znajduje się w katalogu i pliku głównym. Rozszerzenie charakterystyk słabej zwartości, np. przez logikę infinitarną, jest propozycją dalszej pracy, a nie niezbędną poprawką.

## 3. Pełne przebiegi CI

- **[CI audytu II — 45068920801, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068920801)**.
- **[CI audytu III — 45069037941, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069037941)**.
- **[CI audytu IV — 45069081544, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069081544)**, commit eeed401b8e06d84b69c83c9acbd47a749757fee4, rzeczywisty artefakt 14772781488.

W pobranym artefakcie końcowym książka ma **331 stron A4**. Rozdział 38 znajduje się na stronach PDF **327–331**. Obejrzenie wszystkich pięciu stron nie wykazało obciętych równań ani kolizji tekstu. Po wyrenderowaniu w 72 dpi porównano je piksel po pikselu z niezależnym artefaktem przebiegu 45068706353: **5/5 stron identycznych pikselowo i tekstowo**.

Kontrola logu końcowego: **0** błędów LaTeX, **0** overfull, **0** undefined references, **0** missing characters, **1** ostrzeżenie underfull w całym skrypcie bez widocznego defektu. Wszystkie 9 testów rozdziału 38 przeszło w pełnym CI. Etykiety i odsyłacze pozostają zachowane.

## 4. Werdykt końcowy

**Audyt I — nieczysty technicznie (poprawiono nieprawidłową asercję testu). Audyt II — czysty (1/2). Audyt III — czysty (2/2). Audyt IV — czysty (+1 potwierdzający). ROZDZIAŁ 38: STABILNY.** W całej sekwencji audytów źródło rozdziału pozostało tym samym blobem **d0d176bf1d4cbb8426cedcf02fbbd3a28510a152**. Nie wprowadzono niezatwierdzonych rozszerzeń. Wyniki testów i kompilacji LaTeX nie oznaczają formalnego dowodu w Lean.
