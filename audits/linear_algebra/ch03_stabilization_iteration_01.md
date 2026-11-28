# Algebra liniowa — rozdział 03: ponowny audyt stabilizacyjny I (czysty)

**Data:** 22 listopada 2026. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Źródło:** \`chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex\`, blob \`7ee828f8438e6030cb7f47685433aa3639220ab7\`.
**Wynik:** czysty przegląd źródła; nie wprowadzono zmian merytorycznych.

## Matematyka — kontrola wszystkich sekcji i 17 dowodów

1. **Definicje i podstawowe tożsamości.** Dowiedziono równoważności dwóch aksjomatów liniowości z zachowaniem kombinacji \`av+bw\`; poprawnie otrzymano \`T(0)=0\`, \`T(-v)=-T(v)\` i zachowywanie skończonych kombinacji, w tym pustej. Przykład \(T(x,y)=(x+y,x-y,2_Kx)\) jest poprawny także w charakterystyce 2.
2. **Przedłużenie z bazy Hamela.** Konstrukcja nie używa aksjomatu wyboru, kiedy baza jest już podana; dobre określenie odwzorowania wywodzi się z jednoznaczności współrzędnych, liniowość z dodawania rodzin o skończonym nośniku, zaś jednoznaczność z wartości na generatorach. Pusta baza i przestrzeń zerowa są obsłużone.
3. **Jądro i obraz.** Poprawne kryterium podprzestrzeni, równość \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\) wraz z obiema inkluzjami i \(A=\varnothing\), przeciwobrazy podprzestrzeni, jądro i iniektywność. Operator przesunięcia \(p\mapsto Xp\) i usuwania wyrazu stałego działają nad dowolnym ciałem.
4. **Wzór wymiarowy.** Oddzielono dowód w ZFC i wariant skończenie wymiarowy bez AC; niezależność obrazów \(T(D)\) wynika z niezależności rozszerzonej bazy \(C\sqcup D\) i zawarcia wektora w \(\ker T=\operatorname{span}(C)\). W przypadku kardynalnym nie dokonuje się niepoprawnego odejmowania nieskończonych liczb.
5. **Pierwsze twierdzenie o izomorfizmie.** Skontrolowano dobrą określoność odwzorowania \(V/\ker T\to\operatorname{im}T\), liniowość, jądro, surjekcję i diagram \(\widehat T=\widetilde T\circ\pi_{\ker T}\). Własność faktoryzacji przez \(V/U\) posiada poprawne założenie \(U\subseteq\ker T\).
6. **Składanie i izomorfizmy.** Weryfikowano oba zawierania dotyczące jądra i obrazu złożenia, liniowość odwrotności bijektywnego odwzorowania, zachowywanie bazy i kryterium równości wymiarów w skończonym wymiarze. Kontrprzykłady na \(K[X]\) uzasadniają konieczność skończoności.
7. **\(\operatorname{Hom}\) i \(\operatorname{End}\).** Rodzina \(E_{ji}\) jest niezależna i rozpina Hom, włącznie z \(m=0\), \(n=0\); rozdzielności i łączność składania sprawdzono na wektorach. Przykład nieprzemienności działa dla wszystkich ciał. Przypadek \(V=\{0\}\) opisany jawnie.
8. **Projekcje.** Obie implikacje \(P^2=P\iff(V=\operatorname{im}P\oplus\ker P\ \land\ P|_{\operatorname{im}P}=\operatorname{id})\), konstrukcja z dopełnienia oraz jej jednoznaczność są uzasadnione. Przykład \(P'(x,y)=(x-y,0)\) ma podane poprawne jądro i obraz.

## Kontrole formalne i przykłady

- Rozdział: 1019 wierszy, **17 twierdzeń/lematów/stwierdzeń/wniosków i 17 następujących po nich dowodów**, 8 środowisk przykładów, jeden diagram TikZ.
- Sprawdzono 19 odsyłaczy wewnątrz rozdziału, wszystkie rozwiązywalne względem etykiet rozdziałów 01–03; łącznie 150 różnych etykiet w tych rozdziałach, bez duplikatów.
- Kontrola zakazanej terminologii w polskiej treści (m.in. „unia”, „relacja liniowa”, „tensorowanie”, „injektywność”) nie ujawniła wystąpień.
- Istniejąca poprawna kompilacja książki obejmująca *identyczny blob źródłowy rozdziału 03* udostępnia 10-stronicowy rozdział. Wyrenderowano wszystkie strony, sprawdzono diagram faktoryzacji i brak pustych stron, tekstu poza stroną, \`Overfull\`, \`Underfull\`, brakujących glifów i niezdefiniowanych odsyłaczy.

## Regresje i CI

Dodano trwały test \`tools/test_linear_algebra_ch03.py\` oraz krok \`Verify linear maps, kernels, quotient factorization and projections\` w CI. Test wyczerpuje wszystkie 512 endomorfizmów \(\mathbb F_2^3\) i 81 endomorfizmów \(\mathbb F_3^2\), sprawdzając jądro, obraz, twierdzenie o wymiarze, faktoryzację przez podprzestrzeń, \(T(\operatorname{span}A)=\operatorname{span}(T(A))\) i charakterystykę projekcji. Łącznie 8678 konfiguracji faktoryzacji i 172544 przypadków równości przestrzeni rozpiętych. Nowy krok i cały CI dla commitu \`a9e217b42b8a2ce15deb4f5299730d3b04a414e9\` zakończyły się **SUCCESS** ([workflow 45005167546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45005167546)).

**Rezultat:** audyt I czysty, bez korekty źródła; do stabilizacji w bieżącym cyklu wymagana druga czysta kontrola na niezmienionym blobie.
