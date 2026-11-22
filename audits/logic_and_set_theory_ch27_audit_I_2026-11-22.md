# Logika matematyczna i teoria mnogości — rozdział 27, audyt I

**Data:** 22 listopada 2026 r.  
**Plik:** \`chapters/pl/logic_and_set_theory/27-liczby-kardynalne-i-arytmetyka-mocy.tex\`

## Integracja materiału i zachowanie zakresu

Rozdział 27 oparto na pliku bibliotecznym \`27-cardinals-and-cardinal-arithmetic.tex\` oraz pełnej wersji książki \`logika_teoria_mnogosci_iteracja_79.pdf\` (strony PDF 221–227). Wersja PDF zawierała dodatkowy materiał niedostępny w skróconym TeX. Przywrócono:
- twierdzenie o potęgowaniu potęgi, z dowodem przez kurrowanie funkcji i rozważeniem pustych zbiorów;
- przykład zerowej podstawy i wykładnika, włącznie z konwencją \`0^0=1\`;
- przykład odwracania parowania Cantora i rysunek siatki \`N²\` z wyróżnioną przekątną \`m+n=3\`;
- pełne twierdzenie równoważności porównywalności wszystkich mocy z AC, z dowodem nieodwołującym się przedwcześnie do formalnej teorii ordynałów.

Zachowano wszystkie wcześniejsze definicje, uwagi, przykłady i konstrukcje bijekcji przedziałowych.

## Pierwszy audyt matematyczny

1. **Włączenie i nierówność dla zbiorów skończonych:** uzasadniono \`n≥1\` przy właściwym podzbiorze \`A⊊B\`.
2. **Cantor–Bernstein:** jawnie wskazano funkcję \`T(X)=g[f[X]]\` na \`P(A)\`, dzięki której rekursja na \`ω\` definiuje cały ciąg \`(A_n)\`. Rozpisano przejście od sumy zbiorów do \`C=A₀∪g[f[C]]\`, bez ukrytej przesłanki AC.
3. **Arytmetyka mocy:** cztery podstawowe bijekcje rozwinięto do postaci z określonymi dziedzinami, przeciwdziedzinami i sprawdzeniem obu kierunków. Prawo potęgowania potęgi również posiada obustronnie określony wzór.
4. **Porównywalność:** przy dowodzie AC z porównywalności użyto zbioru Hartogsa \`H(A)\` z rozdziału 26, który istnieje już w ZF, więc uniknięto błędnego koła i odwołania do jeszcze niewprowadzonej formalizacji ordynałów.
5. **Odsyłacze:** \`ch:ordinals\` jest świadomie niedokończonym odesłaniem do planowanego rozdziału 28. Workflow kontroluje go jako jedyny dopuszczalny forward reference; wszystkie pozostałe cele są rozwiązane.

## Walidacja

- Inwentarz w pierwszej integracji: 4 definicje, 11 twierdzeń, 2 wnioski, 5 przykładów, 6 uwag, 12 dowodów, 1 rysunek; 24 etykiety i 12 odsyłaczy.
- Nowe testy \`tools/tests/test_logic_and_set_theory_ch27.py\`: **PASS**.
- GitHub Actions [45006175561](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006175561): **SUCCESS**. Cały skrypt 212 stron, rozdział 27 zajmuje 8 ostatnich stron; PDF rozdziału wyrenderowano i przejrzano wizualnie, w tym diagram parowania. Brak przepełnień i niedozwolonych niezdefiniowanych odsyłaczy.

**Werdykt:** integracja pełnej treści zakończona, pozostają audyty stabilizacyjne rozdziału 27 bez rozszerzania zakresu.
