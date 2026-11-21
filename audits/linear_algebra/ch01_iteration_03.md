# Algebra liniowa — rozdział 01: audyt 3

Data: 2026-11-21  
Gałąź: \`biblioteka-matematyczna-iteracja-6\`  
Rozdział: \`chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex\`  
Commit treści po poprawkach: \`e18b5393dbded59638730d66685ec60556cef661\`

## Metoda

Ponownie sprawdzono wszystkie definicje, założenia i główne dowody: kryterium podprzestrzeni, wzory na przestrzenie rozpięte, definicję niezależności indeksowanej, kryteria dołączania wektora, lemat Steinitza, uzupełnianie do bazy, wymiar podprzestrzeni, współrzędne, własności baz Hamela i dowód przez lemat Zorna. Skontrolowano przypadki \(V=\{0\}\), rodziny puste i działania nad ciałami o dodatniej charakterystyce.

Dodatkowo porównano wyrenderowany PDF z tekstem źródłowym, przeanalizowano log kompilacji, sprawdzono ilustracje i zweryfikowano odsyłacze.

## Usterki znalezione i naprawione

1. **Dowód lematu o wymianie Steinitza: zakres indukcji.** Wcześniejszy zapis mówił o konstrukcji dla \(0\le k\le r\), mimo że przed wykazaniem \(r\le m\) liczba \(m-k\) mogła być ujemna. Poprawiono zakres na \(0\le k\le\min\{m,r\}\), a następnie formalnie wyprowadzono sprzeczność w przypadku \(r>m\).
2. **Uzupełnianie rodziny do bazy.** Usunięto mylące odwołanie do niejawnej konwencji dołączania „pod nowym indeksem”. Teraz dowód wyjaśnia, dlaczego dodawany wektor nie może być już obecny w rodzinie i stosuje jawnie poprawne kryterium niezależności.
3. **Przykład nad \(\mathbb F_2\).** Zdanie, że każde dwa różne wektory niezerowe w \(\mathbb F_2^2\) są niezależne, uzupełniono pełnym sprawdzeniem możliwych współczynników \(\alpha,\beta\in\mathbb F_2\).
4. **Wielomian zerowy i stopień.** Skorygowano definicję \(K[X]_{\le d}\): stopień stosujemy tylko do wielomianów niezerowych. Uporządkowano też definicję maksimum stopni przy dowodzie nieskończonego wymiaru \(K[X]\).
5. **Rysunek niezależności liniowej.** Dodano diagram dwóch niezależnych wektorów i zależnej trójki z relacją \(w=e_1+e_2\), wraz z podpisem i etykietą. Kod TikZ znajduje się w samym rozdziale, bez zewnętrznego pliku.
6. **Przepełniony wiersz w podsumowaniu.** Usunięto formułę powodującą \`Overfull \hbox (46.26607pt)\`; zastąpiono ją krótkim, precyzyjnym opisem równoważności charakteryzujących bazę.

## Wynik po poprawkach

- Środowiska LaTeX: zrównoważone.
- Etykiety: **58**, bez powtórzeń wewnątrz rozdziału.
- Odsyłacze \`ref\`/\`eqref\`: wszystkie cele lokalne istnieją.
- Rysunki: **2**, oba osadzone w TikZ; sprawdzone wizualnie w PDF.
- Pełna książka \`books/pl/linear_algebra.tex\`: **12 stron** w aktualnej kompilacji.
- CI: **sukces**, run [44890678314](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44890678314), commit \`e18b5393dbde\`. Test importu, katalogu, etykiet i odsyłaczy przeszedł; pełna kompilacja LaTeX i weryfikacja PDF również przeszły.
- Log LaTeX z powyższego runu: nie zawiera wpisów \`Overfull\`, \`Underfull\`, \`LaTeX Warning\` ani \`undefined references\`.
- Kontrola wizualna: na stronie 7 nowy rysunek nie wykazuje kolizji napisów; pierwotny rysunek podprzestrzeni również został sprawdzony.
- Zależności globalne Biblioteki: nadal istnieją wcześniejsze niezwiązane z nowym rozdziałem niezgodności kopii źródłowych i importów; ich raportowanie w CI jest oddzielone od kontroli tego rozdziału. Nie deklarujemy, że zostały naprawione.

## Status cyklu

**Audyt 3 zakończony z poprawkami. Rozdział 01 pozostaje otwarty.**

Następna iteracja: **audyt 4 tego samego rozdziału**, dopiero po audycie bez nowych braków rozważyć zamknięcie. Nie tworzyć jeszcze rozdziału 02.
